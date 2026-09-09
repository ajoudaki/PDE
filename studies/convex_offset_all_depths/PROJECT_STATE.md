# Active convex-mixture question

Literal convex activation with one fixed mixing coefficient at all
finite depths is the current target. The gain-based theorem does
not settle it, and rescaling that activation changes the raw dynamics.

REPORT.md currently proves an initialized conditioning obstruction
for normalized bounded C2 shapes and \(0<\varepsilon<1/2\).
The explicit choice \(\varepsilon=1/4\), \(\psi=\arctan/4\)
has contraction factor \(13/16\).

Full global trained convergence for one depth-independent positive
coefficient remains unproved and unrefuted by this obstruction.
Independent proof-search and review are pending. No claim of global
resolution should be inferred from validation of REPORT.md.

First isolated reviewer Ash validated the conditioning proof but required the raw metric and initialized kernel derivation to make the report self-contained. Those are now reproduced explicitly, including the actual finite Gaussian readout limit. A fresh isolated reviewer receives only the complete resulting 291-line report, SHA256 a6dae64cd54b9ab34520d2b493b78cefbbd4c868b5c222552e169982aff9f668.

Final isolated reviewers Brook and Garnet both PASS the exact report with no objections. Full reports and hashes are preserved in reviews/final; REVIEW_SUMMARY.md states their scope. The intended full global convex trained theorem remains UNRESOLVED. A bounded constructive investigation obtained a local route but did not close global source continuation, trained coercivity or persistent nonaffinity. No counterexample to qualitative fixed-depth global convergence was found.
