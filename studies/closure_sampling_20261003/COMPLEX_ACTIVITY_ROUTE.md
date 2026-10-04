# A complex activity strip for one training input

2026-10-03. Scoped theoretical route for the exact finite Gaussian dense
network, not a modified model. **Internal proof candidate:** for one training
input and a sufficiently short fixed activity interval, the actual dense flow
has a holomorphic continuation of radius proportional to
\(1/\sqrt{\log(n/\varepsilon)}\), with bounded activation coordinates and
\(O(\sqrt{\log(n/\varepsilon)})\) carrier coordinates. This note gives the
complete argument for independent checking; it is not a promotion review.

The assigned activity equations and the manuscript setting were used directly.
The authorized `Q_ORDER_POSITIVE_ROUTE.md` and its complete local insertion
check were read for comparison. No probability theorem from that route is
imported: the one-input change of variables below permits deterministic
deletion bounds, and the Gaussian argument is proved here. No experiments,
other concurrent route files, manuscript changes, or Git operations were used.
The canonical-notation skill and neural reference, rigorous-proof skill, and
conjecture/adversarial-audit instructions were applied.

## 1. Statement and exact change of variables

For the single input \(x=\sqrt d\,e_1\), write \(a=Ae_1\in\mathbb R^n\).
The dense second-layer matrix is \(W\in\mathbb R^{n\times n}\), the readout
is \(w\in\mathbb R^n\), and
\[
 h=\tanh a,\qquad z=Wh,\qquad g=\tanh z,\qquad
 \delta=w\odot\operatorname{sech}^2z,\qquad k=W^\top\delta,
 \qquad f=\frac1n w^\top g.
\]
The squared loss is \((f-y)^2\). In activity time, defined along physical
training by \(ds/dt=2(y-f)\), the exact equations are
\[
 a'=\operatorname{sech}^2a\odot k,\qquad
 W'=\delta h^\top/n,\qquad w'=g.                       \tag{1}
\]
Primes in this note always mean activity derivatives. Initially the entries
of \(W_0\) are independent \(N(0,1/n)\), independent of \(a_0\), and
\(w_0=0\). The continuation theorem holds conditional on every real
\(a_0\); its final coordinate bound also uses the canonical Gaussian law
of \(a_0\).

There exist constants \(T_0,c,C>0\), independent of width and confidence,
such that the following holds. Fix \(0<T\le T_0\) and
\(0<\varepsilon<1/2\). For all sufficiently large widths (the threshold
may depend on \(T,\varepsilon\)), put
\[
 \ell_n=\log(en/\varepsilon),\qquad r_n=c/\sqrt{\ell_n}.
                                                               \tag{2}
\]
With probability at least \(1-\varepsilon\), (1) extends holomorphically
to a neighborhood of the closed rectangle
\[
 D_n=\{s\in\mathbb C:-r_n\le\Re s\le T+r_n,
                           \ |\Im s|\le r_n\}.                 \tag{3}
\]
On this rectangle,
\[
 \|h\|_\infty+\|g\|_\infty
 +\|\operatorname{sech}^2a\|_\infty
 +\|\operatorname{sech}^2z\|_\infty\le C,
 \qquad \|w\|_\infty+\|\delta\|_\infty\le CT,
                                                               \tag{4}
\]
\[
 \|k\|_\infty+\|z'\|_\infty\le CT\sqrt{\ell_n},
 \qquad \|W\|_{\rm op}\le C.                                  \tag{5}
\]
For canonical Gaussian \(a_0\), the same probability statement can include
\[
 \|a\|_\infty+\|z\|_\infty\le C\sqrt{\ell_n}.                  \tag{6}
\]
All transposes in the holomorphic extension are algebraic transposes, with no
complex conjugation. Norms used in estimates are ordinary complex Euclidean,
Frobenius, and operator norms.

The exact simplification is
\[
 F(\alpha)=\frac\alpha2+\frac{\sinh(2\alpha)}4,
 \qquad u_i=F(a_i),\qquad \sigma(u)=\tanh(F^{-1}(u)),\qquad
 H=\sqrt n\,W.                                                \tag{7}
\]
Thus \(F'(\alpha)=\cosh^2\alpha\), and (1) becomes exactly
\[
 h=\sigma(u),\quad z=Hh/\sqrt n,\quad
 \delta=w\odot\operatorname{sech}^2z,
 \qquad
 u'=W^\top\delta,\quad H'=\delta h^\top/\sqrt n,
 \quad w'=\tanh z.                                            \tag{8}
\]
The first-layer carrier no longer occurs as a diagonal multiplier in the
Jacobian of the activity vector field. This property uses the single-input
equation and is not asserted for general finite datasets.

## 2. The inverse in (7) has a fixed strip of analyticity

On \(|\Im\alpha|<\pi/4\),
\[
 \Re F'(\alpha)=\frac{1+\cosh(2\Re\alpha)
                                     \cos(2\Im\alpha)}2\ge\frac12.
\]
For two points in that convex strip, integration on the line segment shows
that \((F(\alpha)-F(\beta))/(\alpha-\beta)\) has positive real part.
Consequently \(F\) is injective and has a holomorphic inverse on its image.
Writing \(\alpha=x+iv\),
\[
 \Re F(\alpha)=x/2+\sinh(2x)\cos(2v)/4,
 \qquad
 \Im F(\alpha)=v/2+\cosh(2x)\sin(2v)/4.                       \tag{9}
\]
The first expression has the sign of \(x\) and modulus at least
\(|x|/2\). At \(v=\pm\pi/4\), the second has modulus at least
\(\pi/8+1/4>1/4\). These facts imply that the image contains
\(|\Im u|<1/4\): continue the local inverse vertically from the unique
real inverse; a finite target in this strip cannot send \(|x|\) to infinity,
reach the two horizontal boundary lines, or meet a zero of \(F'\).

On this inverse branch, \(|\Im a|<\pi/4\), so
\(|\tanh a|\le1\) and \(|\operatorname{sech}^2a|\le2\).
In particular \(\sigma\) is bounded on \(|\Im u|<1/4\).
Cauchy's formula on fixed-radius disks gives uniform bounds for every fixed
number of derivatives of \(\sigma\) on any strictly smaller strip. Also
\[
 (F^{-1})'(u)=\operatorname{sech}^2(F^{-1}(u)),\qquad
 \sigma'(u)=\operatorname{sech}^4(F^{-1}(u)).                    \tag{10}
\]
Fix henceforth a small absolute \(b>0\), for example \(b=1/64\).
The functions \(\sigma,\sigma',\sigma''\) and the first three derivatives
of tanh have uniform bounds on the strips \(|\Im u|\le2b\) and
\(|\Im z|\le2b\), respectively. Finite differences of these functions
are bounded by a constant times the difference of their arguments, because
these strips are convex and their first derivatives are bounded.

## 3. Width-independent deterministic estimates

All statements in this section hold for the full network and for rectangular
networks obtained by deleting one first-layer or one second-layer neuron.
Every normalization remains \(n\). Suppose the initialized operator norm is
at most a fixed constant \(K\), and a solution is holomorphic in a scaled
rectangle \(\lambda D_n\), \(0<\lambda\le1\), with
\[
 \max_i|\Im u_i|\le2b,\qquad \max_j|\Im z_j|\le2b.             \tag{11}
\]
Take widths large enough that \(r_n\le T/4\). Every segment from zero to
a point of \(D_n\) then has length at most \(2T\). Integration of (8)
along that segment gives
\[
 \|w\|_\infty\le CT,
 \quad \|\delta\|_\infty\le CT,
 \quad \|W-W_0\|_{\rm op}\le CT^2,
 \quad \|W\|_{\rm op}\le K+CT^2.                             \tag{12}
\]
The corresponding normalized vector bounds are
\[
 \frac{\|k\|_2+\|h'\|_2+\|z'\|_2}{\sqrt n}\le CT,
 \qquad
 \frac{\|\delta'\|_2+\|k'\|_2}{\sqrt n}\le C.                \tag{13}
\]
Indeed, \(h'=\sigma'(u)\odot k\),
\(z'=W'h+Wh'\),
\(\delta'=\operatorname{sech}^2z\odot w'
      +(w\odot\tanh''z)\odot z'\), and
\(k'=W'^\top\delta+W^\top\delta'\); substituting (12) gives (13).
If also \(\|k\|_\infty\le M_c\), then
\[
 \frac{\|h''\|_2}{\sqrt n}
 \le C(1+TM_c),\qquad
 h''=\sigma''(u)\odot k^{\odot2}+\sigma'(u)\odot k'.           \tag{14}
\]

Here is the finite-difference bound that replaces the much more delicate
linearization in the general-data cavity argument. Compare two retained
states \(\Theta=(u,H,w)\) and \(\Theta^c=(u^c,H^c,w^c)\), both satisfying
(11)--(12), and define
\[
 D=\|u-u^c\|_2+\|H-H^c\|_F+\|w-w^c\|_2.
\]
If the first state has an additional external input \(e\) in its top
preactivation, then the finite differences satisfy
\[
 \|h-h^c\|_2\le CD,
 \qquad \|z-z^c\|_2\le C D+\|e\|_2,
 \qquad \|\delta-\delta^c\|_2\le C D+CT\|e\|_2.              \tag{15}
\]
The factor \(\sqrt n\) in \(H\) is essential:
\(\|(H-H^c)h^c/\sqrt n\|_2\le C\|H-H^c\|_F\).
Substitution in (8), including the normalized outer product in \(H'\),
then bounds the sum of the velocity differences by
\[
 C D+C\|e\|_2+\|q\|_2,                                     \tag{16}
\]
where \(q\) is an additional source in the \(u'\) equation, if present.
The constant is independent of the carrier maximum. The calculation uses
finite differences of the actual endpoint preactivations; it does not assume
that the straight segment in parameter space remains pole-safe.
Gronwall along each complex radial segment therefore applies to (16).

## 4. Deterministic singleton deletion comparisons

The next comparisons are valid on every common scaled rectangle where the
full and cavity solutions satisfy their respective pole bounds. They require
only the initialized deleted row/column norm to be at most \(K\).

**Delete first-layer neuron \(i\).** Its initialized outgoing column is
\(x_i=W_{0,:,i}\). The autonomous cavity retains \(u_{-i},H_{:,-i},w\),
starts from the same retained initialization, and is independent of \(x_i\).
The retained full network has the external top-preactivation input
\[
 e(s)=W_{:,i}(s)h_i(s)
     =x_i h_i(s)+(W_{:,i}(s)-x_i)h_i(s).                       \tag{17}
\]
From (8) and (12),
\[
 \|W_{:,i}-x_i\|_2\le CT^2/\sqrt n,
 \qquad \|e\|_2\le C,
 \qquad \|e\|_\infty\le C\|x_i\|_\infty+CT^2/n.             \tag{18}
\]
Equations (15)--(16), with zero initial difference and \(q=0\), imply
\[
 D_i\le CT,\qquad
 \|\delta-\delta^{-i}\|_2\le CT,
 \|k_{-i}-k^{-i}\|_2\le CT.                                \tag{19}
\]
The last bound follows from
\((W_{:,-i}-W^{-i})^\top\delta
 +(W^{-i})^\top(\delta-\delta^{-i})\), retaining
\(W_{:,-i}-W^{-i}=(H_{:,-i}-H^{-i})/\sqrt n\).
The deleted coordinate itself obeys
\[
 \left|k_i-x_i^\top\delta^{-i}\right|
 \le \|x_i\|_2\|\delta-\delta^{-i}\|_2
       +\|W_{:,i}-x_i\|_2\|\delta\|_2
 \le CT.                                                    \tag{20}
\]
No Gaussian law is being asserted for the actual adaptive carrier.
The only Gaussian quantity is the independent cavity pairing.
For transferring pole bounds we also have
\[
 \|u_{-i}-u^{-i}\|_\infty\le CT,
 \|z-z^{-i}\|_\infty\le CT+C\|x_i\|_\infty+CT^2/n.           \tag{21}
\]

**Delete second-layer neuron \(j\).** Write its initialized row as
\(x_j^\top=W_{0,j,:}\). The autonomous cavity retains
\(u,H_{-j,:},w_{-j}\), starts from the same retained initialization, and is
independent of \(x_j\). The additional source in the retained full
\(u'\) equation is
\[
 q(s)=W_{j,:}(s)^\top\delta_j(s).
\]
It has norm at most \(CT\), since
\(\|W_{j,:}-x_j^\top\|_2\le CT^2/\sqrt n\).
Now (16), with \(e=0\), gives
\[
 D_j\le CT^2,
 \|z_{-j}-z^{-j}\|_2\le CT^2,
 \|k-k^{-j}\|_2\le CT.                                     \tag{22}
\]
The last estimate includes the deleted row's contribution \(q\).
If the row cavity has \(\|k^{-j}\|_\infty\le M_c\), then
\[
 \|h'-(h^{-j})'\|_2
 \le C\|k-k^{-j}\|_2
       +C\|(u-u^{-j})\odot k^{-j}\|_2
 \le C(T+T^2M_c).                                          \tag{23}
\]
Finally,
\[
 z'_j=\delta_j h^\top h/n+x_j^\top h'
                  +(W_{j,:}-x_j^\top)h',
\]
so (12)--(13) and (23) give
\[
 \left|z'_j-x_j^\top(h^{-j})'\right|
 \le C(T+T^2M_c).                                          \tag{24}
\]
This is the forward derivative estimate needed to avoid complex tanh poles.
A real lower-carrier maximum alone would not imply it.

## 5. Stopping domains and transfer to all singleton cavities

Fix a large absolute constant \(A\), to be chosen after the Gaussian estimate,
and set
\[
 M=A T\sqrt{\ell_n},\qquad L=A T\sqrt{\ell_n}.                \tag{25}
\]
The full solution is stopped at the first scale \(\lambda\in(0,1]\) at
which its holomorphic continuation on \(\lambda D_n\) reaches any of
\[
 \max|\Im u|=b,\quad \max|\Im z|=b,
 \quad\max|k|=M,\quad\max|z'|=L.                            \tag{26}
\]
Each singleton cavity has its own stop, using pole caps \(2b,2b\) and
carrier cap \(2M\), with **no forward-derivative cap**. All maxima are
over the corresponding closed scaled rectangle and all relevant coordinates.
These are auxiliary proof stops, not changes to the differential equations.

Initial readout zero gives \(k(0)=z'(0)=0\), and initial \(u,z\) are real,
so the stopped continuations start on a nonempty neighborhood. Ordinary
holomorphic Picard iteration supplies local existence and uniqueness because
the vector field is holomorphic away from the fixed gate boundaries.
Before the displayed caps are reached, (12) and integration of \(u'=k\)
bound all finite-dimensional state coordinates. Hence a solution cannot
terminate first by escape to infinity; the local solutions patch uniquely
across the simply connected scaled rectangles. The same argument applies
to every cavity.

Work on the initialization event
\[
 \|W_0\|_{\rm op}\le K,
 \qquad \max_{i,j}|W_{0,ji}|\le C\sqrt{\ell_n/n}.              \tag{27}
\]
Choose \(T_0\) small enough that the \(CT\) bounds in (21)--(22) are
less than \(b/4\). For sufficiently large widths, their additional entry
terms are also less than \(b/4\). On every common prefix with the full
solution, (19), (21), and (22) imply strictly
\[
 \max|\Im u^c|<2b,\qquad \max|\Im z^c|<2b,
 \qquad\max|k^c|\le M+CT<2M.                                \tag{28}
\]
Consequently no singleton cavity can stop before the full solution. The
comparison is first applied only on the common prefix, and the strict
margins then continue the cavity through the full stop. It never presumes
that survival while establishing the comparison. Only singleton cavities
are used; there is no iterated deletion hierarchy.

## 6. Conditional Gaussian suprema on the stopped cavity domains

Condition on \(a_0\) and on the entire initialization retained by one
cavity. If its initialized operator norm exceeds \(K\), define the reference
curve to be zero. Otherwise the cavity and its own stop scale \(\lambda_c\)
are deterministic under this conditioning, while the omitted vector has
law \(N(0,I_n/n)\).

For a column cavity use \(v(s)=\delta^{-i}(s)\). For a row cavity use
\(v(s)=(h^{-j})'(s)\). Equations (12)--(14) give on its whole stopped
domain
\[
 \sup_s\|v(s)\|_2/\sqrt n\le CT,
 \qquad \sup_s\|v'(s)\|_2/\sqrt n\le C(1+2TM).               \tag{29}
\]
For any fixed complex vector \(v\) obeying the first bound,
\[
 \Pr\{|x^\top v|>t\mid\text{retained initialization}\}
       \le4\exp\{-c t^2/T^2\},                             \tag{30}
\]
by applying the real Gaussian tail separately to the real and imaginary
parts.

Here are sufficient elementary details for uniformity. Parameterize the
stopped domain as \(s=\lambda_c q\), \(q\in D_n\). Use a rectangular
grid in \(q\) of mesh at most
\[
 \eta_n=T n^{-3}/(1+2TM).
\]
The number of grid points is at most
\(C n^6(1+2TM)^2\). By (29), interpolation changes \(x^\top v\)
by at most \(CT n^{-5/2}\) whenever \(\|x\|_2\le K\).
The grid, stop, and its reference values depend only on retained
initialization, so (30) applies to every grid point with no conditioning on
the full stopping event. Its cardinality is at most
\(C_A n^6(1+\ell_n)\), because \(T\le T_0\).

Taking the threshold to be \(C_G T\sqrt{\ell_n}\), where \(C_G\) is
a sufficiently large fixed constant, and unioning (30) over every grid and
the \(2n\) singleton cavities yields an event of probability at least
\(1-\varepsilon/4\) on which
\[
 \sup_{s\in\lambda_{-i}D_n}
          |x_i^\top\delta^{-i}(s)|\le C_G T\sqrt{\ell_n},
 \qquad
 \sup_{s\in\lambda_{-j}D_n}
          |x_j^\top(h^{-j})'(s)|\le C_G T\sqrt{\ell_n},        \tag{31}
\]
simultaneously, whenever the relevant row/column norm is at most \(K\).
The logarithm of the total cardinality is \(O(\ell_n)\), including
arbitrarily small fixed confidence. An increase in the fixed threshold
constant absorbs the fixed \(A\)-dependent factor in the cardinality.
Equivalently, choose fixed constants in the order: a provisional sufficiently
large Gaussian threshold, \(A\) larger than its required multiple, and
then a sufficiently large width threshold to absorb the fixed grid factor.

The initialization event (27) has failure at most \(\varepsilon/4\) for
sufficiently large widths. For completeness, a pair of \(1/4\)-nets of
the real unit sphere has at most \(9^{2n}\) pairs. Applying the Gaussian
tail to each bilinear form bounds
\(\Pr\{\|W_0\|_{\rm op}>K\}\le2e^{-c_Kn}\) for a sufficiently
large fixed \(K\). Individual entry tails and a union over \(n^2\)
entries give the second part of (27). The operator event also bounds every
deleted row and column norm by \(K\).

## 7. Closing the full caps

By (28), every reference in (31) exists throughout the full stopped domain.
The deterministic reinsertion bounds (20) and (24), with \(M_c=2M\), give
\[
 \sup|k|\le C_G T\sqrt{\ell_n}+CT,
 \qquad
 \sup|z'|\le C_G T\sqrt{\ell_n}+CT+CT^2M.                    \tag{32}
\]
Choose \(A\) large enough, and then reduce \(T_0\) if necessary, so that
the right sides are at most \(M/2\) and \(L/2\), respectively. In the
second inequality the feedback-to-cap ratio is \(CT^2\); this is exactly
where short fixed activity is used.

To close the pole caps, take any \(s=u+iv\) in the full stopped rectangle.
The vertical segment from real \(u\) to \(s\) lies in that rectangle.
The actual flow is real on its real interval. Therefore
\[
 |\Im u_i(s)|\le |v|\sup|k_i|\le r_n M/2,
 \qquad |\Im z_j(s)|\le |v|\sup|z'_j|\le r_n L/2.             \tag{33}
\]
Choose \(c\) in (2) sufficiently small that
\(c A T_0/2<b/2\). Both bounds in (33) are then strictly below
\(b/2\). All four full caps have strict margins. The analytic continuation
argument in Section 5 extends the full solution beyond any alleged stop
scale below one and, at scale one, to a neighborhood of the closed rectangle.
This proves (2)--(5).

For (6), conditional on \(a_0\), each initial top preactivation is Gaussian
with variance \(\|\tanh a_0\|_2^2/n\le1\). Gaussian tails give
\(\|z_0\|_\infty\le C\sqrt{\ell_n}\); the canonical first-layer law
gives the same bound for \(\|a_0\|_\infty\). Their combined failure can
be allotted another \(\varepsilon/4\). Equations (5) and (10), integrated
along radial segments of length at most \(2T\), then give (6).
The unused probability margin can absorb all fixed prefactors above.

## 8. Consequences, scope, and remaining review obligation

If the physical fitting theorem gives an activity endpoint
\(S\le C_{\rm fit}y\), take \(T=C_{\rm fit}y\le T_0\).
The rectangle contains the radius-\(r_n\) neighborhood of \([0,S]\).
The original first-layer backward response is
\(\operatorname{sech}^2a\odot k\), so it has the same
\(CT\sqrt{\ell_n}\) bound as the carrier. Forward activations, top
responses, and their gates are bounded by (4). The first-layer columns
orthogonal to \(e_1\) remain exactly at initialization.

For each scalar response coordinate \(R(s)\) among these functions, a disk
of radius, for example, \(r_n/2\) about any real \(s\in[0,S]\) lies in
the proved domain. Cauchy's formula therefore gives
\[
 \frac{|R^{(q)}(s)|}{q!}
       \le \sup_{D_n}|R|\,(2/r_n)^q.                         \tag{34}
\]
This is an actual finite-network estimate, not an assumption inferred from
a real carrier maximum. It supplies a regularity input for compression;
it does not itself prove a sampling, cubature, or learned-state complexity
theorem. In particular, initial derivatives alone need an additional analytic
continuation or approximation argument to cover an interval longer than
their initial Taylor radius.

The proof's nontrivial checks are explicit: the inverse strip in Section 2;
the \(H=\sqrt nW\) normalization in (15)--(16); the deleted-row source in
(22); the \(T^2M\) feedback in (23)--(24); conditional Gaussian grids on
each cavity's own stopped domain; and common-prefix transfer of pole and
carrier caps. No full adaptive event is conditioned upon when using a
Gaussian tail. No conclusion for multiple training inputs, arbitrary labels,
arbitrary depth, or a width-uniform small-label limit is claimed.

## 9. Joint activity and circle-query extension

This appendix was added after the complete basic proof above was frozen at
SHA-256 `d2b5f9be450435ec4e65242c6e9fa774653c8d9a601344d7f871c47cb8b753d4`.
It addresses the supervisor's subsequent query-extension request. It does
not change Sections 1--8. Its status is a further internal proof candidate.

Take \(d=2\), the training input \(\sqrt2 e_1\), and query inputs
\(x_\theta=\sqrt2(\cos\theta,\sin\theta)\). The unchanged second
first-layer column is \(\beta=A_0e_2\). Define the actual query features by
\[
 b_\theta(s)=a(s)\cos\theta+\beta\sin\theta,
 \qquad h_\theta(s)=\tanh b_\theta(s),
 \qquad z_\theta(s)=W(s)h_\theta(s),
 \qquad g_\theta(s)=\tanh z_\theta(s),
 \qquad f_\theta(s)=\frac1n w(s)^\top g_\theta(s).              \tag{35}
\]
Here \(h_0=h\), \(z_0=z\), and \(g_0=g\); the subscript zero in these
three identities is the query angle, not initialization time.

After reducing the fixed constant in the activity radius (2), there is a
fixed \(c_\theta>0\) such that, with probability at least
\(1-\varepsilon\), these functions are jointly holomorphic on a
neighborhood of
\[
 s\in D_n,\qquad |\Im\theta|\le r_{\theta,n},
 \qquad r_{\theta,n}=c_\theta/\sqrt{\ell_n},                  \tag{36}
\]
with \(2\pi\)-periodicity in \(\Re\theta\). Uniformly there,
\[
 \|h_\theta\|_\infty+\|g_\theta\|_\infty\le C,
 \quad \|W_0h_\theta\|_\infty+\|z_\theta\|_\infty
                      +\|b_\theta\|_\infty\le C\sqrt{\ell_n},
 \quad |f_\theta|\le CT,                                   \tag{37}
\]
and
\[
 \|\partial_s z_\theta\|_\infty
       +\|\partial_s(W_0h_\theta)\|_\infty\le CT\sqrt{\ell_n},
 \qquad
 \|\partial_\theta z_\theta\|_\infty
       +\|\partial_\theta(W_0h_\theta)\|_\infty
                                          \le C\sqrt{\ell_n}. \tag{38}
\]
The proof requires no additional query backward-carrier estimate.

Allocate, for example, confidence \(\varepsilon/4\) to the basic theorem
and fixed additional fractions to the events below. Changing
\(\log(en/\varepsilon)\) to \(\log(4en/\varepsilon)\) changes only
absolute constants in (36)--(38).

The canonical Gaussian initialization supplies the event
\[
 \frac{\|a_0\|_2+\|\beta\|_2}{\sqrt n}\le C,
 \qquad \|a_0\|_\infty+\|\beta\|_\infty\le C\sqrt{\ell_n}. \tag{39}
\]
The maximum bound follows from scalar Gaussian tails; the normalized norm
bound follows by multiplying the Gaussian-square moment generating functions
and applying Markov's inequality, giving failure \(Ce^{-cn}\).
Conditional on any realization satisfying (39), the full training solution
and every stopped row cavity obey
\[
 \|a\|_2/\sqrt n\le C,
 \quad \|a\|_\infty\le C\sqrt{\ell_n},
 \quad \|\Im a\|_\infty\le4b.                              \tag{40}
\]
For the first two estimates integrate \(a'=\psi'(u)k\), where
\(\psi=F^{-1}\), using (10), (13), and the full or cavity carrier cap.
The last estimate follows by integrating \(\psi'\) from real \(\Re u\)
to \(u\), with the cavity pole cap \(2b\).

For \(\theta=t+i\tau\), (40) implies
\[
 \|\Im b_\theta\|_\infty
 \le4b\cosh|\tau|
       +(\|\Re a\|_\infty+\|\beta\|_\infty)\sinh|\tau|.
                                                               \tag{41}
\]
Choose \(c_\theta\) sufficiently small. Then the right side is below
\(1/4\) throughout (36), for both the full solution and every row
cavity on its own stopped training domain. Thus all query first-layer gates
and their first few derivatives are bounded before any assertion about the
query top preactivation is used. The matrices \(W\) and features
\(h_\theta\) already define jointly holomorphic \(z_\theta\); possible
poles arise only on subsequently applying tanh to \(z_\theta\).

Let
\[
 B_\theta(u,\beta)
 =\operatorname{sech}^2(\psi(u)\cos\theta+\beta\sin\theta)
                              \cos\theta\,\psi'(u),
 \qquad q_\theta=-a\sin\theta+\beta\cos\theta.              \tag{42}
\]
These are componentwise definitions. On the domain just proved safe,
\(|B_\theta|+|\partial_u B_\theta|\le C\), and
\[
 \partial_s h_\theta=B_\theta\odot k,
 \qquad \partial_\theta h_\theta
                =\operatorname{sech}^2b_\theta\odot q_\theta.
                                                               \tag{43}
\]
The full and every stopped row cavity consequently have
\[
 \|\partial_s h_\theta\|_2/\sqrt n\le CT,
 \qquad \|\partial_\theta h_\theta\|_2/\sqrt n\le C.         \tag{44}
\]
Since \(\|q_\theta\|_\infty\le C\sqrt{\ell_n}\) and its normalized
Euclidean norm is bounded, differentiating (43) gives the uniform bounds
\[
 \frac{\|\partial_s^2h_\theta\|_2}{\sqrt n}
                      \le C(1+2TM),
 \quad
 \frac{\|\partial_\theta\partial_sh_\theta\|_2}{\sqrt n}
                      \le CT\sqrt{\ell_n},
 \quad
 \frac{\|\partial_\theta^2h_\theta\|_2}{\sqrt n}
                      \le C(1+\sqrt{\ell_n}).                \tag{45}
\]
For the first bound use
\(\partial_s^2h_\theta=(\partial_uB_\theta)\odot k^{\odot2}
 +B_\theta\odot k'\). For the second use
\(|\partial_\theta B_\theta|\le C(1+|q_\theta|)\).
For the third use
\(\partial_\theta^2h_\theta
 =\tanh''b_\theta\odot q_\theta^{\odot2}
 -\operatorname{sech}^2b_\theta\odot b_\theta\).

For a row cavity, (22), (40), and the Lipschitz bounds just established give
\[
 \|\partial_s h_\theta-\partial_s h_\theta^{-j}\|_2
                       \le C(T+T^2M),
 \qquad
 \|\partial_\theta h_\theta
               -\partial_\theta h_\theta^{-j}\|_2
                       \le CT^2(1+\sqrt{\ell_n}).             \tag{46}
\]
In the second inequality the difference of \(q_\theta\) costs
\(C\|a-a^{-j}\|_2\le CT^2\). The difference of the gate multiplies
\(q_\theta^{-j}\), whose maximum is \(C\sqrt{\ell_n}\); it costs
\(C\sqrt{\ell_n}\|a-a^{-j}\|_2\). This explicitly accounts for the
otherwise dangerous initialized coordinate maximum.

Condition now on \(a_0,\beta\) and each row cavity's retained initialization.
The omitted row remains \(N(0,I_n/n)\). Apply the same Gaussian net argument
as in Section 6, this time to
\[
 v(s,\theta)=\partial_s h_\theta^{-j}(s)
 \quad\hbox{or}\quad v(s,\theta)=\partial_\theta h_\theta^{-j}(s),
\]
on its own stopped training domain times one angular period of (36).
Parameterize \(s=\lambda_c q\) as before. A grid in the four real
coordinates of \(q,\theta\), with mesh
\(n^{-3}/[C(1+\sqrt{\ell_n})]\), has polynomial cardinality in \(n\)
and \(\ell_n\). Equations (45) make interpolation error
\(O(n^{-5/2})\) on \(\|x_j\|_2\le K\). For fixed \(T>0\), this is
smaller than \(T\) at sufficiently large width. Equations (44) and the
complex Gaussian tail (30), followed by a union over rows and grid points,
therefore give with the allotted failure probability
\[
 \sup_{s,\theta}|x_j^\top\partial_s h_\theta^{-j}(s)|
                       \le CT\sqrt{\ell_n},
 \qquad
 \sup_{s,\theta}|x_j^\top\partial_\theta h_\theta^{-j}(s)|
                       \le C\sqrt{\ell_n}.                  \tag{47}
\]
Again, the conditional domains are the cavities' own domains, and the
Gaussian inequality is never conditioned on a full-network event. If (39)
or the retained operator condition fails, set the reference to zero before
applying the conditional argument.

For the actual query top preactivation,
\[
 \partial_s z_{\theta,j}
 =\delta_j\,h^\top h_\theta/n
       +x_j^\top\partial_s h_\theta
       +(W_{j,:}-x_j^\top)\partial_s h_\theta,
\]
\[
 \partial_\theta z_{\theta,j}
 =x_j^\top\partial_\theta h_\theta
       +(W_{j,:}-x_j^\top)\partial_\theta h_\theta.           \tag{48}
\]
Insert (44), (46), (47), and
\(\|W_{j,:}-x_j^\top\|_2\le CT^2/\sqrt n\). The respective errors
are at most \(C(T+T^2M)\) and \(CT^2(1+\sqrt{\ell_n})\).
Because \(M=AT\sqrt{\ell_n}\) with fixed \(A,T\), these prove (38)
for \(z_\theta\). Deleting the first and last terms in the first equation
of (48), and the last term in the second, proves the corresponding estimates
for \(W_0h_\theta\).

It remains to verify the query top gate. Start at real activity
\(\Re s\) and real angle \(\Re\theta\), where \(z_\theta\) is real.
Move vertically in activity, and then vertically in angle. The derivative
bounds (38), valid before this top gate is ever evaluated, give
\[
 \|\Im z_\theta(s)\|_\infty
 \le CT\sqrt{\ell_n}\,r_n
       +C\sqrt{\ell_n}\,r_{\theta,n}
 = C(Tc+c_\theta).                                         \tag{49}
\]
Reduce \(c,c_\theta\) so this is, for example, below \(1/4\).
Thus tanh of the query top preactivation has a fixed pole margin and is
jointly holomorphic and bounded. The \(\sqrt{\ell_n}\) coordinate bounds
for \(z_\theta,W_0h_\theta\) follow by starting from their known bound
at activity zero and angle zero and integrating (38) over a real angular
period and the bounded activity interval. Equation (41) gives the same
bound for \(b_\theta\); (4) gives \(|f_\theta|\le CT\).
This completes (36)--(38). No query top gate, no query backward response,
and no query quantity feeds into the training dynamics.

## 10. Exact activity parity and the symmetric rectangle

The zero-readout initialization implies the following exact analytic parity:
\[
 u(-s)=u(s),\quad H(-s)=H(s),\quad a(-s)=a(s),\quad
 w(-s)=-w(s).                                               \tag{50}
\]
To verify it, substitute
\(\widetilde u(s)=u(-s)\), \(\widetilde H(s)=H(-s)\), and
\(\widetilde w(s)=-w(-s)\) into (8). Its top response is
\(\widetilde\delta(s)=-\delta(-s)\), so all three differential equations
and the initial condition agree. Local analytic uniqueness proves (50).
Reflection therefore extends the solution from \(D_n\) to \(-D_n\).
The two definitions agree near zero and hence throughout their connected
overlap by the analytic identity theorem. Their union is the closed rectangle
\[
 |\Re s|\le T+r_n,\qquad |\Im s|\le r_n,                    \tag{51}
\]
with a neighborhood of holomorphy and the same coordinate bounds.
The query first-layer, top-layer, and frozen-matrix source vectors
\(h_\theta(s),g_\theta(s),W_0h_\theta(s)\) are all even in activity;
\(f_\theta(s)\) is odd. The training top response and lower carrier are
odd. The joint angular strip and all its bounds extend by the same reflection.

For clarity, (51) is a rectangle of holomorphy, not a disk of radius \(T\)
about zero. An approximation scheme using initial jets must respect this
geometry; parity does not enlarge the Taylor disk at the origin.
