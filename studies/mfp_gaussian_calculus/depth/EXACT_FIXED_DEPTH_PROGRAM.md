# Exact finite-width order-three program at arbitrary fixed depth and batch

## 1. Status and scope

This note records an **exact finite-width compiler**, not a large-width
Gaussian-normal-form theorem.  For any finite width `n`, hidden-layer count
`H >= 1`, batch size `B >= 1`, positive-semidefinite input Gram, channel `c`,
and activation derivatives through order three, the compiler returns

\[
  \bigl(g_c,\;D_cg_c,\;D_c^2g_c,\;D_c^3g_c\bigr)
\]

at the supplied parameters.  Here

\[
  D_c=n\nabla_\theta g_c\mathbin{\cdot}\nabla_\theta
\]

is a variable-coefficient differential operator.  The implementation follows
the full nonlinear feature-ascent ODE

\[
  \dot\theta(t)=n\nabla_\theta g_c(\theta(t)),\qquad \theta(0)=\theta_0,
  \tag{1.1}
\]

so it is **not** the frozen-direction curve
`theta_0 + t n grad(g_c)(theta_0)`.

The executable entry point is
[`finite_width_jet.py`](./finite_width_jet.py).  The state helpers are in
[`model.py`](./model.py), and an independent raw-coordinate audit is in
[`raw_coordinate_jet_audit.py`](./raw_coordinate_jet_audit.py).

## 2. Exact model and normalization

Let `X` have `B` columns and define

\[
 Q^0=\frac{X^\top X}{d_0}\succeq0.
\]

No inverse of `Q^0` is used.  Consequently singular and repeated inputs are
allowed.  With raw parameter matrices and a raw readout,

\[
\begin{aligned}
 z^1 &= \frac{W^1X}{\sqrt{d_0}},
 &h^1&=\phi_1(z^1),\\
 z^\ell&=\frac{W^\ell h^{\ell-1}}{\sqrt n},
 &h^\ell&=\phi_\ell(z^\ell),\qquad 2\leq \ell\leq H,\\
 f_\beta&=\frac1n\sum_{i=1}^n a_i h^H_{i\beta},
 &g_c&=\sum_{\beta=1}^B c_\beta f_\beta.
\end{aligned}
\tag{2.1}
\]

The project model has one shared activation `phi`.  The implementation also
accepts a tuple `(phi_1,...,phi_H)` because that makes layer indexing and the
audit sharper; passing one oracle repeats it at all layers.

All raw parameter blocks use metric factor `n`, exactly as in (1.1).  The
first raw matrix can be eliminated without approximation: its induced
preactivation motion depends on the inputs only through `Q^0`.

## 3. Closed finite-width forward/reverse ODE

Define top and lower reverse sources

\[
\begin{aligned}
 \delta^H
   &=a[:,\mathrm{None}]\odot\phi_H'(z^H)
       \odot c[\mathrm{None},:],\\
 r^\ell
   &=\frac{(W^{\ell+1})^\top\delta^{\ell+1}}{\sqrt n},\\
 \delta^\ell&=\phi_\ell'(z^\ell)\odot r^\ell,
       \qquad 1\leq\ell<H.
\end{aligned}
\tag{3.1}
\]

A direct raw-coordinate differentiation of (2.1) gives the complete ODE

\[
\begin{aligned}
 \dot a &= h^Hc,\\
 \dot W^\ell
   &=\frac{\delta^\ell(h^{\ell-1})^\top}{\sqrt n},
       &&2\leq\ell\leq H,\\
 \dot z^1&=\delta^1Q^0.
\end{aligned}
\tag{3.2}
\]

Equations (2.1), (3.1), and (3.2) are already an exact finite DAG for any
fixed `H` and `B`.  They contain both the forward occurrence of every
`W^ell` and its reverse transpose occurrence.  That reuse is harmless in the
finite-width calculation but becomes a central response/Onsager obligation
in any later Gaussian peeling proof.

## 4. Ordinary-series recursion

For any time-dependent array `x`, write

\[
 x(t)=\sum_{k=0}^3 x_{[k]}t^k+O(t^4).
\]

Products use the ordinary Cauchy convolution

\[
 (xy)_{[k]}=\sum_{r=0}^k x_{[r]}y_{[k-r]}.
\tag{4.1}
\]

For scalar entrywise composition define
`C_k[psi;z]=[t^k]psi(z(t))`.  Through degree three,

\[
\begin{aligned}
 C_0[\psi;z]&=\psi(z_{[0]}),\\
 C_1[\psi;z]&=\psi'(z_{[0]})z_{[1]},\\
 C_2[\psi;z]&=\psi'(z_{[0]})z_{[2]}
  +\frac12\psi''(z_{[0]})z_{[1]}^2,\\
 C_3[\psi;z]&=\psi'(z_{[0]})z_{[3]}
  +\psi''(z_{[0]})z_{[1]}z_{[2]}
  +\frac16\psi'''(z_{[0]})z_{[1]}^3.
\end{aligned}
\tag{4.2}
\]

At each degree `k=0,1,2,3`, the compiler performs the following forward pass:

\[
\begin{aligned}
 h^\ell_{[k]}&=C_k[\phi_\ell;z^\ell],\\
 z^\ell_{[k]}&=\frac1{\sqrt n}\sum_{r=0}^k
    W^\ell_{[r]}h^{\ell-1}_{[k-r]},\qquad \ell\geq2,\\
 g_{c,[k]}&=\frac1n\sum_{r=0}^k
    a_{[r]}^\top h^H_{[k-r]}c.
\end{aligned}
\tag{4.3}
\]

For `k<3`, set

\[
 p^\ell_{[k]}=C_k[\phi_\ell';z^\ell]
\]

and perform the reverse pass

\[
\begin{aligned}
 \delta^H_{[k]}
   &=\left(\sum_{r=0}^k a_{[r]}[:,\mathrm{None}]
       \odot p^H_{[k-r]}\right)\odot c[\mathrm{None},:],\\
 r^\ell_{[k]}
   &=\frac1{\sqrt n}\sum_{r=0}^k
       (W^{\ell+1}_{[r]})^\top\delta^{\ell+1}_{[k-r]},\\
 \delta^\ell_{[k]}
   &=\sum_{r=0}^k p^\ell_{[r]}\odot r^\ell_{[k-r]}.
\end{aligned}
\tag{4.4}
\]

Finally integrate the vector field coefficient:

\[
\begin{aligned}
 a_{[k+1]}&=\frac{h^H_{[k]}c}{k+1},\\
 W^\ell_{[k+1]}&=\frac1{(k+1)\sqrt n}
   \sum_{r=0}^k\delta^\ell_{[r]}
       (h^{\ell-1}_{[k-r]})^\top,\\
 z^1_{[k+1]}&=\frac{\delta^1_{[k]}Q^0}{k+1}.
\end{aligned}
\tag{4.5}
\]

The division by `k+1` is essential: these are ordinary coefficients, not
derivatives.  Once (4.3)--(4.5) finish,

\[
  D_c^k g_c=\left.\frac{d^k}{dt^k}g_c(\theta(t))\right|_{t=0}
           =k!\,g_{c,[k]},\qquad 0\leq k\leq3.
\tag{4.6}
\]

Equation (4.6) follows by applying the chain rule to (1.1); the coefficient
recursion is simply formal Picard iteration of that ODE.  No width limit or
probabilistic replacement occurs.

Only `phi,phi',phi'',phi'''` are evaluated.  Although (4.2) applied to
`phi'` might appear to ask for `phi''''`, the reverse pass stops at degree two
when an order-three output is requested.

## 5. Executable interface

```python
from studies.mean_field_peeling.generic_first_stieltjes.depth import (
    feature_ascent_jet,
    sample_state,
)

state = sample_state(width=n, input_gram=Q0, hidden_layers=H, seed=seed)
jet = feature_ascent_jet(state, Q0, c, activation_derivative)
C_c_n = jet.derivatives[3]
```

`activation_derivative(r, x)` must return `phi^(r)(x)` entrywise for
`r=0,1,2,3`.  A sequence of `H` such callables selects layerwise activations.

The arithmetic cost at fixed Taylor order is

\[
 O(Hn^2B)
\]

with a small order-three convolution constant.  The stored parameter series
costs `O(H n^2)`, and the forward/reverse feature series costs `O(H n B)`.

## 6. Audit gates passed

Run

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.depth.run_checks
```

The current gate checks:

1. **Accepted `H=2` specialization.**  All ordinary coefficients agree
   seedwise with `b2/finite_width_jet.py` in 54 combinations: six activations,
   three batch Grams (including singular and `B=3` cases), and three widths.
   The `H=2` sampler also reproduces the old draw order exactly.
2. **Independent raw-coordinate tensors.**  For `H=1,2,3` at width one, a
   multivariate third-order jet differentiates the original raw network in
   every parameter and verifies
   \[
     g'=n\|p\|^2,\quad
     g''=2n^2p^\top Hp,\quad
     g'''=n^3\{4\|Hp\|^2+2T[p,p,p]\}.
   \]
   It agrees with all four compiler outputs.  The audit also verifies that a
   tested full-flow third derivative differs from the literal frozen-line
   contraction `n^3 T[p,p,p]`.
3. **Arbitrary fixed `H` and `B`.**  An `H=5`, `B=4`, rank-two Gram case with
   distinct layer activations runs without a special branch and obeys the
   exact channel homogeneity
   \[
     D_{\lambda c}^k g_{\lambda c}
       =\lambda^{k+1}D_c^k g_c.
   \]
4. **The base depth.**  `H=1`, `B=3` is exercised directly.

These are exact deterministic equality tests, not Monte Carlo evidence.

## 7. What this does and does not settle

**Subsequent analytic update.**  The companion
‘DEPTH_B1_GAUSSIAN_RECURSION.md’ now discharges the response-aware
large-width Gaussian normal form for arbitrary fixed \(H\) at \(B=1\) under
the polynomially-smooth activation envelope.  The qualifications below
describe what the finite-width compiler alone proves and remain applicable
to the combined \(H>2,\ B>1\) extension.

The map

\[
 c\longmapsto D_c^3g_c
\]

is a homogeneous quartic polynomial.  Therefore its associated symmetric
four-channel tensor can, in principle, be recovered by polarization, and a
fixed initial loss-residual channel can be inserted directly.  The compiler thus supplies
the exact finite-width object whose expectation/limit is needed for the first
feature correction.

It does **not** yet provide any of the following:

- a Gaussian normal form for `E[D_c^3 g_c]` at arbitrary depth;
- a proof that the finite-width random DAG converges to a proposed Gaussian
  recursion;
- response coefficients for reused `W^ell/(W^ell)^T` pairs;
- an annealed/uniform-integrability bridge;
- a sign or Stieltjes-moment claim for the resulting limit.

In particular, replacing every reverse product
`(W^ell).T @ delta^ell` by an independent fresh Gaussian would generally be
wrong: the same matrix already created the forward preactivation and evolves
through (4.5).  The next analytic depth extension must expose and audit those
response branches before claiming Gaussian closure.
