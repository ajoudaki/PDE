# Generalized causal producer and multisample driver checks

2026-10-07. Bounded implementation audit, not a reproduction or review of the
scientific campaign. This report persists the generalized producer's completed
checks and the subsequent static/deterministic driver audit. No campaign data
were inspected, no research cohort was launched, and no favorable dataset was
selected. Numerical sources were not edited during the frozen driver audit.

The generalized equations, dense normalization, passive-force exclusion, and
initial-curvature formulas passed the checks below. One driver validation
defect remains: modes intended for the other implementation silently run full
dynamics. The intended, correctly paired controls remain valid. A separate
reporting qualification concerns physical versus normalized-time curvature.

## Frozen source identification

| Source | SHA-256 |
|---|---|
| `causal_panel_simulator.py` | `e3eec0c1e7f7692460c804dedc1cce2476324a9c2013b35123efe5db7afd522a` |
| Frozen dependency `causal_population_simulator.py` | `4431bef401087ca0e0f0bd465f1d31d88e7486403ec18d331eab8bbc035e5d76` |
| `multisample_experiment.py` | `eb58b62ca466649989067cd1287aa199b99b41899b59536cec02baa186c78b2d` |

The original simulator was never modified. An independent producer check
identified covariance-diagnostic temporary arrays absent from the first memory
estimate. Before the final producer freeze, the estimate was augmented by four
additional \([p(K+1)]^2\) float64 arrays. This changed the reported memory
budget, not the scientific equations or simulated fields. All three hashes
above were checked again after the driver audit and were unchanged.

Scientific reading was restricted to these implementation sources and the
assigned causal-system specification. No other study or research history was
used. The checks below do not establish population convergence, dense-width
accuracy, full-horizon stability, or scientific agreement in the campaign.

## Generalized causal equations and indexing

The producer takes \(m\) labels and \(p\ge m\) normalized input rows in
\(\mathbb R^d\). Rows \(0,\ldots,m-1\) train; the remaining rows are passive.
Its Euler learning factor is exactly \(2\Delta t/m\).

For \(N\) quadrature particles and \(K\) steps, the retained tangent arrays at
step \(k\) have shapes

\[
\text{lower}[k]:[N,m,mk],\qquad
\text{upper}[k]:[N,m,m(k+1)].
\]

The current lower tangents evaluate all \(p\) samples against active primitive
coordinates. Their stored active-evaluation history supplies subsequent
recursions. Every covariance and response history has shape
\([K+1,K+1,p,p]\), with the evaluated sample before the source sample.
The input root has shape \([N,d]\), and its panel is formed by multiplication
with the supplied input vectors. The full input Gram enters lower updates,
their tangents, replay, and the kernel diagnostic.

All learned writes and the readout sum only over the first \(m\) samples.
Every passive source column of \(R^h\) vanishes. For \(R^\delta\), active
source columns are retained for every evaluated sample, and every passive
sample also has its current direct diagonal

\[
R^\delta_{aa}(k,k)=
\frac1N\sum_{i=1}^Nw_i^k\tanh''(z_{2,a,i}^k),\qquad a\ge m.
\]

These passive diagonals enter only their respective passive backward fields.
They do not create passive training forces. Matmul implementations of the
history and tangent contractions preserve the original index contractions.

The first built-in comparison used the same seed and configuration as the
frozen two-sample producer, with \(N=31,K=4,\Delta t=0.2\). Outputs,
residuals, all feature/response Grams, response histories, and returned fields
agreed within \(1.11\times10^{-16}\). This is equivalence to roundoff for
that program, not a claim of bitwise equality for all numerical contractions.

The built-in generalized panel has \(m=4,p=7,d=3,N=31,K=4\), simulator seed
17, and \(\Delta t=0.2\). It checks full dynamics, removal of both reciprocal
directions, and removal of both learned middle-memory directions. Results:

| Check | Maximum error |
|---|---:|
| Frozen-coefficient replay | \(0\) |
| Centered primitive-response probes | \(1.233\times10^{-12}\) |
| Exact Euler readout-history identity | \(6.94\times10^{-18}\) |

The readout identity tested is

\[
f_a^k=\frac{2\Delta t}{m}
       \sum_{j<k,b<m}C^2_{ab}(k,j)c_b^j.
\]

Passive probes leave active predictions bitwise unchanged. The built-in test
also covers zero-label singular histories, zero steps, no-passive panels,
\(m=1\), and the preallocation memory guard.

An additional independent check covered nonzero labels at \(m=1,8,16\):

| \((m,p,d,N)\) | Largest primitive-probe error |
|---|---:|
| \((1,4,2,17)\) | \(1.06\times10^{-12}\) |
| \((8,11,4,23)\) | \(1.27\times10^{-12}\) |
| \((16,19,5,31)\) | \(7.86\times10^{-13}\) |

These used three steps of size 0.2, so physical horizon 0.6. Frozen replay
was exact, all Grams independently recomputed from returned fields agreed
within \(1.67\times10^{-16}\), and the readout-history identity agreed within
\(6.94\times10^{-18}\). Both primitive families were tested for the last
active sample and each of three passive samples. Same-time response diagonals
were correct for all samples, and passive probes again left active outputs
bitwise unchanged.

This passive-exclusion check concerns formal primitive perturbations with
population coefficients frozen, as required by the response definition. It
does not assert identical finite-quadrature random realizations after changing
the whole panel and rerunning the Gaussian factorization.

## Dense physical flow and initial curvature

The dense driver uses \(n\) neurons, with
\(z_{1,a}=Av_a\), \(h_{1,a}=\tanh z_{1,a}\),
\(z_{2,a}=Wh_{1,a}\), \(h_{2,a}=\tanh z_{2,a}\), and
\(f_a=w^\top h_{2,a}/n\). Only training outputs enter
\(c_a=y_a-f_a\). With \(\delta_{2,a}=g(z_{2,a})\odot w\) and
\(\delta_{1,a}=g(z_{1,a})\odot W^\top\delta_{2,a}\), its velocities are

\[
\dot A=\frac2m\sum_{a<m}c_a\delta_{1,a}v_a^\top,
\qquad
\dot W=\frac2{mn}\sum_{a<m}c_a\delta_{2,a}h_{1,a}^\top,
\qquad
\dot w=\frac2m\sum_{a<m}c_ah_{2,a}.
\]

All three factors match the canonical physical flow. Its parameter-block
kernel and loss derivative are consistent with
\(\dot f=(2/m)Kc\) and
\(d(\|c\|^2/m)/dt=-4c^\top Kc/m^2\).

At zero initial readout, both hidden velocities vanish. Write
\(G=W(0)\) and
\(Q=\dot w(0)=(2/m)\sum_{b<m}y_bh_{2,b}(0)\). Differentiating the
physical velocities gives

\[
\begin{aligned}
A''(0)&=\frac2m\sum_{b<m}y_b
 \left[g(z_{1,b}(0))\odot G^\top
        (g(z_{2,b}(0))\odot Q)\right]v_b^\top,\\
W''(0)&=\frac2{mn}\sum_{b<m}y_b
       (g(z_{2,b}(0))\odot Q)h_{1,b}(0)^\top.
\end{aligned}
\]

The two factors \(2/m\), one inside \(Q\) and one in the hidden update,
are both present in `initial_curvature`. Residual derivatives multiply the
zero initial hidden force and do not add another term. If
\(J_{\ell,a}=h_{\ell,a}''(0)\), then

\[
\begin{aligned}
J_{1,a}&=g(z_{1,a}(0))\odot A''(0)v_a,\\
J_{2,a}&=g(z_{2,a}(0))\odot
       [W''(0)h_{1,a}(0)+GJ_{1,a}],\\
(C^\ell_{ab})''(0)&=
       [J_{\ell,a}^\top h_{\ell,b}(0)
        +h_{\ell,a}(0)^\top J_{\ell,b}]/n.
\end{aligned}
\]

The code evaluates these formulas. `frozen_middle` removes \(W''(0)\).
The anchored-affine mode has the same initial curvature as full tanh,
because every term involving activation curvature also contains a vanishing
initial hidden velocity.

The driver self-test at \(m=4,n=19\) passed with output-derivative error
\(2.37\times10^{-13}\), loss-derivative error \(1.45\times10^{-13}\),
initial-curvature error \(3.47\times10^{-18}\), and zero passive-exclusion
error. Additional checks at \(m=4,8,16,n=23\), for all three dense modes,
gave output-derivative error at most \(3.96\times10^{-13}\). Changing only
passive directions left all parameter velocities bitwise unchanged. Independent
centered short-time RK4 checks of Gram curvature, at times \(\pm0.001\),
agreed within \(1.05\times10^{-9}\). A separate centered-RHS check at
\(n=19\), all three training sizes and modes, agreed within
\(3.47\times10^{-18}\).

## Geometry, time convention, and wrapper bookkeeping

The fixed driver dataset has \(d=8\), \(m=4,8,16\), and exactly four passive
inputs, so \(p=m+4\). It constructs all 16 training directions from fixed
centers and geometry seed 6201, normalizes them, and uses a nested first-\(m\)
prefix. Labels use a deterministic mixed-sign, unequal-magnitude rule. The
first three passive inputs are normalized combinations of the first four
training inputs; the fourth is a fixed normalized direction. No passive label
is created. All inspected norms differed from one by at most
\(1.12\times10^{-16}\). A passive direction need not be outside the training
span for every value of \(m\); this audit does not assign that interpretation.

The saved normalized time is \(\tau=2t/m\). The driver sets physical
\(\Delta t=h m/2\) from `normalized_step=h`; consequently the causal
learning step \(2\Delta t/m=h\) matches the dense Euler coefficient. With
\(h=0.4\), the intercepted wrapper calls have physical steps
\(0.8,1.6,3.2\) for \(m=4,8,16\), respectively, and 48 steps. Their
normalized horizon is 19.2, and their physical horizons differ across \(m\).
The interception did not execute those trajectories.

`initial_curvature` is a derivative with respect to physical \(t\). Thus a
quadratic baseline may use \(t^2 C''_t(0)/2\). If plotted using
\(\tau\), the curvature must first be multiplied by \((m/2)^2\):

\[
C''_\tau(0)=(m/2)^2C''_t(0).
\]

The argument called `n` in the driver is a dense width for `dense` and a
quadrature particle count for `causal`. The causal wrapper passes it as
`population_size`, not a neural matrix dimension. Their equal numerical values
do not identify the two approximations or couple their random initializations.

The causal feature-motion reconstruction is the exact empirical identity

\[
\mathbb E[(h_a^k-h_a^0)^2]
=C_{aa}(k,k)+C_{aa}(0,0)-2C_{aa}(k,0).
\]

Its indexing is correct for both layers. The driver includes full two-time
histories and responses in causal outputs, whereas the dense outputs contain
same-time Grams and parameter-block kernels. This audit does not equate those
different output arrays.

## Control validity and the remaining dispatch defect

| Implementation | Intended mode | Implemented change |
|---|---|---|
| Dense | `full` | All three physical parameter blocks train. |
| Dense | `frozen_middle` | The middle matrix velocity is zero. |
| Dense | `affine_gates` | Forward features use their initialized affine maps, and backward gates use their corresponding fixed derivatives. |
| Causal | `full` | All learned-memory and reciprocal terms remain. |
| Causal | `no_middle` | Both learned middle-memory directions are disabled. |
| Causal | `no_reciprocal` | Both reciprocal corrections are disabled and the modified circuit's tangents are recomputed. |

The causal reciprocal ablation is a change to the causal circuit; it is not
automatically a dense-network gradient control. The producer correctly marks
its usual kernel diagnostic as not a gradient-kernel claim for these modified
memory/reciprocal settings. The dense affine control is a different forward
model with matched fixed derivatives, not an intervention that merely deletes
a curvature source from a completed full-model trajectory.

The CLI accepts all listed mode names for both implementations, but it does
not validate their pairing. Therefore:

- Dense `no_middle` and `no_reciprocal` silently execute full dynamics. Their
  parameter velocities were confirmed bitwise identical to `full` at the
  tested nonzero-readout states.
- Causal `frozen_middle` and `affine_gates` silently execute full dynamics,
  because neither disables a causal switch.

This is a control-label validation defect. A run with one of these unsupported
pairs cannot support its nominal ablation interpretation. Runs using the
intended pairings in the table are unaffected by this defect. It was reported
to the campaign coordinator immediately; the frozen driver was not edited.
This audit did not inspect campaign records to determine which pairs were run.

## Commands, deterministic limits, and memory budget

The two built-in commands were run from
`studies/transparent_learning_dynamics_20261007`:

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python causal_panel_simulator.py --self-test
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python multisample_experiment.py selftest
```

The producer built-in tests used \(N\le31,K\le4,T\le0.8\). Its initial
scientific-array tests preceded the final memory-estimate-only amendment; that
amendment changes no tested equation or field. The final estimator itself was
executed to produce the memory table below. No numerical-source changes
followed the final hash.

The additional generalized tests ran in an isolated `python -B` process with
the same one-thread environment. Their reproducible setup was:

```python
for m, p, d, n in ((1, 4, 2, 17), (8, 11, 4, 23), (16, 19, 5, 31)):
    rng = np.random.default_rng(123 + m)
    vectors = rng.normal(size=(p, d))
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)
    labels = np.linspace(-.12, .17, m) if m > 1 else np.array([.13])
    result = simulate_population(labels, dt=.2, steps=3, population_size=n,
        seed=37, input_vectors=vectors, return_fields=True)
```

At probe time index 1, centered perturbations of size \(10^{-5}\) were applied
to sources \(m-1,m,\ldots,p-1\), for both primitive families. Gram checks
used `np.einsum('ina,jnb->ijab', fields, fields)/n` on the returned layer
fields. These checks did not write output files.

Additional dense checks used `dataset(m)`, \(n=23\), seed \(471+m\), and a
readout `np.linspace(-.11,.17,23)` for nonzero-state derivative checks, for
\(m=4,8,16\). Centered directional increments were \(10^{-5}\). The
curvature check returned to zero readout and took one RK4 step to each of
\(t=\pm0.001\), for `full`, `frozen_middle`, and `affine_gates`. The
independent centered-RHS curvature check used \(n=19\), seed 39, and the
same three training sizes and modes. Wrapper argument checks replaced the
simulator with an intercept that stopped before execution; neither long-horizon
`dense()` nor `causal()` was allowed to execute during this audit.

For \(m=16,p=20,d=8\), `return_fields=False`, the final producer estimates:

| Particles \(N\) | Steps \(K\) | Estimated arrays, MiB | Packed tangent history alone, MiB |
|---:|---:|---:|---:|
| 256 | 32 | 834.988 | 544.5 |
| 256 | 48 | 1654.777 | 1200.5 |
| 512 | 32 | 1640.738 | 1089.0 |
| 512 | 48 | 3240.277 | 2401.0 |

The packed tangent history alone uses \(8Nm^2(K+1)^2\) bytes. These are
array estimates with explicit working and covariance-diagnostic allowances,
not observed peak process memory; interpreter/BLAS overhead is excluded.
The generic producer defaults to a 3072 MiB guard, whereas the campaign wrapper
explicitly requests 11500 MiB and a 12 GiB process address-space limit.
The latter is an execution budget, not an accuracy claim.

No full scientific cohort, large-population memory allocation, campaign timing,
or complete dense-versus-causal reproduction is certified by this report.
