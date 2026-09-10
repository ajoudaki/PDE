# Internal review of the angular error certificate

Reviewer: `sign_structure`, 2026-09-10.

**Verdict: ACCEPT for its stated conditional angular-error bound.**
No required mathematical or implementation correction was found. The proof
certifies the difference between the exact angle integral and the exact
256-node periodic rule, conditional on `|beta|<=1/10`. It does not certify
the nodal Gaussian expectations, the covariance parameters, the value of
beta, rounding in a coefficient producer, or the sign of chi.

This is an internal audit. The reviewer authored SIGN_STRUCTURE.md and
therefore is not a fresh isolated promotion reviewer. The reviewer did not
author ANGULAR_CERTIFICATE.md or angle_error_bound.py and made no edits to
their sources. Only the report and the fresh generated run below were
written. No quadrature of the scientific coefficient, training, random
sampling or parameter search was performed.

## Inputs and read coverage

Read every line of ANGULAR_CERTIFICATE.md (214 lines) and
angle_error_bound.py (88 lines). Reconstructed their formulas against the
complete CUBIC_DERIVATION.md read during this task, in particular its
equations (14)--(22). The current initialized Gaussian source/response
proof, notation, finite normalization and relevant skill instructions were
already read for the preceding analytic subtask; its precise source scope
is recorded in SIGN_STRUCTURE.md. The new audit uses the initialized
Gaussian law and exact cubic coefficient, not a new population-flow
existence or remainder argument.

SHA-256 values of the reviewed inputs:

| Input | SHA-256 |
|---|---|
| ANGULAR_CERTIFICATE.md | `a60fb1a63e060c2b9fc7dc3b211a8bc0e71ce51195364c9a681127dcf0adb4d2` |
| angle_error_bound.py | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| CUBIC_DERIVATION.md | `3f46c878a77dd046c876d5195950f6262b3db06a025cb756518643f4c97ca495` |
| SIGN_STRUCTURE.md | `00fb949d4401797676fcaa31d09cb067532bf3359e7d0731071a2cb18d9bc599` |

## Reconstruction of the exact integrand

The notation `M_bj=E[partial_j U_b]` with `U_b=S d_b` gives exactly
`M_bj=p_j E[d_j d_b]+1_(j=b) E[S d'_b]`. Because all nonpassive indices
are training-only, `sum_j |M_bj|<=2P`. Hence the lower response mean
`mu_b=sum_j h_j M_bj` satisfies `|mu_b|<=2P`.

For the first term, the full reused-transpose contraction is

`C_x(U_x)=sum_b p_b {Q_xb E[U_x U_b]+G_xb Lambda_xb(U_x,U_b)}`.

Its response-free part is the first two terms of (A6). Its derivative
mean is `E[partial_i U_x]=p_i E[d_i d_x]+1_(i=x)E[S d'_x]`.
These two summands give exactly the third and fourth terms of (A6),
including the passive lower feature `h_x` in the fourth term. Neither
response mean is omitted.

For the second term, differentiate the actual upper function `H_x d_a`:

`E[partial_i(H_x d_a)]=1_(i=x)E[d_x d_a]+1_(i=a)E[H_x d'_a]`.

The direct second moment and the two derivative terms give the three
displayed terms of (A7), with exactly the factors `mu_b` and `h_a mu_b`.
The weights remain `p_a p_b`; the `S` inside the upper expectation has
not been dropped. The reconstruction agrees with
`J=4 C_x(U_x)+(4/3)sum_a p_a C_a(H_x d_a)`.

An important boundary check is a passive angle equal to a training angle.
The passive coordinate is still differentiated with respect to its own
angle; the training fields in `S`, `M_bj`, and every training-only moment
stay fixed. Equations (A6)--(A7) use precisely this convention. Coincident
or antipodal Gaussian slots require no covariance inverse or differentiation
of a conditional variance.

## Scalar and Gaussian derivative bounds

The low-order real bounds in (A2) are valid. In particular
`sup|tanh''|=4/(3sqrt(3))<1`, and the third derivative polynomial takes
values in `[-2,2/3]` as `tanh(x)^2` varies from zero to one. Thus the
choices `m_2=1` and `m_3=2` are conservative. For the higher derivatives,
the radius-3/4 circles are pole-free and lie inside `|Im z|<pi/4`.
The displayed formula gives `|tanh z|<=1` there, so the stated Cauchy
bound applies at every real center with the same radius.

The odd Gaussian absolute moment majorant is conservative because
`sqrt(2/pi)<4/5`; the even moments and ceiling square roots used for
`c_j` are exact integer constructions. Every lower angular derivative of
`Z_alpha` is a standard Gaussian up to sign and rotation. Holder's
inequality controls a product of `j` such variables in L1 by `mu_j`, and
in L2 by the square root of the `2j`-th absolute Gaussian moment. It does
not require independent derivatives. The Stirling-number majorant for
the lower composite derivative therefore has the claimed coefficients.

The Gaussian smoothness premise in the upper derivative argument is
adequate. The initialized `Y_alpha` is the isonormal image of `h_alpha`;
each lower L2 derivative is a limit of difference quotients in their
closed linear span. Isometry transfers this derivative to a centered
Gaussian upper derivative. Convergence in L2 of Gaussian difference
quotients implies convergence in each fixed finite Lp because their Lp
norms are a fixed Gaussian moment times their standard deviations.
Joint derivatives have the required Gaussian product bounds regardless
of their covariance or degeneracy. Repeated product and chain rules,
with bounded tanh derivatives and Gaussian moments, justify differentiating
all displayed expectations through order eight. No sample-path analyticity,
invertibility of an augmented covariance, or smooth matrix square root is
required.

The Bell recurrence in (A3) is the correct exponential partial Bell
recurrence. For a product containing `j` upper angular derivatives, Holder
gives `mu_j` times their standard deviation bounds. Substitution of the
`s_k` bounds into the Bell polynomial gives exactly `u_r(k)`. The largest
scalar derivative order needed is ten, available in (A2).

## Independent check of (A8)--(A9)

Tracking each term with absolute weights gives the following bounds:

| Term | Bound after summing absolute label weights |
|---|---|
| (A6), first | `P^3 (l_0*u_1)` |
| (A6), second | `P^3 (g*l_1*u_1)` |
| (A6), third | `2P^3 (g*l_1*u_1)` |
| (A6), fourth | `P^3 (g*l_2*u_2)` |
| (A7), first | `2P^3 u_0` |
| (A7), second | `2P^3 (l_0*u_1)` |
| (A7), third | `2P^3 u_0` |

The fourth line uses the exact identity `e_x h_x=-phi''(Z_x)/2`; its
factor `1/2` cancels the factor two from `sum_j|M_bj|<=2P`.
Thus (A8) is correct, including its coefficient three. Multiplying the
first four lines by four and the final three by `4/3` gives the coefficients
`20/3,12,4,16/3` in (A9). The outer factor two is required by the risk
coefficient definition, and the clock contribution is
`2 |beta| P u_0` before that outer multiplication. The teacher derivatives
are bounded by `3^k`. Finally `P<27/50` follows, for example, from
`sqrt(5)<56/25`; replacing the positive powers of P by this rational bound
can only enlarge the majorant.

## Periodic quadrature and symmetry

The constructed integrand is C8 and periodic. Eight integrations by parts
give the stated `D/|k|^8` Fourier bound with no boundary terms. This gives
an absolutely convergent Fourier series, so averaging it on the N nodes
is valid. The surviving nonzero aliases are `k=ell N`, giving
`2 zeta(8)D/N^8`. The integral upper bound `zeta(8)<=8/7` has the correct
direction and normalization.

Reflection preserves the training design and its equal side labels.
Antipodal input reversal preserves the oddness of the predictor and of
the cubic profile. The product with the teacher is therefore even and
pi-periodic. In the 256-node rule, angle zero and angle pi supply two
copies of `F(0)`. Each index 1 through 63 has four equal contributions.
The two remaining nodes, pi/2 and 3pi/2, vanish because their teacher is
zero. This proves precisely (A10). The weights account for all 256
nodes; no factor of two or endpoint weight is missing.

## Executed exact scalar check

Command, run from `/home/amir/Codes/PDE` with Python 3.10.12:

```text
python -B studies/two_layer_test_risk/angle_error_bound.py --output data/generated/two_layer_test_risk/angular_review_20260910_01
```

The fresh directory was created by the script with `exist_ok=False`.
Exit status was zero. All acceptance arithmetic used integers/Fraction;
floating conversion was used only for the explanatory decimal string.
The exact results were

```text
D = 41272525446939874982/31640625
angular error <= 20636262723469937491/127677049435953561600000000
              < 1/1000000.
```

The reported decimal is `1.6162859977291121e-7`.
The result is retained at
`data/generated/two_layer_test_risk/angular_review_20260910_01/result.json`,
SHA-256 `2a1d5ec88889cbe2f9dd80cd9b4faa7274b727db33a6c37d8c122122662c5f0a`.
This reruns the author producer after independently checking its mathematical
recurrences and exact-arithmetic implementation; it is not an independent
coefficient integrator.

## Remaining obligations and acceptance scope

The angle bound can be used in a complete sign certificate once a rigorous
training enclosure verifies `|beta|<=1/10` and rigorous enclosures are
available for all 64 exact nodal values in (A10). Their weighted interval
sum must then be enlarged by a proved angular-error interval. Its final
sign must be checked after all primitive, covariance and rounding errors
are included. Nothing in this review supplies those enclosures or checks.
There are no additional unresolved objections to the angular proof itself.
