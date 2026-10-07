# Bounded assembly check of the polynomial-width continuation

2026-10-07. This is a bounded assembly check, not a fresh isolated promotion
review or a check of the full decoder theorem.

The checked version of `POLYNOMIAL_WIDTH_RESULT.md` has SHA-256
`9aa112abc9829a0b06d82d5141cce29bc4f5e6eb5268e32066fe7416ee0f01b3`.

**Verdict: equations (1)–(4) and the stated scope of the unchanged tables
pass. One confidence-dependence qualification should be made explicit.**
The sufficient envelope (4) is polynomial in \(\delta^{-1}\), not in
\(\log(1/\delta)\). This remains a limitation for the stronger target
specified in POLYNOMIAL_SOURCE_WIDTH, Section 7. It is distinct from the
two missing scientific bounds identified in the assembly.

## Inputs and scope

I read the current assembly completely, the complete
`EXPLICIT_FITTING_WIDTH.md`, `GAP_REFINED_PHASE_COSTS.md`, and
`FINITE_COMPLEX_MOMENT_GATE.md`, and used the already read radius candidate
and its eight authorized sources. The three additional source hashes are:

| Source | SHA-256 |
|---|---|
| EXPLICIT_FITTING_WIDTH.md | `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d` |
| GAP_REFINED_PHASE_COSTS.md | `817617951efb926d2729cd7f20eaccf7cb5c4e25e17eb531502c8b2618e017bc` |
| FINITE_COMPLEX_MOMENT_GATE.md | `04e428c5d31b56ebd05c10535fbb7cf394475e169958dd96a2cae8c05f756bb0` |

I did not read linked reviews, insertion derivations, or weak-decoder-route
files. Their scientific validity is outside this assignment. The check
uses the required rigorous-proof and canonical-notation instructions
already read. Only this report is written.

## 1. Fitting and radius formulas

Equation (1) is exactly the sufficient envelope in
EXPLICIT_FITTING_WIDTH (12). It preserves the unweighted population gap
\(\gamma\), so the inverse normalized gap is \(m/\gamma\).
The fitting source's event depends only on initialization and inputs and
supports every label vector in its original allowance. Consequently the
assembly correctly states both the individual-width probability and the
simultaneous-in-label deterministic consequence. It does not identify that
event with the trained-source event.

Equation (2) is the repaired physical-time half-width
\[
 r_t=[\beta^{100L}(1+\gamma/m)\sqrt{\log(en)}]^{-1}.
\]
In normalized time \(\tau=(\gamma/m)t\), it becomes
\[
 r_\tau=[\beta^{100L}(1+m/\gamma)\sqrt{\log(en)}]^{-1}.
\]
The unchanged old step is \(h_0=r_\tau/64\), whereas the radius
candidate in the patch minimum is \(r_\tau/8=8h_0\). Thus the
minimum stays at \(h_0\). The statements that the basic repair leaves
the partition, degree and inherited resource bounds unchanged are valid
conditional substitutions. They do not establish the source event or
the downstream decoder comparison at a particular width.

The optional additional shrinkage by the moment order \(p\) is correctly
separated from this basic repair. Taking \(p\) equal subdivisions of each
old certified patch gives exactly \(pH\) patches and needs only an
additional \(O(\log p)\) in the degree. The assembly explicitly says
that the complete table is not being reused for that modified partition.
Its finite-complex-correction statement retains the stopped-path
hypothesis. The conditional collision statement also retains its
distinct-neuron-moment hypothesis. No full source probability is inferred
from either statement.

## 2. Explicit removal of the logarithmic width dependence

For this calculation define
\[
 B=\beta^{100L},\qquad r=m/\gamma,\qquad
 z=\log\left(e+\frac{(m+d+2)B(1+r)}\delta\right),
 \qquad \ell=\log(en)\ge1.
\]
Then \(Z=\ell+z\le(1+z)\ell\), since \(z\ge0\).
Writing the numerical constant in (3) as \(C_3\), its nonlogarithmic
prefactor is
\[
 A=C_3\delta^{-1}\beta^{512L}(m+d+2)^2(1+r)^2.
\]
For \(\ell\ge1\), the derivative of
\(\ell^6e^{-\ell/2}\) has the sign of \(6-\ell/2\). Its maximum
is therefore at \(\ell=12\), and
\[
 \frac{\ell^6}{\sqrt n}
 =e^{1/2}\ell^6e^{-\ell/2}
 \le C_*:=e^{1/2}(12/e)^6.
\]
Hence, for every integer \(n\ge1\),
\[
 AZ^6\le A(1+z)^6C_*\sqrt n.
\]
It follows that
\[
 n\ge A^2C_*^2(1+z)^{12}
 \quad\Longrightarrow\quad n\ge AZ^6.
\]
Substitution gives exactly (4), with its absolute constant chosen at
least \(C_3^2C_*^2\). This proves the implication for every larger
width as well, despite the appearance of \(n\) in \(Z\) on the
right of (3). No monotonicity assumption or eventual parameter absorption
is being used. The powers \(1024L\), four, four, and twelve in (4)
are correct.

Equation (3) itself matches GAP_REFINED_PHASE_COSTS (9), including its
factor \(\delta^{-1}\) and the original \(Z\). The separate
\(n\ge d\), \(nY\ge1\), and horizon conditions are not implied
away or altered by this calculation. The small-label option is described
only as a numerical refinement and does not claim uniform source
probability as \(Y\) tends to zero.

## 3. Confidence qualification and presentation correction

The phrase “the ordinary numerical gates are polynomial too” is correct
when failure probability is parameterized by \(\delta^{-1}\), or when
confidence is fixed. It does not establish polynomial dependence on
\(\log(1/\delta)\), which POLYNOMIAL_SOURCE_WIDTH, Section 7,
explicitly included in the full target. Equation (3) still has an
algebraic inverse-confidence factor, and the conservative explicit
envelope (4) squares it.

For fixed remaining parameters, the displayed envelope scales as
\(\delta^{-2}[\log(1/\delta)]^{12}\). No fixed power of
\(\log(1/\delta)\) bounds this as \(\delta\downarrow0\).
This is a limitation of the current sufficient gate, not a lower bound
on what a different block-sampling proof or construction could achieve.

A sufficient wording correction is:

> Equations (3)–(4) are polynomial in inverse confidence \(1/\delta\).
> They do not yet meet a target polynomial in \(\log(1/\delta)\);
> that stronger confidence dependence remains to be improved in addition
> to the two scientific gaps below.

The heading identifying “two indispensable gaps” can be qualified as
“two indispensable scientific gaps” to make that distinction explicit.
Nothing in the algebra needs to change.

There is also a rendering issue in the checked version: several inline
formulas use literal parentheses, such as `(L\ge2)` and `(n\ge1)`,
instead of mathematical delimiters `\(L\ge2\)` and `\(n\ge1\)`.
Those should be repaired consistently. This is a presentation correction,
not a change to the mathematical conclusions.

## 4. Untouched table and unresolved implications

GAP_REFINED_PHASE_COSTS remains conditional on its sharper physical-source,
finite-source, passive-decoder, and external evaluation interfaces. The
assembly preserves its original \(Z\), width gate and scientific error
target. It makes no new table claim for the \(p\)-refined partition or
for the optional small-label partition. It also retains the current
decoder's uncontrolled asymptotic error absorption as an open step.

The declared omissions concerning finite insertion, cavity transfer,
training-conditioned decoding, and population-to-dense comparison are
appropriately presented as missing proofs rather than impossible neural
behaviors. This report does not independently validate those route
analyses. The assembly's opening and closing statements correctly reject
a full polynomial-width theorem; the confidence qualification above
is needed to keep the stronger target equally precise.

## Closure on the corrected assembly

2026-10-07. I reread the complete corrected assembly, SHA-256
`97ab1c8ac799c4dc007da53c7e3390c3197fff140e2dc1e145c77fc7c3a6f421`.
The new paragraph after (4) explicitly distinguishes the algebraic
\(\delta^{-1}\) and \(\delta^{-2}\) factors from the unresolved
polynomial-in-\(\log(1/\delta)\) target. The following heading now
identifies two *scientific* gaps, and the inline mathematical delimiters
have been restored. Displayed formulas (1)–(4) are unchanged.

Both requested corrections are closed. **Final bounded assembly verdict:
PASS at this corrected hash**, with the scientific and external-interface
limitations stated above. This closes the assembly wording check only;
it does not upgrade the full polynomial-width compression claim.
