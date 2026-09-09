# Exact TP-III TeX source audit after access recovery

9 September 2026. Fresh, isolated source audit of `/tmp/tp3-audit.Trwr6N/proofs.tex`, authorized by the user. Only this report was written. Existing files, including the master and both comparison audits, were preserved. No experiments, source-code execution, replay of historical shell commands, task operations or messages, other agents, permission changes, or research campaign were used.

## Decision for the master

**The exact-file access limitation is resolved; the Appendix-N proof gap is not.** The recovered TeX contains the same no-rank-stability statement, normalization errors, scalar-feedback conditioning issue, and unproved conditional-coefficient step identified in the existing primary-literature audit. No source comment, qualification, alternate local proof, or additional estimate found in the fully read proof file and its required local dependencies closes that step.

The central unresolved result is **Lemma N.2**, source label `lemma:ADeltah`, at [proofs.tex:3948](/tmp/tp3-audit.Trwr6N/proofs.tex:3948): preservation of all vanishing empirical moments under the reused matrix action $A\Delta h$. **Section N.3** is the induction section; **Lemma N.3**, label `lemma:removeVanishing`, is the separate, elementary pseudo-Lipschitz perturbation lemma. These three references must not be confused.

This audit does **not** establish a counterexample to Theorem E.15, TP-IV G.4, or the parameterless TP-III master theorem. It establishes that the exact newly readable source does not discharge the existing deeper-import proof obligation. The theorem's stated scope and the certification status of its printed proof remain distinct.

## Read protocol, exact identity, and coverage

I personally read the mathematical skill [SKILL.md](/etc/codex/skills/solve-math-rigorously/SKILL.md), all lines 1–115, before the audit. Its requirement to check imported theorem hypotheses guided the dependency trace. No applicable `AGENTS.md` was found at the checked ancestors of the source and output paths. The user-defined single-report scope governed this work.

The initial independent pass read the entire substantive proof text and the main local definitions/statements before opening either comparison audit. An in-session checkpoint recorded the coefficient gap, normalization error, remaining scalar dependence, and the limited scope of the earlier moment estimates before that comparison. Subsequent reads checked correspondence, repaired output truncation, and checked EOF. Conclusions were not copied from the earlier audits and then presented as an independent check.

### Entire proof file, including comments and EOF

The file is **168,962 bytes**, SHA256 **`b601c9a00007dd033c4cda2fa5fb412d87cbadf5e42117aeccd3fe20cc63d3da`**, agreeing with the user's fingerprint. It has **3,970 logical lines**, although `wc -l` reports **3,969 newline characters**: the final `\end{document}` at line 3970 has no trailing newline. That final line was explicitly read during EOF verification. It is not missing mathematical text.

The user's later coordination update reports an archive copy with exactly one terminal newline added and that the root has already updated access wording. Those are coordination facts, not an additional archive identity check performed here. This report's fingerprint and line references concern the original file, whose hash was rechecked unchanged. The archive newline is not a mathematical correction.

Full consecutive proof reads were requested for lines **1–300, 301–700, 701–1100, 1101–1500, 1501–1800, 1801–2250, 2251–2650, 2651–3050, 3051–3450, 3451–3969**. A combined tool response clipped the middle of the 301–1100 output; **661–820 was explicitly reread**, covering the omitted material. EOF was then explicitly reread at **3963–3970**, including the unterminated last line. The union is **1–3970 without a gap**. Percent comments, footnotes, labels, macro definitions, and all proofs were included; this was not a search-only read.

| Proof-file range | Content fully read |
|---|---|
| 1–1149 | Appendix K: probability, pseudoinverses, Gaussian conditioning, Hermite expansions, projection correlations, weak/strong Gaussian-image laws and their moment proof |
| 1150–3784 | Appendix L: parameterless master theorem, all preliminaries, adjunction calculations, base cases, conditional means/covariances, rank/zero stability, core-set induction, and all three moment-convergence terms and helper proofs |
| 3785–3868 | Appendix M: parameter-controlled extension **assuming** rank stability |
| 3869–3970 | Appendix N: no-rank extension, definitions/invariants, base case, both induction branches, Lemmas N.2–N.3, and EOF |

### Local dependency reads and hashes

All file links below point into the exact source folder. SHA256 hashes identify complete files; a hash is not a claim to have read unlisted ranges.

| File | Bytes; logical lines | Personally read scope | SHA256 |
|---|---:|---|---|
| [main.tex](/tmp/tp3-audit.Trwr6N/main.tex) | 34,055; 410 | **All 1–410**: macros, title, assembly order, surrounding assertions | `3f81af940e629af7510e521898bfa8134bb8c1f44220213f9389aa363747e55e` |
| [NetsorT2.tex](/tmp/tp3-audit.Trwr6N/NetsorT2.tex) | 21,364; 239 | **All 1–239**: fixed program, initialization, $Z,\hat Z,\dot Z$, parameterless theorem, derivative/regression convention | `fd17b3ffc58ee9fef10d27e090f9556d7f89ea9d4ccf1ca31074c357ecefa5f2` |
| [advancedNetsorT.tex](/tmp/tp3-audit.Trwr6N/advancedNetsorT.tex) | 34,294; 401 | **All 1–401**: scalar instructions, regularity, rank assumption, all three scalar-program theorem variants, variable dimensions | `5d3b8745c6999dac98b24922dd74e56780ed52df5bb5a00470261233ca646a78` |
| [extraTheorems.tex](/tmp/tp3-audit.Trwr6N/extraTheorems.tex) | 10,653; 163 | **All 1–163**: mean/conditional-expectation assertions, norm-tail fact, conjectured stronger mean convergence, extension conditions | `c98f990eb8c1f03422409da254b5d6deac7cc908fd91409a7f24bbcd1b807db6` |
| [proofsketch.tex](/tmp/tp3-audit.Trwr6N/proofsketch.tex) | 17,981; 165 | **All 1–165**: G-vars, finite conditioning, rank and Gaussian-image proof outline | `5d849f2b690a045c77aabd21d6e89bbf8a7e6d1bc44663abad4f317e2e541d20` |
| [FIPProof.tex](/tmp/tp3-audit.Trwr6N/FIPProof.tex) | 27,028; 294 | **1–35 and 85–146**, including the complete imported `prop:hatZRandomSource` statement and its proof instruction, 135–144; not the complete FIP proof | `a3d77562236be4e52d79ccecf12f2880fdd3241394b2dd683d3fb28423001e59` |
| [mymacros.sty](/tmp/tp3-audit.Trwr6N/mymacros.sty) | 1,905; 74 | **All 1–74**; no macro changes the contested formula | `bbb91dcc0d54e92c2b0d7505d918a547eab889bae3d2a0c127f83e033b9e88a7` |
| [main.bbl](/tmp/tp3-audit.Trwr6N/main.bbl) | 19,624; 435 | **47–59, 260–269, 327–337**: Bayati–Montanari, O'Donnell, Tao citation identities; no claim of reading their external proofs | `03cddf00d24cd0a7fd260bf37e8d3db3beb194cd755e9ce270e5255a445c5e79` |

Dependency output repairs: the clipped `advancedNetsorT.tex` passage was reread at **290–345**; an omitted `extraTheorems.tex` response was replaced by an untruncated **1–162** read. Final unterminated `\end{document}` lines were separately read at main:410, NetsorT2:239, advancedNetsorT:401, extraTheorems:163, and proofsketch:165. The skill file is 7,593 bytes, SHA256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.

The source-folder inventory and reference searches were used to resolve dependencies, not substituted for the reads above. The other application files, figures, and layout style were not fully read or audited: their unrelated semicircle, Marchenko–Pastur, GP/NTK, and FIP application results are not premises needed to locate the Appendix-N gap. In particular, the imported Gaussian-source measurability proposition has an elementary induction directly from the fully read $Z$-rules: each new $Z$ is formed from earlier $Z$'s and, for a G-var, a new hatted source; conversely a G-var's hatted source is its full $Z$ minus its correction, which depends on previous sources. No downstream FIP theorem is needed for that fact.

### Comparison-audit scope, read after the initial independent check

* [PRIMARY_LITERATURE.md](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/source_audits/PRIMARY_LITERATURE.md): **all of §4, lines 128–202**, including §§4.1–4.4; output additionally included lines 203–205. Whole-file fingerprint: 46,385 bytes, 287 lines, SHA256 `03a93ca3647ee907ccf58b729e3894aa7488b6b1023ae69982bfca02f3bdfef8`. Other sections were indexed, not fully reread. The TP-IV/IIb source claims in that section are comparison context, not newly audited external papers here.
* [OPERATOR1.md](/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/access_recovery_2026_09_09/OPERATOR1.md): **191–224**, complete relevant L2-import discussion and residual-access passage. Whole-file fingerprint: 42,624 bytes, 270 lines, SHA256 `e5dd8fc58ab530e7a477871485056d394edfa3ed76e0901111eddc023036012f`. In particular, lines 199 and 220 record this exact TeX's former inaccessibility. No other Operator1 proof was re-audited here.

These fingerprints were checked again after the comparison reads and were unchanged.

## Correspondence to the readable TP-III text

[tensor-programs-iii.txt](/tmp/tensor-programs-iii.txt) is 423,216 bytes, SHA256 `7da471803779bc2f584cf34b262b47d353ec98181c4ffaa88f4d18b2571648d7`, with 6,338 newline characters and 6,339 logical lines. Its front matter identifies **arXiv:2009.10685v3, 8 May 2021**. This audit read **1–35, 1864–2142, 3900–3975, 4635–4694, 5400–5447, and 6090–6339** for correspondence; the whole text extraction was not newly read.

The correspondence is supported by content and reference structure, not filenames or timestamps:

| TeX label/content | Matching text content |
|---|---|
| `thm:PLNetsorT+MasterTheoremNoRS`, advancedNetsorT:215–236 | Theorem **E.15**, text:2114–2136; same hypotheses, pseudo-Lipschitz tests, scalar convergence, and pointer to Appendix N |
| `assm:asRankStab`, advancedNetsorT:103–109 | Assumption **E.7**, text:1977–1980; same eventual equality of finite-vector and limiting-variable ranks |
| `sec:netsortplusMasterTheoremProof`, proofs:3785–3867 | Appendix **M**, text:6096–6180; same explicit rank assumption and added parameter-fluctuation term |
| `sec:proofNetsorTPlusNoRS`, proofs:3869–3946 | Appendix **N**, text:6182–6305; same ordered invariants, two branches, retained scalar arguments, and malformed normalization |
| `lemma:ADeltah`, proofs:3948–3959 | **Lemma N.2**, text:6306–6324; same full-history conditioning, coefficient assertions, and Gaussianity sentence |
| `lemma:removeVanishing`, proofs:3960–3968 | **Lemma N.3**, text:6325–6333; same estimate and one-line Hölder proof |
| `thm:controlHighMoments`, proofs:901–931 | **Theorem K.23**, text:3937–3958; same $n^{-3/2}$ and averaged-higher-moment bounds |
| `prop:pseudoinverseLambda` and subsequent coefficients, proofs:1849–1912 | **L.5–L.7**, text:4646–4693; same rank premise, pseudoinverse passage, and misplaced $1/n$ in the variance calculation |
| `lemma:YgConditionalDistribution`, proofs:2955–3023 | **L.19** proof, text:5400–5446; same output/input and variance/standard-deviation error |

Thus the inspected source corresponds substantively to the readable v3 text, including the disputed proof and distinctive errors. This is **not** a claim of byte equivalence between TeX and text, a fresh compilation/PDF identity check, or an exhaustive comparison of every application section. There is no evidence here of a later corrected Appendix N concealed in the TeX.

## Mathematical findings

### 1. The three scopes remain different

The parameterless theorem, [NetsorT2.tex:186](/tmp/tp3-audit.Trwr6N/NetsorT2.tex:186), fixes the program and its coordinate functions as width grows and permits polynomially bounded functions/tests. Appendix L derives rank stability by simultaneous induction; it does not simply assume it. The scalar-program E.5/E.11 statements explicitly assume rank stability, at advancedNetsorT:75 and 146. Their proof is Appendix M.

By contrast, E.15 at advancedNetsorT:215–227 and its proof at proofs:3869 onward expressly remove that assumption while requiring pseudo-Lipschitz tests. The alternative Assumption E.6, advancedNetsorT:88–95, requires joint pseudo-Lipschitz regularity when vector and parameter arguments occur, and allows continuous scalar-only Moment functions. It is not a hidden rank assumption. Nor does the Appendix-N convention that nonlinearities take G-vars eliminate scalar feedback; its own line 3921 explicitly permits scalars generated from both core and vanishing vectors.

The source's discontinuous-test example at advancedNetsorT:181–195 demonstrates why rank matters for the **less regular** statement. Its test is discontinuous on the vanishing-coordinate hyperplane and therefore is not an E.15-admissible pseudo-Lipschitz test. Treating it as a counterexample to E.15 would be a scope error.

### 2. The earlier rank proof cannot be silently imported into Appendix N

Appendix L introduces `Moments` and `CoreSet` at proofs:1183–1215, including `Basis`, `Density`, and `NullAvoid`. For fixed coordinate functions, the zero-stability proof, 2483–2517, uses the limiting density and avoidance of its null sets to turn a limiting zero into eventual exact zero. The rank proof, 2405–2453, applies this to a finite basis of the limiting Gram kernel. It then obtains eventual equality of kernels/ranks, which justifies pseudoinverse convergence at **1849–1854** and coefficient convergence at **1895–1912**.

Appendix N deliberately allows vectors that are nonzero at finite width but vanish only in the limit. Its `Orthogonal` invariant, **3905–3906**, controls the **core input families** $\mathcal M_A^*$. It does not establish rank stability for the enlarged family of core and vanishing inputs used in **3954–3958**. Invoking L.5 or the L.7 coefficient limits for that enlarged family without checking their rank premise would be a wrong invocation. Assuming that premise throughout would return to the narrower E.11/Appendix-M branch, not prove E.15 as stated.

### 3. Precise missing conditional-mean estimate

Even granting the usual sequential Gaussian-conditioning identity, the fully displayed finite-width formula earlier in the source is, for histories $X=AY$, $U=A^\top V$, and query $q$,

\[
Aq\mid\mathcal F\ \overset d=\ Xd+Ve+sP_V^\perp z,
\quad z\sim N(0,I_n),
\]
\[
\Upsilon=Y^\top Y/n,\quad \Lambda=V^\top V/n,\quad
\Gamma=U^\top Y/n,\quad \gamma=Y^\top q/n,\quad \delta=U^\top q/n,
\]
\[
d=\Upsilon^+\gamma,\qquad e=\Lambda^+(\delta-\Gamma\Upsilon^+\gamma),
\qquad s^2=\sigma_A^2\|P_Y^\perp q\|_2^2/n.
\]

See proofs:1736–1803 and 1886–1905; this uses the corrected normalization of the variance. For $q=\Delta h$, the enlarged histories may contain disappearing directions. Empirical moment convergence of their entries does not alone control either pseudoinverse or the resulting conditional mean in every empirical $L^p$ norm.

**Line 3958 asserts the needed convergence of coefficients; it does not derive it.** It refers to the limiting hatted/dotted decomposition and asserts zero limiting coefficients on bounded core columns and finite limiting coefficients on vanishing columns. There is no finite-width regression calculation, rank-uniform bound, rate comparison, or independent lemma at that point that proves those assertions. The $C^+b$ convention in NetsorT2:222–231 defines limiting response coefficients; it does not prove convergence of finite-width coefficients across rank loss. In a singular representation, coefficient vectors also need not equal every formal derivative vector componentwise: only the contracted correction is invariant.

For clarity, an elementary regression diagnostic is $K_n=\varepsilon_n^2$, $b_n=\varepsilon_n^{3/2}$, with $\varepsilon_n\downarrow0$. Both converge to zero, but $K_n^+b_n=\varepsilon_n^{-1/2}$ diverges. These can be the Gram and cross moment of a column $\varepsilon_n w_n$ and query $\sqrt{\varepsilon_n}w_n$, with $n^{-1}\|w_n\|_2^2=1$. The query's second moment tends to zero while the coefficient diverges; the contracted vector nevertheless tends to zero in that norm. **This is a diagnostic of the invalid inference, not a constructed admissible TP trajectory or a counterexample to Lemma N.2/E.15.** A valid repair may control contracted vectors directly and need not establish boundedness of every nonunique coefficient.

### 4. High-moment estimates really are present, but do not fill this gap

K.23 at proofs:901–931, proved at 954–1146, supplies high-moment bounds for centered averages of functions of weakly correlated Gaussians. For a conditional centered average $Q_n$, its second form gives

\[
\mathbb E_z|Q_n|^{2p}
\le C n^{-3/2+1/L}
\left(\frac1n\sum_\alpha\mathbb E_z|\phi_\alpha(z_\alpha)-\mu_\alpha|^{2pL}\right)^{1/L},
\quad p\ge6.
\]

The constant is independent of the functions and width once the correlation bound is fixed. The projection-correlation argument and its simpler alternative are fully present at 562–810. In the ordinary induction, proofs:3026–3281 explicitly handle random conditional functions, bound their averaged higher moments, and obtain a summable conditional bound (3051–3074). The uniform empirical bounds for **every fixed polynomial power of $\omega$** at 3185–3281 are particularly relevant: their proof uses the already established convergent coefficients in L.7. It would be circular to use them as the missing rank-changing coefficient estimate.

These Gaussian-image estimates can control an already justified residual $s_nP_nz_n$ with $s_n\to0$ and the stated projection/moment conditions. They do not themselves establish high empirical moment bounds for the **conditional mean** $Xd+Ve$ in the degenerate-history setting. Thus acknowledging the substantial earlier estimates does not close N.2.

Also distinguish empirical almost-sure bounds from unconditional integrability. The constants at proofs:3054 and 3072 can depend on the realized history; they are not a general uniform-integrability theorem. `extraTheorems.tex` 79–85 explicitly leaves general polynomial-test mean convergence as a conjecture. Its bounded/quadratic-test results and rank-qualified scalar extensions are not an alternate proof of the missing N.2 estimate.

The operator-norm observation at proofs:3952 supplies only

\[
\frac1n\|A\Delta h\|_2^2
\le \|A\|_{\rm op}^2\frac1n\|\Delta h\|_2^2\longrightarrow0.
\]

The norm bound itself has an elementary independent justification in the stated iid Gaussian setup: take a $1/4$-net of the unit sphere of size at most $9^n$, obtained by disjoint-radius-$1/8$ ball packing. Approximating both unit vectors in $u^\top Av$ gives $\|A\|_{\rm op}\le2\max_{u,v\text{ in net}}|u^\top Av|$. Each fixed bilinear form is $N(0,\sigma_A^2/n)$, so

\[
\Pr(\|A\|_{\rm op}>2t)
\le2\,9^{2n}\exp[-nt^2/(2\sigma_A^2)].
\]

For fixed sufficiently large $t$ this is summable in $n$; Borel–Cantelli gives the required eventual almost-sure bound. No independence across widths is needed. This verifies the limited second-moment step without relying on an unread matrix-concentration proof. It supplies no dimension-free empirical $L^{2k}$-operator bound for a general dependent query. For example, normalized second moment tending to zero does not imply normalized fourth moment tending to zero: $n^{1/4}e_1$ has these quantities $n^{-1/2}$ and 1. This is only a norm-implication example, not an output asserted to arise from an admissible TP.

### 5. Algebraic repair in N.3 does not repair Lemma N.2

At proofs:3926 the source correctly sets $\widehat h^0=h^0-\Pi h^0$. But at **3932** it sets $h^1=h^0/(\|\widehat h^0\|_2^2/n)$, then uses an expansion that adds $\Pi h^0$ again. With that definition the alleged expansion equals $h^0+\Pi h^0+\Delta h$, rather than $h^0+\Delta h$. Nor does that $h^1$ generally have norm $\sqrt n$ or lie orthogonal to the old core input space.

On the nonzero-limit branch the intended local repair is

\[
s_n=(\|\widehat h^0\|_2^2/n)^{1/2},\qquad
h^1=\widehat h^0/s_n,\qquad h^0=s_nh^1+\Pi h^0.
\]

Then $\|h^1\|_2=\sqrt n$ and $h^1\perp\mathcal M_A^*$. The assumed positive limiting squared norm ensures the division is valid eventually almost surely. A complete rewritten-program proof must still specify harmless definitions off that eventual branch and preserve its regularity conditions. These corrections are **audit repairs**, not hidden corrections found in the TeX. They do not establish the degenerate conditional-mean bound.

### 6. Scalar dependence and the elementary perturbation lemma

At **3921–3924**, $h^0=\phi(z,0;\theta_n)$ retains scalars $\theta_n$ computed from both $z$ and $\bar z$. Therefore the claim at **3930**, repeated in the argument at **3944**, that it suffices to condition only on the core vectors needs an additional measurability or replacement argument. Conditioning additionally on such scalars cannot simply be assumed to preserve the same Gaussian conditional law. Freezing scalar limits could be part of a repair, but one must then prove that the matrix image of the resulting error is negligible; that does not bypass the all-moment difficulty by itself.

Lemma N.3 at **3960–3968** is different: its terse Hölder proof can be filled without the missing matrix lemma. Put $x_\alpha=(z_\alpha,\bar z_\alpha,\theta_n)$, $y_\alpha=(z_\alpha,0,\theta_*)$. Pseudo-Lipschitzness gives

\[
|\psi(x_\alpha)-\psi(y_\alpha)|^t
\le C D_\alpha^t B_\alpha^t,
\quad D_\alpha=\|\bar z_\alpha\|+\|\theta_n-\theta_*\|,
\]

where $B_\alpha$ is a fixed polynomial-growth bound in the displayed inputs. Cauchy–Schwarz on the normalized coordinate sum bounds the average by

\[
C\left(\frac1n\sum_\alpha D_\alpha^{2t}\right)^{1/2}
\left(\frac1n\sum_\alpha B_\alpha^{2t}\right)^{1/2}\longrightarrow0.
\]

The first factor vanishes and the second stays bounded by the assumed empirical even moments and scalar convergence; noninteger powers are controlled by sufficiently high even moments via the power-mean inequality on the normalized coordinate measure. This proves the displayed perturbation estimate. It proves that $\Delta h$ is small **before** multiplying by the reused matrix, not that $A\Delta h$ has all vanishing empirical moments.

## Source-algebra checks against the prior six correction groups

All six errors listed in PRIMARY_LITERATURE §4.2 are still present in this exact TeX. The initial source pass identified the relevant formulas; comparison supplied the existing grouping.

| Location in this exact TeX | Check and consequence |
|---|---|
| proofs:231–289, K.9 | The undefined $Y$ appears in the conditional mean/proof; a $Q^\top$ appears where $Q^+$ is needed in the multiplier formula. The corrected mean is $ZQ^++P^{+\top}X^\top-P^{+\top}P^\top ZQ^+$. |
| proofs:1039–1144, K.23 | The single-collision contribution has exponent $2p-1-(p-1)/4=(7p-3)/4$, not $7(p-1)/4$. After division by $n^{2p}$ it is $n^{-(p+3)/4}$, still at most order $n^{-3/2}$ for the selected $p\ge6$. This algebra correction does not remove the usable moment bound. |
| proofs:1577–1635, L.3 case 2 | The conditioned source vector must be hatted Gaussian $U=(\hat Z^{u^j})_j$; correction columns after the adjunction substitution are full $Z^{v^j}$, not hatted columns. Use the contracted regression identity in the singular case. |
| proofs:1864–1869, L.6 | Correct finite variance: $\sigma_A^2[(h^\top h)/n-\gamma^\top\Upsilon^+\gamma]$. |
| proofs:3017–3021, L.19 | Correct limiting conditional variance: $\sigma_A^2[\mathbb E(Z^h)^2-\mathring\gamma^\top\mathring\Upsilon^+\mathring\gamma]=\mathring\sigma^2$. The printed $Z^g$ and $\mathring\sigma$ are not the required input variable and variance. |
| proofs:3660–3669, L.23 | The upper bound is $\max(\sigma^2,\mathring\sigma^2)^p$, with limit $\mathring\sigma^{2p}$, not exponent $p/2$. Boundedness, the conclusion used there, survives. |

This is not a claim that the six groups exhaust every typographical or technical issue in the paper. In particular, ancillary statements should not be imported with stronger scopes than were checked. The pseudo-Lipschitz composition-degree claim at advancedNetsorT:66 also still says $d_1+d_2$; the class is closed under composition, but the numerical degree generally needs enlargement, as already noted in PRIMARY_LITERATURE:149.

## Deeper-import boundary and recommendation

The required **local** definitions, statements, proof sections, and proof-level dependencies for this decision were personally read to the ranges above. The exact statement and proof of the disputed lemma are now accessible. The remaining failure is **missing justification inside an available proof**, not missing access to that proof.

The fresh read is not a complete recursive certification of every TP-III theorem. Original external proofs in Bayati–Montanari, O'Donnell, Tao, TP-I, and TP-II were not read here; bibliographic entries are not proofs. The relevant Gaussian-conditioning lemmas and Gaussian-image moment proof are present locally and were read; the limited Gaussian operator-norm implication and the elementary perturbation step were checked explicitly above. A full certification of every auxiliary Hermite/conditioning/convergence assertion would still require checking its own exact hypotheses and any remaining imported facts. Neither the mean-convergence appendix nor the Operator1 downstream manuscripts were certified by this task.

The **load-bearing unclosed dependency** remains a proof, valid under E.15's actual hypotheses, of all empirical moments vanishing for the relevant $A\Delta h$, including the conditional mean after histories with disappearing directions and scalar dependence are accounted for. An alternate applicable proof could establish the contracted estimates directly. It was not found in this exact artifact or the required local dependencies; the source's assertion of coefficient convergence cannot count as that missing proof.

Recommended master disposition:

1. **Supersede only the access status** in OPERATOR1:199/220 for this exact hash. Its earlier EACCES observation remains a truthful historical observation; this audit records the later full read, including EOF. Do not rewrite it as though the previous auditor had access.
2. **Retain PRIMARY_LITERATURE §4.2's Appendix-N qualification.** Add this report as independent TeX-level corroboration. No newly found qualification narrows E.15 to rank-stable programs, and no newly found estimate closes Lemma N.2.
3. **Keep scope distinctions explicit:** incorrect invocation of a rank-qualified theorem; algebra errors with identified local repairs; a printed but unproved rank-changing coefficient/all-moment step; and an actual counterexample are different findings. Only the first three are relevant to the present certification boundary. No actual E.15/G.4 counterexample was established here.
4. **Keep the parameterless specialization separate.** Appendix L has its own rank/zero-stability mechanism, so the Appendix-N gap is not a refutation of the fixed parameterless import described in OPERATOR1. Conversely, this focused read does not by itself certify all downstream L2/L3 claims or turn those source-algebra repairs into a complete external-theorem certification.
5. **Do not enlarge time or convergence-mode claims.** Fixed-program statements and history-dependent empirical moment bounds do not supply growing-step, uniform-time, or arbitrary mean-convergence conclusions. The other residual artifact in OPERATOR1:221 is outside this audit and remains untouched.

**Handoff status:** exact TeX access/full-read obligation closed; substantive Appendix-N import-proof obligation retained; master not edited.
