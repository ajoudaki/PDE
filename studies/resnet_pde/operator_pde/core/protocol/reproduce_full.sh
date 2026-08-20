#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON_BIN:-python}"
workers="${WORKERS:-8}"

cd "$project_dir"
export PYTHONPATH=src

# Algebraic gates.
"$python_bin" -m unittest discover -s tests -v

# Primary PDE and autonomous continuation through the plateau.
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 256 --R 128 \
  --seed 20260723 --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 256 --R 128 \
  --seed 20260723 --duration 24 --dt 0.1 --sample-dt 0.1 \
  --restart-from results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz

# Time-step refinement.
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 64 --R 32 \
  --seed 20260723 --duration 4 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 64 --R 32 \
  --seed 20260723 --duration 4 --dt 0.01 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 64 --R 32 \
  --seed 20260723 --duration 4 --dt 0.005 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 64 --R 32 \
  --seed 20260723 --duration 4 --dt 0.005 --sample-dt 0.04 \
  --integrator heun

# Depth refinement.
for depth_nodes in 8 16 32; do
  "$python_bin" run_pde.py --quadrature sobol --P 5 --N "$depth_nodes" \
    --M 128 --R 64 --seed 20260724 --duration 4 --dt 0.02 --sample-dt 0.04
done

# Cubature refinements and independent scrambles.
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 128 --R 64 \
  --seed 20260723 --duration 4 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 512 --R 128 \
  --seed 20260723 --duration 4 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 256 --R 256 \
  --seed 20260723 --duration 4 --dt 0.02 --sample-dt 0.04
for seed in 20260725 20260726; do
  "$python_bin" run_pde.py --quadrature sobol --P 5 --N 16 --M 256 --R 128 \
    --seed "$seed" --duration 4 --dt 0.02 --sample-dt 0.04
done

# Basis and independent cubature-method checks.
"$python_bin" run_pde.py --quadrature sobol --P 15 --N 16 --M 128 --R 64 \
  --seed 20260723 --duration 4 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature sobol --P 15 --N 16 --M 256 --R 128 \
  --seed 20260723 --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature gauss-hermite --P 5 --N 16 \
  --base-order 3 --fast-order 3 --seed 20260723 \
  --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature hybrid --P 5 --N 16 --R 128 \
  --base-order 3 --seed 20260723 --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature hybrid --P 15 --N 16 --R 128 \
  --base-order 3 --seed 20260723 --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature hybrid --P 15 --N 16 --R 256 \
  --base-order 3 --seed 20260723 --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_pde.py --quadrature hybrid --P 35 --N 16 --R 128 \
  --base-order 4 --seed 20260723 --duration 8 --dt 0.02 --sample-dt 0.04

# Canonical dense-network ensembles. These never enter the PDE velocity.
"$python_bin" run_exact_reference.py --n 64 --depth 16 --seeds 64 \
  --seed-start 1000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 64 --depth 32 --seeds 64 \
  --seed-start 4000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 96 --depth 32 --seeds 48 \
  --seed-start 2000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 128 --depth 32 --seeds 32 \
  --seed-start 3000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 128 --depth 32 --seeds 64 \
  --seed-start 5000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 256 --depth 32 --seeds 32 \
  --seed-start 6000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 256 --depth 32 --seeds 32 \
  --seed-start 8000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 256 --depth 32 --seeds 64 \
  --seed-start 10000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 256 --depth 64 --seeds 16 \
  --seed-start 7000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 512 --depth 32 --seeds 16 \
  --seed-start 14000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04
"$python_bin" run_exact_reference.py --n 256 --depth 64 --seeds 48 \
  --seed-start 12000 --workers "$workers" --duration 8 --dt 0.02 --sample-dt 0.04

"$python_bin" combine_references.py \
  results/raw/exact_ensemble_n128_L32_S32_seed3000_dt0p02_T8p0.npz \
  results/raw/exact_ensemble_n128_L32_S64_seed5000_dt0p02_T8p0.npz \
  --output results/processed/exact_combined_n128_L32_S96.npz
"$python_bin" combine_references.py \
  results/raw/exact_ensemble_n256_L32_S32_seed6000_dt0p02_T8p0.npz \
  results/raw/exact_ensemble_n256_L32_S32_seed8000_dt0p02_T8p0.npz \
  --output results/processed/exact_combined_n256_L32_S64.npz
"$python_bin" combine_references.py \
  results/raw/exact_ensemble_n256_L32_S32_seed6000_dt0p02_T8p0.npz \
  results/raw/exact_ensemble_n256_L32_S32_seed8000_dt0p02_T8p0.npz \
  results/raw/exact_ensemble_n256_L32_S64_seed10000_dt0p02_T8p0.npz \
  --output results/processed/exact_combined_n256_L32_S128.npz
"$python_bin" combine_references.py \
  results/raw/exact_ensemble_n256_L64_S16_seed7000_dt0p02_T8p0.npz \
  results/raw/exact_ensemble_n256_L64_S48_seed12000_dt0p02_T8p0.npz \
  --output results/processed/exact_combined_n256_L64_S64.npz

# Required iid-depth homogenization diagnostic.
cd "$project_dir"
"$python_bin" audits/numerics/paired_w_variance.py \
  --width 128 --pairs 24 --depths 8 16 32 64 \
  --train-time 0.5 --dt 0.02 --workers "$workers"

# Main and independent statistical analyses.
cd "$project_dir"
MPLCONFIGDIR=/tmp/matplotlib-cache MPLBACKEND=Agg \
  "$python_bin" analyze.py
cd "$project_dir"
"$python_bin" audits/statistical_audit/analyze.py
"$python_bin" audits/statistical_audit/reference_noise_update.py
"$python_bin" audits/statistical_audit/ordered_limit_update.py

echo "Full genuine-PDE protocol completed."
