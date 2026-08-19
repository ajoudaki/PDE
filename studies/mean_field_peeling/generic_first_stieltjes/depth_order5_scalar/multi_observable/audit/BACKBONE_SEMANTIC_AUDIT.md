# Hostile semantic reconstruction of the audited order-five backbone

This note reconstructs the meanings from the frozen local Bell polynomials and
contraction code, rather than from a proposed multi-observable guide.

## 1. What a sweep and a layer transition mean

Each of `F1,R1,F2,R2,F3,R3` visits all `H` hidden layers exactly once.  A
forward sweep has the directed edges

\[
 0\longrightarrow1\longrightarrow\cdots\longrightarrow H,
\]

and a reverse sweep has the opposite edges.  The printed closed-form
initialization at layer 1 is the layer-0-to-layer-1 transition with the fixed
input/boundary values already substituted; it is not a missing transition.
Likewise a top initialization is the output-to-layer-`H` boundary transition.
Thus each sweep costs exactly `H` nearest-neighbour local maps.

Within one sweep, the same polynomial template is reused at every internal
layer, after substituting the local `b_ell`, `tau_(ell-1)`, moments, and cached
states.  This does **not** mean all sweeps use the same map.  The six maps carry
different jet grades and have dimensions `7,8,4,4,3,3`, respectively.

At `d=1`,

\[
 b_\ell=d^{H-\ell}=1,\qquad \tau_\ell=1+d+\cdots+d^\ell=\ell+1.
\]

The layer-`ell` map therefore uses `tau_(ell-1)=ell`; the numerical map remains
layer-dependent through this value and through the stored states.

## 2. Local jet language

Two types of jet occur.

- A **frozen-line jet** differentiates the network on the straight parameter
  line `theta+s p(theta)` while keeping the initial direction fixed.  Write its
  hidden activation and reverse/backpropagation jets as `X_r^f` and
  `Delta_r^f`.
- A **moving-flow jet** differentiates along the actual feature-ascent ODE.  Its
  second and third activation/reverse jets are denoted `X_2^m,Delta_2^m` and
  `X_3^m,Delta_3^m`.

All covariance descriptions below mean the normalized large-width annealed
inner product at the indicated layer.  The `c`, `a`, and `d` coordinates are
Stein response coefficients: derivatives of a local jet with respect to the
fresh forward or reverse Gaussian consumed by a transpose multiplication.
They are already deterministic scalars in the displayed recurrence; this
semantic explanation does not reintroduce a response operation into that
recurrence.

## 3. Meanings of all 29 propagated coordinates

### F1: frozen forward jet

The first five coordinates are covariances

\[
\begin{array}{c|c}
u=G_{02}&\langle X_0^f,X_2^f\rangle/n\\
v=G_{04}&\langle X_0^f,X_4^f\rangle/n\\
w=G_{11}&\langle X_1^f,X_1^f\rangle/n\\
x=G_{13}&\langle X_1^f,X_3^f\rangle/n\\
y=G_{22}&\langle X_2^f,X_2^f\rangle/n.
\end{array}
\]

The remaining coordinates `j=a3` and `k=a5` are the layerwise Stein response
of `X_3^f` and `X_5^f` to the fresh reverse Gaussian that enters the frozen
first preactivation jet.  Their combinations

\[
 S_{3,\ell}=j_\ell+3u_\ell,\qquad
 S_{5,\ell}=k_\ell+5v_\ell
\]

are the fully assembled straight third and fifth output contractions at the
top.  In particular, `v=G04` is a frozen-straight-line covariance and is **not**
the moving-flow observable `Gamma_04`.

### R1: frozen reverse jet

The four `e` coordinates are

\[
 e02=\langle\Delta_0^f,\Delta_2^f\rangle/n,
 \quad e11=\|\Delta_1^f\|^2/n,
 \quad e13=\langle\Delta_1^f,\Delta_3^f\rangle/n,
 \quad e22=\|\Delta_2^f\|^2/n.
\]

The four `c` coordinates are the transpose-response channels retained by
liveness pruning:

\[
 c10:\Delta_1^f\leftrightarrow F_0,\quad
 c21:\Delta_2^f\leftrightarrow F_1,\quad
 c30:\Delta_3^f\leftrightarrow F_0,\quad
 c32:\Delta_3^f\leftrightarrow F_2.
\]

Here the first digit is the reverse-jet grade and the second is the forward
innovation grade.  The local definitions include the direct covariance terms
required by Gaussian integration by parts (for example `c10` contains the
base reverse variance, and `c30` contains three copies of the `02` covariance);
they are not bare formal partial derivatives.

### F2: moving feature jet of order two

\[
\begin{array}{c|c}
q02&\langle X_0^f,X_2^m\rangle/n=\Gamma_{02}\\
q22&\|X_2^m\|^2/n=\Gamma_{22}\\
qfm&\langle X_2^f,X_2^m\rangle/n\\
a2&\text{reverse-innovation response of }X_2^m.
\end{array}
\]

The actual coefficient injected into the next layer is `l2=1+a2`; the `1` is
the direct parameter-flow contribution.

### R2: moving reverse jet of order two

\[
\begin{array}{c|c}
r02&\langle\Delta_0^f,\Delta_2^m\rangle/n\\
r22&\|\Delta_2^m\|^2/n\\
rfm&\langle\Delta_2^f,\Delta_2^m\rangle/n\\
d21&\text{forward-innovation response of }\Delta_2^m
       \text{ in channel }F_1.
\end{array}
\]

Again `d21` includes the direct base-reverse covariance term prescribed by
the transpose-response rule.

### F3: moving feature jet of order three

\[
\begin{array}{c|c}
q13&\langle X_1^f,X_3^m\rangle/n=\Gamma_{13}\\
a30&\text{response of }X_3^m\text{ to the frozen reverse innovation }E_0\\
a32&\text{response of }X_3^m\text{ to the moving reverse-grade-2 innovation }J_2.
\end{array}
\]

The combinations passed to the local Bell polynomial are

\[
 l30=4q02+3w+a30,\qquad l32=1+a32.
\]

### R3: moving reverse jet of order three

\[
\begin{array}{c|c}
r13&\langle\Delta_1^f,\Delta_3^m\rangle/n\\
d30&\text{coefficient of }X_0\text{ in }\Delta_3^m=J_3+d30X_0+d32X_2\\
d32&\text{coefficient of the moving feature-grade-2 }X_2\text{ above}.
\end{array}
\]

As before, `d30,d32` include their required direct covariance pieces.

## 4. Autonomous order-three projection

Inspection of the explicit maps confirms that

\[
 (w,u,j;e11,c10)
\]

is closed under F1/R1 and does not reference any of the other 24 coordinates.
It is precisely the accepted order-three state `(V,M,J;E,C)`.  Its terminal
readout is

\[
 S_{3,H}=j_H+3u_H,\qquad
 B_H=2S_{3,H}+4\mathcal H,
\]

where `mathcal H` starts at `w_H` and folds the `s11+s00*w` layer sources.

## 5. Reading A, B, and C

The order-one coefficient is the deterministic path-sum backbone node

\[
 A_H=\tau_H.
\]

The order-three coefficient uses the F1 endpoint and the R1 fold just given.
The fifth coefficient reads

\[
 C_H=2S_{5,H}+10AC+10Bm2+4M2+12Am3,
\]

where

\[
\begin{array}{c|c}
AC&\langle Hp,U[p,p,p]\rangle\\
Bm2&\langle T[p,p],D^2p\rangle\\
M2&\|D^2p\|^2\\
Am3&\langle Hp,D^3p\rangle.
\end{array}
\]

These are deterministic terminal folds over already contracted layer sources.
No extra Gaussian evaluation occurs at readout.

## 6. Audit cautions for observable heads

The universal part is the parameter-flow backbone and its cached local source
contractions.  An observable head is universal only after its required
contractions have been shown to be functions of those nodes plus a fixed
number of new deterministic states.  In particular:

- identifying `q02,q22,q13` with moving-flow hidden-feature covariances is
  supported by their frozen local definitions;
- identifying `v` with `Gamma_04` is false because `v` uses the frozen line;
- a hidden-activation `Gamma_04` head is a new contraction obligation;
- a preactivation-RMS head cannot be inferred from an activation-RMS head:
  it has a different observable derivative tensor and must be derived and
  audited separately.
