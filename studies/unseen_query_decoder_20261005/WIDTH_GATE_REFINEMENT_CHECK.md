# Bounded reconstruction of the factorized source-width gate

2026-10-07. Verdict: **conditional PASS**, with one citation correction
not affecting the inequalities. The factorized gate and enclosing power
1,100 suffice for the finite-width composition under its original
scientific component estimates. This report does not independently
validate the augmented insertion theorem, scalar trace identities,
autonomous-cavity conditioning, or dense-reference theorem.

The checked candidate is WIDTH_GATE_REFINEMENT.md, SHA-256
5dd082f39f139af775233cf7c270783bc0f10c4905e881b79e20719240209419.
This is a separate bounded reconstruction with reused author context,
not a blind independent review: the reviewer previously derived the
word-resource refinement and read CLOSURE_COMPOSITION_COSTS.md and
the exact-query construction. No other review verdict was used.

## 1. Scope and hypotheses

Let \(n\) be width, \(m\ge d\ge1\), \(L\ge2\),
\(\lambda=\gamma/m>0\), \(\beta\ge10\), and \(0<\rho<1/4\).
Write \(Y=\|y\|_2/\sqrt m\), \(S=16Y/\lambda\), and retain the
original complete upper-label intersection. At \(Y=0\), use the
stationary branch separately. Define

\[
 p=\max\left\{1,\left\lceil
 \frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\},
 \quad Q=m+d+p+1,\quad
 \mathcal A=\beta^{2000L}(1+\lambda^{-1})^4Q^4,
 \quad \ell=1+\log n .
\]

FULL_FINITE_SOURCE_PROBABILITY.md supplies the deterministic source
ledger, enlarged Gaussian-map/interpolation coefficients, scaled
nonlinear remainder, endpoint/trace estimates, and stopped Gaussian
moments. They are accepted at their stated scientific boundaries.
This task replaces the width used to combine them, without weakening
their hypotheses or changing their failure allocations. Qualitative
asymptotic constants would not support this replacement.

## 2. Solving the actual absorption inequality

The factorized gate is

\[
 n\ge\left\lceil\max\left\{
 [2\mathcal A(2000\log(2\mathcal A))^{16}]^{1000},
 \frac{64mL}{\rho}\right\}\right\rceil .
 \tag{1}
\]

Put \(u=\log(2\mathcal A)\) and
\(x_0=1000[u+16\log(2000u)]\).
Since \(\log\mathcal A\ge4000\log10>9000\),
\(\log(2000u)\le u/320\): it holds at 9000, and its right
side minus left side increases thereafter. Thus \(x_0\le1050u\),
\(1+x_0\le2000u\), and

\[
 \mathcal A(1+x_0)^{16}
 \le\mathcal A(2000u)^{16}=\tfrac12e^{x_0/1000}.
\]

For \(x>15999\), the derivative of
\(x/1000-16\log(1+x)\) is positive. Every width in (1) therefore
satisfies the original source absorption and confidence gates

\[
 \mathcal A\ell^{16}\le n^{1/1000},
 \qquad n\ge64mL/\rho .
 \tag{2}
\]

Also \(1050\log(2\mathcal A)\le1100\log\mathcal A\), so
the first term of (1) is at most \(\mathcal A^{1100}\).
Since \(\beta^{2000L}\ge64L\) and \(Q^4\ge m\),
\(\mathcal A\ge64mL\). Consequently

\[
 n\ge\lceil(\mathcal A/\rho)^{1100}\rceil
 \tag{3}
\]

implies both terms of (1). Ceilings do not reverse the implication.
The factorized gate retains its large numerical coefficient; no
unspecified universal constant is silently set to one.

For all later checks, (2) gives

\[
 \log n>9\cdot10^6,\quad
 p,m,d\le n^{1/4000},\quad
 L\le\beta^L\le n^{1/2000000},
\]
\[
 \log(1/\rho)\le\log n,\qquad
 \log(64nmL/\rho)\le2\log n .
 \tag{4}
\]

Every numerical absorption below can be checked at
\(x=\log n=9\cdot10^6\) and then by monotonicity of
\(ax-k\log(1+x)-\log C\). Its derivative is positive at and
beyond that point for the candidate's displayed constants/exponents.
No problem-dependent eventual onset is introduced.

## 3. Initialization and confidence

EXPLICIT_FITTING_WIDTH.md (5), with its proved envelope (12),
at failure \(\rho/32\), contains the bracket
\[
 dL\log\beta+\log[512L(m+1)^2/\rho]\le2(d+1)\ell .
\]
Equations (4) justify this bound. Its product with
\(\beta^{32L}(1+\lambda^{-1})^2\), plus the ceiling, is
at most \(\mathcal A\ell<n\).

The remaining initialization gates were checked as follows.

| Requirement | Consequence of (2)–(4) |
|---|---|
| Initial coordinates | \(Z_0=2H\sqrt{2\log(64nmL/\rho)}\le4H\sqrt\ell\) |
| Initial exponential budgets | \(15mL/(16n)\le15\rho/1024<\rho/32\) |
| Initial row/column norms | \(4nLe^{-n/2}\le\rho/32\), since \(2n^2e^{-n/2}\le m\) |
| Cavity RMS/singular-value margin | \(D_{\rm init}\le\beta^{10L}\sqrt{p\ell}\), and \(32\beta^{10L}\sqrt p\max(1,\lambda^{-1/2})\le\sqrt{\mathcal A}\) |
| Upper-layer cavity coordinate union | \(2pmL^2n^{p+1}\exp[-n^{4/5}/(2D_{\rm init}^2)]<\rho/32\) |
| Initial budget transfer | \(8Le^{\eta n^{-1/10}}+p/n<\mathcal B/2\), using \(\eta\le1,\ \mathcal B=1024e^2L\) |

For the coordinate union, \(D_{\rm init}^2\le\mathcal A\ell\)
makes the negative exponent at least \(n^{0.799}/2\);
the prefactor logarithm is at most \(10n^{1/4000}\ell\).
Their sum is below \(-n^{0.7}\), and
\(e^{-n^{0.7}}<\rho/32\) follows from \(\rho\ge64mL/n\).
Thus confidence is paid explicitly. Initialization totals less than
\(\rho/4\), with the original own-initialization and zero-reference
cavity convention unchanged.

## 4. Gaussian event and continuum interpolation

Write \(B=\beta^{1000L}(1+\lambda^{-1})^2
=\sqrt{\mathcal A}/Q^2\). The accepted source interface bounds
map norms by \(B\sqrt p\,n^{1/4000}\ell^5\), control moduli
with \(\ell^4\), and terminal derivatives with \(\sqrt n\,\ell^8\).

The map norm is at most \(n^{3/4000}\le n^{1/200}\).
The Gaussian Euclidean-image mean is at most
\(\sqrt{2p}n^{1/200}<n^{1/100}/2\).
Both candidate quadratic-tail exponents
\[
 n^{0.79}/(8192p),\qquad n^{0.895}/128
\]
exceed \(n^{0.78}\); the variance factor \(p\) is retained.
The separate root-norm union over at most \(pLn^p\) deletion
sets has logarithm at most \(-pn/2<-2n^{0.7}\).

Control interpolation at \(\tau=n^{-1/8}\) follows from
\[
 80Bp^{3/2}\ell^4\le80\sqrt{\mathcal A}\ell^4
 \le80n^{1/2000}<n^{99/4000}.
\]
This includes the centered quadratic trace. For terminal mesh
\(h_t=n^{-2}/(1+\mathcal A\ell^8)\), the interpolation error
is at most \(15n^{-1.49975}<n^{-1/10}/8\).
The exact rectangular grid has fewer than \(n^6\) points.
The control net has log cardinality at most
\(\mathcal A\ell^8n^{5/8}\le n^{0.626}\).

Including every terminal, deletion set and scalar/vector/form test
therefore gives the proposed failure bound
\[
 4pL\mathcal A n^{p+9}\exp[n^{0.626}-n^{0.78}],
\]
whose logarithm is below \(-2n^{0.7}\) at (4).
Adding root-norm failure leaves less than
\(e^{-n^{0.7}}<\rho/16\).
The deterministic-control union still precedes adaptive substitution;
no new two-dimensional arbitrary-control or independence assertion
has been introduced.

## 5. Nonlinear, stop and moment inequalities

Use \(N=n^{1/100}\), \(d_0=n^{-1/10}\), \(u_0=n^{-1/25}\),
\(R=d_0N+d_0u_0+u_0^2\), and \(P=(N+u_0)^2/\sqrt n\).
Here \(R,P\) are local remainder quantities.
Then \(R\le3n^{-0.08}\), \(P\le4n^{-0.48}\).
The original coefficient ledger and (2) give:

- The strip expression, multiplied by \(32/a\), is at most
  \(16\mathcal A n^{-0.04}\le16n^{-0.039}<1\).
- The integrated closing remainder is at most
  \(4n^{-0.07875}<u_0/2\).
- The bracket in candidate (21) is at most \(15n^{-0.04}\).
  Its endpoint bound is consequently at most
  \(240n^{-0.039}<n^{-1/30}\).
- The singleton scalar-error allowance is at most
  \(32n^{1/1000-1/30}<n^{-1/40}\).
- Learned row/column increments retain their \(S^2\) factors and
  are less than one. Budget and pole transfers have the original
  strict margins.

The local remainder and trace estimates are necessary for the third
and fourth bullets. Their coefficients lie within the original
explicit \(\mathcal A\ell^8\) ledger. This arithmetic check does
not independently prove their scientific identities.

For Gaussian maxima, threshold \(31V\sqrt\ell\), where
\(V=\max(1,H_{\max},\tau_*)\), reserves \(V\sqrt\ell\)
for interpolation within the original \(32V\sqrt\ell\).
The exponent \(31^2\ell/8\), with at most
\(\mathcal A n^6\) tests, gives failure below \(n^{-100}\).
The response multiplier 64 gives a stronger bound for training
sample pairs. Their total \(2n^{-100}<\rho/16\) follows from (2).

POLYNOMIAL_SOURCE_WIDTH.md (12)–(15) supplies contour,
residual-growth, activity and operator gates at every width.
Dividing the radius by \(p\) improves them.
The finite propagator coefficient \(J_0n^{1/4000}\) stays inside
the source ledger; no older separate absorption is required.

For \(v_n=4n^{-49/100}\), the logarithm in the supplied
common-cavity mean estimate is at most \(\ell\): its argument
is at most \(e+n^{0.491}/4\). Therefore
\[
 p\mu_n+p^2v_n^2
 \le1032n^{-0.48975}\sqrt\ell+16n^{-0.9795}<10^{-3}.
\]
FINITE_COMPLEX_MOMENT_GATE.md (13) holds for every \(n\ge1\)
at the chosen radius and order, conditional on its original
derivative hypotheses. Its obsolete extra logarithmic-width
simplification is unnecessary.

The collision gate \(n\ge4p^3\) follows from (4). The sharper
condition \(\binom p2 e^{\sqrt\ell/100}/(16n)\le1\)
is exactly the exponent-at-most-one condition of
QUANTITATIVE_INSERTION_WIDTH.md (7), with distinct-root base 16.
The chosen \(p\) finally gives
\(emL(64e^2)^{-p}\le\rho/4\).
Combined allocated failure is at most
\(\rho/4+\rho/16+\rho/16+\rho/4<\rho\).
No new lower-label assumption or changed moment base is used.

## 6. Decoder qualifications and citation correction

The dimension/horizon conditions, RMS gate with its actual
universal \(C_0\), numerical absorption
\(n\ge\max\{1,(A_{\rm num}/32)^{1/9}\}\), and optional
quadratic-work gate remain separate as displayed.
Numerical absorption uses the explicitly instantiated mesh
certificate of NUMERICAL_BENCHMARK_ABSORPTION.md, Section 5,
where \(b_n\ge32Y/n\). It would not follow for an arbitrary
previously fixed smaller mesh coefficient.

At \(\rho=2^{-20}\delta\), the quadratic-work bracket is at most
\((\mathcal A/\rho)^3\), so (3) dominates its square.
It likewise dominates the displayed RMS gate up to the retained
\(C_0\); the candidate correctly does not silently set \(C_0=1\).
For the factorized gate, these separate decoder conditions must
remain visible. The clean precision branch still uses \(nY\ge1\);
smaller positive labels pay the enlarged logarithm and field counts.

One citation should be corrected when incorporating the result.
Candidate (28)'s carrier gate
\(n\ge\max\{1,(\beta^{23L}/8)^{1/15}\}\) is not displayed in
CLOSURE_COMPOSITION_COSTS.md, Section 6. It follows from
POLYNOMIAL_SOURCE_WIDTH.md (29)–(30), using
\(C_{\rm tail}\le\beta^{20L}\),
\(\lambda^{1/2}\le\beta^{3L}\), and \(K_{\rm src}\ge1\).
This is a provenance correction, not a failed width implication.

The enclosing activation factor is \(\beta^{2200000L}\),
versus \(\beta^{40000000L}\) before. Both are single exponential
in depth at fixed \(\beta\).
The factorized source gate has its explicit algebraic
\(\rho^{-1}\) term, besides logarithmic dependence through \(p\).
This is a sufficient-gate statement, not an optimal-confidence theorem.

## Read record and verdict boundary

Read completely: WIDTH_GATE_REFINEMENT.md,
FULL_FINITE_SOURCE_PROBABILITY.md, EXPLICIT_FITTING_WIDTH.md,
QUANTITATIVE_INSERTION_WIDTH.md, POLYNOMIAL_SOURCE_WIDTH.md,
FINITE_COMPLEX_MOMENT_GATE.md, INSERTION_MAP_MODULI.md, and
NUMERICAL_BENCHMARK_ABSORPTION.md.
The complete earlier read of CLOSURE_COMPOSITION_COSTS.md was reused.
Four originally supplied review filenames did not exist; the supervisor
confirmed the exact same-study replacements above.
No prior checks, other-study artifacts, book material, experiments
or Git history were read. Canonical-notation instructions, their neural
reference and rigorous-mathematics instructions were reused while
current. Only this report was written.

Conditional PASS applies to the gate arithmetic and its composition
with the accepted original scientific interfaces. It does not
independently establish those interfaces or authorize promotion.
No blocking arithmetic error was found.

## Citation correction recheck

2026-10-07. Verified the revised opening pointers and Section 6 of
WIDTH_GATE_REFINEMENT.md at SHA-256
c10a99d53be95d1623f38671392e4a66dcd0396a5d7ac388bbdebd18105a3832.
Section 6 now attributes the carrier-extension gate to
POLYNOMIAL_SOURCE_WIDTH.md (29)–(30), while retaining the dimension
and horizon attribution to CLOSURE_COMPOSITION_COSTS.md, Section 6.
The original citation finding is resolved; the displayed gates in
that passage are unchanged. The added opening links were not followed.
The original reviewed hash and finding above remain as the historical
record. Conditional PASS and its scientific scope are unchanged.
