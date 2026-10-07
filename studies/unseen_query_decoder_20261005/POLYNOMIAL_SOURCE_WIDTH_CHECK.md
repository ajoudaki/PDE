# Isolated check of the deterministic source-radius repair

2026-10-07. Independent isolated mathematical check of the frozen candidate
`POLYNOMIAL_SOURCE_WIDTH.md`, SHA-256
`352b98adf16e57f7844cb75d0ec4622e897b56ba9ac44527cc0141448443ad22`.

**Scoped verdict: PASS, conditional on the identified source and numerical
interfaces.** Sections 2–4 correctly remove the displayed short-contour
width gate while preserving the actual Taylor step and the original upper
label allowance. The optional numerical small-label refinement in Section 5
and the deterministic tail thresholds in Section 6 also check out. No
mathematical correction to those claims is required by this check.

This verdict does not validate the insertion theorem, an effective source
probability, the external scalar-forcing or finite-packet lemmas, or a complete
passive-query decoder. In particular it is not a polynomial stochastic
sufficient-width theorem. Those limitations are stated accurately in the
candidate.

## Input boundary

I read the entire frozen candidate and all eight scientific inputs listed in
its Section 8. Their hashes match the candidate's manifest:

| Input | SHA-256 |
|---|---|
| PHYSICAL_PARAMETER_ACCOUNTING.md | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| SANE_TAYLOR_SOURCE.md | `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af` |
| GAP_DEGREE_REFINEMENT.md | `78e209842b99ac054659bf32a2dd9e77ed9fef26af6047d209312152aa619875` |
| FAST_TAYLOR_NOISE.md | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| ../integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md | `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d` |
| ../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md | `f3e277e9591be6e48357a13217927c05bcc2c59843a26a3fa5423ae5afc4c7d8` |
| ../integrated_general_compression_20261004/GENERAL_EXPLICIT_FITTING.md | `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6` |
| ../integrated_general_compression_20261004/ANALYTIC_TAIL_EXTENSION.md | `70ec072f0e83c74364f068d61f04148bf110771fd06b4b2b874bb3c5d8dfc349` |

I followed no further scientific links and read no other study history or
review. I applied `solve-math-rigorously`, `explain-with-canonical-notation`,
and the latter's neural-network conventions. Only this report is written.

## 1. Coefficients, labels, and physical normalization

Retain the candidate's actual network, physical equations (3), and physical
sum norm. In the following calculations
\(\lambda=\gamma/m>0\), \(r=\lambda^{-1}\),
\(Y=\|y\|_2/\sqrt m>0\), \(S=16Yr\le S_*^{\rm src}\le1\),
\(\ell=\log(en)\ge1\), and \(B=\beta^{100L}\), with
\(\beta\ge10\), \(L\ge2\). The real fitting allowance remains
intersected with the source allowance. No calculation below assumes
\(\lambda\le1\) or the stronger lower-bridge cap
\(Y/\lambda\le\beta^{-30L}\).

The source forward/backward recurrences support (7)–(9). In particular the
full-label response bound \(U_{\rm fin}\le\beta^{72L}\) does not require
the optional stronger cap. As an independent loose check, the recurrences
in UNBOUNDED_COMPRESSOR_BRIDGE (7), (8), (22), and (24), using the
candidate's bounds on \(H_j,P_j,k_j,\tau_j\), give
\[
 A_*\le\beta^{11L},\quad H_*\le\beta^{13L},\quad
 D_0\le\beta^{29L},\quad K_{\rm src}\le\beta^{38L},\quad
 T_Q\le\beta^{25L}.
\]
For example, its mixed-response coefficients obey
\(g\le\beta^{10L}\), \(q_j\le\beta^{14L}\),
\(r_j\le\beta^{13L}\), and \(e_j\le\beta^{20L}\), by unrolling
the recurrence with multiplier \(10s\le\beta^2\). Substitution in
GENERAL_TRAJECTORY_LOWER_BRIDGE (9), with \(S\le1\), even gives
\(U_{\rm fin}\le\beta^{66L}\). Thus the candidate's exponent 72
has slack independently of its source's sharper intermediate ledger.

Each squared hidden-gradient term in \(\mathcal K\) is at most
\(\beta^{18L}\); there are at most \(L+1\le\beta^L\) terms,
including the readout. Hence \(\mathcal K\le\beta^{20L}\) and
\(D_W\le\beta^{9L}\) are valid. Also the population RMS recursion
is dominated by \(H_j\), so
\(\lambda\le\gamma\le Q^{(L)}_{aa}\le H_L^2\le\beta^{6L}\).
This is the needed bound on a possibly large normalized gap.

For the source coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\), direct
substitution in the physical equations gives
\[
 \dot\Theta=-\frac2m\sum_a r_a\nabla_\Theta(nf_a).
\]
Consequently the candidate's definition of \(R_a^{(j)}\) gives precisely
\(\dot z^{(j)}=-(2/m)\sum_a r_aR_a^{(j)}\), with neither an omitted
factor of \(n\) nor an extra residual. The proof normalization
\(\tau=\lambda t\), \(\bar u=u/Y\) preserves those physical dynamics.

## 2. Radius and short complex contours

The finite-query source explicitly permits any fixed
\(0<c\le a/(64YSU_{\rm fin})\). For
\(c_{\rm safe}=[B(1+\lambda)]^{-1}\), use
\(64YS=4\lambda S^2\), \(a^{-1}\le\beta/16\), and
\(U_{\rm fin}\le\beta^{72L}\). They give
\[
 \frac{c_{\rm safe}}{c_{\max}}
 \le \frac{\lambda}{1+\lambda}\frac{\beta^{73L}}B<1.
\]
The four right-hand products in the old gate are respectively bounded by
\[
 \frac8B,\qquad \frac1B,\qquad
 \frac{\beta^{21L}}B,\qquad \frac{\beta^{10L}}B.
\]
All are strictly below one, so \(\sqrt\ell\ge1\) suffices for every
integer width. The fourth product uses
\(32YS=2\lambda S^2\), which is essential when \(\lambda>1\).

The underlying contour calculation also works, rather than merely its
displayed gate. The normalized algebraic residual Gram and the parameter
negative-Gram generator, divided by its factor two, have operator norm
at most \(\mathcal K\), by absolute Cauchy–Schwarz on the gradient
blocks. On two short segments of total length at most \(2r_t\), where
\(r_t=c_{\rm safe}/\sqrt\ell\), this gives
\[
 \rho(z)\le\rho(t_*)e^{4\mathcal K r_t}\le2\rho(t_*),
 \qquad \rho=\|f-y\|_2/\sqrt m.
\]
The real negative-Gram contraction is used only on the real part of the
path. Complex time uses the displayed absolute norm bound; no Hermitian
positivity is needed or asserted.

The extra activity is bounded by
\(8Yr_t\le8Y/\lambda=S/2\). Each relevant hidden or normalized
first-weight increment is at most
\(8YSD_Wr_t\le1/4\). Finally the response bound and sample
Cauchy–Schwarz give
\(\|\dot z^{(j)}\|_\infty\le4YSU_{\rm fin}\sqrt\ell\), so
the preactivation increment over both segments is at most
\(8YSU_{\rm fin}c_{\rm safe}\le a/8\). These are the correct
factors for the physical clock and the finite collection of real training
queries. There is no additional complex query segment.

This is a valid deterministic rerun on the smaller stopped domain. It
does not assume the old larger domain is already available at a width
that fails its old gate. The insertion and stop-transfer estimates remain
conditional scientific inputs, exactly as the candidate states.

## 3. The actual Taylor partition remains available

The repaired normalized radius is exactly
\[
 r_{\tau,\rm safe}=\lambda r_t
       =[B(1+r)\sqrt\ell]^{-1}.
\]
The old radius lower bound \(r_\tau\ge[B\sqrt\ell]^{-1}\)
makes the third entry of the old patch minimum its smallest entry:
\[
 h_0=[64B(1+r)\sqrt\ell]^{-1}.
\]
After the repair, \(r_{\tau,\rm safe}/8=8h_0\), so the new
minimum is still exactly \(h_0\). The equal-patch certified-ceiling
convention of FAST_TAYLOR_NOISE is consequently unchanged. Moreover
\(4h_j\le4h_0=r_{\tau,\rm safe}/16\), leaving strict room for
the complex disks, their residual estimates, and their thin parameter tubes.
The source's centered-activation calculation uses \(h_j\le h_0\)
and remains unchanged.

The horizon gate gives
\(\log(1+66Br)\le2\ell\), hence
\(T\le(2a_0+4)\ell\le28\ell<32\ell\). It therefore needs no
later stochastic domain. Real parameter-to-output subtraction and the
inherited real fitting tail continue to control every real unit query
and every later physical time. This does not assert complex analyticity
for every query on the sphere.

Thus the substitution preserves the physical source count and precision
envelopes in (20), at their inherited claim level. In particular the
real one-sided stability argument of GAP_DEGREE_REFINEMENT is not being
applied on a complex disk.

## 4. Optional numerical small-label branch

The thin-tube and forcing formulas contain \(Y>0\) and
\(S/Y=16r\), but do not need \(Y\ge n^{-1}\) to hold as
inequalities. The latter lower bound was used to simplify logarithms and
coordinate-to-normalized-state precision conversions. With
\(Z_Y=Z+\log_+(Y^{-1})\),
\[
 \log_+(S^{-1})
 \le\log_+(Y^{-1})+6L\log\beta,
\]
which verifies the stated replacement in the tolerance estimates.

The degree/patch refinement is finite and its inequalities are valid. Since
\(H_1\ge H_0\ge1\),
\[
 \frac{1+16c_LH_1}{1+16c_LH_0}\le\frac{H_1}{H_0}\le4K_0.
\]
Only the logarithm of this ratio changes in \(\mathfrak k\). The
ceiling difference is at most its base-two logarithm plus one; the
candidate's extra two is safe. Therefore
\(K_1\le K_0+\log_2(4K_0)+2\le2K_0\). If no refinement occurs,
\(K_1=K_0\le H_1/4\); otherwise \(H_1=4K_0\), so again
\(K_1\le H_1\). No implicit fixed point has been assumed.

Every new patch has length at most \(h_0\). The left activity sum
remains at most nine and the same local real and complex estimates apply
at the new anchors. The bounds
\(H_1\le CB(1+r)Z_Y\sqrt\ell\), \(K_1\le CBZ_Y\)
give (24). Also \(Br\ge\beta^{94L}\) implies \(T>1\), so
\(h_j^{-1}=H_1/T\le H_1\). The added inverse-step cost is
logarithmic. A field count chosen to dominate \(mLH_1K_1\) also
dominates \(H_1\); thus the polynomial factors in \(R+K+1\)
in (25) can pay for this refined inverse-step conversion.

The extra degree lower bound pays for \(\log\delta_0^{-1}\) when
\(Y\) is small, and permits \(J=O(K_1)\) in the explicit activation
interpolation interface. For \(N=mLH_1\), \(K_1\le H_1\le N\)
indeed yields \(NK_1^3\le(NK_1)^2\), preserving the stated activation
arithmetic envelope. It still excludes the activation-value evaluator's
work, as declared.

The factor \(\min\{1,Y\}\) in (25) pays directly for the
physical-to-normalized error conversion that previously used
\(Y^{-1}\le n\). Its logarithmic price is
\(\log_+(Y^{-1})\); the remaining powers of \(n+1\) give slack.
The explicitly displayed root-coupling target already includes \(Y\).
The scalar-pair conclusion remains conditional on the external interface
described in GAP_DEGREE_REFINEMENT: its stated polynomial dependence on
\(Y^{-1}\) costs logarithmic precision, but that interface's proof is
not in the allowed packet and is not certified here.

The proposed source tolerance
\(\epsilon_{\rm src}=\frac14\min\{n^{-1},Y,S\}\) meets all three
source-pairing caps and has logarithmic inverse at most \(CZ_Y\).
Including \(S\) separately is necessary: \(Y\ge n^{-1}\) need not
give \(S\ge n^{-1}\) when \(\lambda>16\). The candidate correctly
requires resubstitution in coefficient and quadrature formulas.

These conclusions remove a numerical precision use of the lower label
gate. They do not establish a source event uniform in vanishing labels.
The retained fixed-label asymptotic qualification and the alternative of
keeping \(n\ge Y^{-1}\) are both stated explicitly. At \(Y=0\),
the stationary zero predictor is a valid separate branch.

## 5. Deterministic tail and variational gates

For the training-query version of ANALYTIC_TAIL_EXTENSION, the old
parameter-ball left side is at most
\(A_{\rm tail}(en)^{-16}\), with the candidate's (27).
The three nontrivial thresholds in (28) imply respectively
\[
 A_{\rm tail}n^{-16}\le\frac1{16},\qquad
 A_{\rm tail}n^{-16}\le\frac{SH_L}{16},\qquad
 A_{\rm tail}n^{-16}\le\frac{a}{32\sqrt nP_*}.
\]
The exponent \(2/31\) is correct because the last rearrangement
uses \(n^{16-1/2}=n^{31/2}\). Thus the minimum is at most
\(b_n/4<b_n/2\); the original factor \(e^{-16}\) gives further
slack. The carrier recurrence gives \(C_{\rm tail}\le\beta^{20L}\)
with slack, and its gate follows from
\(n(en)^{-16}\le n^{-15}\) and \(\sqrt\ell\ge1\), giving
exactly (29).

The cancellations in (30) are exact. More explicitly,
\(2Y\sqrt r=S/(8\sqrt r)\), while
\(8Y\sqrt{\mathcal K}c_{\rm safe}
=S\lambda\sqrt{\mathcal K}/[2B(1+\lambda)]\).
Together with \(r^{-1}\le\beta^{6L}\), these bound the thresholds
polynomially in \(\beta^L\), with no inverse-label factor and no
stronger upper label cap.

For the variational absorption, division by \(n^{1/4000}\) leaves
the required inequality
\[
 n^{3/4000}\ge2e^{1/4}(2\mathcal B)^{1/4000},
\]
whose solution is exactly (30a). The large numerical constant is
parameter independent. The separate condition
\(\ell\ge\max\{e^2,2\mathcal B\}\), with
\(\mathcal B=1024e^2L\), costs \(e^{CL}\), a fixed power of
\(\beta^L\), and has no inverse-gap dependence. Retaining
\(\log(2\mathcal B)\) in the indicated interpolation estimate is
also valid. None of these observations removes the dimension dependence
of the distinct spherical source-count formulas.

## Remaining conditional boundary

The deterministic gate repair and its numerical substitutions are supported
by the permitted formulas and the checks above. The source probability
still uses fixed-degree limits and unspecified insertion constants. The
finite scalar-forcing and finite-packet proof dependencies identified by
the candidate are absent from the packet. The fitting probability supplied
by GENERAL_EXPLICIT_FITTING has its own explicit dimension and confidence
costs. This report does not upgrade any of those inputs or authorize a
blanket decoder or polynomial stochastic-width claim.
