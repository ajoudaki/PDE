# Factoring the finite-source width gate

2026-10-07. Scoped author arithmetic refinement. This note factors the
width conditions in `FULL_FINITE_SOURCE_PROBABILITY.md` and its checked
local interfaces. It does not reconstruct the underlying scalar insertion
trace or independent-cavity probability argument, change the model, or
constitute an independent review. No experiment, Git mutation, promotion,
or write to another file was performed.

The existing source proof can use the factorized sufficient condition
(4) below. A simpler, weaker consequence is to replace its outer power
20,000 by 1,100, leaving its inner coefficient and moment order unchanged.
The improvement is logarithm and probability bookkeeping; no better
insertion estimate is asserted.

The separate bounded reconstruction is recorded in
`WIDTH_GATE_REFINEMENT_CHECK.md`. The current combined word-cost and
confidence interface is `STREAMLINED_METHOD_RESULT.md`.

## 1. Setup and claim boundary

Keep the network, independent Gaussian initialization, zero readout,
physical gradient flow, activation class, and complete original intersection
of upper label conditions of `FULL_FINITE_SOURCE_PROBABILITY.md`, Section 1.
Here \(n\) is width, \(m\ge d\ge1\), \(L\ge2\),

\[
 \lambda=\gamma/m>0,\qquad Y=\|y\|_2/\sqrt m,\qquad
 S=16Y/\lambda,\qquad \ell=\log(en),
\]

and the original half-strip envelope satisfies \(\beta\ge10\).
For positive labels all estimates use the original allowance

\[
 Y\le\lambda/(8H\sqrt F),\qquad S\le S_*^{\rm src},
\]

with the original recurrence-defined \(H,F,S_*^{\rm src}\). No replacement
power cap, moment-dependent label cap, or positive lower bound on \(Y\)
is imposed. At \(Y=0\), use the stationary zero predictor and initialization
estimates directly, without a barred variable.

Let \(0<\rho<1/4\) be the failure allocation for this one source theorem.
Define exactly as before

\[
 p=\max\left\{1,\left\lceil
 \frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\},
 \qquad Q=m+d+p+1,
\tag{1}
\]

\[
 \mathcal A=\beta^{2000L}(1+\lambda^{-1})^4Q^4.
\tag{2}
\]

The time rectangle and its physical half-width remain

\[
 [-r_t,32\ell/\lambda+r_t]+i[-r_t,r_t],\qquad
 r_t=[p\beta^{100L}(1+\lambda)\sqrt\ell]^{-1}.
\tag{3}
\]

The retained scientific inputs are the stated deterministic source bounds,
local Taylor estimates, response-map and interpolation bounds, scalar
trace estimates, and stopped Gaussian moment estimates in the assigned
source packet. This note audits the *width inequalities used to combine
those inputs*. A new proof of their scientific premises is outside its
scope. In particular, the earlier independent PASS is not used as a
substitute for the gate calculations below.

## 2. A factorized sufficient gate and its power envelope

Put \(u=\log(2\mathcal A)\). The following condition is sufficient for
every finite-width step in the source composition:

\[
 n\ge\left\lceil\max\left\{
 [2\mathcal A(2000\log(2\mathcal A))^{16}]^{1000},
 \frac{64mL}{\rho}
 \right\}\right\rceil.
\tag{4}
\]

It is polynomial in \(\beta^L,m,d,1+\lambda^{-1},\rho^{-1}\), up to
the explicitly displayed logarithm and the logarithmic moment order \(p\).
Its first term is a constant times

\[
 \beta^{2000000L}(1+\lambda^{-1})^{4000}Q^{4000}
 [\log(2\mathcal A)]^{16000}.
\]

The only explicit algebraic inverse-confidence factor outside \(p\) and
logarithms in (4) is \(\rho^{-1}\). This is a sufficient gate for the
unchanged event, not an optimal-confidence assertion.

The simpler enclosing condition

\[
 n\ge\left\lceil(\mathcal A/\rho)^{1100}\right\rceil
\tag{5}
\]

implies (4). Thus, at \(\rho=2^{-20}\delta\), the originally displayed
decoder source gate admits the replacement

\[
 n\ge\left\lceil\left[
 \frac{2^{20}\beta^{2000L}}\delta
 (1+m/\gamma)^4(m+d+p+1)^4
 \right]^{1100}\right\rceil,
\tag{6}
\]

with the same \(p\) as the original theorem. Its activation factor is

\[
 \beta^{2200000L},
\]

compared with \(\beta^{40000000L}\) in the power-20,000 condition.
Both are single exponential in depth \(L\), for fixed \(\beta>1\);
neither is double exponential in \(L\).

Here is the exact logarithmic calculation. Since

\[
 \log\mathcal A\ge4000\log10>9000,
\]

we have \(\log(2000u)\le u/320\). Indeed it holds at \(u=9000\)
because \(\log(18{,}000{,}000)<17<9000/320\), and the derivative
of \(u/320-\log(2000u)\) is positive thereafter. At

\[
 x_0=1000[u+16\log(2000u)]\le1050u,
\]

we consequently have \(1+x_0\le2000u\), and

\[
 \mathcal A(1+x_0)^{16}\le
 \mathcal A(2000u)^{16}=\tfrac12e^{x_0/1000}.
\]

The derivative of \(x/1000-16\log(1+x)\) is positive for
\(x>15999\). Hence every larger width obeys the actual absorption gate

\[
 \mathcal A\ell^{16}\le n^{1/1000}.
\tag{7}
\]

Also \(1050\log(2\mathcal A)\le1100\log\mathcal A\), so the first
term of (4) is at most \(\mathcal A^{1100}\). The inequality
\(\mathcal A\ge64mL\) follows directly from (2), \(Q\ge m\), and
\(\beta^{2000L}\ge64L\). Therefore (5) dominates both terms of (4).
Ceilings only strengthen these implications.

For use below, the two economical sufficient gates are precisely

\[
 \mathcal A\ell^{16}\le n^{1/1000},\qquad
 n\ge64mL/\rho.
\tag{8}
\]

They imply

\[
 \begin{gathered}
 \log n>9\cdot10^6,\qquad
 p,m,d\le\mathcal A^{1/4}\le n^{1/4000},\qquad
 L\le\beta^L\le n^{1/2000000},\\
 \log(1/\rho)\le\log n,\qquad
 \log(64nmL/\rho)\le2\log n.
 \end{gathered}
\tag{9}
\]

All small numerical margins below are uniform on this explicit range.
For example \(10^6(1+\log n)^2\le n^{1/1000}\) follows by checking
the logarithms at \(\log n=9\cdot10^6\); their right-minus-left
derivative is positive afterwards. This supplies a concrete numerical
onset whenever a harmless polynomial in \(\log n\) is compared below
with a positive numerical power of \(n\).

## 3. Initialization gates and their probability shares

These are the complete initialization requirements in the source proof.

1. The fitting event uses \(n\ge N_{\rm fit}(\rho/32)\), with the
   explicit maximum in `EXPLICIT_FITTING_WIDTH.md` (5). Its envelope is
   bounded by
   \[
   \beta^{32L}(1+\lambda^{-1})^2
   [dL\log\beta+\log(512L(m+1)^2/\rho)]+1.
   \]
   Using (9), the bracket is at most a fixed numerical multiple of
   \((d+1)\ell\); its entire expression is at most
   \(\mathcal A\ell\), with ample explicit activation-power slack.
   Equation (7) makes this less than \(n\). Its failure share remains
   \(\rho/32\).

2. The initial-coordinate event uses the deterministic value
   \[
   Z_0=2H\sqrt{2\log(64nmL/\rho)}\le4H\sqrt\ell,
   \]
   and retains failure at most \(\rho/32\). The final inequality uses
   precisely the second gate in (8), rather than concealing confidence
   inside a coordinate coefficient.

3. Initial exponential budgets have failure at most
   \(15mL/(16n)\le15\rho/1024<\rho/32\).

4. All initialized hidden rows and columns have norm at most two except
   with probability \(4nLe^{-n/2}\le\rho/32\). For this last inequality,
   \(\rho\ge64mL/n\) reduces the required comparison to
   \(2n^2e^{-n/2}\le m\), which holds on (9).

5. Let
   \[
   D_{\rm init}=(8s)^L\sqrt p\,(b+sZ_0),
   \]
   as in the source (7), where \(b\le\beta\), \(s\le\beta\), and
   \(H\le\beta^{2L}\). Its two deterministic gates are
   \[
   D_{\rm init}/\sqrt n\le H/8,
   \qquad D_{\rm init}/\sqrt n\le\sqrt\lambda/32.
   \tag{10}
   \]
   The elementary bound
   \(D_{\rm init}\le\beta^{10L}\sqrt{p\ell}\) gives both, since
   \(32\beta^{10L}\sqrt p\max\{1,\lambda^{-1/2}}
   \le\sqrt{\mathcal A}\), \(H\ge1\), and (7) applies.
   No independent cavity-Gram concentration is needed.

6. The upper-layer initial-coordinate comparison has failure at most
   \[
   2pmL^2 n^{p+1}
   \exp[-n^{4/5}/(2D_{\rm init}^2)]\le\rho/32.
   \tag{11}
   \]
   In fact \(D_{\rm init}^2\le\mathcal A\ell\), so the negative
   exponent is at least \(n^{0.799}/2\). By (9) the logarithm of the
   prefactor is at most \(10n^{1/4000}\ell\). Their difference is less
   than \(-n^{0.7}\), which is less than \(\log(\rho/32)\) on (9).
   The associated initial-budget margin is
   \[
   e^{\eta n^{-1/10}}8L+p/n<\mathcal B/2,
   \qquad\mathcal B=1024e^2L.
   \tag{12}
   \]
   It already follows from \(\eta\le1\), \(p/n\le1\), \(L\ge2\).

The initialization failure allocations total less than \(\rho/4\), as required.
The own-initialization tests and zero-reference convention of the source
remain in force before any omitted Gaussian root is integrated.

## 4. The local Gaussian event: value, interpolation, and union gates

The explicit coefficient ledger in source Sections 3--4 bounds the enlarged
linear maps and centered quadratic matrices, including the added training
responses, by

\[
 B\sqrt p\,n^{1/4000}\ell^5,
 \qquad B=\beta^{1000L}(1+\lambda^{-1})^2
          =\sqrt{\mathcal A}/Q^2.
\tag{13}
\]

Their control moduli have the same coefficient and at most \(\ell^4\);
their terminal-time derivative bounds have the same coefficient and at
most \(\sqrt n\ell^8\). These are the enlarged response bounds of source
(23), together with `INSERTION_MAP_MODULI.md` (4)--(22). They are
accepted local interfaces, not newly derived response estimates here.

The following list separates every condition used in forming the event.

* **Map envelope and mean.** Equation (7) bounds (13) by
  \(n^{3/4000}<n^{1/200}\), since \(\sqrt p\le Q^2\).
  Every Gaussian Euclidean-image mean is consequently at most
  \(\sqrt{2p}\,n^{1/200}<n^{1/100}/2\). The latter follows from
  \(p\le n^{1/4000}\) and
  \(2\sqrt2<n^{0.004875}\), valid on (9).

* **Fixed-grid tails.** Use coordinate/form threshold \(n^{-1/10}/8\)
  and input covariance \(I_{2pn}/n\). Splitting real and imaginary
  parts, the Gaussian and Gaussian-square bounds imply a common tail
  at most \(4e^{-n^{0.78}}\). For example a conservative quadratic
  exponent is
  \[
  \min\{n^{0.79}/(8192p),\ n^{0.895}/128\}.
  \tag{14}
  \]
  Each term exceeds \(n^{0.78}\) by (9); the linear tail is stronger.
  The image-mean condition above also makes the Euclidean tail stronger.
  This keeps the factor \(p\) in the quadratic variance bound.

* **Root norm.** For each deletion set,
  \(\Pr(\|g\|>2\sqrt{2p})\le e^{-pn}\). The union over at most
  \(pLn^p\) sets must be paid. Its logarithm is at most \(-pn/2\),
  hence below \(-2n^{0.7}\), on (9). No adaptive-control net
  multiplies this root event.

* **Control interpolation.** The control accuracy remains
  \(\tau=n^{-1/8}\). The centered quadratic error, including its
  trace, is at most
  \[
  10B p^{3/2}n^{1/4000}\ell^4\tau.
  \]
  Thus the sufficient gate at allocated error \(n^{-1/10}/8\) is
  \[
  80Bp^{3/2}\ell^4\le n^{99/4000}.
  \tag{15}
  \]
  Since \(p^{3/2}\le Q^2\), the left side is at most
  \(80\sqrt{\mathcal A}\ell^4\le80n^{1/2000}\), which satisfies
  (15) on (9). The linear root multiplier \(2\sqrt{2p}\) is smaller.

* **Terminal interpolation.** Retain the source's mesh
  \(h_t=n^{-2}/(1+\mathcal A\ell^8)\). A centered quadratic error
  between adjacent rectangular grid points is at most
  \[
  10\sqrt2 Bp^{3/2}n^{1/2+1/4000}\ell^8 h_t
  \le15n^{-1.49975}<n^{-1/10}/8.
  \tag{16}
  \]
  The linear error is smaller. The exact rectangular grid count from
  `INSERTION_MAP_MODULI.md` (22) is at most \(n^6\): its side lengths
  are at most \(34(1+\lambda^{-1})\ell\), its inverse mesh at most
  \(2n^{2.001}\), and
  \((1+\lambda^{-1})\ell\le n^{1/4000}\). Fixed numerical factors
  are paid by (9).

* **Control entropy and remaining tests.** The enlarged control count is
  at most \(4p(m+1)^2\); amplitude and speed are the original source
  bounds, with the single \(\sqrt n\) speed conversion. The explicit
  scalar-net construction gives
  \[
  \log N_{\rm ctrl}\le\mathcal A\ell^8n^{5/8}
       \le n^{0.626}.
  \tag{17}
  \]
  The coordinate, norm, pairing and probe count is at most
  \(\mathcal A n^3\). Including terminals and all deletion sets, the
  fixed-grid failure is therefore at most
  \[
  4pL\mathcal A n^{p+9}
       \exp[n^{0.626}-n^{0.78}].
  \tag{18}
  \]
  Equations (9) give a logarithm less than \(-2n^{0.7}\). Adding the
  root-norm failure leaves a total below \(e^{-n^{0.7}}<\rho/16\).

These gates are for one-dimensional control restrictions along the
prescribed contours. The original analytic terminal extension is retained;
no independence or path-independence assertion for adaptive arbitrary
two-dimensional controls is added.

## 5. Nonlinear, stop-transfer, and moment gates

Use exactly the original local exponents

\[
 N=n^{1/100},\quad d_0=n^{-1/10},\quad u_0=n^{-1/25},\qquad
 R=d_0N+d_0u_0+u_0^2,\quad P=(N+u_0)^2/\sqrt n.
\]

The local size conditions are \(N+u_0\le\sqrt n\) and
\(u_0+R+P\le1\). They follow on (9), using
\(R\le3n^{-0.08}\), \(P\le4n^{-0.48}\).

The complex Taylor strip gate is the unchanged explicit inequality

\[
 d_0+\beta^{10L}u_0+\beta^{30L}(R+P)<a/32.
\tag{19}
\]

Since \(a^{-1}\le\beta/16\), its left side multiplied by \(32/a\)
is at most \(16\mathcal A n^{-0.04}\le16n^{-0.039}<1\).
The learned-port interpolation and current-row norm gates follow from
the same size bound and the displayed learned-source bounds

\[
 \|\Delta W_{:,i}\|\le S^2\tau_*A_n/\sqrt n,
 \quad\|\Delta W_{i,:}\|\le S^2H_{\max}B_n/\sqrt n,
\]

where \(A_n,B_n\le\beta^{80L}\ell\), \(\tau_*\le\beta^{6L}\),
\(H_{\max}\le\beta^{3L}\). In particular each row increment is less
than one; original row norm two becomes at most three. The original
learned-source and top-offset cutoff degree is three and is not increased.

The exact integrated nonlinear closing gate is source (24):

\[
 \mathcal A\ell^8n^{1/4000}
 [n^{-0.08}+u_0^2+n^{-0.48}+n^{-1/2}]<u_0/2.
\tag{20}
\]

Its left side is at most \(4n^{-0.07875}\) by (7), so (20) needs
only \(8<n^{0.03875}\), already in (9). The differentiated remainder
on the unlocalized \(u_0\) direction is retained, as in the scaled lemma.

For the subsequent endpoint comparisons, the displayed local derivative,
Taylor, added-response, and learned-port coefficients are bounded by the
same ledger \(\mathcal A\ell^8\). A conservative combined bound is

\[
 16\mathcal A\ell^8
 [d_0+u_0+R+P+d_0(N+u_0+(N+u_0)^2)]
 \le256n^{-0.039}<n^{-1/30}.
\tag{21}
\]

The final inequality uses \(256<n^{0.039-1/30}\), explicit on (9).
The corresponding Euclidean excess over the retained linear radius is
smaller than \(N\), yielding the unchanged \(2N\) comparison. Thus the
required transfer gates are

\[
 e^{2\eta n^{-1/30}}\mathcal B+p/n<2\mathcal B,
 \qquad n^{-1/30}<a/16,
\tag{22}
\]

together with the doubled coordinate/response margins. They follow from
\(\eta\le1\), (9), \(a^{-1}\le\beta/16\), and the source caps,
whose coefficients are at least one. This is the same stopped-prefix
comparison, not conditioning on successful full-network evolution.

The singleton scalar error uses the nonlinear endpoint error, centered
forms, learned sources, and adaptive rank-one trace. The latter is bounded
by \(\mathcal A\ell^8n^{-1+1/4000}\). All the former coefficients
are in the stated singleton ledger; allowing their sum a factor
\(16\mathcal A\ell^8\), the resulting finite error is bounded by

\[
 32\mathcal A\ell^8 n^{-1/30}<n^{-1/40}.
\tag{23}
\]

The exponent margin is \(1/30-1/40-1/1000>0\). The nonvanishing
trace means and the original scalar absorption coefficient are unchanged.
This bound does not supply a new proof of the underlying trace identities.

For Gaussian maxima, retain a time mesh of size \(n^{-2}\). The source
raw derivative bound includes its \(\sqrt n\) normalization factor;
the coefficient is paid by (7). Hence the interpolation error is less
than one and the terminal count at most \(n^5\). There are at most
\(\mathcal A n^6\) singleton scalar tests including terminals. With
\(V=\max\{1,H_{\max},\tau_*\}\), use grid threshold
\(31V\sqrt\ell\) and reserve \(V\sqrt\ell\) for interpolation, within
the original \(C_G\sqrt\ell=32V\sqrt\ell\). A complex scalar Gaussian
with real and imaginary variances at most \(V^2\) has tail at most

\[
 4\exp[-31^2\ell/8].
\]

The union is at most \(n^{-100}\). The training-response multiplier 64
and at most \(m^2\) sample pairs give a stronger tail by the same argument.
Their total \(2n^{-100}<\rho/16\) follows from (9). These maximum
events precede budget removal.

The pole, residual-growth, operator, activity and short-contour propagator
gates require no additional width. `POLYNOMIAL_SOURCE_WIDTH.md`
(12)--(15) verifies them already at \(p=1,n\ge1\); replacing the radius
by its value divided by \(p\) improves each. The unabsorbed propagator
\(J_0n^{1/4000}\), \(J_0=2e^{1/4}(2\mathcal B)^{1/4000}\), is already
charged in the map/remainder ledger. Its separate older absorption into
\(n^{1/1000}\) is not needed as an extra scientific premise.

For common-cavity corrections retain source (29)--(30):

\[
 v_n=4n^{-49/100},\qquad
 \mu_n\le256v_n\sqrt{\log(e+
 \beta^{400L}(1+\lambda^{-1})\ell^4/v_n)}+2v_n.
\tag{24}
\]

Their explicit moment gate is \(p\mu_n+p^2v_n^2<10^{-3}\).
Since \(\beta^{400L}(1+\lambda^{-1})\ell^4\le
\mathcal A\ell^{16}\le n^{0.001}\), the logarithm in (24) is at
most \(\ell\). Thus

\[
 p\mu_n+p^2v_n^2
 \le1032n^{-0.48975}\sqrt\ell+16n^{-0.9795}<10^{-3}
\tag{25}
\]

on (9). The projected difference paths, their conditioning, and the
source's Hölder allocation are unchanged.

The complex-minus-real moment estimate needs *no width gate*:
`FINITE_COMPLEX_MOMENT_GATE.md` (13) holds for every \(n\ge1\) at
the same \(p\) and radius (3). In particular the older
\(\ell\ge\max\{e^2,2048e^2L\}\) simplification is not required.
The source's distinct-root base stays sixteen, with its original constants.

Finally, the sufficient collision gate \(n\ge4p^3\) follows at once
from \(p\le n^{1/4000}\) and (9). It can itself be sharpened, without
any new moment theorem, to the exact condition

\[
 \binom p2\frac{e^{\sqrt\ell/100}}{16n}\le1,
\tag{26}
\]

because the proved repeated-index bound is \(e^{\sqrt\ell/100}\),
not necessarily its coarser power envelope. Neither collision version
changes the controlling gate (7). Budget-hit probability remains

\[
 emL(64e^2)^{-p}\le\rho/4
\tag{27}
\]

by the unchanged integer choice (1).

Equations (10)--(27), the initialization shares, and the local event
account for every deterministic and probabilistic width inequality in
the finite source composition. Their total failure remains below
\(\rho/4+\rho/16+\rho/16+\rho/4<\rho\). No additional dependence
on a positive lower label amplitude appears.

## 6. Decoder gates remain separate and costs do not worsen

The reduced scientific width does not remove implementation conditions.
`CLOSURE_COMPOSITION_COSTS.md`, Section 6, supplies the dimension and
physical-horizon gates below. `POLYNOMIAL_SOURCE_WIDTH.md` (29)--(30)
supplies the all-time carrier-extension gate:

\[
 \begin{gathered}
 n\ge d,\qquad
 n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}/\lambda}\},\\
 n\ge\max\{1,(\beta^{23L}/8)^{1/15}\},
 \end{gathered}
\tag{28}
\]

for dimension, physical horizon and all-time carrier extension; and

\[
 n\ge C_0
 [p\beta^{201L}(m+d+2)(1+\lambda^{-1})/\rho]^2,
\tag{29}
\]

for the additional source/query Gaussian RMS failures. Here \(C_0\) is
the same universal numerical constant in the existing cost interface.
It must either be retained, or included in the unchanged universal
outer enlargement; this note does not set an unspecified universal
constant equal to one.

Numerical-error absorption still uses

\[
 n\ge\max\{1,(A_{\rm num}/32)^{1/9}\}.
\tag{30}
\]

The unmodified clean precision table uses \(n\ge1/Y\). The original
alternative for \(0<nY<1\) instead enlarges the precision and field-count
logarithm by \(\log_+(1/(nY))\); it preserves the full label range and
must be charged if that branch is used.

For the optional quadratic-in-\(n\) internal-work envelope, retain

\[
 n\ge
 [\beta^{1335L}(m+d+2)^5(1+\lambda^{-1})^5(d+1)p^5/\delta]^2.
\tag{31}
\]

At \(\rho=2^{-20}\delta\), its bracket is at most
\((\mathcal A/\rho)^3\), exactly as in the original cost note, so
the simpler scientific gate (5) already dominates (31). It also
dominates (28)--(29), up to the same universal constant \(C_0\).
For the more economical factorized scientific gate (4), retaining
(29)--(31) as separate displayed conditions avoids reinstating an
unnecessarily large algebraic confidence power.

Neither (4) nor (5) changes \(p\), the source radius, the numerical patch
length, Taylor degree, generator, median, or evaluator/data interfaces.
Thus the existing whole-sphere, all-time error implication and near-linear
width work bounds retain their original component assumptions and costs.
This note strengthens only their sufficient source-onset statement.
No new whole-sphere complex-source theorem or new decoder comparison
is claimed.

## 7. Status and source scope

The proved new statements are the factorization (8), its explicit
solution (4), the safe power envelope (5), and the gate-by-gate arithmetic
substitutions above, conditional on the displayed scientific interfaces
of the current source proof. The exact collision condition (26) is an
additional minor arithmetic simplification. No proof gap in those
width implications was found. This is not a fresh independent audit of
the augmented insertion, scalar trace, or decoder theorem.

Complete scientific files read were the assigned
`FULL_FINITE_SOURCE_PROBABILITY.md` and its check;
`QUANTITATIVE_INSERTION_WIDTH.md` and its check;
`FIXED_ORDER_INSERTION_JETS.md` and its check;
`SCALED_INSERTION_REMAINDER.md`; `INSERTION_MAP_MODULI.md`;
`FINITE_COMPLEX_MOMENT_GATE.md` and its check;
`POLYNOMIAL_SOURCE_WIDTH.md`; `EXPLICIT_FITTING_WIDTH.md`;
`CLOSURE_COMPOSITION_COSTS.md`; and `TWO_GAP_CLOSURE_RESULT.md`.
Links to older studies were not followed. Required canonical-notation,
neural-network, rigorous-math, research-state, and adversarial-audit
instructions were read and applied. The parent task owns any study
summary update and any independent review request.
