# Complete local Taylor, activation and streamed-assembly interface

2026-10-06. Root synthesis after the three components were frozen and read
completely. The Taylor author supplied the integration observation; the root
reconstructed the four-term error allocation below. This is not a claim that
the unamended component interfaces were identical.

Scientific inputs and frozen hashes:

- `LOCAL_CONTINUATION_SETUP.md`:
  `c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe`.
- `LOCAL_ACTIVATION_BACKEND.md`:
  `cbf26326c081fc19da31f5d38781eff2dfa2a5b97dee12eb1a8022770a2843e4`
  (explicit-log notation cleanup of the originally reviewed
  `25e8c6dd6381d46b561a839339d538ea38926f4130af62dfb848f91cc6f54cbb`).
- `LOCAL_CONTINUATION_ASSEMBLY.md`:
  `488216678b1ea31fcfb8da5f396c8323eae3a38be067c2e431de21a600df2fe2`.
- `RESULT.md` and the prior quadrature/stability notes cited in those
  components, at their recorded hashes. No other study was used.

## 1. Precision and source-jet compatibility

Let \(\delta_{\rm node}>0\) be the global quadrature's coordinate-error
allowance. It is defined in assembly equation (3), with its separate
dimension-one convention. Run the polynomial-activation backend with the
stricter requested nodal tolerance

\[
\tau=\frac{\delta_{\rm node}}{32\sqrt n}.
\tag{1}
\]

All its scalar approximation and global defect budgets use this \(\tau\)
in place of its local symbol \(\delta_{\rm node}\). Let
\(\widehat R_n,V,C_{\rm src}\) be the explicit radius, velocity and
original-source comparison coefficient of that backend and the core note.
Set

\[
C_g=\max_j\{H_j+1,B_j+1\},
\tag{2}
\]

where \(H_j,B_j\) are the core's complex forward-feature and backward
response RMS bounds. Increase the backend's training Taylor degree, if
necessary, to the maximum of its equation (A22) and

\[
\left\lceil\log_2\max\left\{1,
 \frac{128V\widehat R_n C_{\rm src}n^{3/2}}{\delta_{\rm node}}
 \right\}\right\rceil,
\qquad
\left\lceil\log_2\max\left\{1,
 \frac{64\sqrt n C_g}{\delta_{\rm node}}
 \right\}\right\rceil.
\tag{3}
\]

Use that same degree \(K\) for training and passive sources. Increasing it
preserves the previous tail/defect inequalities. All additional inverse
tolerances have logarithm \(O(\log(en))\) in the polynomial-accuracy
regime, so \(K=O(\log(en))\) is unchanged.

To verify the assembly's Euclidean error interface, consider one panel and
one passive real unit query. Write \(v\) for the exact local solution of
the polynomial-activation setup field, \(p\) for its computed degree-\(K\)
parameter Taylor polynomial, and \(g_K\) for the degree-\(K\) Taylor
polynomial of a base source \(h^{(j)}\) or \(\delta^{(j)}\) along
\(v\), using the setup activations. Denote original and setup activation
evaluation by \(g^0\) and \(g^p\), respectively. The desired source is
\(g^0(\theta(t))\), on the original dense trajectory.

On the local complex disk, both original feature and response RMS are
bounded by \(H_j,B_j\). The activation replacement estimate applies
there at each fixed real query: every original carrier has RMS bounded by
the core coefficient, hence coordinate maximum at most \(\sqrt n\)
times that coefficient, exactly as used in backend equations (A15), (A24).
Equation (A25) with (1) makes the additional source RMS smaller than one.
Thus \(\|g^p(v)\|_2\le\sqrt n C_g\) throughout the complex disk.
Vector-valued Cauchy and the half-radius panel give

\[
\|g_K-g^p(v)\|_2\le\sqrt n C_g2^{-K}
                         \le\delta_{\rm node}/64.
\tag{4}
\]

The remaining differences are split before estimating:

\[
g_K-g^0(\theta)
=[g_K-g^p(v)]+[g^p(v)-g^0(v)]
 +[g^0(v)-g^0(p)]+[g^0(p)-g^0(\theta)].
\tag{5}
\]

The second term has each coordinate at most \(\tau/2\), by backend
(A24)--(A25); its Euclidean norm is therefore at most
\(\sqrt n\tau/2=\delta_{\rm node}/64\).

For the third term the original-source comparison gives a coordinate
bound \(C_{\rm src}n\|v-p\|_2\). It applies to these two real states:
both remain within the core's real operator/readout neighborhood, and its
passive-query proof uses only those caps and the RMS-to-coordinate estimate,
not a probabilistic maximum for the perturbed state. The Taylor tail gives
\(\|v-p\|_2\le2V\widehat R_n2^{-K}\). Conversion to Euclidean norm
and (3) thus give at most \(\delta_{\rm node}/64\).

For the fourth term the backend's global estimate (A23), with tolerance
\(\tau\), gives original-source coordinate error at most \(\tau/2\).
Its Euclidean norm is again at most \(\delta_{\rm node}/64\).
Combining the four terms proves

\[
\|g_K-g^0(\theta)\|_2\le\delta_{\rm node}/16
                              <\delta_{\rm node}/8.
\tag{6}
\]

This is precisely the stronger nodal interface needed for assembly (5).
It permits forming initialized-matrix image coefficients only after global
accumulation: their coordinate error is bounded by eight times the base
Euclidean error. The two computed members satisfy the exact pairing by
linearity, while their error is measured against their own original analytic
source functions. The unchanged quadrature and source-tail allocation then
gives source-coordinate approximation below the original tolerance \(\eta\).

## 2. Why the factored execution still applies

The assembly's original statement names Taylor jets of the actual dense
field \(F\). Here they are jets of the certified disposable field
\(\widetilde F\), with activations \(\psi_j\). This is an explicit
interface replacement, justified by (6) and the following exact identity.

The polynomial-activation system has the same rank-one gradient equations,
loss normalization and mobilities; only its scalar activation functions are
different. Coefficient comparison therefore gives the identical equations
(15)--(20) of the assembly note, using its actual residuals, responses and
features. The cached action formula and grouped dense-anchor advancement
remain exact for those jets. The proof of their arithmetic count uses only
these finite sums, not a special activation or zero readout at a restart.
There is no extra dense matrix factor hidden in changing \(F\) to
\(\widetilde F\).

For one scalar degree-\(D\) polynomial \(\psi\), the Chebyshev
recurrence is linear in a product by the scalar input series. At time order
\(k\), computing every recurrence index in increasing polynomial degree
uses already known lower time coefficients and the just computed order-\(k\)
coefficients at the preceding recurrence indices. Each product costs
\(O(k+1)\); there are \(O(D)\) such indices. Summing over
\(0\le k\le K\) gives \(O(DK^2)\) work and \(O(DK)\)
sufficient persistent words. Preparing \(\psi'\) costs \(O(D^2)\)
once and its series composition has the same bound. Thus both online
training and offline passive-query backend costs satisfy

\[
a_{\rm on}(K),a_{\rm off}(K)=O(DK^2),\qquad
b_{\rm on}(K),b_{\rm off}(K)=O(DK).
\tag{7}
\]

The exact original initialized features and their images must be computed
separately using \(\phi_j\), as prescribed by the backend. They must not
be replaced by the constant-order \(\psi_j\) features. This costs
\(O(mP)\) arithmetic and \(O(Lmn)\) original value calls and restores
the exact initialized Gram and action conditions. The final compressed
network uses the original activations and optimizer at original time zero;
neither the last dense anchor nor the setup polynomials survive as runtime
state.

## 3. Complete costs and headline specialization

Use the supplied internal counts and geometry from the assembly note.
Let \(J\) be the number of local panels in this section. Its complete
time envelope (24) and memory envelope (25) apply after the substitutions
(7), with the following explicit additions and qualifications:

- Add \(O(LD^2+mP)\) arithmetic for the polynomial backend and exact
  original initialized features, and \(O(LD)\) polynomial coefficient words.
- Add \(O(LD+Lmn)\) original real activation-value calls. There are no
  high derivative, original first-derivative, complex activation or
  trained-reference oracles. The activation-value precision allowed by
  backend (A10) is polynomially small in width in this regime.
- Panel counts, degrees and tolerances are explicit scalar formulas in
  the backend and (1)--(3). Their evaluation fits its displayed scalar
  preprocessing. There are no adaptive rejections, implicit nonlinear
  solves or uncharged certification runs; take the assembly's
  \(C_{\rm cert},M_{\rm cert}\) to be this elementary scalar overhead.
- Fresh initialization adds the original Gaussian draws and sampler costs.
  All arithmetic counts otherwise have numerical, implementation-only
  big-O constants. Finite precision, numerical rank reliability and bit
  complexity are not implied by these exact-real counts.

In particular, with spatial-first projection, a sufficient complete
non-activation bound is

\[
\begin{split}
O\big(&P+LD^2+mP
 +JP(m+N_x)K+JLm(m+N_x)K^2(n+K)\\
 &+JLn(m+N_x)DK^2+(N_t+J)(p+1)K\\
 &+LnJK(N_xH_{\rm sph}+N)+Ln^2N\\
 &+LnRr+Lnr^3+Ln^2r+Lq^2r
 +G_{\rm time}+N_t\log(2+N_t)\big),
\end{split}
\tag{8}
\]

where \(P=(L-1)n^2+n(d+1)\). A sufficient peak count in real words is

\[
\begin{split}
O\big(&P+LmnDK+Lm^2K^2+LnR+Lq^2+LnKH_{\rm sph}+LD\\
 &+(p+1)K+N_t+J+m(d+1)+G_{\rm memory}\big).
\end{split}
\tag{9}
\]

The quadrature geometry terms in these formulas are the explicitly specified
recomputed-per-panel or cached choice in the assembly note; the chosen time
and memory versions must be used together. No source or dense trajectory
array is retained after selection.

For each separately fixed admissible dataset, depth, activation, positive
label size and confidence, at the original source tolerance \(1/n\) and
horizon \(32(m/\gamma)\log(en)\), the certified choices satisfy

\[
D=O(\log(en)^{3/2}),\quad K=O(\log(en)),\quad
J=O(\log(en)^{3/2}),
\]
\[
N_t,p+1=O(\log(en)^{5/2}),\quad
N_x,H_{\rm sph}=O(\log(en)^{3(d-1)/2}),\quad
N,R,r=O(\log(en)^{3d/2+1}).
\tag{10}
\]

Use the assembly's two-point conventions at \(d=1\). With actual selected
width \(q=O(R)\), every term of (8) is bounded by

\[
O\!\left(n^2\log(en)^{3d/2+1}
             +n\log(en)^{9d/2+3}+\operatorname{polylog}(n)\right).
\tag{11}
\]

For example the new activation arithmetic is at most
\(n\log(en)^{3d/2+7/2}\), which is bounded by the second term for
every fixed integer \(d\ge1\). The \(n^2\) terms include source-image
formation and initialized mixer assembly, not merely the dense integrator.
The \(n\)-proportional terms are eventually smaller than the displayed
quadratic term, giving the convenient headline

\[
\text{setup work}=O\!\left(n^2\log(en)^{3d/2+1}\right),\qquad
\text{peak setup memory}=O(n^2).
\tag{12}
\]

Both statements are at fixed admissible structural parameters. The explicit
separate \(m,d,L\), order and source-radius dependence is in (8)--(10)
and the backend's degree/step formulas; it has not been identified or
discarded. Bounded-cost scalar evaluations and Gaussian sampling, or a
supplied initialization for the latter, are required to include those
costs inside the work shorthand in (12); otherwise add their exposed costs.
At \(d=1\), (12) has logarithmic exponent \(5/2\).

The original whole-sphere/all-time error and retained inventory are unchanged:
source approximation is below \(1/n\), so the original comparison gives
\(n^{-1+o(1)}\) error and \(O(\log(en)^{3d+2})\) retained words.
No statement of optimality among all setup algorithms or finite-precision
implementations follows from these sufficient bounds.

For ordinary dense Euler at physical step \(h\), full source horizon
\(T=32(m/\gamma)\log(en)\), and the same scalar-cost convention, the
work is \(\Theta(mPT/h)\). At fixed parameters the setup/Euler ratio is
therefore at most

\[
O\!\left(h\log(en)^{3d/2}\right).
\tag{13}
\]

In particular \(h=n^{-1/2}\) gives a ratio tending to zero, and the
same holds for every fixed inverse-polynomial step. This comparison does
not assert that such an Euler step is necessary or sufficient for a
particular numerical accuracy. The construction may cost more than a dense
solver using the same high-order continuation, which omits source sampling
and compression assembly. It meets the user's clarified Euler benchmark,
not a lower-bound separation from all dense training methods.
