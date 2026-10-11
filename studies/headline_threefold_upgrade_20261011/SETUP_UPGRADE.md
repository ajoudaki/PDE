# Efficient supplied-dense initialization for the current selected models

2026-10-11. Scoped theoretical result. No experiments, paper edits, Git
operations, or promotion. The conclusions below are conditional on the
current paper's fitting/source event and retain its eventual-width
qualification. They are exact-real arithmetic results, not finite-word
implementation theorems.

Here preservation of the current relative comparison means the paper's
ratio of two complete-trajectory norms on its original query domains. It
does not establish a quotient at each time, or a test-only Taylor lower
denominator; those separate obligations are recorded in `RESULT.md`.

## Result and its precise scope

The current Harmonic and Taylor models can both be initialized by a disposable
finite dense rollout, with their current retained-coordinate orders, declared
query domains, corrected optimizer, all-time comparison, and fitted endpoint
preserved. For separately fixed admissible problem parameters, write
\(\ell=\log(en)\). Sufficient bounds are

| Model | Supplied-dense setup arithmetic | Peak setup real coordinates | Retained real coordinates |
|---|---:|---:|---:|
| Harmonic | \(O(n^2\ell^{3d/2+1})\) | \(O(n^2)\) | current \(O(\ell^{3d+2})\) bound |
| Taylor | \(O(n^2\ell^{5/2})\) | \(O(n^2)\) | current \(O(\ell^3)\) bound |

The Taylor row is an adaptation proved here. Its more informative arithmetic
bound is \(O(n^2\ell^{5/2}+n\ell^5+\operatorname{polylog}(n))\);
the lower-order terms must be retained outside fixed-parameter asymptotics.
The complete parameter/order ledger appears below. The constants need not be
uniform in \(m,d,L,\beta,\gamma^{-1},Y^{-1}\), or the passive-panel size.

Both rows achieve \(Y/n\) absolute error against their supplied coupled dense
run on the same domain and all physical times, including infinity, eventually
at each fixed confidence. Consequently the current negligible-relative-error
comparison is preserved. This result constructs a valid member of the current
selected-model family; it need not reproduce the coordinates selected by one
particular exact-coefficient initializer.

The arithmetic includes source construction, initialized images, basis
formation, selection, metrics and small-matrix assembly. It counts ordinary
scalar activation values, elementary scalar functions and Gaussian samples
as primitives only when explicitly stated. The rollout needs no oracle for
high activation derivatives. Exact initialized training features and exact
linear algebra remain part of the real-arithmetic model. A finite-precision
version covering those operations and the subsequent all-time nonlinear
evolution is not proved.

## Inputs and the current transfer theorem

Use the network, loss, Gaussian initialization, zero initial readout, and
mobilities in `paper/compact.tex`, equations `cp:network`--`cp:flow`. In
particular, \(v=x/\sqrt d\),
\[
z^{(1)}=W^{(1)}v,\quad z^{(j)}=W^{(j)}h^{(j-1)},\quad
h^{(j)}=\phi_j(z^{(j)}),\quad f_n=w^\top h^{(L)}/n,
\]
\[
\delta^{(L)}=w\odot\phi_L'(z^{(L)}),\qquad
\delta^{(j)}=\phi_j'(z^{(j)})\odot W^{(j+1)\top}\delta^{(j+1)}.
\]
When a prediction is indexed by \(v\) below, it means the same prediction
at original input \(x=\sqrt d\,v\), with no output rescaling.
All training examples have unit normalized inputs. Let
\(\lambda=\gamma/m\in(0,1]\), \(z=Y/\lambda>0\), and \(S=16z\).
Assume the current sufficient label allowance
\(z\le\beta^{-30L}\), with the current definition of \(\beta\).
This is not an assertion about a larger historical label interval.

The four source families are
\[
h^{(j)},\quad W_0^{(j)}h^{(j-1)},\quad
\delta^{(j)},\quad W_0^{(j+1)\top}\delta^{(j+1)},
\qquad W_0^{(j)}=W^{(j)}(0),
\]
with the first forward image and last reverse image omitted. Harmonic covers
all unit inputs. Taylor covers \(M=m+p\) inputs fixed before initialization;
its backward sources need only the \(m\) training inputs.

The source-to-runtime proposition in `paper/compact_selected.tex`,
`cp:selected`, requires a time-independent space \(E_j\subset\mathbb R^n\)
at each layer. It requires coordinate source error at most \(\eta\), exact
initialized-image pairing, the constant vector, exact initialized training
features/images, and first-layer weight columns. It does **not** require that
the generators be literal derivatives, or that the same support be obtained
under a different valid coefficient approximation.

Use the current horizon
\[
T=32\ell/\lambda.
\]
Let \(\mathcal A_n>0\) be the explicit finite-horizon coefficient in
`cp:selected-coefficients` and \(\mathcal D\) its endpoint-tail coefficient
in the same proof. A completely specified tolerance is
\[
\eta=\min\{1,Y,S,Y/(2n\mathcal A_n)\}.
\tag{1}
\]
Impose the eventual gate
\(\mathcal D e^{-8\ell}\le Y/(2n)\). The transfer bound then gives
\(\mathcal A_n\eta+\mathcal D e^{-8\ell}\le Y/n\).
Equivalently one may use `cp:selected-tolerance` and its eventual-width
qualification. The coefficient ledger is a finite recurrence in the supplied
parameters, and \(\log(1/\eta)\le2\ell\) eventually for every fixed
admissible problem.

The older `paper/cost_appendix.tex` prescription lengthens the horizon when
inverting its older comparison certificate. That is a valid distinct
prescription; it is unnecessary for the present compact theorem and is not
silently substituted here.

## A common finite dense rollout

The setup integration panels below are distinct from Taylor's retained source
panels. The rollout uses short numerical panels even when a source is
analytic on a much larger disk. This avoids any need to reconstruct large-disk
Taylor derivatives from an inaccurately located anchor.

The dense coordinates for the error estimates are
\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\quad r_a=f_n(v_a)-y_a,\quad \rho=\|r\|_2/\sqrt m,
\]
with the Euclidean block norm (Frobenius on matrix blocks). With
\(\xi_a=\nabla_\theta f_n(v_a)\), the stated mobilities give exactly
\[
\dot\theta=F(\theta),\qquad
F(\theta)=-\frac2m\sum_{a=1}^m r_a\xi_a.
\]
Thus the proof compares against the fully trained nonlinear dense network.
The disposable activation-polynomial field changes only its scalar
activations while producing source approximations to this original field.

The required deterministic integration results are proved in the allowed
setup sources:

- `LOCAL_CONTINUATION_SETUP.md`, equations (6)--(30): complex restarts from
  computed anchors, Taylor defects, and global signed-defect stability.
- `SETUP_INTEGRATION_PROOFS.md`, “Signed defect stability”, “Real-value
  activation backend”, “Dense local jets and anchor advancement”, and
  “Source-jet compatibility and complete explicit costs”: finite real-value
  activation construction, factored jets, and a Euclidean source-value bound.
- `SETUP_INTEGRATION_ORDERS.md`: the complete scalar recurrence recipe.

The hypotheses needed from the current source proof are present in
`paper/compact_foundations.tex`: its working whole-sphere domain has the
preactivation strip margin, its equation `cp:src-improved-maxima` bounds
complex training carriers, and `cp:source` bounds all source/operator RMS
norms. Only disks inside the current finite source rectangle are needed.
The old all-horizon complex extension is not needed here.

Here is an explicit way to instantiate that recipe using the current bounds.
Set
\[
r_t=\frac{\lambda}{\beta^{30L}Y^2\sqrt{(d+3)\ell}},\quad
H_j^{\rm src}=\beta^{3L},\quad K_{\rm src}=\beta^{21L},
\quad M_c=2SK_{\rm src}\sqrt\ell,
\tag{2}
\]
and use \(b=\beta-1\), \(s=t_2=\beta\) in the deterministic
recurrences. All are conservative upper/lower bounds in the appropriate
direction. In Taylor's input-reduced construction below, replace \(d\) by
the reduced dimension \(k\). Set the old late-extension correction
\(Z_n\) to zero: complex carrier control is already available throughout
the finite rectangle being used. There is no claim about later disks.

For explicit numerical orders, let \(P_*\), \(\kappa_*(M)\),
\(G\), and \(J_{\rm loc}(M)\) be exactly the finite recurrences (6)--(7)
of `LOCAL_CONTINUATION_SETUP.md`, with the substitutions (2), and with
\(R=1+S\beta^{3L}\). Define
\[
b_n=\min\{1/4,a/(16\sqrt nP_*),
                    1/(\sqrt n\kappa_*(M_c))\},
\]
\[
L_n=2G^2+2(2Y+G)J_{\rm loc}(M_c+1),\quad
V=2G(2Y+G),\quad
\widehat R_n=\min\{r_t/2,(8L_n)^{-1}\}.
\tag{3}
\]
Let \(A_n,C^{\rm r},J^{\rm r},C_{\rm src}\) be the **real-defect**
coefficients (21)--(22) of that note, evaluated at
\(M=2SK_{\rm src}\sqrt\ell\). This \(A_n\) is distinct from the
selected-model coefficient \(\mathcal A_n\) in (1).

Suppose a consumer wants every evaluated base-source vector to have Euclidean
error at most \(\varepsilon_v\). In the source-jet bridge take its
\(\delta_{\rm node}=\varepsilon_v\) and its activation-backend requested
coordinate tolerance
\(\tau=\varepsilon_v/(32\sqrt n)\). Define
\[
e_d=e^{-A_n}\min\left\{\frac14,
 \frac1{\sqrt8(C^{\rm r}+J^{\rm r})\sqrt T},
 \frac{\tau}{4C_{\rm src}n},\frac{b_n}{16}\right\},
\quad
\zeta_F=\min\{e_d/(2T),b_nL_n/4,V/2\}.
\tag{4}
\]
Use the activation backend's finite recurrences (Setup-A.12)--(Setup-A.25),
with this \(\tau\), to choose its scalar approximation tolerance
\(\epsilon\). These recurrences bound the difference between the original
dense field and its disposable polynomial-activation field on a verified
moving parameter tube; they do not assume a numerical trajectory stays there.

A sufficient real-part bound for that backend is
\[
Z_*=[\beta^{21L}+16\sqrt{d+3}\,\beta^{3L}+1
           +\beta^{26L}\sqrt{d+3}\,S^2]\sqrt\ell+a/8.
\]
Use its ellipse construction with
\[
B=8(Z_*+a+1),\quad
\tau_o=\operatorname{arsinh}(31a/(64B)),\quad
\tau_i=\operatorname{arsinh}(29a/(64B)),\quad
\Delta=\tau_o-\tau_i,
\]
\[
C_a=\max\{1,512/a,2(512/a)^2\},\quad
\epsilon_p=\epsilon/C_a,\quad M_\phi=b+s(B+a),
\]
\[
D=\max\left\{1,\left\lceil\Delta^{-1}
\log\max\{e,24M_\phi/(\epsilon_p\Delta)\}\right\rceil\right\}.
\tag{5}
\]
For each layer, \(4(D+1)\) real activation-value calls and cosine sums
produce a degree-\(D\) polynomial approximating the activation and its first
two derivatives on the required domain. Finite value-call error at most
\(\epsilon_p/[4(D+1)e^{D\tau_i}]\) is allowed for this disposable
polynomial only. This is a certified value backend, not a high-derivative
oracle. Exact initialized training additions remain separate original-
activation evaluations.

Let \(C_g=\max_j\{H_j+1,B_j+1\}\), where \(H_j,B_j\) are the
local complex recurrences in (6) of `LOCAL_CONTINUATION_SETUP.md`. Choose
\[
\begin{split}
K_{\rm num}=\max\bigg\{&8,
\left\lceil2\log_2\max\{1,16TV/e_d\}\right\rceil,
\left\lceil\log_2\max\{1,8V\widehat R_n/b_n\}\right\rceil,\\
&\left\lceil\log_2\max\{1,
128V\widehat R_nC_{\rm src}n^{3/2}/\varepsilon_v\}\right\rceil,
\left\lceil\log_2\max\{1,64\sqrt nC_g/\varepsilon_v\}\right\rceil
\bigg\}.
\end{split}
\tag{6}
\]
Take
\[
J_{\rm num}=\lceil2T/\widehat R_n\rceil
=\lceil\max\{4T/r_t,16TL_n\}\rceil
\tag{7}
\]
equal physical-time panels. Generate the parameter and passive-source jets to
degree \(K_{\rm num}\) on each panel. Evaluating the source jets anywhere
in their real panel gives Euclidean error at most
\(\varepsilon_v/16<\varepsilon_v\), by (Setup-B.4)--(Setup-B.6).
This statement includes accumulated global parameter error, local parameter
truncation, activation replacement and source-series truncation.

For completeness, the stability mechanism is
\[
E'\le2J^{\rm r}\rho E+\tfrac12(C^{\rm r}+J^{\rm r})^2E^3+\|d\|,
\quad \int_0^\infty\rho\le2Y/\lambda,
\]
where \(E\) is normalized parameter error and \(d\) the continuous
ODE defect. The negative square of the training prediction discrepancy is
used before obtaining this inequality. Under the explicit defect allowance
(4), prefix induction gives \(E\le2e^{A_n}e_d\) and validates every
successive approximate anchor. Thus the exponential amplification is
\(e^{O(\sqrt\ell)}\), rather than a horizon-length Lipschitz exponential.
The local polynomial field still has exactly the original rank-one gradient
equations, so the factored arithmetic proof applies without a new dense
factor.

At fixed problem parameters, if \(\log(1/\varepsilon_v)=O(\ell)\),
these formulas give
\[
J_{\rm num}=O(\ell^{3/2}),\qquad K_{\rm num}=O(\ell),
\qquad D=O(\ell^{3/2}).
\tag{8}
\]
The bounds retain all dimensions, gap, depth, labels and activation envelopes
through (2)--(7) and the cited finite recurrences. No practical or polynomial
joint-parameter width threshold is asserted.

## Taylor source spaces from real nodes: the new bridge

First reduce the input span exactly. Let \(U_0\in\mathbb R^{d\times k}\)
have orthonormal columns spanning the \(M=m+p\) declared normalized inputs,
where \(k\le\min(d,M)\). Use \(U_0^\top v_i\) and
\(W_0^{(1)}U_0\). The reduced inputs have norm one, their Gram is
unchanged, and initialized Gaussian rows remain standard Gaussian. First-layer
updates lie in this span. The original and reduced dense trajectories are
therefore exactly equal on every declared input. This is the same reduction
as in `cp:panel`; it is needed to preserve the stated dependence on \(d\).

Here is a deterministic source partition using only current scalar envelopes.
Put
\[
\nu=\lambda/4,\quad \overline{\mathcal K}=\beta^{14L},\quad
\bar r=\frac{\lambda}{1024\beta^{27L}Y^2\sqrt\ell},\quad
\bar h(t)=\frac{\log(1+2\overline{\mathcal K}\bar r e^{\nu t})}
                        {2\overline{\mathcal K}}.
\]
Starting at \(t_0=0\), use
\[
r_b=4\bar h(t_b)/9,\qquad
t_{b+1}=\min\{T,t_b+r_b/2\}.
\tag{9}
\]
These disks lie in the working finite-panel domain
`cp:src-panel-working`. Indeed its actual constants obey
\(U_{\rm fin}/a\le\beta^{27L}\) and
\(\mathcal K\le\beta^{14L}\). The function
\(K\mapsto\log(1+2Kx)/(2K)\) decreases for \(x>0\), because
\(u/(1+u)\le\log(1+u)\). Thus \(\bar h\le h\).
Its certified radius is \(h/[2(1+d_h)]\), with
\(d_h=\lambda/(8\mathcal K)\le1/8\); hence it is at least
\(4h/9\ge r_b\).

The number \(J_{\rm src}\) of panels in (9) obeys the same bound as the
current public theorem:
\[
J_{\rm src}\le1+\beta^{30L}z^2\sqrt\ell
       +\beta^{16L}\lambda^{-1}\log(1+4\ell/\log2).
\tag{10}
\]
To verify the count directly, \(\bar h'\le1/8\), and each full panel
contributes at least \(8/37>1/5\) to
\(\int dt/\bar h(t)\). Split that integral at
\(2\overline{\mathcal K}\bar r e^{\nu t}=1\). Before the split use
\(\log(1+x)\ge x/2\); afterward its derivative is at least
\(\nu/2\). This gives
\[
J_{\rm src}\le1+5\left[\frac2{\nu\bar r}
 +\frac{4\overline{\mathcal K}}\nu
                   \log(1+\nu T/(2\log2))\right].
\]
Substitution gives coefficients \(40960\beta^{27L}\) and
\(80\beta^{14L}\), bounded respectively by \(\beta^{30L}\) and
\(\beta^{16L}\) for \(\beta\ge10,L\ge2\). The disks have coordinate
source bound \(M_n=\beta^{6L}\sqrt n\).

Choose
\[
K_T=\max\{8,\lceil2\log_2(64M_n/\eta)\rceil\},\qquad
N_{\rm src}=K_T+1,
\quad \varepsilon_v=\frac{\eta}{128N_{\rm src}}.
\tag{11}
\]
Here \(K_T\) is the source interpolation degree, distinct from the
numerical integration degree \(K_{\rm num}\) and the source-envelope
coefficient \(K_{\rm src}=\beta^{21L}\) in (2).

For a panel of length \(h_b=t_{b+1}-t_b\), its \(N_{\rm src}\)
real nodes are
\[
s_{bi}=t_b+\frac{h_b}{2}\left[1+
\cos\frac{(i+1/2)\pi}{N_{\rm src}}\right],
\qquad 0\le i<N_{\rm src}.
\tag{12}
\]
Supply the approximate base-source vectors at these nodes using the common
rollout with tolerance \(\varepsilon_v\). For every vector, form its
initialized matrix image exactly. The generators can be these nodal vectors
themselves; computing or retaining interpolation coefficients is unnecessary.

Here is the full approximation proof. Let \(I_K\) denote interpolation at
the \(K+1\) Chebyshev roots in (12), transported to the panel. Discrete
cosine orthogonality gives constant coefficient
\((K+1)^{-1}\sum_i g_i\) and degree-\(j\) coefficients
\(2(K+1)^{-1}\sum_i g_i\cos[j(i+1/2)\pi/(K+1)]\), \(1\le j\le K\).
Since \(|T_j|\le1\) on the real interval,
\[
\|I_Kg\|_\infty\le(2K+1)\max_i|g_i|
\le2(K+1)\max_i|g_i|.
\tag{13}
\]
The same estimate holds for Euclidean vector norms by the triangle inequality.

For each exact scalar source, its degree-\(K\) Taylor polynomial about
\(t_b\) has error at most \(M_n2^{-K}\), by the certified disk and
\(h_b\le r_b/2\). Interpolation reproduces this polynomial, so
\[
\|g-I_Kg\|_\infty
\le(2K+3)M_n2^{-K}
\le4M_n2^{-K/2}\le\eta/16.
\tag{14}
\]
The middle inequality holds for \(K\ge8\), and the final one is exactly
(11). This argument is applied separately to a base source and its exact
initialized image: no coordinate-to-coordinate matrix norm is assumed.

At an approximate base node the Euclidean error is at most
\(\varepsilon_v\). The initialized hidden matrix and its transpose have
operator norm at most eight. Their nodal-image error is therefore at most
\(8\varepsilon_v\) in Euclidean norm and hence in each coordinate.
By (13), the interpolated image perturbation is at most
\(16N_{\rm src}\varepsilon_v=\eta/8\); the base error is smaller.
Combining with (14), both families have coordinate error below \(\eta\).
Linearity gives the **exact** identity
\(I_K(W_0\widetilde g)=W_0I_K\widetilde g\). The corresponding
transpose identity is identical. Therefore every hypothesis of the current
source-to-runtime transfer holds after adding its exact initialized vectors.

There are \(M\) forward base curves and \(m\) backward base curves per
layer, and at most twice that many curves after including their images.
Writing \(r=\max_j\dim E_j\) and \(q=\max_j|I_j|\) for the actual
selected width, a safe bound is
\[
r\le R:=2m+k+1+2(2m+p)J_{\rm src}N_{\rm src},\qquad q\le9r\le9R.
\tag{15}
\]
The transfer proposition's symbol \(q\) denotes a source-dimension bound;
its application here uses that symbol equal to \(R\). Our \(q\) in (15)
is the actual number of retained coordinates, as in the setup-cost ledger.
If the budget reaches width \(n\), use its exact full-width fallback.

Because \(\log(1/\eta)\le2\ell\) eventually, (11) gives
\(N_{\rm src}\le8\ell\) eventually. Equations (10) and (15), followed
by the current selected inventory, consequently preserve the exact published
parameter order
\[
C(m+p)^2\left[z^4\ell^3+
 \lambda^{-2}\ell^2\{\log(e+\ell)\}^2\right]+C(m+p)d.
\tag{16}
\]
In particular, the label factor \(z^4\) has not been suppressed. The
operator constants and comparison coefficients have no extra dependence on
the passive list length. Passive labels never enter the algorithm.

The source partition, nodal vectors, all source coefficients and the disposable
rollout are discarded after selection. The final model starts at original
time zero with the original activations and the corrected readout in
`cp:selected-readout`; it has no retained time schedule or trajectory oracle.

## Complete Taylor operation and memory ledger

Let \(P_k=(L-1)n^2+n(k+1)\) be the reduced dense parameter count,
\(P_d=(L-1)n^2+n(d+1)\) the supplied count, and
\(N_s=J_{\rm src}N_{\rm src}\) the total temporal nodes. Write
\(K=K_{\rm num}\), \(J=J_{\rm num}\). All quantities below are actual
integers prescribed above; \(R,r,q\) are as in (15).

The factored recurrence for a hidden matrix, with unscaled local coefficients,
is
\[
[W^{(j)}]_s=-\frac2{mns}\sum_a\sum_{i+k'=s-1}
[r_a\delta_a^{(j)}]_i[h_a^{(j-1)}]_{k'}^\top,\qquad s\ge1.
\tag{17}
\]
Its action on a query series can be computed by first caching inner products
of the training feature coefficients with the query coefficients. This costs
\(O(Lm(m+M)K^2(n+K))\) per numerical panel for shared training jets and
all declared input jets. The constant dense matrices act only on \(K+1\)
vectors per query, costing \(O(P_k(m+M)K)\). The matrix endpoint increment
can be grouped into \(mK\) outer products by summing the scalar time weights
against the feature coefficients first. Thus advancing a dense anchor costs
\(O(P_kmK+LnmK^2)\), already absorbed. It does not materialize one dense
matrix for every derivative order.

Each scalar degree-\(D\) activation polynomial costs \(O(DK^2)\)
for online series composition and \(O(DK)\) scratch. Evaluating the source
jets at all nodes costs \(O(LnMKN_s)\). Source vectors themselves can be
stored directly. Exact initialized images still cost dense matrix actions;
these cannot be omitted because a source span is small.

A sufficient total arithmetic bound is
\[
\begin{split}
O\big(&P_d+dM^2+ndk+LD^2+mP_k\\
&+J\{P_k(m+M)K+Lm(m+M)K^2(n+K)
                         +Ln(m+M)DK^2\}\\
&+LnMKN_s+Ln^2R+LnRr+Lnr^3+Lq^2r\\
&+N_s\log(2+N_s)+C_{\rm scalar}\big).
\end{split}
\tag{18}
\]
The first line includes supplied initialization access, input-span reduction,
activation-polynomial coefficients and exact original initialized features.
The third line includes source-image multiplication, source orthogonalization,
the deterministic selector, initialized-mixer assembly and metric formation.
One may separately list two \(Ln^2R\)-type terms for image formation and
final assembly; the displayed bound covers both. The last line sorts/merges
temporal nodes with numerical panels; \(C_{\rm scalar}\) is the finite
scalar-recurrence and node-generation cost from (1)--(12), with elementary
primitive costs charged separately. No integration rejection or oracle
certification step is hidden in it.

The deterministic selector costs \(O(nr^3)\) per layer: orthonormalize the
source list, then perform at most \(9r\) rank-one barrier iterations, each
testing \(n\) rows with \(O(r^2)\) quadratic-form work, alongside small
matrix updates. Its exact metric formula is `cp:metric`. The Gram used there
has eigenvalues in \([1,4]\) after selection. Forming the selected metric
and initialized mixers costs \(O(q^2r+n^2r)\) per layer. These are
arithmetic bounds, without a numerical rank or comparison margin guarantee.

A sufficient peak real-coordinate count is
\[
O\big(P_d+LnmDK+LnMK+LmM K^2+LnR+Lq^2
        +LD+N_s+J+Md+dk\big).
\tag{19}
\]
One may process the \(M\) passive source jets one at a time to lower the
\(LnMK\) term. The bound safely allows it. Only a current dense anchor,
initialized dense arrays, current-panel jets and source generators are live;
neither \(JP_k\) anchors nor \(JKP_k\) dense jets are stored.

There are additionally \(O(LD+Lmn)\) original real activation-value calls.
Only the \(O(LD)\) calls constructing the disposable polynomial may use its
finite tolerance from (5); exact initialized training additions use the
original real-arithmetic primitive. There are no high-derivative calls during
setup. If the initialization is freshly sampled, add
\(nd+(L-1)n^2\) Gaussian draws and their generation work/scratch. For a
supplied dense realization those draws are omitted. Runtime still needs the
original activation and first derivative.

At fixed admissible parameters, (10)--(11) give
\(N_s,R,r,q=O(\ell^{3/2})\), while (8) gives the numerical orders.
The terms proportional to \(n^2\) in (18) are at most
\(O(n^2\ell^{5/2})\). The largest displayed term proportional to \(n\)
is the activation composition term \(O(n\ell^5)\); the selector is
\(O(n\ell^{9/2})\). Equation (19) is \(O(n^2)\) eventually. This
proves the Taylor row, including all setup stages.

## Harmonic transfer and its quadrature dimensions

Harmonic uses the same backend with the current \(T,\eta\) and radii
\(r_t\) in (2), \(r_q=1/[\beta^{3L}\sqrt{(d+3)\ell}]\), and
\(M_n=\beta^{6L}\sqrt n\). Its already proved positive quadrature and
streamed coefficient assembly apply to these radii without a change of source
space dimension. Their proofs are in the allowed setup document's complete
“Positive coefficient quadrature” and “Streamed explicit assembly” sections.

To make the orders auditable, for \(d\ge2\) put
\[
\alpha=r_t/(4T),\quad b_d=2d-2,\quad D_d=2^{d+1}d^{d-2},\quad
P_T=18D_db_d!2^{b_d+1}/(\alpha r_q^{b_d+1}),
\]
\[
H_*=2\log(16M_nP_T/\eta),\quad
p_t=\lfloor H_*/\alpha\rfloor,\quad
j_*=\lfloor H_*/r_q\rfloor,
\]
\[
h_j={j+d-1\choose d-1}-{j+d-3\choose d-1},\quad
N=\sum_{j=0}^{j_*}h_j\left(1+\left\lfloor
                              \frac{H_*-r_qj}\alpha\right\rfloor\right),
\quad H_{\rm sph}=\sum_{j=0}^{j_*}h_j.
\tag{20}
\]
Then \(R=2m+d+1+4N\) and the actual selected width satisfies \(q\le9R\).
The positive-quadrature prescription uses
\[
a_t=\alpha/2,\quad h_{\rm ang}=r_q/[2(d-1)],\quad
\sigma=\operatorname{arsinh}(2h_{\rm ang}/\pi),\quad
\mathcal Y=\max_{j\le j_*}\sqrt{h_j},
\]
\[
A_d=\prod_{b=1}^{d-2}\frac{\pi}{\int_0^\pi\sin^b u\,du},\quad
B_{\rm int}=2M_n\mathcal Y A_d
e^{a_tp_t+j_*(d-1)h_{\rm ang}}
(\cosh h_{\rm ang})^{(d-2)(d-1)/2},
\]
\[
\epsilon_c=\eta/(16N\mathcal Y),\qquad
\delta_{\rm node}=\eta/(64NA_d\mathcal Y^2),
\]
\[
N_t=\max\{1,\lceil a_t^{-1}\log(1+4dB_{\rm int}/\epsilon_c)\rceil\},
\quad
N_\varphi=\max\{1,\lceil h_{\rm ang}^{-1}
                         \log(1+4dB_{\rm int}/\epsilon_c)\rceil\},
\]
\[
N_\theta=\max\{1,\lceil\sigma^{-1}
\log[8dB_{\rm int}/(\epsilon_c(1-e^{-\sigma}))]\rceil\},
\quad N_x=N_\varphi N_\theta^{d-2}\quad(d\ge3).
\tag{21}
\]
For \(d=2\), \(A_d=1\), \(N_x=N_\varphi\), and there is no polar
rule. For \(d=1\), use two inputs, no spherical degree, and the explicit
two-point prescription in `SETUP_INTEGRATION_ORDERS.md`, with
\(N_1=1+\lfloor\alpha^{-1}\log[64M_n/(\alpha\eta)]\rfloor\),
\(R=2m+d+1+8N_1\), and \(\delta_{\rm node}=\eta/(64N_1)\).
The normalization of positive and zero time modes is respectively two and one.
There is no assumption that quadrature counts equal basis counts.

Use the source-jet bridge with its requested \(\delta_{\rm node}\) from
(21). Its Euclidean source guarantee leaves the necessary factor-eight budget
for initialized images. Accumulate **global** time--sphere coefficients from
all numerical panels, then form initialized images exactly. Do not retain a
separate harmonic source block for every numerical integration panel.

The complete supplied-order arithmetic and memory are (Setup-B.8)--(Setup-B.9)
of `SETUP_INTEGRATION_PROOFS.md`, with (20)--(21) and (2)--(8) substituted.
They explicitly contain passive source construction, quadrature projection,
\(Ln^2N\) initialized images, \(LnRr+Lnr^3+Ln^2r+Lq^2r\) selection
and assembly, evaluator work, and geometry tables. At fixed parameters,
\[
p_t+1,N_t=O(\ell^{5/2}),\quad j_*=O(\ell^{3/2}),\quad
N_x,H_{\rm sph}=O(\ell^{3(d-1)/2}),\quad
N,R,r,q=O(\ell^{3d/2+1}).
\tag{22}
\]
The resulting work is
\(O(n^2\ell^{3d/2+1}+n\ell^{9d/2+3}+\operatorname{polylog}(n))\)
and peak memory is \(O(n^2)\). The present \(\eta\) still has logarithmic
inverse accuracy, so the proof of those orders is unchanged. Since the computed
coefficient spaces satisfy the **current** transfer theorem, its current
Harmonic retained count and \(Y/n\) guarantee follow.

The separately proved implicit-Gaussian Harmonic algorithm is not needed for
this supplied-dense result. Its fresh coupled Gaussian reference cannot be
presented as a subquadratic conversion of a supplied dense realization.

## Numerical perturbations: what transfers and what remains open

There are three distinct perturbation questions.

1. **Inexact rollout and approximate source generators:** handled above. The
   selected space is the span of the actually computed generators, so its
   exact metric preserves that span. The proof uses a worst-case generator
   count, not preservation of an accidental rank deficiency. No perturbation
   theorem comparing two old and new projectors is needed.
2. **Exact initialized additions and exact metric/mixer construction:** still
   exact-real operations. They preserve the initialized training Gram and
   the initialized actions required by the current fitting theorem. Replacing
   these additions by approximate values without a new quantitative argument
   would fail to verify an actual hypothesis. Finite source-value tolerance
   alone does not resolve this issue.
3. **Finite-word execution:** unresolved. Although the source polynomial and
   rollout tolerances are polynomially small at fixed parameters, this does
   not bound the bits needed by source rank detection, orthogonalization,
   barrier comparisons, or selected weights. The metric's generalized bounds
   \(D/4\preceq M\preceq D\) and \(I\preceq P^\top DP\preceq4I\)
   do not bound the condition number of \(D\) in ordinary coordinates.
   Small singular values of a source generator matrix are likewise not
   excluded by the analytic source event. No uniform rank gap or selector
   decision margin has been proved. A finite-word theorem must also analyze
   the changed selected initial Gram, mixer/image defects and any numerical
   error in the corrected-readout Gram solve and infinite-time evolution.

Thus there is a rigorous efficient real-arithmetic initializer for both
current methods. The current hypotheses do not yet yield a finite-bit setup
and runtime theorem with the same all-time guarantee. Analyticity alone also
does not supply an algorithm for evaluating an arbitrary activation; every
concrete evaluator's description, work and scratch remain additional costs.

For ordinary dense Euler with physical step \(h\), work on this horizon is
\(\Theta(mP_dT/h)\) under the same scalar convention. Taylor setup divided
by this benchmark is \(O(h\ell^{3/2})\) at fixed parameters; Harmonic's
ratio is \(O(h\ell^{3d/2})\). Both tend to zero for any fixed inverse-
polynomial \(h=n^{-\alpha}\), \(\alpha>0\). This comparison does not
prove that Euler requires such a step, or that setup beats a high-order dense
solver using the same continuation method.
