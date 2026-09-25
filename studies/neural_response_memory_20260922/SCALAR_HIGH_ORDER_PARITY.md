# Readout-sign parity of the scalar hierarchy

2026-09-25. Scoped theory and descriptive check for the canonical finite-width
model. The parity identities and zero-readout reduction below are exact. The
table summarizes only previously saved initialization tensors; no coefficient
generation, training, new GPU computation or modification of frozen sources
was performed. No observed training outcome is used in the proof.

## 1. Coordinate involution and the directional operators

Fix width n, the hidden matrices W=(W1,W2,W3), all input rows, and the
canonical parameter mobility B, equal to n on W1 and c and to 1 on W2,W3.
Let theta=(W,c). Define the linear orthogonal involution

    S(W,c)=(W,-c),    S^T=S,    S^2=Id.

The hidden features h3(W,u) do not depend on c, and

    f_theta(u)=c^T h3(W,u)/n.

Consequently f_(S theta)(u)=-f_theta(u) for every input, training or passive.
Differentiation with respect to theta gives

    S grad f_u(S theta)=-grad f_u(theta),
    grad f_u(S theta)=-S grad f_u(theta).

Since B commutes with S, each training direction g_i=B grad f_i obeys

    g_i(S theta)=-S g_i(theta).                         (1)

Now let a smooth scalar parameter observable A have parity sigma in {+1,-1}:
A(S theta)=sigma A(theta). Its gradient satisfies
grad A(S theta)=sigma S grad A(theta). Therefore

    (D_i A)(S theta)
      = grad A(S theta)^T g_i(S theta)
      = (sigma S grad A(theta))^T (-S g_i(theta))
      = -sigma (D_i A)(theta),                         (2)

where D_i=g_i dot grad. Every D_i reverses parity. This argument includes
the theta dependence of g_i; it does not replace g_i by a fixed direction.

Define T1_a=f_a and T(j+1)_(a1,...,aj,b)=D_b Tj_(a1,...,aj). Applying (2)
componentwise and inducting on j yields, with every index held fixed,

    Tp(W,-c)=(-1)^p Tp(W,c),    p>=1.                 (3)

No differentiation indices were interchanged. Thus the identity applies to
the actual ordered hierarchy, including repeated indices, and to every
passive-query tensor with training directions on the other axes.

In particular T2,T4,T6 are even in c, whereas T1,T3,T5 are odd. At c=0,

    T1=T3=T5=0.                                      (4)

Parity does not force any of T2,T4,T6 to vanish. For example the canonical
kernel formula immediately gives T2_ab=h3_a^T h3_b/n at c=0, because every
backward field delta is then zero. Parity alone gives no sign, size or
stability information for the higher even tensors.

## 2. A stronger finite polynomial statement

At fixed W, f_i is linear in c. Its derivatives with respect to W are
linear in c, while its derivative with respect to c is independent of c.
Since B is constant, each D_i can therefore be written as

    D_i = A_i(W,c) dot partial_W + b_i(W) dot partial_c,

where A_i(W,c) is homogeneous of degree one in c. If P_d(W,c) is homogeneous
of degree d in c, its first contribution under D_i has degree d+1, and its
second has degree d-1 (or is zero when d=0). Starting from degree-one f,
induction proves the exact finite decomposition

    Tp(W,c) = sum_(0<=d<=p, d=p mod 2) P_(p,d)(W,c),  (5)

where P_(p,d) is homogeneous of degree d in c. Its coefficient functions
are smooth in W. Some of these homogeneous components may be zero.

In particular T5 contains only degrees 1,3,5, and T6 only degrees 0,2,4,6.
For fixed W and a fixed readout direction cbar, (5) implies

    T_(2k+1)(W,epsilon cbar)=O(epsilon),
    T_(2k)(W,epsilon cbar)=T_(2k)(W,0)+O(epsilon^2)

as epsilon tends to zero, in any fixed finite-dimensional tensor norm.
The constants depend on W, cbar, width, data and order. This is not a
width-uniform estimate: the canonical width-dependent initialization also
changes W and the dimension of c. The stored canonical readout has component
standard deviation 1/n, but that fact and parity alone do not establish any
particular normalized tensor limit as n increases.

## 3. Exact redundancy of an odd terminal order at zero readout

The order-P truncation freezes TP at its initialized value and evolves

    Tj' = T(j+1):v,    j<P,    v=-2(T1-y)/M,          (6)

where the contraction is over the last tensor index. Suppose c(0)=0 and
P=2k+1 is odd. By (4), TP(0)=0; since the truncation freezes TP, it remains
zero. Equation (6) then makes T(P-1)'=0. The equations for T1,...,T(P-2)
are exactly those of the order-(P-1) truncation with the same initialization.

Both are finite polynomial ODEs, hence locally Lipschitz. Uniqueness on
their common interval of existence proves equality of their retained lower
components. Appending the identically zero TP to the lower-order solution
also solves the larger system, so the reduction is exact, not asymptotic.
The same proof applies to passive tensors and outputs driven by that common
v. If a first downward training-loss crossing exists, its time and passive
outputs agree as well.

Thus, at exactly zero initial readout, P3 reduces to P2 and P5 reduces to
P4. The actual saved canonical readouts are nonzero, so their P5 and P4
systems are not identical. Small initial T5 suggests a small *initial forcing
of T4*, not equality or a guaranteed small endpoint discrepancy.

This zero-readout degeneracy belongs to the frozen-terminal truncation.
It is not a statement that the odd tensors stay zero in dense training.
At c=0, the dense readout velocity is

    c'(0)=(2/M) sum_i y_i h3_i,

which generally does not vanish. The exact dense hierarchy also gives

    T5'(0)=T6(0):(2y/M),

which parity does not force to be zero. An order-six closure retains this
initial source for T5; that fact alone does not imply improved stability or
accuracy. In particular it does not explain or prove any observed P6
instability. Finite truncation need not preserve all constraints of actual
network observables, including positive semidefiniteness of T2.

For completeness, c -> -c alone is not a symmetry of fixed-label training:
f-y transforms to -f-y, not -(f-y). Simultaneously transforming y -> -y does
give equivariance, by (1). The coefficient parity requires no transformation
of labels, because labels do not enter initialized tensors or D_i.

## 4. Why small T5 initially is not a long-time error estimate

In P5, T5 is a fixed coefficient, so integration of its T4 equation yields
the exact identity

    T4(t)-T4(0)=T5(0):z5(t),    z5(t)=integral_0^t v5(s) ds.

Consequently, for the ordinary Euclidean/Frobenius norms,

    ||T4(t)-T4(0)||_F <= ||T5(0)||_F ||z5(t)||_2.     (7)

Small initial coefficients do not control accumulated signed residuals z5.
The changed T4 also feeds T3,T2 and f, altering the residual and future
evolution. Endpoint comparison at each model's own fitting time introduces
another sensitivity that initial tensor norms do not bound.

A conditional finite-time perturbation estimate makes the gap explicit.
Augment P4 with a constant T4 coordinate and write

    X=(T1,T2,T3,T4),
    F4(X)=(T2:v,T3:v,T4:v,0).

Then P4 satisfies X4'=F4(X4), while P5 satisfies
X5'=F4(X5)+(0,0,0,T5(0):v5). Both have the same initial X. Suppose both
solutions exist on [0,T] and F4 is L-Lipschitz on a ball containing their
paths. Such a finite L exists for any fixed bounded pair of paths because
F4 is polynomial. The integral equations, the contraction estimate used in
(7), and the scalar integrating-factor inequality give

    ||X5(t)-X4(t)||
      <= ||T5(0)||_F integral_0^t exp(L(t-s)) ||v5(s)||_2 ds,  t<=T. (8)

One can verify the last step directly: the norm difference is bounded by
the integral of L times itself plus ||T5(0)||_F||v5||; multiplying the
corresponding scalar comparison equation by exp(-Lt) and integrating gives
(8). Neither the exponential factor nor the residual integral is controlled
by parity. This note supplies no useful all-time, large-width or fitted-
endpoint bound. Tensor entries of different ranks also enter different
contractions, so raw norm ratios are descriptive, not dynamical error bars.

## 5. Descriptive initialization check, no new experiment

Read only the already saved training tensors in
`data/generated/neural_response_memory_20260922/scalar_high_order_training01/`
for seeds 20260920 and 20260927. Both records specify width2048, M=8, three
hidden tanh layers, `quadrant_alternating`, GPU1 and float64. Every saved
Tp has shape (8,)*p and finite entries. The actual SHA256 values of the
coefficient archive, configuration and result match each saved manifest.

Define entry RMS=sqrt(mean(Tp^2)), Frobenius norm=sqrt(sum(Tp^2)), and maximum
entry magnitude=max(abs(Tp)); every stored ordered entry is counted.

| Seed | Tensor | Entry RMS | Frobenius norm | Maximum magnitude |
|---|---|---:|---:|---:|
| 20260920 | T1 | 1.8821832828e-6 | 5.3236182507e-6 | 2.9537674783e-6 |
| 20260920 | T2 | 0.14332042074 | 1.1465633659 | 0.16967748489 |
| 20260920 | T3 | 6.1484017678e-6 | 1.3912245067e-4 | 1.5039132259e-5 |
| 20260920 | T4 | 0.26231983557 | 16.788469477 | 0.37859826362 |
| 20260920 | T5 | 3.6641425790e-5 | 6.6328065659e-3 | 1.1392293558e-4 |
| 20260920 | T6 | 0.32406643421 | 165.92201432 | 1.2376374604 |
| 20260927 | T1 | 1.4722392080e-6 | 4.1641213101e-6 | 2.0213172444e-6 |
| 20260927 | T2 | 0.13745521229 | 1.0996416983 | 0.16775034108 |
| 20260927 | T3 | 5.2057308138e-6 | 1.1779224190e-4 | 1.2374277036e-5 |
| 20260927 | T4 | 0.24865991684 | 15.914234677 | 0.38709349333 |
| 20260927 | T5 | 3.2135819864e-5 | 5.8172047731e-3 | 1.1117408910e-4 |
| 20260927 | T6 | 0.30656274932 | 156.96012765 | 1.3273079189 |

The entry-RMS ratios T5/T4 are 0.00013968225357 and 0.00012923602756.
These initialized arrays exhibit the small odd coefficients compatible with
the exact parity mechanism. They neither verify a c=0 identity numerically
(the readouts are nonzero) nor prove long-time closeness, monotone order
improvement or a cause of instability. No trajectory artifact was read for
this note, beyond the supervisor's scoped statement of the motivating question.

### Actual artifact hashes

All paths below are relative to the shared repository root.

| Seed | File within scalar_high_order_training01/seedSEED | SHA256 |
|---|---|---|
| 20260920 | coefficients.npz | 48d194f9c79636a864beab9d20ec946582b985a37ba8992495e1df70f6d4ed26 |
| 20260920 | configuration.json | 16a0d5db7496782e1c94d36813e7c69d1b55fcdd93f5f636c8d11053148d1ec0 |
| 20260920 | result.json | b73288ad8b7924c7650074c31c2580c43c90456b42950cf8961894e444d1c6b5 |
| 20260920 | manifest.json | f8b1f1ecea998555f30e40aab589f23e305018a8aa13fe10ed376849bff23c61 |
| 20260927 | coefficients.npz | a1e09ff9e849ff8d0c463251498a50c3413d60f81de30ffa011e73d3fec6d2a2 |
| 20260927 | configuration.json | 62deea6b0bab3a41c88067c2027e3d0997e576247e6e8b85d09a8f53dfa66ad5 |
| 20260927 | result.json | b3c7626c35ff942a7e57379b51895a66e0de79ee7d207ed053843be522779bc6 |
| 20260927 | manifest.json | d0960df5403950db0f5f4789f038d72141be158a09c816f6622d29d280ae6d74 |

Both archived manifests and actual current source hashes agree on:

- `scalar_aggregate_engine.py`:
  `e765083bbf50e536a06dfc820da0a64a53f1b2580cd0c03ef56b873c78a231eb`.
- `scalar_high_order_initialization.py`:
  `3faea59d7de150edccfb01d936b8525a29324269af2810996207a28858fe6d56`.

The saved full-parameter initialization hashes are
`d35aa2cc3a8d3d0f2868ce3f87df0c5ccac48736fa5c2d11845f5e92b949e727`
and `b42dfabc1fcf2c5e243667edd710201243f0b3cef2e68c58624a9bdb6ced8690`.
They are reported from the saved results, not recomputed by redrawing networks.

### Reproduction of this read-only check

From `/home/amir/Codes/PDE`, use `/home/amir/miniconda3/bin/python` with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
PYTHONDONTWRITEBYTECODE=1`. The executed calculation was equivalent to:

```python
import hashlib, json
from pathlib import Path
import numpy as np

base = Path('data/generated/neural_response_memory_20260922/scalar_high_order_training01')
for seed in (20260920, 20260927):
    folder = base / f'seed{seed}'
    manifest = json.loads((folder / 'manifest.json').read_text())
    for name, digest in manifest['outputs'].items():
        assert hashlib.sha256((folder / name).read_bytes()).hexdigest() == digest
    with np.load(folder / 'coefficients.npz') as saved:
        for p in range(1, 7):
            value = saved[f'T{p}']
            assert value.shape == (8,) * p and np.isfinite(value).all()
            print(seed, p, np.sqrt(np.mean(value * value)),
                  np.linalg.norm(value.ravel()), np.max(np.abs(value)))
```

The actual checks exited successfully for both seeds. This retained analysis
is a complete author derivation and descriptive artifact check, not a fresh
independent review or a promoted result. Its scientific inputs were limited
to the assigned canonical definitions/current initializer and the two named
initialization artifacts and their metadata; no linked artifact was fetched.
