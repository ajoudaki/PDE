# Internal check of direct-reference transfer

2026-10-05. **PASS for the elementary conditional claims checked below.**
No mathematical correction is required to either inspected file. This is a
bounded same-study internal check with prior context retained, not a fresh
isolated promotion review. It does not establish a direct initializer or
certify any inherited neural approximation theorem.

The complete scientific inputs inspected were:

- `docs/notation.qmd`;
- `VIRTUAL_REFERENCE.md`, SHA-256
  `526da5e8d7325cbb2dfec919d54170a4ad0b4764ba00ea5a6abe56f484a75ef8`;
- `DIRECT_INITIALIZER_TARGET.md`, SHA-256
  `e5c54849f72322eee0aa0e471bf5afee787ff75069b75b2d1ad408f03f602c5b`.

The current proof and conjecture-investigation instructions were retained.
The previously disclosed inability to read the canonical-notation skill and
its authorized notation fallback remain applicable. No linked source,
other study, experiment, test, Git operation, or external scientific source
was used.

## Probability, transport, and averaging

All numbered references in this section are to `VIRTUAL_REFERENCE.md`.

1. **Minimal coupling and exact-law transfer, (3a) and (3): correct.**
   A joint pair consisting of the direct compact initialization and a
   canonical virtual dense trajectory may be correlated internally.
   Adjoining an independent canonical dense reference gives the required
   independent dense pair. The triangle inequality and union bound add the
   coupling and dense-pair errors and failure probabilities. The actual
   direct-model/reference experiment has this same product law. In the
   specialization, equality of the complete compact initialization law
   gives equality of its product law with the independent reference.
   Independence of the two failure events is unnecessary.

2. **Total variation, (4): correct with the stated normalization.**
   The reference-averaged failure function takes values in $[0,1]$.
   Integrating its level sets bounds the difference of its expectations by
   $\sup_A|P(A)-Q(A)|$, with no extra factor of two. Pushing initialization
   laws through a measurable training map cannot increase this total
   variation bound. No dynamical continuity is needed.

3. **Trajectory transport, (6)--(8): correct.**
   An arbitrary admissible coupling of the two compact trajectory laws can
   be taken independent of the actual reference. The already established
   independent-reference property of its paired-law marginal is sufficient;
   no additional gluing to a particular dense seed is required. Near-optimal
   couplings and the elementary moment tail bound give $(\tau/r)^p$.
   Letting the near-optimality error tend to zero is valid because the
   probability being bounded depends only on the fixed product law.
   For $\tau=0$, the events with threshold $e+v+r$ increase, as $r$ decreases
   to zero, to the event with threshold $e+v$. Thus the claimed zero-radius
   conclusion does not assume existence of an optimal coupling.

4. **Parameter transport, (9)--(11): correct as conditional statements.**
   On the event that the parameter distance is at most $r$, the assumed
   nondecreasing modulus bounds the trajectory distance by $\omega(r)$.
   A global Lipschitz estimate therefore gives trajectory Wasserstein error
   at most $L\tau$. The local version correctly charges the exceptional
   masses under both laws, regardless of their coupling. The scalar flow
   $\dot x=x$ correctly disproves a general inference from small parameter
   transport to small uniform-in-time trajectory transport.

5. **Deterministic centers and witnesses, (12)--(13): correct.**
   If a bounded measurable conditional failure function has expectation at
   most $c$, some point has value at most $c$: otherwise its strictly
   positive excess above $c$ would have positive expectation. Applying this
   observation to the dense-pair law and then to the transferred compact
   law proves the two existence statements. The selected point may depend
   on width, confidence, data, and distance. Neither selection is an
   algorithm or a simultaneous statement over these choices. The
   two-point counterexample correctly distinguishes a successfully paired
   but atypical seed from a good independent-reference witness.

The measurability and observation-existence assumptions are explicit and
adequate. Confidence allocations, full joint initialization metadata, and
the use of one common physical clock and comparison distance are tracked
correctly. The proofs remain conditional if this distance includes all
times, the sphere, and the endpoint; none supplies those neural estimates.

## Elementary Gaussian checks

For the adaptive scalar example in `DIRECT_INITIALIZER_TARGET.md`, let
$u$ be a deterministic unit vector and let $W_{ij}$ be independent
$\mathcal N(0,1/n)$. The coordinates of $Wu$ are independent
$\mathcal N(0,1/n)$. Consequently

$$
n\|Wu\|_2^2\sim\chi_n^2,\qquad
\mathbb E\|Wu\|_2^2=1,\qquad
\operatorname{Var}(\|Wu\|_2^2)=2/n.
$$

For $v=Wu/\|Wu\|_2$, the coefficient $v^TWu=\|Wu\|_2$ tends in probability
to one. By contrast, two deterministic unit directions give a coefficient
distributed as $\mathcal N(0,1/n)$, which tends to zero. A width-one
centered Gaussian does not converge to one either. These claims, including
the possibility of directly sampling this individual chi-distributed
coefficient, are correct; they do not supply a joint initializer sampler.

For the backward projection, condition on a nonzero $h$ independent of $W$
and put $z=Wh$. With

$$
P_h=I-\frac{hh^T}{\|h\|_2^2},
$$

each row decomposes as

$$
W_i=\frac{z_i}{\|h\|_2^2}h^T+\xi_i^T,\qquad
\xi_i\mid(h,z)\sim\mathcal N(0,P_h/n).
$$

The residual rows are conditionally independent. Their Gaussian covariance
with the projected row coordinates is zero, which proves the required
conditional independence. If $b$ is a measurable vector function of $z$,
it is fixed under this conditioning, so

$$
W^Tb\mid(h,z)\sim
\mathcal N\!\left(
h\frac{z^Tb}{\|h\|_2^2},\,
\frac{\|b\|_2^2}{n}P_h
\right).
$$

Since $P_h^2=P_h$, the displayed projected-standard-Gaussian representation
in the target note has exactly this covariance, including when $b=0$.
For $b_i=\tanh(z_i)\tanh'(z_i)$, every nonzero $z_i$ has $z_ib_i>0$.
Conditionally on nonzero $h$, the Gaussian coordinates $z_i$ are nonzero
almost surely, so the conditional mean is nonzero almost surely. Replacing
this response by an independent centered Gaussian would be incorrect.

## Scope of the pass

The elementary retained-size arithmetic is consistent: for fixed $d,m$,
$q\ge m$ and the stated width bound, the displayed coordinate counts have
order $q^2$, giving the reported logarithmic exponent. The underlying
width bound, source basis construction, selection metrics, and accounting
for all additional initializer or decoder objects are **unreviewed inputs**.
Likewise, the old paired error, independent dense-pair error, and maintained
Gaussian compiler's existence, scope, and resource claims were not checked
against their sources.

Both files correctly preserve the missing rate obligation. An
$O(n^{-1/2})+o(1)$ bound or an $n^{-1/2+o(1)}$ bound does not imply
$C/\sqrt n$ with a width-independent constant. A direct sampler, a valid
full joint law or alternative canonical coupling, admissible computational
resources, and sufficiently sharp discrepancy bounds remain separate
requirements. The inspected reduction matches a fresh independent dense
reference and does not infer any of these requirements from the probability
argument alone.

This report is frozen at handoff; its SHA-256 is supplied separately.
