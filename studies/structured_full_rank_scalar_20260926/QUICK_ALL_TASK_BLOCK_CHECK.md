# All-circle-task block comparison: internal data check

The saved run contains 60/60 checkpoints; 55 reached training MSE 0.01. The plot includes 33/36 fitted block/reference pairs and 11/12 fitted control/reference pairs.

Width 2048, seed 1, all 12 declared circle tasks, blocks 8/16/32. Each method uses its own first refined MSE-0.01 crossing and is compared with the Gaussian reference for the same task. These are different physical stopping times. The Gaussian control changes only the initial middle matrix; outer weights are matched. Every middle matrix is trained without a block restriction.

| Task | k = 8 RMS | k = 16 RMS | k = 32 RMS | Gaussian-control RMS |
|---|---:|---:|---:|---:|
| pair_cos1 | 0.0054903 | 0.0055225 | 0.0027356 | 0.0127143 |
| pair_cos3 | 0.0033362 | 0.0017253 | 0.0022857 | 0.0031793 |
| near_pair_sin9 | 0.0131279 | 0.0069286 | 0.0031547 | 0.0016661 |
| triple_cos3 | 0.0128313 | 0.0063293 | 0.0052403 | 0.0023632 |
| triple_mixed | 0.0016013 | 0.0015618 | 0.0015622 | 0.0018465 |
| cluster_triple_cos9 | 0.0464803 | 0.0286791 | 0.0201441 | 0.0227434 |
| broad_ridge6 | 0.0018872 | 0.0029411 | 0.0011112 | 0.0044371 |
| sharp_ridge8 | 0.0013972 | 0.0009334 | 0.0011579 | 0.0006861 |
| alternating3 | 0.0054368 | 0.0041690 | 0.0025637 | 0.0033381 |
| alternating5 | 0.0145666 | 0.0076628 | 0.0069043 | 0.0068157 |
| alternating9 | excluded | excluded | excluded | excluded |
| multiscale12 | 0.0056588 | 0.0045656 | 0.0016758 | 0.0014069 |

The following saved runs did not reach the target. When a task's Gaussian reference is nonfitted, all its comparison pairs are excluded, including any fitted candidate. These checkpoints are retained; no extension or rerun is included.

| Task | Method | Partial training MSE | Stop reason |
|---|---|---:|---|
| alternating9 | gaussian | 0.23657866 | deadline |
| alternating9 | gaussian_control | 0.22717650 | deadline |
| alternating9 | block8 | 0.55751633 | deadline |
| alternating9 | block16 | 0.50802869 | deadline |
| alternating9 | block32 | 0.33331458 | deadline |

RMS means the unnormalized root mean square of the difference between saved trained functions over 2048 uniform circle angles. The figure uses a separate linear y scale in each panel and a log2 x scale. A missing or nonfitted member excludes the corresponding pair; raw partial results remain in the run directory.

**Internal audit:** All source/data hashes, schemas, circle/training grids, labels, saved-output training MSEs, fitted flags and nonreference circle RMSs checked. All dense weight shapes/dtypes inspected; two predetermined saved states checked for finite weights and forwarded on sparse inputs. No solver refinement.

Maximum 2048-versus-1024-grid RMS change: 4.03e-17. Maximum saved training time: 50.065 s; maximum saved total time: 50.587 s. Maximum recorded accepted-step loss rise: 0.

The sparse weight-forward check was fixed before run completion: First declared task/Gaussian and last declared task/block32; circle indices 0,137,1024,1901 and each full training set; atol 1e-12.

- `pair_cos1/gaussian`: maximum circle difference 0; maximum training-output difference 0.
- `multiscale12/block32`: maximum circle difference 0; maximum training-output difference 0.

This check verifies saved data and plotting consistency. It does not certify global integration error. One seed, one width and three block sizes do not establish a convergence rate or a population limit; MSE 0.01 is a finite-loss endpoint. This remains study-local evidence, without independent promotion review.

Run directory: `/home/amir/Codes/PDE/data/generated/structured_full_rank_scalar_20260926/quick_blocks2048_all_tasks_loss01_20260926`.

Outputs: `all_task_block_curves.png`, `all_task_block_curves.pdf`, `all_task_summary.csv`, `plot_audit.json`.
