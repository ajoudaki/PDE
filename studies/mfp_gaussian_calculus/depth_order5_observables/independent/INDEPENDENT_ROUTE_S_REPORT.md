# Independent Route S: amortized hidden-RMS `Gamma_04` head

## Bottom line

For every separately fixed hidden depth `H`, after the audited universal
feature-ascent backbone has completed `F1,R1,F2,R2,F3,R3`, the missing
hidden-activation RMS quantity

\[
 \gamma^\ell_{04}=\Gamma^\ell_{04}
 =\lim_{n\to\infty}\mathbb E\,n^{-1}
   \langle X_{\ell}^{(0)},X_{\ell}^{(4)}\rangle
\]

closes in exactly one additional nearest-neighbour forward pass.  The
smallest state found has two dynamic scalars,

\[
 \boxed{(\gamma_{04},a_{41})},
\]

independent of `H`; no minimality claim is made.  The transition contains
only deterministic arithmetic, existing backbone states, and the declared
one-dimensional `M` atoms.  The full literal 64-term/17-term transition is
frozen in `FROZEN_GAMMA04_REDUCED_TRANSITIONS.md`.

This Route-S producer was frozen before Route A was inspected.  The two
producer maps subsequently agreed exactly: `83/20/1` terms before eliminating
the redundant third coordinate and zero sparse-monomial discrepancies.

## 1. Universal flow and observable-specific head

Along

\[
 \dot\theta=p(\theta)=n\nabla f(\theta),\qquad
 D=p\mathbin\cdot\nabla,
\]

the parameter-flow jets are

\[
 \theta'=p,\qquad \theta''=Dp,\qquad
 \theta'''=D^2p,\qquad \theta^{(4)}=D^3p.
\]

For any scalar observable `O(theta)`, ordinary differentiation gives the
exact universal readout law

\[
\begin{aligned}
 O'={}&O_1[p],\\
 O''={}&O_2[p,p]+O_1[Dp],\\
 O'''={}&O_3[p,p,p]+3O_2[p,Dp]+O_1[D^2p],\\
 O^{(4)}={}&O_4[p,p,p,p]+6O_3[p,p,Dp]+3O_2[Dp,Dp]\\
 &\quad+4O_2[p,D^2p]+O_1[D^3p].
\end{aligned}
\tag{1.1}
\]

Thus the expensive part—constructing `p,Dp,D^2p,D^3p` and their required
feature/reverse contractions—is universal.  Changing `O` changes only the
small terminal or layerwise head that contracts (1.1).

For hidden activation norm, put

\[
 Q_\ell(s)=n^{-1}\|X_\ell(s)\|^2,
 \qquad
 \Gamma^\ell_{rs}
 =\lim_n\mathbb E\,n^{-1}\langle X_{\ell}^{(r)},X_{\ell}^{(s)}\rangle.
\]

Leibniz differentiation is exact at finite width:

\[
 \boxed{Q_\ell^{(k)}(0)=
 \sum_{r=0}^{k}{k\choose r}\Gamma^\ell_{r,k-r}.}
\tag{1.2}
\]

The independently checked backbone dictionary is

\[
 \boxed{
 \Gamma_{11}^\ell=w_\ell,\qquad
 \Gamma_{02}^\ell=q02_\ell,\qquad
 \Gamma_{22}^\ell=q22_\ell,\qquad
 \Gamma_{13}^\ell=q13_\ell.}
\tag{1.3}
\]

Consequently

\[
 \boxed{Q_\ell''(0)=2(w_\ell+q02_\ell)},
\tag{1.4}
\]

and the new head supplies

\[
 \boxed{Q_\ell^{(4)}(0)
 =2\gamma^\ell_{04}+8q13_\ell+6q22_\ell.}
\tag{1.5}
\]

## 2. Exact local fourth-jet derivation

At finite width, the matrix and activation product rules give

\[
 Z_4=F_4+(5\widehat\Gamma_{03}+10\widehat\Gamma_{12})\Delta_0
 +(9\widehat\Gamma_{02}+8\widehat\Gamma_{11})\Delta_1
 +7\widehat\Gamma_{01}\Delta_2
 +\widehat\Gamma_{00}\Delta_3,
\tag{2.1}
\]

\[
 X_4=\phi^{(4)}Z_1^4+6\phi^{(3)}Z_1^2Z_2
 +3\phi''Z_2^2+4\phi''Z_1Z_3+\phi'Z_4.
\tag{2.2}
\]

Equation (2.1) contains all five weight-jet branches; (2.2) contains all five
integer partitions of four with multiplicities `1,6,3,4,1`.  The complete
finite-width and free-index derivation is in
`FINITE_WIDTH_AND_WIDTH_AUDIT.md`.

Readout reflection sends

\[
 X_\ell^{(r)}\longmapsto(-1)^rX_\ell^{(r)}.
\tag{2.3}
\]

It therefore removes the deterministic odd-total Grams and the even-indexed
transpose responses, leaving

\[
 Z_4=G_4+l41\,d_1+l43\,d_3,
\qquad
 l41=9q02+8w+a41,
\qquad l43=1+a43.
\tag{2.4}
\]

The three-state producer initially closes

\[
 \gamma04^+=\mathbb E[X_0X_4],\quad
 a41^+=\mathbb E[\partial_{E_1}X_4],\quad
 a43^+=\mathbb E[\partial_{J_3}X_4].
\tag{2.5}
\]

Complete Wick--Stein elimination gives 83, 20, and 1 local scalar monomials.
The last transition is exactly

\[
 a43_\ell=d(1+a43_{\ell-1}),\qquad a43_0=0.
\]

Since the backbone uses

\[
 \tau_r=1+d+\cdots+d^r,
\]

induction yields

\[
 1+a43_{\ell-1}=\tau_{\ell-1}=l1.
\tag{2.6}
\]

Thus `a43` is not dynamic state.  Substituting `l43=l1` into the two remaining
literal transitions gives the public two-state recurrence.  Its exact
initialization is

\[
 \gamma04_0=a41_0=0,
\tag{2.7}
\]

and at layer `ell`, after setting

\[
 l1=\tau_{\ell-1},\qquad
 l41=9q02_{\ell-1}+8w_{\ell-1}+a41_{\ell-1},
\tag{2.8}
\]

one applies the two fully displayed polynomials in
`FROZEN_GAMMA04_REDUCED_TRANSITIONS.md`.  No Gaussian, covariance matrix,
response derivative, or unnamed contraction remains in those polynomials.

One target layer costs `ell` constant-size head transitions after the
backbone.  Retaining the output at every layer costs one pass of `H`
transitions, not `H` separate passes.  Hence the incremental factored-DAG
work is `O(ell)` for one target and `O(H)` for all hidden layers.

## 3. RMS formulas

Under unit Gram, `Q_l(0)=1`.  Reflection gives
`Q_l'(0)=Q_l'''(0)=0`, so direct differentiation of
`R_l=sqrt(Q_l)` yields

\[
 \boxed{R_\ell''(0)=w_\ell+q02_\ell},
\tag{3.1}
\]

\[
 \boxed{
 R_\ell^{(4)}(0)=\gamma^\ell_{04}+4q13_\ell+3q22_\ell
 -3(w_\ell+q02_\ell)^2.}
\tag{3.2}
\]

Odd annealed feature-ascent derivatives of `Q_l` and `R_l` vanish by (2.3).
This parity is exact under the reflected finite-width initialization law; it
does not say an individual unpaired network has zero odd derivative.

## 4. Algebraic and finite-width audits

The Route-S recurrence was expanded with exact rational arithmetic and
compared with a separately reconstructed response-aware population jet using
two distinct distributive canonicalizers.  All dictionary nodes in (1.3) and
the new `Gamma04` node matched at every layer:

| depth | observed layers | largest `Gamma04` map | total discrepancies |
|---:|---:|---:|---:|
| 2 | 2 | 549 | 0 |
| 3 | 3 | 3,165 | 0 |
| 4 | 4 | 8,005 | 0 |

The exact three-state and reduced two-state schedules also agree at every
layer for `H=1,2,3,4`.

The local equality-partition census covers all set partitions of up to five
neuron labels.  Relative free-index exponents are `n^(|pi|-m)`; the complete
class counts for `m=1,...,5` are recorded in the width audit.  Same-matrix
transpose contractions are peeled before this accidental-collision count and
appear explicitly in the four response branches `s=0,1,2,3`.

Two finite-width differentiators—coefficient convolution and ordinary
binomial/Bell differentiation—agreed over 30 layer-cases at widths `1,2,5`,
with maximum scaled error `1.38e-15`.  Readout parity agreed seedwise to exact
floating-point zero in the audit.

The independent producer comparison is

| transition | Route S | Route A | discrepancies |
|---|---:|---:|---:|
| `gamma04_next` | 83 | 83 | 0 |
| `a41_next` | 20 | 20 | 0 |
| `a43_next` | 1 | 1 | 0 |

The hostile 82-term candidate is falsified, not merely differently factored.
It reused four existing forward slots and renamed them as
`(f1,g2,g3,g4)`, forgetting that the slots already mean
`(F1,F2_frozen,F2_moving,F3_moving)`.  It consequently placed `Gamma04` in
slot `(0,4)` instead of appending `(0,5)`.  Exact comparison finds 31 wrong
`Gamma04` monomials and four wrong `a41` monomials.

## 5. Exact controls

For `phi=1`, every hidden derivative and every displayed head output is zero
at all tested depths and layers.

For `phi(x)=x`, the exact `Q''/Q^(4)` controls are

| `H` | layerwise `(Q'',Q^(4))` |
|---:|---|
| 1 | `(4,16)` |
| 2 | `(6,96)`, `(18,528)` |
| 3 | `(8,320)`, `(24,1408)`, `(48,4064)` |
| 4 | `(10,800)`, `(30,3120)`, `(60,8320)`, `(100,18080)` |

For the normalized affine control `phi(x)=(3+4x)/5`, selected exact values
are

| `H`, layer | `Q''` | `Q^(4)` |
|---|---:|---:|
| 1,1 | `1312/625` | `83968/15625` |
| 2,1 | `33792/15625` | `172045824/9765625` |
| 2,2 | `2221344/390625` | `3705931776/48828125` |
| 3,3 | `2311684896/244140625` | `986607534958592/3814697265625` |
| 4,4 | `1942453166368/152587890625` | `6329777151199971328/11920928955078125` |

Every intermediate `Gamma` value for every layer of `H=1,2,3,4` is stored
exactly in `POST_FREEZE_EXACT_AUDIT.json`.

## 6. Smooth nonpolynomial regression

For

\[
 \phi(x)=\frac{\sin x}{\sqrt{(1-e^{-2})/2}},
\]

the frozen prediction at `H=2`, layer 2 is

\[
 \gamma_{04}=1521.914807371915.
\]

The preregistered 2,550-network panel at widths `16,32,64,128` passed.  The
affine-in-`1/n` intercept was `1403.3464 +/- 64.0677`, giving
`z=-1.851`; the chi-square p-value was `0.211`.  This is empirical support,
not a proof of the population contraction or annealed limit.

## 7. Regularity and claim boundary

The exact finite-width head identities require `phi in C^4` and the moments
appearing in the finite expectations.  When attached to the existing
order-five output backbone, the common calculation requires derivatives
through `phi^(5)`.

A convenient sufficient theorem-level condition at every separately fixed
`H` is that `phi` is smooth with every derivative of polynomial growth and
that the associated finite tensor program converges in every finite `L^p`.
For a weaker probability-limit route, one must separately prove convergence
in probability and, for some `epsilon>0`, uniform integrability such as

\[
 \sup_n\mathbb E\left|n^{-1}
 \langle X_\ell^{(r)},X_\ell^{(s)}\rangle\right|^{1+\epsilon}<\infty
\tag{7.1}
\]

for `(r,s)=(1,1),(0,2),(2,2),(1,3),(0,4)` and the finite collection of
internal transition monomials.  The algebra and regression do not prove
(7.1).

Claim levels are therefore:

1. (1.1)--(1.2), (2.1)--(2.2), and the finite-width norm differentiation are
   exact finite-width identities.
2. The literal two-state transition is a formal Wick--Stein normal form.
3. The exact producer/reference comparisons make it an algebraically audited
   fixed-depth normal form.
4. The sine panel is empirical support only.
5. Equality with the annealed width limit is theorem-level only under the
   stated regularity and uniform-integrability bridge.

No claim covers growing depth, positive time, multi-sample training, an
all-orders observable calculus, or a complexity bound for fully distributed
monomial expansions.  The `O(H)` statement concerns the factored local DAG.

## 8. Reproduction

From the repository root run

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5_observables.independent.run_checks
```

The required outcome is zero `H=2,3,4` population discrepancies, zero
two-state projection discrepancies through `H=4`, exact Route-A agreement,
a rejected 82-term hostile map, and a passing sine regression.
