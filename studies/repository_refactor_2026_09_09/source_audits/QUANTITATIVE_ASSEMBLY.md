# Quantitative discretization incorporation report

## Deliverable and status

The appendable mathematical draft is:

`/tmp/pde-quantitative-discretization.CTuyBG6U/ADDITION.md`

This report is:

`/tmp/pde-quantitative-discretization.CTuyBG6U/REPORT.md`

The draft supplies the requested fixed-finite-(L,N) exact-compiler
step-doubling statement, including the explicit fifth-order remainder,
using the existing internal fixed-program width theorem at its exact
scope. I found no remaining mathematical dependency gap in this target
after the detailed checks below. This is an incorporation draft for the
main task's fresh, independent audit of the actual combined chapter;
this report does not represent such an independent audit.

The section number is **8, provisional**, as requested. The source
snapshot has top-level Sections 1--6. Section 7 has been left available
for the main task; no allocation beyond provisional Section 8 has been
assumed. All new equation identifiers start with `8.`. Integration should
recheck the then-current chapter for concurrently assigned identifiers.

At completion the addition has 863 lines and SHA-256:

`bc41e23b07917257ce5810018d3d6ab2937551ce079a44d6e936965061f0d46d`

The private directory was created with `mktemp -d`; its verified mode is
`0700`. Only the two requested Markdown drafts were authored, using
`apply_patch`. No existing repository document was edited.

## Full source-read and hash ledger

All paths in the following table are relative to `/home/amir/Codes/PDE`.
Each listed file was read to EOF, without omitted or truncated portions.
The required two library documents were read completely before reading
the two required study documents.

| Source | Lines read | Read coverage | SHA-256 |
| --- | ---: | --- | --- |
| `docs/NOTATION.md` | 98 | 1--98, full | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/gaussian_calculus.md` | 1812 | 1--260, 261--620, 621--990, 991--1370, 1371--1812; full | `cda68e7decce4d35ddadb74ae0dffc4a78f5558f369eb21c7b312f516165a25e` |
| `studies/mfp_depth_time_doubling/COMPILER_DEPTH_TIME.md` | 862 | 1--310, 311--610, 611--862; full | `a7fde275877801a4185fdfe048c94a2a1baee81b45b5b5c75b7a0f88851d663f` |
| `studies/mfp_depth_time_doubling/AUDIT_UNCONDITIONAL.md` | 259 | 1--259, full | `205aa0e0cc20abaa05f1ec3d0db0afd33d58e329bc3d2e7312468e28b7492973` |
| `studies/mfp_depth_time_doubling/AUDIT_COMPILER.md` | 277 | 1--277, full | `00a51cd900090123551bc282a03ca2f068555335771216d911ab618cea57fa15` |

The first four files are the required donors. The fifth is the exact
additional audit dependency read to check the compiler's derivative,
syntax-size, call-count, and exponent obligations. Its PASS verdict was
not used as a mathematical premise; the draft gives the arguments.

The four required donor hashes were obtained before reading them and
rechecked after drafting. They matched. The compiler audit hash was
obtained with its full read and also matched on the later check.

The skill instruction read in full was
`/etc/codex/skills/solve-math-rigorously/SKILL.md`, SHA-256
`9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
Its rigorous-proof workflow guided the explicit hypothesis checks,
derivative accounting, and contained proofs of the facts previously
invoked by name. No separate research-program skill or broad research
workflow was used.

## Internal mathematical dependency boundary

The addition depends on the following parts of the existing chapter,
with no study-file link in its mathematical dependency chain:

| Internal location in the read snapshot | Exact use |
| --- | --- |
| Section 4, starting at line 193 | Finite positive-semidefinite Gaussian square-root representation; elementary Gaussian moment background. The additional radial-moment calculation is written out in Section 8.4. |
| Section 5.1, starting at line 260 | Fixed-program width theorem for each fixed finite depth, step count, and nonzero signed step; separate constant and L=1 branches. |
| Section 5.2, starting at line 351 | Stored-weight initialization and mobility convention, raw simultaneous feature-ascent updates, recomputation, and normalization. |
| Section 5.3, starting at line 460 | Exact `(2N+1)(L-1)` raw-action chronology, including the terminal forward sweep. |
| Section 5.5, starting at line 633 | Inverse-free population program, layer probability spaces, Gaussian blocks, source derivative convention, and terminal output. |
| Sections 5.4, 5.6--5.11 | Already-contained proof of the theorem being invoked: adaptive reused-matrix conditioning, response cancellation, strict rank including the affine branch, empirical ledger, coupling, moment tower, stopping removal, and terminal uniform integrability. Read in full; not reproduced. |
| Section 6, starting at line 1739 | Scope compatibility: no extension to a same-space algebra, infinite Taylor expansion, or depth/step-count-uniform conclusion. |

The stronger activation assumption in the addition implies the internal
theorem's condition with `M = 2 M_phi`: its linear-growth bound is then
satisfied, and the sum of the first two derivative suprema is at most
`2 M_phi`. The normalization is identical. The theorem is used twice,
at `(L,N,2h)` and `(L,2N,h)`, only when `h != 0` is fixed. The
finite-width zero-step expectation is computed separately from the
independent centered readout. No uniform nonzero-step conditioning gap
is borrowed or claimed.

`WIDTH_DEPTH_TIME.md` was deliberately not reread or imported: its
role has already been incorporated into the fully read internal Section
5. The required unconditional audit refers to it historically, but the
new section cites and uses the internal theorem instead. The long width
proof was not duplicated. `CUBIC_DEPTH_TIME.md`, its nine-moment recursion,
uniform-time studies, continuous-time bridges, generators, and experiment
scripts were neither needed nor used. A directory filename inventory
does not mean those files were read.

## Donor-to-addition map and canonical notation changes

| Donor component | Location in addition | Changes |
| --- | --- | --- |
| Compiler Sections 1--2 | 8.2 | Use the internal population definitions; retain all local call histories, dimensions, source dependence, and the exact terminal call count. |
| Compiler Section 3 | 8.3 | Expand the positive-definite density computation, integrations by parts, commuting square-root bound, uniform convergence, and integrated-derivative argument. |
| Compiler Section 4 | 8.4 | Preserve the exact envelope recursion and guard; distinguish ambient response differentiation from total step differentiation; give radial-moment derivation. |
| Compiler Section 5 | 8.5 | Preserve every numerical recurrence and the final exponent; expand the syntax, multiplicity, assembly, initialization, and one-call Gaussian-moment accounting. |
| Compiler Section 6 | 8.4 | Construct exact jets before their derivative interpretation; show reduction to finite activation integrals after ambient differentiation. |
| Compiler Section 7 | 8.6 | Preserve symmetry; replace the marked-time-slice sketch with an explicit response-derivative recurrence for the linear clock. |
| Compiler Sections 8--9 | 8.1, 8.7 | Preserve coefficient, fifth-order constant, broad `|h| <= 1/2` domain, optional shared-base radius, L=3 exponent, and constant branch. |
| Compiler Section 10 and unconditional audit | 8.7 | Close the actual width-first interpretation using internal Section 5; retain exact fixed-program scope. |

Specific alias translations:

| Study alias | Canonical form in addition |
| --- | --- |
| Discrete time `s` | Step index `k` |
| Doubling count `t` | Fixed integer `N`, with doubled count `2N`; `t` remains physical time |
| Comparison step `eta` | Scalar feature-ascent step `h`; `eta_n` remains loss-GD step |
| `Z_{ell,s}` | Population preactivation `Z^(ell)_k` |
| `X_{ell,s}` | Population feature `H^(ell)_k` |
| `D_{ell,s}` or study cotangent `C_ell^s` | Population cotangent `Delta^(ell)_k` |
| Study backsignal `H_{ell,s}` | Population incoming backsignal `q^(ell)_k` |
| `A_s` | Stored population readout `W^(L+1)_k`; `A` stays its initial standard Gaussian root |
| `Q^ell`, `K^ell` | Internal `Q_{ell,jk}`, `K_{ell,jk}` and their finite history matrices |
| `rho^ell`, `sigma^ell`, `R^ell`, `T^ell` | Typed deterministic history coefficients with internal layer/comparison indices |
| `d_phi` | `mu_{phi'}`, matching the existing chapter and avoiding the network input dimension `d` |
| `kappa^{cmp}_{phi,L,t}` | `mathcal C^{cmp}_{phi,L,N}`; `kappa_ell` remains the mobility multiplier |
| Generic Gaussian dimension `d` | Auxiliary dimension `b`; actual network input dimension stays `d=1` |
| Layer-unspecified contractions | `E_ell` or explicitly typed local Gaussian expectations |

Finite weights remain stored weights throughout the theorem. No update
using an unscaled middle matrix is silently transplanted. The readout
has order-one stored coordinates; it is never changed to the library's
different small-readout convention. Plain `Delta` is never used for
feature time or a step count.

## Detailed obligation checks

1. **Chronology and dimensions.** Interior forward, top, interior
   backward, and bottom calls number `(L-2)+1+(L-2)+1` per update.
   The terminal sweep has `L-1` calls. Dimensions are respectively
   `2k+1`, `k+2`, `2k+2`, `k+2`, then `2N+1`, `N+2`, all at most
   `D_N=2N+2`. L=2 has empty interior ranges; L=1 has exactly one
   scalar Gaussian call. New outputs of the same call never enter its
   own covariance or integrand.
2. **Singular Price formula.** The needed derivative is proved from
   the Gaussian density, including the ordered-pair factor `1/2`.
   Regularization adds `epsilon I` only inside the proof. The square
   root inequality is proved eigenvalue by eigenvalue because the two
   matrices commute. Derived integrands have uniform polynomial
   Gaussian domination. Uniform limits of all six expectations are
   passed through integrated derivative identities. This verifies
   regularity at zero step and any other covariance rank change.
3. **Derivative budget.** The guard is
   `r+j+ceil(q/2) <= 5`, with strict inequality before a recursion
   step. It implies `2r+j+q <= 10`. An undifferentiated atom has
   activation order at most one; the extra ambient response derivative
   raises that to two. Hence order twelve is sufficient. Scalar tokens
   and covariance entries require only five step derivatives. No sixth
   scalar token derivative or thirteenth activation derivative occurs.
4. **Envelope arithmetic.** Ordered spatial-list sums and covariance
   entrywise absolute sums dominate every contraction, including
   off-diagonal pairs. The `j Q_(j-1)` term from differentiating `hQ`
   is retained. The radial Gaussian moment factor is derived directly.
5. **Raw syntax count.** A sum of at most `2N+3` products, each of at
   most three previously built expressions of size at most R, has size
   at most `(2N+3)(3R+3)-1 <= 16(N+2)(R+1)`. The `8(N+1)` raw
   iterations cover every local history and the L=1 terminal feature.
6. **Derivative and multiplicity count.** All integer coefficients,
   binomial multiplicities, covariance pairs, and spatial lists are
   expanded for size accounting. A formal derivative has size at most
   `2(|e|+1)^2`. One Price level has at most `1+32D^2` expanded
   summands. The `64(D+1)^10(c+1)^2` map covers each operation;
   `10+1+1+5+2=19 < 24` levels cover differentiation, response,
   aggregation, Price, and assembly. The actual derivative guard still
   forbids an activation derivative above twelve.
7. **One-call exponent.** Syntax size, token count, and polynomial
   degree are bounded by `C_N`. The envelope coefficient is at most
   `(2B_phi)^C_N S^C_N`. The covariance's entrywise norm is at most
   `(D+1)^2 S`, and the Gaussian moment cost is at most
   `S^(C_N/2) nu_N`. Assembly of sums is performed under one common
   moment bound; it does not introduce a second `nu_N`. Therefore
   the output bound is exactly `B_phi^r_N S^p_N` with the donor's
   `p_N=2C_N` and `r_N=C_N+alpha_N`.
8. **Initialization and iteration.** Only truly constant initial
   scalar functions are seeded at `B_phi^(2L)`, with positive-order
   jets zero. The value of a dynamic Gram at `h=0` is not used to
   bound its derivatives. Every dynamic node is compiled. The affine
   exponent recurrence runs through `M_{L,N}` calls and solves to
   the donor's exact `E_{L,N}`. Its denominator is a finite geometric
   sum because `p_N>1`.
9. **Monotonicity.** Increasing N increases the raw recurrence, the
   syntax recurrence, the Gaussian dimension and moment exponent, the
   ceiling parameter, and (for L>=2) the call count. Coupling standard
   Gaussian vectors by initial coordinates proves the required moment
   monotonicity. Thus `E_{L,N} <= E_{L,2N}`.
10. **Exact coefficient.** Earlier scalar jets are available before
    each new call. Five finite Price iterations and zero-step Gaussian
    integration define the output jets before they are identified as
    derivatives. Ambient differentiation precedes coalescing repeated
    sources. The resulting terms are finite products of the stated
    one-dimensional activation integrals and ordinary Gaussian moments.
11. **Linear clock.** Symmetry makes every covariance first derivative
    zero. If `b_{ell,kj}=rho'_{ell,kj}(0)`, direct ambient
    differentiation gives `b_{2,kj}=mu_{phi'}` and
    `b_{ell+1,kj}=mu_{phi'}(1+b_{ell,kj})`. The terminal derivative
    is consequently `N sum_(a=0)^L mu_{phi'}^a`. This explicitly
    accounts for response contributions and avoids the donor's more
    compressed marked-slice argument.
12. **Taylor and branch checks.** Oddness removes constant, quadratic,
    and quartic terms. The linear terms cancel, the cubic factor is
    `(8 J_3(N)-J_3(2N))/6`, and the error factors are `32/120`
    and `1/120`. The common `2N` exponent and `33/120<1` give the
    claimed error. Negative steps use oriented integral remainders.
    Constant activations and zero step are separately justified. The
    internal theorem supplies the nonconstant affine and L=1 cases at
    their stated scope.

## External-result proof containment

The nontrivial analytic result needed beyond the internal fixed-program
theorem is finite-dimensional Price differentiation through singular
covariance. The donor contains a regularization proof, but abbreviates
its nonsingular density step and invokes a square-root estimate. The
addition supplies both calculations and the uniform-limit derivative
argument. It also supplies the radial Gaussian moment calculation,
the syntax induction, the exponent iteration, and the first-order
response calculation. No external paper, online theorem, unpublished
study proof, or audit verdict is needed to complete the new statement.

Ordinary finite-dimensional Gaussian square-root representation is
already explained in internal Section 4. The other elementary ingredients
used here are differentiation and integration of smooth densities,
chain and product rules, polynomial Gaussian integrability, and repeated
integration for Taylor's formula, with their uses made explicit. No
external-source search or new literature dependency was introduced.

## Verification and integration notes

Read-only static checks over the actual source chapter and the private
addition passed: all equation tags are unique across the two files;
parenthesized numerical references in the addition resolve to existing
or new equations/sections; and the addition's inline/display math
delimiters and LaTeX environments balance. This check read the combined
text in memory and did not write a combined chapter.

No numerical compiler execution, mathematical experiment, historical
generator, install, build, seal write, Git command, or subagent was used.
No external message was sent. All source access was read-only, and all
draft writes were confined to the new private directory.

The donor's exact exponent and compiler coefficient have been retained.
The substantive exposition changes are proof expansions and the explicit
first-order response recurrence, not changes to the target theorem.
The epsilon-dependent cubic corollary uses the already proved larger
domain `|h| <= 1/2` instead of unnecessarily imposing the optional
smaller shared-base radius. That optional radius is also recorded.

The draft deliberately does not assert the compact nine-moment identity,
a growing-N bound, a small-readout version, a physical-loss-GD statement,
an infinite Taylor series, or a continuous-time limit. It is not a
conditional substitute for the requested fixed-(L,N) statement: the
width identification is supplied by the internal theorem and its
hypotheses are checked explicitly. The main task can append the draft
after final identifier coordination and subject the resulting combined
document to the independently planned audits.
