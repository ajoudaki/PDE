# Cubic scalar initializer and decoder: implementation design and audit

2026-09-30. Scoped derivation by the `cubic_decoder_design` subagent. This
is an implementation-level algebra check, not an independent review of the
small-amplitude theorem or a training experiment. The supervisor selected
the same finite Gaussian initialization as the dense width-1024 reference
for the primary experiment; the initial block-quadrature proposal is therefore
secondary. No root-owned source files were edited.

Scientific inputs read completely:

- `KERNEL_SCALAR_ROUTE_20260930.md`, SHA256
  `3dec09ff84227b213e0a2bedc35a514672c929301eea1c2dde29078825236c9c`.
- `cubic_scalar_algebra_check_20260930.py`, SHA256
  `e1b2f5abb8ad2657801ce87c454517ecaa508c940582f4bc81fa774cd3985eed`.

Shared instructions and `solve-math-rigorously` were also read. No other
study research inputs were inspected during the derivation. The later
module and saved-experiment audits, with their expanded supervisor-assigned
input scopes, are recorded below.

## Finite dense initialization

Let training inputs `U` have shape `(m,din)`, input weights `w` shape
`(n,din)`, and middle weights `W` shape `(n,n)`, with `W[o,i]` mapping
first-layer coordinate `i` to second-layer coordinate `o`. The same actual
`W` must be used in forward and transpose contractions. Define

```python
p = np.tanh(U @ w.T)           # (m,n)
H = np.tanh(p @ W.T)           # (m,n)
q = 1 - p*p
d = 1 - H*H
gamma = d[:,None,:] * H[None,:,:]          # (a,b,o)
beta = (gamma @ W) * q[:,None,:]          # (a,b,i)
inputGram = U @ U.T
pGram = p @ p.T / n
K0 = H @ H.T / n
S = (inputGram[:,None,:,None]
     * np.einsum('abi,cdi->abcd', beta, beta) / n
     + pGram[:,None,:,None]
     * np.einsum('abi,cdi->abcd', gamma, gamma) / n)
```

Here `gamma[a,b] = d_a H_b` and `beta[a,b] = q_a W.T(d_a H_b)`
in column-vector mathematical notation. The array multiplication is
`gamma @ W`, not `gamma @ W.T`. The two normalized inner products in the
second term of `S` are evaluated separately and then multiplied.

The paired matrix `S.reshape(m*m,m*m)` is positive semidefinite up to
floating-point roundoff. Its first term is a Gram matrix of `beta_ab`
tensored with `u_a`. Its second term is the entrywise product of the
lifted positive semidefinite matrix `pGram[a,c]` with the `gamma` Gram
matrix. Neither symmetry nor positivity permits interchanging the two
positions within a pair.

## Only two query tensor slices are needed

For a batch of queries `X`, form `px,Hx,qx,dx` by the same initialization
map. Define two tensors, each of shape `(number_of_queries,m,m,m)`:

\[
A_{xabc}=S_{(a,x),(b,c)},\qquad
B_{xabc}=S_{(x,a),(b,c)}.
\]

Their vectorized construction is

```python
gammaA = d[None,:,:] * Hx[:,None,:]       # (x,a,o)
betaA = (gammaA @ W) * q[None,:,:]
gammaB = dx[:,None,:] * H[None,:,:]       # (x,a,o)
betaB = (gammaB @ W) * qx[:,None,:]
A = (np.einsum('xai,bci->xabc', betaA, beta) / n
     * inputGram[None,:,:,None]
     + np.einsum('xai,bci->xabc', gammaA, gamma) / n
     * pGram[None,:,:,None])
B = (np.einsum('xai,bci->xabc', betaB, beta) / n
     * (X @ U.T)[:,None,:,None]
     + np.einsum('xai,bci->xabc', gammaB, gamma) / n
     * (px @ p.T / n)[:,None,:,None])
kx = Hx @ H.T / n
```

The decoder tangent term needs `S[(x,b),(a,c)]`, which is a permutation
of `B`; it needs no additional query tensor. Changing dummy indices in
the term with `P[a,c,b]` gives the single combined coefficient

\[
C_{xabc}=A_{xabc}+B_{xabc}+B_{xbac}+B_{xcab}.
\]

```python
Cquery = A + B + B.transpose(0,2,1,3) + B.transpose(0,2,3,1)
Ctrain = (S.transpose(1,0,2,3) + S
          + S.transpose(0,2,1,3) + S.transpose(0,2,3,1))
```

Consequently only `kx,Cquery` are needed for each fixed query batch at
runtime. Initial features and intermediate `A,B` can be discarded. The
initialization can process queries in batches and never forms a tensor
of shape `(m+number_of_queries,)*4`.

## Autonomous state and decoding

Set `alpha=2/m`. Starting from `r=-y`, `z=0`, `J=0`, `P=0`, evaluate

```python
M = alpha**2 * np.einsum('bc,aqbc->qa', J, S)
Nt = alpha**2 * np.einsum('d,b,qdab->qa', z, z, S)
T = np.eye(m) + np.linalg.solve(K0, M)
Khat = T.T @ K0 @ T + Nt
rdot = -alpha * (Khat @ r)
zdot = r
Jdot = np.outer(r, z)
Pdot = np.einsum('a,bc->abc', r, J)
```

This requires positive definite `K0`. An undocumented ridge or
pseudoinverse would change the prescribed model. If a full `J` is
integrated, monitor `J+J.T-np.outer(z,z)`: the identity is exact for the
continuous ODE but is not automatically preserved by every integrator.
Alternatively store only the upper-triangular entries of the skew matrix
`Omega`, reconstruct `J=outer(z,z)/2+Omega`, and evolve
`Omega'=(outer(r,z)-outer(z,r))/2`.

For any requested coefficient batch,

```python
f_cubic = -alpha * (
    kx @ z + alpha**2 * np.einsum('abc,xabc->x', P, Cquery))
f_cubic_train = -alpha * (
    K0 @ z + alpha**2 * np.einsum('abc,xabc->x', P, Ctrain))
f_query = f_cubic + kx @ np.linalg.solve(K0, y+r-f_cubic_train)
```

At a training alias `kx` is exactly the corresponding row of `K0`, so
the final line returns `y+r` up to floating-point error. Differentiating
the cubic readout and using `J+J.T=zz.T` gives
`-alpha*(K0+M+M.T+Nt)@r` at training points. The completion restores
the contribution of `M.T@solve(K0,M)` through the alias correction.

The exact vector field stops at `r=0`, including `P`. This is a useful
deterministic check without running a training trajectory.

For `m=1`, the state can collapse further to one scalar, with
`K0=kappa`, `S=s`, `J=z*z/2`, `P=z**3/6`:

```python
zdot = -y - 2*kappa*z - (16/3)*s*z**3 - (8/5)*(s*s/kappa)*z**5
f_query = (-2*kx*z - (4/3)*z**3*(A+3*B)
           - (8/5)*(kx*s*s/(kappa*kappa))*z**5)
```

The one-state formula is algebraically exact for this surrogate; its
accuracy for the original system retains the small-label qualification.

## Block quadrature variant

For block size `k`, each quadrature node contains `w0` of shape `(k,din)`
and `G` of shape `(k,k)`. With positive weights `omega[l]` summing to one,
replace every finite bracket by

\[
\langle v,w\rangle_Q=\sum_l\omega_l\,v_l^T w_l/k.
\]

For equal weights this is the dot product across flattened block and
coordinate indices divided by `number_of_blocks*k`. Form block-local
`gamma[l,a,b,o]=d[l,a,o]*H[l,b,o]` and
`beta[l,a,b,i]=q[l,a,i]*sum_o gamma[l,a,b,o]*G[l,o,i]`.
The training and query formulas above then apply using the weighted
block bracket. The second term remains
`bracket(p_a,p_c)*bracket(gamma_ab,gamma_cd)`, not an average of
same-block products. This construction preserves the paired Gram
positivity with positive quadrature weights.

For Gaussian input weights of variance one and Gaussian block entries
of variance `1/k`, a Gaussian node has dimension `k*din+k*k`, which is
24 for `k=4,din=2`. A scrambled Sobol initializer can use an inverse
normal transform of 4096 points; its numerical integration error still
needs a declared convergence check. Nodes are discarded after forming
the coefficients. This numerical quadrature is not needed by the
supervisor's matched finite-initialization primary comparison.

## Costs at m=9, 128 queries, width 1024

The training backward contractions use about `m*m*n*n = 8.49e7`
multiply-adds. Both query roles use about `2*128*m*n*n = 2.42e9`.
The four query cross contractions add about `4*128*m**3*n = 3.82e8`.
Including query forward features brings the initialization to about
`3.0e9` multiply-adds, or `6.0e9` floating-point arithmetic operations.
These are operation counts, not observed timings.

With batches of 16 queries, each query-role feature array uses 1.125 MiB
in float64. The original dense `W` uses 8 MiB; it need not be retained
by the trained scalar object. Runtime saved arrays have 81 `K0` entries,
6561 `S` entries, 1152 query kernel entries, and 93312 combined query
decoder entries. The last array uses 729 KiB. Storing `Ctrain` adds
6561 entries, or it can be derived from `S` when needed.

The full-`J` ODE has `2m+m*m+m**3=828` coordinates; skew compression
reduces this to `2m+m*(m-1)/2+m**3=783`. Training alone needs 99 or 54,
respectively. A naive training RHS takes `O(m**4)` work, and decoding
all queries takes `O(number_of_queries*m**3)`. The initialization and
saved query coefficient costs must be reported separately from evolving
state counts.

## Executed algebra check

A fresh, inline NumPy calculation used `default_rng(127)`, `m=3`,
`n=12`, seven queries, independent standard-normal input/query arrays
and input weights, and `W=standard_normal((n,n))/sqrt(n)`. It formed
the above slice contractions and separately materialized the full
10-input tensor as a small independent indexing oracle. A random `P`
was contracted both by the combined tensor and by explicit four-level
loops implementing the original decoder. A separate random skew matrix
and `z` gave `J=zz.T/2+Omega`; its training decoder derivative was
compared to the separately contracted cubic kernel. Observed gaps:

| Check | Maximum absolute gap |
| --- | ---: |
| Combined decoder versus explicit original sums | `4.440892098500626e-16` |
| Query-first slice versus full tensor | `1.1102230246251565e-16` |
| Query-second slice versus full tensor | `1.1102230246251565e-16` |
| Training decoder derivative versus cubic kernel | `2.7755575615628914e-17` |

The paired `S` matrix had smallest eigenvalue
`0.00030671175731324395`. The check involved no integration, training,
large-width benchmark, or theorem validation. Its immediate purpose was
to verify the orientation formulas above before checking the actual
implementation.

## Actual module audit

The supervisor subsequently supplied `cubic_scalar_ode.py`, which was
read completely at SHA256
`1e2a99aa61aff986ba96f07b1213784f07f0dd4de33423266360480a3f8d578f`.
**Outcome: no blocking implementation error found.** This is the module's
internal implementation audit, not a promotion review or theorem review.

The initializer uses `gamma @ W` in the backward contraction, divides
each distinct normalized bracket by `n`, and multiplies the separate
first-feature and backward-feature brackets. The matrix reshape and
transpose in `kernel` implement `M[qa]=alpha**2 sum_bc J[bc]S[a,q,b,c]`.
The `N` contraction has the required indices. With `K0=L L.T`, the code
forms `L.T@(I+solve(K0,M))`; its matrix Gram is the desired positive
completion. Reconstruction from the skew entries gives the correct
`J`, its antisymmetric derivative, and `P'=r tensor J`.

Both query roles and their combined permutations agree with the
derivation. `predict` applies the completion using the current residual
and the current cubic training readout. The integration routine keeps
accepted states on partial outcomes. On a target crossing, it locates
the crossing inside the last accepted step and recomputes the entire
state, residual, MSE, and prediction at that interpolated time. Thus the
reported residual and the decoded endpoint refer to the same state.

An independent test used `default_rng(5031)`, width 12, three circle
training inputs at angles `(0,0.63,1.42)`, labels `(0.12,-0.08,0.07)`,
and seven additional random query points. Instead of copying the
module's factored `S` expression, the oracle flattened the actual
parameter-gradient features

\[
\Phi_{ab}=\left(
   \operatorname{vec}(\beta_{ab}u_a^T)/\sqrt n,
   \operatorname{vec}(\gamma_{ab}p_a^T)/n\right)
\]

and formed their ordinary Gram matrix. Its middle component therefore
checks the complete dense matrix parameter normalization independently.
The query tensor was assembled by explicit index loops from that Gram.
The test also evaluated arbitrary skew and third-order states, with no
assumption that they came from a training trajectory.

| Module check | Observed value |
| --- | ---: |
| `S` versus direct parameter-gradient Gram, maximum gap | `1.3877787807814457e-16` |
| Query tensor versus direct Gram slices, maximum gap | `2.7755575615628914e-16` |
| Initial `K0`, maximum gap | `2.7755575615628914e-17` |
| Training alias prediction, maximum gap | `1.2351231148954867e-15` |
| `M`, explicit index-sum gap | `2.168404344971009e-18` |
| `N`, explicit index-sum gap | `8.673617379884035e-19` |
| Positive completion versus expanded formula, maximum gap | `5.551115123125783e-17` |
| Completed kernel minimum eigenvalue | `0.0035323946009217537` |
| Paired `S` minimum eigenvalue | `0.00011965310266957097` |
| Cubic decoder derivative, maximum gap | `8.673617379884035e-19` |
| `J+J.T=zz.T`, maximum gap | `3.7947076036992655e-19` |
| All RHS coordinates at zero residual | exactly zero |

A second check used only the first training input and label, with MSE
target `0.005`, `rtol=1e-10`, `atol=1e-12`, and maximum step `0.05`.
The module reached the target at time `1.2122246756603259`. Its solution
was compared against the one-coordinate polynomial ODE, independently
integrated at tighter tolerances. This was a tiny numerical consistency
check, not the authorized dense-reference empirical campaign.

| Endpoint check | Absolute gap |
| --- | ---: |
| Reported MSE versus target | `0` |
| Reported MSE versus returned residual squared | `0` |
| Residual versus the one-coordinate polynomial identity | `7.42045314083839e-14` |
| `z` versus independent one-coordinate integration | `6.55586696041155e-14` |
| `P=z**3/6` | `3.0627627170543015e-14` |
| Query prediction versus explicit one-coordinate decoder | `7.419065362057609e-14` |
| Training alias | `0` |

No accepted-step loss rise occurred. The check process exited zero.
This confirms the requested orientations, finite dense scaling,
decoder, and endpoint consistency on the exercised cases; it does not
measure large-width speed, establish finite-amplitude accuracy, or
certify every malformed-input path.

Two reporting qualifications are nonblocking. The current implementation
uses three coordinates for `m=1` (`r,z,P`), although the optional
one-coordinate reduction is available mathematically. Its
`coefficient_nbytes` property counts the main coefficient arrays but
omits the small eigenvalue and triangle-index metadata arrays and
Python-object overhead. Runtime numbers should retain these meanings.
For a previously unspecified finite-network query, computing new
coefficients still requires the finite initialization supplied to
`query_coefficients`; the scalar object itself correctly retains none
of those neuron arrays.

The substantive independent oracle can be repeated from the repository
root with this command (NumPy and SciPy required):

```bash
python - <<'PY'
import importlib.util
import sys
import numpy as np
from scipy.integrate import solve_ivp
path = 'studies/structured_full_rank_scalar_20260926/cubic_scalar_ode.py'
spec = importlib.util.spec_from_file_location('audit_cubic', path)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)
rng = np.random.default_rng(5031)
m, n = 3, 12
theta = np.array([0., .63, 1.42])
U = np.c_[np.cos(theta), np.sin(theta)]
X = np.r_[U, rng.normal(size=(7, 2))*.4]
w = rng.normal(size=(n, 2))
W = rng.normal(size=(n, n))/np.sqrt(n)
y = np.array([.12, -.08, .07])
model = mod.initialize(w, W, U, y)
coeff = mod.query_coefficients(w, W, U, X, batch_size=4)
V = np.r_[U, X]
p = np.tanh(V@w.T)
H = np.tanh(p@W.T)
count = len(V)
feature = np.empty((count, count, n*2+n*n))
for a in range(count):
    for b in range(count):
        gamma = (1-H[a]**2)*H[b]
        beta = (1-p[a]**2)*(W.T@gamma)
        feature[a,b] = np.r_[np.outer(beta,V[a]).ravel()/np.sqrt(n),
                                 np.outer(gamma,p[a]).ravel()/n]
flat = feature.reshape(count*count, -1)
S = (flat@flat.T).reshape((count,)*4)
C = np.empty_like(coeff.cubic)
for x in range(len(X)):
    q = x+m
    for a in range(m):
        for b in range(m):
            for c in range(m):
                C[x,a,b,c] = (S[a,q,b,c]+S[q,a,b,c]
                             +S[q,b,a,c]+S[q,c,a,b])
assert np.max(abs(model.response_gram-S[:m,:m,:m,:m])) < 2e-13
assert np.max(abs(coeff.cubic-C)) < 2e-13
state = model.initial_state()
state[model.slices[0]] = rng.normal(size=m)*.05
state[model.slices[1]] = rng.normal(size=m)*.1
state[model.slices[2]] = rng.normal(size=model.area_count)*.01
state[model.slices[3]] = rng.normal(size=m**3)*.002
r,z,J,P = model.unpack(state)
K,M,N = model.kernel(z,J)
Mo, No = np.zeros_like(M), np.zeros_like(N)
for q in range(m):
    for a in range(m):
        for b in range(m):
            for c in range(m):
                Mo[q,a] += model.alpha**2*J[b,c]*S[a,q,b,c]
                No[q,a] += model.alpha**2*z[b]*z[c]*S[q,b,a,c]
K0 = model.initial_gram
Ko = K0+Mo+Mo.T+No+Mo.T@np.linalg.solve(K0,Mo)
assert np.max(abs(K-Ko)) < 2e-13
assert np.linalg.eigvalsh(K)[0] > 0
assert np.max(abs(model.predict(state,coeff)[:m]-(y+r))) < 2e-13
stopped = state.copy()
stopped[model.slices[0]] = 0
assert np.max(abs(model.rhs(0,stopped))) == 0
single = mod.initialize(w,W,U[:1],y[:1])
query = mod.query_coefficients(w,W,U[:1],X,batch_size=3)
s,meta = mod.integrate(single,target=.005,rtol=1e-10,atol=1e-12,
                      time_cap=10,deadline_seconds=5,max_step=.05)
r,z,J,P = single.unpack(s)
z = float(z[0])
k,ss = float(single.initial_gram[0,0]), float(single.response_gram.ravel()[0])
label = float(y[0])
def one_scalar(t,z):
    return -label-2*k*z-(16/3)*ss*z**3-(8/5)*ss**2/k*z**5
independent = solve_ivp(one_scalar,(0,meta['physical_time']),[0.],
                        rtol=2e-12,atol=2e-14,max_step=.025)
expected = (-2*query.cross_gram[:,0]*z
            -(4/3)*query.cubic[:,0,0,0]*z**3
            -(8/5)*query.cross_gram[:,0]*ss**2/k**2*z**5)
assert meta['stop_reason'] == 'target'
assert abs(meta['train_mse']-.005) < 1e-12
assert abs(meta['train_mse']-float(np.mean(r*r))) == 0
assert abs(float(r[0])-one_scalar(0,z)) < 1e-9
assert abs(z-float(independent.y[0,-1])) < 1e-9
assert np.max(abs(single.predict(s,query)-expected)) < 1e-9
print('Independent module contraction and endpoint audit passed.')
PY
```

## Saved nine-task experiment audit

The supervisor expanded the assignment to audit the completed results
under `data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930/`.
Additional inputs were the complete `run_cubic_scalar_circle.py`, the
complete experiment protocol, that run's arrays and JSON metadata, the
same-study reference arrays it consumed, the reference's source manifest,
and the initialization/forward portions of `dense_compare.py`. The
checks did not inspect other studies or rerun the dense reference.

**Outcome: the reported raw errors reproduce; no coefficient,
decoder, endpoint, metric, sampling, or hash artifact was found that
explains the two large discrepancies.** Nine direct recomputations of
`sqrt(mean((scalar-dense)**2))` gave exactly the stored values:

| Task | Raw circle RMS |
| --- | ---: |
| `pair_cos3` | `0.12125336662429967` |
| `pair_orthogonal_cos1` | `0.04520530695082602` |
| `near_pair_sin9` | `1.2056281769659525` |
| `cluster_triple_cos9` | `1.337774074698305` |
| `cluster_triple_cos1` | `0.042560839283627416` |
| `triple_wide_mixed` | `0.007534823623190559` |
| `quartet_mixed` | `0.03991637658651804` |
| `broad_ridge6` | `0.043183463126388925` |
| `alternating3` | `0.08980045591871255` |

The stored angle arrays are exactly `2*pi*arange(256)/256`, without a
duplicated endpoint. Each 128-point check is the every-other-point
subsample of this same grid. The largest change in reported RMS is
`3.792536640290223e-8`, on `cluster_triple_cos9`; the change on
`near_pair_sin9` is `1.0805178973782859e-10`. No declared `1e-3`
refinement trigger was crossed. This checks numerical sampling of the
saved curves; it is not an analytic continuum quadrature-error bound.

Reconstructing all nine `ScalarModel` and `QueryCoefficients` objects
from their saved arrays gives exactly their saved circle and training
predictions. The largest representative training-alias error is
`2.142730437526552e-14`. Every returned residual MSE and every decoded
original-dataset MSE equals `0.001` within `2.7e-16`. History endpoint
time and loss match the returned state exactly, and all saved accepted
histories decrease monotonically. Each endpoint kernel has positive
smallest eigenvalue; the smallest among the nine is approximately
`0.00060588753`. The source's conditioning gate was respected.

For `alternating3`, opposite training inputs cancel within `3.33e-16`,
their labels cancel exactly, and decoded antipodal predictions cancel
within `5.55e-16`. The three groups each have multiplicity two, so the
uniform three-representative reduction has the prescribed original
six-example normalization; it does not replace a singular Gram by a ridge.

All nine raw dense prediction arrays are exact copies of their hashed
reference arrays. All nine output NPZ digests and reference checkpoint
digests match their records. All six current source hashes match the run
manifest, including the unchanged audited module. The saved summary SHA256
is `51902cdadaf5defda46699173a9cccd743b06f45db0d9385e3852bb0a120d031`.

The frozen-kernel prediction was independently recomputed by
eigendecomposing each saved initial Gram and applying the recorded
endpoint time. The largest prediction discrepancy is `1.04e-13`; all
reported frozen-vs-dense RMS values reproduce exactly. **The
`cluster_triple_cos9` frozen control is not a matched-target comparison:**
it stops at time `3000` with MSE `0.007490239161461014`. Its plotted
function and raw error remain valid capped-run diagnostics.

## Matched initialization provenance and the difficult cluster

The original dense source manifest at
`quick_blocks1024_seed1_overlay_20260926/manifest.json` identifies width
1024, seed 1, first-weight stream `[1,1]`, Gaussian middle stream
`[1,101]`, and the same `dense_compare.py` SHA256 as the scalar run:
`4cbafbd5888ec46c286e4269451d5ade8ad34df9fa86f7b2629418fed302d936`.
The original dense checkpoint's JSON and its later reference metadata
agree on the task, width, seed, target, time, and checkpoint chain.

For `cluster_triple_cos9`, the audit independently regenerated these
Gaussian arrays directly from `numpy.random.SeedSequence`, rather than
calling the module initializer. Their raw float64 array hashes are

- First weights:
  `4635fbf0a2ec035841f0225a28a42e7c1d92013978b80d9a3b1764cc4a66fcf1`.
- Middle weights:
  `c9617c6a451cbf03d8253b436fcab8d96c7655fed9840a35ca5d2afe2fac9095`.

The independent calculation reproduced saved `K0` exactly and all saved
training `S` entries within `5.55e-17`. Query coefficient slices were
computed by explicit scalar index loops at circle indices `0,37,128,255`:
the largest query Gram gap was `2.23e-16`, the largest cubic coefficient
gap `1.67e-16`, and the largest directly reconstructed query prediction
gap `4.01e-12`. This is negligible relative to the reported RMS `1.3378`.

The canonical dense initializer has a small nonzero readout, whereas the
surrogate starts from zero. Its independently reconstructed circle RMS
at initialization is `1.4079002859285932e-5`, matching the run record.
The run's separate pair-task control records a readout-convention
effect of `1.2164e-5` and a dense-tolerance effect of `4.3484e-7` in
circle RMS. Those controls were performed by the parent task, not this
auditor, and measure that pair task rather than every difficult task.
The raw primary comparison retains its stated convention discrepancy.

## Why the positive completion is large on the failing tasks

The following are deterministic diagnostics of the saved states:

| Diagnostic | `near_pair_sin9` | `cluster_triple_cos9` |
| --- | ---: | ---: |
| `||z||_2` | `8.04195556` | `50.46902511` |
| `||K0^-1 M||_op` | `4.06234531` | `13.04217727` |
| Scalar circle-output RMS | `2.41911964` | `2.19551332` |
| Dense circle-output RMS | `1.25374810` | `0.93033394` |
| Cubic-readout circle RMS | `1.32780107` | `1.10242567` |
| Alias-completion circle RMS | `1.09943560` | `1.26838299` |
| Cubic readout versus dense RMS | `0.17133187` | `0.49677363` |

Here `M` is computed from the saved state by the audited contraction;
`||K0^-1 M||_op` is its matrix operator norm after solving the initial
Gram. It measures the relative feature-Gram correction occurring in
the positive completion, not an observed neural weight displacement.
The source's simple sufficient coercivity argument uses a bound of
`1/2` on this quantity; neither endpoint is in that sufficient regime.
More directly, the total residual motion satisfies
`R(t)=integral ||r(s)|| ds >= ||z(t)||`, so neither endpoint lies in
the source estimate's `R<=1` neighborhood. This invalidates an appeal
to that small-motion estimate for these particular unit-label runs;
it does not invalidate its conditional derivation.

The displayed completion is exactly
`kx@solve(K0,labels+r-f_cubic_train)` at the saved state. It is
mathematically required by the specified decoder to agree with its
completed-kernel training dynamics. Its nominal higher-order status
does not make it small outside the small-motion regime. The
cubic-only error is a decomposition diagnostic on the completed
trajectory, **not** a validated replacement surrogate: removing the
completion would generally break the training aliases. No such
replacement was trained or selected.

## Additional hard-task numerical verification

The original protocol tightened only its first two scalar tasks. Those
saved checks change the circle output by `3.23655e-11` and
`1.13168e-11`, respectively. After this audit identified the lack of
a tolerance replicate on the two difficult tasks, the supervisor
authorized exactly two additional numerical solves with the unchanged
saved coefficients. The extension was recorded before either solve in
`CUBIC_NUMERICAL_CHECK_ADDENDUM_20260930.md`, SHA256
`3bc99903952c43c5f2139c2580d7aeea961068f1ed20b5bbab09365857af071c`.
Its full executable source, motivation, criterion, provenance, and
limits are retained there. This is an explicitly post-result check.

Both tighter solves used `rtol=1e-9`, `atol=1e-11`, target MSE `0.001`,
and a 10-second per-solve cap. They both reached the target without a
loss rise, taking approximately `0.060` and `0.104` seconds:

| Task | Circle change from original | Tighter scalar-vs-dense RMS |
| --- | ---: | ---: |
| `near_pair_sin9` | `2.0368748978694372e-11` | `1.2056281769463386` |
| `cluster_triple_cos9` | `9.271770211013988e-11` | `1.3377740747538531` |

The residual MSEs equal `0.001` within `1.4e-18`; decoded MSEs within
`7.6e-17`; the largest tighter-solve alias gap is `2.97e-14`.
Both pass the frozen numerical-change threshold `1e-4`. Their raw
records are in `hard_task_tolerance_checks.json` and endpoint states,
predictions, and histories are in `hard_task_tolerance_endpoints.npz`
under the original run directory. The latter has SHA256
`f127d4454bb8d6634bb4fbff41a27ac982908941765373eaa634011e8283f64e`.
The original run products were not overwritten. No additional solves
were conducted by this auditor after these two checks.

The large discrepancies therefore persist under the checked tighter
scalar integration and resolved circle sampling. They are substantive
failures of this particular completed cubic-response approximation on
these finite unit-label tasks, within the remaining stated dense-reference
and initialization-convention qualifications. They make no claim about
an arbitrary-accuracy extension or a different scalar construction.
