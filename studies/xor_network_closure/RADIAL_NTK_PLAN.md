# Frozen initial NTK overlay, T=100

Authorized side-task continuation of the explicitly supplied radial plot, 2026-09-14.
Only this extension's source/products and a short README link are written; existing
training, plots and main-task work are preserved. No subagents or network training.

Use the retained 16-point shifted-XOR data and dense directions from
`radial_output_002`, retaining its actual-network and N1/N3/N5 curves exactly.
For each original width8192 seed (11,29,47), regenerate initial parameters in their
original RNG order, check both float64 and float32 byte hashes, and evaluate the
full initial tangent kernel with the original block mobilities (n,1,n). Evaluate
the float32-stored initial parameters and inputs in float64 on CPU, with two BLAS
threads, to avoid disturbing the main task's GPUs. This is a finite-width
linearization at initialization, not a conventionally reparameterized NTK model.

For unit directions u, initial hidden features h1,h2 and residual-free backward
fields delta1,delta2, the three cross-kernel blocks are

    K1(u,v) = (u·v) (delta1(u)·delta1(v))/n
    K2(u,v) = (h1(u)·h1(v)) (delta2(u)·delta2(v))/n²
    K3(u,v) = (h2(u)·h2(v))/n.

These are exactly `code/pde/finite_network.py:kernel_blocks` under x=sqrt(2)u.
Let K=K0(X,X)=V diag(lambda) V^T and r0=f0(X)-y. The unhalved MSE clock gives

    f_NTK(t,u) = f0(u) - K0(u,X) V diag(q_t(lambda)) V^T r0,
    q_t(lambda) = -expm1(-2 t lambda/m)/lambda,
    q_t(0) = 2 t/m.

No inverse, ridge, spectral clipping, refitted learning rate, or infinite-time
interpolation is used. Average the three T=100 output curves, as for the actual
network. Also calculate the readout-only version K3 to quantify its difference
from the full initial NTK; only the full NTK needs a new plotted line.

Numerical checks: cross-kernel blocks versus the maintained oracle at a small
nonzero readout (absolute tolerance 2e-12); spectral propagation versus an
independent augmented matrix exponential (2e-11), including a singular kernel;
training endpoint spectral identity (2e-11); reconstructed initial predictions
versus saved values (3e-9), initial training Gram versus saved values (3e-6);
kernel symmetry/PSD (absolute 1e-11). Preserve all prior curve arrays bitwise.
Record source/input/output hashes, command, versions and run time.

Report each seed's and the mean curve's training MSE and the full-circle difference
from the actual network; these are descriptive comparisons with no new convergence
claim. New outputs are `data/generated/xor_network_closure/radial_ntk_001/`.
Budget: one evaluation for each of the three fixed seeds, at most 300 seconds
of execution, 3 GiB resident memory and 100 MiB outputs. Stop on a validity failure
and retain the diagnostic; no extra training or parameter search is authorized.
