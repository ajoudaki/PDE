# C-H3 contract and bounded execution record

Status: active research; no C-H3 theorem, certified solver, or promotion claimed.
Coordinator: `/root`, task `01a096c9-0ffc-7173-8198-831cf5b6ac53`.
Started 2026-09-12 at HEAD `117991a49487209a8859c9294369482b35825e58`.

## Target and source recovery

Complete useful certified computation of the SAME autonomous nonlinear population
GF as C.4.7.9: bias-free two-hidden-layer tanh, independent stored Gaussian
variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, residual `f-y`, unhalved
mean-square loss and physical horizon `T=1/200`. Finite-network statements retain
the actual random finite readout. Both directions use the same initialized action.

The coordinator read AGENTS.md, both workflow parts, docs/README.md,
docs/NOTATION.md, code/README.md, both required skills and all five applicable
research references. The complete H2 v3 theorem, prototype, tests, notes,
contract, checks, acceptance and promotion records were recovered. All 3569 lines
of dependencies_v1.md and H1 dependency parts 1–3, 5–6 and 8 were read.
Live hash checks match all five approved H2 destinations; H2 and H1 are literal
insertions in the current chapter; all seven dependency excerpts match their
named maintained sources. Valid completed H2 scientific audits are not rerun.

The decisive obstacle is H2.10: its compact target-dependent source error tends
to zero, but supplies neither a computable order selector nor useful numerical
bounds. Replacing this error by agreement of resolutions is forbidden. Gaussian
source conditioning, population integration and small first-layer motion are
additional costs to assess before a large solver investment.

## Required claim ladder

1. Computable represented fixed law family inside the H2 neighborhood, including
   nonorthogonal and nonatomic laws; its radius and T do not depend on accuracy.
2. Autonomous finite equations and complete initialization, observation and
   restart implementation, without trajectory inputs, fitting, arbitrary action
   oracle or accumulated training history.
3. Terminating refinement for every fixed admitted represented law and positive
   tolerance, controlling whole-circle prediction on all of `[0,T]` and every
   separately fixed admissible same-population joint observation tuple in W2.
4. Separate closure, Gaussian/initialization, population/input integration, time,
   and finite-arithmetic errors, all derived from computable inputs or proved
   bounds. No assumed small tail or unknown exact trajectory in a certificate.
5. Useful executed and independently reproduced demonstration, with positive
   resolved prediction and BOTH paired hidden-motion signals and actual costs.
6. Total fixed working storage at a chosen accuracy, including frozen marks,
   populations, matrices, numerical/certification buffers and precision; restart
   carries its existing error budget.
7. Independent relevance, two fresh complete isolated scientific reviews,
   separate assembled-edition integration review, then concrete user approval
   before any established book/code change.

No conditional certificate or partial implementation completes these claims.
Failure of a witness or proof route is not impossibility of the objective.

## Independent initial portfolio and ownership

Each route starts without inherited conversation. Allowed scientific sources
are the selected H2 v3 theorem and its named established dependencies, with the
prototype/notes additionally allowed for the effective route. Required skills
and process instructions remain applicable. No other study is an input.

| Owner | Mechanism | Owned output |
|---|---|---|
| `/root/h3_residual_route` | Computable a posteriori defect and one-reference stability | H3_route_residual.md |
| `/root/h3_shorttime_route` | Short-time Duhamel bounds and tailored initialized fields | H3_route_shorttime.md |
| `/root/h3_effective_route` | A priori effective dictionary / Gaussian program compilation | H3_route_effective.md |
| `/root` | Source recovery, synthesis, contract, shared README and sole Git writer | remaining coordinator H3_* files |

Routes do not read each other's reports until frozen. Any later collaboration
will be recorded. The coordinator noticed that N19 may close at T=.005 and sent
that suggestion to the effective route with an instruction to retain first-route
isolation until freezing; the agent reports it had independently noticed N19
immediately beforehand. This overlap is disclosed rather than counted as a blind
independent confirmation.

## Preregistered demonstration and numerical bounds

Freeze before any trajectory: Y=1, reference law
`nu*=.5 delta_(sqrt(2)e1,+1)+.5 delta_(sqrt(2)e2,-1)`; observation physical times
`0,1/400,1/200`; saved restart at `1/400`. This law is within every H2 ball.
The supported theorem must additionally cover an effective fixed family with
nonorthogonal and nonatomic examples; success at the reference alone is not it.

Primary final-time metrics are the whole-circle norm
`sup_u |f(T,sqrt(2)u)-f(0,sqrt(2)u)|` and
`D_l=(integral E_l|H_l(T,u)-H_l(0,u)|^2 dnu*)^(1/2)` for l=1,2, using the same
initial/current coordinates. Pass requires certified lower bounds above `1e-4`
for prediction and `1e-7` for EACH motion. Prediction absolute error must be
at most `1e-5` on the full time/input domain; each reported paired RMS error
must be at most `1e-7`. Zero is the predeclared null signal. A stable approximate
curve alone is inconclusive. Broader learning/superiority claims are not tested.

Numerical work: one core per process, at most 8 GiB resident memory, at most
900 seconds for initialization plus evolution per demonstration execution;
at most two coordinator executions (one initial and one numerical-validity
repair without changing scientific thresholds), plus two independent fresh
reproductions. Total trajectory budget 3600 core seconds. Deterministic
preflight/certificate checks have a separate 600-core-second cumulative cap.
Record actual initialization/evolution time, peak RSS, precision, conditioning,
source/config hashes and environment. No trajectory starts before a justified
certificate path and resource estimate are available. A preflight can terminate
a route before trajectory execution. Failed/inconclusive runs are preserved.

Any precision or resolution refinement must keep the scientific configuration,
times and thresholds fixed. Arbitrarily fine requested accuracies need not fit
the demonstration budget. Stop numerical work at its bounds; preserve exact gaps.
No neural-network training campaign, broad sweep or time-40 extension is allowed.

Generated results use fresh `data/generated/observable_hierarchy/H3_*` run
directories. No unique proof/configuration/source is stored only in generated
data. Shared Git transactions take the nonblocking common pde-writer.lock,
recheck HEAD/index, stage explicit owned paths, verify the exact staged list,
commit and release. Existing concurrent modifications remain untouched.
