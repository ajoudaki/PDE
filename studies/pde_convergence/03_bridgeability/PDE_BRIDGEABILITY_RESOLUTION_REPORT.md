# Neural-PDE Hermite gap: targeted bridgeability resolution

**Date:** 25 July 2026  
**Question:** Was the adverse \(P=15\to35\) generator result a fixable
numerical/basis issue, or evidence of a fundamental obstruction to the
finite-neural-PDE framework?  
**Scope:** Canonical dense Euclidean \(\mu\)P residual-tanh benchmark; targeted
diagnostics, not a theorem-level certification of the full conjecture.

## Executive verdict

The most alarming gap was **bridgeable and has been fixed**.

The previous study compared

\[
5\leftarrow15
\qquad\text{against}\qquad
15\leftarrow35
\]

and interpreted the larger second defect as adverse Hermite noncontraction.
That comparison is mathematically invalid for the canonical odd-activation
model:

- \(P=5,15,35,70,126\) are the complete Hermite spaces through degrees
  \(1,2,3,4,5\);
- exact sign equivariance makes every even-degree shell dynamically inert;
- therefore \(P=5\) and \(P=15\) are the same exact PDE, as are \(P=35\) and
  \(P=70\);
- the old \(5\leftarrow15\) denominator should be zero, while
  \(15\leftarrow35\) contains the first genuine cubic correction.

The old ratios \(2.54\)–\(26.53\) were consequently ratios against numerical
symmetry leakage, not evidence of divergence.

After enforcing the exact parity symmetry in the Gaussian cubature:

- \(P=5\) and \(P=15\) agreed to \(10^{-17}\) at positive training times;
- on the correct odd-degree ladder \(P=5\to35\to126\), the outgoing generator
  residual contracted by factors of \(31\)–\(34\) at \(t=0.25\) in two
  independent cubature scrambles, and by a factor of \(17\) at \(t=0.5\);
- actual observable differences and observable-generator defects remained
  between \(10^{-5}\) and \(3\times10^{-4}\) in the project's normalized
  metric.

One issue remains: aggregate high-to-low feedback grew by roughly
\(39\%\)–\(46\%\) at \(t=0.25\), and its normalized observable effect grew by
\(42\%\)–\(64\%\). The same tension persisted at \(t=0.5\). There are 56
quintic modes but only 20 cubic modes; per mode, most degree-five shell
quantities decreased, while their aggregate did not yet decrease.

The defensible conclusion is therefore

\[
\boxed{\text{The reported Hermite obstruction was a fixable diagnostic flaw.}}
\]

\[
\boxed{\text{The corrected outgoing Hermite tail contracts strongly.}}
\]

\[
\boxed{\text{Arbitrary-accuracy convergence still needs high-to-low tail
control.}}
\]

This is evidence for a **bridgeable, pre-asymptotic approximation gap**, not a
fundamental unbridgeable failure. It is not a complete proof that the pure
Hermite hierarchy converges for all accuracy levels.

## 1. Exact parity lemma

Let \(\theta=(B(0),a(0)/A)\in\mathbb R^4\), let
\(\phi_\nu\) be a Hermite function of total degree \(|\nu|\), and define

\[
J_{\nu\nu}=(-1)^{|\nu|}.
\]

For odd \(\sigma=\tanh\), even \(\sigma'\), and the symmetric Gaussian
initialization, the operator PDE is equivariant under

\[
(B,a,\rho^\theta)
\longmapsto
\bigl(-B(-\theta),-a(-\theta),J_\#\rho^{-\theta}\bigr).
\]

The output \(f=\int ah\,d\mu\), and hence the residual \(e=f-y\), is invariant.
Arbitrary fixed inputs and asymmetric/nonzero labels do not break this
symmetry. The initialization is fixed by the transformation, so uniqueness
gives

\[
B(-\theta)=-B(\theta),\quad
a(-\theta)=-a(\theta),\quad
h_q(-\theta)=-h_q(\theta),\quad
p_q(-\theta)=-p_q(\theta).
\]

Consequently,

\[
H_{\nu q}
=\langle\phi_\nu,h_q\rangle
=(-1)^{|\nu|+1}H_{\nu q},
\]

and \(H_{\nu q}=0\) for every even \(|\nu|\). Since

\[
V_\nu=-\gamma\sum_q e_q\beta_qH_{\nu q},
\]

the even-degree learned row coordinates have zero velocity. Their centered
Gaussian initialization remains inert, and their transpose contribution
vanishes.

For four latent coordinates:

| Maximum Hermite degree | Full \(P\) | Active odd modes |
|---:|---:|---:|
| 1 | 5 | 4 |
| 2 | 15 | 4 |
| 3 | 35 | 24 |
| 4 | 70 | 24 |
| 5 | 126 | 80 |

Thus the nontrivial ladder is

\[
P=5\to35\to126,
\]

or \(4\to24\to80\) after deleting inert coordinates.

## 2. Why the earlier evidence was misleading

The earlier fast Sobol rule was centered and whitened, but not paired under

\[
\varepsilon_\nu\mapsto(-1)^{|\nu|}\varepsilon_\nu.
\]

It therefore did not integrate the exact nonlinear sign symmetry. Training
could turn its small parity leakage into a nonzero \(5\leftarrow15\) defect.
That defect was used as the denominator in the reported noncontraction ratio.

This also qualifies the earlier rank-five POD comparison. The first five
Hermites contain only four active linear modes plus one inert constant. A
rank-five POD basis can choose five active mixtures, including cubic content.
Its improvement was real, but it was not an equal-active-rank comparison and
cannot by itself diagnose static-basis inefficiency versus missing history.

## 3. Bounded experiment

The scientific vector field was not changed. A small diagnostic wrapper:

1. paired fast Gaussian points under the exact Hermite-parity map;
2. used a symmetric tensor Gauss-Hermite base rule;
3. evolved only the levels needed for the requested comparison;
4. measured outgoing residual, high-to-low feedback, observable-generator
   defect, observable distance, and degree-shell norms;
5. omitted shadows, random bases, tangent gains, bootstraps, and broad grids.

### 3.1 Even-shell null

Configuration:

\[
N=4,\quad M=625,\quad R=128,\quad \Delta t=0.04,
\quad t\in\{0.25,0.5\}.
\]

| Time | \(P5\)-\(P15\) observable distance | \(R_{\rm back}\) | \(R_{\rm out}\) |
|---:|---:|---:|---:|
| 0.25 | \(2.19\times10^{-17}\) | \(3.51\times10^{-17}\) | \(2.00\times10^{-17}\) |
| 0.50 | \(1.60\times10^{-17}\) | \(2.22\times10^{-17}\) | \(9.69\times10^{-18}\) |

Quadratic state, velocity, forward, and adjoint shell norms were likewise at
roundoff. This directly validates the parity lemma in the discretized solver
and falsifies the old use of \(5\leftarrow15\) as a physical truncation step.

### 3.2 Correct odd-shell ladder

The degree-five run used a base rule exact for degree-five Hermite Gram
products:

\[
N=4,\quad M=6^4=1296,\quad R=256,\quad \Delta t=0.05.
\]

Seed 20260723 was run through \(t=0.5\). Seed 20260724 was run only through
\(t=0.25\), according to the hard stop rule.

#### Generator results

| Seed/time | Quantity | \(5\leftarrow35\) | \(35\leftarrow126\) | Ratio |
|---|---|---:|---:|---:|
| 20260723, 0.25 | outgoing residual | \(1.9743\times10^{-4}\) | \(5.7237\times10^{-6}\) | **0.0290** |
| 20260724, 0.25 | outgoing residual | \(2.0991\times10^{-4}\) | \(6.7174\times10^{-6}\) | **0.0320** |
| 20260723, 0.50 | outgoing residual | \(3.1202\times10^{-4}\) | \(1.8381\times10^{-5}\) | **0.0589** |
| 20260723, 0.25 | high-to-low state feedback | \(6.5919\times10^{-3}\) | \(9.1541\times10^{-3}\) | 1.389 |
| 20260724, 0.25 | high-to-low state feedback | \(7.0412\times10^{-3}\) | \(1.0287\times10^{-2}\) | 1.461 |
| 20260723, 0.50 | high-to-low state feedback | \(4.3824\times10^{-3}\) | \(6.2354\times10^{-3}\) | 1.423 |
| 20260723, 0.25 | normalized observable-generator defect | \(3.8829\times10^{-5}\) | \(5.5307\times10^{-5}\) | 1.424 |
| 20260724, 0.25 | normalized observable-generator defect | \(4.3204\times10^{-5}\) | \(7.1013\times10^{-5}\) | 1.644 |
| 20260723, 0.50 | normalized observable-generator defect | \(1.5328\times10^{-4}\) | \(2.6961\times10^{-4}\) | 1.759 |

#### Actual observable differences

| Seed/time | \(P5\)-\(P35\) distance | \(P35\)-\(P126\) distance | Ratio |
|---|---:|---:|---:|
| 20260723, 0.25 | \(2.1092\times10^{-5}\) | \(3.1104\times10^{-5}\) | 1.475 |
| 20260724, 0.25 | \(2.3591\times10^{-5}\) | \(3.9947\times10^{-5}\) | 1.693 |
| 20260723, 0.50 | \(5.2961\times10^{-5}\) | \(7.9425\times10^{-5}\) | 1.500 |

These differences are \(0.0021\%\)–\(0.0079\%\) of the fixed observable
scale. The nonmonotone ordering matters for an arbitrary-accuracy theorem,
but not for the existing \(5\%\) practical claim.

### 3.3 Shell multiplicity

The cubic shell has 20 modes and the quintic shell 56. Dividing shell norms
by the square root of the shell size gives the following degree-five versus
degree-three ratios:

| Seed/time | learned state \(c\) | velocity \(\dot c\) | forward coefficients | adjoint coefficients |
|---|---:|---:|---:|---:|
| 20260723, 0.25 | 0.691 | 0.656 | 0.708 | 0.924 |
| 20260724, 0.25 | 0.716 | 0.697 | 0.751 | 1.001 |
| 20260723, 0.50 | 0.634 | 0.573 | 0.640 | 0.939 |

Most per-mode quantities contract; aggregate high-to-low feedback does not
yet contract because the shell widens substantially. Per-mode normalization
is diagnostic only: convergence in the Hilbert norm still requires control of
the full aggregate shell.

## 4. The repair

The concrete compiler should be reduced to odd Hermite modes from the start.
Numerically, its Gaussian cubature should be paired under \(J\). This:

- removes identically inert coordinates;
- prevents parity leakage from masquerading as a truncation residual;
- replaces the incorrect \(5,15,35,70\) test ladder by \(5,35,126\);
- reduces the degree-five learned source dimension from 126 to 80.

This repair preserves the same canonical PDE and all orientation/transpose
identities. It is not a fitted basis and uses no trajectory information.

## 5. What the theory now needs

The remaining compact-time proof has a standard Galerkin form. Let
\(\Pi_K\) project onto odd Hermite degrees through \(2K+1\). If:

1. the infinite parity-reduced operator PDE is well posed on \([0,T]\);
2. its vector field is locally Lipschitz with trajectory bound \(L_T\);
3. the aggregate outgoing/high-to-low residual
   \(\eta_K(T)\) tends to zero;

then a Grönwall estimate has the schematic form

\[
\sup_{t\le T}\|Y_K(t)-Y(t)\|
\le
e^{L_TT}
\left(
\|Y_K(0)-\Pi_KY(0)\|+\eta_K(T)
\right).
\]

Hermite completeness supplies pointwise projection convergence for fixed
square-integrable queries. The missing mathematical step is uniform
trajectory compactness and high-to-low commutator control strong enough to
make \(\eta_K(T)\to0\). The new experiment supports the outgoing part and
does not yet support aggregate feedback contraction.

The broader response-enriched route remains a fallback. Earlier finite-matrix
response experiments improved by roughly one to two orders of magnitude per
response grade through \(K=3\), but they retained dense matrices and are not
an implemented width-independent PDE. They are mechanism evidence, not the
resolution of the present Hermite gate.

## 6. Evidence ledger

| Question | Resolution after this round |
|---|---|
| Was the old \(15\leftarrow35\) noncontraction ratio valid evidence against Hermite convergence? | **No. Settled.** Its comparator is an exactly inert even shell. |
| Can the numerical symmetry defect be fixed cheaply? | **Yes. Settled.** Parity-paired cubature gives \(P5=P15\) to \(10^{-17}\). |
| Does the first proper outgoing odd-Hermite tail contract? | **Yes, strongly in this diagnostic.** \(31\)–\(34\times\) at \(t=0.25\), replicated across two seeds. |
| Does aggregate high-to-low feedback already contract at degree five? | **No.** It grows at this first proper step, although its observable effect is tiny. |
| Is this evidence of a fundamental unbridgeable closure failure? | **No.** There is no projectability witness, no large same-state continuation gap, no outgoing-tail failure, and no instability. |
| Is arbitrary-accuracy pure-Hermite convergence proved? | **No.** The aggregate feedback tail remains the decisive unresolved theorem obligation. |
| Is a useful low-order finite PDE supported? | **Yes, more strongly than before.** The prior adverse hierarchy argument is removed without changing the successful \(P=5\) model. |

## 7. Budget and exclusions

Admissible positive-time scientific runs used approximately 331 seconds:

- parity-null test: 23.3 s;
- primary odd ladder: 212.2 s;
- independent-seed checkpoint: 95.3 s.

About 31 additional seconds were spent on zero-time feasibility checks and
one discarded run using the wrong all-coordinate sign pairing. That discarded
run is excluded from every scientific conclusion.

No broad resolution grid, \(P=70\) run, shadow campaign, response compiler,
tangent gain, bootstrap, or dense-network campaign was launched.

## Final conclusion

The highest-leverage uncertainty has been resolved asymmetrically:

> The specific “Hermite defects worsen with \(P\)” obstruction raised by the
> lean salvage study was not fundamental. It came from comparing a
> symmetry-forbidden quadratic shell with the first active cubic shell.
> An exact odd-mode reduction fixes the compiler and the diagnostic, and the
> corrected outgoing tail contracts very strongly.

What remains is narrower:

> The degree-five shell has not yet entered an aggregate high-to-low
> contraction regime. Proving or numerically observing that aggregate tail
> decay—not inventing a wholly new PDE—is now the central pure-Hermite gap.

Accordingly, the evidence favors **bridgeable/fixable** over
**fundamental/unbridgeable**, while stopping short of claiming that the full
arbitrary-accuracy conjecture is proved.
