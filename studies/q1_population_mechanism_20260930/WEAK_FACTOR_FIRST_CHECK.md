# Internal check of the weak-factor first-layer route

**Verdict: PASS for the conditional first-layer result in the checked package.**
The canonical conditional drift, all displayed weak-factor coefficients and
remainder orders, the pointwise all-time inequality, and the minimum-norm
decoder conclusion are correct under the stated regular-flow and equivariance
assumptions. The executed interval certificate closes the three strict sign
obligations. Outward interval postprocessing also closes the optional sign in
equation (11). This is an internal check, not promotion or a proof of population
well-posedness.

The frozen note by itself ends with an open sign obligation. The complete
package checked here comprises that note, the supplied source definitions,
the frozen certificate source, the retained executed certificate, and the
analytic certificate justification below. No correction to the coefficient
formulas is required. Integration requests appear at the end.

## Scope, versions, and independence

Checker: fresh scoped agent `weak_factor_first_check`, 2026-09-30. Read every
line of these scientific inputs:

| Input | SHA256 |
| --- | --- |
| `WEAK_FACTOR_ROUTE.md` | `3ed97591b90f84d0fc14eb06c9bbca1f95410fde5c8d3b8bc22e695fb525a337` |
| `weak_factor_interval_certificate.py` | `51c7570b1f34a066287f286295868c87283ac45f16d0895d4b4d716c7010be54` |
| Author certificate `weak_factor_interval_certificate_20260930_01/results.json` | `316a83c28ccba4415d47d54f6bdb7ad2cd1a307150e86e0b9694ce4feded62cf` |

The two source hashes were checked again after the audit; the code hash was
also checked immediately before and after the fresh execution. The mathematical
note was not edited. The code was not edited. At the prewrite metadata check,
HEAD was `7fce699a7decf2239dc3eb50486eca661783b535`; the index was empty. No Git
mutation was made.

The supervisor supplied the missing source definitions in an explicit review
message after the checker requested them. They were:

\[
 H_a=\tanh(A\cdot u_a),\quad
 B=T+m^{-1}\sum_a V_a\otimes K_a,\quad Z_a=BH_a,\quad G_a=\tanh Z_a,
\]
\[
 F_a=\mathbb E_2[WG_a],\quad D_a=W(1-G_a^2),\quad
 L_a=(1-H_a^2)B^*D_a,
\]
with physical equations
\[
 \dot W=-2\operatorname{mean}_a r_aG_a,\quad
 \dot A=-2\operatorname{mean}_a r_aL_au_a,\quad
 \dot V_a=-2r_aD_a,\quad
 \dot K_a=(\rho/\tau)(H_a-K_a),\quad \dot\tau=\rho,
\]
where \(r_a=F_a-y_a\), \(\rho=(\operatorname{mean}r^2)^{1/2}\), and initialization
is Gaussian \(A\), canonical Gaussian \(T\), \(W=V=0\), \(K=H_0\), \(\tau=1\).
The supplied feature-clock rules were
\(W'=\operatorname{mean}yG\), \(A'=\operatorname{mean}yLu\),
\(V_a'=y_aD_a\), \(K_a'=(H_a-K_a)/(2+s)\), and \(\tau=1+s/2\),
under \(F_a=y_af\) and before \(f=1\). The source reverse rule is exactly
the rule printed in the note. These definitions were checked as supplied;
this assignment did not independently authenticate them against the book.

Required instructions and the proof/research skills were read, including the
research-contract and adversarial-audit references. No README, study history,
other route, other study research, archived book, or prior review was read.
An initial metadata-only filename search exposed names of other workflow
instruction copies but none of their contents. A fresh child saw only the
frozen certificate source and required instructions to crosscheck interval
primitives and analytic bounds. It reported no issue. The present checker
independently derived the same bounds and executed the checks reported below;
no author-route summary entered the check.

## Canonical normalization and the source-dependent drift

At initialization \(D=0\), \(W'=g_y\), and \(A'=V'=K'=0\). Thus
\(B'=H'=Z'=G'=0\). Differentiating the supplied definitions gives
\[
 D_a'=g_y\phi'(z_a),\qquad
 L_a'=\phi'(A\cdot u_a)T^*[g_y\phi'(z_a)],
\]
which gives equation (2), with the factor \(1/4\) contained in the sample
mean. No trained middle-operator term survives at this order.

For \(U_a=g_y\phi'(z_a)\), direct differentiation yields
\[
 \partial_bU_a={y_b\over4}\phi'(z_b)\phi'(z_a)
     +\mathbf1_{a=b}g_y\phi''(z_a).
\]
Consequently the note's \(C_{ab}=y_a\mathbb E[\partial_bU_a]/4\)
is symmetric and is one half the expected Hessian of \(g_y^2\). The
canonical reverse innovation has conditional mean zero given \(A_0\);
discarding it here is legitimate. Discarding it from the random acceleration
itself would not be legitimate. No covariance subtraction was made.

There is a useful normalization detail behind equation (3). At the symmetric
initial covariance, the group invariance of \(g_y^2\) implies
\(C_{ga,gb}=C_{ab}\). Thus \(C\) is diagonal in the four Walsh characters.
With the unnormalized characters satisfying \(\sum_a\chi(a)^2=4\),
\[
 J_\chi=\sum_{ab}C_{ab}\chi(a)\chi(b),\qquad
 C_{ab}={1\over16}\sum_\chi J_\chi\chi(a)\chi(b).
\]
Substitution into the conditional acceleration gives
\[
 \sum_{ab}C_{ab}\nabla H_a\,H_b
 =\sum_\chi J_\chi h_\chi\nabla h_\chi
 ={1\over2}\sum_\chi J_\chi\nabla h_\chi^2.
\]
This checks the factor \(1/2\) in (3) directly, including the Walsh and sample
normalizations. The Gaussian covariance derivative identity used to identify
\(J_\chi\) is valid here: all derivatives of the bounded smooth integrand are
bounded, so the positive-definite density proof extends to boundary variances
by dominated convergence. It is a covariance derivative, not a derivative
with respect to a standard deviation.

Because \(A'(0)=0\), the second derivative of
\(\mathbb E h_\eta(A_s)^2\) contains only the gradient paired with \(A''\),
giving (4). Sufficient regularity for this step is an \(L^2\)-twice
differentiable first-layer trajectory at startup, with the displayed source
calls differentiable there; bounded derivatives of \(h_\eta\) then justify
the expectation interchange. A merely formal trajectory would not suffice.
The result remains conditional on this regularity and on the local source
flow stipulated in the candidate.

Finally, \(ds/dt=2\) at initialization and every energy has zero first
derivative there. The physical-time acceleration is exactly four times the
feature-time acceleration. There is no missing factor of two in (9).

## Weak-factor asymptotics and strict local conclusions

The Taylor expansions (5) hold in every finite Gaussian \(L^p\), including
any fixed finite number of weight derivatives. For \(\varepsilon\) in a
fixed small neighborhood of zero, \(c=1+O(\varepsilon^2)\); Taylor remainders
are bounded by finite-degree polynomials in \(|X|+|Y|+|Z|\), times the stated
power of \(\varepsilon\). All these polynomials have finite Gaussian moments.
Walsh parity removes the intervening odd or even powers. This also gives the
two-power improvements in the remainder orders of the Gram entries.

Conditioning on \(\zeta_0\), the leading target coefficient is
\(\phi'(\zeta_0)\zeta_y+\phi''(\zeta_0)\zeta_\sigma\zeta_\tau\).
The cross term has zero expectation. Applying the Gaussian heat derivative
to this bounded smooth integrand before expanding verifies all three
derivative statements in (6). In particular, differentiating a bare
\(O(\varepsilon^6)\) statement is not needed. The small-variance orders
\(v_\sigma,v_\tau=O(\varepsilon^2)\), \(v_y=O(\varepsilon^4)\) give the
claimed derivative remainders, uniformly near the positive limiting context
variance.

All seven Gram entries in (7) were recomputed from
\[
 \nabla h_0^2=(2\phi p,0,0)+O(\varepsilon^2),
\]
\[
 \nabla h_\sigma^2=2\varepsilon^2(Y^2pq,Yp^2,0)+O(\varepsilon^4),
\]
\[
 \nabla h_y^2=2\varepsilon^4
  (Y^2Z^2qr,YZ^2q^2,Y^2Zq^2)+O(\varepsilon^6),
\]
and the exchanged factor formula. The needed Gaussian multipliers are
\(\mathbb EY^2=1\), \(\mathbb EY^4=3\),
\(\mathbb EY^4Z^2=3\), and \(\mathbb EY^4Z^4=9\).
No Gram coefficient is missing a multiplicity from the two primitive factors.

The algebraic reduction was checked with
\(q=-2\phi p\), \(r=4p-6p^2\), and \(\phi^2=1-p\). For example,
\[
 12pq^2r+4p^2q^2=208p^4-496p^5+288p^6,
\]
\[
 36q^2r^2+24q^4=2688p^4-9984p^5+12480p^6-5184p^7,
\]
which reproduce \(16P\) and \(192U\). The other three displayed reductions
and the derivative identity
\(J_n'=2n^2J_n-n(2n+1)J_{n+1}\) reproduce all of (8). Combining orders in
(4) yields exactly (9), including the error orders \(8,6,10\).

For any ratio \(E_i/E_j\), zero first derivatives give
\((E_i/E_j)''=(E_i''E_j-E_iE_j'')/E_j^2\) at startup. Substituting the
initial-energy expansions gives both (10) and (11), including their
\(O(\varepsilon^8)\) errors. The limiting quantities \(v\), \(a_1\), and
\(a_2\) are strictly positive, so the required denominators remain nonzero
for sufficiently small positive \(\varepsilon\).

The certified leading coefficients below therefore imply: for every
sufficiently small fixed positive \(\varepsilon\), all the named energy
and ratio changes have the stated strict sign on some positive local time
interval, provided their second derivatives are continuous there. This
argument uses a finite startup derivative and continuity. It establishes
neither convergence of a time Taylor series nor a time interval uniform in
\(\varepsilon\). It does not establish monotonic acquisition for all time.

## All-time geometry and decoder meaning

For any monotone real activation, the two differences
\(\Delta_\pm=\phi(x+a\pm b)-\phi(x-a\pm b)\) have the same sign.
Hence \(|\Delta_+-\Delta_-|\le|\Delta_++\Delta_-|\), proving
\(|h_y|\le|h_\sigma|\); exchanging the roles of \(a,b\) proves the other
bound. This includes decreasing monotone activations. For strictly monotone
tanh at finite logits, both differences are nonzero when \(a\ne0\), so the
first bound is strict then. If \(a=0\), both \(h_\sigma\) and \(h_y\)
vanish; the corresponding statement holds when \(b=0\). No exception was
found in the equality or vanishing cases.

This pointwise statement gives \(E_y\le\min(E_\sigma,E_\tau)\) for every
existing first-layer distribution, even if its symmetry has broken. The
decoder interpretation additionally needs the stated equivariant law.
For tanh, oddness makes the signed feature \(y_aH_a\) equal to
\(\tanh(A\cdot p_a)\). The matrices
\(\operatorname{diag}(\alpha\beta,\beta,\alpha)\) act transitively on the
signed input group. An invariant population law therefore gives a covariance
depending only on group difference, which is diagonalized by the characters.
Multiplication by the signed gauge permutes characters and preserves their
orthogonality. Coordinate exchange gives equal primitive-factor energies.

Write \(H_a=\sum_\eta\eta(a)h_\eta\). Under this orthogonality,
\(w_\chi=h_\chi/E_\chi\) satisfies
\(\mathbb E[w_\chi H_a]=\chi(a)\) and
\(\|w_\chi\|_2^2=1/E_\chi\). Any exact decoder \(w\) must satisfy
\(\mathbb E[wh_\chi]=1\), so Cauchy–Schwarz gives
\(\|w\|_2^2\ge1/E_\chi\). This proves the claimed minimum, for
\(E_\chi>0\). If \(E_\chi=0\), that nonzero character has no exact
\(L^2\) decoder. The accessibility conclusion is consequently correct in
its stated invariant population setting; the pointwise inequality alone
does not imply this decoder formula for an arbitrary nonsymmetric law.

## Why the executed interval certificate is rigorous

All numerical arguments below concern only the intended calls
\(0<v\le1\), radius \(R=10\), and spacing \(h=1/2000\).

**Arithmetic and elementary functions.** Each primitive arithmetic operation
uses a dedicated Decimal context with rounding toward the appropriate
infinity. Multiplication considers all four endpoint products; reciprocal
division excludes zero. `copy_negate` is exact. Repeated interval
multiplication is possibly overwide but remains an enclosure. Rational
arguments are converted with directed division, and no binary floating-point
input is used in the certificate. Local Python 3.10.12 `Decimal.exp` and
`Decimal.sqrt` docstrings explicitly state correctly rounded half-even
results. The adjacent representable Decimal on each side therefore encloses
the exact result; monotonicity permits endpoint evaluation. There is no
underflow or overflow in the used range. The 42-digit precision is explicit.

**Pi.** The arctangent series is alternating with decreasing terms at both
\(1/5\) and \(1/239\). Its rational partial sum and partial sum plus the
next term enclose the exact arctangent. The combinations of lower and upper
endpoints have the correct signs in Machin's identity. For a direct identity
check, \(\tan(2\arctan(1/5))=5/12\),
\(\tan(4\arctan(1/5))=120/119\), and the tangent subtraction formula gives
\(\tan(4\arctan(1/5)-\arctan(1/239))=1\); the angle is between zero and
\(\pi/2\). Thus the implemented identity gives \(\pi\), not a shifted
branch. The resulting interval is
\[
 [3.14159265358979323846264338327950288419716,
  3.14159265358979323846264338327950288419717].
\]

**Derivative bound.** Put \(g_n(x)=\operatorname{sech}^{2n}x\).
If \(P_{n,0}(t)=(1-t^2)^n\) and
\(P_{n,k+1}(t)=(1-t^2)P_{n,k}'(t)\), then
\(g_n^{(k)}(x)=P_{n,k}(\tanh x)\). Because \(|\tanh x|\le1\), the sum
of absolute polynomial coefficients bounds the derivative. The integer
recurrence in `derivative_bound` implements exactly this rule through order
four.

Let \(\gamma(x)=e^{-x^2/2}/\sqrt{2\pi}\). Its derivatives through order
four are \(\gamma,-x\gamma,(x^2-1)\gamma,(-x^3+3x)\gamma,
(x^4-6x^2+3)\gamma\). For \(j>0\), maximizing
\(|x|^je^{-x^2/2}\) gives \((j/e)^{j/2}\). In particular
\[
 \|\gamma^{(4)}\|_\infty
 \le{16/e^2+12/e+3\over\sqrt{2\pi}}<6.5<10,
\]
using \(e>2\), \(\pi>2\); the displayed lower derivatives give still
smaller bounds by the same argument. Thus Leibniz's rule for
\(\gamma(x)g_n(\sqrt v x)\), with \(v\le1\), is bounded by exactly
\(10\sum_{k=0}^4\binom4k\|P_{n,k}\|_{\ell^1}\), as implemented.
The computed bounds for \(n=1,\ldots,7\) are
\[
 9460,\ 96040,\ 570320,\ 2621600,\ 10329920,\ 36680320,\ 120782080.
\]
The interval square root of the singleton variance 1 extends slightly above
1 numerically; this causes no problem. The derivative estimate bounds the
true parameter, which is exactly 1, while the quadrature intervals enclose
its values.

**Simpson error.** On a panel of width \(2h\), Simpson's rule has error at
most \(h^5\|f^{(4)}\|_\infty/90\). One self-contained check is its Peano
kernel on \([-1,1]\): on \(0\le t\le1\),
\(K(t)=-(1-t)^3(1+3t)/72\), extended evenly. Its absolute integral is
\(1/90\); it arises by applying the integral-minus-quadrature functional to
\((x-t)_+^3/6\), since the functional annihilates cubics. Scaling and
summing panels gives \(Rh^4\|f^{(4)}\|_\infty/180\) on \([0,R]\).
Evenness doubles the error exactly as in line 107 of the frozen source.

**Tail and parameter enclosure.** Since \(0<g_n\le1\), the two tails
are bounded by \(2\int_R^\infty\gamma\le2\gamma(R)/R\). The latter
inequality follows by replacing 1 by \(x/R\) in the tail integral and
integrating \(x\gamma(x)=-\gamma'(x)\). The implementation encloses
\(2e^{-R^2/2}/(\sqrt{2\pi}R)\); its upper endpoint is less than
\(1.539\times10^{-23}\). Adding this nonnegative tail only to the upper
integral endpoint is correct. The outer variance is the interval
\(1-I_1\); evaluating all nodes with that interval encloses every possible
true variance in it. The same Simpson derivative bound holds throughout
that interval. No monotonicity shortcut or ignored variance uncertainty is
used.

Together these steps prove that each moment interval contains the exact
Gaussian moment. Ordinary outward interval evaluation of (8) then proves
the coefficient signs, even though some combinations suffer cancellation.

## Executed checks and retained evidence

Fresh run directory:
`data/generated/q1_population_mechanism_20260930/weak_factor_first_check_lkgufn3v/`.
Its `run_metadata.json` records the precommitted purpose, pass condition,
single-run resource bound, actual command, exit status, stderr, and source
hashes. From `/home/amir/Codes/PDE`, the command was:

```text
python studies/q1_population_mechanism_20260930/weak_factor_interval_certificate.py --output data/generated/q1_population_mechanism_20260930/weak_factor_first_check_lkgufn3v/certificate.json
```

Observed exit code 0; empty stderr; Python 3.10.12; elapsed 8.775215 seconds.
The output `certificate.json` has SHA256
`05eb824c36579c47eb760c5b32f343a9839640a7d3e35b20e1bcbfd6db8f1843`.
Its fields agree exactly with the author run after removing only
`elapsed_seconds`. The authoritative detailed endpoints are in those JSON
files. The following decimal endpoints are widened outward for readability:

| Exact leading quantity | Certified enclosure |
| --- | --- |
| \(F_\sigma/2=F_\tau/2\) | \([0.1924107034,\ 0.1924835650]\) |
| \(F_0/2\) | \([-0.0479569579,\ -0.0479535577]\) |
| \(F_y/2\) | \([2.8279836149,\ 2.8332964956]\) |
| \((vF_\sigma-a_1F_0)/(2v^2)\) | \([0.6312306069,\ 0.6314255540]\) |
| \((a_1F_y-a_2F_\sigma)/(2a_1^2)\) | \([5.8215753929,\ 5.8331171370]\) |

The last two bounds were computed using the same audited interval primitives
on the certified output: if `fs`, `f0`, `fy` denote the three first-row
accelerations, the exact expressions are
`(v*fs-a1*f0)/(v*v)` and `(a1*fy-a2*fs)/(a1*a1)`, with
`a1=I2` and `a2=4*(I2-I3)`. Their complete endpoints and the exact-run
comparison are retained in `verification.json`.

Additional actual checks:

- 95 exact-rational enclosure assertions for addition, subtraction,
  multiplication, and nonzero division over all pairs from
  \(\{-7/3,-1/7,0,2/9,17/4\}\) passed. They test positive, negative,
  zero, and repeating-decimal inputs, with exact Fraction comparisons of
  returned Decimal endpoints. The count and outcome are persisted in
  `verification.json`.
- A separately written standard-float Simpson implementation using 40,000
  panels on \([0,10]\) gave approximately \(0.19244713424\),
  \(-0.04795525784\), and \(2.83064005525\), each inside the certified
  interval. This was a diagnostic consistency check only, not evidence
  replacing the rigorous enclosure. No training simulation was run.
- All algebraic identities and all cases in the monotonicity argument were
  checked directly as described above. The source derivative rules were
  checked only after the missing actual q1 definitions were supplied.

## Remaining conditions and integration requests

There is no unresolved numerical or algebraic objection to this conditional
first-layer theorem. The following boundaries remain substantive:

1. Existence, uniqueness/equivariance, and sufficient differentiability of the
   canonical population flow are assumptions. This check establishes no
   finite-width-to-population limit or global population well-posedness.
2. The acquisition interval and the smallness threshold for
   \(\varepsilon\) are existential. There is no explicit numerical
   \(\varepsilon_0\), uniform time horizon, global fitting result, or
   all-time acquisition theorem.
3. The all-time inequality is architectural; the minimum-norm decoder
   formula additionally uses population symmetry. Neither implies
   second-layer acquisition, which is outside this assigned check.

For the supervisor's assembled theorem, incorporate the actual source
initialization and definitions used above, the Gaussian/Walsh normalization
step, and the analytic quadrature justification with the frozen code/output
hashes. Update the acquisition status to refer to the now-executed certificate;
the original note's final section correctly describes its earlier incomplete
package but is no longer the full current evidence. The source docstring says
the error proof is recorded in the study proof; that proof was absent from the
frozen note and is supplied explicitly in this report. These are integration
requests, not corrections to (3)–(12). No promotion approval is implied.
