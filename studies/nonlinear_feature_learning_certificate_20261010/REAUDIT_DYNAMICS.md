# Interrupted dynamics reaudit: exposure and partial checks

Date: 2026-10-10. Status: **No independent verdict. Review stopped at the supervisor's instruction.**

The assigned scientific inputs were the following four frozen files. The initial SHA-256 hashes were:

| Input | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21` |
| `paper/feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `paper/compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |

I read the required `solve-math-rigorously` and `explain-with-canonical-notation` skills and the latter's neural-network reference. The intended scope was the probability quantifiers, real-time bounds, adjoint telescoping, cubic tangent-kernel discrepancy, first-layer nonlinear projection, and compression transfer. Compression approximation bounds were supplied dependencies, not review targets.

## Isolation failure

After initial source reading and an initial derivation of the cubic coefficient, I called `collaboration.list_agents` solely to check whether a delegation slot was available. The response included completed agents' verdict summaries and substantive prior-review conclusions. This exposed material outside the permitted inputs. I did not open their reports, retrieve study history, or modify the paper. I immediately disclosed the exposure to the supervisor. The supervisor instructed me to stop and save this record so that a replacement isolated reviewer could perform the audit.

This record must not be used as an independent review or as evidence that the complete theorem has passed review. No full assessment of gaps, probability statements, initialization, or fitting is issued here.

## Partial calculation completed before exposure

The following normalization check had been derived and reported to the supervisor before the agent-list response. It is a conditional algebraic check, assuming the stated short-time remainders and initial acceleration formulas; it does not establish those assumptions.

Write (k=2/m), and define the hidden acceleration energy by

\[
E_n=\frac{\|\ddot W^{(1)}(0)\|_F^2}{n}
       +\sum_{\ell=2}^L\|\ddot W^{(\ell)}(0)\|_F^2.
\]

With the source's initial adjoints and its expansion
\(\Delta W=\tfrac12t^2\ddot W(0)+o_*(t^2)\), the adjoint pairing at the top layer has coefficient \(t^2 E_n/(2k^2)\). Consequently the readout-Gram contribution to
\(y^\top[K(t)-K(0)]y\) is \(t^2 E_n/k^2\): the cross term appears twice. The hidden-block kernel contribution has the same coefficient because \(\delta_a^{(\ell)}(t)=ktB_a^{(\ell)}+o_*(t)\) and the squared outer-product formulas for the accelerations contribute a factor \(k^4\). Thus the proposed total coefficient is

\[
y^\top[K(t)-K(0)]y
   =\frac{2t^2}{k^2}E_n+o_*(t^2).
\]

Integrating the difference equation with flow factor \(k\) gives

\[
y^\top(f_n(t)-f_{\mathrm{NTK},n}(t))
 =\frac{2}{3k}t^3E_n+o_*(t^3)
 =\frac m3t^3E_n+o_*(t^3).
\]

This supports the displayed normalization conditional on the analytic and probabilistic steps, but those steps require the replacement review. The read-through and targeted checks remained incomplete when stopped.
