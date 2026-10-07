# Exponent and runtime accounting for the current decoder

2026-10-06. Scoped author accounting, not an independent review or a
promotion. The eight scientific inputs listed below were read completely.
No review, prior verdict, other study, experiment, or external source was
used. The required custom notation skill could not be read because of
filesystem permissions; the supervisor authorized the explicit repository
notation requirements as the fallback. The rigorous-math and research-audit
skills were read and applied.

The current sources prove an **unspecified absolute** polylogarithmic
space exponent. They do not currently supply an audited numerical value
for it. In particular, the packet-count exponent 16 and raw-entry exponent
24 are not the exponent of the complete decoder. Nor is that exponent a
tunable particle count: reducing the retained packet count below the
proved acquisition bound would require another approximation argument.

This note derives explicit downstream accounting in terms of the missing
compiler bounds. It does not assign numerical degrees to an unspecified
polynomial.

## 1. Counts already explicit

Put \(\ell=\log(en)\). All constants below may depend on the fixed
admissible problem and fixed confidence. Let \(R\) be the number of named
training fields/noisy matrix calls, \(P\) the number of scalar training
summaries, \(D\) the Gaussian packet dimension, and \(q\) the number of
selected packets. The current proof supplies

\[
 R=O(\ell^8),\qquad P=O(R^2)=O(\ell^{16}),\qquad
 D=O(R)=O(\ell^8),\qquad q\le P+1.
 \tag{1}
\]

Consequently the raw selected-packet/history storage is
\(O(PD+P)=O(\ell^{24})\). The largest matrix dimension is at most
\(R^2=O(\ell^{16})\), so the dense representation of one such matrix is
bounded by \(O(R^4)=O(\ell^{32})\) scalar entries. This is an upper
bound for this implementation, not a lower bound on every decoder.

A passive forward query adds a fixed number of named fields and their
pair moments with the existing fields. The bound \(S=O(R^2)\) therefore
suffices for its additional summary count \(S\), even though a tighter
bound may be available. This is the same all-pairs bound used in the
physical bridge, not a new increasing-depth assumption.

The physical matrix noise is explicitly
\(\sigma=\exp(-\ell^2)\). Its reciprocal may be huge, but
\(\log(\sigma^{-1})=\ell^2\), which is the quantity entering precision
and space estimates.

## 2. A single counted parameter for the missing compiler bounds

Use a finite row/coefficient graph in which a gapped inverse, square root,
PSD projection or Sylvester solve is one specified matrix subroutine.
Its implementation is counted below. Let \(N\) bound its graph size,
including both the training-prefix row functions and passive-query row
functions, and let \(I\) bound the retained instruction descriptions and
numerical certificates. Instruction addressing bits are included in
\(I\).

Let \(B\ge1\) bound the training and query row functions, let
\(\Lambda\ge1\) bound their joint Lipschitz constants, and let \(U\ge1\)
bound the exact scalar and small-matrix intermediate magnitudes and
clipped packet arguments. Let \(0<\alpha\le1\) be a common positive gap
for the exact gapped matrix operations and any scalar divisors. An
ungapped PSD projection uses its separate numerical construction; its
internal tolerance-dependent gap is counted in Section 4. Include the
fixed primitive sensitivity bounds in \(U\) by enlarging that bound if
necessary.

Define the nonnegative accounting parameter

\[
 \mathcal A=2+N+I+P+S+D+R^2+\ell+\log(1/\delta)
       +\log(2+B+\Lambda+U+\alpha^{-1}).
 \tag{2}
\]

Every quantity in (2) is a counted instruction parameter or a proved
range/sensitivity certificate. The current sources assert that
\(\mathcal A=O(\ell^a)\) for some absolute exponent \(a\), but do not
give a numerical value of \(a\). Defining \(\mathcal A\) does not repair
that missing numerical bookkeeping.

## 3. Scalar noise, density and retained precision

On the event that all scalar noise marks have magnitude at most \(n\),
the acquisition recurrence gives prefix error at most

\[
 \eta nP(1+\Lambda)^P.
 \tag{3}
\]

The appended query satisfies the same recurrence with at most \(S\)
additional summaries. For a target physical error \(n^{-c}\), with
fixed \(c>0\), one may therefore choose positive dyadic scalar noise
scales with

\[
 \log(\eta_{\rm tr}^{-1})+
 \log(\eta_{\rm q}^{-1})=O(\mathcal A^2).
 \tag{4}
\]

Indeed, the logarithm of the amplification is bounded by a fixed multiple
of \((P+S)\log(1+\Lambda)+\ell+\log(P+S+2)\). Smoothed CDF tests have
absolute bound one and Lipschitz constant \(K=O(n)\), so their extra
\(\log K=O(\ell)\) cost is included. A separate smaller query scale, if
used by the Fourier approximation, has the same bound (4).

For a prefix of length \(j\le P\), the all-prefix density threshold is

\[
 d_j=\frac{\rho}{P(2B+2)^j},\qquad \rho=\delta/4.
\]

Thus \(\log(d_j^{-1})=O(\mathcal A^2)\), uniformly in the prefix.
The conditional Fourier proof uses
\(P_{\max}=(\sqrt{2\pi}\eta_{\rm tr})^{-j}\). Its logarithm is at
most \(O(P\log\eta_{\rm tr}^{-1})=O(\mathcal A^3)\).
Equations (39)--(41) of that proof then give a sufficient history
accuracy \(\varepsilon_{\rm hist}\) with

\[
 \log(\varepsilon_{\rm hist}^{-1})=O(\mathcal A^3).
 \tag{5}
\]

For clarity, the denominator Lipschitz bound contributes
\(\log P_{\max}+\log\eta_{\rm tr}^{-1}+\log(1+\Lambda)+\log P\).
The query-test Lipschitz bound contributes at most
\(\log K+\log S+(S+1)\log(1+\Lambda)\). Their sums, and
\(\log(d_j^{-1})\), have the claimed order. No inverse density is
counted as a free constant.

The acquisition rounding recurrence adds
\(P\log(1+\Lambda)+\log(B+\Lambda+2)\) bits beyond (5). Hence
\(O(\mathcal A^3)\) bits per selected packet, noise, weight or history
entry suffice. Use the common nonnegative weight grid from the acquisition
proof, after the finite rational source selection. This avoids retaining
the larger exact rational weights. The \(O(PD+P)\) retained numerical
entries therefore use at most \(O(\mathcal A^5)\) bits. This is a
conservative bound, and still excludes the separately counted evaluator.

## 4. Fourier and small-matrix workspace

Denote the Fourier theorem's complexity parameter by \(\Pi\), to avoid
confusing it with the training summary count \(P\). Include the fixed
training noise, passive-query instructions and logarithmic density
threshold in that parameter. Equations (2)--(4) permit

\[
 \Pi=O(\mathcal A^2).
 \tag{6}
\]

The Fourier theorem gives \(O(\Pi^8)\) overhead bits and requests its
row evaluator at precision \(b=O(\Pi^4)\). Hence its explicit overhead
and requested precision satisfy

\[
 \text{Fourier overhead}=O(\mathcal A^{16}),\qquad
 b=O(\mathcal A^8).
 \tag{7}
\]

The row evaluator is not free. For a macro graph of size \(N\), the
small-matrix proof's common-grid estimate (25) adds precision at most

\[
 C N[\log(r+1)+\log(U+1)+\log(1/\alpha)],
\]

where \(r\le R^2\) is the largest actual matrix dimension. This is
\(O(\mathcal A^2)\), dominated by \(b\). Thus a common word length
\(w=O(\mathcal A^8)\) suffices. Storing all \(N\) intermediate small
matrices if desired, and using one matrix-subroutine scratch area at a
time, costs at most

\[
 O(Nr^2w+w^2)=O(\mathcal A^{16}).
 \tag{8}
\]

This includes the full Kronecker arrays. The PSD projection's internally
introduced gap has logarithmic reciprocal
\(O(\log r+\log\varepsilon^{-1})=O(\mathcal A^8)\), already covered
by the word length. The fixed common grid prevents repeated precision
doubling between macros.

Consequently, excluding the original activation/data precision
interfaces, the actual displayed algorithms have total bit overhead
\(O(\mathcal A^{16})\). With exact original activation primitives this
is also a conservative upper bound on their scalar-register/counter
storage. If the supplied fixed interfaces use at most \(O(b^e)\) space
on these bounded inputs, their additional contribution is
\(O(\mathcal A^{8e})\). The exponent \(e\) is a separate hypothesis;
bare strip analyticity supplies no such interface.

Thus, **conditional on a proved numerical bound**
\(\mathcal A=O(\ell^a)\), the construction permits

\[
 k=16a
 \quad\text{for the primitive model},\qquad
 k=\max\{16a,8ae\}
 \quad\text{for the stated finite-bit interface}.
 \tag{9}
\]

These are downstream formulas, not numerical values of \(k\).

## 5. Runtime, with the interface qualification kept explicit

The Fourier tensor grids have total logarithmic point count
\(O(\Pi^4)=O(\mathcal A^8)\). At each grid point a row graph is
evaluated. For a matrix subroutine, the series truncation degree in the
small-matrix proof obeys \(\log D_{\rm series}=O(w)\); its runtime
\(O(D_{\rm series}r^3\operatorname{poly}(w))\) is therefore at most
\(\exp(O(\mathcal A^8))\). Elementary scalar arithmetic and the
specified convergent-series routines fit the same bound. Multiplying
these costs, and the \(O(\log(nU+2))\) median-bisection iterations,
preserves the bound

\[
 T_{\rm query}\le\exp(O(\mathcal A^8))
               =\exp(O(\ell^{8a})).
 \tag{10}
\]

Equation (10) is an operation bound **with unit-cost evaluations of the
original activation primitives and their original derivatives**. It
does not follow as a bit-time bound merely from polynomial-space
activation interfaces. If \(T_{\rm interface}(b)\) bounds their actual
runtime at the requested precision and input magnitude, the explicit
finite-bit bound is instead

\[
 \exp(O(\mathcal A^8))
       [1+T_{\rm interface}(C\mathcal A^8)].
 \tag{11}
\]

No numerical exponent is asserted for this interface runtime. No
preprocessing runtime or workspace improvement follows from (10).
Even with numerical \(a\), the bound is generally much larger than a
polynomial in \(n\); it is not a practical inference guarantee.

## 6. Exact unresolved bookkeeping

The first missing numerical degree is in
`SHORT_CAUSAL_TRAINING_PROGRAM.md`, Section 5: after the explicit Gaussian
call count, the scalar combinations in (13) are said to add a fixed
polynomial number of instructions. The physical bridge's Section 2
likewise states a polynomial bounded-arity expansion without giving its
degree. Its Sections 4--5 leave the logarithmic intermediate-cap and
global-sensitivity polynomials unspecified. These are needed to turn
\(N,I,B,\Lambda,U\) in (2) into a numerical power of \(\ell\).

The acquisition note gives useful partial constants: one-call coefficient
degree \(C_0=100\), and \(c_0=2\) for its stated binary-operation/macro
graph with coefficient-cap logarithms growing at most linearly in the
instruction count. These do not supply the physical compiler's graph
size or certify that particular cap-growth bound for the compiled
physical program.

For a sharper substitution, suppose those missing checks supply
\(N=O(\ell^s)\), \(I=O(\ell^i)\), logarithmic operand/primitive
bounds \(O(\ell^v)\) with \(v\ge2\), and the acquisition estimate
with \(c_0=2\). Then
\(\beta=2s+v\) bounds \(\log(B+\Lambda+2)\),
\(\log\eta^{-1}=O(\ell^{\beta+16})\), and retained-history precision
is \(O(\ell^{\beta+32})\). With
\(u=\max\{i,\beta+16\}\), the same explicit calculation gives space
\(O(\ell^{8u})\) and primitive-operation time
\(\exp(O(\ell^{4u}))\). This also remains conditional until numerical
\(s,i,v\) and the specified cap convention are proved.

The next accounting step is therefore to specify and count one complete
physical scalar/macro compiler and its intermediate caps. Assigning a
large integer to the existing word “polynomial” would not perform that
step. This audit leaves the existence-of-an-absolute-exponent claim
unchanged while declining to invent its numerical value.

## Scientific input versions and check scope

All eight files below were read in full. The check was symbolic
substitution into their displayed counts, error recurrences, quadrature
and matrix routines; no runtime experiment was performed. No source was
edited. This accounting has not received an independent reconstruction.

| File | SHA-256 |
|---|---|
| `CURRENT_STATE_DECODER_CANDIDATE.md` | `9b1e87e3c2e2e74efdf56a40c130c8ff91d74484ab215d6afe03c8ae2c808411` |
| `SHORT_CAUSAL_TRAINING_PROGRAM.md` | `0fbffab2a0782cb34987f49c944491fb50f920c4c4acbd888548947131be35a5` |
| `PHYSICAL_NOISY_PROGRAM_BRIDGE.md` | `b20650d28fe3a4c8ebc76105bd5f4347503bd0485bcced588dd1680bc65cadc6` |
| `NOISY_TWO_ORIENTATION_TRANSCRIPT.md` | `0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac` |
| `NOISY_SCALAR_HISTORY_ACQUISITION.md` | `b301507a73de79310634ca67da75a9f5817a139edc498ad145aaeb857cae6fab` |
| `FOURIER_ROW_PROGRAM_EVALUATION.md` | `55dd1adb0234448ac2ec022446fd1c3a4ad7245e26f10deabac614f2ac17b1d1` |
| `SMALL_MATRIX_FUNCTION_EVALUATION.md` | `466316e156faaef58f8574876466ef513c34c45258370b046d35383eb8b28b33` |
| `FINITE_PRECISION_SOURCE_SELECTION.md` | `bef48fe4f546792326cedeb438a09fda0d6b3f616f60e2d907bf20b8888ced90` |
