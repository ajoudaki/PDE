# Version and rebuttal log

## Version 0

- Candidate TeX: `CANDIDATE_V0.tex`
  - SHA-256: `daa583a94be0c32103761d3391bde7292e5d2c5d3fe6b2ea5f1530a411a36f21`
- Candidate PDF: `CANDIDATE_V0.pdf`
  - SHA-256: `f49ede7be2a271333c9ccf43e408b465b7081d3792ef966e0c6fb1e4509d935c`
- Bibliography: `REFERENCES_V0.bib`
  - SHA-256: `da2733eac725f263c325be153a1acc3354f1d1fc8165a1f435c086da7e8c1421`
- Reviewer assignment: `NEUTRAL_ASSIGNMENT.md`
- Evidence inventory: `LITERATURE_PACKET.md`
- Review output: `REVIEW_R0.md`
  - SHA-256: `7535a9a5718aef8bdf7a8f022405359fdac9238493492a3415e1aae456ce164d`
  - Recommendation: major revision; no fatal defect found in either compact-horizon theorem
  - Principal correction: Variant B adds a shared evolving Gram state of
    `P(P+1)/2` independent entries, so complete moving-state scaling at target
    error `epsilon` is `O(Hmn epsilon^{-1/2} + epsilon^{-1})`.
- Author response: `AUTHOR_RESPONSE_R0.md`
  - SHA-256: `7cda134ef70b083f62f3bf667d7708cc351d18b1c03fa028da93e5f2d650f576`
- Superseding candidate: `CANDIDATE_V1.tex` / `CANDIDATE_V1.pdf`
  - TeX SHA-256: `83cc0dcdbe9b2a1c1db3d894e34110b98605dfc889e258755a9b5c455fe11755`
  - PDF SHA-256: `2bec8ec7baf9e6207e1f494e910da98aa88232c740c3bade109a7dda201b7af2`
- Bibliography: `REFERENCES_V1.bib`
  - SHA-256: `5a650c1456b0b4eefb5126045f23b3ef50045671ab40c88e4ba319bf8ad7dbe9`
- Source diff: `DIFF_V0_V1.patch`
  - SHA-256: `47da802a4f679bb14e0c3b6d6f0cf250e67f96ee8d760820652728079a6370ac`
- Build: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
  completed with no LaTeX or package warnings.

The earlier verdict-oriented agents were interrupted before producing files and are
not inputs to this loop.

### Evidence-packet amendment after Round 0

- `LITERATURE_PACKET.md` SHA-256:
  `f0f23071600b71c7d93ef663bdbbecbcd0158dd97ff88839fd1eba8e4f67f2d7`
- Corrected the identities of arXiv:1902.06720 and arXiv:1805.01053.
- Added already completed shallow-circle and factor-control reports, protocols,
  independent checks, and machine-readable metrics under
  `data/generated/response_memory_significance_20260926/existing_experiments/`.
- No new training was run.
