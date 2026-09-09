**CORRECTIONS REQUIRED for unconditional integration acceptance: the required test run remains incomplete.** I found no mathematical or implementation correction in the audited scope. However, `make check` exited with status 2: 85 tests passed, while five boundary-fixture tests could not create temporary directories in this read-only environment. Those errors do not establish a source defect, but I cannot report a successful complete check.

The frozen-bottom guide example passed. Every supplied input and `INPUTS.json` remained unchanged.

**Review contract and method.** This was a fresh, independent, nondelegated review. Mathematical and code evidence came exclusively from the manifest and its 27 listed files. I did not inspect another checkout, study, dataset, temporary packet, historical verdict, task history, or external source. I personally read both requested skills and all three references:

- [solve-math-rigorously/SKILL.md](/etc/codex/skills/solve-math-rigorously/SKILL.md)
- [investigate-conjectures/SKILL.md](/etc/codex/skills/investigate-conjectures/SKILL.md)
- [research-contract.md](/etc/codex/skills/investigate-conjectures/references/research-contract.md)
- [evidence-ledger.md](/etc/codex/skills/investigate-conjectures/references/evidence-ledger.md)
- [adversarial-audit.md](/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md)

I performed no training or trajectory simulation. Computation consisted of the stated tests, the requested guide example, integrity/navigation checks, and small deterministic algebra/derivative checks. No files were edited or artifacts produced inside the packet.

**Integrity ledger.** All byte counts, newline counts and SHA-256 hashes below matched the manifest before substantive review and matched again after reading and execution. Each displayed digest is therefore both the before and after digest.

`C` means the entire file was personally read, lines `1–N` inclusive, with no unread lines. `P` means the exact partial-read ranges appear in the next table.

| Input | Bytes | Lines N | Read | SHA-256, before = after |
|---|---:|---:|:---:|---|
| `Makefile` | 257 | 9 | C | `740d59f44f085975520f375a5d96c8871ecf3a07afdf767c3090bfde61e7db65` |
| `code/README.md` | 23,528 | 437 | C | `1bd1a68b9357c054dfc4a7e1b708ef302bcc357e776229e33247b5c00a3316d7` |
| `code/pde/__init__.py` | 611 | 26 | C | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/exact_calculus.py` | 10,108 | 249 | C | `d7cd27b3bffed6152bb9fad40514a8e2848561fa6d44e0cb1aa0fd652d7e5aa3` |
| `code/pde/finite_jets.py` | 8,466 | 176 | C | `1d8e5bdf4ca056645c720fce69a4df9e82dbbdf840da7f9f4599efe5c401aca2` |
| `code/pde/finite_network.py` | 15,525 | 363 | C | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_reductions.py` | 15,571 | 346 | C | `391dc35773a35d86f889cebda9f95820d793a656f2fb05f9b01bb7453be20a4c` |
| `code/pde/gaussian_moments.py` | 4,464 | 114 | C | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/tests/test_exact_calculus.py` | 10,214 | 217 | C | `58881bee416ba4b5db9e7688003bfcbef985c4fc82e006c29dbe8a25c32ce242` |
| `code/tests/test_finite_jets.py` | 15,562 | 296 | C | `991ae49dc65f1e0970c02ab57596560fabd79a1e71416879b43c52aa5e75c88a` |
| `code/tests/test_finite_network.py` | 15,154 | 297 | C | `a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931` |
| `code/tests/test_finite_reductions.py` | 18,563 | 340 | C | `7b1a4023334956a25afd4217de7a311145b64c240fc78b87f84b16d2af7dedb0` |
| `code/tests/test_gaussian_moments.py` | 5,179 | 110 | C | `9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea` |
| `code/tests/test_library_boundary.py` | 2,352 | 58 | C | `375a033e737923ea5f10df687adb0556baee5bcd1a44dff184b88d76b381966a` |
| `code/tests/test_numerical_contract.py` | 10,601 | 202 | C | `c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92` |
| `code/tools/check_library.py` | 4,910 | 100 | C | `7ae3148f2418ec60744435e0685cde63d2de5a8448816b98d1ed4b700dfb48f6` |
| `docs/NOTATION.md` | 5,110 | 98 | C | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | 20,440 | 265 | C | `d87109e73ec792779d1e495538b74488950c08865e21e4f29aa32f1a1937ff5a` |
| `docs/arctan_limits.md` | 143,086 | 3,117 | P | `19f01b6112949f4d186ef17ff94415804830ed51a519b155ed45343c26cbbead` |
| `docs/continuous_depth.md` | 88,920 | 2,474 | P | `1ce60f0ff159851b0087c143c49eeb59d227f7b2cf675d53dda07f24989f515d` |
| `docs/finite_dynamics.md` | 48,489 | 1,275 | C | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `docs/finite_optimization_and_controls.md` | 135,529 | 3,394 | P | `6c598905b1ba51b69d9bae9f336baaca26534ff8ce3e9e93ea5faa146e00c7e3` |
| `docs/gaussian_calculus.md` | 193,338 | 4,719 | P | `73b19ef2212596d25ce3caaa96eb772427fbc4d35d304bc754dc0459c3e61b8d` |
| `docs/global_nonlinear.md` | 83,472 | 1,796 | P | `becfba469f81bc4573275bc679aa3ee102f2e553c03c00357c3268792a556c95` |
| `docs/linear_dynamics.md` | 104,904 | 2,641 | P | `c1920b78c8788c6025776943944da4f4756717cb8250189e7e91ea81ee830090` |
| `docs/special_data_limits.md` | 466,384 | 9,362 | P | `be4573af77f32d53913b1a50f0eb6e003f54bbf7571db95951d47ebc6c65719a` |
| `requirements.txt` | 111 | 2 | C | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |

The manifest itself was completely read, lines **1–169**, and independently rechecked:

| File | Bytes | Lines | SHA-256, before = after |
|---|---:|---:|---|
| `INPUTS.json` | 5,232 | 169 | `32c415fae346bd6084098e9f6fe51ebd4a776de8c9582e538ca176fb3c480816` |

**Exact partial-read ledger.** Ranges are inclusive. “Scope/navigation” includes introductory conventions and the beginning of some older statements; it does not signify acceptance of their older proof bodies.

| File | Scope/navigation personally read | New proof personally read and audited | Unread older text |
|---|---|---|---|
| `docs/arctan_limits.md` | 1–100 | — | 101–3117 |
| `docs/continuous_depth.md` | 1–100 | 1886–2474 | 101–1885 |
| `docs/finite_optimization_and_controls.md` | 1–110 | 2410–3394 | 111–2409 |
| `docs/gaussian_calculus.md` | 1–120 | 4169–4719 | 121–4168 |
| `docs/global_nonlinear.md` | 1–100 | — | 101–1796 |
| `docs/linear_dynamics.md` | 1–110 | — | 111–2641 |
| `docs/special_data_limits.md` | 1–140 | — | 141–9362 |

All of `finite_dynamics.md`, including its introduction and new lines **663–1275**, was read and audited. Every requested new section includes its full introductory scope paragraphs. The new proofs did not require an omitted older theorem to complete their arguments.

| Unique coverage category, excluding manifest | Lines | Bytes |
|---|---:|---:|
| Twenty completely read files | 4,980 | 235,215 |
| New proofs in the three partially read files | 2,125 | 74,772 |
| Scope/navigation reads in seven partial files | 780 | 36,589 |
| **Total personally read** | **7,885** | **346,576** |
| Unread older text | 24,598 | 1,104,272 |
| **All 27 inputs** | **32,483** | **1,450,848** |

The four expressly required new ranges total **2,738 lines and 98,238 bytes**. Their finite-dynamics portion is already included in the complete-file count, not counted twice. Including the manifest, total packet coverage is **32,652 lines / 1,456,080 bytes**, of which **8,054 lines / 351,808 bytes** were personally read.

Hashing and automated structural scanning consumed complete files mechanically; neither is counted as a personal proof read.

**Normalization, initialization and interface contract.** The notation, finite chapter, guide and production core agree on
\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
f_a=a^Th_a^{(L)}/n.
\]
Stored hidden matrices already contain their initialization scaling. An additional forward factor \(1/\sqrt n\) would be incorrect for this API.

Backpropagation is residual-free:
\[
\delta_a^{(\ell)}=n\,\partial f_a/\partial z_a^{(\ell)}.
\]
With mean full squared loss, the raw gradients are multiplied by \(2/m\), and the mobilities are
\[
n\kappa_1,\ \kappa_2,\ldots,\kappa_L,\ n\kappa_{L+1}.
\]
Consequently
\[
\dot f=-\frac2m Kr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr.
\]
The code’s kernel blocks contain the mobility but neither the residual nor the loss factor. Their Gram-product formulas match these derivatives. Correlated, repeated, opposite and rank-deficient inputs are preserved; no Gram inverse or whitening occurs.

`initialize` draws first entries with variance \(1\), hidden entries with variance \(1/n\), and stored readout entries with variance \(1/n^2\), in the documented order with an explicit private RNG seed. This must not initialize the new order-one-readout theorems without modification.

The distinct conventions are correctly exposed:

| Result/interface | Activation and initialization | Clock/architecture |
|---|---|---|
| Core finite API | Supplied layerwise activation; initializer uses small stored readout | Full mean squared loss; all blocks trained |
| Gaussian §11 | Normalized smooth activation; independent standard Gaussian \(a,u\) | Shallow feature-ascent Euler, without residual |
| Finite §8.1 | \(z^2/\sqrt3\); frozen Gaussian bottom and order-one readout for the theorem | Half-square loss; only connector/readout trained |
| Finite §9 | \(\sqrt2\,z_+\); order-one Gaussian readout | Half-square loss; all blocks trained |
| Controls §14.1–14.5 | Arctangent; deterministic correlated hidden initialization and zero initial readout | Full-loss GF, with explicitly justified feature clock |
| Controls §14.6–14.7 expectation | Arctangent; prescribed independent small-readout Gaussian law | Full finite tangent flow |
| Continuous §15 | Bounded \(C^2\) activation; specified coherent kernel | \(W/n\), fixed endpoints, separate trunk metric |

Raw GD uses the old state in every block. Raw parameters are interpolated first and nonlinear fields recomputed. The arctangent primitive is a continuous-flow identity, not an exact transformation of raw GD into transformed Euler.

The special-data introductory storage conversion \(V^{(1)}=W^{(1)}/\sqrt d\) and loss conversion \(\mathcal L_c=cm\,\mathcal L_{\rm mean}\) are algebraically consistent. These introductory checks do not re-establish that chapter’s population theorems.

**Gaussian §11.1–§11.3: model, explicit constant and exact defect.** The new [shallow proof](/tmp/pde_assembly2_final_library/docs/gaussian_calculus.md:4169) is valid within its stated contract.

For \(\psi(a,u)=a\phi(u)\), its Euclidean gradient is
\[
g(a,u)=(\phi(u),a\phi'(u)).
\]
This gives exactly the feature-ascent recursion. Each neuron depends only on its own independent initial pair. Therefore
\[
E f_n^N(h)=E[A_N\phi(U_N)]
\]
holds at every finite width, rather than requiring a matrix-program limit.

The growth envelope satisfies
\[
R(E_{\alpha h}z)\le(1+\alpha M|h|)R(z),
\qquad R(z)=1+|a|+|u|.
\]
It supplies the integrability needed for this expectation identity.

The coarse/fine comparison uses
\[
C_h=E_{2h},\qquad B_h=E_h\circ E_h,\qquad
B_hz-C_hz=h^2b_h(z),
\]
where
\[
b_h(z)=\int_0^1Dg(z+\tau hg(z))[g(z)]\,d\tau.
\]
Telescoping consecutive hybrid compositions gives the signed transported-defect identity SD16. It does not assume that \(B_h\) and \(C_h\) commute.

The constant \(B_\phi^{\rm sh}\) is explicitly specified through finite nonnegative envelope recursions and a Gaussian expectation. It contains no trajectory-fitted coefficient, stored numerical array, or assumed bound on the desired output derivative.

**Gaussian §11.4: uniform derivative envelopes.** The intermediate-state coverage is sufficient. With \(c=(16M)^{-1}\) and \(k|h|\le c\), pre-defect paths, the actual convex interpolation segment, and the remaining fine steps all satisfy
\[
R(z)\le e^{6Mk|h|}R(z_0)<2R(z_0).
\]
Thus the derivative bounds can use \(\Lambda=12MR(z_0)\). The interpolation is correctly bounded by convexity; it is not incorrectly identified with an Euler trajectory.

The differentiated step recurrences retain the homogeneous tangent factor and every source term. Summing them yields
\[
\|\partial_h^q y_j\|\le X_qk^q,\qquad q=1,2,3.
\]
For example, the second-order source sum gives
\[
X_2=P(8\Lambda X_1+4c\Lambda X_1^2),
\]
and the third-order sources give the displayed \(12\Lambda\) and \(4c\Lambda\) terms. The later \(\mathcal Z_q,T_q,V_q\) recurrences correctly account for derivatives of \(h^2b_h\), the moving interpolation point, and transport of the defect direction.

There are \(k\) transported defects, each costing at most \(k^3\) for its third step derivative. This proves
\[
|\partial_h^3Q_k(h,z_0)|
\le6\mathcal C_M(R(z_0))k^4.
\]
Every envelope is bounded by a polynomial in \(R\) times \(e^{CR}\), not \(e^{CR^2}\). Gaussian integrability therefore holds for every finite constant arising here. Bounds for derivative orders zero through three justify the successive expectation/derivative interchanges. No unproved uniform-integrability premise is hidden in this step.

**Gaussian §11.5: parity, coefficient and sharpness.** The transformation
\[
(h,a_0,u_0)\mapsto(-h,-a_0,u_0)
\]
negates the output and preserves the initial law. Hence the expected discrepancy is odd. After its exact \(h^2\) factorization, the remaining function has vanishing constant and quadratic Taylor terms. Integrating its third derivative gives the claimed fifth-order remainder.

The independent coefficient calculation is consistent. Writing
\[
\mathsf S=E\,D^3\psi[g,g,g],\qquad
\mathsf H=E\|Dg[g]\|^2,
\]
the finite-step derivatives give
\[
F_N^{(3)}(0)
=\frac{N(4N^2-3N+1)}2\mathsf S
+2N(N-1)(2N-1)\mathsf H.
\]
Gaussian averaging over \(a_0\) gives
\[
\begin{aligned}
\mathsf S&=3E[\phi\phi'^2\phi''+\phi'^3\phi'''],\\
\mathsf H&=E[\phi'^4+\phi^2\phi'^2
+2\phi\phi'^2\phi''+3\phi'^2\phi''^2].
\end{aligned}
\]
Thus \(\mathsf S+4\mathsf H=J_\phi\), including the coefficient \(11\) of \(\phi\phi'^2\phi''\). The coarse-minus-fine cubic coefficient is exactly
\[
-\frac{k(2k-1)}2J_\phi.
\]

For \(\phi(z)=z\),
\[
F_N(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2,
\]
and the fifth coefficient is
\[
32\binom{2k}{5}-\binom{4k}{5}
=-\frac43k(k-1)(2k-1)(8k-9).
\]
Its order \(k^4\) proves the asserted sharpness by taking \(h\to0\) at fixed \(k\), then \(k\to\infty\). I additionally checked this integer identity for \(k=1,\ldots,8\). The constant-activation branch also agrees: the discrepancy vanishes.

**Gaussian §11.6: dyadic expectation limit.** Substitution \(h=s/(2k)\) is admissible precisely on the stated interval \(S\le2c_\phi\). It gives
\[
\sup_{|s|\le S}|G_{2k}(s)-G_k(s)|
\le \frac{|J_\phi|S^3}{8k}
+\frac{B_\phi^{\rm sh}S^5}{32k}.
\]
Summing over dyadic \(k\) proves the uniform limit and SD40’s constants. Continuity follows from finite-recursion continuity and uniform convergence.

Accepted conclusion: a short-interval, dyadic, terminal **expected-output** limit. This does not identify a restart state, arbitrary partitions, hidden trajectories, physical-loss GD, or a growing reused-matrix program.

**Finite dynamics §1–§7 and their implementation interfaces.** I read and checked the entire [finite chapter](/tmp/pde_assembly2_final_library/docs/finite_dynamics.md). The all-depth gradients and energy identities are consistent with the core API. Global finite-width GF follows from local Lipschitzness and
\[
\|D^{-1/2}(\theta(t)-\theta(s))\|
\le\sqrt{(t-s)\mathcal L(0)}.
\]
At fixed width this prevents a finite-time parameter escape and supplies a finite limiting state for continuation. Bounded slopes are needed for the further width-uniform forward/backward RMS bounds, not for the basic finite smooth-flow continuation.

For QI/IQ/QQ, differentiating the raw output gives the chapter’s feature-ascent fields and kernels. In particular the first-block ascent factors are \(2u\odot q\), \(2q\), and \(4u\odot q\), respectively. Physical velocities multiply the entire field by \(-2r\).

The QI/IQ Lax factors use the correct Euclidean isometries \(v/\sqrt n\). Their commutator equations follow from symmetric generators anticommuting with the signature matrix. The retained matrices have size \(n+1\). The orientation witness has the same output \(1/3\) and conjugate Lax matrices, but kernels \(68/9\) and \(28/3\); it therefore refutes the specified spectrum-based instantaneous closure.

The RMS derivative is
\[
DN_\varepsilon(x)
=\sigma^{-1}\left(I-\frac{N_\varepsilon(x)N_\varepsilon(x)^T}{n}\right).
\]
For \(\varepsilon>0\), the parenthesis has radial eigenvalue \(\varepsilon/\sigma^2\); it is not generally an orthogonal projection. Both denominators are differentiated in the chapter and code. The resulting row and column balance drifts are
\[
-4fv_i^2,\qquad
\frac{4\varepsilon f}{\beta^2}h_j^2.
\]
The reduced RMS restart statement is correctly restricted to raw-image states with \(\|h\|^2/n<1\). None of these identities establishes a population limit.

**Finite §8.1: frozen reduction, arbitrary vanishing steps and API.** For \(c=1/\sqrt3\),
\[
f=\frac cn\sum_i a_i z_i^2,\qquad Q=\|h\|^2/n,
\]
raw differentiation gives
\[
a^+=a-\eta r\,cz^2,\qquad
z^+=z-\eta r\,2cQ\,a\odot z.
\]
The two raw kernel blocks are
\[
K_W=4c^2Q\,\frac1n\sum_i a_i^2z_i^2,\qquad
K_a=c^2\,\frac1n\sum_i z_i^4.
\]
The half-loss identities are therefore
\[
\dot f=-r(K_W+K_a),\qquad
\dot\ell=-r^2(K_W+K_a).
\]
These agree with [the frozen API](/tmp/pde_assembly2_final_library/code/pde/finite_reductions.py:257), including its connector/readout block order.

The API’s reduced-state domain is exact. If \(Q=0\), then \(h=0\) requires \(z=0\). If \(Q>0\), every finite \(z\) is realizable by
\[
W=zh^T/\|h\|^2.
\]
`frozen_quadratic_step` uses one old-state evaluation for both increments. It does not silently train the bottom vector.

For the probabilistic theorem, conditioning on the frozen bottom gives independent rows
\[
a_i^0\sim N(0,1),\qquad z_i^0\sim N(0,Q_n).
\]
The moment computations are correct:
\[
EQ_n=1,\quad \operatorname{Var}(Q_n)=\frac{32}{3n},\quad
E(f_n^0)^2=\frac1n\left(1+\frac{32}{3n}\right).
\]

The hitting-time proof handles every deterministic constant-per-width step sequence \(\eta_n\downarrow0\), without a width-dependent rate assumption:

- Before an output hit, \((1-\delta)\eta_n\le s_k\le(1+\delta)\eta_n\), and every \(a_i^k\) increases.
- A row still negative is controlled by its initial negative readout and an exponential envelope. One conditional Chebyshev event bounds the aggregate negative contribution at **all** surviving grid times. There is no growing-step union bound.
- A fixed positive Gaussian tail block has asymptotic frequency at least \(p_b/2\). Its coordinates dominate \(y^+=y+\gamma\eta_n y^2\).
- The reciprocal decrement reaches a fixed level \(M\) within \(2\sqrt2/(\gamma b)+\eta_n\). The proof chooses \(b\), then \(M\), independently of width. Eventually \(\gamma\eta_nM\le1\), regardless of the rate \(\eta_n\to0\).
- The resulting positive contribution contradicts survival below \(\delta\).

Thus \(\tau_n(\delta)\to0\) in probability. Continuous raw interpolation must cross \(\delta\) or \(-\delta\), yielding a predictor change bounded away from zero and a loss displacement at least \(\delta-\delta^2/2\) from the limiting initial loss. This excludes uniform-in-probability convergence to a continuous initialized path.

This is a frozen-bottom obstruction under its specific unbounded quadratic activation and Gaussian initialization. It is not a theorem for fully trained quadratic dynamics or arbitrary nonuniform time meshes.

**Finite §8.2: failure of deletion comparison.** The width-one calculation is exact. The full and frozen steps share \(a^+,w^+\), while
\[
u^+/u=-1-4\varepsilon.
\]
The frozen terminal output is negative, so multiplication by \((1+4\varepsilon)^4>1\) makes the fully trained output strictly smaller. Choosing \(\rho\) sufficiently small keeps all named outputs within the survival interval. This refutes the proposed pointwise comparison, even for arbitrarily small steps with step-dependent states. It provides no typical-Gaussian trajectory conclusion.

**Finite §9.1: reached prescribed-ReLU noncontinuation.** At the stated width-two contact, direct multiplication gives the normal velocities
\[
p=\frac38>0,\qquad
q=\frac34(1/2-4\lambda)<0,\qquad
v_0=\frac34(1/2-4\lambda\sigma/c).
\]
For every prescribed real \(\sigma\), choosing \(\lambda>1/8\) outside at most one exceptional value makes \(v_0\ne0\).

Both adjacent smooth fields point into the contact surface. If an absolutely continuous continuation existed, \(w=|z_1^{(2)}|\) would have negative derivative wherever positive and zero derivative almost everywhere on its zero set. Integration forces \(w\equiv0\), contradicting the assigned nonzero normal derivative on the gate.

The preceding smooth trajectory reaches such a contact from an open set: bounded speed prevents escape from the chosen neighborhood before the strictly decreasing normal coordinate hits zero. The independent finite Gaussian law has positive density on that open set. The proof therefore establishes the stated reached obstruction, not merely a specially initialized contact.

Its scope is the prescribed pointwise vector field, even in the almost-everywhere absolutely continuous solution class. Differential inclusions with additional selection rules remain separate.

**Finite §9.2: positive local scalar Euler compactness.** Here the restriction \(|\sigma|\le\sqrt2\) is essential to the displayed bounds and is stated. The proof gives
\[
R^+\le R+6\eta R^5.
\]
On the high-probability initialization event, telescoping bounds \(R\le12\) through the enlarged horizon. The constants satisfy the required identity
\[
6T_*(2\cdot6)^5=6.
\]
Eventually \(\eta_n\le T_0\), so every endpoint needed for interpolation through \(T_0\) lies within this controlled interval.

ReLU Lipschitzness, not differentiation through gates, bounds the recomputed output’s modulus. The stated \(60S^7\) coefficient is a valid conservative bound. Bounded equicontinuous output paths form a compact subset of the uniform path space; the loss is their continuous image. The treatment of finitely many smaller widths completes tightness of the whole sequence.

The initialization computation \(EF_n(0)^2=1/n\) fixes the trace of every weak subsequential limit. Raw-recomputed and grid-linear predictor interpolants differ by \(O(\eta_n)\) on the high-probability event. The additional discrepancy between linear loss interpolation and the loss of a linear predictor is exactly
\[
\frac12\lambda(1-\lambda)(x-y)^2=O(\eta_n^2).
\]
Consequently all stated interpolation variants have the same subsequential limits.

Accepted conclusion: tightness in \(C([0,T_0];\mathbb R^2)\), with initialized traces. No uniqueness, deterministic population dynamics, kernel limit, full-state compactness, or extension beyond \(T_0\) follows.

**Finite §9.3: occupation information.** In the invariant strip, the exact normalized update is
\[
x_{k+1}=x_k+\lambda-I_k.
\]
Its telescoping discrepancy is strictly less than one, proving the occupation frequency. Since \(I_k^r=I_k\), every positive integer gate moment averages to \(\lambda\), while replacing the gate by its mean gives second moment \(\lambda^2\).

The equal-speed examples correctly distinguish identical from complementary phases: identical marginals can have joint product averages \(1/2\) or zero. These are frozen scalar witnesses, explicitly not asserted reachable random-network configurations. They substantiate why scalar-output compactness does not identify the products entering neural kernels.

**Controls §14.1–§14.2: complete finite geometry.** In the scaled coordinates
\[
\Theta=(z^{(1)},\sqrt nW^{(2)},\sqrt nW^{(3)},c),
\qquad \mathscr F=nf,
\]
the feature field is \(b=\nabla\mathscr F\), with
\[
\mathsf B=Db=
\begin{pmatrix}A&J^T\\J&0\end{pmatrix}.
\]
This correctly represents the stored mobilities \((n,1,1,n)\).

The [Hessian formula](/tmp/pde_assembly2_final_library/docs/finite_optimization_and_controls.md:2517)
\[
u^TAu=\sum_{\ell=1}^3(T_\ell u)^TM_\ell T_\ell u
+2(S_2u)^TD_1T_1u+2(S_3u)^TD_2T_2u
\]
contains both mixed matrix/feature terms. It follows by twice differentiating the forward map along a straight parameter variation.

The material derivative formulas differentiate:

- all current preactivations and activation derivatives;
- both trained matrices in their forward and transpose uses;
- the moving readout;
- the tangent maps \(T_\ell,S_\ell\).

The resulting full quadratic form is
\[
U^T(\mathsf B'-\kappa\mathsf B^2)U
=u^TA'u+2\xi^TJ'u
-\kappa\bigl(\|Au+J^T\xi\|^2+\|Ju\|^2\bigr).
\]
This is the complete finite Jacobian/material identity, not a diagonal activation calculation.

**Controls §14.3: terminal obstruction.** The balanced vector and bulk/rare-coordinate orthogonalities in the construction give the stated matrix operator norms and forward/backward fields. In particular,
\[
\nu_{2,\mathrm{rare}}
=\sqrt n\,k(\mu v-w),\qquad
q^{(2)}_{\mathrm{rare}}=\sqrt n\,kv.
\]
At the first rare coordinate,
\[
\nu_{2,1}q_1^{(2)}=(\mu-1)nk^2<0.
\]
Because \(\phi''(0)=0\) but \(\phi'''(0)=-2\), \(M_2\) vanishes there whereas
\[
(M_2')_{11}=2(1-\mu)nk^2>0.
\]

For the specified unit matrix tangent, the complete material derivative equals
\[
\begin{aligned}
U_n^T\mathsf B'U_n
={}&2\mu(1-\mu)nk^2\\
&+\mu\{\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H\}\\
&+(a_0\Lambda/2)\varepsilon k\phi''(Z).
\end{aligned}
\]
The remaining terms are bounded independently of width. The terminal Hessian is uniformly bounded because the potentially concentrated diagonal term vanishes and the mixed maps are controlled by RMS norms. Hence subtracting any fixed real \(\kappa\mathsf B^2\) cannot cancel the positive order-\(n\) term.

The scalar identity
\[
\phi'''\phi'-\tfrac32(\phi'')^2=-2(\phi')^4
\]
does not contradict this: the actual middle mobility mixes coordinates, and the material velocity need not have the scalar sign pattern.

I independently differentiated the forward potential twice in the specified tangent and then differentiated that expression along the full feature field. At \(n=4,8,32\), the results matched equation 14.19 within \(1.5\times10^{-12}\). This checked the identity; it was not a trajectory or numerical reachability test.

**Controls §14.4–§14.5: reachability and physical clock.** Identical third-matrix rows and a common readout form an invariant subspace. Backwards from the terminal state,
\[
d\chi/d\sigma=-\phi(y)\le-h_*.
\]
The explicit smallness conditions on \(\varepsilon\) keep both matrix norms inside their margins and \(y\) bounded away from zero until \(\chi\) reaches zero. Fixed-width bounded-state continuation justifies the entire backward segment. Its length satisfies
\[
\varepsilon/(\pi/2)\le\tau_n\le\varepsilon/h_*.
\]
This constructs an actual deterministic initial state with exactly zero readout; it is not an assumed initial state on an inaccessible terminal surface.

Along the forward segment, \(0\le f\le1/4\), so
\[
\alpha=2(1-f)\in[3/2,2].
\]
The physical Jacobian is
\[
\mathsf C=\alpha\mathsf B-\frac2n bb^T,
\]
and its material derivative is
\[
\dot{\mathsf C}
=\alpha^2\mathsf B'
-\frac{2\alpha}{n}\|b\|^2\mathsf B
-\frac{2\alpha}{n}\{(\mathsf Bb)b^T+b(\mathsf Bb)^T\}.
\]
The clock corrections have bounded terminal operator norm. The physical obstruction therefore follows with the stated positive order-\(n\) lower bound.

Accepted conclusion: failure of the specified width-independent pointwise signed estimate under the stated primal bounds, even from zero readout. The construction is deterministic and correlated. It neither establishes a Gaussian-typical obstruction nor rules out estimates using Hessian history, integrated control, or additional response information.

**Controls §14.6: positive nuclear and every-plane volume bounds.** Bounded activation gives a triangular polynomial continuation estimate:
\[
R(u)=R_0+Pu,\qquad
K_3(u)=M+PR_0u+\tfrac12P^2u^2,\qquad
K_2(u)=M+P\int_0^uK_3(v)R(v)\,dv.
\]
These bound the readout RMS and both matrix norms in either feature-time direction. The first-layer displacement is then bounded by integrating \(K_2K_3R\). Thus the finite feature flow is complete and has an invertible full derivative.

The nuclear estimate uses the full Hessian decomposition. Diagonal curvature terms satisfy
\[
\|T^T\operatorname{diag}(d)T\|_*
\le\|T\|_{\rm op}^2\sum_i|d_i|.
\]
The diagonal sums are \(O(n)\) by RMS bounds; mixed terms have rank at most \(2n\). With \(t_2=P+K_2\), \(t_3=P+K_3t_2\), this proves
\[
\|\mathsf B\|_*\le n\mathcal P_S,
\]
where
\[
\mathcal P_S
=2R(K_2K_3+t_2^2K_3+t_3^2)
+4R(K_3+t_2)+2t_3.
\]

For every full-column-rank transported tangent matrix,
\[
\frac d{ds}\log\sqrt{\det(\mathcal T^T\mathcal T)}
=\operatorname{Tr}(\Pi_{\mathcal T}\mathsf B).
\]
The projector has operator norm one, so the nuclear trace bound applies simultaneously to every tangent plane and every tangent dimension. Integration gives both upper and lower bounds
\[
e^{-n|s|\mathcal P_S}
\le\frac{V_{\mathcal T}(s)}{V_{\mathcal T}(0)}
\le e^{n|s|\mathcal P_S}.
\]

The Gaussian expectation step is justified under the full prescribed law. The finite-net tail bound provides all width-uniform moments of the initial hidden operator norms. Convexity/concavity gives the required Gaussian RMS moments, including \(ER_0^p\le C_pn^{-p}\). Hölder controls each mixed polynomial monomial. Thus the expected supremum of the absolute log-volume change is \(O(n)\).

The physical result also retains \(-2bb^T/n\), allows either initial residual sign, and uses the bounded signed clock variation. It does not replace fixed-physical-time derivatives with fixed-feature-time derivatives.

These are expected **log-volume** bounds. They do not by themselves provide a width-independent largest singular value or an exponential-moment bound for volume.

**Controls §14.7: hidden projection.** For the hidden initial plane,
\[
\mathcal T=\binom{\mathsf P}{\mathsf R},\qquad
Q=\mathcal T(\mathcal T^T\mathcal T)^{-1/2}
=\binom{Q_H}{Q_C},
\]
the orthonormal-column identity gives
\[
|\det\mathsf P|
=V_{\mathcal T}\sqrt{\det(I_n-Q_CQ_C^T)}
=V_{\mathcal T}\prod_{j=1}^n\sqrt{1-a_j^2}.
\]
The singular-value argument justifies changing determinant dimension and includes singular \(\mathsf P\).

Where \(\mathsf P\) is invertible,
\[
\log|\det\mathsf P|
=\log V_{\mathcal T}
-\tfrac12\log\det(I_n+\mathsf K\mathsf K^T),
\qquad \mathsf K=\mathsf R\mathsf P^{-1},
\]
and
\[
\mathsf K'=J-\mathsf KA-\mathsf KJ^T\mathsf K.
\]
The physical block Riccati equation correctly includes every block of \(\mathsf C\).

The extra factor can approach zero independently of the full intrinsic-volume estimate. The chapter appropriately claims no hidden-projection nonsingularity, projected lower-volume/entropy bound, conditional covariance estimate, or adaptive-query control.

**Continuous §15.1–§15.2: finite metric and actual carrier.** The [coherent-kernel section](/tmp/pde_assembly2_final_library/docs/continuous_depth.md:1886) uses a separate architecture. Its finite derivatives satisfy
\[
\nabla_{W_\ell}f_a
=\frac{\alpha}{Ln^2}b_a^{(\ell)}(h_a^{(\ell-1)})^T.
\]
Mobility \(Ln^2\) yields the stated update and dissipation
\[
\dot{\mathcal E}_n
=-\frac1{Ln^2}\sum_\ell\|\dot W_\ell\|_F^2.
\]
The batch sum is taken before squaring. Embedding depth and neuron cells gives precisely the \(L^2(ds\,du\,dv)\) metric and operator action \(W_\ell/n\).

The strong kernel space is the intersection of row- and column-\(L^2\)-bounded kernels. Completeness follows because Cauchy limits in the two mixed spaces share the same scalar \(L^2\) representative. The depth space is expressly
\[
\mathbb K=L^2_s(\mathcal K)
\]
in the **Bochner** sense. The text does not silently equate joint scalar measurability with strong \(\mathcal K\)-valued measurability.

Cauchy–Schwarz proves the row and column actions into \(L^\infty\); Fubini identifies the actual adjoint. The outer-product row/column formulas are correct, and the relevant continuous bilinear maps preserve strong measurability. This supports the claimed Bochner integrals.

**Continuous §15.3: existence, gradient and global continuation.** Under bounded fixed endpoints, \(\phi\in C_b^2\), lower-bounded \(C^2\) loss, and \(w_0\in\mathbb K\), the proof supplies all necessary stages.

First, depth contractions use the integrable row/column coefficients. They construct unique \(L^\infty\)-valued Bochner absolutely continuous forward and adjoint curves. Bounded activation gives a uniform forward bound, while the adjoint initially has the stated exponential column-bound estimate.

Second, local Lipschitzness closes in the actual carrier. Forward differences are controlled uniformly in depth; local-field differences are controlled in \(L^2_sL^\infty_u\). The adjoint difference contains
\[
\chi(w)\,\|Z-\widetilde Z\|_\infty,
\]
whose depth integral is finite by Cauchy–Schwarz. No maximum-over-depth preactivation bound is inserted. Outer-product estimates then prove local boundedness and Lipschitzness of \(\mathcal G:\mathbb K\to\mathbb K\).

Third, the Fréchet derivative is justified despite having only a depth-\(L^2\) field bound. The Taylor remainder integrates to
\[
O\!\left(\|Z(w+v)-Z(w)\|_{L^2_sL^\infty_u}^2\right)
=O(\|v\|_{\mathbb K}^2).
\]
The remaining product error is likewise quadratic. Gronwall establishes the proposed linearized forward equation. Pairing with the actual adjoint cancels the homogeneous terms and gives
\[
D\mathcal E(w)[v]=\langle\mathcal G(w),v\rangle_{\mathbb H}.
\]
This is an \(\mathbb H\)-pairing representation of the derivative on \(\mathbb K\), not an asserted extension to an open set of bare \(\mathbb H\).

Finally, global continuation closes in the stronger norm through an ordered argument:
\[
\text{energy in }\mathbb H
\ \Longrightarrow\ P\text{ bounded in }L^2
\ \Longrightarrow\ \text{column growth bounded}
\ \Longrightarrow\ P\text{ bounded in }L^\infty
\ \Longrightarrow\ \text{row growth bounded}.
\]
The resulting column bound is linear and row bound quadratic in training time on each fixed horizon. Together they bound \(\|w(t)\|_{\mathbb K}\). Local boundedness of \(\mathcal G\) then makes a putative finite terminal path Cauchy in that Banach space, permitting restart and ruling out a finite maximal endpoint.

The proof therefore establishes global \(C^1\) training flow, uniqueness, the energy identity and restart from every state in the stated carrier.

**Continuous §15.4: scope.** The conclusion keeps bounded fixed input/readout profiles, finite sample count, bounded \(C^2\) activation, coherent normalization and the specified metric. The proof neither constructs the Gaussian \(W/\sqrt n\) model nor proves finite-network approximation, noisy joint width/depth convergence, raw-GD convergence, fitting, or population-of-data convergence. The introduction and conclusion agree on these restrictions.

**Remaining production interfaces and their tests.** All code was read in full; the following acceptance concerns the actual finite operations.

| Interface | Substantiation and acceptance limit |
|---|---|
| `finite_network` | Raw derivatives, mobility cancellation, batch normalization, kernel Gram products and simultaneous GD match the finite chapter. Coordinate/output finite differences and energy tests provide independent numerical checks. |
| `finite_jets.flow_jet` | Ordinary Taylor coefficients use full bilinear convolutions. Both matrices, their reused transpose, and the residual move. Division by \(k+1\) is correct. Output order three needs activation derivatives only through order three; the unused terminal backward coefficient is not computed. This is a finite derivative oracle, not a positive-time Taylor theorem. |
| `gaussian_moment` | Exact rational Schur complements handle positive and zero pivots, including singular covariance. Wick recursion removes one leg and counts remaining pairing multiplicities. Validation occurs before constant/odd-degree shortcuts; the cache is local and cleared. |
| `forest_key` | Sorted rooted color encodings, minimized over roots and sorted over components, characterize finite colored-forest isomorphism while preserving component multiplicity. Union-find rejects cycles and duplicate edges. It is not a general coefficient compiler. |
| `revert_series`, `determinant` | Coefficient matching isolates the new inverse coefficient through the nonzero linear term. Rational elimination tracks row-swap signs and handles singular/empty matrices. Independent composition and permutation-determinant tests passed. |
| `quadratic_axis_certificate` | The implementation regenerates derivatives from \(X=z^2\partial_a+6az\partial_z\), Gaussian scalar moments, series reversion and exact rational quadratic forms. The displayed certificate tests passed. This verifies the finite certificate arithmetic; it does not re-audit the older Gaussian initialization-jet theorem. |
| Euler pullback primitives | Positive compositions carry \(\binom{N}{q}\); paired coefficients implement \(\binom{2N}{q}-2^j\binom Nq\). Slot enumeration and direct nonlinear scalar composition through degree six passed. These finite words do not give growing-step or population convergence. |
| Mixed/RMS reductions | Their gradients, field derivatives, kernels, physical factors, Lax conventions and balance drifts agree with the fully read finite chapter. |
| Frozen quadratic evaluator/step | Correct half-loss factors, old-state simultaneous update, realizable reduced domain, fresh outputs, and documented numerical restrictions. All four dedicated tests passed. |

The older exact certificate’s raw-square feature field is distinct from the new normalized frozen quadratic half-loss API. Their coefficients and clocks must not be interchanged.

Callback inputs/results are copied where the guide promises ownership. `Parameters` constructor aliasing is explicitly documented. Float64 evaluators reject the specified nonfinite results but do not promise universal intermediate-overflow protection or certified rounding. The core’s scaled-product treatment is correctly narrower than such a promise; the reductions explicitly retain ordinary float64 intermediate restrictions.

**Execution evidence.** The installed runtime was **Python 3.10.12, NumPy 1.26.4**, matching the pinned NumPy requirement. No heavy dependency was installed or used.

`make check` produced:

| Stage | Result |
|---|---|
| Standalone boundary/link checker | Passed: 25 `.md`/`.py` files |
| Unittest discovery | 90 tests attempted |
| Passed tests | 85 |
| Assertion failures | 0 |
| Errors | 5 boundary-fixture tests |
| Overall command | Exit status 2 |

All five errors arose at `tempfile.TemporaryDirectory`, before fixture assertions, with:
```text
FileNotFoundError: [Errno 2] No usable temporary directory found in
['/tmp', '/var/tmp', '/usr/tmp', '/tmp/pde_assembly2_final_library']
```

The blocked tests cover dangling symlinks, existing relative modules, missing links, missing/undeclared modules, and valid links/math lookalikes. Their source was audited, but their fixture assertions did not execute. I did not skip them, mock a passing result, modify the tests, or bypass the read-only restriction.

I then executed the exact Python example from `code/README.md`, lines **406–412**, including both assertions. It passed:

```text
output          0.004618802153517007
residual       -0.995381197846483
loss            0.4953918645131497
kernel_blocks  [0.018666666666666675, 0.004533333333333335]
output_velocity 0.02309284379003842
loss_velocity  -0.02298618251341016
next_a         [0.3009194937640367, -0.7997701265589908]
next_z         [0.40096546845223857, -0.19871270873034858]
```

**Navigation, provenance and claim ledger.** A manifest-only automated scan checked **43 local links, including 23 fragments**, without finding an unresolved target. The four external contextual references in the reading guide were not opened or independently verified. The production runtime imports only the supplied package, standard-library facilities and NumPy. The audited new proofs are self-contained with their stated notation and elementary analytic/probabilistic arguments; neither their proofs nor runtime need studies, stored data, archived arrays, chats or historical verdicts.

The PDF exporter and its tests were absent from the manifest and from the executed 90-test suite. Their absence is consistent with the requested standalone scope.

| Claim | Review status | Exact limit |
|---|---|---|
| New shallow estimate and dyadic consequence | Proved under stated hypotheses | Feature-ascent expected output; short interval; dyadic consequence |
| Frozen quadratic initial layer | Proved under stated initialization | Frozen bottom; deterministic \(\eta_n\to0\); convergence in probability |
| Prescribed ReLU contact obstruction | Proved | Reached width-two event of positive probability; no width-uniform probability claim |
| ReLU Euler output compactness | Proved | Local scalar path laws; subsequential distributional limits |
| Coherent kernel flow | Proved | Global strong Bochner carrier flow with fixed endpoints |
| Full Hessian/material/clock identities | Exact under stated finite model | All trained blocks included |
| Reachable signed obstruction | Proved | Deterministic correlated construction; no Gaussian-typical inference |
| Nuclear and intrinsic-volume bounds | Proved | Every full tangent plane; Gaussian expected absolute log-volume |
| Hidden-projection factor | Exact | Additional factor remains uncontrolled |
| Finite implementation checks | Supported by source audit and passing numerical/exact tests | Finite arithmetic and stated contracts |
| Complete `make check` validation | Incomplete | Five fixture tests blocked by filesystem permissions |

The chapter introductions and guide accurately describe the **new** conclusions. Older chapter theorem claims appearing in those introductions were read for compatibility and scope, not independently accepted through their unread proofs.

**Required resolution and acceptance limits.** No mathematical or production-code change is requested on the evidence of this review. The sole outstanding integration requirement is to rerun the unchanged `make check` with a writable temporary directory **outside the packet**, retaining disabled bytecode generation. The five fixture tests must execute successfully before the complete check can be recorded as passing.

Acceptance is otherwise confined to the personally audited proofs and interfaces above. It does not promote compactness to uniqueness, deterministic constructions to Gaussian-typical behavior, formal coefficients to trajectories, coherent kernels to noisy dense limits, or finite results to population results. It also does not imply whole-book proof acceptance from hashes, navigation checks, or boundary tests.