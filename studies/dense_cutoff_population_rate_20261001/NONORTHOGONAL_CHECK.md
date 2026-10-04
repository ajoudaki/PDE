# Check of the attempt to remove input orthogonality

2026-10-02. Internal mathematical reconstruction, not a promotion review.

The user's requested extension is the original, unclipped, same-width
closure-versus-dense prediction bound for general fixed input geometry.
**That extension remains open.** The unconditional advance is a bound on
the accumulated defect in the closure's parameter differential equation.
The prediction comparison below is explicitly conditional on a finite
carrier-tail estimate not proved for general geometry.

## Inputs and check scope

The coordinator read both complete candidates below, the complete current
`paper/proof_tracking.tex`, the complete initialization/projection/fitting
portion of `paper/proof_alltime.tex`, and the exact network setting in
`paper/main.tex`. The full manuscript had been read earlier; the source
hashes relevant here are unchanged. The complete own-study finite-tail
proof and its original check were also read. No other study was accessed.

The direct-route author and tail-route author started separate scoped
attempts. During the attempt the coordinator passed the direct route's
weaker sufficient tail target to the tail route. They are collaborators,
not isolated promotion reviewers. A further scoped checker, who had
previously checked the same-width implication, received a self-contained
statement of the new source calculation and conditional exponent argument.
It reconstructed both without accessing these candidates. The coordinator
checked their actual manuscript hypotheses and complete written versions.

## 1. Arbitrary-geometry defect bound: PASS

There are two tanh hidden layers, fixed finite inputs, the manuscript's
positive initial **feature**-Gram gap, zero readout, small fixed label RMS
\(Y\), and the actual autonomous learning-speed closure at every order.
No raw input Gram invertibility or orthogonality is needed for this part.
On the common initialized event the manuscript proves fitting and the
physical speed bounds before making a dense comparison.

The only stored backward history is
\(b_a^{(2)}=(r_a/\rho)\delta_a^{(2)}\), where
\(\delta_a^{(2)}=w\odot\operatorname{sech}^2 z_a^{(2)}\).
The readout equation gives \(\|w\|_\infty\le 2Y/\kappa\). Therefore
\[
\frac{\|\dot\delta_a^{(2)}\|_2}{\sqrt n}
\le \frac{\|\dot w\|_2}{\sqrt n}
 +2\|w\|_\infty\frac{\|\dot z_a^{(2)}\|_2}{\sqrt n}
\le C\rho,
\qquad
\frac{\|\dot b_a^{(2)}\|_2}{\sqrt n}\le C(Y+\rho).
\]
This calculation never differentiates the first-layer gate and never
uses an individual first-layer carrier bound.

For a history frozen after physical time \(T\), the clock-weighted
derivative energy is at most \(CY^2(1+T)\). Indeed, after changing
variables \(d\xi=\rho(s)ds\), its integrand has the factor
\(\tau(s)(A-\tau(s))/\rho(s)\le \sup_t\tau(t)/\kappa\).
The remaining clock mass is at most \(CY e^{-\kappa T}\), so the freeze
error in normalized history \(L^2\) is at most
\(CY^{3/2}e^{-\kappa T/2}\). The zero readout makes the prefix join
continuous. On each fixed finite horizon the positive residual makes the
frozen history an admissible \(H^1\) input for the projection lemma.

Multiplication by the already proved forward history tail
\(CY^{3/2}/q\) in the exact absolute-defect identity gives
\[
\int_0^\infty\|E_2(t)\|_Fdt
\le C\left[
Y^{5/2}\frac{\sqrt{1+T}}{q^2}
 +Y^3\frac{e^{-\kappa T/2}}q\right].
\]
The left side is the discrepancy in the hidden-matrix velocity between
the closure and the dense vector field evaluated **at the closure state**.
It is not a distance between their separately evolved trajectories.
Taking \(T=2\log q/\kappa\) (including \(T=0\) for \(q=1\)) proves
\[
\int_0^\infty\|E_2(t)\|_Fdt
\le CY^{5/2}q^{-2}\sqrt{\log(e+q)}.
\]
Increasing finite terminal times is valid because the left side is
nondecreasing and the right side is uniform. The case \(Y=0\) is
stationary and is handled without dividing by the residual.

## 2. Conditional prediction consequence: PASS, hypothesis open

Retaining the activity dependence in the manuscript's integrating factor
gives \(D\le C e^{C_0YM}(\epsilon_q+Z_n(M))\), where \(D\) is the
all-time normalized parameter discrepancy and \(Z_n\) is the residual-
weighted dense carrier tail. All deterministic constants can be uniform
over the fixed small-label interval.

If on one probability-\(1-\delta\) event
\[
Z_n(YR)\le B_\delta Y^2e^{-a_0R}
\]
holds simultaneously at all integer \(R\) above a fixed threshold, put
\(\theta=1-C_0Y^2/a_0>0\). Balancing its exponential against
\(\epsilon_q\) yields
\[
D\le C_{\delta,Y}q^{-2\theta}
 [\log(e+q)]^{\theta/2}.
\]
Rounding the cutoff changes only a fixed prefactor. Any lower cutoff
restriction and the finitely many small orders are absorbed using the
common physical bound. With
\[
q_n=\left\lceil n^{1/(4\theta)}[\log(e+n)]^{1/4}\right\rceil,
\]
the logarithmic factors cancel and the result is at most
\(C_{\delta,Y}/\sqrt n\). It uses \(q_n=o(n)\) when
\(\theta>1/4\). The manuscript's whole-input estimate transfers this
to the time-supremum prediction norm for fixed test laws with finite
second moment. None of these implications establishes their tail input.
Pointwise confidence statements for each cutoff do not suffice: the
tail envelope must be simultaneous, or supplied with a valid summable
probability argument.

## 3. Exact reductions and obstructions: checked within their scope

The tail route's carrier evolution follows by separately expanding
\(dW^\top\delta_a\), \(W^\top\operatorname{diag}(\gamma_a)dw\),
and \(W^\top\operatorname{diag}(w\odot\gamma'_a)dz_a^{(2)}\).
Its affine carrier coefficients have bounded operator norm \(CS\),
but their adaptive dependence prevents an independent-Gaussian argument.

The rescaling \(H=\sqrt n W\) makes the controlled dynamics the
ordinary Euclidean gradient of \(nf_a\) in \((A,H,w)\). The only
potentially unbounded Hessian blocks are indeed neuron-local, proportional
to \(k_{a,i}\tanh''(z_{a,i}^{(1)})v_av_a^\top\). The other blocks
are bounded using the coordinate bound on \(w\), bounded slopes, and
\(\|W\|_{\rm op}\). This is a location of the difficulty, not a
bound on the resulting averaged response.

The nonzero Lie bracket of two correlated, nonparallel input vector
fields precludes simultaneously mapping both to constant vector fields.
It does not preclude another probabilistic proof. The localized Gaussian
integration-by-parts identity retains its localization derivative and
exhibits the missing tilted response trace/directional response. No
derivative of a hard good-event indicator was silently discarded.

The direct route's explicit loss-Hessian example also checks algebraically:
its individual carrier is of order \(-Y\sqrt n\), its residual is
negative of order \(Y\), and its positive Jacobian term stays \(O(Y^2)\).
Its negative curvature is therefore \(-cY^2\sqrt n+O(Y^2)\).
This is an arbitrary admissible tube state, not a Gaussian-initialized
trajectory or a negative approximation-rate example.

## Frozen versions

```text
5619965ad3ea85c186385951d07f59f3fe7e01c0f52b5b7710de65ba38896522  NONORTHOGONAL_DIRECT_ROUTE.md
6ce0d9034b92d5a80afffe5053b833a102660015875ebf8e86b113cfa90c3134  NONORTHOGONAL_TAIL_ROUTE.md
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be  paper/proof_tracking.tex
```

No experiments, manuscript edits, or Git writes were performed. These
checks preserve the original orthogonal theorem and establish the new
general-geometry source bound, while leaving general-geometry prediction
tracking unresolved.
