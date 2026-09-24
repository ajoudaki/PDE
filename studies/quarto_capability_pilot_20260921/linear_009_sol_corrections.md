# Packet 009 Sol preservation audit: bounded corrections

Verdict: **FAIL; correction required.** The frozen hashes match, exact replay and native-TeX projection checks hold, and the 30 focused checker tests pass. The unchanged checker, invoked with repository root `/home/amir/Codes/PDE`, correctly fails on remaining references. No rendering was attempted.

## 1. Automatic-reference omissions

Replace every occurrence below with an automatic reference while preserving nouns, qualifiers, punctuation, ranges, and link captions. Add the listed future targets to `linear_009_targets.json` where absent.

- `sec-docs-global-nonlinear-l1842` (A.1): source lines 2458, 2629, 3977, 4285, 4687, 5579.
- `sec-docs-global-nonlinear-l1854` (A.2): 2458, 2629, 3439, 3977, 4289.
- `sec-docs-global-nonlinear-l1864` (A.3): 5482, 6157.
- `sec-docs-global-nonlinear-l1903` (B.1): 5534, 5575, 5681, 5989, 6163.
- `sec-docs-global-nonlinear-l2462` (C.1): 2456, 2460, 3820.
- `sec-docs-global-nonlinear-l2924` (C.2): 2669, 3978, 4387, 4392, 4411, 4414, 4736.
- `sec-docs-global-nonlinear-l3441` (C.3): 2456 and every occurrence at 3820, 3825.
- `sec-docs-global-nonlinear-l3836` (C.4): 5272, 5428.
- `sec-docs-global-nonlinear-l3982` (C.4.1): range starts at 3838, 3852; named occurrence 5613.
- `sec-docs-global-nonlinear-l4949` (C.4.4): range ends at 3838, 3842, 3852.
- `sec-docs-global-nonlinear-l5270` (C.4.5): 3843.
- reserve `sec-docs-global-nonlinear-l6596` (C.4.5.3): 5357, 5374, 5390, 5419, 5432.
- existing reservations `sec-docs-global-nonlinear-l6904`, `-l8978`, `-l17554`: C.4.6 at 3850; C.4.7 at 3846 and 5272; C.4.9 at 3851. Convert the three old fragment-only Markdown links at 3846, 3851, 5272 to `global-nonlinear.qmd#<stable-id>` with captions unchanged.
- Local “Section 2” means `sec-docs-global-nonlinear-l4230` at 4217, 4384, 4625. Local “Section 3” means `sec-docs-global-nonlinear-l4307` at 4227, 4459, 4513.
- Add exact section targets in `docs/special_data_limits.md`: III.F.1 `sec-docs-special-data-limits-l3789`, F.4 `-l3946`, F.5 `-l4009`, F.7 `-l4072`, F.9 `-l4169`, F.10 `-l4201`. Use them at 3977 (F.1–9), 4232, 4241, 4242, 4246, 4249, 4687 (F.1–7), and 6255 (F.1–5), preserving range punctuation.

Convert all local numeric equation references in the following exact groups:

- C.2: `eq-...-l2958` at 3145,3218,3279; `l2970` at 3144,3294,3378,3394,3422; `l2976` at 3144,3145,3216,3378; `l2984` at 3422; `l3013` at 3439; `l3044` at 3146,3229,3296,3395; `l3049` at 3146,3206,3279,3289,3376; `l3064` at 3439; `l3103` at 3249,3307,3403; `l3119` and `l3125` at 3384; `l3135` at 3230; `l3148` at 3177,3360; `l3158` at 3180,3374; `l3163` at 3177,3360; `l3171` at 3340; `l3221` at 3249,3374; `l3251` at 3262,3340,3349,3374,3381; `l3281` at 3294; `l3300` at 3404; `l3310` at 3331,3349,3353,3364; `l3388` at 3406.
- C.3: `l3488` at 3703; `l3538` at 3543; `l3573` at 3813; `l3588` at 3598; `l3631` at 3675.
- C.4.4: `l4959` at 5181; `l5036` at 5043,5063; `l5048` at 5062,5070,5086,5135; `l5107` at 5135,5154; `l5126` at 5135,5154; `l5160` at 5167; `l5203` at 5219,5221; `l5210` at 5250; `l5228` at 5262; `l5239` at 5245,5250.
- C.4.5 statement: `l5317` at 5345,5412,5433; `l5340` at 5426,5433; `l5376` and `l5394` at 5404. At 5374 reserve and reference the complete future tagged display `eq-docs-global-nonlinear-l6880`, span 6880–6883, for equation (15).

Do **not** turn checker lookalikes into equation references: source 2921 `O(1)`, 3839–3840 `W^(2)`, `W^(3)`, 4847 `1/(4m)`, and 4863 `rho(0)` are mathematical notation and require inline transcription.

## 2. Incorrect declared transcriptions

Replace the affected `inline-transcription` entries and replay the candidate:

- 4054: `Lip(phi')<=2` → `$\operatorname{Lip}(\phi')\le2$` (remove nested `\operatorname`).
- 4072–4075: every `T_ball` → `T_{\mathrm{ball}}`.
- 4718: `F_nu(barTheta_n,k)` → `$F_\nu(\bar\Theta_{n,k})$`; typeset adjacent `o_P(1)` as `$o_{\mathbb P}(1)$`.
- 4845: `(diam Z)/2 sum_j |p_hat_j-p_j|` → `$(\operatorname{diam}\mathcal Z/2)\sum_j|\widehat p_j-p_j|$` (retain the source's observation-space symbol consistently).
- 5083: preserve multiplication: `$W(t)H_a(t)-W_0h_a$`, not `W_{0h}`.
- 5123: `$p\sum_a\mathbb E[SE_a]$`; the second standalone source `E_a` is `$E_a$`, not `\mathbb E_a`.
- 5526: `$\langle q\otimes v,B\rangle_{\mathrm{HS}}=\langle q,Bv\rangle_2$`.
- 5548: use `\bar Z^2`, `\bar c` throughout: `$\|\phi'(Z^2)c-\phi'(\bar Z^2)\bar c\|_2\le\|c-\bar c\|_2+2\|\bar c\|_\infty\|Z^2-\bar Z^2\|_2$`.
- 5594: retain the atom tuples: `$\nu_*=\tfrac12\delta_{(e_1,+1)}+\tfrac12\delta_{(e_2,-1)}$`.
- 5660: `o_L2(s)` → `$o_{L^2}(s)$`.
- 5670–5722: every symbolic `*_dagger` uses subscript `\dagger` (`s_\dagger,w_\dagger,A_\dagger,c_\dagger`), not letters `dagger`.
- 5929 and 6262: `|phi''|<=2` → `$|\phi''|\le2$` (current `\phi^{\prime}'` is not the source notation).
- 5972 and all later raw occurrences: `t_act` → `t_{\mathrm{act}}`.
- 6015–6017: retain function arguments: `\arctan(1/5)`, `\arctan(1/239)`, and `\tan(4\arctan(1/5))`; braces alone discarded the source parentheses.
- 6139 and 6159: `s_infty` → `$s_\infty$`.
- 6249: retain `\sinh(2z)`.

## 3. Omitted mathematical typesetting

The candidate still contains unmarked ASCII/Unicode mathematics. Add bounded inline transcriptions for every residual notation span on these frozen source lines (combine adjacent tokens into one expression where that preserves the paragraph). This list excludes prose uses of words such as “tanh” and includes all detected symbolic residue:

```text
2460, 2468, 2476–2477, 2521, 2550–2551, 2558, 2576–2578, 2599,
2642, 2683, 2720–2721, 2731, 2733, 2739, 2742–2749, 2754, 2792,
2799, 2819, 2826, 2870, 2875, 2884, 2909, 2916, 2921,
3839–3840, 3850–3851, 3856, 3864, 3876, 3879, 3883, 3889–3892,
3907–3908, 3930–3931, 3939–3941, 3955, 3959–3960,
4218, 4226, 4309, 4636, 4648, 4656–4657, 4687, 4704, 4707,
4715, 4718–4719, 4721, 4731, 4735, 4740–4742, 4750–4754, 4772–4773,
4808–4811, 4818, 4828, 4834, 4839, 4842–4848, 4854, 4863–4867,
4875–4877, 4881, 4884, 4919, 4929,
5272, 5276, 5283, 5288–5289, 5298, 5302–5303, 5309–5310,
5313–5316, 5325, 5330, 5344–5348, 5362–5363, 5372–5374,
5381, 5398–5400, 5403–5404, 5410, 5417–5420, 5426, 5433–5435,
5442, 5448, 5545, 5551, 5762, 5928, 5945, 6101, 6152
```

Representative mandatory spans include `1/n`; `L`/`n`/`m`; `W^(L+1)`; `T_*>0`; `<=S0`; `Delta omega_b`; the full two-line tensor inequality at 2720–2721; `C(Delta+Delta')`; `R->infinity`; `C exp(-cR^2)`; `O(1)`; `T=40`; `t=tau/epsilon`; `q=0`, `q>1`; `T_*`, `D_n`, `o_P(1)`; `1/(4m)`; `m>=1`, `m>=L_Z`, `q=0`; `Z=sqrt(2)S¹ x {-1,+1}` and its cost; `f_*^infinity`; the complete `s_dagger` clock condition; all raw exponential/numerical inequalities at 5362–5374; `RMS<=2`; and the three inequalities in 6101.

Re-run the checker and add a focused regression that distinguishes real references from math lookalikes (`O(1)`, `1/(4m)`, `rho(0)`) once those expressions are inside math. Do not alter untouched checker behavior or native TeX payloads.

## 4. Surgical review of the first corrected bundle

The first corrected frozen bundle resolves the accepted mappings and transcription defects above, including the C.4.6/C.4.8 source distinction. Its 31 focused checker tests pass. The following bounded residuals still require correction; all other inspected additions are accepted.

- Make the range endpoints automatic references: source 3977, `III.F.1–9`, endpoint `9` to `@sec-docs-special-data-limits-l4169`; source 4687, `III.F.1–7`, endpoint `7` to `@sec-docs-special-data-limits-l4072`; source 6255, `III.F.1–5`, endpoint `5` to `@sec-docs-special-data-limits-l4009`. Preserve the en dash and surrounding prose.
- Typeset the remaining source notation at 2578 (`ell`), 2599 (`L2`), 2680 (`A^(ell)`), 2744–2746 (`P_j-P`, `[phi'(Z_j)-phi'(Z)]P`, `phi'`), 2870 (`n`), 3075 (`sigma`), 3825 (`S,U,B,T,M,A and R`, `y_b`, `p_b`), 3834 (`p_a`, both order-in-`t` phrases, `p`, `y`), 3891 (both `L²`), 4752 (`lambda_k`), 4828 (`u`), 4839 (`m`, `mu`), 4840 (`mu`), 4877 (`C`), 4884 (the second `S` and `i`), 5309 (`P`), 5436 (`mu`), and 5781 (`epsilon`).
- At source 3856, replace the added `$R^2$` by `$\mathbb R^2$`; the source's Unicode `R²` denotes Euclidean space in this context.
- The exhaustive residual scan also finds plain symbolic spans at source 2790, 2806, 2856, 2859, and 4746 (`Delta`); 3851 and 5781 (`epsilon`); 3920, 4831, 4883, and the already listed 4839, 4840, 5436 (`mu`); and 4829 plus the already listed 4752 (`lambda_k`). Typeset each symbol in place.
- At source 4828, repair the first corrected bundle's accidental `$L$ipschitz`: restore the prose word `Lipschitz`, then typeset the actual symbols as `constant $L$ in $u$`. At source 4881, also typeset the mathematical `z` in “uniformly in z and time.”
- At source 2870, repair the analogous accidental `reco$n$struction`: restore `reconstruction` and typeset the intended final occurrence as `uniformly in $n$`.
- The completed bounded residual scan also requires the explanatory `s` at source 2491, `t` at 2730, `c` at 4737, `u` at 4776, both occurrences of `k` at 4812–4813, and deterministic `t` at 4888 and 4904 to be typeset in place.
- Surgical review of the late delta accepts every other addition, but source 2745–2746 was added as direct `\phi\prime`. Use the derivative notation `$[\phi'(Z_j)-\phi'(Z)]P$` and `$\phi'$` (or the equivalent explicit superscript `\phi^{\prime}`) so the prime is attached as a superscript.
