# Check of the full-parameter transport limitation

2026-10-03. Scoped internal reconstruction requested by the coordinator.
This is collaborative research validation, not an isolated promotion
review. No experiments or other study inputs were used.

Checked complete source: `POPULATION_TRANSPORT_LIMIT.md`, SHA-256
`e6fef85f4168e0a83f8ba6cc740bd65d19e7125d60c3ee1199c5e0a65352e2b2`.

**Verdict: PASS.** The deterministic transport lower bound and the
independent Hilbert-valued averaging identity are both correct. Their
different scopes are correctly distinguished from a trained-prediction
rate.

For fixed positive integer dimension \(d\), the standard Gaussian
density is bounded above by \(b_d=(2\pi)^{-d/2}\). For arbitrary
centers \(A_1,\ldots,A_n\), a union bound on Lebesgue volumes and
this density bound give
\[
 \gamma_d\left(\bigcup_i B(A_i,r)\right)
                  \le b_d n v_d r^d.
 \tag{1}
\]
This remains true with repeated centers. At
\(r=(2b_d v_d n)^{-1/d}\), at least half the Gaussian mass lies
outside that union. For every coupling whose first marginal is supported
on these centers and whose second marginal is \(\gamma_d\), that
event implies \(\|A-G\|\ge r\). Hence
\[
 \mathbb E\|A-G\|^2\ge r^2/2,
 \qquad
 \|A-G\|_{L^2}\ge
       \frac{(2b_dv_d)^{-1/d}}{\sqrt2}\,n^{-1/d}.
 \tag{2}
\]
The argument does not even require equal atomic weights. In particular
it applies to the specified empirical law, deterministically for every
realization of its Gaussian sample rows.

For \(d>2\), the logarithm of the ratio between (2) and the proposed
near-root scale is
\[
 \left(\tfrac12-\tfrac1d\right)\log n
                    -C\sqrt{\log n}+O_d(1),
 \tag{3}
\]
which tends to positive infinity for every fixed \(C\). Thus no
coupling of the entire empirical read-in law to the nonatomic canonical
Gaussian law can supply that near-root \(L^2\) parameter error.
Embedding the finite rows as step functions changes neither marginal
law, so it does not evade the bound. Fixed factors of \(\sqrt d\)
from the network input normalization only change its constant. For
\(d\le2\), this particular lower bound does not rule out the target
scale, as the source correctly confines its conclusion to \(d>2\).

For the second claim, let \(X_i=\Psi(A_i)-\mathbb E\Psi(G)\)
be independent centered Hilbert-valued random variables. Interpret the
expectation in the usual Bochner sense; the feature map is measurable and
its finite second moment gives all needed integrability. Expanding the
squared norm gives
\[
 \mathbb E\left\|\frac1n\sum_iX_i\right\|_H^2
 =\frac1{n^2}\sum_i\mathbb E\|X_i\|_H^2
       +\frac1{n^2}\sum_{i\ne j}\mathbb E\langle X_i,X_j\rangle_H.
 \tag{4}
\]
Independence and centering make each cross term zero. Cauchy--Schwarz
justifies its integrability. Identical marginal laws reduce the first
sum to \(n^{-1}\mathbb E\|\Psi(G)-\mathbb E\Psi(G)\|_H^2\),
which is exactly the source's functional-averaging identity.

Consequently slow transport of an entire atomic law and root-width
averaging of a fixed feature observable coexist. The network's zero
initial readout is an especially direct example: its initial prediction
error is zero despite the positive parameter-transport lower bound.
Neither calculation controls an adaptively trained nonlinear predictor.
The source therefore identifies a limitation of one finite-width use
of common-space parameter stability, while leaving the requested
prediction theorem unresolved.
