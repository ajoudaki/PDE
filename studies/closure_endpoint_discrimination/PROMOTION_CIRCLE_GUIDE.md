## Optional GPU backend for the finite circle closure

`pde.observable_torch_circle` implements the same finite quadrature equations
as `observable_solver` in float64 Torch on CPU or CUDA. Install PyTorch in the
chosen environment to import this optional module; ordinary `import pde`
remains NumPy-only. There is no mixed precision or automatic device selection.
The module does not change global Torch settings. CPU initialization and transfer
are included in initialization cost, separately from GPU evolution.

The public initialized and imported order range is exactly **p=1,3,5** (the
existing chapter denotes order by N). Retained feature dimensions are
(5,3), (35,10), (128,21). Other orders are rejected even if the CPU producer
can form them. Dimension is exactly d=2, with inputs u=x/sqrt(2) on the unit
circle. P1,P2 are population integration rows, not network widths n. The
unchanged CPU producer retains every dictionary output, including p=5's two
redundant constant tails, the Gaussian response term, the ridge
1/[1024(p+1)^2] and the inverse-Cholesky transpose. Q and P remain separate
coefficient and population quadratures. Float64 quadrature is not exact
Gaussian integration.

For fixed marks b1,b2 and probabilities pi1,pi2 the complete fields are

```text
h(u)=tanh(w u),  a(u)=b1.T diag(pi1) h(u)
H(u)=tanh(b2 M a(u)),  f(u)=pi2.T diag(c) H(u)
d(u)=b2.T diag(pi2) [c*(1-H(u)^2)],  q(u)=b1 M.T d(u).
```

The stored Gaussian network convention is (1,1/n,1/n^2), bias-free two-hidden
layer tanh, output divided by n and physical mobilities (n,1,n). The finite
closure begins at w=g,c=0,M=D, with the zero readout representing the population
small-readout limit. For data (u_a,y_a,rho_a), write r_a=f(u_a)-y_a. Its
physical unhalved loss is sum rho_a r_a^2. The implemented finite velocities are

```text
w_dot = -2 sum_a rho_a r_a [(1-h(u_a)^2)*q(u_a)] u_a.T
c_dot = -2 sum_a rho_a r_a H(u_a)
M_dot = -2 sum_a rho_a r_a d(u_a) a(u_a).T.
```

Forward and backward actions use the same M and M.T. These are the gradient
velocities for the population-weighted w,c metric and ordinary Frobenius M
metric: differentiate f with respect to c_i,w_j,M_ij, and cancel the pi2_i
and pi1_j factors against those metric weights. Zero-weight nodes contribute
nothing to fields and may be omitted. `evolve` performs simultaneous explicit
Heun, k=F(s), l=F(s+h*k), s_next=s+h*(k+l)/2. It is numerical integration of
this flow; it is neither an exact finite-time flow nor arbitrary discrete GD.
No loss-decrease or step-stability guarantee is supplied.

```python
from pde import observable_torch_circle as closure
state = closure.initialize(3, initialization_nodes=64, population_nodes=32,
                           device='cpu')  # choose 'cuda:0' explicitly for GPU
law = closure.data_law([[1.,0.],[.6,.8]], [1.,-1.], [.5,.5],
                       device=state.device)
final = closure.evolve(state,law,steps=4,step_size=.005,block_size=2)
output = closure.predict(final,law.inputs)
pairs = closure.paired_observations(final,law,include_pairs=False)
assert output.shape == (2,)
assert pairs['rms'].shape == (2,)
```

Factories, CPU transfer and evolution own their resulting arrays. Public state
and data tensors remain mutable and are revalidated at call boundaries; changing
frozen marks changes the model. There are no cached derived contractions.
Metadata must preserve the supported dictionary/order tags; these identify
coordinates, not a certificate that a supplied state was reached by training.
`fields` returns a whole panel; `predict`, `rhs` and `paired_observations`
accept positive `block_size`. `observe` returns full input-index hidden Grams,
activation RMS, paired displacement RMS, prediction and loss; its whole-panel
workspace is explicit. Pair arrays have shape (P_l,m,2), initial then current,
and come with their population and input weights. Initial fields are recovered
from g,D on the same marks without external observation history. Finite panels
are not whole-circle error certificates.

With feature counts K1,K2, retained arrays contain
P1(K1+5)+P2(K2+2)+2K1K2 float64 scalars. Data contain 4m. An RHS block of B inputs
uses O(B(P1+P2+K1+K2)) field scalars and work
O(B[P1(2+K1)+P2 K2+K1K2]); complete RHS work sums over all blocks.
Heun retains a fixed number of moving arrays P1*2+P2+K1*K2, independent of
elapsed steps. Full Grams add 2m^2 outputs and O((P1+P2)m) field workspace;
explicit pairs add 2(P1+P2)m outputs. `state_bytes` counts tensor entries only,
not Python objects, CUDA context, allocator reservation, stages or archives.
CPU initialization retains its own maintained resource limits and cost.

`save_restart(path,state,law)` and `load_restart(path,device=...)` use the
existing portable float-hex checkpoint: all nine frozen/current arrays,
metadata and the finite law. Loading calls no initializer. Decimal/rational
states and unsupported order tags are rejected, not down-converted. Working
values transfer exactly; exact continuation requires the same device, reduction
environment, block sizes and step sequence. Cross-device outputs are compared
with tolerances, not promised bitwise equal. No absolute clock or history is
stored; callers retain intended physical time and step schedule separately.

Ordinary floating matrix products and 1-tanh(z)^2 can saturate, underflow or
fail through nonfinite intermediates; detected nonfinite fields/stages raise.
There is no extreme-range or correct-rounding promise. GPU/CPU agreement tests
finite implementation parity only. All existing population theorem hypotheses,
law families, horizons and iterated limits remain unchanged. Fixed precision,
fixed order, other laws or long horizons receive no new accuracy guarantee.

Run the deterministic CPU suite and then the explicitly requested CUDA suite:

```text
PYTHONPATH=code CIRCLE_TEST_DEVICE=cpu python -B code/tests/test_observable_torch_circle.py
PYTHONPATH=code CIRCLE_TEST_DEVICE=cuda:0 python -B code/tests/test_observable_torch_circle.py
python -B code/scripts/validate_torch_circle.py --device cuda:0 --output data/established/circle_gpu_check
```

The maintained validation command refuses an existing output directory and
executes the fixed p=1,3,5 circle example from its initializer. It records
source hashes, software/device settings, phase times, state bytes, process RSS,
CUDA allocated/reserved peaks, reference discrepancies and own-state restart.
`validation_work_seconds` starts after interpreter/import/device setup and
source hashing; it includes initialization, transfer, evolution, observations,
reference checks and restart work, but excludes final record writing. It is
not process end-to-end time. Evolution timings synchronize CUDA at boundaries.
The Linux producer fixes numerical thread environment variables before imports.
The declared budget is one worker, one CPU numerical thread, at most 120 wall
seconds, less than 1 GiB tensor allocation and three orders, with no adaptive
parameter search. This is an operational example, not a network-fidelity,
speedup, convergence-rate or settled-endpoint empirical conclusion.
