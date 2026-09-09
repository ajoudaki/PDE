# Primary order-five Gaussian normal form for H=2, B=1

**Status:** algebraically audited normal form; theorem-level annealed limit
under the hypotheses in Section 8.

**Scope.**  This document gives the primary derivation and the literal
moment-only artifacts for

\[
A=F'(0),\qquad B=F^{(3)}(0),\qquad C=F^{(5)}(0).
\]

It uses the exact model and limit order in [`PROOF_CONTRACT.md`](PROOF_CONTRACT.md).
No Hermite or polynomial approximation of the activation occurs anywhere in
the derivation.  Polynomial activations are used only after the formula is
frozen, as exact controls.

Explicitly, for one fixed input \(x\),

\[
u_j={w_j^\top x\over\sqrt{d_0}},\qquad
z_i={1\over\sqrt n}\sum_{j=1}^nW_{ij}\phi(u_j),\qquad
f_n={1\over n}\sum_{i=1}^na_i\phi(z_i),
\tag{0.1}
\]

where all entries of \(w,W,a\) are mutually independent standard Gaussians
at initialization.  With the Euclidean gradient over every trainable
parameter,

\[
D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad
F^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^kf_n].
\tag{0.2}
\]

The first forward Gram is
\(Q^0=\lVert x\rVert^2/d_0\); the two hidden-layer widths are both \(n\),
and every finite-width differentiation is performed before the limit in
(0.2).

The exact finite-width fifth-derivative tensor identity is audited in the
companion finite-width note.  The present note starts from an exact
finite-width feature-flow jet, performs the alternating matrix peel, and
eliminates every auxiliary Gaussian.  Its terminal artifacts contain only
rational arithmetic and explicitly named one-dimensional Gaussian moments.

## 1. Two terminal moment alphabets

For arbitrary forward variances put

\[
X_\nu=
\mathbb E_{U\sim N(0,Q^0)}
 \prod_{r=0}^5\phi^{(r)}(U)^{\nu_r},
\qquad Q^1=X_{200000},
\tag{1.1}
\]

and

\[
Y_\nu=
\mathbb E_{Z\sim N(0,Q^1)}
 \prod_{r=0}^5\phi^{(r)}(Z)^{\nu_r},
\qquad Q^2=Y_{200000}.
\tag{1.2}
\]

The literal arbitrary-variance formula is
[`compiler/LAYER_SEPARATED_ABC_NORMAL_FORM.txt`](compiler/LAYER_SEPARATED_ABC_NORMAL_FORM.txt).
It contains the forward Gram `Q0` and only the atoms (1.1)--(1.2).

For the clean unit-Gram specialization,

\[
Q^0=Q^1=Q^2=1,
\qquad
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}
 \prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},
\tag{1.3}
\]

we take the exact quotient

\[
Q^0\mapsto1,\qquad X_\nu,Y_\nu\mapsto M_\nu,
\qquad M_{200000}\mapsto1.
\tag{1.4}
\]

The last substitution is part of the unit-Gram hypothesis, not an informal
simplification.  The complete terminal formula in this quotient is
[`compiler/UNIT_GRAM_ABC_NORMAL_FORM.txt`](compiler/UNIT_GRAM_ABC_NORMAL_FORM.txt).
It is a dependency-first arithmetic DAG: every `t_N` is a deterministic
sum or product of earlier deterministic nodes and literal `M` atoms.
There are no random variables, recursions to evaluate, pseudoinverses,
innovations, tangent Grams, or response derivatives in that file.

## 2. Compact formulas for A and B

The order-one answer is particularly small.  Set

\[
d=M_{020000}.
\]

Then

\[
\boxed{A=1+d+d^2.}
\tag{2.1}
\]

For a readable factorization of `B` define only the following deterministic
arithmetic abbreviations:

\[
\begin{gathered}
c=1+d,\quad
e=M_{040000},\quad m=M_{121000},\quad j=M_{030100},\\
s=M_{022000},\quad \ell=M_{220000},\quad
b=M_{101000},\quad r=M_{010100},\quad v=M_{002000},
\end{gathered}
\tag{2.2}
\]

\[
\tau=\ell+2cm+3c^2s+edv,
\qquad
k=2d+b+c(r+v),
\qquad
\kappa=3d(m+j),
\tag{2.3}
\]

\[
\begin{aligned}
H_3={}&c^2e+\tau+2ed^2+3d^2s+k^2\ell+\tau d+2dkm,\\
S_3={}&3c^2m+3edb+3dm(d+b)+3c^3j
+3cedr+3cdm(r+v)+\kappa d.
\end{aligned}
\tag{2.4}
\]

Thus

\[
\boxed{B=4H_3+2S_3.}
\tag{2.5}
\]

Expanding (2.5) gives exactly the 46-monomial `B` coefficient map in
the terminal artifact.

## 3. Literal finite formula for C

The fifth-order answer is too large for a useful single display after full
distribution: it has 974 nonzero rational monomials.  Its canonical factored
form has 1,018 deterministic compound nodes and ends with

\[
\boxed{C=120\,t_{01016},}
\tag{3.1}
\]

where every node `t_00000` through `t_01016` is explicitly defined,
dependency first, in
[the unit-Gram normal-form artifact](compiler/UNIT_GRAM_ABC_NORMAL_FORM.txt).
Equation (3.1) plus those displayed assignments is an actual finite formula,
not a request to run the response recursion.  The independently distributive
974-term representation is
[`compiler/PRIMARY_UNIT_COEFFICIENT_MAP.json`](compiler/PRIMARY_UNIT_COEFFICIENT_MAP.json).

The terminal census is

| coefficient | fully distributed monomials | maximum activation derivative |
|---|---:|---:|
| `A` | 3 | 1 |
| `B` | 46 | 3 |
| `C` | 974 | 5 |

No atom involving `phi^(6)` or above survives.  The deliberately
over-complete internal covariance registry can momentarily produce derivative
orders six and seven when Stein differentiation is applied to covariances
that the terminal scalar never uses.  Exact canonicalization cancels or
discards all of them before the terminal map is formed; the frozen terminal
ceiling is exactly five.

## 4. Exact finite-width source and chronological peel

### 4.1 The six tensor-contraction families

In whitened coordinates `vartheta=theta/sqrt(n)` put

\[
p=\nabla_\vartheta f,
\quad H=\nabla_\vartheta^2f,
\quad T=\nabla_\vartheta^3f,
\quad U=\nabla_\vartheta^4f,
\quad V=\nabla_\vartheta^5f.
\]

Since \(D_n=p\mathbin\cdot\nabla_\vartheta\), repeated product rules give the exact
finite-width identity

\[
\boxed{
\begin{aligned}
D_n^5f_n={}&2V[p,p,p,p,p]
+22U[Hp,p,p,p]
+14T[T[p,p],p,p]\\
&+30T[H^2p,p,p]
+36T[Hp,Hp,p]
+16\lVert H^2p\rVert^2.
\end{aligned}}
\tag{4.0a}
\]

Equivalently, if all tensors are now raw `theta` derivatives and
\(v=n\nabla_\theta f_n\), then

\[
\boxed{
\begin{aligned}
D_n^5f_n={}&2V[v,v,v,v,v]
+22n\,U[Hv,v,v,v]
+14n\,T[T[v,v],v,v]\\
&+30n^2T[H^2v,v,v]
+36n^2T[Hv,Hv,v]
+16n^3\lVert H^2v\rVert^2.
\end{aligned}}
\tag{4.0b}
\]

The coefficient vector `(2,22,14,30,36,16)` passed four independent
finite-width checks:

1. direct symbolic differentiation of `D_n^4f_n`;
2. exact rational polynomial equality for a generic inhomogeneous degree-five
   function of two variables;
3. seedwise equality of the moving feature-flow jet and raw multivariate
   Taylor AD at widths one and two for linear, generic cubic, `tanh`, and
   normalized-sine activations (worst scaled error `5.53e-14`); and
4. equality of raw AD's fifth operator iterate with its separately
   materialized sum of the six tensors (worst scaled error `2.59e-14`).

The detailed product-rule and raw-scaling calculation is in
[`FINITE_WIDTH_ORDER5_AUDIT.md`](FINITE_WIDTH_ORDER5_AUDIT.md).

### 4.2 Exact feature-flow jet

This section explains the derivation; none of its internal variables occurs
in the terminal files.  Write

\[
M=W/\sqrt n,\quad h=\phi(u),\quad z=Mh,\quad g=\phi(z),
\quad b=a\phi'(z),\quad r=M^Tb.
\]

The feature-ascent path whose Taylor derivatives are `D_n^kf_n` obeys the
exact finite-width ODE

\[
\dot a=g,\qquad
\dot M={1\over n}bh^T,\qquad
\dot u=Q^0\phi'(u)r.
\tag{4.1}
\]

All series below are ordinary Taylor series, `v(t)=sum_k v_k t^k`.
Consequently

\[
M_m={1\over mn}\sum_{p+q=m-1}b_p h_q^T,\qquad m\ge1.
\tag{4.2}
\]

At each order `k`, the dense initialization matrix is peeled before the
rank updates (4.2).  If `F_k` and `R_k` denote the temporary fresh
forward and transpose Gaussian coordinates, their covariances and response
coefficients are

\[
H_{k\ell}=\mathbb E[h_kh_\ell],\quad
B_{k\ell}=\mathbb E[b_kb_\ell],\quad
\alpha_{ks}=\mathbb E\,\partial_{R_s}h_k,\quad
\beta_{ks}=\mathbb E\,\partial_{F_s}b_k.
\tag{4.3}
\]

The complete chronological identities are

\[
\begin{aligned}
z_k={}&F_k+\sum_{s<k}b_s\alpha_{ks}
+\sum_{m=1}^k{1\over m}\sum_{p+q=m-1}
b_p\,\mathbb E[h_qh_{k-m}],\\
r_k={}&R_k+\sum_{s\le k}h_s\beta_{ks}
+\sum_{m=1}^k{1\over m}\sum_{p+q=m-1}
h_q\,\mathbb E[b_pb_{k-m}],\\
u_{k+1}={Q^0\over k+1}\sum_{p+q=k}[\phi'(u)]_p r_q,
\qquad a_{k+1}={g_k\over k+1}.
\end{aligned}
\tag{4.4}
\]

These identities are internal proof devices, not the delivered normal form.
They are triangular in `k` and are expanded through `k=5` by the typed
compiler.

### 4.3 Equality partitions, width counting, and transpose census

Treat the row- and column-neuron indices as distinct types.  A dense
`M0` entry has width valuation `n^(-1/2)`, a coordinate vector has
valuation one, and every explicit `M_m` entry in (4.2) has valuation
`n^(-1)`; its subsequent inner product supplies one free typed sum and
therefore exactly compensates that factor.

There are precisely six surviving sector classes at each chronological
coefficient:

| orientation | all-free sector | opposite-use equality sectors | exact rank-update sectors |
|---|---:|---:|---:|
| forward `M0 h_k` | 1 fresh Gaussian | `k` responses | `k(k+1)/2` updates |
| transpose `M0^T b_k` | 1 fresh Gaussian | `k+1` responses | `k(k+1)/2` updates |

The first column is the same-orientation Wick sector; the second contains all
opposite-orientation identifications with earlier matrix uses; the third is
the literal finite-width gradient update (4.2).  Any additional equality of
free indices loses one free sum without a compensating normalization and is
`O(n^(-1))`.  A numerical row-index/column-index equality is not a legal
Wick delta because the two index types are untied.  These cases exhaust all
equality partitions through order five.

All 21 forward covariances `H_kl,0<=l<=k<=5` and all 15 reverse
covariances `B_kl,0<=l<=k<=4` are materialized.  The complete nonzero
transpose-response registry is

\[
\begin{array}{c|c|c}
k&\{s:\alpha_{ks}\ne0\}&\{s:\beta_{ks}\ne0\}\\ \hline
0&\varnothing&\varnothing\\
1&\{0\}&\{0\}\\
2&\{1\}&\{1\}\\
3&\{0,2\}&\{0,2\}\\
4&\{1,3\}&\{1,3\}\\
5&\{0,2,4\}&--
\end{array}
\tag{4.5}
\]

with every omitted entry identically zero by readout parity.  Thus all 15
forward and 15 transpose response slots are evaluated, including the zero
`beta_00` slot; none is silently dropped.  Wick pairing of the surviving
fresh sectors is retained in the covariance registries and eliminated only
by Section 5's exact rules.

## 5. Exact elimination of the temporary Gaussians

On the first-neuron side, the activation argument `U` is independent of
the temporary transpose Gaussian family.  Ordinary Wick recursion therefore
eliminates every `R` monomial into products of `B_ij` and one `X` atom.

On the second-neuron side, `F_0=Z` is the activation argument.  For
`i>=1`, the only needed integration identity is the exact multivariate
Stein rule

\[
\begin{aligned}
\mathbb E[F_iF^\rho Y^\nu]
={}&\sum_{j\ge1}\rho_jH_{ij}
\mathbb E[F^{\rho-e_j}Y^\nu]\\
&+H_{i0}\sum_{r\ge0}\nu_r
\mathbb E[F^\rho Y^{\nu-e_r+e_{r+1}}].
\end{aligned}
\tag{5.1}
\]

Together with Wick's rule for the independent readout Gaussian, (5.1)
strictly lowers the number of explicit temporary Gaussian factors.  Its base
case is exactly a one-dimensional `Y_nu` atom.  Thus termination and the
one-dimensional terminal grammar are proved, not inferred from numerical
experiments.

## 6. Algebraic audits and controls

The primary factored map was frozen before inspecting the independent map.
A second compiler then expanded its own derivation distributively.  After the
common quotient (1.4), exact rational comparison gave

| map | primary terms | independent terms | discrepancies |
|---|---:|---:|---:|
| `A` | 3 | 3 | 0 |
| `B` | 46 | 46 | 0 |
| `C` | 974 | 974 | 0 |

The machine-readable ledger is
[`compiler/INDEPENDENT_COMPARISON.json`](compiler/INDEPENDENT_COMPARISON.json).
Before the unit quotient, the independently frozen layer-tagged
\(Q^0=1\) maps also agree exactly: 3, 50, and 1,045 monomials for
\(A,B,C\) with zero discrepancies.  The explicit symbolic \(Q^0\) powers
also received an independent exact audit.  Before loading the primary map,
the independent compiler was evaluated at the six fixed rational points
\(1/2,1,3/2,2,5/2,3\) and interpolated under the separately proved degree
bounds \(1,3,5\) for \(A,B,C\).  Its unused \(Q^0=7/2\) holdout had zero
discrepancies; the resulting graded map was then frozen and compared with the
primary map.  All 3, 50, and 1,045 graded terms agreed exactly, with zero
discrepancies.  The frozen map and comparison are
[`independent_symbolic_q0_coefficient_map.json`](independent/independent_symbolic_q0_coefficient_map.json)
and
[`SYMBOLIC_Q0_PRIMARY_COMPARISON.json`](independent/SYMBOLIC_Q0_PRIMARY_COMPARISON.json).
Thus the arbitrary-variance DAG and the unit-Gram quotient have both received
full independent coefficient audits.  In particular the linear activation
gives exactly
\((A,B,C)=(3Q^0,48(Q^0)^2,1464(Q^0)^3)\).  This is an additional
scaling check, not an assumption used by the interpolation.

The exact layer-separated controls are

\[
\begin{array}{c|ccc}
\phi & A&B&C\\ \hline
c&c^2&0&0\\
x&3&48&1464\\
1+x&6&112&4400\\
x^2&111&1\,685\,184&77\,400\,633\,120.
\end{array}
\tag{6.1}
\]

The unnormalised quadratic row uses `Q0=1,Q1=3,Q2=27` and therefore
tests the layer-separated formula, not the unit-Gram quotient.  It gives

\[
\mu_0={280864\over4107},\qquad
\mu_1={38443196932\over5616860517}.
\tag{6.2}
\]

At every finite width, readout reflection gives
`(D_n^k f_n)(r,W,-a)=(-1)^(k+1)(D_n^k f_n)(r,W,a)`.
Gaussian readout symmetry therefore proves
`E f_n=E D_n^2f_n=E D_n^4f_n=0` before the limit.  Equivalently,
`F(t)=-F(-t)` after annealing: if `S` flips the initial readout
signs, the flow satisfies
`theta(t;S theta_0)=S theta(-t;theta_0)`.  Hence

\[
F(0)=F''(0)=F^{(4)}(0)=0.
\tag{6.3}
\]

For the preregistered normalized sine

\[
\phi(x)={\sin x\over\sqrt{(1-e^{-2})/2}},
\]

exact finite Fourier evaluation of the terminal sine/cosine products
(independently confirmed by Gaussian quadrature) gives

\[
\begin{aligned}
A&=4.03709694646564,\\
B&=-103.257331146774,\\
C&=29944.4323429373,\\
\mu_0&=-3.16776198608130,\\
\mu_1&=-3.03999737837846.
\end{aligned}
\tag{6.4}
\]

Both putative moment coefficients are negative.  Thus for this activation the
one-pole rational object is a **Padé approximation only**, not a positive
Stieltjes approximant.

The preregistered finite-width panel used widths
`32,64,128,256,512` with 256 independent networks per width.  The two
finite-width fifth-derivative implementations first agreed seedwise to
`2.92e-14` scaled error.  Weighted affine extrapolation in `1/n` gave

\[
\widehat C_\infty=26949.7517\pm2326.2946,
\]

so the theoretical prediction in (6.4) is `1.2873` standard errors away.
The regression diagnostic was valid
(`chi^2=0.7734` on three degrees of freedom), hence this is a
preregistered **pass**, not a post-hoc enlarged experiment.

## 7. Inversion, Padé kernel, and induced loss curve

Assume `A != 0`.  From parity,

\[
F(t)=At+{B\over3!}t^3+{C\over5!}t^5+O(t^7).
\]

Direct local series reversion and substitution into
`K(y)=F'(F^{-1}(y))` give

\[
\boxed{
\mu_0={B\over2A^2},
\qquad
\mu_1={4B^2-AC\over24A^5},
}
\tag{7.1}
\]

and, with the sign convention fixed as displayed,

\[
\boxed{
K(y)=F'(F^{-1}(y))
=A+\mu_0y^2-\mu_1y^4+O(y^6).
}
\tag{7.2}
\]

If additionally `mu0 != 0`, the requested first one-pole Padé
approximant to **the kernel `K`** is

\[
\boxed{
K_{[0/1]}(y)
=A+{\mu_0y^2\over1+(\mu_1/\mu_0)y^2}.
}
\tag{7.3}
\]

It is called a positive Stieltjes approximant only after separately verifying
the local setup \(A>0\), the moment signs \(\mu_0>0\) and
\(\mu_1\ge0\), and the relevant nondegeneracy/no-pole conditions (a genuine
finite one-pole scale has \(\mu_1>0\)).  Smoothness of `phi` does not imply
these conditions, as the sine control demonstrates.

For one-sample MSE with label one and no `1/2` in the loss, the rational
kernel (7.3) induces

\[
\dot y=2\eta(1-y)K_{[0/1]}(y),
\qquad L_{[0/1]}=(1-y)^2.
\tag{7.4}
\]

Starting from `y(0)=0`, its exact separated solution is

\[
\boxed{
2\eta t
=\int_0^{y(t)}
{1+(\mu_1/\mu_0)s^2
\over
(1-s)\left[A+(A\mu_1/\mu_0+\mu_0)s^2\right]}
\,ds,
\qquad
L_{[0/1]}(t)=(1-y(t))^2.
}
\tag{7.5}
\]

Equation (7.5) holds on the connected interval from zero containing no pole
or zero of its displayed denominator.  It is an exact curve for the rational
kernel, not a claim that the positive-time finite-width neural trajectory
equals this curve.

## 8. Annealed theorem hypotheses and claim ladder

The exact finite-width identities through order five need only the displayed
derivatives of `phi` to exist and the finite contractions to be integrable.
A convenient finite-algebra envelope is `phi in C^5` with
`phi^(r)` of polynomial growth for `0<=r<=5`.

For the theorem-level annealed limit used here, a sufficient envelope is:

1. `phi in C-infinity` and, for every `r>=0`, there are finite
   `C_r,m_r` with
   `|phi^(r)(x)| <= C_r(1+|x|^m_r)`;
2. `Q0` is fixed and finite, depth and batch are fixed, and all
   initialization variables are the independent standard Gaussians in the
   model;
3. the exact chronological graph (4.1)--(5.1), including every transpose
   response and empirical moment, is treated as one fixed finite
   NETSOR-transpose-plus scalar program.

There are then two distinct routes from the fixed-program limit to the
annealed statement.  Under polynomial smoothness, Golikov--Yang,
[*Non-Gaussian Tensor Programs*](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf),
Theorem 3.7, directly supplies convergence in every finite \(L^p\)
(Gaussian matrices are a special case), and therefore expectation
convergence.

In a weaker almost-sure or in-probability tier, one must separately assume or
prove, for some \(\epsilon>0\), the uniform moment bound

\[
\sup_n\mathbb E|D_n^kf_n|^{1+\epsilon}<\infty,
\qquad k\in\{1,3,5\}.
\tag{8.1}
\]

Bound (8.1) implies uniform integrability; together with convergence in
probability it yields \(L^1\), hence expectation, convergence.  It is not
equivalent to \(L^{1+\epsilon}\) convergence and is not claimed to be.
The weaker almost-sure pseudo-Lipschitz program limit itself is supplied by
the NETSOR-transpose master theorem in
[*Tensor Programs III*](https://arxiv.org/abs/2009.10685), Appendix E.15;
that tier by itself does not justify annealed convergence.

The result's status ladder is therefore:

- **exact finite width:** the feature ODE, Taylor jet, parity identity, and
  six-family `D_n^5f_n` tensor contraction;
- **formal candidate:** the response-aware population peel before Gaussian
  elimination;
- **algebraically audited:** the terminal `A,B,C` moment maps, after
  exact Wick--Stein elimination, frozen unit, layer-tagged, and symbolic-
  \(Q^0\) atomwise comparisons, and all controls;
- **theorem-level:** `F^(k)(0)=lim_n E[D_n^kf_n]` for
  `k=1,3,5` under the polynomial-smooth fixed-program and
  uniform-integrability envelope above.

No Hermite approximation is used at any level.

## 9. Final claim level

The exact finite-width ODE (4.1)--(4.2) is an identity.  Equations
(4.3)--(5.1) are the formal population peel.  The emitted formulas are
algebraically audited normal forms because the independently frozen maps
agree atom by atom in every declared quotient and all exact controls pass.
Under Section 8's
polynomial-smooth fixed-program envelope, the all-finite-`Lp` bridge
promotes them to the stated annealed large-width derivatives.
