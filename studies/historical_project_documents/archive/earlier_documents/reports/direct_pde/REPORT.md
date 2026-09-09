# Direct neural-PDE simulation report

## Bottom line

An actual width-independent PDE has now been integrated for the canonical
continuous-depth, fully dense, unconstrained Euclidean \(\mu\)P ResNet.

This is the first experiment in this project that passes the literal PDE
test:

- the dynamical law has no network width \(n\);
- it stores no \(n\times n\) matrix;
- its velocity is derived from the architecture and current PDE moments;
- it never reads dense-network curves;
- it is autonomous and restartable;
- it preserves the same \(W/W^\top\) orientation through an exact shared
  transpose;
- independent characteristic implementations agree to numerical precision.

The PDE predicts the loss, all three outputs, and the complete
time-by-depth \(3\times3\) hidden-Gram field through the fitted plateau.
Against a preregistered 128-network \(n=256,L=32\) ensemble, the maximum
discrepancy in the
entire Gram-*evolution* surface is

\[
7.243\times10^{-3},
\]

while the feature motion being predicted is

\[
6.338\times10^{-1}\quad\text{(PDE)},\qquad
6.399\times10^{-1}\quad\text{(dense ensemble)}.
\]

Thus the curvewise Gram-evolution discrepancy is about \(1.14\%\) of the feature
motion. The maximum loss-curve discrepancy, using the loss of the dense
ensemble-mean predictor, is

\[
1.846\times10^{-3}.
\]

The curves are visually close; see
`figures/pde_vs_dense_curves.png`.

This is strong direct numerical consistency evidence for a neural PDE. It
is not yet a proof that this PDE is the exact ordered \(n\to\infty\), then
\(L\to\infty\) limit. The independent held-out bootstrap audit *does*
resolve the \(P=5\) discrepancy from Monte Carlo error in this finite
\(n=256,L=32\) reference; it does not determine whether that discrepancy is
caused by finite width, finite residual depth, finite PDE order, or
cubature.

## 1. What PDE was actually solved

The earlier \(K/J/N\) response-word note does not emit an executable PDE:
\(J_*\), the retained tag and history tables, the Gaussian kernel
\(\Gamma\), and the finite drift DAGs are not enumerated. It therefore
cannot honestly be simulated without adding new closure choices.

The successful equation is a new, explicit **Hermite/isonormal
operator-Galerkin Liouville PDE** for the same canonical dense model.
After the width limit, an iid dense row is projected onto \(P\) fixed
Hermite functions of the immutable neuron type
\(\theta=(B_i(0),a_i(0))\). The conditional law of its \(P\) total row
coefficients \(w\) obeys

\[
\partial_t\rho_{s,t}^{\theta}
+\nabla_w\cdot\left(\rho_{s,t}^{\theta}V\right)=0,
\]

\[
V_j
=-\gamma\sum_q e_q\,
\beta_q\langle\phi_j,h_q\rangle.
\]

The slow hidden field and adjoint solve coupled forward/backward depth
equations. The same \(w_j\)'s define both \(W_P\) and \(W_P^\ast\), so
transpose reuse and the projected Onsager term are exact.

The full derivation is in `theory/operator_galerkin_pde.md`.

The primary compiler/solver settings are

\[
P=5,\qquad N=16,\qquad M=256,\qquad R=128,
\]

where \(P\) is Hermite order, \(N\) is depth resolution, and \(M,R\) are
base-label and Gaussian-row cubature resolutions. The augmented
characteristic representation has 14 scalar coordinates per depth
location; the equivalent conditional law in total row coefficient \(w\)
has 9. These numbers are independent of \(n\), \(L\), and the requested
training horizon.

## 2. PDE versus dense dynamics

The main curvewise comparisons are:

| Dense reference | Max output gap | Max loss-of-mean gap | Max absolute Gram gap | Max Gram-increment gap | Dense feature motion |
|---|---:|---:|---:|---:|---:|
| \(n=64,L=32\), 64 seeds | \(4.311\times10^{-2}\) | \(2.066\times10^{-2}\) | \(9.001\times10^{-2}\) | \(2.464\times10^{-2}\) | \(6.419\times10^{-1}\) |
| \(n=128,L=32\), 96 seeds | \(1.818\times10^{-2}\) | \(3.778\times10^{-3}\) | \(4.115\times10^{-2}\) | \(9.255\times10^{-3}\) | \(6.285\times10^{-1}\) |
| \(n=256,L=32\), 64 seeds | \(1.708\times10^{-2}\) | \(1.498\times10^{-3}\) | \(2.787\times10^{-2}\) | \(6.731\times10^{-3}\) | \(6.392\times10^{-1}\) |
| \(n=256,L=32\), 128 seeds | \(1.075\times10^{-2}\) | \(1.846\times10^{-3}\) | \(1.941\times10^{-2}\) | \(7.243\times10^{-3}\) | \(6.399\times10^{-1}\) |
| \(n=256,L=64\), 64 seeds | \(1.660\times10^{-2}\) | \(3.318\times10^{-3}\) | \(3.766\times10^{-2}\) | \(6.564\times10^{-3}\) | \(6.386\times10^{-1}\) |
| \(n=512,L=32\), 16 seeds | \(2.398\times10^{-2}\) | \(1.987\times10^{-2}\) | \(3.868\times10^{-2}\) | \(9.897\times10^{-3}\) | \(6.351\times10^{-1}\) |

The absolute Gram comparison contains static finite-width initialization
noise. The increment comparison subtracts each system's own initialization
and directly tests the learned feature trajectory. Its improvement with
width is the cleaner signal.

At \(n=256\), increasing dense depth from \(L=32\) to \(L=64\) changes the
mean Gram-increment surface by only

\[
4.226\times10^{-3}.
\]

The \(P=5\) PDE's \(L=64\) Gram-increment gap is
\(6.564\times10^{-3}\) against the pooled 64-seed reference. The held-out
width comparison changes the dense Gram-increment surface by
\(9.350\times10^{-3}\) from \(n=256\) to \(n=512\) at \(L=32\).

These are Cauchy diagnostics rather than extrapolated limits. Under the
preregistered curvewise bootstrap, neither the width nor depth Cauchy gap is
statistically resolved at 5%: their pooled/stratified 95% thresholds are
\(9.967/10.306\times10^{-3}\) and
\(8.568/8.978\times10^{-3}\), respectively. The current sampling noise is
therefore still large enough to prevent identifying the ordered
width-then-depth limit.

## 3. Genuine global-time prediction

The primary PDE was integrated through the full active transient to \(t=8\)
and then restarted from its hashed autonomous state and continued to
\(t=32\).

Over \(8\le t\le32\):

| Plateau quantity | Maximum |
|---|---:|
| output drift from \(t=8\) | \(4.996\times10^{-13}\) |
| all-depth Gram drift from \(t=8\) | \(4.236\times10^{-13}\) |
| tangent-kernel drift | \(4.168\times10^{-13}\) |
| residual norm | \(4.996\times10^{-13}\) |
| \(|\dot{\mathcal L}|\) | \(8.253\times10^{-25}\) |

This is not a local Taylor experiment. One fixed PDE is integrated from
initialization through fitting and then for 24 additional units of flat
tail. No approximation order is increased and no target curve is queried.

## 4. Numerical convergence of the PDE itself

### Time integration

Three RK4 resolutions and an independent second-order Heun integrator give:

| Comparison | Output | All-depth Gram | Tangent kernel |
|---|---:|---:|---:|
| RK4 \(dt=.02\) vs \(.01\) | \(6.826\times10^{-8}\) | \(1.090\times10^{-7}\) | \(3.559\times10^{-7}\) |
| RK4 \(dt=.01\) vs \(.005\) | \(4.179\times10^{-9}\) | \(6.670\times10^{-9}\) | \(2.177\times10^{-8}\) |
| Heun vs RK4 at \(dt=.005\) | \(1.727\times10^{-5}\) | \(1.555\times10^{-5}\) | \(4.442\times10^{-5}\) |

### Depth discretization

Against \(N=32\):

| Depth order | Output | All-depth Gram | Tangent kernel |
|---:|---:|---:|---:|
| \(N=8\) | \(6.108\times10^{-4}\) | \(2.521\times10^{-3}\) | \(1.970\times10^{-2}\) |
| \(N=16\) | \(2.051\times10^{-4}\) | \(8.449\times10^{-4}\) | \(6.628\times10^{-3}\) |

### Cubature

Relative to the primary \(M=256,R=128\) run:

| Cubature | Output | All-depth Gram | Tangent kernel |
|---|---:|---:|---:|
| \(M=64,R=32\) | \(7.330\times10^{-3}\) | \(1.274\times10^{-2}\) | \(1.214\times10^{-1}\) |
| \(M=128,R=64\) | \(3.586\times10^{-3}\) | \(6.382\times10^{-3}\) | \(1.012\times10^{-1}\) |
| \(M=512,R=128\) | \(1.526\times10^{-4}\) | \(7.832\times10^{-4}\) | \(6.323\times10^{-3}\) |
| \(M=256,R=256\) | \(1.118\times10^{-4}\) | \(1.160\times10^{-3}\) | \(6.321\times10^{-3}\) |

Three independent primary-resolution QMC scrambles have maximum radii

\[
1.32\times10^{-3}\ \text{pairwise in output},\qquad
2.13\times10^{-3}\ \text{pairwise in all-depth Grams}.
\]

An independent tensor Gauss--Hermite implementation agrees with the main
implementation to \(2.78\times10^{-16}\) in outputs and
\(8.88\times10^{-16}\) in every Gram entry when both use the same cubature.
The low-order GH3 rule itself differs from the refined QMC result by
\(1.94\times10^{-2}\) in Grams, so it is retained as an implementation
cross-check, not as the primary accuracy result.

### Operator-order and cubature-method audit

The original \(P=35,M=64,R=64\) pilot is explicitly excluded: its raw base
and fast cubature condition numbers are 371 and 98.8.

A clean complete-quadratic level was then run. \(P=15\) contains exactly all
four-variate Hermites through total degree two. At refined
\(M=256,R=128\), changing \(P=5\to15\) changes outputs by
\(1.152\times10^{-3}\), all-depth Grams by
\(2.814\times10^{-3}\), and the tangent kernel by
\(2.225\times10^{-2}\).

To remove the finite-Sobol basis-whitening confound, an independent hybrid
solver uses exact order-three tensor Gauss--Hermite quadrature only in the
four-dimensional immutable neuron label and Sobol characteristics in the
15-dimensional row innovation. Its base Hermite Gram defect is
\(9.1\times10^{-16}\). Under this clean nested basis:

| Comparison | Output | All-depth Gram | Tangent kernel |
|---|---:|---:|---:|
| hybrid \(P=5\) vs \(P=15,R=128\) | \(1.124\times10^{-3}\) | \(2.761\times10^{-3}\) | \(2.070\times10^{-2}\) |
| hybrid \(P=15,R=128\) vs \(R=256\) | \(6.045\times10^{-4}\) | \(9.648\times10^{-4}\) | \(7.680\times10^{-3}\) |
| hybrid \(P=15,R=256\) vs refined-QMC \(P=15\) | \(5.654\times10^{-4}\) | \(7.573\times10^{-4}\) | \(1.250\times10^{-2}\) |

The two \(P=15\) methods therefore agree well in the Gram observable.
However, \(P=15\) does **not** improve the finite-reference match:

| PDE | Gram-increment gap to \(n=256,L=32,S=128\) | Fraction of PDE feature motion |
|---|---:|---:|
| refined-QMC \(P=5\) | \(7.243\times10^{-3}\) | \(1.143\%\) |
| refined-QMC \(P=15\) | \(9.202\times10^{-3}\) | \(1.457\%\) |
| hybrid \(P=5\) | \(7.540\times10^{-3}\) | \(1.190\%\) |
| hybrid \(P=15,R=256\) | \(9.223\times10^{-3}\) | \(1.460\%\) |
| hybrid \(P=35,R=128\), cubic stress | \(1.373\times10^{-2}\) | \(2.192\%\) |

Thus the finite PDE remains close at both compiler levels, and the
quadratic correction is small and reproducible, but the first clean
operator-order refinement moves in the wrong direction for this finite
dense reference. This is an explicit negative result: the current data do
not establish \(P\to\infty\) convergence toward the dense curves.

The complete-cubic \(P=35\) execution uses order-four Gauss--Hermite in the
base label, giving basis Gram condition \(1+8\times10^{-15}\), and passes
all algebraic/PSD/plateau checks. Its row-innovation rule has raw condition
6.20, however, and no preregistered \(R\)-refinement. Its continued motion
away from the finite dense reference is therefore reported as directional
stress evidence, not as a clean third point of a cofinal \(P\)-limit. No
post-outcome \(P=35,R=256\) run was added.

## 5. Algebraic and anti-cheat audits

Independent audits found:

- shared \(W/W^\top\) transpose pairing defect at numerical roundoff;
- generic positive-time coordinate-gradient defects at most
  \(1.41\times10^{-11}\);
- energy identity defect \(7.62\times10^{-13}\);
- \(\dot f=-\Theta_Pe\) defect at most \(1.70\times10^{-10}\) over 20
  random states;
- \(\Theta_P\succeq0\) in all tested states;
- direct versus split/restarted integration agreement
  \(4.44\times10^{-16}\);
- an intentional independent-transpose mutation is detected by the
  orientation test;
- a positive-time PDE state accepts changed labels without consulting its
  prior trajectory;
- wrong-seed, same-shape restarts rejected by a static
  compiler/quadrature hash;
- no call from the PDE source to dense reference files;
- no width \(n\) or dense \(W\) state in the PDE.

The canonical post-simulation hostile report is
`agent_outputs/final_adversarial_pde_audit.md`. The earlier
`agent_outputs/adversarial_audit.md` is preserved as the historical audit
that rejected the old finite-matrix surrogate and specified the acceptance
gates.

The independent statistical report, code, bootstrap tables, and raw
discrepancy decompositions are under `agent_outputs/statistical_audit/`.
Against the preregistered \(n=256,L=32,S=128\) reference, the curvewise
Gram-increment gap is \(7.243\times10^{-3}\). The pooled and
block-stratified 95% bootstrap thresholds are respectively
\(5.062\times10^{-3}\) and \(4.981\times10^{-3}\), with
\(p\approx0.0030\) and \(p\approx0.0035\). The nonzero finite-reference
gap is therefore statistically resolved. Leave-one-block-out gaps remain
between \(6.73\times10^{-3}\) and \(7.85\times10^{-3}\), so this conclusion
is not driven by one seed block.

The separately frozen ordered-limit audit then added two exact-network
blocks without changing the PDE. Against the pooled
\(n=256,L=64,S=64\) reference, the \(P=5\) gap is
\(6.564\times10^{-3}\), below both 95% thresholds
\(7.073\times10^{-3}\) and \(7.112\times10^{-3}\)
(\(p\approx0.077/0.080\)). Against the smaller
\(n=512,L=32,S=16\) block, the gap is \(9.897\times10^{-3}\), narrowly
above its \(9.216\times10^{-3}\) threshold (\(p\approx0.028\)).

These apparently different finite-grid decisions are compatible with the
same conclusion: the PDE is close, but finite-network sampling and
width/depth bias have not been separated. Moreover, \(P=15\) is
statistically farther than \(P=5\) against all three pooled/held-out
references under the preregistered signed-improvement test. The frozen
protocol, all 2,000-replicate bootstrap distributions, and every decision
table are in `agent_outputs/statistical_audit/`.

## 6. Evidence for the depth-homogenization step

The PDE replaces centered fast depth noise by its conditional mean while
retaining the shared-transpose/Onsager component. This is valid only if the
centered row and column innovations average away under \(1/L\) residual
scaling.

Paired dense runs share \(B(0)\) and \(a(0)\) but independently redraw all
\(W_\ell\). Across \(L=8,16,32,64\), their conditional variances have the
following log--log slopes:

| Field | initialization | after training to \(t=0.5\) |
|---|---:|---:|
| hidden \(H\) | \(-1.0193\) | \(-1.0039\) |
| adjoint \(P(0)\) | \(-0.9993\) | \(-0.9924\) |

Thus both variances scale as \(1/L\), or RMS \(L^{-1/2}\), exactly as the
homogenized PDE requires. This is numerical evidence, not a propagation-of-
chaos proof.

## 7. Precise conclusion

The direct simulation question now has a positive answer:

\[
\boxed{
\text{a genuine finite, autonomous, width-independent neural PDE was
simulated and it tracks the dense Euclidean \(\mu\)P curves through plateau.}
}
\]

The strongest observed agreement is the full Gram-evolution surface:
approximately \(1.14\%\) discrepancy relative to nonlazy feature motion.
Time and depth error are well below this scale, while QMC scramble spread is
about \(2.1\times10^{-3}\) and basis/cubature-method systematics require
further refinement. The held-out width/depth Cauchy gaps are not
statistically resolved, so the experiment cannot yet decide whether the
small PDE discrepancy vanishes in the ordered dense limit. The first
complete quadratic compiler refinement is statistically farther from each
audited finite reference, so the current evidence does not establish a
convergent finite-\(P\) hierarchy.

What remains open is mathematical identification:

\[
\boxed{
\text{prove trained iid-depth homogenization and }P\to\infty
\text{ Hermite convergence for the canonical dense limit.}
}
\]

Accordingly, these experiments are strong, audited consistency evidence for
the central PDE thesis, not a proof of the original all-time conjecture or a
demonstration of arbitrary-accuracy convergence.
