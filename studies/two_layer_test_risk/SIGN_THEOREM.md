# Early test-risk improvement at equal training loss for the fixed tanh model

This is the complete signed result of the reopened study. The proof includes
a finite deterministic arithmetic certificate. Its initial status is a
candidate complete proof pending the fresh final independent audits recorded
in the study README. It is not an established-book addition.

## Fixed model and comparison

There are exactly two tanh hidden layers, no biases, and a scalar linear
readout. The canonical stored finite weights have independent Gaussian
initialization variances `1,1/n,1/n^2`; their mobilities are `(n,1,n)`.
The stored prediction is `W3^T tanh(W2 tanh(W1 x/sqrt(2)))/n`.
All three blocks train under mean squared loss on the three prescribed
angles `0,pi/5,-pi/5`, with `x(alpha)=sqrt(2)(cos alpha,sin alpha)` and
labels `1,(1-sqrt(5))/4,(1-sqrt(5))/4`.

Let f be its actual population predictor on the established local physical
time interval, and let g freeze both initial hidden layers and train only
the readout under the same loss. Its population initial readout is zero.
Let

\[
 \mathcal L(h)=\tfrac13\sum_{a=1}^3(h(x_a)-y_a)^2,\quad
 R(h)=\frac1{2\pi}\int_0^{2\pi}(h(x(\alpha))-\cos3\alpha)^2\,d\alpha.
\]

The unique matching time satisfies `L(g_tau(t))=L(f_t)`, `tau(0)=0`,
and `Delta(t)=R(g_tau(t))-R(f_t)`. The three training examples are a
fixed design; no iid training-sample or sample-complexity assertion is made.

## Theorem

For this exact model there are `T>0` and finite `M>=1`, independent of
width and vanishing GD step, for which the matching clock is well-defined
and unique on `[0,T]`, both clocks remain within the established local
interval, and

\[
 \tau(t)=t+\beta t^3+O(t^4),\qquad
 |\Delta(t)-\chi t^3|\le Mt^4\quad(0\le t\le T).
 \tag{S1}
\]

The coefficients obey the strict rational bounds

\[
 \frac{27}{100000}<\chi<\frac{273}{1000000},\qquad
 \frac{35309}{1000000}<\beta<\frac{35311}{1000000}.
 \tag{S2}
\]

In particular, the cubic term is the first nonzero term of the matched
test-risk difference. On the width-independent positive interval

\[
 0<t\le t_0:=\min\left\{T,\frac{27}{200000M}\right\},
 \qquad
 R(g_{\tau(t)})-R(f_t)\ge\frac{27}{200000}t^3>0.
 \tag{S3}
\]

Thus learning the hidden features improves test prediction at the same
training loss for sufficiently early positive times in this model.
The number t0 and the remainder constant are not numerically evaluated.

## Proof of the signed conclusion

The complete actual-flow proof in MATCHING_AND_REMAINDER, with the exact
coefficient in CUBIC_DERIVATION, proves (S1). The canonical proof in
PROMOTION_C4 contains the same result and all operative Gaussian/flow
dependencies in its frozen packet. These proofs retain the moving residual,
first-layer update, connector update, induced readout update and both uses
of the initial connector. They prove strict frozen loss decrease and unique
matching before expanding it. In particular (S1) is a trajectory remainder,
not a formal finite jet promoted to a positive-time statement.

For clarity, the exact scalar targeted by the new calculation is

\[
 \chi=2\int\cos(3\alpha)[J_\alpha-\beta a_\alpha],d\mu(\alpha),
 \quad a_x=2E_2[S H_x],\quad
 \beta=\frac{8\mathcal A}{3B_0},
 \quad B_0=E_2[S^2],\quad S=\sum_a p_aH_a,\quad p=y/3,
\]
\[
 \mathcal A=p^\top(G\circ D+Q\circ V)p,\qquad
 J_x=4\mathcal C_x(U_x)+\tfrac43\sum_a p_a\mathcal C_a(H_x\phi'(Y_a)).
 \tag{S4}
\]

Every field/moment in (S4) is defined without an operator oracle by
CUBIC_DERIVATION (14)--(19). The explicit response mean products are
retained. DRIVER_CERTIFICATION (D5)--(D6) restates the scalar assembly.

CERTIFIED_ERROR proves a normalized Gaussian tensor-rule bound with tails,
and a covariance perturbation bound valid at singular covariances. The
driver applies these to the actual two-root input law and to each upper
Gaussian tuple. CERTIFICATION_ENGINE proves an absolute arithmetic error
of at most `10^-9` for each primitive finite sum, under its checked compiler
and input contracts. The driver then uses outward rational interval
operations for every coefficient contraction and the clock division.
ANGULAR_CERTIFICATE proves the remaining circle-rule error is below
`10^-6` after the separately checked `|beta|<=1/10` hypothesis.
DRIVER_CERTIFICATION combines these bounds, including input constants,
label rounding, covariance errors and singular passive nodes.

The target-26 calculation uses a fixed 256-angle rule, reduced by exact
symmetry to 64 distinct nonzero contributions, and anisotropic Gaussian
root grids with truncation radius at least eight. Grid choices depend
only on certified root-column sizes and the fixed error target. No
training, random sampling, parameter sweep or teacher selection occurs.

The executed certificate encloses the exact coefficient in

\[
 \frac{5358604107658561212253567}{19807040628566084398385987584}
 \ \le\chi\le\ 
 \frac{21597479156841685713774185}{79228162514264337593543950336}.
 \tag{S5}
\]

The endpoints are approximately `0.00027054037037366814` and
`0.00027259851133052906`; those decimal displays are not used to decide
the sign. Exact integer cross-multiplication places (S5) strictly inside
the rational chi bounds in (S2). The same execution gives

\[
 \frac{2797504526179671494928101665}{79228162514264337593543950336}
 \ \le\beta\le\ 
 \frac{2797556156441557459457527739}{79228162514264337593543950336},
 \tag{S6}
\]

which lies strictly inside the displayed beta interval and in `[-1/10,1/10]`.
All primitive inputs and output bits, intermediate enclosures, exact final
fractions and source hashes are retained in the fresh run
`data/generated/two_layer_test_risk/certificate_20260910_01/`.
This is a deterministic computer-assisted inequality, not an empirical
estimate with a confidence level. The complete error arguments and
executed arithmetic are part of its proof and must both be checked.

Finally (S1), (S2), and `Mt<=27/200000` imply

\[
 \Delta(t)\ge t^3(\chi-Mt)
 >t^3\left(\frac{27}{100000}-\frac{27}{200000}\right),
\]

proving the conservative non-strict lower bound (S3). Strict positivity
also proves nonvanishing of the cubic coefficient. No new population
existence or global continuation theorem is needed.

## Finite networks, hidden movement and size of the conclusion

Finite comparisons retain the same actual small random initial readout;
its hidden tangent blocks need not vanish at finite width. The prior
passive-circle capture and inverse-loss argument transfer this positive
comparison in probability as width tends to infinity, for finite GF and
for every deterministic raw-GD step tending to zero, on every fixed
closed interval `[delta,t0]` with `delta>0`. There is no quantitative
width requirement or a finite-width sign claim uniformly down to zero.
The established convergence scope is not enlarged by the arithmetic proof.

Both hidden activation and preactivation displacements have nonzero
order-`t^2` onset, and the fixed-model local nonaffinity bounds already
proved in RESULT continue to apply. These activity facts alone did not
prove benefit; the new signed, matched-risk coefficient supplies that
additional conclusion.

The initial test risk is exactly `1/2`, and the leading benefit is only
about `0.000272 t^3`. The theorem establishes a strictly positive local
effect, without claiming a practically substantial improvement or a
numerically specified useful time window. It concerns this single fixed
teacher/design and two-layer architecture. It does not establish a
universal benefit, later-time dominance, global fitting, an iid-average
generalization theorem, or growing depth/sample/dimension limits.

## Reproduction and supersession

The complete reproducible source and proof are retained in the study:
`certificate_driver.py`, `certificate_kernel.cpp`,
`DRIVER_CERTIFICATION.md`, `CERTIFICATION_ENGINE.md`,
`CERTIFIED_ERROR.md`, `ANGULAR_CERTIFICATE.md`, and the exact scalar
and supplied-state checks. The command is in DRIVER_CERTIFICATION and
must use a fresh generated output directory. The first full run exited
zero, used 31.18 CPU seconds, and evaluated 86,101,134 upper Gaussian
nodes in total. Its result SHA-256 is
`89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d`.

This signed theorem supersedes the previously open scalar-sign obligation,
once its complete fresh checks are recorded. It does not retrospectively
turn the old diagnostic quadrature into a sign certificate. The old
partial-result promotion proposal and its reviews cover their old scope
only; no established book or code is changed by this study result.
