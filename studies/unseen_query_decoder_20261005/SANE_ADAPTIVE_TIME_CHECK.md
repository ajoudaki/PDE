# Independent bounded reconstruction of the residual-cap source solver

2026-10-06. Fresh isolated reconstruction of the frozen candidate
`SANE_ADAPTIVE_TIME.md`. This is an internal mathematical check, not a
promotion review or a new source-event theorem. No experiments were run.

**Bounded verdict: PASS, conditional on the supplied fitting, complex-time,
and physical matrix-perturbation interfaces.** The candidate's patchwise
residual caps preserve the exact real trajectory. Its physical and normalized
Lipschitz bounds, accumulated stability exponent, full causal collocation
convergence, matrix-call count, and physical matrix-noise precision follow
from those interfaces. There is no missing derivative of the cap and no
omitted nondecaying residual-map stiffness. No correction to the frozen
candidate is required for this bounded conclusion.

The conclusion does not establish a compact autonomous decoder, its uniform
unseen-query law, a complete scalar precision or memory bound, a larger
complex-time source domain, or an effective stochastic success width.

## Frozen inputs and scope

The complete candidate and these complete permitted dependencies were read:

| File | SHA-256 |
| --- | --- |
| `SANE_ADAPTIVE_TIME.md` | `adb3aca056819e7276e82e6c18b969fd0f67cbe1fdb56c290c929a9a8b4f2d9f` |
| `SANE_INTEGRATED_COLLOCATION.md` | `8e92214a0ab090b2d32636d4fdf7e31f3b479092fac29e71c62d0b2c9bd8c60e` |
| `PHYSICAL_PARAMETER_ACCOUNTING.md` | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| `SHORT_CAUSAL_TRAINING_PROGRAM.md` | `0fbffab2a0782cb34987f49c944491fb50f920c4c4acbd888548947131be35a5` |
| `../integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md` | `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d` |

The last dependency was used for the exact gradient formulas and the
forward/backward coefficient definitions underlying the accounting interface.
Links to further research inputs were not followed. Study history, README,
other route notes, and prior reviews were not read. The isolated assignment
replaces ordinary author startup reading.

The rigorous-math and conjecture skills and the latter's research-contract
and adversarial-audit references were read. The canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` returned
OS permission denied; no copy was found in the accessible skill directories.
The assignment-authorized fallback was the explicit repository notation
instructions. This report reuses the candidate's notation and defines the
few additional comparison quantities locally.

## 1. Exact real path and the capped field

Use the candidate's physical displacement norm, normalized clock
\(\tau=\lambda t\), normalized displacement
\(\bar u(\tau)=u(\tau/\lambda)/Y\), and parameters
\[
\lambda=\gamma/m,\quad r=\lambda^{-1},\quad
Y=\|y\|_2/\sqrt m>0,\quad S=16Yr\le1,\quad
\ell=\log(en),\quad B=\beta^{100L},
\]
\[
Z=(a_0+1)\ell+\log(e+B(1+r)),\qquad a_0\ge1.
\]
The supplied real residual bound is
\(\|r(\tau/\lambda)\|_2/\sqrt m\le Ye^{-\tau/4}\).
Here \(r_a\) denotes a sample residual, while the unindexed \(r\) is the
inverse normalized covariance gap.

On a patch beginning at \(\tau_j\), put
\(q_j=2^{-\lfloor\tau_j/4\rfloor}\), \(R_j=Yq_j\), and project the
residual vector onto its Euclidean ball of radius \(\sqrt m R_j\).
For every time in that patch,
\[
e^{-\tau/4}\le e^{-\tau_j/4}
\le 2^{-\lfloor\tau_j/4\rfloor}=q_j.
\]
The second inequality uses
\(\lfloor\tau_j/4\rfloor\log2\le\tau_j/4\). Thus the residual
projection is the identity on the exact path, including at patch boundaries.
The inherited parameter projections and protected carrier clips also fix
that path. Consequently each normalized patch field \(F_j\) satisfies
\(F_j(\bar u(\tau))=\bar u'(\tau)\) throughout its own real patch.

Each cap is selected from the known patch time and input label scale,
before the stage calculations. It contains no future residual measurement.
Within a patch its radius is constant. Differentiating the projection
with respect to time or radius is unnecessary: the proof uses a difference
bound for a fixed-radius nonexpansive map. The change of field at a boundary
requires no error charge because both comparisons use the same exact
trajectory and the next patch starts from the committed endpoint.

## 2. Reconstructing the dependence on the residual radius

Let \(F_R\) be the field in physical state and physical time, with fixed
residual RMS cap \(R\le Y\). Compare two physical states a distance \(D\)
apart in the displacement sum norm. Their projected states are no farther
apart. Use the source coefficients \(H_j,P_j,f_j,k_j,\tau_j\) defined in
the permitted source equations (5)--(6), and its activation bounds \(s,t\).
The accounting proof supplies, uniformly over real unit inputs,
\[
\|h^{(j)}\|_{2,n}\le H_j,\quad
\|\widehat\delta^{(j)}\|_{2,n}\le S\tau_j,\quad
\|\Delta h^{(j)}\|_{2,n}\le f_jD,
\]
and output difference at most
\((H_L+SH_Lf_L)D\). The residual projection is nonexpansive, so its
RMS difference obeys this same output bound, independently of \(R\).

Write \(M_c=2K_{\rm src}S\sqrt\ell\) for the carrier clipping level
to distinguish it from the candidate's field bound \(M\). Clipping before
the activation derivative gives the backward difference coefficients
\[
C_L=s+tM_cP_L,\qquad
C_j=s(10C_{j+1}+S\tau_{j+1})+tM_cP_j.
\]
These recurrences are sums of a propagated response difference, a changed
matrix multiplying a bounded response, and a changed gate multiplying a
clipped carrier. In particular they have the form
\(C_j\le\beta^{50L}(1+S\sqrt\ell)\) with ample slack in the
accounting power ledger. There is one carrier-maximum factor, not one per
layer.

For a hidden gradient, subtract the three factors as
\[
\rho_a\widehat\delta_a h_a^\top
-\rho'_a\widehat\delta'_a h_a'^\top
=(\rho_a-\rho'_a)\widehat\delta_a h_a^\top
 +\rho'_a(\widehat\delta_a-\widehat\delta'_a)h_a^\top
 +\rho'_a\widehat\delta'_a(h_a-h'_a)^\top,
\]
where \(\rho,\rho'\) are the projected residual vectors, not their
scalar RMS norms. Divide rank-one norms by \(n\) as in the gradient
formula and average over samples. Cauchy--Schwarz bounds the first term
using the residual difference, and the other two using
\(\|\rho'\|_2/\sqrt m\le R\). The first-weight block has the same
calculation with fixed unit input vectors; the readout block has only the
residual and feature factors. Summing the blocks yields
\[
\operatorname{Lip}(F_R)
\le\beta^{70L}(1+R+RS\sqrt\ell).
\]
The first term is essential: making residual values small does not make
the derivative of the residual map small. It is retained in the candidate.
Bounded gradient factors also give
\(\|F_R\|\le R\beta^{12L}\le Y\beta^{12L}\).

The normalized field is \((r/Y)F_R(Y\bar u)\). Its Lipschitz bound
is multiplied by \(r\), since the state argument contributes the
cancelling factor \(Y\). Hence
\[
\operatorname{Lip}(F_j)
\le\beta^{70L}
 [r+Yr q_j+16(Yr)^2q_j\sqrt\ell]
\le\Lambda_j:=B(1+r)(1+q_j\sqrt\ell).
\]
The magnitude and true complex derivative are bounded by
\(M=B(1+r)\). The normalized prediction sensitivity is at most \(B\),
since dividing output and displacement by the same \(Y\) cancels again.
There is no inverse-label loss in these steps.

## 3. Accumulated stability and complete collocation error

With the inherited true-trajectory radius \(r_\tau\), take
\[
h=\min\{1/8,r_\tau/4,[16B(1+r)\sqrt\ell]^{-1}\}.
\]
Let \(h_j\le h\) be the actual patch lengths, shortening only the last.
Since \(q_j\le1\) and \(\ell\ge1\),
\(h_j\Lambda_j\le1/8\). Since
\(r_\tau^{-1}\le B\sqrt\ell\), the number of patches is
\(H\le1+16TB(1+r)\sqrt\ell\).

The decreasing right-continuous function
\(q(\tau)=2^{-\lfloor\tau/4\rfloor}\) has integral
\(4\sum_{k\ge0}2^{-k}=8\). On each patch its left-rule excess is
at most \(h[q(\tau_j)-q(\tau_{j+1})]\). Summing telescopes, including
the shortened last patch, and proves
\[
\sum_jh_jq_j\le8+h\le9,\qquad
\sum_jh_j\Lambda_j\le E:=B(1+r)(T+9\sqrt\ell).
\]
For the candidate's \(T=2[a_0\log n+\log(1+66Br)]\), one has
\(T\le CZ\), \(E\le CB(1+r)Z\), and
\(H\le CB(1+r)Z\sqrt\ell\).

The degree-independent integrated interpolation inequality is valid in
the displacement sum norm. For scalar interpolant \(p\), the Chebyshev
root rule integrates \(|p|^2\) exactly against
\(w(s)=[\pi\sqrt{s(1-s)}]^{-1}\). Cauchy--Schwarz therefore bounds
the indefinite integral by
\(\pi/(2\sqrt2)\) times the largest nodal magnitude. Applying norm-one
dual functionals proves the same bound for vector data. Thus the node
Picard map has contraction at most \(2h_j\Lambda_j\le1/4\).

Only the true derivative is continued to complex time. A disk of radius
\(2h_j\) about a patch midpoint lies inside its inherited analytic disk.
Taylor approximation and the integrated operator bound give true integrated
defect at most \(6Mh_j2^{-K}\). Neither the clipped field nor its
projection is asserted to be holomorphic. This remains valid when the
true real residual touches the cap.

Let \(e_j\) be the starting error and \(V\) the exact node array.
The node fixed point obeys
\(\|U^*-V\|_{\max}\le2(e_j+6Mh_j2^{-K})\).
Starting from the constant array and performing \(J=K\) iterations gives
\(\|U^{(K)}-U^*\|_{\max}\le2h_jM4^{-K}\).
The positive endpoint weights sum to one, giving
\[
e_{j+1}\le(1+2h_j\Lambda_j)e_j+8Mh_j2^{-K}.
\]
Indeed the defect contribution is at most
\(6Mh_j2^{-K}(1+2h_j\Lambda_j)\), and the iteration contribution
is at most \(2h_j^2\Lambda_jM4^{-K}\); their sum is below the
displayed forcing bound. Starting from the exact initial state and using
\(\prod_j(1+2h_j\Lambda_j)\le e^{2E}\) proves endpoint error
at most \(8MT e^{2E}2^{-K}\).

For an interior time, the integrated operator norm gives error at most
\[
(1+4h_j\Lambda_j)e_j
 +(1+4h_j\Lambda_j)6Mh_j2^{-K}
 +4h_j^2\Lambda_jM4^{-K}.
\]
Consequently the candidate's complete path bound
\(32M(T+1)e^{2E}2^{-K}\) holds, with slack.
Its power-of-two choice (16) makes the prediction error less than
\(n^{-a_0}/8\) and satisfies \(K=J\le CB(1+r)Z\).
The supplied fitting tail then gives all-time, whole-sphere normalized
prediction error less than \(3n^{-a_0}/8\), including the fitted endpoint,
when the numerical endpoint is frozen after \(T\).

## 4. Calls, perturbations, and scaling

Every patch uses exactly \(K(J+1)\) field evaluations in the stated
schedule: \(J\) Picard updates and the final evaluation defining the
patch polynomial and endpoint. Each evaluation uses \(O(mL)\)
initialized matrix or transpose actions. The residual cap adds no such
action; it uses the already computed residual coordinates. The existing
rank-one displacement representation is preserved by projection, summation,
and these field evaluations. Including the first-layer roots gives
\[
R_{\rm calls}\le C\{d+mLHK(J+1)\}
\le C\left[d+mL\beta^{300L}(1+r)^3Z^3\sqrt\ell\right]
\le C\left[d+mL\beta^{300L}(1+r)^3Z^{7/2}\right].
\]
At fixed admissible problem parameters this is a sufficient logarithmic
power seven-halves, and therefore also a sufficient integer power four.
The bound still counts operations on width-\(n\) vectors. Dense work and
live stage storage retain the candidate's stated width dependence.

For additive field errors of normalized-state norm at most \(\delta\),
one noisy Picard update adds at most \(2h_j\delta\). Geometric summation
under contraction \(1/4\) gives at most \((8/3)h_j\delta\) in the final
node array. The noisy final evaluation and positive endpoint weights add
\[
h_j\delta+h_j\Lambda_j(8/3)h_j\delta
\le(4/3)h_j\delta.
\]
The same stability product and the interior integrated bound then give
additional prediction error at most \(CB(1+T)e^{2E}\delta\).

The supplied matrix-perturbation interface gives
\(\delta\le CB r(1+r)\sqrt\ell\,\sigma\). Its uniformity under
the smaller residual caps is justified: each fixed-radius residual
projection remains nonexpansive and its output RMS is no larger than
before. In particular no inverse cap radius enters the perturbation bound.
Forward answer error is \(O(B\sigma)\); its output error is multiplied
by the readout bound proportional to \(S\), so dividing output by \(Y\)
uses \(S/Y=16r\). In the gradient, terms other than residual error carry
a residual at most \(Y\), cancelling the state normalization. Time
normalization contributes \(r\). These are the sources of the displayed
\(r(1+r)\) factor, with no \(1/Y\) factor.

Combining this interface with the propagation bound requires only a
universal multiple of
\[
1+E+(a_0+4)\ell+
\log\{1+B^2(1+r)^2(1+T)\}
\]
bits in the exponent of \(\sigma=2^{-b_\sigma}\). The inequality
\(r(1+r)\le(1+r)^2\) and the extra \(\ell\) terms absorb the
remaining polynomial factors. Since \(E\le CB(1+r)Z\), the least
sufficient integer obeys
\(b_\sigma\le C\beta^{100L}(1+r)Z\). The supplied Gaussian RMS
union bound becomes \(R_{\rm calls}e^{-cn}\) with the revised chronology.
This is a conditional application of that interface, not a fresh proof of
its Gaussian construction or of every scalar arithmetic error model.

The cap schedule uses exact dyadic factors, but its label scale and stage
arithmetic need their own finite-precision treatment. The candidate
expressly retains that qualification. In particular the matrix-noise
calculation does not establish the scalar-history sensitivity requirement,
the costs of activation evaluation, or the full decoder's precision.

## 5. Scope and surviving obligations

The main possible structural objections are resolved at the claimed level:
the cap uses no future information; the fixed-radius projection has no
missing time derivative; residual-map stiffness remains; real clipping is
not analytically continued; shortened patches obey the same bounds; and
the final field evaluations and conditioning exponent are charged.

The candidate also correctly distinguishes a larger complex-time domain
from its proved improvement. A scalar stationary solution of
\(\theta'=-2\theta\) has variational multiplier \(e^{-2z}\), so small
residual alone cannot imply a uniform factor-two backward propagator.
Complex symmetry is not Hermitian symmetry. The auxiliary ball-continuation
inequality follows by integrating
\(\rho(t)e^{2K|z-t|}\) against the velocity bound
\(2\sqrt K\rho\); it is conditional on the stated ball bounds and
does not establish the missing larger tube. The exact late-time ball size
is an inherited interface, not independently rederived in this check.

The accepted statement is a finite causal approximation of the same dense
nonlinear flow at the same physical times, with the full inherited label
allowance and whole-sphere observable. It is not an autonomous compact
substitute for that flow. The original source-event success conditions and
unquantified stochastic width qualification remain in force. Compiling the
chronology into a compact unseen-query law and counting all memory, work,
and scalar precision remain separate obligations; simply squaring the call
count already produces a sufficient logarithmic power seven. The present
PASS cannot be used as a promotion certificate or as a resolution of those
obligations.
