# Nonlinear selection generalization (milestone B)

Status: active research; no milestone claim and no promotion proposal.

## Contract frozen before learning analysis

Work starts from established C.4.9 in `docs/global_nonlinear.md`, present at
HEAD `b14dc38bdca0c7835685e768e6ca0657d60cf10d`, SHA-256
`7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465`.
No unpromoted milestone-A inputs are admitted. Scientific inputs are this
study and established book/code. All research sources and reports remain flat
here; generated checks go to `data/generated/nonlinear_selection_generalization/`.

Retain C.4.9's two-hidden-layer bias-free tanh model, independent stored
Gaussian variances (1,1/n,1/n^2), mobilities (n,1,n), division of the readout by
n, unhalved square loss, physical GF, full first rows, reused Gaussian middle
action and its actual adjoint. Every physical run uses its fixed mixture from
the original initialization. Anchors retain their exact known weights.

**Frozen task class.** Write x=sqrt(2)(cos(alpha),sin(alpha)), alpha modulo
2*pi, and let rho be normalized arc measure on the entire circle. Inputs have
density p with respect to rho, 1/2 <= p <= 2, integral p=1, and circular
Lipschitz constant at most D, where D>=0 is fixed. The support is the entire
circle and never shrinks. For an integer N>=0 and s>=1, set

q(alpha)=cos(alpha)^3-sin(alpha)^3 + sin(2*alpha)^2 v(alpha),

v(alpha)=sum_{k=0}^N [a_k cos((2k+1)alpha)+b_k sin((2k+1)alpha)],

sum_k (2k+1)^s (|a_k|+|b_k|) <= R <= 1/8.

The coefficients, N, R and s specify independently varying target shape and
complexity; they do not depend on any trained predictor. This is odd and
equals +1 and -1 at the two anchors. Noise satisfies E[xi|X]=0,
|xi| <= sin(2*alpha)^2/8 and E[xi^2|X] <= sigma^2 (sigma<=1/8).
Then |Y|<=1, hence this class is admitted for every supplied Y>=1:
|cos^3(alpha)-sin^3(alpha)| <= 1-sin(2*alpha)^2/4, while
|v|<=1/8 and the noise consumes at most the other 1/8 of that margin.
The class also admits the absolutely convergent infinite series with the same
weighted coefficient bound; truncation is an explicit approximation option.
Any later material change to this class must be recorded before deriving a
favorable conclusion. A robust subfamily may be identified inside this class.

Observations (X_i,Y_i) are iid only from the added law and independent of
initialization. Test error is ||f-q||^2_{L2(nu_X)}, subtracting irreducible
noise from squared risk. Whole-circle prediction remains an observable.

Required result: population and empirical nonlinear slow selection with
continuation/capture at t=tau/epsilon; explicit target-dependent approximation
or contraction; sampling and centered-noise control and an available stopping
rule; strict unseen-risk improvement and paired second-hidden displacement on
a robust subfamily; actual finite-GF transfer with width first, then epsilon
down to zero, then sample size increasing. A finite positive episode with a
declared approximation floor is sufficient. No training experiments or broad
computational campaign are authorized. Deterministic verification is allowed.

## Work and ownership

The root coordinator owns this README and the synthesis. Independent attempts
will receive fresh contexts, explicit input scopes and disjoint flat files.
Only the coordinator may stage or commit, under the shared pde-writer flock;
other tasks' modified and untracked paths remain untouched.

Required reading: AGENTS.md, both parts of RESEARCH_WORKFLOW.md, docs/README.md,
docs/NOTATION.md, complete C.4.9 and relevant complete established dependencies.
Skills: solve-math-rigorously and investigate-conjectures, including research
contract, proof-search orchestration, evidence and adversarial-audit references.

## Evidence and open obligations

The following first-round arguments are persisted as candidates, not yet
independently checked or promoted:

- [Population spectral route](attempt_population.md): signed-measure
  separation, continuum middle-gradient injectivity, a spectral contraction
  with a Fourier approximation floor, and robust risk/activation margins.
- [Finite-section oracle route](attempt_alternative.md): the same structural
  injectivity reached independently, a comparator oracle with nonlinear
  drift, and training/validation sampling options.
- [Finite target-mode route](attempt_finite_modes.md): root's direct
  degree-dependent contraction, using a finite space containing the
  established reference residual exactly. This avoids requiring an
  unknown Fourier-tail estimate for that reference residual.
- [Statistical lemma](sampling_lemma.md): root's separate input/noise Hilbert
  variance argument and explicit Osgood propagation on the slow horizon.
- `attempt_continuation.md` is owned by continuation_route and is being
  completed before integration. Its role is arbitrary-law construction,
  original-mixture continuation, selection and actual finite-GF capture.

The independent agents started with fork_turns="none" and did not read each
other's attempts before freezing. All three independently identified the
same protected-row/sign-Fourier mechanism; their approximation methods
differ. No failed mechanism is being presented as a false target.
After population_route froze its candidate, it was assigned an internal
audit of the root's frozen finite-mode and statistical files. This later
comparison is explicitly not an independent promotion review.

The established exact rational reference certificate was rerun successfully:
[check source](check_reference_certificate.py), generated report
`data/generated/nonlinear_selection_generalization/reference_check_20260912_01/reference_certificate.json`.
Python 3.10.12, all exact assertions passed; output was
`[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`.
Reproduce with
`python3 studies/nonlinear_selection_generalization/check_reference_certificate.py data/generated/nonlinear_selection_generalization/<fresh-directory>`.
No training experiment was run.

Current scientific gap: the full integrated theorem has not yet been
assembled or audited. Each learning argument retains the continuum
continuation premise until its separate proof is accepted. Next authorized
action: compare the frozen attempts, verify every bridge, prepare the
smallest complete candidate, then obtain fresh relevance, scientific and
integration reviews before requesting approval for established changes.
