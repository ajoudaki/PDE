# Three-input diagnostic: executed results and validity limits

2026-09-16. This report concerns only the predeclared finite-quadrature
diagnostic in three_exp_contract.md. It is not a population theorem.
The source was fixed before execution in three_exp_diagnostic.py.

Exact command from /home/amir/Codes/PDE:

```text
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/closure_lyapunov_p1_20260916/three_exp_diagnostic.py --output data/generated/closure_lyapunov_p1_20260916/three_exp_diagnostic_01
```

The process exited 0 and completed all seven predeclared integrations.
Cumulative CPU time was 3.7003 seconds; peak resident memory was 111372 KiB.
The 180-second, 1-GiB and RHS-count caps were not reached. No extra run,
angle search or unplanned refinement was performed. NumPy 1.26.4 and
SciPy 1.13.0 were used. The retained records contain the Python version,
all actual source hashes, initializer metadata, tolerances, time panels,
final states and array hashes. Integration and initialization were
deterministic; there is no random seed.

## Primary outcome: inconclusive

The primary potential was the scalar-reference candidate

    (1+||c||^2)/(C_0+F^2),  F=(f_1+f_2-f_3)/3.

Its exact finite-system derivative included the movement of w,M,c.
On the first predeclared triple (angles 0.1,1.4,0.75), both population
resolutions produced positive derivatives well above the predeclared
threshold at common times 11,12,13. Their maximum positive derivatives
were 0.12734 and 0.31289. The tighter time integration had maximum
derivative discrepancy 2.407e-5 on the common panel.

However the two quadrature resolutions differed by 0.61460 in prediction
on that panel, exceeding the predeclared 0.02 validity threshold.
Therefore the primary result is **inconclusive_population_refinement**,
exactly as recorded by the executed script. It does not falsify the
population candidate. The candidate also remains unproved.

| Angle triple | Q/P | Stop time | Final finite-rule loss | Maximum observed readout norm |
|---|---:|---:|---:|---:|
| (0.1,1.4,0.75) | 2048/512 | 40.63885 | 1e-8 | 2.58741 |
| same | 4096/1024 | 44.17968 | 1e-8 | 2.64143 |
| (0.15,2.5,4.3) | 2048/512 | 400 | 3.8243e-5 | 1.56981 |
| same | 4096/1024 | 400 | 9.9301e-5 | 1.55736 |
| (0,pi-0.2,pi+0.4) | 2048/512 | 400 | 1.3314e-8 | 2.20494 |
| same | 4096/1024 | 400 | 1.2219e-8 | 2.20756 |

The remaining triples' prediction refinement discrepancies were 0.005245
and 0.009997, respectively. The one authorized time-refinement branch
was used on the first triple, so these later panels are not promoted into
an alternative primary violation test. The scalar potential's largest
positive derivative on the second triple was below its threshold; on the
third it was above. These are descriptive finite-rule observations only.

## Verification and interpretation

The diagnostic used the maintained correlated canonical initializer,
including the reverse-response term, ridge and inverse-Cholesky transforms.
Its direct full velocity was compared against the maintained RHS at
initialization and at a fixed deterministic nonzero-readout perturbation
for every run. All absolute discrepancies were below 1e-12. The complete
physical energy identity was independently recomputed on every retained
time panel. These checks test the finite calculation, not quadrature
accuracy or population convergence on these horizons.

A secondary calculation on retained panels showed that L(1+||c||^2)
can also increase before capture in the finite-rule dynamics. A subsequent
fully analytical, initialized-trajectory obstruction for that different
potential is recorded in the explicitly root-supplied final section of
three_exp_openfamily.md. Its proof does not use these numerical values.

Nothing here shows failure of fitting. All six primary finite runs reduce
loss substantially; this also supplies no proof of population fitting,
an exponential rate, a uniform readout bound, or the current-state capture
condition. The diagnostic is closed at its declared terminal stop.

Raw record: data/generated/closure_lyapunov_p1_20260916/three_exp_diagnostic_01/records.json.
Raw arrays: the same directory, with one initial file per quadrature and
one time-panel/final-state NPZ per integration. Exact hashes are in the
record. The contract's harmless joined-word typo in its exclusions was
left unchanged so its recorded source hash remains reproducible.
