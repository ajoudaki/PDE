# Final-edition comparison

Date: 2026-09-16. Scope: direct comparison only; no new scientific audit
or promotion review.

**Verdict: the final edition preserves the audited mathematical content
and every constant.** A direct unified diff of the complete files shows
only the title/status/provenance edits and the four presentation
corrections identified in `audit_extension.md`:

1. Define `nu_+` consistently instead of the isolated `u_+` typo.
2. Restrict the positivity sentence to the entries of `m_0` and `a_0`.
3. Define the lower active block without overloading the upper envelope
   symbol `B_2`.
4. State that all canonical feature equations remain active, rather than
   imply that every symmetry-constrained coordinate must move; the
   neighboring label wording retains the existing fixed-`A>0` scope.

All estimates, constants, hypotheses, proof arguments, physical-time
factors, topology claims, and scope exclusions are unchanged. The one
equation-text change corrects the previously identified input-variable
name and does not alter the input vector. The status sentence at the end
now calls the internally checked result a theorem; the new opening
explicitly retains its status as study material rather than established
library material.

| File | SHA256 |
|---|---|
| `route_extension.md` | `2764f92f5ca13308d0e4d8f41b7ac5afc7ee9f7cc86ec1dcd05447c60881a4df` |
| `proof.md` | `8cb77d4a1a1f879fa75780efc521f39c63c56feafec4a6c32f15e97ca1621dd0` |
| Original `audit_extension.md`, unchanged | `507192fca11cf2df583c5470747099ad11cd26883f1a5948ae081d22e55fe11d` |

The original audit report was not modified. I did not read the synthesis,
other route files, or other check files. The added provenance reference to
another check is observed as an editorial change, not independently
verified here. No substantive change requiring a new mathematical audit
was found; the original internal PASS applies to this final edition with
the four noted presentation corrections resolved.
