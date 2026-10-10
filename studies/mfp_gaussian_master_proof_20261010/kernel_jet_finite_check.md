# Exact finite-width check of the symbolic kernel-jet example

The scoped verification agent `kernel_jet_finite_check` completed three focused
tests on 2026-10-10. All passed using exact `fractions.Fraction` arithmetic.
This checks finite-program construction, all trainable parameter blocks, and
factorial-normalized kernel derivatives through order two. It is not a Gaussian
limit test, an audit of the master theorem, or an independent promotion review.

The scientific input scope was exactly `symbolic_kernel_jets.py`,
`mfp_compiler.py`, `mfp_finite.py`, `mfp_expr.py`, and `compiler_usage.md`;
each was read completely. No study history, other report, other study, book
chapter, or external scientific source was consulted. The shared process
instructions and `explain-with-canonical-notation` skill with its neural-network
reference were applied. This agent owns only this report,
`test_symbolic_kernel_jets.py`, and its generated evidence namespace. It made
no compiler, example, or shared-index changes.

## Independent oracle

There are two training samples and two hidden layers of common width
\(n\in\{2,3\}\). The fixed normalized inputs are
\(x_1/\sqrt d=(\alpha,0)\), \(x_2/\sqrt d=(\beta,\gamma)\), with \(d=2\).
Write the actual first-layer columns as \(U,V\in\mathbb R^n\), the hidden
matrix as \(W^{(2)}\in\mathbb R^{n\times n}\), and the stored readout as
\(W^{(3)}\in\mathbb R^n\). The oracle directly computes

\[
z_1^{(1)}=\alpha U,\qquad z_2^{(1)}=\beta U+\gamma V,\qquad
h_a^{(1)}=(z_a^{(1)})^{\odot2},\qquad
z_a^{(2)}=W^{(2)}h_a^{(1)},\qquad
h_a^{(2)}=(z_a^{(2)})^{\odot2},
\]
\[
f_a=\frac1n W^{(3)\top}h_a^{(2)},\qquad
r_a=f_a-y_a,\qquad
\mathcal L=\frac{r_1^2+r_2^2}{4},\qquad
K_{12}=\frac1n h_1^{(2)\top}h_2^{(2)}.
\]

Here powers with \(\odot\) mean componentwise powers. Ordinary chain rules give
the vectors of partial derivatives of the scalar output with respect to each
preactivation:

\[
\delta_a^{(2)}:=\frac{\partial f_a}{\partial z_a^{(2)}}
 =\frac2n W^{(3)}\odot z_a^{(2)},\qquad
\delta_a^{(1)}:=\frac{\partial f_a}{\partial z_a^{(1)}}
 =2z_a^{(1)}\odot W^{(2)\top}\delta_a^{(2)}.
\]

With vector mobility \(n\), matrix mobility one, and negative gradient flow,
the independent dense equations are

\[
\begin{aligned}
\dot U&=-\frac n2\bigl(r_1\alpha\delta_1^{(1)}
                              +r_2\beta\delta_2^{(1)}\bigr),&
\dot V&=-\frac n2 r_2\gamma\delta_2^{(1)},\\
\dot W^{(2)}&=-\frac12\sum_{a=1}^2r_a\delta_a^{(2)}h_a^{(1)\top},&
\dot W^{(3)}&=-\frac12\sum_{a=1}^2r_a h_a^{(2)}.
\end{aligned}
\]

The test's `_dense_flow` implements these array equations directly. It does
not derive them using a compiler gradient or derivative function. Matrix
velocity values from the tested program are decoded from its documented
representation \(\sum c u v^\top/n\), then compared entry by entry with the
dense equations.

For the second-order oracle, let \(\theta\) collect every weight entry and
write its dense velocity field as \(F(\theta)\). The test implements truncated
ordinary power series with exact coefficient convolution. First set
\(\theta_1=F(\theta_0)\), evaluate
\(F(\theta_0+t\theta_1)\), and define \(\theta_2\) as one half of its
coefficient of \(t\). This is exactly the coefficient equation for
\(\dot\theta=F(\theta)\) through degree one:

\[
\theta(t)=\theta_0+t\theta_1+t^2\theta_2+O(t^3),\qquad
2\theta_2=DF(\theta_0)[\theta_1].
\]

Substitution of this series into the dense forward pass gives the independent
coefficients \(K_{12}(0),\dot K_{12}(0),\ddot K_{12}(0)/2\). The oracle uses
no `Program.gradient`, `Program.directional`, `Program.jets`, or `mfp_expr.diff`.
Those routines are used only to construct the objects being tested. Thus
evolving residuals, readout motion, and all other field dependencies enter
through ordinary arithmetic on the dense ODE.

## Checks and outcomes

The deterministic nonzero fixtures use
\((\alpha,\beta,\gamma)=(2/3,-3/5,4/7)\) and
\((y_1,y_2)=(5/6,-2/5)\). Rational arrays and every matrix entry are specified
in `_fixture`; matrix entries are actual stored values, without any extra
width rescaling. They are deterministic test states, not Gaussian draws.

1. At both widths, the program's loss and every component of all four velocity
   blocks agree exactly with dense backpropagation. Every tested velocity entry
   is nonzero, so the fixtures do not hide an omitted training block.
2. For both explicit `z**2` and generic `phi` evaluated with the exact quadratic
   derivatives, all three `moving=True` jets match the dense ODE series at both
   widths. As a control, `moving=False` matches the independently evaluated
   straight path with initial velocity held fixed. Its coefficient of order
   two differs from the moving coefficient in every case, while orders zero
   and one agree. This makes the acceleration contribution detectable.
3. The same symbolic program is evaluated again with labels
   \((-7/4,3/8)\). Its zeroth kernel coefficient stays fixed and both positive
   orders change, each matching the oracle. Setting all geometry parameters
   to zero yields zero features, all-zero velocities and kernel jets, and
   loss \((y_1^2+y_2^2)/4\) despite nonzero labels. No division by a geometric
   quantity or residual is needed.

The implementation is
[test_symbolic_kernel_jets.py](test_symbolic_kernel_jets.py). No tolerance,
random seed, numerical differencing, quadrature, or external package is used.
This is a bounded deterministic check; it does not establish correctness for
arbitrary activation functions, all states, higher orders, or Gaussian
compilation. The symbolic-activation branch is exercised with quadratic
derivative values only.

## Reproduction and retained evidence

From `/home/amir/Codes/PDE`, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s studies/mfp_gaussian_master_proof_20261010 -p 'test_symbolic_kernel_jets.py' -v
```

Observed: Python 3.10.12, three tests passed in 0.123 seconds, process exit
status zero. A 60-second subprocess limit bounded the check. HEAD was
`c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`; relevant source hashes are more
specific because the study files were untracked. Only the focused new test
file was run.

The fresh run directory is
[`data/generated/mfp_gaussian_master_proof_20261010/kernel_jet_finite_check/20261010T172700.662389Z/`](../../data/generated/mfp_gaussian_master_proof_20261010/kernel_jet_finite_check/20261010T172700.662389Z/).
It retains `metadata.json` (command, working directory, Python version, exact
precision, source hashes, HEAD and exit status), empty `stdout.txt`, and the
complete successful unittest output in `stderr.txt`.

| Evidence file | SHA-256 |
| --- | --- |
| `stdout.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `stderr.txt` | `024ef8b26d25bb6eea944528615d2dffadbbf35568675092434670e6d0372ee8` |
| `metadata.json` | `4eb7fa3f2f21244596f6adc13535a204552f55d672687a2851346dd6a8ba32a7` |

| Input | SHA-256 at execution |
| --- | --- |
| `symbolic_kernel_jets.py` | `acb52d118d4ee51b50f8ca4476c4206bcab568b22a3c564597354d9ba4937797` |
| `mfp_compiler.py` | `f6d0b2f786e9a0b676476487dff3e3c393c8fd7145261661d8b45737cae215ce` |
| `mfp_finite.py` | `7e39ff0fd2026c6fd7fd6f3f2e6f6f2a82025a72fd83b533c38d7b4be03ed6d8` |
| `mfp_expr.py` | `82bce3fe5f8180aa89c009fa117c1fdb6563bbb0247d20e60296fbe199f070de` |
| `compiler_usage.md` | `f8c7c6acc5931aeabb5efda7ebc9f24e4108c2c4aaeb7c05b48048d7403334ff` |
| `test_symbolic_kernel_jets.py` | `1fdcb0e304cc0f57ff5ae0aaf579bc39bb1bead1854f819736827c1d9cfb7f12` |

The result is internally checked for these exact tests and source versions.
There are no unresolved failures within that scope. Changed scientific inputs
require a fresh run; this report is not a promotion approval.
