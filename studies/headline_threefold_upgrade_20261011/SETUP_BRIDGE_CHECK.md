# Scoped check of the Taylor real-node setup bridge

2026-10-11. Assignment: check the new Taylor source-span bridge and its
operation/memory accounting in `SETUP_UPGRADE.md`, without importing the
unassigned numerical-setup dependency packet. Only this report is written.

**Verdict:** the new deterministic Taylor bridge, its source tolerance and
rank accounting, and the stated arithmetic/memory ledger are valid under
the explicitly supplied numerical source-value guarantee. I found no
rank/count error requiring a change. This is not an independent validation
of the inherited rollout backend, the Harmonic quadrature backend, or a
finite-word implementation theorem.

## Scope and fixed input

The checked draft is `SETUP_UPGRADE.md`, SHA-256
`71734813774f8d49d6184f390e94542674cd39bcde102afca5af7f5928aec993`.
The relevant current proofs are `cp:src-panel-working` and `cp:source` in
`paper/compact_foundations.tex`, and `cp:selection`, `cp:selected`,
`cp:metric`, and `cp:panel` in `paper/compact_selected.tex`. These modules
were read directly. Required rigorous-math and canonical/neural notation
skills were applied. No other setup-study files were read.

Retain the current network and physical gradient flow, analytic activation
assumptions, Gaussian initialization, zero readout, and label cap. Write
\(\lambda=\gamma/m\le1\), \(z=Y/\lambda\),
\(\ell=\log(en)\), \(T=32\ell/\lambda\), and \(M=m+p\) for
the declared panel size. Its input span has dimension
\(k\le\min(d,M)\). The current source theorem supplies coordinate
bound \(M_n=\beta^{6L}\sqrt n\) on the certified analytic disks.
All eventual-width qualifications remain in force.

The inherited backend input needed for this check is precise: one
disposable dense rollout returns every requested base-source value with
Euclidean error at most \(\varepsilon_v\), on the current fitting/source
event, using numerical orders
\(J_{\rm num}=O(\ell^{3/2})\),
\(K_{\rm num}=O(\ell)\), and activation-polynomial degree
\(D=O(\ell^{3/2})\) when
\(\log(1/\varepsilon_v)=O(\ell)\). Its finite recipe and costs are
the draft's (2)--(8). The conclusions below are conditional on this
input, whose independent status is specified at the end.

## 1. The source partition is certified and has the advertised count

The actual working finite-panel radius is
\(r=\lambda/[1024Y^2(U_{\rm fin}/a)\sqrt\ell]\).
Since \(U_{\rm fin}/a\le\beta^{27L}\), the draft's
\(\bar r=\lambda/(1024\beta^{27L}Y^2\sqrt\ell)\) is no larger.
For positive \(x\),

\[
\frac{d}{dK}\frac{\log(1+2Kx)}{2K}
=\frac{2Kx/(1+2Kx)-\log(1+2Kx)}{2K^2}\le0.
\]

Thus replacing the actual \(\mathcal K\) by
\(\overline{\mathcal K}=\beta^{14L}\ge\mathcal K\) and the
actual radius by \(\bar r\) produces \(\bar h(t)\le h(t)\).
The actual certified disk radius is
\(h(t)/[2(1+d_h)]\), where \(d_h=\lambda/(8\mathcal K)\le1/8\).
It is at least \(4h(t)/9\), proving containment of every proposed disk
\(r_b=4\bar h(t_b)/9\).

The partition step is \(2\bar h(t_b)/9\). Since
\(0\le\bar h'\le1/8\), on a full panel
\(\bar h(t)\le(37/36)\bar h(t_b)\), and therefore

\[
\int_{t_b}^{t_{b+1}}\frac{dt}{\bar h(t)}\ge\frac8{37}>\frac15.
\]

The draft's split of the integral at
\(2\overline{\mathcal K}\bar r e^{\lambda t/4}=1\) is valid even
when the split lies outside the interval. It yields

\[
J_{\rm src}\le1+40960\beta^{27L}z^2\sqrt\ell
+80\beta^{14L}\lambda^{-1}\log(1+4\ell/\log2).
\]

At \(\beta\ge10,L\ge2\),
\(40960\le\beta^{3L}\) and \(80\le\beta^{2L}\), proving
the draft's (10) with precisely the current parameter powers. No later
dense state is used to choose this partition.

## 2. Real-node interpolation meets the full source contract

Let \(K=K_T\ge8\), \(N=K+1\), and \(I_K\) be interpolation
at the transported Chebyshev roots in a source panel. Its discrete cosine
coefficients give

\[
\|I_Kg\|_\infty\le(2K+1)\max_i|g(s_i)|\le2N\max_i|g(s_i)|.
\tag{A}
\]

The same calculation holds for Euclidean vector norms. No sharp Lebesgue
constant is needed.

For an exact coordinate source, Cauchy's coefficient bound on the disk
and panel length at most half its radius give a degree-\(K\) Taylor
polynomial \(p\) with \(\|g-p\|_\infty\le M_n2^{-K}\).
Since \(I_Kp=p\),

\[
\|g-I_Kg\|_\infty
\le(2K+2)M_n2^{-K}
\le(2K+3)M_n2^{-K}
\le4M_n2^{-K/2}\le\eta/16.
\tag{B}
\]

The last inequality uses the prescribed
\(K_T\ge2\log_2(64M_n/\eta)\). This proof applies separately
to each exact base source and to its exact initialized image, because
both have the coordinate bound \(M_n\). Multiplication of a coordinate
tail by a dense matrix is not assumed to preserve coordinate norm.

Let an approximate base vector at each node have Euclidean error at most
\(\varepsilon_v=\eta/(128N)\). The initialized hidden matrix and its
transpose have operator norm at most eight on the fitting event. Hence
their paired nodal images have Euclidean error at most
\(8\varepsilon_v\). Formula (A) bounds the interpolated perturbations
by \(\eta/64\) for the base and \(\eta/8\) for the image. Each
coordinate has no larger error. Adding (B) leaves both strictly below
the required \(\eta\).

Using the same scalar interpolation weights for a base and its image
gives exactly

\[
I_K(W_0\widetilde g)=W_0I_K\widetilde g,
\qquad
I_K(W_0^\top\widetilde g)=W_0^\top I_K\widetilde g.
\]

Thus the source contract's exact initialized-image pairing is met.
The generators can indeed be the nodal vectors themselves: every
interpolant is a linear combination of them. Adding the constant,
the required exact initialized training features and images, and the
first-layer columns supplies the remaining `cp:selected` hypotheses.
Different panel interpolants need not match at boundaries because that
theorem uses their values and uniform errors, not their derivatives.

The selected tolerance
\(\eta=\min(1,Y,S,Y/(2n\mathcal A_n))\) respects all source
constraints and gives finite-horizon error at most \(Y/(2n)\).
The separately imposed endpoint-tail gate then gives the required
complete-trajectory \(Y/n\) estimate. This proof preserves the current
corrected optimizer; source generators are discarded before its evolution.

## 3. Rank and retained-storage accounting

At each layer there are \(M\) forward and \(m\) backward base
curves, hence at most \(2(M+m)=2(2m+p)\) curves after adjoining
initialized images. Each contributes at most
\(J_{\rm src}N_{\rm src}\) generators. Consequently

\[
\max_j\dim E_j\le
R=2m+k+1+2(2m+p)J_{\rm src}N_{\rm src}.
\tag{C}
\]

This counts the stored **span**, not a collection of independent runtime
models, one per panel. The source rank and selected width are distinct;
exact-metric selection gives at most nine times the actual rank.

Because \(\log(1/\eta)\le2\ell\) eventually and
\(\log M_n=\tfrac12\log n+6L\log\beta\),

\[
N_{\rm src}\le\frac5{\log2}\ell+O_{\rm problem}(1)<8\ell
\]

eventually. Combine this with the verified partition bound and
\(k\le M\). Squaring (C) and absorbing the constant and plain
\(\ell^2\) terms into \(\lambda^{-2}\ell^2\log(e+\ell)^2\)
gives

\[
R^2\le C M^2\left[z^4\ell^3+
\lambda^{-2}\ell^2\{\log(e+\ell)\}^2\right],
\]

with activation/depth-only \(C\). The existing selected inventory and
input-span map add only \(CMd\). Thus the draft preserves the full
published retained-storage dependence, including \(z^4\), rather than
only its fixed-parameter \(O(\ell^3)\) shorthand. The eventual gate may
depend on \(Y\), confidence, and the other fixed parameters.

The full-width fallback is valid on the fitting event but costs dense
storage. It does not turn the displayed polylogarithmic count into an
all-width assertion.

## 4. Arithmetic and peak-memory ledger

The draft correctly charges dense initialized-image multiplications.
They cannot be recovered for free from small source rank. The terms
\(Ln^2R\) cover these products and, up to a numerical factor, the
later initialized mixer products. Source orthogonalization costs
\(O(LnRr)\) for actual rank \(r\le\min(n,R)\).

The stated factored-jet cost does not require materializing a dense
matrix for every Taylor coefficient. To check the potentially problematic
cubic sum, write \(u_{a,i}=[r_a\delta_a]_i\) and \(v_{a,j}=[h_a]_j\).
The action of a hidden increment on query coefficient \(h_{b,t}\)
contains sums of

\[
\frac{u_{a,i}\langle v_{a,j},h_{b,t}\rangle}{i+j+1},
\qquad i+j+t+1=s.
\]

Cache the \(O(K^2)\) inner products per driver/query pair in
\(O(nK^2)\) work, combine their scalar time weights in \(O(K^3)\),
and only then form the \(O(K^2)\) vector combinations in
\(O(nK^2)\). This gives the stated
\(O(Lm(m+M)K^2(n+K))\) cost, not \(O(nK^3)\) for each pair.
The transpose actions obey the same grouping. Endpoint increments group
into \(mK\) outer products, with the scalar weights summed first.

Other components of (18) are accounted for as follows:

| Stage | Sufficient arithmetic |
|---|---:|
| Supplied arrays and input-span reduction | \(P_d+dM^2+ndk\) |
| Exact initialized training additions | \(mP_k\), plus \(O(Lmn)\) original value calls |
| Activation polynomial and series compositions | \(LD^2+JLn(m+M)DK^2\), plus \(O(LD)\) original value calls |
| Constant dense actions in the rollout | \(JP_k(m+M)K\) |
| Evaluate source jets at all requested nodes | \(LnMKN_s\) |
| Form initialized images, orthogonalize, select, assemble | \(Ln^2R+LnRr+Lnr^3+Lq^2r\) |
| Temporal scheduling | \(N_s\log(2+N_s)\), with scalar generation charged separately |

For the selector, at most \(9r\) iterations test \(n\) rows using
\(O(r^2)\) quadratic-form work each. Even recomputing the shifted small
matrix inverses costs at most \(O(r^4)\), absorbed by \(O(nr^3)\)
because \(r\le n\). The metric construction costs \(O(q^2r)\).
An initialized mixer can be formed in \(O(n^2r+q^2r)\), including its
intermediate basis products; \(r\le n\) and \(q\ge r\) absorb those
products. Exact rank decisions and exact comparisons are part of this
real-arithmetic accounting; no numerical rank margin is inferred.

The peak-memory bound (19) is achievable by computing the training jets
jointly and evaluating the remaining declared inputs one at a time.
Its \(LnmDK\) term then pays activation-composition scratch;
\(LnMK\) safely pays stored source jets; and \(LmMK^2\) pays cached
pairings. Initialized arrays, one current anchor, \(LnR\) source
generators/bases, and \(Lq^2\) selected matrices suffice. Source times
and numerical panel endpoints account for \(N_s+J\). No entire sequence
of dense anchors or dense matrix jets need be stored. This streaming
schedule matters: allocating composition scratch for all passive inputs
simultaneously would require the larger \(LnMDK\) term.

At fixed admissible parameters the orders are
\(J=O(\ell^{3/2})\), \(K=O(\ell)\),
\(D=O(\ell^{3/2})\), and
\(N_s,R,r,q=O(\ell^{3/2})\). The largest quadratic-in-width
term is \(n^2JK=O(n^2\ell^{5/2})\). The largest displayed
linear-in-width term is composition,
\(nJDK^2=O(n\ell^5)\); selection costs
\(O(n\ell^{9/2})\). This proves the detailed Taylor work bound
in the draft, given the backend orders. The peak is
\(O(n^2+n\ell^{5/2}+\operatorname{polylog}n)=O(n^2)\) eventually.
These simplifications are fixed-parameter statements and are not uniform
joint-parameter bounds.

## 5. What remains outside this check

The new bridge needs only accurate real source values. Its proof does not
itself prove that the numerical rollout supplies those values. In particular,
independent validation would need the complete files named by the draft:

- `LOCAL_CONTINUATION_SETUP.md`: restart-tube recurrences, signed
  defect stability, and explicit accumulated parameter error.
- `SETUP_INTEGRATION_PROOFS.md`: the real-value activation backend,
  source-jet compatibility and the precise source-value error bound,
  including all numerical backend costs.
- `SETUP_INTEGRATION_ORDERS.md`: the finite prescription of numerical
  orders and backend tolerances.

These were not assigned and were not fetched. The current paper supplies
the analytic disks, source envelopes, and source-to-runtime transfer, but
does not supply those numerical integration lemmas. Thus this report
certifies the new Taylor bridge and ledger conditional on the stated
backend, not the full efficient-setup theorem unconditionally.

The Harmonic quadrature section is inherited rather than a new Taylor
bridge and was not independently certified here. Finite-word precision,
rank stability, selector decision margins, and numerical execution of the
final all-time optimizer also remain outside the proved claim, as the
draft explicitly states. No empirical tests are needed for these exact
algebraic and counting checks.

Receiving proof hashes: `compact_foundations.tex`
`6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0`;
`compact_selected.tex`
`3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885`.
