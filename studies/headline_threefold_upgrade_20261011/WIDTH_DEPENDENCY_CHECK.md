# Finite width dependencies: direct reconstruction

2026-10-11. Scoped mathematical audit. This note supersedes the
**uninspected-input qualification** in `WIDTH_UPGRADE.md`, not that note's
distinction between the finite-query and whole-sphere problems. No paper,
book, implementation, experiment, or Git change is made.

## Verdict and scope

The three newly authorized inputs were read completely:
`INSERTION_MAP_MODULI.md`, `EXPLICIT_FITTING_WIDTH.md`, and
`QUANTITATIVE_INSERTION_WIDTH.md` under
`studies/unseen_query_decoder_20261005/`. Their raw coefficient recurrences
and finite initialization argument supply the previously missing inputs.
Combined with the actual nonlinear identities in the current
`paper/compact_foundations.tex`, the finite composition in
`SOURCE_SCOPE_CHECK.md` and `TAYLOR_ROUTE.md`, and the corrected prefix
meshes, they close the proposed polynomial sufficient **source-event**
widths for Legendre and finite-panel Taylor below. This is a new direct
composition check; it is not a claim that an earlier PASS or the earlier
limited audit had already checked these files.

Two qualifications are essential. The Legendre finite source uses a
smaller, confidence-dependent complex rectangle, not the current paper's
original radius. The Taylor statement requires its capped radius and the
level-mesh repair in `TAYLOR_PREFIX_REPAIR.md`. Neither assertion supplies
a polynomial whole-sphere Harmonic onset, a same-time denominator, or an
end-to-end numerical setup theorem. No additional linked study was read.

## 1. Exact source statements checked

Use the current paper's model: normalized unit inputs
\(v_a=x_a/\sqrt d\), hidden width \(n\), depth \(L\ge2\),
\(m\ge2\) training inputs, independent first-layer entries
\(N(0,1)\), subsequent entries \(N(0,1/n)\), and zero initialized
readout. The prediction is \(f_a=w^\top h_a^{(L)}/n\), the loss is
\(m^{-1}\sum_a(f_a-y_a)^2\), and physical mobilities are
\((n,1,\ldots,1,n)\). Retain the paper's analytic activation envelope
\(\beta\ge10\), population Gram gap \(\gamma>0\), and assumptions

\[
X=\beta^L,\qquad \lambda=\gamma/m\in(0,1],\qquad
Y=\|y\|_2/\sqrt m>0,\qquad Y/\lambda\le X^{-30}.
\]

Write \(S=16Y/\lambda\), \(\chi=1+\lambda^{-1}\), and
\(\ell=\log(en)\). For \(0<\rho<1/4\), set

\[
u=\max\left\{1,\left\lceil
\frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\}.
\tag{1}
\]

Here \(u\) is a deletion/moment count; it is not a passive-input count.

**Legendre dependency.** Put

\[
A_{\mathrm L}=X^{2000}\chi^4(m+d+u+1)^4,
\qquad n\ge\left\lceil(A_{\mathrm L}/\rho)^{1100}\right\rceil.
\tag{2}
\]

With probability at least \(1-\rho\), the training forward/backward
source and all training preactivation responses exist on a neighborhood of

\[
[-r,T+r]+i[-r,r],\qquad
T=32\ell/\lambda,\qquad
r=[uX^{100}(1+\lambda)\sqrt\ell]^{-1}.
\tag{3}
\]

The event includes the ambient \(d\)-dimensional real fitting event.
In particular, for the exact response

\[
R_{ba}^{(j)}=D_\Theta z_b^{(j)}\nabla_\Theta F_a,
\quad \Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w),
\quad F_a=nf_a,
\]

the coordinate source bound is
\(\max_{a,b,j,i,t}|R_{ba,i}^{(j)}(t)|
\le S U_{\rm fin}\sqrt\ell\), with the paper's unchanged
\(U_{\rm fin}\le X^{26}\). The original RMS, coordinate and training
backward bounds are retained. The real late-time extension in
`SOURCE_SCOPE_CHECK.md`, Section 6, uses fitting decay and introduces only
a polynomial gate already dominated by (2).

**Finite-panel Taylor dependency.** For \(p\ge0\) declared passive
inputs, put \(N=m+p\) and

\[
A_{\mathrm T}=X^{4000}\chi^8(N+d+u+1)^8,
\qquad n\ge\left\lceil(A_{\mathrm T}/\rho)^{40000}\right\rceil.
\tag{4}
\]

The capped radius, flaring domain, and panel cover of `TAYLOR_ROUTE.md`,
Sections 2–3, give the finite-input source with probability at least
\(1-\rho\): forward families at all \(N\) inputs, backward families
only at the \(m\) training inputs, and all \(mN\) driver/evaluation
responses. The cap uses
\(b_n=\log(e+\ell)\), \(B_n=1+(S^2/\eta_*)b_n\), and a radius
no larger than \([X^{300}(1+\lambda B_n)\sqrt{b_n}]^{-1}\),
in addition to the route's original pole restriction. Its radius does
not depend on \(u\). The source constants and claimed panel-count order
are unchanged; the geometric constant can increase.

These are polynomial sufficient widths in
\(X,\lambda^{-1},m,d,p,\rho^{-1}\). Since \(X=\beta^L\), this
does not mean polynomial dependence on \(L\) separately. The gate does
not contain \(Y^{-1}\). Any later inverse-label gate used to simplify a
storage display is a separate deterministic statement.

## 2. Finite fitting and dimension scope

`EXPLICIT_FITTING_WIDTH.md` does not rely on its historical \(m\ge d\)
front-matter restriction. Its proof tracks empirical standard deviations
and covariance entries separately. With its explicitly defined
\(R,K,D,T_1,T_2,C\), the induction is

\[
\Delta_j\le\varepsilon+s\Delta_{j-1},\qquad
E_j\le(2K+1)\varepsilon+s^2E_{j-1}+D\Delta_{j-1}.
\tag{5}
\]

Thus \(\Delta_j\le\varepsilon T_1\) and
\(E_j\le\varepsilon C\). Choosing
\(\varepsilon\le\min\{(8T_1)^{-1},\gamma/(2mC)\}\)
gives Gram error at most \(mE_L\le\gamma/2\).

The covariance comparison behind (5) is valid even at singular
covariances. Shrink each pair's marginal standard deviations to their
componentwise minima, bound this scaling error by Lipschitz activation
growth, and interpolate the correlation at the common marginals.
Gaussian integration by parts bounds the correlation derivative by
\(s^2\tau_a\tau_b\). The identity
\(\tau_a\tau_b|\rho-\rho'|
\le|C_{ab}-C'_{ab}|+2R\Delta\) then proves the stated comparison.
Zero marginal variances follow by continuity; no inverse covariance is
used.

Gaussian norm concentration applies to the possibly degenerate feature
vectors because the maps from the underlying standard Gaussian row are
Lipschitz. Polarization supplies the off-diagonal estimate. The sphere
net costs \(d\log(1+2/h)\); the first-layer operator tail costs
\(d\log9-(8-\log9)n\). Neither compares \(m\) with \(d\).
The explicit bound is dominated by

\[
X^{32}\chi^2
\left[dL\log\beta+\log\frac{512L(m+1)^2}{\rho}\right]+1.
\tag{6}
\]

The source budgets at initialization have conditional mean below four
and second moment below fifteen. Conditional Chebyshev gives a union
cost at most a constant times \(mL/n\). It is paid by (2) or (4).
Initial cavities do not require a covariance concentration union over
all deletion sets: zero embedding and the full operator bounds give
feature discrepancy
\((8s)^L\sqrt u(b+sZ_0)\), then singular-value perturbation transfers
the fitting margin. The fresh-row coordinate comparison has tail
\(2\exp[-n^{4/5}/(2D_{\rm init}^2)]\). The stated gates pay for
the deletion union before that row's operator restriction is imposed.

Equivalently, the training-span isometry in `SOURCE_SCOPE_CHECK.md`
reduces training dimension to \(k\le\min(m,d)\), preserving roots,
physical time and the response. Its frozen orthogonal first-layer block
must be retained for ambient queries. Intersect with (6), rather than
claiming that a reduced training network alone represents the sphere.

## 3. Scaling, raw maps, and explicit coefficient bounds

Let \(\bar u=(\Theta-\Theta_0)/S\), \(\bar F=F/S\), and
\(\bar r=r/S\). The exact retained equation is

\[
\dot{\bar u}=-\frac2m\sum_a\bar r_a
\left[\nabla_{\bar u}\bar F_a+
D_{\bar u}h_a^{(j-1)\top}\bar q_a\right].
\tag{7}
\]

Zero readout initialization gives
\(\bar F_a=\bar u_w^\top h_a^{(L)}\). Consequently there is no
inverse \(S\) in any Taylor coefficient. The forward residual in (7)
includes the entire omitted top prediction offset; it multiplies both
retained terms. A reverse port is not inserted into the prediction.

For frozen controls, differentiating (7) gives exactly the three forcing
maps in the new inputs: the changed-residual rank-one term, the forward
gradient derivative, and the reverse-force derivative. Their Duhamel
bound is

\[
\sqrt u\,J_0n^{1/4000}
\{A_n(2T\sqrt{\mathcal K}\,\tau_*+M_\delta)+Sf_*B_n^{\rm ctrl}\}.
\tag{8}
\]

The control symbol \(B_n^{\rm ctrl}\) in (8) is not the logarithmic
factor \(B_n\) in Section 1. In the old modulus recurrences their
\(V_j\) is the current activity constant \(V_j^0\), not the angular
bound \(V_j(G)\). Their local \(D_0\) is also not the source trace
constant named \(D_0\).

Here is a direct, deliberately loose exponent check of the modulus
recurrences (4)–(20), using \(T_0\le64/\lambda\). All powers are
powers of \(X\); scalar additions and geometric layer sums are included.

| Coefficient family | Sufficient bound |
| --- | --- |
| \(H_j,P_j,f_j;\ k_j,\tau_j;\ V_j^0\) | \(X^3;\ X^4;\ X^7\) |
| \(A_*,D_*,\eta_*^{-1},\mathcal B,\sqrt{\mathcal K},J_0\) | \(X^5,X^6,X^{27},X^3,X^7,X\) |
| \(M_0,A_0,B_0,E_0\) in modulus (4) | \(X^{31},X^{33},X^{32},X^{38}\) |
| Control-speed recurrence \(T_j^0,D_0\) | \(X^{45},\lambda X^{45}\) |
| Raw parameter, forward, backward map coefficients | \(X^{80}\chi,X^{85}\chi,X^{125}\chi\) |
| Control-difference coefficients | \(X^{90}\chi\) |
| Reference speeds after their factor \(\lambda\) | at most \(X^{47}\) |
| Raw parameter, forward, backward time derivatives | \(X^{125}\chi,X^{140}\chi,X^{190}\chi\) |

For example, \(M_0=\eta_*^{-1}[1+\log(2\mathcal B)]\),
\(v_0=J_0\{A_0(2T_0\sqrt{\mathcal K}\tau_*+E_0)+Sf_*B_0\}\),
and \(z_j^0=P_j(Sv_0+A_0)\) give the first raw-map rows directly.
Backward propagation multiplies by \(10s\), whose complete layer
product is at most \(X^2\); the reference-carrier factor is an
additive forcing, not a factor incurred at every layer. In the largest
time-derivative forcing, \(t_2M_0z_j^t\), the displayed exponents sum
to at most \(1+31+140\); its layer propagation fits within 190.
Control differences use the same linear equation with amplitude one.
The lower probe recurrence uses the same bounded propagation.
The third derivative is bounded by \(\beta^2\) on the old strict
strip, or by \(4\beta^2\) on the current joining strip; the table's
slack covers the latter.

In particular the asserted common coefficient
\(C_0\le X^{300}\chi\) follows without a depth-squared exponent,
an inverse label, or an unspecified width threshold. Quadratic matrices
are \(R=\operatorname{sym}(E_i^\top L)\), so their norms and control
moduli have the same bounds. Centered interpolation costs
\(10u\|\Delta R\|\), including the trace change; its explicit
control gate is \(40C_cu^{3/2}\ell^2\le n^{99/4000}\).

One old boundary statement must be corrected: the incoming-row increment
with a factor \(n^{-1/2}\) applies only to layers \(j\ge2\).
At the first layer the bound is \(sS^2M\), without that factor.
The current compact proof explicitly handles it: there is no retained
reverse port below the first layer, and this row enters the omitted
neuron's uniformly tested scalar controls. Thus the learned **retained**
port estimate remains valid; applying the old formula literally at
\(j=1\) would not be valid.

## 4. Augmented response and nonlinear closure

The needed response is not an arbitrary Jacobian norm. Its scaled
recurrence is exactly

\[
\bar R_{ba}^{(1)}=\bar\delta_a^{(1)}v_a^\top v_b,\qquad
\bar R_{ba}^{(j)}=\bar\delta_a^{(j)}c_{ab}^{(j-1)}
+W^{(j)}\bar Q_{ba}^{(j-1)},\quad
\bar Q=\phi'(z_b)\odot\bar R,
\quad c_{ab}=h_a^\top h_b/n.
\tag{9}
\]

Besides its outgoing response port, deletion introduces the lower
observable \(C_bC_a^\top\bar q_a\), where
\(C_b=D_\Theta h_b\). The Gaussian event must include forward images
of \(C_a^{0\top}y_i\). The exact subtraction is

\[
(C_b^1C_a^{1\top}-C_b^0C_a^{0\top})y_i
=(C_b^1-C_b^0)C_a^{0\top}y_i
+C_b^1(C_a^1-C_a^0)^\top y_i.
\tag{10}
\]

The first term uses the reference probe's coordinate localization; the
second uses the lower adjoint recursion. Hence their common small factor
is \(d_0+n^{-1/2}\), not a merely bounded operator difference.
In the activated-response subtraction, only the additive second-order
gate term multiplies the reference response maximum. Homogeneous
propagation remains \(10s\). This checks that passive inputs add copies
of maps, not one cutoff factor per layer or a new optimizer sum.

With the raw-amplitude envelope \(M_0\le X^{80}\) and
\(U_{\rm fin}\le X^{26}\), all these augmented coefficients are
bounded by

\[
X^{100}(1+M_0+4U_{\rm fin})^2(1+C_0)^2
\le X^{1000}\chi^2=:C.
\tag{11}
\]

The resulting map, control-modulus, and actual analytic derivative
bounds are respectively
\(C\sqrt u\,n^{1/4000}\ell^5\),
\(C\sqrt u\,n^{1/4000}\ell^4\), and
\(C\sqrt{un}\,n^{1/4000}\ell^8\).
There are at most \(4u(N+1)^2\) real controls, of amplitude
\(C\ell\) and speed \(C\sqrt n\ell^3\).
The factor \(\sqrt n\) occurs once: a reference coordinate time
derivative is obtained from an RMS derivative. In the term
\(\phi''\dot z_b\bar R_{ba}\), use the stopped coordinate response
cap and the RMS speed of \(z_b\).

The compact proof now supplies the nonlinear part missing from the
historical modulus note. Set
\(N_0=n^{1/100}\), \(d_0=n^{-1/10}\), \(u_0=n^{-1/25}\).
Its exact activation, mixer, gradient, reverse-force and top-offset
subtractions, including (10), yield the integrated bound

\[
A\ell^8n^{1/4000}
\{n^{-0.08}+u_0^2+n^{-0.48}+n^{-1/2}\},
\tag{12}
\]

where \(A=A_{\mathrm L}\) or \(A_{\mathrm T}\).
Both numerical gates give \(A\ell^{16}\le n^{1/1000}\).
Thus the largest power in (12) is \(n^{-0.07875}\), strictly below
\(u_0/2\) at the stated gates. The joining-strip inequality is paid
at the same gate. This closes the first-exit remainder and gives retained
coordinate differences below \(n^{-1/30}\), including the response.

The new files alone do not prove (12). The present conclusion uses the
explicit current-paper identities just checked; it does not silently
promote the old note's stated open nonlinear interface into a theorem.

## 5. Finite meshes, traces, and budget probability

At fixed cavity and deterministic controls, Gaussian root covariance is
\(I/n\) in dimension at most \(2un\). The gates make each map norm
at most \(n^{1/200}\). Coordinate and centered-quadratic tails at
\(n^{-1/10}/8\) are at most \(4e^{-n^{0.78}}\), using
\(\|R\|_{\rm HS}\le\sqrt{2un}\|R\|\). The Euclidean-image
mean is at most \(\sqrt{2u}\,n^{1/200}<n^{1/100}/2\).
The logarithmic control entropy is bounded by
\(A\ell^8n^{5/8}\); deletion and remaining finite unions keep the
total below \(n^{0.65}\). The local failure is below
\(e^{-n^{0.7}}<\rho/16\).

The endpoint argument is not a Gaussian assertion at a full-root-dependent
stop. For (3), the inward tensor mesh from `SOURCE_SCOPE_CHECK.md`
lies in every common rectangle prefix. For Taylor, the deterministic
level-and-endpoint mesh from `TAYLOR_PREFIX_REPAIR.md` is indispensable:
test \(P_{\min(s_j,\sigma_c)}q\), where \(\sigma_c\) is the
cavity's own retained-measurable stop; only afterward choose a level below
the common stop. The respective endpoint counts are at most \(n^6\)
and \(n^9\). Actual analytic derivatives are used only inside the
common domain. Own-stopped clamped extensions are not called holomorphic.

The scalar expansion retains all four nonzero means in compact equation
`cp:src-traces`: lower forward trace, upper residual-Hessian trace,
direct port Hessian, and adaptive-residual rank-one trace. Normalized
Schatten Hölder and the activity-ordered exponential series bound the
first three with the original source constants. Endpoint rank is at most
\(n\), so normalization is \(1/n\), not inverse parameter dimension.
The fourth trace is at most \(A\ell^8n^{-1+1/4000}\). The finite
remainders are below \(n^{-1/40}\). The two sample-RMS feedback
inequalities have product at most \(1/2\), giving the original
\(C_{\rm abs}\), independently of \(u,N\).

The Gaussian rectangle lemma in the compact proof applies to complete
own-stopped coefficient paths: radius \(D\), modulus \(K\), and
rectangle side \(H\) give mean at most
\(256D\sqrt{\log(e+HK/D)}\) and log moment bounded by that mean
times the exponent plus \(2a^2D^2\). Its sample-RMS form adds \(2D\).
This lemma is proved there by dyadic meshes and Gaussian concentration.

For Taylor the complete common-cavity complex-reference estimates
(15)–(23) in `TAYLOR_ROUTE.md` give a fixed-exponent correction moment
\(\le e^{X^{-180}}\), including arbitrarily small \(\lambda\).
The factor \(\lambda\) in the normalized coefficient derivative
and the cap \(1+\lambda B_n\) are both necessary for that estimate.
Each complete root reference \(A_i\) then satisfies
\(\mathbb E(A_i^2\mid\text{common cavity})<3\).
Independence is used only across distinct root pairs of this common
cavity, not across samples or correction paths.

For completeness the smaller Legendre rectangle also closes directly
without a fixed-\(u\) limiting argument. Its provisional derivative
recurrences give \(J_*\le X^{34}\), so one can bound its correction
radius and modulus by

\[
D\le X^{40}\lambda B_n r,\qquad K\le X^{40}\lambda B_n,
\qquad H\le64\ell/\lambda.
\tag{13}
\]

With (3), \(B_n\le1+\log(e+\ell)\), the rectangle lemma's mean
plus \(2D\) is at most \(X^{-50}\). To check uniformity, split the
entropy logarithm into \(\log128+\log u+100\log X+
\log\chi+(3/2)\log\ell\), use
\(u^{-1}\sqrt{\log u}\le1\),
\(\lambda\sqrt{\log\chi}\le2\), and boundedness of
\((1+\log(e+\ell))(1+\sqrt{\log\ell})/\sqrt\ell\).
The remaining numerical constants are absorbed by five of the sixty
available powers of \(X\). This gives the same complete-reference
fixed-exponent construction as Taylor. One need not demand that an
unrooted order-\(u\) complex moment approach one uniformly in \(u\).

Singleton-to-common-cavity differences are extended by their separate own
stops and projected onto the deterministic ball of radius
\(4n^{1/100}\). Both paths omit the paired root. Their Gaussian radius
is \(v_n=4n^{-49/100}\), and their mean is bounded by

\[
\mu_n\le256v_n\sqrt{\log(e+X^{400}\chi\ell^4/v_n)}+2v_n.
\]

The gates imply \(u\mu_n+u^2v_n^2<10^{-3}\).
Cauchy–Schwarz separates main-root and correction products; Hölder handles
the dependent corrections. Dropping the full-event indicator only after
pathwise domination gives, for \(|I|\le u\),

\[
\mathbb E\left[1_E\prod_{i\in I}
e^{\eta_*(Z_{a,i}+K_{a,i}/S)}\right]\le16^{|I|}.
\tag{14}
\]

The recurrence constants give \(2\eta_*K_{\rm src}\le33/4096<1/100\),
so each repeated weight is at most \(e^{\sqrt\ell/100}\).
Partitioning an ordered \(u\)-tuple by its distinct indices, and
encoding each repetition by an edge from its block minimum, bounds the
collision multiplier by
\(\exp\{\binom u2 e^{\sqrt\ell/100}/(16n)\}\le e\)
under \(n\ge4u^3\). Consequently the empirical \(u\)-th moment is
at most \(e16^u\). Markov and the sample/layer union give budget-hit
probability at most \(emL(64e^2)^{-u}\le\rho/4\).

Initialization costs less than \(\rho/4\), local maps less than
\(\rho/16\), and the two scalar/response maximum events together less
than \(\rho/16\). Cavity budget, pole, activity and operator stops
have strict transferred margins by (12). The total is below \(\rho\),
including the extra ambient fitting intersection if the training-span
argument is used. This is a finite probability calculation at (1)'s
actual confidence-dependent count, not a limit at each fixed count.

## 6. What is and is not resolved

The previously uninspected coefficient inputs are now checked and the
Legendre/Taylor source-event probability gates (2) and (4) are closed by
the stated composition. The independent deterministic structural onset
repairs in `WIDTH_UPGRADE.md` remain separate pieces of their respective
compression theorems. Small-width fallback algorithms, normalization
denominators and numerical setup are not newly proved by this note.

No whole-sphere source event is inferred from these finite-query events.
In particular this audit does not resolve the Harmonic question or turn
a trajectory-wide lower bound into a same-time lower bound. It does not
claim that the maintained paper already states these new polynomial
gates; promotion would be a separate authorized action.

## Frozen input hashes

SHA-256 of the newly authorized files, all read in full:

| File in `studies/unseen_query_decoder_20261005/` | SHA-256 |
| --- | --- |
| `INSERTION_MAP_MODULI.md` | `ea71fbc226d4ac02031661a96650256a44260553550ef2b2fd0e10a68b78c93e` |
| `EXPLICIT_FITTING_WIDTH.md` | `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d` |
| `QUANTITATIVE_INSERTION_WIDTH.md` | `40fc026d7e0d18b968ae1526a94792290dc25cd56f97972db526dfd3e8aeb31b` |

Previously allowed proof inputs used in the composition:

| File | SHA-256 |
| --- | --- |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `polynomial_width_compression_20261010/SOURCE_SCOPE_CHECK.md` | `767d252e9b5083a3f9e8372856ead1c481b62d3fdfa959d67f73c55b8d78dded` |
| `polynomial_width_compression_20261010/TAYLOR_ROUTE.md` | `d9153aa789ec23d23683b79f9e5e5a6215a4bb884757079ff1b516235504030e` |
| `polynomial_width_compression_20261010/TAYLOR_PREFIX_REPAIR.md` | `7e9e027676f68fa362cf4016f578ee4ff96cc8cfbaa7ba63d6457417ebcb0c48` |

The historical dependencies cited inside the three new files were not
fetched. Where their old interfaces were incomplete, the exact current
paper formulas and the explicitly allowed later repairs above supplied
the proof; earlier verdict labels supplied none of it.
