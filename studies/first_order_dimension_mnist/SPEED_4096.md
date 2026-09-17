# Width 4096: speed and peak GPU memory

The user requested a narrow computational continuation after the initial MNIST campaign: test P=n=4096 for speed and peak memory. This matched-horizon benchmark found that the p=1 closure is **1.61–1.77× faster on the same GPU** at4096 and uses **63.2% less peak live GPU memory**. At2048 the closure was slightly slower. This measures the current implementations, data and numerical settings; it is not a universal speed ratio.

| P=n | Network integration time to T100 | Closure integration time to T100 | Network peak | Closure peak |
|---:|---:|---:|---:|---:|
| 2048 | 17.46 s (15.76–19.16) | 18.52 s (17.26–19.79) | 320.16 MiB | 207.32 MiB |
| 4096 | 55.72 s (49.24–62.20) | 32.84 s (30.53–35.15) | 756.96 MiB | 278.42 MiB |

Times are the mean and range of two repetitions, one on each RTX3090. Memory is identical in both repetitions. Network timing spread exceeds the predeclared15% threshold, so precise timing claims are limited. Comparing network to closure on the same device gives a1.77× speed ratio on GPU0 and1.61× on GPU1. The ratio of the two-device mean times is1.70×. These measurements are consistent about which implementation is faster at4096, despite device/run timing variation.

Doubling the size increased mean integration time by3.19× for the network and1.77× for the closure. Peak live memory increased by2.36× and1.34× respectively. This is compatible with the different width dependence of their state and computations, but two sizes do not establish an asymptotic scaling law. The closure's automatic contraction association can also change with dimensions.

## Matched protocol

Eight short trajectories use the unchanged production engines: two models × two widths × two repetitions. All use the same 10,552 MNIST3/5 training images, all784 coordinates, seed1729, full-batch Heun, float32 with TF32 disabled, and data block2048. Repetition1 runs2048 then4096; repetition2 reverses that order and swaps model-to-GPU assignments. No adaptive continuation or late precision probe is used. Every run completes T100 without hitting the runtime cap.

The previously validated network step is0.25 (400 Heun steps), while the closure step is0.125 (800 steps). The main comparison is time to the same physical horizon, so the closure's extra steps are included. This is whole-T100 integration timing, including its initial RHS calls, rather than a warmed kernel-only microbenchmark. It excludes initialization, observations, checkpoint saving and final test reporting. Training walltime, which includes observations/checkpoint cloning, averages17.76/18.75seconds at2048 and56.18/33.10seconds at4096 for network/closure. Initialization and all per-run details are retained separately.

Peak memory is `torch.cuda.max_memory_allocated` during training: live tensors including the prepared data, integrator stages, retained fixed/initial arrays, best checkpoint and observations. It excludes subsequent test/probe work, CUDA reservation/context overhead and unrelated processes; it is not total VRAM reported by nvidia-smi. Neither initialized-state counts nor forward-only memory are substituted for this measured training peak.

At4096, moving-state payload is76.27MiB for the network versus10.82MiB for the closure. Retained model plus initial/fixed arrays and caches is152.53MiB versus58.40MiB. Nominal closureP4096 still uses sign-paired quadrature:2,048 independent base particles plus their implicit negatives in each population. This is the same representation used at2048; it is not a new precision or approximation shortcut.

## Checks, evidence and reproduction

All runs have the same core source hashes, prepared dataset hash, precision and declared settings. Repeat train/validation predictions and both hidden Grams are bitwise identical across the two GPUs at every recorded time. This reproduces the numerical computation; timing naturally varies. No new4096 predictive-accuracy or continuous-flow error claim is made by this short speed experiment.

- [Every timing and allocation measurement](../../data/generated/first_order_dimension_mnist/speed4096_analysis_001/timings.csv).
- [Aggregate metrics, ratios, source hashes and repeated-output checks](../../data/generated/first_order_dimension_mnist/speed4096_analysis_001/summary.json).
- [Independent timing/memory audit](SPEED_4096_CHECK.md).
- Raw trajectories, checkpoints, configuration and source snapshots: `data/generated/first_order_dimension_mnist/speed4096/`.

Executed from the repository root:

```sh
/home/amir/miniconda3/bin/python -B studies/first_order_dimension_mnist/BATCH.py speed4096
/home/amir/miniconda3/bin/python -B studies/first_order_dimension_mnist/SPEED_ANALYZE.py
```

Existing run directories prevent accidental overwrite. A fresh repetition can use RUN.py with the same settings, `--horizon 100`, no continuation/probe flags, and a new output name. The bounded campaign used 4.54 summed GPU-process minutes, below the additional 10-minute cap; no longer training was launched.
