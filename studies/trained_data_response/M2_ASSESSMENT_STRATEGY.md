# Independent strategic assessment after P2

Assessment date: 2026-09-11. Author: `/root/m2_strategy_fresh`.
This is a read-only scientific assessment with one assigned report write,
not a proof, experimental campaign, promotion review, or authorization to
change established material.

**Recommendation.** Make the next milestone a theorem of beneficial
out-of-training-support prediction caused by data-dependent hidden-feature
adaptation. It should give a strict test-risk improvement on a predefined
nonlinear teacher family, compared both with the unperturbed predictor and
with an explicitly matched readout control. Keep physical time 40 and the
actual two-hidden-layer Gaussian tanh model. The missing result is a signed,
mechanistically attributable prediction statement, not a longer existence
interval or another norm estimate.

The central signs proposed below are open. I cannot infer them from P2,
and I do not claim that the particular witness family below must succeed.
This is a strategically substantive, falsifiable target with a relatively
short logical bridge from the available tools, rather than a guaranteed
next theorem.

P2 constructs a strong raw population flow for a positive Wasserstein
neighborhood of the opposite-label reference, identifies actual finite GF,
and makes the already identified trained response approximate actual
nonlinear contaminations uniformly over their laws. These are substantial
advances. Nevertheless, uniqueness tells us which trajectory occurs only
through its full evolution. It does not explain why its passive predictions
are useful. The inherited risk bound concerns laws extremely close to two
atoms; it gives no useful-risk theorem for a broad circle teacher and no
causal benefit of feature motion. C.4.6.P30–P31 identify directions preserving
the two fitted predictions to first order, but explicitly do not determine
their passive evaluations or their usefulness.

Several other goals are scientifically attractive. A global correlated-law
flow or an endpoint-selection theorem would be deeper than a finite-time
result, but P2's reference-anchored source cap is not uniform in the new
horizon. Moreover, bounded homogeneous propagation permits a forced response
of order T, and the endpoint has neutral training-preserving directions.
These leave a nonlinear long-time problem, not simply a continuation
exercise. A statistical fluctuation theorem would quantify sampling
variability, but would still leave the selected predictor's bias unexplained
and needs a valid empirical-measure differentiability bridge. A variational
description of implicit bias might explain selection, but no such functional
or minimizer characterization follows from the raw gradient structure.
Extending raw-GD capture or improving the neighborhood, constants, or
remainder order would be useful infrastructure; none alone supplies the
missing prediction explanation. The proposed risk-selection milestone has
the best present balance of mechanism relevance and proximity to proved
tools. This ranking does not declare the alternatives impossible.

**A precise proposed theorem target.** Use P2 with Y=3, T=40, mobilities
(n,1,n), unhalved mean squared loss, no biases, and the independent centered
Gaussian stored variances (1,1/n,1/n²). All three parameter blocks train.
The initialized Gaussian middle action and its actual adjoint survive.
Use normalized inputs u=x/sqrt(2). Before inspecting any new learned
trajectory, fix the following teacher family:

\[
 \tau_\kappa(u)=(u_1-u_2)(1+\kappa u_1u_2),
 \qquad -1\le\kappa\le1,\quad \kappa\ne0.
\]

Its labels at e1,e2 are +1,-1, and its absolute value is at most
3 sqrt(2)/2<3. Its cubic component is not proportional to its linear
component on the circle. Let P exchange the coordinates. For an oblique
u=(a,b) with a,b>0, a²+b²=1, a≠b, put

\[
 \nu_{\kappa,u}
  =\tfrac12\delta_{(\sqrt2u,\tau_\kappa(u))}
   +\tfrac12\delta_{(\sqrt2Pu,\tau_\kappa(Pu))},
 \qquad
 \mu_{\epsilon,\kappa,u}=(1-\epsilon)\nu_*+\epsilon\nu_{\kappa,u}.
\]

The additional training inputs are correlated with each other and with the
reference inputs. The test input is uniform arc length on the entire
circle, with the same teacher labels. Define its risk by

\[
 \mathcal R_\kappa(g)=\frac1{2\pi}\int_0^{2\pi}
  [g(\sqrt2(\cos\alpha,\sin\alpha))-
       \tau_\kappa(\cos\alpha,\sin\alpha)]^2\,d\alpha.
\]

This is a specified covariate-shift transfer problem: almost every test
input lies outside the four-point training support. It is not an ordinary
iid train–test gap assertion. Its fixed teacher and test law exclude defining
the desired labels from the network's learned output or selecting a test
measure after observing where that output looks favorable.

The matched control is especially useful here. Let
\(h_*(t,u)=H_*^{(2)}(t,u)\) be the entire upper-feature trajectory of the
actual nonlinear reference training. Give this trajectory to a readout
trained on the changed law:

\[
 \dot{\bar c}_{\epsilon}(t)
 =-2\int[\langle\bar c_{\epsilon}(t),h_*(t,v)\rangle-y]
                    h_*(t,v)\,d\mu_{\epsilon,\kappa,u}(v,y),
 \quad \bar c_{\epsilon}(0)=0,
 \quad \bar f_{\epsilon}(t,\sqrt2v)
       =\langle\bar c_{\epsilon}(t),h_*(t,v)\rangle.
\]

Measures in this formula are pushed forward to normalized input v.
At epsilon=0 this is exactly the reference readout, so both algorithms
have the same baseline predictor at every time. The control receives all
reference feature learning; only its dependence on the new data is removed.
Its features are supplied by the separately specified reference dynamics,
not by the target changed-law trajectory. It is an explicit causal control,
not a proposed replacement or autonomous approximation for the nonlinear
learner. It is also not a claim about optimal fixed-kernel predictors or
every possible frozen-feature algorithm.

The proposed theorem would exhibit a rational nonzero kappa0 in (-1,1),
an explicit rational circle point u0 with positive unequal coordinates,
neighborhoods I of kappa0 and A of u0 within those constraints, and constants
c>0 and epsilon0>0, such that for every kappa in I, u in A, and
0<epsilon<=epsilon0,

\[
 \mathcal R_\kappa(f_{\mu_{\epsilon,\kappa,u}}(40))
 \le \mathcal R_\kappa(f_*(40))-c\epsilon,
 \tag{M2.1}
\]
\[
 \mathcal R_\kappa(f_{\mu_{\epsilon,\kappa,u}}(40))
 \le \mathcal R_\kappa(\bar f_{\epsilon}(40))-c\epsilon.
 \tag{M2.2}
\]

The constants and exhibited parameters must be certified from the model
and the fixed teacher family. They cannot assume either risk inequality,
an unspecified favorable response alignment, or a teacher chosen by copying
the trained prediction. The theorem must provide actual values of kappa0
and u0, rather than stop at a conditional response formula. Open I and A
would make the benefit robust to small teacher and geometry changes.
The existential witness is not an assertion that every nonlinear teacher
benefits, nor that a better predictor merely exists in the network class:
(M2.1)–(M2.2) concern the predictor selected by the specified GF.

Include a finite-network conclusion at each separately fixed positive
epsilon and each fixed pair (kappa,u): both inequalities, with c/2 in
place of c, hold with probability tending to one for the actual initialized
finite GF and the corresponding finite readout control as width tends to
infinity, using the actual finite reference GF for the baseline in (M2.1).
The same should hold for independent iid samples with m,n tending
to infinity without a relative growth condition. The finite control uses
the actual finite reference features and actual initial readout; it does
not reset that readout. Proving its approximation is an additional, bounded
linear-equation comparison obligation. P2 supplies capture for the nonlinear
learner. No simultaneous epsilon/width or epsilon/sample rate is part of
this target, and no GD or endpoint theorem is implicit.

**Why this is within reach of the new tools.** The target retains one fixed
substantial-training time. Its law directions belong to P2's allowed
contamination cone for every small positive epsilon, including arbitrarily
small atom masses. The new weighted coefficient transport, same-mesh law
comparison, passive tails, and radial inverse-gate moment bounds are what
construct those nonlinear trajectories and justify the uniform remainder.
P2 is therefore doing more than transferring robustness of one known curve.

There is a concrete bridge to the desired signs. Put
\(\sigma=\nu_{\kappa,u}-\nu_*\),
\(D=\mathscr D_\sigma f(40,\cdot)\), and let
\(\bar D=\partial_{\epsilon+}\bar f_{\epsilon}(40,\cdot)|_0\).
P2 gives \(f_\epsilon=f_*+\epsilon D+o(\epsilon)\) uniformly in input.
Writing the uniform remainder as r_epsilon and expanding the square gives

\[
 \mathcal R_\kappa(f_\epsilon)-\mathcal R_\kappa(f_*)
 =2\epsilon\int(f_* -\tau_\kappa)D\,d\rho+o(\epsilon),
 \tag{M2.3}
\]

where rho is uniform normalized circle measure. Indeed the extra terms
are \(2\int(f_*-\tau_\kappa)r_\epsilon\,d\rho\) and
\(\int(\epsilon D+r_\epsilon)^2\,d\rho\); bounded f*, teacher, and D
make these o(epsilon). In (M2.3)–(M2.4), predictors and their responses are
evaluated at sqrt(2)u when integrated against rho(du). The readout control has the analogous elementary
linear-ODE variation. Consequently it would suffice to certify strict
inequalities, uniformly on smaller I and A,

\[
 2\int(f_* -\tau_\kappa)D\,d\rho<-2c,
 \qquad
 2\int(f_* -\tau_\kappa)(\bar D-D)\,d\rho>2c.
 \tag{M2.4}
\]

This reduction explains feasibility; (M2.3) alone is not the milestone.
The open scientific content is the concrete signed witness (M2.4) and an
explanation of its data geometry. A proof could use a directly controlled
nonlinear comparison, a symmetry or harmonic analysis, an adjoint risk
calculation, or a certified representation of the trained response. No
particular one is presupposed.

The exact response supplied by C.4.6 is
\(D_\sigma f(T,x)=\ell(T,x)\int_0^T U(T,s)b_\sigma(s)\,ds\).
Both moving evaluation features and residual-curvature propagation enter.
The matched control removes the response of the hidden trajectory to sigma,
so a strict advantage in (M2.2) attributes a test-risk benefit to that
adaptation, including its effect on subsequent readout learning. It does
not prove separate necessity of each hidden block. The model's nonlazy
reference motion is already certified at time 1/200, not at time 40;
small-law continuity can preserve that early motion for this chosen family.
The proposed risk comparison supplies the missing causal link that a
displacement lower bound alone cannot provide.

**The genuinely open obstacles.** The response bounds give magnitude and
well-posedness, not sign. Positivity of the two-input training Gram does not
make cross-input transfer positive, and the trained propagator is not an
everywhere positive or self-adjoint test-risk operator. The endpoint
projection leaves passive values undetermined. Even proving D differs from
the readout response would be insufficient: its difference must align with
the predefined teacher residual on a test set of positive measure. The
existing enormous constants do not resolve such an alignment.

The second obstacle is attribution without giving a weak control an
artificial disadvantage. Matching the entire reference feature trajectory
and the baseline predictor removes a large source of ambiguity. It does not
prove superiority over an optimally tuned initial kernel, match every
post-contamination training statistic, or explain generalization universally.
Those claims must not be appended to this theorem. Conversely, replacing
the full target learner by its readout control would destroy the target.

The third obstacle is that the proposed low-degree teacher family may have
no beneficial signed witness at T=40. That possibility is substantive and
should be allowed to falsify this witness family. It would not falsify P2,
show that feature adaptation never helps, or rule out another independently
specified task. No witness search, parameter sweep, or new proof campaign
was undertaken in this assessment.

Finally, the statistical and long-time boundaries remain real. For a
nonatomic law, its empirical law is supported on a finite set of zero
population mass, so their total-variation mass distance is two almost surely.
P2's uniform contamination differentiability therefore supplies no
sample-size delta method. A CLT would need an appropriate weaker tangent
topology, derivative continuity and a stochastic remainder estimate (plus
the necessary empirical-process limit); these have not been provided.
Likewise, an all-time homogeneous propagator bound and a theorem through
time 40 do not give changed-law endpoints or selection on their neutral
manifold. The proposed theorem avoids relying on either missing bridge.

**Read scope and provenance.** The scientific inputs actually read were
exactly the following three frozen files, all in full. Truncated tool
displays were repaired with overlapping smaller reads; no scientific
complement in these three files remains unread.

| Frozen input | Complete read coverage | SHA-256 before and after reading |
|---|---|---|
| `P2_SECTION.md` | Lines 1–2461; complete C.4.7 statement and every proof subsection | `707a7d42eb2e2e58ae92fa2ee8e25343977224fe1307675e7c0c82609b0571f0` |
| `P2_PROMOTION_DEPENDENCIES.md` | Lines 1–7434; all listed complete proof units and the full included guide/notation | `a68aaa0107f4f73cd0df22af8a8f3867b1c76b515c5d0a920ef387ff2d32acd3` |
| `P2_PROMOTION_MANIFEST.json` | Lines 1–51; metadata, hashes and scope | `7ad4d1a5479153bc568c67706c1497ed28d5c64acace30ac0f43ef5f8334a73e` |

The complete dependency units were the embedded base `docs/README.md`
(including research philosophy), `docs/NOTATION.md`, finite dynamics §§1–4,
special-data III.F.1–11, global-nonlinear A.1–A.4 and B.1, C.2, and the
complete C.4 introduction through C.4.6. I read the embedded rational
certificate code and reported output as source material; I did not execute
it or claim a fresh reproduction. I did not fetch the contextual external
papers linked in the reading guide or import any theorem from them.

Process inputs read in full: root `AGENTS.md`, `RESEARCH_WORKFLOW.md`,
`/etc/codex/skills/solve-math-rigorously/SKILL.md`,
`/etc/codex/skills/investigate-conjectures/SKILL.md`, and that skill's
`references/research-contract.md` and `references/adversarial-audit.md`.
The instruction hashes remained those in the frozen manifest:
`7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba`
and `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12`.

No study README, history, prior verdict, reviewer report, other agent's
findings, unassigned code or live book content was read. Initial filename
discovery exposed some unassigned path names as metadata only; their
contents were not opened. There was one metadata-only supervisor status
request and reply after the scientific reading and report drafting; no
scientific findings were exchanged. No delegation, web retrieval,
experiments, code execution from the scientific packet, Git operations,
book edits, or additional output writes occurred. The only research output
is this assigned report. No scientific inputs were missing for the stated
assessment; the proposed sign estimates remain new open obligations.
