# Current manuscript reconciliation, 2026-09-30

This continuation explicitly uses paper/main.tex as its primary scientific
context. Root read its complete 1,969 lines, including all theorem/proof and
appendix bodies and figure captions, plus the complete included files
comparison_appendix.tex (448 lines) and sphere_appendix.tex (29 lines).
Neither included file has further TeX inputs. Root also read docs/index.qmd,
docs/notation.qmd, current AGENTS.md and RESEARCH_WORKFLOW.md before research.
No other studies or old_docs were read. The paper was not edited.

The earlier study does not retain a paper snapshot/hash identifying which
manuscript version its original prompt came from. Consequently no historical
manuscript change is asserted. The exact equations in the current study were
checked against the current manuscript instead. Their correspondence is exact
with the qualifications below.

## Exact dictionary and clock

Take two hidden layers, tanh, and q=1 in manuscript equations `eq:old-clock`,
`eq:old-ode`, `eq:old-recon` and the outer-block equations `eq:dense-flow`.
The zeroth Legendre polynomial is p_0=1. The dictionary is

| Study | Manuscript |
|---|---|
| A | W^(1) |
| h_a | h_a^(1) |
| B (derived only) | reconstructed W-hat^(2) |
| g_a | h_a^(2) |
| d_a | delta_a^(2) |
| ell_a | delta_a^(1) |
| k_a | bar h^(1)_(a,0)/tau |
| v_a | -2 bar delta^(2)_(a,0) |

In particular the raw moments obey

\[
\dot{\bar h}_{a,0}=\rho h_a,\quad
\dot{\bar\delta}_{a,0}=r_a d_a,\quad \dot\tau=\rho.
\]

Differentiating k=bar h/tau and v=-2 bar delta gives precisely the study's
kdot=(rho/tau)(h-k) and vdot=-2rd. Reconstruction becomes

\[
B=W_0-\frac{2}{mn\tau}\sum_a\bar\delta_{a,0}\bar h_{a,0}^T
 =W_0+\frac1{mn}\sum_a v_a k_a^T.
\]

There is no extra factor 1/sqrt(n) in Bh and no physical-time rescaling.
The factor -2 belongs in v; the normalization 1/tau belongs in k; neither
absorbs m or n. With the manuscript's mobilities (n,1,n), the unhalved mean
squared loss gives wdot=-2 mean r_a g_a and
Adot=-2 mean r_a ell_a x_a^T/sqrt(d), exactly as in the study.

The unit history prefix has constant initial h and zero backward history.
It gives k_a(0)=h_a(0), v_a(0)=0, tau(0)=1. First-layer Gaussian variance is
1 and hidden-mixer variance 1/n, in agreement with the current study. This
study additionally fixes w(0)=0, finite normalized circle/sphere inputs and
binary labels. The main manuscript's setting permits a small stored readout
and its fixed-width theorem permits arbitrary finite initializations. Exact
zero readout is a valid specified instance, not interchangeable with a
nonzero small random finite-width readout. The book's stated small-readout
Gaussian variance is 1/n^2, so that convention is also distinguished.

For the manuscript's defect `eq:defect`, the q=1 projected endpoints are
h_a^*=k_a and b_a^*=-v_a/(2tau). Thus its internal defect is

\[
\frac{2\rho}{mn}\sum_a(b_a-b_a^*)(h_a-k_a)^T
=\frac1{mn}\sum_a(2r_a d_a+(\rho/\tau)v_a)(h_a-k_a)^T.
\]

This is exactly the signed term Z in ENERGY_ROUTE.md; it does not confer
the dense flow's unconditional loss descent on the closure.

## What transfers, and what depends on zero readout

All results proved for the study's stated equations apply directly to this
specified q=1 manuscript instance. No result here requires higher order or
tracking another trained model. Algebraic key averaging, signed memory work,
oddness and the fixed-comparator identity hold more generally. With arbitrary
initial readout and Y^2=mean y_a^2, the readout balance is

\[
\frac{\|w(t)\|^2}{2n}+\int_0^t[\mathcal L+\operatorname{mean} f_a^2]ds
=\frac{\|w(0)\|^2}{2n}+Y^2t.
\]

The comparator penalty is then ||w(0)-u||^2/(2nT). The exact local
reinforcement expansion, the exact zero-signal arrested trajectory, and the
existing scalar sign-cone theorem use w(0)=0. They are not asserted for
generic nonzero small readout. The new endpoint theorem likewise states
zero readout and zero values explicitly. None is a width-limit theorem.

The current paper already proves global finite-time existence for the
learning-speed closure at every fixed order when activation and derivative
are bounded. The study's separate q=1 proof is consistent with that result;
global finite-time existence is not a new manuscript-level claim here.

## The joint-clock qualification

In `eq:new-ode`, the q=1 Gram scalar is M=1+integral rho dt, even though
the joint coordinate clock is tau_joint=1+integral(rho+||Psi_dot||)dt.
At q=1 the normalized key is bar h/M, not bar h/tau_joint. Its coordinate
dilation term vanishes. There is also an initialization distinction: the
joint construction uses a matching backward prefix b_a(0), rather than the
learning-speed construction's zero prefix, and subtracts its initial product.
On matched histories its reconstructed operator differs from the
learning-speed operator by

\[
-\frac2{mn}\sum_a b_a(0)[k_a-h_a(0)]^T.
\]

For this study w(0)=0, hence b_a(0)=0. Its physical q=1 variables therefore
also coincide with the joint closure while the latter is defined, although
the two coordinate clocks differ. With generic nonzero readout the prefix
term can remain. The paper's sentence that changing the coordinate alone
does not change the constant-mode closure should not be read as discarding
this prefix distinction. No paper edit or claim about general joint-clock
all-time continuation is made.

## Provenance and scope of checks

An independent scoped normalization audit by agent `/root/notation_audit`
read the complete ENERGY_ROUTE.md and ENERGY_CHECK.md, the complete relevant
manuscript construction and clock proofs, and selected included material.
It independently recovered all factors above and the prefix qualification.
It did not read the original study assignment; root checked its dictionary
against the complete current study model in README and SYNTHESIS. This is
internal checking, not a promotion review or historical version comparison.

Frozen SHA256 values at this continuation:

```text
paper/main.tex
fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605
paper/comparison_appendix.tex
de103310bbb43ecfcafc7d5e4e833b1f40559cad2cefe55a212f2507908a3adf
paper/sphere_appendix.tex
f1a5c87937b1c805faa89edee9fb2ad2809de1f873b4e83888ccf5e5cdf673e2
ENERGY_ROUTE.md
015b9c83cfdcc52c16913f56ef2e2d5f50bd391064a88dba8f0592253c9377b3
ENERGY_CHECK.md
16f5f7f6f9d8ff96a4e395479fdc8ada79f7243e03a8aad63704c20f29ac5f39
```
