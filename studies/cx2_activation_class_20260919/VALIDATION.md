# Deterministic identity validation

Run 2026-09-19 from `/home/amir/Codes/PDE`. No training trajectory or empirical promotion claim.

Python `3.10.12`, NumPy `1.26.4`. One BLAS/OMP thread.

Command:

```sh
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B studies/cx2_activation_class_20260919/check_identities.py
```

Observed exit status: 0. Two tests passed in 0.055 seconds, each with four activation subcases: Softplus, oscillating-linear, offset sine and C1,1 quadratic-smoothed ReLU.

The checks validate exact supplied-state symmetry, simultaneous raw-step equivariance, the feature directional chain rule, and raw-metric normalization. They do not prove population convergence, continuation, tail control, fitting at a later horizon, or numerical closure accuracy.

Source SHA256 values:

- `studies/cx2_activation_class_20260919/check_identities.py`: `22e441ce52e0e3efab6aa91708c5ff5a0460fa876660c0e812c450eca0982f44`

- `code/pde/finite_network.py`: `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551`

- `code/pde/__init__.py`: `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3`

- `code/pde/gaussian_moments.py`: `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae`
