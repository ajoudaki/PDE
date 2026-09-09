# Exact finite-width directional program for L=2, B=2

**Status:** exact finite-width identity and executable compiler; no width-limit
Gaussian normal form is claimed here.  
**Activation:** generic through derivatives zero to three; no Hermite or
polynomial approximation.  
**Observable:** `g_c = c^T f` for an arbitrary deterministic
`c=(c1,c2)`.

## 1. Frozen model and notation

Let `Q0` be an arbitrary positive-semidefinite 2-by-2 input Gram.  Store batch
coordinates in columns. At initialization,

\[
U_{j,:}\sim N(0,Q^0),\qquad A=W/\sqrt n,
\qquad X_r=\phi^{(r)}(U),
\]

\[
Z=AX_0,\qquad Y_r=\phi^{(r)}(Z),\qquad
f_s=\frac1n\sum_i a_iY_{0,is}.
\]

For two `n`-by-2 channel matrices define

\[
M(P,R)=\frac1nP^TR.
\]

All products below are coordinatewise unless matrix multiplication is shown.
Put `C=diag(c1,c2)` only in this note and define the top backward source

\[
P=(a\mathbf 1_2^T)Y_1C,\qquad R=A^TP.
\tag{1.1}
\]

The first-layer metric acts across batch coordinates:

\[
\dot U=(X_1R)Q^0,\qquad \dot X_0=X_1\dot U.
\tag{1.2}
\]

These are exact identities obtained by scalarizing the raw first weight
matrix. No inverse of `Q0` is used, so singular input Grams are admitted.

## 2. Frozen straight-line tangents

Let

\[
Q_n=M(X_0,X_0),\qquad
\zeta=PQ_n+A\dot X_0.
\tag{2.1}
\]

Along the frozen parameter line, the first preactivation is linear. Hence

\[
\ddot X_0=X_2\dot U^2,\qquad
X_0^{(3)}=X_3\dot U^3.
\tag{2.2}
\]

Because the middle matrix is also linear along that line,

\[
\sigma=2P M(X_0,\dot X_0)+A\ddot X_0,
\tag{2.3}
\]

\[
\tau=3P M(X_0,\ddot X_0)+AX_0^{(3)}.
\tag{2.4}
\]

Thus `(zeta,sigma,tau)` are exactly the first three derivatives of the two
top-preactivation columns.

## 3. Differentiated gradient blocks

The readout feature velocity and differentiated top source are

\[
v_a=Y_0c,
\]

\[
\dot P=\left[(v_a\mathbf1_2^T)Y_1
 +(a\mathbf1_2^T)Y_2\zeta\right]C.
\tag{3.1}
\]

Since the middle velocity is `(1/sqrt(n)) P X0^T`, differentiating its
transpose channel gives

\[
\dot R=X_0M(P,P)+A^T\dot P.
\tag{3.2}
\]

Finally set

\[
\dot S=X_2\dot U R+X_1\dot R,
\tag{3.3}
\]

where `S=X1 R` is the coefficient representation of the raw first-weight
gradient.

## 4. Exact scalar output

The straight-line third derivative is

\[
\begin{aligned}
T_{n,c}=\frac1n\sum_i\{&a_i
\sum_s c_s(Y_{3,is}\zeta_{is}^3
+3Y_{2,is}\zeta_{is}\sigma_{is}+Y_{1,is}\tau_{is})\\
&+3(v_a)_i\sum_sc_s
(Y_{2,is}\zeta_{is}^2+Y_{1,is}\sigma_{is})\}.
\end{aligned}
\tag{4.1}
\]

The three Hessian-square blocks are

\[
H_{a,n}=\frac1n\left\|(Y_1\zeta)c\right\|^2,
\tag{4.2}
\]

\[
\begin{aligned}
H_{W,n}={}&\operatorname{tr}\{M(\dot P,\dot P)M(X_0,X_0)\}\\
&+\operatorname{tr}\{M(P,P)M(\dot X_0,\dot X_0)\}\\
&+2\operatorname{tr}\{M(\dot P,P)M(\dot X_0,X_0)\},
\end{aligned}
\tag{4.3}
\]

\[
H_{U,n}=\operatorname{tr}\{M(\dot S,\dot S)Q^0\}.
\tag{4.4}
\]

Therefore the vectorized analogue of the one-sample contraction is

\[
\boxed{
C_{n,c}=D_c^3g_c
=2T_{n,c}+4(H_{a,n}+H_{W,n}+H_{U,n}).
}
\tag{4.5}
\]

Equations (1.1)--(4.5) use a fixed number of `MatMul`, transpose-`MatMul`,
coordinate-map, and 2-by-2 `Moment` operations independent of width. They are
therefore a fixed finite Tensor Program. This statement is exact at finite
width; it does not identify the program's width limit.

## 5. Directional channels and checks

The named specializations are

\[
c_+=(1,1),\qquad c_-=(1,-1).
\]

They are unnormalized: replacing `c` by `lambda*c` multiplies `g_c` and
`D_c` by `lambda`, hence

\[
C_{n,\lambda c}=\lambda^4C_{n,c}.
\]

`finite_width_directional.py` evaluates (1.1)--(4.5) directly.
`finite_width_jet.py` independently propagates the full finite-width feature
ODE through order three. Seedwise equality is tested for:

- linear, affine, quadratic, cubic, sine, and tanh activations;
- nonsingular correlated, diagonal, and singular input Grams;
- `c_+`, `c_-`, and a generic asymmetric channel;
- widths 1, 3, and 6.
- exact reduction to the audited B=1 program when `c=(1,0)`, including a
  correlated inactive sample and hence a nondiagonal `Q0`.

Run from the repository root:

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.b2.run_checks
```

Passing this check establishes the exact finite-width directional encoding.
The completed layerwise Gaussian/response peel is stated separately in
`B2_GAUSSIAN_NORMAL_FORM.md` and audited in `B2_FINITE_WIDTH_AUDIT.md`; it is
intentionally not claimed by the finite-width identity alone.
The same executable also contains the two additional frozen MSE response
scalars and the exact residual-dependent loss third derivative derived in
Section 9 of the audit.
