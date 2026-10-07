# Audit of parameter dependence in the local decoder

2026-10-06. Scoped mathematical audit of the nine inputs listed at the end.
This is a conditional dependency audit, not a fresh proof of scientific
interfaces cited but not supplied in those inputs. No experiments, other-study
sources, review reports, maintained-book changes, or Git operations were used.

The current result establishes polynomial **internal** resource bounds at an
already admissible width. It does not establish polynomial total cost in the
underlying problem parameters, including the width required for its accuracy
claim. The assertion “no exponential dependence anywhere” is false for the
unrestricted computational interfaces and unproved for the scientific width
threshold, even after choosing an efficient activation such as tanh. These
limitations are already explicitly acknowledged in the current synthesis;
they must survive any shorter presentation of its cost table.

## 1. Nine shared parameters and the precise scope

Use only the following shared symbols. Other letters below are temporary
quantities defined where their particular accounting or comparison is used.

| Symbol | Meaning |
|---|---|
| \(n\) | Dense hidden width |
| \(m\) | Number of training inputs |
| \(d\) | Input dimension; the spanning training data have \(m\ge d\) |
| \(L\) | Fixed number of hidden layers, \(L\ge2\) |
| \(\gamma\) | Positive initial population feature-Gram gap |
| \(Y\) | Label RMS, \(\|y\|_2/\sqrt m\) |
| \(\beta\) | The explicit activation regularity envelope below |
| \(\delta\) | Failure probability |
| \(Z\) | The shared logarithm below |

For strip width \(a>0\) and layer activations \(\phi_j\), the definitions are

\[
\begin{aligned}
\beta&=\max\left\{10,1+\max_{j\le L}|\phi_j(0)|,16/a,
 \max_{j\le L,\,k=1,2}\sup_{|\operatorname{Im}z|\le a/2}
 |\phi_j^{(k)}(z)|\right\},\\
Z&=\log(en)+\log\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right).
\end{aligned}
\]

All bare constants in the current local resource table are universal. Its
\(\beta^{cL}\) factors are explicitly exponential in depth; at fixed depth
they are polynomial in \(\beta\). They are not uniform constants over
activation families whose \(\beta\) itself grows with \(m,d\), or
\(1/\gamma\). Likewise polynomial dependence on \(1/\gamma\) can become
exponential in another parameter if the actual gap decays exponentially in
that parameter. Neither change of parameter is excluded by displaying a
polynomial in the gap inverse.

The accuracy target is the entire sphere and physical trajectory, including
the endpoint, relative to an independently initialized dense run at its
dense-pair upper-certificate scale. It is not accuracy relative to a specified
realized dense trajectory. The complete original label intersection remains
assumed; \(16Ym/\gamma\le1\) is only a consequence. These are the stated
conditions in FAST_LOCAL_EFFICIENCY_RESULT.md, lines 28–65.

## 2. What the polynomial internal bounds do establish

In this section only, let \(R\) be the constructive source field/action
certificate and \(p\) the common word length, including argument ranges.
FAST_LOCAL_COMPOSITION.md, (1)–(5), uses

\[
\begin{aligned}
R&\le C\beta^{201L}(m+d+2)(1+m/\gamma)^2Z^{5/2},\\
p&\le C\beta^{110L}(d+1)(1+m/\gamma)Z.
\end{aligned}
\]

Its structural counts are

\[
\begin{aligned}
\text{retained and peak training/query bits}
 &\le C[R^2p+(L+1)Rp^2],\\
\text{metric initialization work}&\le CnR^5p^3,\\
\text{all compact update work}&\le C(R^5p^2+R^4p^3),\\
\text{one query work}&\le C(L+1)
 [s(Rp^5+R^2p^4)+R^5p^2+R^4p^3].
\end{aligned}
\]

Here \(s\) is the explicitly chosen number of rows per statistical block.
The source-generation terms are separately displayed at lines 133–144 and
are also covered by the final initialization envelope. The word and seed
costs therefore do not hide constant-bit reals, an uncounted time integrator,
or an enumerated sphere grid. Large coefficient magnitudes require their
logarithms in bit precision; an exponentially small artificial noise floor
does not alone imply exponentially many arithmetic iterations. The local
source recipe makes this distinction explicitly in
FAST_FINITE_SOURCE_BRIDGE.md, (20)–(23), lines 285–350.

For example, \(R^2p\) has powers
\(\beta^{512L}(m+d+2)^2(d+1)(1+m/\gamma)^5Z^6\), and
\(nR^5p^3\) has powers
\(n\beta^{1335L}(m+d+2)^5(d+1)^3(1+m/\gamma)^{13}Z^{31/2}\).
Replacing \(d+1\) by \(m+d+2\) and allowing the displayed slack gives
the synthesis's memory and initialization bounds. These are polynomial in
\(m,d,1/\gamma\), \(\beta^L\), and \(Z\), with explicit powers.

The statistical gate itself need not hide an exponential. In the same local
notation let \(\alpha\) be a confidence share, let \(P\asymp R^2\) be the
actual complete pair count, let \(B_F\ge1\) cap its tests, and let
\(\eta\) be scalar noise. The assembly chooses

\[
K_* =\max\left\{1,\frac{P}{2\alpha}
 \log(1+B_F^2/\eta^2)\right\},\qquad
K_*\le\widehat K_*\le2K_*,\qquad
s=\left\lfloor\frac{n}{128\widehat K_*}\right\rfloor,
\quad n\ge512\widehat K_*.
\]

The chosen precision gives \(K_*\asymp R^2p/\alpha\). Consequently a
sufficient local sampling gate is

\[
n\ge C\alpha^{-1}\beta^{512L}(m+d+2)^2(d+1)
 (1+m/\gamma)^5 Z^6.
\]

The stated confidence allocation permits \(\alpha=c\delta\) for a fixed
positive absolute \(c\). FAST_FINITE_PASSIVE.md fixes the transfer threshold
at \(q_0=1/64\), both conditional comparison failure shares at most
\(1/8\), and the conditional Gram failure share as a fixed constant.
Thus those steps multiply failure probabilities only by absolute constants;
they do not force \(\alpha\) to be of order \(\delta^2\). With this
allocation the displayed sampling coefficient is \(C\delta^{-1}\).
This reconstructs the stated interface, not the omitted full proof of its
all-prefix information theorem.

This is an implicit polynomial-times-logarithm gate, not a condition of the
form \(\log n\ge\operatorname{poly}(m,d,1/\gamma)\). For temporary
nonnegative quantities \(A,H\), a gate
\(n\ge A[\log(en)+H]^6\) is satisfied by
\(n\ge C(A^2+AH^6+1)\): use
\((u+v)^6\le32(u^6+v^6)\) and
\([\log(en)]^6\le C\sqrt n\). Thus this gate admits a polynomial
sufficient solution in its coefficient and logarithmic offset. It does not
resolve the separate scientific gates.

Evidence: FAST_LOCAL_COMPOSITION.md, lines 50–104, 126–207, 216–271;
FAST_LOCAL_EFFICIENCY_RESULT.md, equations (1)–(5).

## 3. Computational interfaces that prevent an unconditional total bound

Every phase adds its evaluator-call count times the actual supplied
activation/data-evaluation work. Peak space adds one live evaluator workspace;
retained code, original data, scales and certificates add their description
lengths. Certificate production or verification, query/time acquisition and
output writing are separate costs. No polynomial bound for these functions
or descriptions follows from the nine shared parameters.

This is a mathematical obstruction to the unrestricted claim, not a suspected
missing factor in the internal arithmetic. COST_CONTRACT.md, lines 228–236,
exhibits \(\phi(x)=\sin x+c\), with a bounded noncomputable real
\(0<c<1\): its strip envelope is uniformly bounded, but evaluating at zero
would compute \(c\). Within the supplied finite-evaluator interface,
noncomputable examples are excluded by the interface itself; the work and
description size of the supplied computable evaluator are still unrestricted.
An assumption of a supplied evaluator is not an assumption that it runs in
polynomial time. Exact finite input descriptions can also have arbitrarily
large length at the same geometric parameters.

For tanh the activation issue is repaired concretely. At \(p\) bits of
requested precision and argument length,
FAST_TANH_EVALUATION.md proves \(O(p^3)\) bit work and \(O(p)\) scratch,
and its call-count substitution fits all current internal envelopes. This
does not supply the missing input or certificate algorithms. The population
Gram-gap lower bound and analytic strip certificate are explicitly not free
quadrature or optimization oracles.

Evidence: FAST_LOCAL_EFFICIENCY_RESULT.md, lines 148–189;
COST_CONTRACT.md, lines 151–236; FAST_TANH_EVALUATION.md, all 77 lines.

## 4. Tiny labels: precision is bounded only after a width restriction

For a temporary normalized precision \(p\), the following raw
absolute-precision label allowance suffices:

\[
p+\lceil\log_2(16\sqrt m)\rceil
 +\lceil\log_2\max(1,1/Y)\rceil
\]

fractional bits. On the nonzero branch \(nY\ge1\), the last logarithm is
at most \(\log_2n\). Therefore this term does not refute the internal
polynomial bound on its stated domain. But the same condition is the width
requirement \(n\ge1/Y\). It does not give a bound independent of label
scale, or a polynomial bound in the *encoding length* of that scale.

For example, an admissible label family with \(Y\le e^{-m}\) must use
\(n\ge e^m\) under this construction; with
\(Y\le2^{-2^m}\), its gate is \(n\ge2^{2^m}\). These are conditional
illustrations of the explicit gate, not assertions that every such family
satisfies the full inherited label/data assumptions. Nothing in the supplied
cost interface imposes a lower bound on nonzero \(Y\) in terms of
\(m,d,\gamma\). The algorithm generates \(n\) source rows, so choosing an
exponentially large admissible width has an actual width-dependent work
cost even though the resource formula is polynomial in the chosen width.

The output scale also has a representation cost. A floating exponent can
encode tiny \(Y\) compactly, while a fixed-point output relative to \(Y\)
needs the corresponding leading fractional positions. The exact zero-label
branch requires a supplied way to know it is zero; no equality-deciding
procedure for arbitrary real oracles was proved.

Evidence: COST_CONTRACT.md, lines 23–28 and 206–226;
FAST_FINITE_SOURCE_BRIDGE.md, lines 320–350;
FAST_LOCAL_EFFICIENCY_RESULT.md, lines 183–205.

## 5. The exact remaining accuracy comparison

In this section only, write \(b_n\) for the inherited dense-pair certificate
at the fixed confidence allocation. Let \(R,K_*\) have the local meanings
above. The actual finite estimator obeys FAST_FINITE_PASSIVE.md, (30):

\[
\sup_{t,x}|\widehat f(t,x)-f_n^{\rm independent}(t,x)|
\le2b_n+
 CY\mathcal P\sqrt{(R+1)(K_*+1)/n}+CYn^{-10}.
\]

Its sufficient fixed-depth propagation factor is explicitly

\[
\mathcal P=(1+\mathcal C)
 [C(1+\mathcal B)^2(1+\mathcal C)(1+\beta)^2]^{L+2}.
\]

Here \(\mathcal B\ge2\) caps the passive feature values, and
\(\mathcal C\) bounds the normalized readout RMS and the posterior
mean-plus-learned-displacement operator norms. The supplied bound is
\(\mathcal B\le C\beta^{110L}\sqrt{d+1}Z^{3/2}\).
The note says \(\mathcal C\) is polynomial in its original physical
constants and \(\sqrt{(L+1)/\delta}\), but does not display its complete
major-parameter monomial. This is sufficient to identify the point where
it enters, not to supply missing detailed physical estimates.

To deduce the advertised \(3b_n\) bound from this particular displayed
estimate, the additional explicit test is

\[
C\mathcal P\sqrt{(R+1)(K_*+1)}+Cn^{-19/2}
 \le \frac{\sqrt n\,b_n}{Y}.                       \tag{A}
\]

This is the exact bound-level absorption condition, after division by
\(Y/\sqrt n\). It is not enough to write the additional error as
\(n^{-1/2+o(1)}\). Also, substituting
\(\sqrt{K_*+R+1}\) for
\(\sqrt{(R+1)(K_*+1)}\) would be invalid: the former controls the
population/full-array comparison, while the latter is the actually
implemented vector of block-median estimates. The source explicitly corrects
this distinction at lines 533–541 and 693–697.

For fixed parameters and a width-independent physical \(\mathcal C\),
the available envelopes give
\(\sqrt{(R+1)(K_*+1)}\le C R^{3/2}\sqrt{p/\alpha}\),
with logarithmic power \(17/4\). The general feature cap contributes the
additional power \(3(L+2)\) through \(\mathcal P\). Thus an available
bound on the left side of (A) has logarithmic power
\(3L+41/4\), before any extra width dependence of a separately supplied
physical bound. A complete parameter audit must keep the associated
coefficient as well as this degree.

After identifying the missing certificate formula, scope was explicitly
expanded to RESULT.md in full; no links from it were followed. Its lines
108–123 supply the following actual right side of (A), at a fixed confidence
share \(\delta_0\) of \(\delta\):

\[
\frac{\sqrt n\,b_n(\delta_0)}Y
 =c_0 e^{c_1Y^2\sqrt{\log(en)}}
 \sqrt{8\log\frac{8(n+1)(1+2n)^d}{\delta_0}}
 +\frac{c_2}{\sqrt n}.                              \tag{A'}
\]

The positive constants \(c_0,c_1,c_2\) distinguish the three occurrences
of the source's \(C\). Unlike the constants in the algorithmic resource
table, their inherited meaning permits dependence on the entire fixed
problem, including \(m,d,\gamma,Y\), activation and confidence. No
polynomial dependence is established for them. Equations (A) and (A') are
the exact additional bound-level test; they expose both the amplification
and the inherited constants that the resource table does not resolve.

The certificate has fixed-problem logarithmic power \(1/2\): for
\(n\ge e\), its square-root logarithm is at least
\(2\sqrt{d+1}\sqrt{\log(en)}\), since
\(\log(n+1)+d\log(1+2n)\ge(d+1)\log n\) and
\(\log n\ge\tfrac12\log(en)\). It is also bounded above by a
fixed-problem multiple of \(\sqrt{\log(en)}\).

For the following sufficient comparison only, let
\(A=2c_0\sqrt{d+1}\), let \(c=c_1\), and choose \(D>0\) and
\(q>1/2\) so the left side of (A) is at most \(DZ^q\).
The general cap gives the sufficient choice \(q=3L+41/4\) under the
width-independent physical bound just stated. Put
\(H=Z-\log(en)\) and \(x=\sqrt{\log(en)}\). Comparing this upper
envelope to the certified lower bound on the leading term in (A') gives
the exact sufficient inequality

\[
cY^2x\ge
 \log(D/A)+(2q-1)\log x+q\log(1+H/x^2).             \tag{B}
\]

If \(D\ge A\) and \(x\ge e\), satisfying (B) implies

\[
x\ge\frac{2q-1}{cY^2},\qquad
n\ge\exp\left(\frac{(2q-1)^2}{c^2Y^4}-1\right).     \tag{C}
\]

Indeed every term dropped from the right of (B) is then nonnegative and
\(\log x\ge1\). This elementary lower bound on the onset of *this
sufficient comparison* already has exponential inverse-label dependence.
For a family in which \(A,D,c,H,q\) are fixed with \(D\ge A\), its
larger crossing has \(x\) of order \(Y^{-2}\log(1/Y)\).
To check the order, divide (B) by \(2q-1\) and put
\(t=cY^2x/(2q-1)\). At the larger equality crossing,
\(t=\log(1/Y^2)+\log t+O(1)\); the \(H/x^2\) term tends to zero.
Consequently the logarithm of width has order
\(Y^{-4}\log^2(1/Y)\). These family assumptions are essential; (A')
expressly permits its coefficients to depend on \(Y\) and the other data.

If, additionally, \(c\) stays bounded above across a family and the
comparison hypotheses hold, the inherited cap \(Y\le\gamma/(16m)\)
turns (C) into an exponential lower bound in \((m/\gamma)^4\) for
this absorption test. The current packet does not justify claiming that
uniform coefficient assumption, so this is a conditional mechanism, not
a proved necessary width for all instances. No estimate here is a lower
bound against a different algorithm or a sharper analysis.

This calculation pinpoints the issue: logarithmic resource bounds can be
fully polynomial while the width at which their advertised accuracy
comparison applies is not polynomially controlled. Besides (A), the inherited
scientific source/fitting threshold is unquantified. Improving (A) alone
does not resolve that separate gap.

Evidence: RESULT.md, lines 108–123 and 146–151;
FAST_FINITE_PASSIVE.md, (2)–(7), (28), (30), lines 43–98,
469–487, 533–541 and 662–681; FAST_LOCAL_EFFICIENCY_RESULT.md, lines
191–205; FAST_COMPOSITION.md, lines 388–398.

## 6. A genuine narrow reduction for tanh

For tanh one may use the fixed passive cap \(\mathcal B=2\) and
\(\psi_\ell=\tanh\) directly: \(|\tanh|\le1\),
\(|\tanh'|\le1\), and \(|\tanh''|\le2\). All uses of the passive
value/derivative cap in (3), (25), (27) and (28) remain valid. This removes
the artificial \(Z^{3(L+2)}\) contribution to the sufficient statistical
amplification factor above, leaving logarithmic power \(17/4\) from
\(R^{3/2}\sqrt p\), when the physical operator/readout bound is
width-independent. It is a reduction of this statistical upper envelope,
not a change to the generic analytic-activation theorem or a proof of a
polynomial crossover. No synthesis or algorithm was edited for this audit.

Another already proved saving should not be dropped in implementation.
With \(R\) again the source field certificate and \(p\) its word length,
the query stream has the sharper structural bound
\(C(L+1)n(p^4/R+p^3)\), obtained from
\(s\le Cn/(R^2p)\). The published major-parameter table replaces it by
\(C(L+1)n(p^4+p^3)\). Eliminating the fourth power uniformly would need
an additional valid relation between the actual \(p\) and \(R\); the
current assembly expressly does not assume \(p\le R\).

## 7. Verdict and read provenance

| Claim | Verdict |
|---|---|
| Universal polynomial internal cost in the displayed parameters at admissible width | Supported by the stated conditional interfaces and reconstructed accounting |
| Same internal envelopes include a certified tanh evaluator | Established by the supplied elementary evaluator proof |
| Total costs of all allowed activation/data/certificate interfaces are polynomial in the nine parameters | False without extra computational/encoding assumptions |
| The raw-label precision adds an uncharged power of \(1/Y\) on \(nY\ge1\) | False; its logarithm is explicitly charged and bounded there |
| The nonzero width gate is harmless uniformly over arbitrarily small labels | False; it requires \(n\ge1/Y\) |
| Scientific success and certificate absorption occur at polynomial width in all problem parameters | Unproved; (A) and the inherited source threshold remain necessary proof obligations |
| The current work proves that every valid decoder needs exponential width or query time | Not established; no such impossibility argument was supplied |

The source claims that the local assembly is internally checked. This audit
does not infer independence or correctness of an unprovided review from that
status text. Older frozen component wording is interpreted using the current
synthesis's explicit status statement, without importing linked reports.

All scientific lines of the following files were read; truncated aggregate
output was repaired before analysis. The hashes identify this audit's inputs.

| Input | SHA-256 |
|---|---|
| FAST_LOCAL_EFFICIENCY_RESULT.md | `9d28ab126f94a4105866773fb897c89ceeedcb5170d6ff7282b7b08c0985f4e3` |
| FAST_LOCAL_COMPOSITION.md | `7d101fd08dd5e612963263bb5dd565b146d4ca3b330adb074bd5673b77f40bb2` |
| FAST_FINITE_PASSIVE.md | `7f298bc637afffc207375692ee725290e752cdeb818b42f82563646f74416777` |
| FAST_FINITE_SOURCE_BRIDGE.md | `7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6` |
| FAST_TANH_EVALUATION.md | `55f4128718603b64371fc0f6e74968cc992aa01b181c958044f668a6a1a3e618` |
| COST_CONTRACT.md | `3e29f96ef535ec58dc6b70bcdbd304ea6e9074579ad7652c9f377f15c948d03c` |
| FAST_COMPOSITION.md | `77f5deaffcd7133e6bafb0c1b2e8cf216399bbf787503812e8667ea2e5da53cc` |
| QUADRATIC_RESOURCE_RESULT.md | `e753d74e80bb4061d10c2c7f735e33991382d93f27c6c638a35c80afac695ccd` |
| RESULT.md, after explicit scope expansion | `c76aedb9ae7351fa3a0582d7f85a47c6b3e0765e83d16d9021e19ec6dcfc0d65` |

Research-audit, rigorous-math and canonical-notation instructions, including
the neural-network reference, governed the distinction between conditional
internal bounds, unrestricted interfaces and missing width guarantees.
