**CLEAN — within the requested scientific-library integration scope.** I found no required correction in the new proofs, their stated conclusions, or the implementation interfaces audited below. All 90 tests and the frozen-bottom guide example passed. Every input and the manifest remained unchanged.

This is scoped acceptance. It does **not** accept every older chapter theorem: 23,500 older-body lines were not read substantively. Hashing and structural checks over those lines provide no mathematical acceptance.

**Review contract.** I worked independently, without delegation. Mathematical and code evidence came exclusively from `INPUTS.json` and its 27 listed files. I personally read both requested skills and all three requested references:

- [solve-math-rigorously/SKILL.md](/etc/codex/skills/solve-math-rigorously/SKILL.md)
- [investigate-conjectures/SKILL.md](/etc/codex/skills/investigate-conjectures/SKILL.md)
- [research-contract.md](/etc/codex/skills/investigate-conjectures/references/research-contract.md)
- [evidence-ledger.md](/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md)
- [adversarial-audit.md](/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md)

These supplied review procedure, not additional mathematical premises. I inspected no checkout, study, stored data, other packet, previous verdict, task history, or external source. No training or trajectory simulation was performed. The only writes were the boundary tests’ temporary fixtures under the supplied scratch directory; their `TemporaryDirectory` contexts removed them. No report or other artifact was written.

**Exact integrity ledger.** For every row below, the SHA-256, byte count, and line count matched the manifest before review and again after all reading and execution. The final check also verified newline termination and agreement between newline counts and split-line counts.

“Full” means every line was substantively read. Partial files have their exact ranges immediately after this table.

| Input | Bytes | Lines | Content read | SHA-256, identical before and after |
|---|---:|---:|---|---|
| `Makefile` | 257 | 9 | Full: 1–9 | `740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65` |
| `code/README.md` | 23,528 | 437 | Full: 1–437 | `1bd1a68b9357c054dfc4a7e1b708ef302bcc357e776229e33247b5c00a3316d7` |
| `code/pde/__init__.py` | 611 | 26 | Full: 1–26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/exact_calculus.py` | 10,108 | 249 | Full: 1–249 | `d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3` |
| `code/pde/finite_jets.py` | 8,466 | 176 | Full: 1–176 | `1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2` |
| `code/pde/finite_network.py` | 15,525 | 363 | Full: 1–363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_reductions.py` | 15,571 | 346 | Full: 1–346 | `391dc35773a35d86f889cebda9f95820d793a656f2fb05f9b01bb7453be20a4c` |
| `code/pde/gaussian_moments.py` | 4,464 | 114 | Full: 1–114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tests/test_exact_calculus.py` | 10,214 | 217 | Full: 1–217 | `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242` |
| `code/tests/test_finite_jets.py` | 15,562 | 296 | Full: 1–296 | `991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a` |
| `code/tests/test_finite_network.py` | 15,154 | 297 | Full: 1–297 | `a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931` |
| `code/tests/test_finite_reductions.py` | 18,563 | 340 | Full: 1–340 | `7b1a4023334956a25afd4217de7a311145b64c240fc78b87f84b16d2af7dedb0` |
| `code/tests/test_gaussian_moments.py` | 5,179 | 110 | Full: 1–110 | `9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea` |
| `code/tests/test_library_boundary.py` | 2,352 | 58 | Full: 1–58 | `375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a` |
| `code/tests/test_numerical_contract.py` | 10,601 | 202 | Full: 1–202 | `c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92` |
| `code/tools/check_library.py` | 4,910 | 100 | Full: 1–100 | `7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6` |
| `docs/NOTATION.md` | 5,110 | 98 | Full: 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | 20,440 | 265 | Full: 1–265 | `d87109e73ec792779d1e495538b74488950c08865e21e4f29aa32f1a1937ff5a` |
| `docs/arctan_limits.md` | 143,086 | 3,117 | Partial | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `docs/continuous_depth.md` | 88,920 | 2,474 | Partial | `1ce60f0ff159851b0087c143c49eeb59d227f7b2cf675d53dda07f24989f515d` |
| `docs/finite_dynamics.md` | 48,489 | 1,275 | Full: 1–1275 | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/finite_optimization_and_controls.md` | 135,529 | 3,394 | Partial | `6c598905b1ba51b69d9bae9f336baaca26534ff8ce3e9e93ea5faa146e00c7e3` |
| `docs/gaussian_calculus.md` | 193,338 | 4,719 | Partial | `73b19ef2212596d25ce3caaa96eb772427fbc4d35d304bc754dc0459c3e61b8d` |
| `docs/global_nonlinear.md` | 83,472 | 1,796 | Partial | `becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95` |
| `docs/linear_dynamics.md` | 104,904 | 2,641 | Partial | `c1920b78c8788c6025776943944da4f4756717cb8250189e7e91ea81ee830090` |
| `docs/special_data_limits.md` | 466,384 | 9,362 | Partial | `be4573af77f32d53913b1a50f0eb6e003f54bbf7571db95951d47ebc6c65719a` |
| `requirements.txt` | 111 | 2 | Full: 1–2 | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |

The manifest itself was read completely, lines **1–169**, and independently fingerprinted before and after:

```text
INPUTS.json
bytes: 5232
lines: 169
sha256: 32c415fae346bd6084098e9f6fe51ebd4a776de8c9582e538ca176fb3c480816
```

**Exact partial-file read ledger.** Ranges are inclusive. Scope/navigation reads are not proof acceptance. For each fully read file above, scope-only and unread ranges are empty.

| File | Complete technical/proof reads | Scope/navigation reads | Unread as mathematical text |
|---|---|---|---|
| `docs/arctan_limits.md` | None | 1–100 | 101–3117 |
| `docs/continuous_depth.md` | 1886–2474 | 1–100 | 101–1885 |
| `docs/finite_optimization_and_controls.md` | 2410–3394 | 1–100 | 101–2409 |
| `docs/gaussian_calculus.md` | 1–262; 1824–2440; 3305–3671; 4169–4719 | Exact list below | Exact list below |
| `docs/global_nonlinear.md` | None | 1–100 | 101–1796 |
| `docs/linear_dynamics.md` | None | 1–100 | 101–2641 |
| `docs/special_data_limits.md` | None | 1–100 | 101–9362 |

Gaussian scope/navigation ranges:

```text
263–270; 361; 470; 536; 643; 770; 896; 1127; 1180; 1558;
1729; 1749; 2441; 2451; 2528; 2643; 2741; 2904; 3093;
3206; 3672; 3682; 3838; 3916; 4050
```

Gaussian unread ranges:

```text
271–360; 362–469; 471–535; 537–642; 644–769; 771–895;
897–1126; 1128–1179; 1181–1557; 1559–1728; 1730–1748;
1750–1823; 2442–2450; 2452–2527; 2529–2642; 2644–2740;
2742–2903; 2905–3092; 3094–3205; 3207–3304; 3673–3681;
3683–3837; 3839–3915; 3917–4049; 4051–4168
```

The additional complete Gaussian reads cover the finite conditioning and derivative identities, exact Gaussian moments, moving physical-flow jets, forest/certificate foundations, and finite loss-GD pullback interfaces. They do not amount to reviewing the older fixed-program or positive-metric/Taylor-obstruction proofs.

| Aggregate, excluding manifest | Lines | Bytes |
|---|---:|---:|
| 20 files read completely | 4,980 | 235,215 |
| Complete technical sections in partial files | 3,371 | 131,878 |
| Scope/navigation reads | 632 | 30,264 |
| **Total substantive content read** | **8,983** | **397,357** |
| Unread older bodies | 23,500 | 1,053,491 |
| **All 27 inputs** | **32,483** | **1,450,848** |

The four prescribed new-proof ranges contain **2,738 lines**, all read. Including the manifest, the packet totals **32,652 lines and 1,456,080 bytes**; substantive reads total **9,152 lines and 402,589 bytes**. Repeated reads are counted once. Mechanical hashing and structural scans are excluded from substantive-read counts.

**Normalization and interface contract.** The core implementation agrees with [NOTATION.md](/tmp/pde_assembly2_final_library_r2/docs/NOTATION.md) and the fully read finite-dynamics chapter:

\[
z^{(1)}=W^{(1)}X/\sqrt d,\qquad
z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
f=a^Th^{(L)}/n.
\]

There is no additional hidden-forward width factor. The initializer draws first entries with variance \(1\), hidden entries with variance \(1/n\), and stored readout entries with variance \(1/n^2\), using a local explicitly seeded generator.

For mean full-square loss, the raw output derivatives are
\[
\nabla_{W^{(1)}}f_a=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},
\quad
\nabla_{W^{(\ell)}}f_a=\frac{\delta_a^{(\ell)}
(h_a^{(\ell-1)})^T}{n},
\quad
\nabla_a f_a=h_a^{(L)}/n.
\]
Applying mobilities \(n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}\) yields the implementation’s velocity and kernel blocks. Consequently,
\[
\dot f=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr.
\]
Neither \(\delta\) nor the raw kernel contains a residual.

The reviewed exceptions are explicitly specified:

| Result/model | Initialization and activation | Clock/loss |
|---|---|---|
| Shallow Gaussian §11 | Independent order-one \(a,u\); normalized \(C^{12}\) activation with the stated derivative bounds | Feature-ascent Euler; no loss factor |
| Frozen quadratic §8 | Frozen \(h_j=u_j^2/\sqrt3\); Gaussian connector; order-one stored readout | Half-square physical loss |
| ReLU §9 | \(\sqrt2\,z_+\); order-one readout | Half-square physical loss; prescribed kink value |
| Controls §14 obstruction | Deterministic correlated hidden initialization; exactly zero initial readout | Arctangent; full-square loss |
| Controls §14 Gaussian volume bound | Independent Gaussian hidden blocks; stored readout variance \(n^{-2}\) | Arctangent; feature flow and full-square physical flow separately |
| Continuous §15 | Coherent kernel; fixed bounded input profiles/readout; \(C_b^2\) activation | General \(C^2\), lower-bounded loss; physical training time |

The core accepts a fixed finite batch without whitening or Gram inversion. None of these interfaces silently changes a finite dataset into a data population or fixed depth into a depth limit.

**Gaussian §11: all six subsections accepted within their statements.** The complete proof begins at [line 4169](/tmp/pde_assembly2_final_library_r2/docs/gaussian_calculus.md:4169).

For **§11.1**, the two-coordinate recurrence is exactly the metric output gradient:
\[
g(a,u)=(\phi(u),a\phi'(u))=\nabla[a\phi(u)].
\]
Neuron coordinates remain functions of independent initial pairs. Thus, for every fixed finite \(N,h\), the expected finite-width average equals \(F_{N,1}(h)\) at every width. This identification requires no reused-matrix theorem.

For **§11.2**, the specified constant is genuinely activation-only:
\[
B_\phi^{\rm sh}=E\,\mathcal C_M(1+|a_0|+|u_0|).
\]
The recursion defining \(\mathcal C_M\) is finite and uses earlier quantities only. Since \(\Lambda=12MR\) and \(P=e^{3R}\), every envelope is bounded by a polynomial in \(R\) times \(e^{CR}\). Gaussian integrability follows from the negative quadratic density exponent. The constant does not conceal a trajectory derivative or an unproved modulus.

For **§11.3**, the exact defect
\[
E_h^2z-E_{2h}z
=h^2\int_0^1Dg(z+\tau hg(z))[g(z)]\,d\tau
\]
has the stated sign. The hybrid telescope transports each defect through the remaining fine steps without commuting Euler maps. This yields
\[
\psi(E_{2h}^kz)-\psi(E_h^{2k}z)=h^2Q_k(h,z).
\]

For **§11.4**, the interpolation point is a convex combination of the coarse and fine endpoints. It is not improperly treated as an Euler iterate. The allotted Euler coefficients and \(|h|k\le(16M)^{-1}\) give
\[
R(z_{\rm relevant})\le e^{3/8}R(z_0)<2R(z_0).
\]
The differentiated recurrences retain all terms:
\(Dg\,y'\), \(D^2g[y',y']\), \(Dg\,y''\), and the cubic chain-rule terms. The subsequent tangent transport also differentiates its moving coefficient \(Dg(z)\). Its Leibniz recurrence yields
\[
\sup_{|h|\le c/k}|\partial_h^3Q_k(h,z_0)|
\le6\mathcal C_M(R)k^4.
\]
There are \(k\) defects and at most \(k^3\) from three step derivatives. The lower derivative envelopes supply the domination needed for successive differentiation under expectation. The \(C^{12}\) assumption exceeds the derivative orders actually used here.

For **§11.5**, simultaneous replacement
\((h,a_0,u_0)\mapsto(-h,-a_0,u_0)\) proves oddness of the expected output. Therefore the expected factored defect has zero constant and quadratic terms. The cubic calculation gives
\[
F_{N,1}^{(3)}(0)
=\frac{N(4N^2-3N+1)}2\mathsf S
+2N(N-1)(2N-1)\mathsf H,
\]
where
\[
\mathsf S=E D^3\psi[g,g,g],\qquad
\mathsf H=E\|Dg[g]\|^2.
\]
Averaging the independent readout powers \(Ea_0^2=1\), \(Ea_0^4=3\) gives
\(\mathsf S+4\mathsf H=J_\phi\), including the coefficient \(11\) multiplying \(\phi\phi'^2\phi''\). Thus
\[
\left|F_{k,1}(2h)-F_{2k,1}(h)
+\frac{k(2k-1)}2J_\phi h^3\right|
\le B_\phi^{\rm sh}k^4|h|^5.
\]

The sharpness witness \(\phi(z)=z\) satisfies the activation contract and gives
\[
F_{N,1}(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2.
\]
Its fifth discrepancy coefficient is
\[
-\frac43k(k-1)(2k-1)(8k-9).
\]
Taking \(h\to0\) at each fixed \(k\), then increasing \(k\), rules out a uniform replacement \(k^p\) with \(p<4\). The constant-activation branch is also handled correctly.

For **§11.6**, substituting \(h=s/(2k)\) produces an \(O(k^{-1})\) difference on \(|s|\le S\le2c_\phi\). Summation over \(k=2^j\) gives the stated uniform continuous terminal-expectation limit and its explicit tail bound. It does not establish partition independence, hidden-state convergence, restartability, or physical-loss GD convergence. The chapter introduction and reading guide preserve these restrictions.

**Finite dynamics §§8–9: all new subsections accepted.** The full chapter, including its introductory scope and older finite foundations, was read.

For **§8.1**, differentiating the unreduced frozen model gives
\[
f=\frac c n\sum_i a_i z_i^2,\qquad
a_i^+=a_i+csz_i^2,\qquad
z_i^+=z_i+2cQs\,a_i z_i,
\]
where \(c=1/\sqrt3\), \(Q=\|h\|^2/n\), and \(s=-\eta r\). Multiplication of the simultaneous connector update by the unchanged \(h\) proves the second reduced update exactly. The connector/readout kernel is
\[
K=\frac{4c^2Q}{n}\sum_i a_i^2z_i^2
+\frac{c^2}{n}\sum_i z_i^4,
\]
so the half-loss identities are \(\dot f=-rK\) and \(\dot\ell=-r^2K\).

The initialization calculation is consistent:
\[
EQ_n=1,\qquad
\operatorname{Var}(Q_n)=\frac{32}{3n},\qquad
E(f_n^0)^2=\frac1n\left(1+\frac{32}{3n}\right).
\]
These follow from \(EG^4=3\), \(EG^8=105\), conditional row independence, and the centered readout.

The arbitrary vanishing-mesh argument has the necessary uniformity. Before an output hit,
\[
(1-\delta)\eta_n\le s_k\le(1+\delta)\eta_n,
\]
and every readout coordinate increases. Any currently negative row was negative at all preceding steps, which justifies the single initialization-dependent lower envelope
\[
a_i^k(z_i^k)^2\ge
-a_{i,-}^0(z_i^0)^2
e^{4cQ_n(1+\delta)T a_{i,-}^0}.
\]
Its conditional second moment is uniformly finite on \(Q_n\in[1/2,2]\). Conditional Chebyshev therefore controls the entire negative contribution at all relevant grid times without a union bound over steps.

A fixed positive Gaussian tail block has asymptotic positive row density. Its coordinates dominate
\[
y^+\ge y+\gamma\eta_n y^2,\qquad \gamma=c(1-\delta).
\]
The reciprocal estimate supplies a width-independent hitting-time bound for each fixed target level \(M\). The proof chooses the tail threshold and then \(M\) using only \(T,\delta\); subsequently \(\eta_nM\to0\). No condition coupling \(\eta_n\) to \(n\) is hidden here. The favorable contribution eventually exceeds the bounded negative contribution, contradicting survival.

The interpolation argument also works: continuity of the predictor recomputed from raw interpolated parameters forces passage through \(\delta\) or \(-\delta\). The resulting fixed predictor and half-loss changes at times tending to zero contradict uniform convergence in probability to continuous paths with the initialized traces, including random continuous proposed limits.

For **§8.2**, the width-one deletion example is algebraically valid. With \(f=aw^2u^4\), its full and frozen steps share \(a^+,w^+\), while
\[
u^+/u=-1-4\varepsilon.
\]
The chosen parameters make the frozen output negative, and the full output is its multiple \((1+4\varepsilon)^4>1\). It is therefore strictly smaller. This defeats the proposed pathwise lower comparison. The state depends on the step and is deterministic; it supplies no Gaussian-typical fully trained obstruction.

For **§9.1**, the contact construction retains both the direct connector term and the bottom-layer response. At the displayed width-two state,
\[
\dot z_1^{(2)}=\frac34(4a_1v+2a_2c),
\]
giving negative-side velocity \(3/8>0\), positive-side velocity
\(\frac34(1/2-4\lambda)<0\), and a nonzero prescribed contact velocity after avoiding at most one \(\lambda\).

If an absolutely continuous continuation existed, \(w=|z_1^{(2)}|\) would have negative derivative where positive and derivative zero almost everywhere on its zero level set. Integration forces \(w\equiv0\), contradicting the assigned nonzero normal velocity at contact. The open-set reachability argument uses a bounded smooth field within the adjacent sign cell, with the contact reached before leaving the neighborhood. Positive Gaussian probability follows from the finite-dimensional Gaussian density. This establishes the prescribed-field obstruction, not nonexistence for every differential inclusion.

For **§9.2**, the restriction \(|\sigma|\le\sqrt2\) is sufficient for the pathwise bound
\[
R^+\le R+6\eta R^5,
\quad
R=\max\{1,\|a\|/\sqrt n,\|u\|/\sqrt n,\|W\|_{\rm op}\}.
\]
The constants \(R_*=6\), \(S=12\), and
\[
T_0=\frac1{384\cdot6^4}
\]
close the discrete induction through \(2T_0\). Eventually every interpolation endpoint needed through \(T_0\) lies in that interval.

The Gaussian norm event has probability tending to one; the matrix-net exponent is sufficient because \(9/2>\log81\). ReLU Lipschitzness then bounds the recomputed predictors uniformly and gives a common Lipschitz constant. Compact containment yields tightness in \(C([0,T_0];\mathbb R^2)\). Conditional initialization gives \(EF_n(0)^2=1/n\), fixing the limiting traces.

The interpolation comparisons are justified: predictor differences are \(O(\eta_n)\), and the difference between interpolated grid losses and the loss of the interpolated grid predictor is exactly
\[
\frac12\lambda(1-\lambda)(x-y)^2.
\]
No differentiability at a kink or discrete energy inequality is used. The conclusion remains local scalar-law tightness, without determinism or uniqueness.

For **§9.3**, the invariant-strip transformation gives the exact identity
\[
x_{k+1}=x_k+\lambda-I_k,\qquad
\left|\sum_{k=j}^{j+N-1}I_k-N\lambda\right|<1.
\]
Thus all positive integer moments of the binary occupation have limit \(\lambda\), whereas substituting the mean gate gives second moment \(\lambda^2\). The identical/complementary phase examples correctly show that equal marginal occupations need not determine joint products. These are frozen scalar witnesses, not asserted reachable random-network configurations.

**Controls §14: all seven subsections accepted.** The complete new section begins at [line 2410](/tmp/pde_assembly2_final_library_r2/docs/finite_optimization_and_controls.md:2410).

For **§14.1**, the scaled coordinates
\[
\Theta=(z^{(1)},\sqrt nW^{(2)},\sqrt nW^{(3)},c)
\]
make the stored parameter metric \(1/n\) times the Euclidean metric. With \(\mathscr F=nf\), feature ascent is exactly
\(b=\nabla_\Theta\mathscr F\), and \(f'=\|b\|^2/n\). The potential, Hessian, mobilities, and physical clock therefore agree.

For **§14.2**, the tangent maps \(T_2,T_3\) include the variations of the trained matrices, with the required \(1/\sqrt n\) factors. The complete hidden Hessian is
\[
u^TAu
=\sum_{\ell=1}^3(T_\ell u)^TM_\ell T_\ell u
+2(S_2u)^TD_1T_1u
+2(S_3u)^TD_2T_2u.
\]
The last two terms arise from differentiating the matrix-feature products twice and cannot be dropped.

The full Hessian is
\[
\mathsf B=\begin{pmatrix}A&J^T\\J&0\end{pmatrix}.
\]
The material formulas differentiate the moving preactivations, both transposes, diagonal activation derivatives, and readout. In particular, \(M_3'\) contains the readout contribution \(\phi''(z^{(3)})h^{(3)}\). The full-tangent identity
\[
U^T(\mathsf B'-\kappa\mathsf B^2)U
=u^TA'u+2\xi^TJ'u
-\kappa\bigl(\|Au+J^T\xi\|^2+\|Ju\|^2\bigr)
\]
is correct.

For **§14.3**, the terminal matrices have the stated bounded operator norms. The orthogonal bulk and two-coordinate components yield
\[
q^{(2)}_{\rm rare}=\sqrt n\,k\,v,\qquad
\nu_{2,\rm rare}=\sqrt n\,k(\mu v-w),
\]
with \(\mu=(\pi/4)^2<1\) and \(k=\varepsilon\phi'(Z)\). Since the rare preactivations vanish, \(\phi''(0)=0\) removes their potentially large Hessian diagonal. But \(\phi'''(0)=-2\) gives
\[
(M_2')_{11}=2(1-\mu)nk^2>0.
\]

For the prescribed unit connector tangent, the complete calculation is
\[
U_n^T\mathsf B'U_n
=2\mu(1-\mu)nk^2
+\mu\{\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H\}
+\frac{a_0\Lambda}{2}\varepsilon k\phi''(Z).
\]
The latter terms are width-independent, and \(\phi'(Z)\) has a positive width-independent lower bound. The full Hessian is bounded at this terminal state, so subtracting any fixed real \(\kappa\mathsf B^2\) cannot cancel the linear-in-\(n\) positive term.

The scalar arctangent identity quoted in the section does not invalidate this construction: a positive-semidefinite, non-diagonal mobility need not preserve coordinatewise signs of the response products.

For **§14.4**, identical third-matrix rows and a common readout form an invariant subspace. The backward construction uses
\[
\chi'=\phi(y),
\]
with \(y\) kept positively bounded below. The primal derivative estimates are proportional to \(\chi\); over backward duration \(O(\varepsilon)\), their accumulated changes are \(O(\varepsilon^2)\). The stated \(\varepsilon_0\) closes the matrix and output margins uniformly in width. Fixed-width bounded-state continuation reaches exactly \(\chi=0\), and
\[
\varepsilon/(\pi/2)\le\tau_n\le\varepsilon/h_*.
\]
This proves genuine reachability. It does not assume a Hessian bound throughout the segment or identify the constructed initialization with independent Gaussians.

For **§14.5**, the full physical Jacobian and its material derivative correctly include the residual-clock terms:
\[
\mathsf C=\alpha\mathsf B-\frac2n bb^T,\qquad \alpha=2(1-f),
\]
\[
\dot{\mathsf C}
=\alpha^2\mathsf B'
-\frac{2\alpha}{n}\|b\|^2\mathsf B
-\frac{2\alpha}{n}\{(\mathsf Bb)b^T+b(\mathsf Bb)^T\}.
\]
On the constructed segment, \(\alpha\in[3/2,2]\). At the terminal point, \(\|\mathsf B\|\) and \(\|b\|/\sqrt n\) are bounded, so both correction terms have bounded operator norm. The positive order-\(n\) Rayleigh quotient survives in physical time.

The obstruction therefore rejects a pointwise width-independent signed bound based only on the stated primal norms. It does not reject an estimate using Hessian history, additional responses, Gaussian typicality, or time integration.

For **§14.6**, bounded arctangent and bounded slope give polynomial primal bounds in both feature-time directions:
\[
R(u)=R_0+Pu,\quad
K_3(u)=M+PR_0u+\tfrac12P^2u^2,\quad
K_2(u)=M+P\int_0^uK_3(v)R(v)\,dv.
\]
They establish complete finite feature flow and smooth invertible full response.

The nuclear estimate uses the correct quantity for every tangent plane. Diagonal terms satisfy
\[
\|T^T\operatorname{diag}(d)T\|_*
\le\|T\|_{\rm op}^2\sum_i|d_i|;
\]
the mixed terms and readout off-diagonal block have rank \(O(n)\), despite the full parameter dimension being \(O(n^2)\). This yields
\[
\|\mathsf B\|_*\le n\mathcal P_S(M,R_0)
\]
with the explicit polynomial displayed in the text.

For every full-rank transported tangent matrix,
\[
\frac{d}{ds}\log V_{\mathcal T}
=\operatorname{Tr}(\Pi_{\mathcal T}\mathsf B),
\]
and \(\Pi_{\mathcal T}\) is an orthogonal projector. Hence
\[
\left|\log\frac{V_{\mathcal T}(s)}{V_{\mathcal T}(0)}\right|
\le n|s|\mathcal P_S.
\]
This controls every initial plane simultaneously, not merely the full-dimensional determinant.

The Gaussian expectation step is supported by explicit matrix-net tails and all-order RMS moments. In particular, the small stored readout gives \(ER_0^p\le C_pn^{-p}\). Hölder controls the mixed monomials, proving the expected supremum of absolute log-volume change is \(O(n)\).

For physical time, the signed feature clock is controlled by the residual equation even when the initial residual changes sign across initializations. The additional rank-one term \(2bb^T/n\) has the stated nuclear norm and is included in the polynomial envelope. The result is an expectation bound for **absolute log-volume change**, not an expectation bound for volume or a width-independent response norm.

For **§14.7**, orthonormalizing the full hidden-initial tangent response gives
\[
|\det\mathsf P|
=V_{\mathcal T}\sqrt{\det(I_n-Q_CQ_C^T)}
=V_{\mathcal T}\prod_{j=1}^n\sqrt{1-a_j^2}.
\]
The singular-value argument correctly changes determinant dimension and includes singular \(\mathsf P\). The full-volume bound supplies no lower bound on this additional factor.

Where \(\mathsf P\) is invertible,
\[
\log|\det\mathsf P|
=\log V_{\mathcal T}
-\tfrac12\log\det(I_n+\mathsf K\mathsf K^T),
\qquad
\mathsf K'=J-\mathsf KA-\mathsf KJ^T\mathsf K.
\]
The derivative holds at fixed initial readout; it is not a conditional covariance. The physical-time block Riccati equation correctly uses \(\mathsf C\), including clock terms. No projected nonsingularity, projected entropy bound, or adaptive Gaussian-query estimate follows.

**Continuous-depth §15: all four subsections accepted.** The complete section begins at [line 1886](/tmp/pde_assembly2_final_library_r2/docs/continuous_depth.md:1886).

For **§15.1**, the coherent finite model uses \(W_\ell/n\) and residual increment \(\alpha/L\), with fixed endpoints. Direct differentiation gives
\[
\nabla_{W_\ell}f_a
=\frac{\alpha}{Ln^2}b_a^{(\ell)}
(h_a^{(\ell-1)})^T.
\]
Mobility \(Ln^2\) therefore yields the stated physical flow and
\[
\dot{\mathcal E}_n
=-\frac1{Ln^2}\sum_\ell\|\dot W_\ell\|_F^2.
\]
The loss derivatives are summed before squaring, preserving cross-sample terms. The cell embedding has exactly this normalized metric and acts as \(W_\ell/n\). This proves metric compatibility, not convergence of trained discretizations.

For **§15.2**, the carrier is the intersection of the row and column mixed spaces, with their common \(L^2(U^2)\) representative. This proves completeness of \(\mathcal K\). The depth space is explicitly the **Bochner**
\[
\mathbb K=L^2((0,1);\mathcal K),
\]
requiring strong measurability. Joint scalar measurability plus finite displayed norms is not substituted for that condition.

The row and column estimates
\[
\|T_kg\|_\infty\le\rho(k)\|g\|_2,\qquad
\|T_k^*g\|_\infty\le\chi(k)\|g\|_2
\]
use the actual adjoint. Continuous bilinear action and outer-product maps preserve the strong measurability needed for the subsequent integrals.

For **§15.3**, the hypotheses are adequate: fixed bounded endpoints, finitely many samples, \(\phi\in C_b^2\), a \(C^2\) lower-bounded loss, and \(w_0\in\mathbb K\).

The forward and backward depth contractions use integrable row and column bounds. They produce Bochner absolutely continuous \(L^\infty(U)\)-valued paths. The local field \(Z\) only needs \(L^2\) in depth. In the adjoint comparison, the potentially problematic product
\[
\chi(w(s))\|Z(s)-\widetilde Z(s)\|_\infty
\]
is integrable by Cauchy–Schwarz. Thus the local Lipschitz proof works in the actual carrier without imposing an unproved maximum-over-depth bound.

The Fréchet derivative argument also uses the correct topology. Its nonlinear remainder is bounded by \(M_2|\zeta|^2/2\); integrating the \(L^2\)-depth estimate gives an \(O(\|v\|_{\mathbb K}^2)\) forcing remainder. Gronwall then establishes the claimed derivative. Pairing the variational forward equation with the residual-free adjoint cancels the homogeneous terms and gives
\[
D\mathcal E(w)[v]=\langle\mathcal G(w),v\rangle_{\mathbb H}.
\]
This is an \(\mathbb H\)-pairing gradient for a functional on the strong carrier. The text correctly avoids claiming Fréchet differentiability on an open subset of bare \(\mathbb H\).

Global continuation does not rely on energy alone. Its order is essential:

1. Energy bounds \(\|w(t)\|_{\mathbb H}\).
2. The Hilbert-space adjoint estimate bounds \(\sup_s\|P_a(s,t)\|_2\).
3. The outer-product column estimate gives \(C_w(t)\le C_w(0)+A_Tt\).
4. The backward equation converts this to an \(L^\infty\) adjoint bound.
5. The row estimate gives \(R_w(t)\le R_w(0)+B_{0,T}t+\tfrac12B_{1,T}t^2\).

These estimates bound the full \(\mathbb K\) norm. The local field bound then makes the trajectory Cauchy in that Banach space at a hypothetical finite endpoint, permitting continuation. This establishes the global \(C^1\) flow, uniqueness, and restart semigroup in the stated carrier.

For **§15.4**, the advertised scope matches the proof: coherent \(W/n\), fixed endpoints, bounded activation, and a current infinite-dimensional kernel state. No ReLU extension, trained-endpoint theorem, fitting result, noisy dense approximation, Gaussian-bulk identification, or joint width/depth/GD-step limit is obtained.

**Implementation and older finite foundations.** All production code, tests, checker, guide, build file, and requirements were read completely.

The fully read finite-dynamics §§1–7 support the core and reduction APIs. Global finite physical GF follows from local Lipschitzness and the energy displacement estimate: a finite maximal endpoint would yield a Cauchy parameter limit in the fixed-width metric, permitting restart. Bounded slopes supply the stated fixed-depth RMS and kernel bounds; they do not supply population compactness.

The quadratic/identity reduction formulas agree with direct differentiation:

- QI: \(u'=2u\odot B^Ta,\ B'=ah^T/n,\ a'=z\).
- IQ: \(u'=2B^T(a\odot z),\ B'=2(a\odot z)h^T/n,\ a'=z^2\).
- QQ: the bottom derivative gains the additional factor \(2u\).

Their kernel blocks are precisely squared output-gradient norms in the declared metric. The isometric Lax factors use \(a/\sqrt n\) or \(h/\sqrt n\); their commutator laws preserve spectra while retaining orientation. The explicit orientation witness has equal output and similar Lax operators but kernels \(68/9\) and \(28/3\), so spectra do not determine output speed.

For RMS normalization,
\[
DN_\varepsilon(x)
=\sigma^{-1}(I-N_\varepsilon(x)N_\varepsilon(x)^T/n).
\]
Both denominators are differentiated in the code. The matrices called \(\Pi_h,\Pi_v\) are positive definite for \(\varepsilon>0\), generally not projections. The code’s backward vectors, feature derivatives, kernels, and signed balance drifts match this derivative. The reduced sign quotient is justified through finite raw lifts and local uniqueness; no \(\varepsilon=0\) continuation is asserted.

The remaining interface findings are:

| Interface | Substantiation and acceptance |
|---|---|
| Core finite network | Correct raw normalization, residual-free backpropagation, block mobilities, simultaneous GD, and mean-loss factors. Arbitrary finite batches retain their correlations. |
| Core numerical contract | Callback inputs/results are copied as documented. Parameters remain mutable internally. Scaled products address selected exponent-range failures; raw matrix arithmetic still has the documented float64 limitations. |
| `flow_jet` | Ordinary-coefficient convolution and composition implement the complete moving physical recurrence through order three. The same moving transpose and residual are retained. Terminal backward coefficients are omitted, so \(C^3\) suffices. |
| Jet clock conversion | The supplied proof correctly gives \(\ddot f=b^2F''-2b(F')^2\) and \(f^{(3)}=b^3F'''-8b^2F'F''+4b(F')^3\). The implementation is not a frozen-direction expansion. |
| `gaussian_moment` | Exact Schur-complement PSD validation handles zero pivots and singular covariances. Wick recursion lowers degree by two, validates before parity shortcuts, and clears its local cache. |
| Forest keys | Rooted-key induction and minimization over roots establish color-preserving tree isomorphism; sorted component keys retain multiplicities. The forest expectation proof separately controls quotient-label powers. |
| Rational certificate | The code regenerates the polynomial derivatives using \(z^2\partial_a+6az\partial_z\), then reverts and composes the series. The complete supplied proof establishes its fixed-order annealed interpretation. Negative shifted determinant and polynomial witness reject only the specified moment representation. |
| Euler words | Composition tuples have weight \(\binom{M}{q}\); paired coefficients are those of \(\binom{2N}{q}-2^j\binom Nq\). Operator order and differentiation of inner moving fields are retained. The separate convex-region bound states the required hybrid containment. |
| `frozen_quadratic` | Correct connector/readout block order, half-loss velocities, and state domain. \(Q=0\) requires \(z=0\); for \(Q>0\), any finite \(z\) has a raw connector realization. |
| `frozen_quadratic_step` | Both increments use the old state. Reduced linear interpolation agrees exactly with multiplying the raw interpolated connector by frozen \(h\). No step-size stability or population-solver guarantee is claimed. |
| Build/checker | Uses the supplied library, standard library, and declared NumPy dependency. The checker is a structural validator, not a theorem verifier or a universal detector of arbitrary dynamic dependencies. |

The guide’s initialization-jet certificate uses raw quadratic activation and feature ascent; it is distinct from the new normalized frozen quadratic half-loss API. I found no conflation between them.

**Execution evidence.** I ran, in the standalone directory:

```sh
TMPDIR=/tmp/pde_assembly2_integration_scratch \
PYTHONDONTWRITEBYTECODE=1 make check
```

Results:

- Structural checker: **25 Markdown/Python files checked**, exit status 0.
- Unit tests: **90 tests passed**, reported test duration 0.431 seconds.
- The five boundary-test methods successfully exercised their scratch fixtures.
- No PDF exporter or exporter tests were required or executed.

I then executed the exact Python statements from `code/README.md` lines **406–412**, with `PYTHONPATH=code`, bytecode disabled, and the supplied scratch directory configured. Both assertions passed.

```text
Python:       3.10.12
NumPy:        1.26.4
output:       0.004618802153517007
residual:    -0.995381197846483
half_loss:    0.4953918645131497
kernel_blocks: [0.01866667 0.00453333]
next_a:        [ 0.30091949 -0.79977013]
next_z:        [ 0.40096547 -0.19871271]
```

Additional authorized inline algebra checks were narrowly bounded:

- Exact integer/rational verification of the shallow identity-activation cubic and fifth coefficients for \(k=1,\ldots,20\): **passed**.
- Independent bivariate Taylor-coefficient evaluation of the full Hessian, including a nonzero readout tangent, at deterministic widths \(4,8,16\): **passed**, maximum absolute discrepancy \(2.61\times10^{-18}\).
- The same independent coefficient method checked the full material identity (14.19): **passed**, maximum absolute discrepancy \(1.67\times10^{-16}\).

These diagnostics used elementary coefficient operations and NumPy; they did not integrate a trajectory or use an automatic-differentiation or symbolic dependency.

**Navigation and dependency findings.** The structural checker passed, and an additional local navigation scan resolved **43 local Markdown references, including 23 fragment references**, with no unresolved file or anchor.

The new chapter introductions and corresponding `docs/README.md` descriptions agree with the audited conclusions: shallow terminal expectations, frozen initial layers, local scalar ReLU compactness, deterministic signed-Hessian failure, full tangent-volume control with an additional projection factor, and coherent-kernel well-posedness remain separately scoped.

The older chapter introductions were read for model and navigation compatibility. Their unread theorem bodies are not accepted by this report. External literature descriptions in `docs/README.md` were read as contextual prose; their links were not followed, their external claims were not independently verified, and they supplied no proof argument.

The runtime and **reviewed proofs and dependencies** require no studies, stored data, archived arrays, chats, historical verdicts, or exporter. The new Gaussian §11, controls §14, and continuous §15 arguments are self-contained with their declared notation and assumptions. The older bodies left unread receive no blanket semantic dependency certification.

**Required corrections: none within the audited scope.** Acceptance is limited to the stated finite identities, exact finite arithmetic interfaces, scoped proofs, and successful execution above. In particular, it grants none of the following extensions:

- ReLU scalar compactness to a deterministic or unique generalized population flow.
- The deterministic reachable Hessian obstruction to Gaussian-typical failure.
- Formal initialization coefficients or certificate arithmetic to positive-time trajectories.
- Full tangent volume to a lower bound on the hidden projected determinant.
- Coherent-kernel existence to noisy dense, Gaussian-bulk, or trained-endpoint convergence.
- Fixed finite data/depth results to data-population, joint depth, or generalization theorems.
- Passing boundary tests to acceptance of the unread older book.