# Proposed C-H1 addition — version 3

Approval status: ready for user approval; both complete scientific reviews and
the independent integration review passed. This proposal changes no established
file. The exact proposed source is
[candidate_v3.md](candidate_v3.md), with the exact full guide replacement in
[README_proposed_v3.md](README_proposed_v3.md). The review input versions are
frozen in [review_inputs_v3.json](review_inputs_v3.json).

## Concrete destinations and value

Insert the entire candidate as `docs/global_nonlinear.md` C.4.7.8, immediately
after C.4.7.7 and before C.4.8. In `docs/README.md`, add its nine-line status
paragraph after the C-H1 scope and adjust the later planning-status sentence.
The exact assembled diffs and book are under
`data/generated/observable_hierarchy/edition_v3/`; their hashes and checks are
preserved in [edition_manifest_v3.json](edition_manifest_v3.json). No maintained
code or API addition is proposed.

The new value is a finite instruction alphabet and explicit finite upward
weak-evolution rule for a current joint observable population state. Existing
Gaussian initialization, population existence and generated-current-state
sufficiency are acknowledged foundations. The addition makes their information
interface concrete and proves the complete hierarchy's restart property.
The independent placement report is [selection_v1.md](selection_v1.md).

## Exact theorem supplied

For each fixed `Y >= 1`, use the canonical no-bias two-hidden-layer tanh model,
stored independent Gaussian variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`,
residual `f-y` and physical gradient flow of unhalved mean-square loss. On
`sqrt(2) S^1 x [-Y,Y]`, use the transport cost
`|x/sqrt(2)-x'/sqrt(2)|+|y-y'|`. Fix

```
T0 = 1/200,
delta = min(delta_Y/4, delta_act,Y, 1/4) > 0,
U = {mu: W1(mu, nu_*) < delta}.
```

Here `delta_Y` is a fixed established C.4.7 radius; part 8 constructs a positive
`delta_act,Y` from nonzero Gaussian contractions and law continuity. These
constants are independent of hierarchy order. The family contains nonorthogonal
and nonatomic laws, and both hidden layers change and remain nonaffine at one
common positive time.

1. At level `j`, retain all same-population joint laws of finite typed programs
   with at most `j` nodes and tuple dimension at most `j`. There are finitely
   many graph types, at most `3j` scalar program marks and `j` circle directions;
   characteristic tests add at most `j` frequencies. The alphabet consists of
   current row/readout and specified frozen initial observations, affine maps,
   sine/cosine/tanh, bounded products, and both orientations of the current
   action applied only to bounded programs. Every finite cross-input and
   initial/current joint appears at a finite level. All circle predictions are
   recovered. Initialization is an explicit finite Gaussian-source construction
   with the actual reused forward/adjoint response corrections and uncentered
   input Grams, including singular cases. Continuum law integration is declared
   exactly. Each separately fixed tuple has the established finite-network
   interpretation in probability in `W2`.

2. Every fixed characteristic observation is `C1` in physical time. Equation
   (H8) is its exact evolution, with every moving coefficient and action
   occurrence retained. A finite reverse compiler reads only level
   `N = 10^6(j+1)^6`, current joint contractions, one training-law integral and
   the specified cutoff limit `R -> infinity` inside that fixed level. The
   level and tuple dimensions do not grow with the cutoff. No unrestricted
   `L2` product algebra, temporal-jet argument or moment-determinacy premise is
   used.

3. Let `S` be reached at time `s <= T0` on a canonical trajectory for `mu in U`.
   Every realization on two probability spaces with square-integrable row and
   frozen seed fields, bounded readout, bounded middle action and its actual
   adjoint, whose complete current hierarchy equals that of `S`, has a unique
   strong continuation under the same `mu` for `[0,T0-s]` in its affine raw
   space with Hilbert–Schmidt middle increments. Throughout that interval its
   whole-circle predictions and every declared same-population joint
   hidden/action/initial-current observation equal the reference continuation's.
   Equality means equality of all finite joint laws and their specified
   second-moment pushforwards/contractions, with zero uniform difference of
   continuous prediction maps. The proof reconstructs the observable probability
   algebras, intertwines both actions, proves invariant continuation by Euler
   comparison, and transports the dynamics. It imposes no separate tail
   hypothesis on a competing strong solution.

## Boundaries and C-H2

Finite levels are finite-type families of probability laws over finite-dimensional
mark domains, not finitely many stored scalars. The exact cutoff and training-law
integrals are information interfaces; the theorem supplies no effective numerical
evaluation rate. A level contains no raw dense operator, full parameter-space
distribution, arbitrary latent-vector query, elapsed transcript or future data.
Only the complete hierarchy reconstructs the dynamically relevant action in
the proof.

Restart covers a reached state and all matching realizations under that reached
state's law. It does not assert arbitrary switching of every unmatched state to
every training law or uniqueness for arbitrary unrealizable formal sequences.
The positive law radius is qualitative. The main C-H1 family and interval are
fixed, although the exact identities/restart mechanism also use the larger
established interval when stated with its remaining horizon.

C-H2 must construct finite autonomous equations and prove their convergence on
one fixed nonlinear interval and law family. Uniform control of the omitted
higher information and the cutoff, realization of limiting dynamics, stability
and closure convergence remain open. Population/input quadrature, arithmetic
precision, practical resource bounds and certified solver performance are later
obligations. The hierarchy does not assume a small omitted tail or claim these
risks are resolved. No training experiment was performed.

## Validation and review record

The original full reports, input hashes and coverage are required evidence;
short verdicts here cannot substitute for them.

| Gate | Outcome | Original evidence |
|---|---|---|
| Independent relevance/placement | Accept for narrow assembly | [selection_v1.md](selection_v1.md) |
| Fresh complete scientific review A | PASS; no required correction | [review_v3_a.md](review_v3_a.md) |
| Fresh complete scientific review B | PASS; no required correction | [review_v3_b.md](review_v3_b.md) |
| Fresh independent integration review | PASS; no required correction | [integration_v3.md](integration_v3.md) |

Both scientific reviewers read all 642 candidate lines and all 3,569 dependency
lines, full guides/notation and complete check sources, and independently ran
both deterministic checks. They had no author/internal verdicts, each other's
findings or project history. The integration reviewer read all assembled new
material and its precisely declared older scope. The coordinator read all
original reports completely and verified unchanged inputs, exact source/output
hashes, execution records and isolation. See
[review_acceptance_v3.json](review_acceptance_v3.json). No required correction
was made after the paired review freeze; optional editorial suggestions remain
unapplied to the reviewed package.

The deterministic static check compares the exact weak identity with independent
forward differentiation and central differences, including both adjoint
orientations and nonorthogonal inputs. It passes. The complete established
rational Gaussian certificate was rerun and all assertions pass. The standalone
edition reruns both from copied source with no study/history/output dependency.
It also validates exact insertion/removal preservation, the guide diff, the new
local link and equation labels. Untouched older book links and unrelated older
proofs are outside this integration scope. There are no new empirical claims.

The upstream established existence/tail proof uses the rational reference
certificate. Part 8's new qualitative hidden-activity proof requires no
additional numeric certificate; this does not remove the upstream dependency.

Reproduce the edition from the repository root with a fresh output directory:

```
python studies/observable_hierarchy/assemble_edition_v3.py /home/amir/Codes/PDE/data/generated/observable_hierarchy/edition_v3_fresh
```

The assembly script verifies frozen source hashes and fails if dependencies
have changed. It creates a standalone proposed edition only. After approval,
the exact reviewed insertion and guide change would be applied under the shared
Git writer lock after rechecking sources and concurrent changes, followed by
candidate-to-live correspondence checks. Any scientific change reopens review
and approval for the changed package.

Recommendation: approve this exact C.4.7.8 insertion and guide update as C-H1.
Its information and restart conclusions pass the completed gates. Retain C-H2
as open, with no claim of finite closure convergence or numerical usefulness.
