# Independent component check of physical query rounding

2026-10-06. Bounded reconstruction of the external-grid change in
`FAST_PHYSICAL_QUERY_GRID.md`. The task is to check replacement of the
decoder-sensitivity mesh by a mesh controlled by the true dense
prediction. Row precision, the source, and the statistical rows per block
are held fixed. This is not a new source audit, full-decoder proof, or
promotion review. Only this report is written; no experiment or Git
operation was performed.

## Inputs and verdict

The complete original target was read at SHA-256
`7947031a22ab1c8583023942d899ec1050149110a241d05bf29f01961d6c3641`.
The complete assigned scientific dependencies were:

| Input | SHA-256 |
|---|---|
| `FAST_UNIFORM_QUERY.md` | `e59f805980ddc664794eee8c0f310f51667e94592d4ee502978663e77c64bcd9` |
| `FAST_COMPOSITION.md` | `77f5deaffcd7133e6bafb0c1b2e8cf216399bbf787503812e8667ea2e5da53cc` |
| `PHYSICAL_PARAMETER_ACCOUNTING.md` | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| `SANE_TAYLOR_SOURCE.md` | `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af` |

No other scientific artifact, study history, or review was read. Current
required proof, research-audit, and canonical-notation skills, including
the neural reference, were applied.

The original needed two finite-interface clarifications: sphere
approximants must belong to a prescribed finite dyadic lattice, and time
rounding must avoid exact floor tests on arbitrary real inputs while using
only available patch coefficients. Both were supplied in the corrected
target, read completely at SHA-256
`50a5e22032a31061e8e1725c061238021e5f265b35037562e68001c698944425`.
The correction uses a fixed coordinate lattice, a certified lower time
approximation followed by a finite floor, and only an already acquired
adjacent patch at ambiguous boundaries.

**Verdict: PASS for the corrected external-grid component, conditional
on the imported source/decoder and dense-event interfaces.** No scientific
input beyond the assignment is needed for this component. It reduces the
median block count and coordinatewise stream work by one factor of \(R\).
It does not reduce \(s\), the working precision, or the retained-source
precision, and it does not prove polylogarithmic query work.

## Dense prediction regularity

Work on the stated uniform operator/readout event and on the nonzero-label
branch \(Y>0\). For a unit input \(v\), the first matrix has
\(\|A\|_{\rm op}/\sqrt n\le C\), each hidden matrix has
operator norm at most ten, and each activation is \(\beta\)-Lipschitz.
Thus forward subtraction gives

\[
 \frac{\|h^{(L)}(v)-h^{(L)}(v')\|_2}{\sqrt n}
 \le C\beta(10\beta)^{L-1}\|v-v'\|_2
 \le C\beta^{2L}\|v-v'\|_2.
\]

Multiplying by the readout RMS bound
\(SH_L\le16Y(m/\gamma)\beta^{3L}\) gives a normalized prediction
Lipschitz constant at most \(C(m/\gamma)\beta^{5L}\), safely
covered by the displayed \(\beta^{20L}(1+m/\gamma)\) envelope
with its numerical slack. The same uniform bound passes to the fitted
limit. The zero-label branch is identically zero and needs no division
by \(Y\).

For time, the displacement norm is exactly the first-matrix normalized
Frobenius norm plus hidden Frobenius norms and readout RMS norm stated in
the Taylor source. Equation (8) of the supplied parameter accounting
gives \(\|F\|\le Y\beta^{12L}\) and
\(\operatorname{Lip}_u f(\cdot,v)\le\beta^{8L}\).
Since \(\tau=(\gamma/m)t\), the chain rule gives

\[
 \frac{|\partial_\tau f_n((m/\gamma)\tau,v)|}{Y}
 \le (m/\gamma)\beta^{20L}.
\]

The time-rescaling factor is therefore included correctly. These are
physical-reference estimates; no history inverse or continuity of the
rounded numerical decoder has entered. Beyond the finite horizon, the
imported fitting tail is used instead of extending a time grid to
infinity.

## Finite codes and acquisition chronology

In the corrected sphere construction the lattice spacing is
\(2^{-p-6-\lceil\log_2(d+1)\rceil}\). Finite coordinate access
at a slightly finer precision can choose a lattice vector \(z\) with
\(\|z-v\|_2\le2^{-p-3}\), without resolving an exact real tie.
All such vectors have coordinates in a fixed bounded interval. There are
at most \(\exp(Cd[p+\log(d+2)])\) possible codes.
Since \(\|z\|_2\ge1/2\),

\[
 \left\|\frac z{\|z\|_2}-v\right\|_2
 \le |1-\|z\|_2|+\|z-v\|_2
 \le2^{-p-2}.
\]

Only the dyadic vector is the code. Its normalized representative is a
well-defined exact sphere point; evaluating its square root and division
to the existing \(w=CR\Theta\) precision is a deterministic
fixed-context numerical error. Coarse external rounding does not license
coarse normalization arithmetic.

Let \(\xi\in[0,1]\) be the current patch fraction and let
\(\Delta=2^{-p}\). Choose a certified lower approximation \(a\)
with \(0\le a\le\xi\) and \(\xi-a\le\Delta\); clipping
an initial lower enclosure at zero enforces this at the left endpoint.
Then \(\widehat\xi=\Delta\lfloor a/\Delta\rfloor\) is a
finite rational calculation and satisfies

\[
 0\le\widehat\xi\le\xi\le1,
 \qquad 0\le\xi-\widehat\xi\le2\Delta.
\]

Thus the code remains in the current patch. Its normalized physical-time
error is at most \(2\Delta\), because the Taylor patch length is
at most one (indeed its stated ordinary length is at most \(1/8\)).
Both boundary labels may be included, but only an already acquired patch
is used when time access is ambiguous. A frozen endpoint contributes one
extra time label for each sphere code.

The required chronology is supplied explicitly. The Taylor recurrence
computes all current-patch coefficients from its anchor in increasing
coefficient order. Interior evaluation then changes scalar polynomial
weights; it makes no new initialized-matrix call. The composition interface
exposes this acquired current parameter polynomial/rank list to passive
queries. Replacing \(\xi\) by \(\widehat\xi\) therefore needs
neither the next patch nor replay of a preceding patch. Historical fields
continue to use their creation-time scalar arguments. This check does not
grant a query access to future unacquired coefficients.

Take a sufficient \(p\) so that the spatial error plus the two-mesh
time error, multiplied by the physical Lipschitz envelope, is at most
\(\varepsilon/8\), where \(\varepsilon=n^{-10}\). It needs
only \(O(\log(en)+L\log\beta+\log(1+m/\gamma))\) bits, with
the stated dimension/patch-count slack. In particular \(p=O(\Theta)\).
Including at most \(P\) current-prefix choices, \(H\) patch labels,
and the time-grid points gives the explicit count

\[
 \log|\mathcal A|
 \le C d[p+\log(d+2)]+Cp+C\log(H+2)+C\log(P+2)
 \le C(d+1)\Theta.
\]

The last inequality uses the imported dimension/count logarithms in
\(\Theta\), with \(P\le CR^2\). The grid is not enumerated.

## Accuracy and probability transfer

Let \(a(v,\tau)\) be any qualifying available code and let the
implemented new decoder return the old fixed-context computation at that
code. On the uniform code-accuracy event, its prediction error obeys

\[
 \begin{split}
 |\widehat f(a(v,\tau))-f_n(v,\tau)|
 &\le |\widehat f(a(v,\tau))-f_n(a(v,\tau))|\\
 &\quad+|f_n(a(v,\tau))-f_n(v,\tau)|.
 \end{split}
\]

The first term uses the unchanged source/posterior/decoder comparison at
a code. The second is at most \(Y\varepsilon/8\) through the finite
horizon, by the physical estimates. The frozen branch uses the unchanged
tail allowance. This proves the same prediction certificate with its
existing external-rounding budget. It makes no claim that uncoded
intermediate moments or decoder outputs vary continuously.

Conditioning on the complete source and earlier stage seeds fixes one
guarded context per external code at the next stage. That stage's seed
is independent, exactly as required by the reachable-context lemma.
The per-coordinate statistical failure is still \(2^{-J/2}\), at
the same moment tolerance determined by \(s\). Taking odd

\[
 J\ge C[\log|\mathcal A|+\log(Q(R+1)/\delta)+1]
\]

therefore admits the sufficient bound \(J=O((d+1)\Theta)\).
The generator's per-test error is reduced by the same finite count.
The common Gaussian exception is still charged once per stage stream;
coordinatewise passes restart the identical stream and introduce no new
tail event. Source and independent-reference good events retain their
separate confidence shares. Adaptive later queries are covered by this
single event over all codes.

Writing \(N=Js\), the direct generator accounting is

\[
 A=C(Dw+F+\log(N+2))\le CR^2\Theta,
 \quad F=O((d+1)\Theta),\quad\log(N+2)=O(\Theta).
\]

This establishes the claimed bound without needing a lower bound
\(D\asymp R\). More specifically, \(D\ge1\), \(d\le R\),
and \(w=CR\Theta\) control the other terms by the row-word
allowance; \(D\le CR\) supplies its upper bound. The stage-seed
allowance \(CR^2\Theta^2\), working precision, Gaussian sampler,
and one-pass tests all remain valid. The block size \(s\) and its
width gate are unchanged.

## Resource and parameter arithmetic

With \(Q=O(L+1)\), one coordinate stores \(Jw\), hence
\(O((d+1)R\Theta^2)\), bits. Current coefficients cost
\(O(R^3\Theta)\); retained independent seeds cost
\(O(QR^2\Theta^2)\). Earlier outputs and other row scratch fit the
same existing bounds. The displayed peak query count follows, with actual
input/evaluator/certificate descriptions and evaluator scratch additional.

There are \(O(R)\) coordinate passes per stage, giving
\(O(Qs(d+1)R\Theta)\) actual packet evaluations. At unchanged
cost \(O(R^5\Theta^4)\) per packet, stream work is
\(O(Qs(d+1)R^6\Theta^5)\). Reused preparation costs
\(O(QR^7\Theta^3)\). Sorting costs
\(O(QRJ\log(J+2)w)\) and is covered for \(s\ge1\).
The incoming context and prepared coefficients must remain fixed until
all coordinate medians are complete, as the algorithm specifies.

Each packet uses \(O(R)\) activation/data calls. Thus the call count is
\(O(Q[s(d+1)R^2\Theta+R^2])\), with the second term for reused
preparation. Multiply by the actual evaluator work at \(CR\Theta\)
precision and add one live evaluator workspace; no regularity hypothesis
is being substituted for evaluator cost.

For the following arithmetic only, abbreviate
\(M=m+d+2\), \(G=1+m/\gamma\). Substitute the target's
\(R\le C\beta^{201L}MG^2Z^{5/2}\),
\(\Theta\le C\beta^{102L}GZ\),
\(Q\le C\beta^L\), and \(d+1\le M\):

| Term | Activation power | Data power | Gap-ratio power | Logarithmic power |
|---|---:|---:|---:|---:|
| Stream, with \(s\le n\) | \(1717L\) | \(M^7\) | \(G^{17}\) | \(nZ^{20}\) |
| Reused preparation | \(1714L\) | \(M^7\) | \(G^{17}\) | \(Z^{41/2}\) |
| Stream evaluator calls | \(505L\) | \(M^3\) | \(G^5\) | \(nZ^6\) |
| Preparation evaluator calls | \(403L\) | \(M^2\) | \(G^4\) | \(Z^5\) |

For example, the stream activation exponent is
\(1+6\cdot201+5\cdot102=1717\), and preparation uses
\(1+7\cdot201+3\cdot102=1714\). The corresponding powers of
\(Z\) are \(6(5/2)+5=20\) and \(7(5/2)+3=41/2\).
The common \(\beta^{1720L}\) work envelope in (8) is therefore
valid. Retaining its separate preparation term avoids any hidden width
absorption. The evaluator envelope is also correct with its preparation
addition and unchanged precision.

These are improvements within the stated conditional composition. The
scientific source event, posterior transport, statistical-error comparison,
and sufficiently-large-width qualifications remain imported obligations.

## Final narrow recheck

The final target hash is
`bd275d6163f54e0668d55be576c789bdeedae2e447a3dffe0881c4cc7defaa0a`.
Its only further changes explicitly clamp the finite time code to
\([0,1]\) and replace the generator-domination wording by the direct
upper bound for \(A\). Both changed passages were read and verified.
Clamping cannot enlarge the time error for a true fraction in \([0,1]\),
and the direct generator bound is precisely the sufficient bound derived
above. The original confidence, coordinate, and stage logarithms are
covered by the existing \(w=CR\Theta\) term and universal constant.

The final verdict remains **PASS within the assigned conditional component
scope, with no unresolved finding**. Earlier hashes identify the two
narrow clarification stages and are not alternative current targets.
