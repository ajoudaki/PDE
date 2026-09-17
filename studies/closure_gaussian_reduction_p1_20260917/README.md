# Exact Gaussian reduction of the p=1 population closure

This study starts from the established book and investigates exact simplifications
of the canonical p=1 two-hidden-layer tanh population closure. It does not study
a Lyapunov potential, a neural-width limit, or convergence in closure order.

## Contract and inputs

Normalized inputs u=x/sqrt(2) lie on S1. The training law is any finite
probability distribution with bounded real labels; repeated, antipodal, and
arbitrarily close inputs are allowed. Preserve the established p=1 dictionary,
eta=1/4096 inverse-Cholesky normalization, complete joint Gaussian initialization,
zero population readout, actual transpose, and unhalved probability-weighted
square-loss physical gradient metric.

Scientific inputs are docs/NOTATION.md, docs/observable_p1.md, the finite Gaussian
source rule and C.4.7.9--C.4.7.10 of docs/global_nonlinear.md, and the finite
Gaussian/observable calculus of docs/gaussian_calculus.md. No other study is an
input. The author works alone; all writes are confined to this flat study and
its generated-data namespace. No Git staging, commits, or established edits.

## Results and evidence

[exact_reduction.md](exact_reduction.md) contains the complete arguments:

1. Explicit dictionaries and universal data-independent M(0), reproducing
   the established coefficient formulas with all correlations intact.
2. Exact removal of inactive constants: the active matrix is 2 by 4. The
   lower and upper carriers need only four and two fixed Gaussian roots.
3. A fixed, explicit two-dimensional Gaussian-integral kernel computes all
   upper activation Grams, including initial/current and cross-time pairs.
4. An autonomous function F on R2 replaces the upper readout population:
   predictions are F(Ma), backward coefficients are grad F(Ma), and its
   evolution is a finite sum of known kernel sections. The representation
   is isometric in the original metric and complete on initialized paths.
5. Exact current lower-contraction and full tangent-kernel equations; exact
   initial velocities/accelerations. The first hidden acceleration is twice
   the hidden-metric gradient of the label-weighted upper feature norm.
6. Every fixed-order initialization time jet is a finite Gaussian DAG on
   the same root carriers. A complex-strip argument proves a positive local
   convergence radius with a remainder bound for this fixed closure.
7. Infinite rank of the fixed upper kernel rules out representing all its
   activation sections in one fixed finite linear feature basis. It is not
   a no-go theorem for all nonlinear or data-specific reductions.

Status: exact/proved, internally author-checked, not established or promoted.
The initialized coefficient formulas and parity reduction are established
inputs rederived here; the kernel/function reformulation, acceleration
interpretation, and explicit analytic bound are the study's extensions.

[validation.md](validation.md) records proof audit, source hashes, edge
cases, exact execution command and limitations. [check_reduction.py](check_reduction.py)
passed deterministic same-quadrature checks against the unreduced formulas,
including a nonsymmetric three-input configuration and a full moving matrix.
No training campaign or empirical convergence claim was made.

The remaining exact state includes a lower characteristic function and the
upper function F; it is not finitely many scalar moments. A single initial
Taylor series need not cover all positive time. General input fitting,
decay rates and neural-network limits are outside this investigation.

The requested exact simplification is complete at this stated scope. The
next possible work is a separately scoped numerical realization of the
kernel/function equations or a further proved lower-population reduction;
neither has been run or assumed here. Promotion is a separate process.
