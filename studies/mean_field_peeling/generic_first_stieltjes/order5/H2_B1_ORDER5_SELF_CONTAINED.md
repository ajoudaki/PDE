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

## Appendix A. Complete unit-Gram arithmetic DAG

This appendix is part of the formula.  It is repeated here so the report is
self-contained.  Every assignment is deterministic and dependency first.

<!-- BEGIN EMBEDDED UNIT ARTIFACT -->
```text
# GENERATED FILE -- do not edit by hand.
# Generator: compiler/generate_artifacts.py
# Grammar: dependency-first deterministic arithmetic DAG.
# Each t_N is defined before use.  There are no random/tangent/response nodes.
# Moment alphabet: M_nu=E_{G~N(0,1)}[product_r phi^(r)(G)^nu_r], with M_200000=1
# Exponent order is (phi,phi',phi'',phi''',phi^(4),phi^(5)).
t_00000 = 1 + M_{020000}
t_00001 = M_{020000} * t_00000
t_00002 = 1 + t_00001
t_00003 = 1/2 * M_{020000}
t_00004 = 1/2 + t_00003
t_00005 = 1/3 * t_00004
t_00006 = 1/2 + t_00003 + t_00005
t_00007 = M_{220000} * t_00006
t_00008 = t_00000 * M_{002000}
t_00009 = t_00000 * M_{010100}
t_00010 = 2 * M_{020000}
t_00011 = M_{101000} + t_00008 + t_00009 + t_00010
t_00012 = 1/2 * M_{220000} * t_00011
t_00013 = M_{020000} * M_{121000}
t_00014 = t_00012 + t_00013
t_00015 = M_{020000} * t_00014
t_00016 = M_{101000} * t_00014
t_00017 = t_00015 + t_00016
t_00018 = 4/3 * t_00017
t_00019 = 1/2 * M_{020000} * M_{020000} * M_{040000}
t_00020 = 2/3 * M_{020000} * M_{101000} * M_{040000}
t_00021 = t_00004 * M_{002000}
t_00022 = 2 + t_00010
t_00023 = 1/2 * M_{010100} * t_00022
t_00024 = M_{020000} + M_{101000} + t_00021 + t_00023
t_00025 = 1/3 * M_{040000} * t_00024
t_00026 = 1/2 * t_00011
t_00027 = M_{101000} + t_00008 + t_00009 + t_00010 + t_00026
t_00028 = 1/3 * t_00027
t_00029 = t_00026 + t_00028
t_00030 = M_{121000} * t_00029
t_00031 = 2 * M_{020000} * M_{022000}
t_00032 = M_{020000} * M_{030100}
t_00033 = 1/2 * M_{020000} * M_{040000}
t_00034 = 1/3 * t_00014
t_00035 = t_00012 + t_00013 + t_00025 + t_00030 + t_00031 + t_00032 + t_00033 + t_00034
t_00036 = M_{020000} * t_00035
t_00037 = 1/2 * t_00000 * t_00000
t_00038 = 1/6 * M_{020000} * t_00000
t_00039 = 1/6 * t_00000
t_00040 = t_00037 + t_00038 + t_00039
t_00041 = M_{040000} * t_00040
t_00042 = 1/2 * M_{020000} * t_00000
t_00043 = 1/2 * t_00000
t_00044 = t_00037 + t_00042 + t_00043
t_00045 = 1/3 * t_00044
t_00046 = t_00000 * t_00004
t_00047 = 3/2 * M_{020000}
t_00048 = 3/2 + t_00047
t_00049 = 1/3 * M_{020000} * t_00048
t_00050 = 1/3 * t_00048
t_00051 = t_00037 + t_00042 + t_00043 + t_00045 + t_00046 + t_00049 + t_00050
t_00052 = M_{121000} * t_00051
t_00053 = M_{002000} * t_00014
t_00054 = M_{010100} * t_00014
t_00055 = t_00053 + t_00054
t_00056 = 1/2 * t_00022
t_00057 = 1/3 * M_{020000}
t_00058 = 1/3 + t_00056 + t_00057
t_00059 = t_00055 * t_00058
t_00060 = 1/2 * M_{020000} * t_00000 * M_{002000} * M_{040000}
t_00061 = 1/6 * M_{020000}
t_00062 = 3 * M_{020000}
t_00063 = 3 + t_00062
t_00064 = 1/6 * t_00063
t_00065 = 1/6 + t_00061 + t_00064
t_00066 = M_{020000} * M_{010100} * M_{040000} * t_00065
t_00067 = t_00042 + t_00043
t_00068 = t_00000 * t_00067
t_00069 = 1/3 * M_{020000} * t_00067
t_00070 = 1/3 * t_00067
t_00071 = t_00068 + t_00069 + t_00070
t_00072 = 3 * M_{022000} * t_00071
t_00073 = 1/6 * M_{020000} * t_00000 * t_00000
t_00074 = 1/6 * t_00000 * t_00000
t_00075 = 1/6 * t_00000 * t_00000 * t_00000
t_00076 = t_00073 + t_00074 + t_00075
t_00077 = 3 * M_{030100} * t_00076
t_00078 = t_00007 + t_00018 + t_00019 + t_00020 + t_00036 + t_00041 + t_00052 + t_00059 + t_00060 + t_00066 + t_00072 + t_00077
t_00079 = 6 * t_00078
t_00080 = M_{020000} * M_{022000}
t_00081 = 1/3 + t_00057
t_00082 = M_{002000} * t_00081
t_00083 = M_{101000} + t_00023 + t_00057 + t_00082
t_00084 = 1/2 * t_00083
t_00085 = t_00061 + t_00084
t_00086 = 1/4 * M_{040000} * t_00085
t_00087 = 1/2 * t_00011 * M_{121000}
t_00088 = 1/2 * M_{020000} * M_{030100}
t_00089 = 1/3 * M_{020000} * M_{040000}
t_00090 = 3/4 * t_00014
t_00091 = t_00080 + t_00086 + t_00087 + t_00088 + t_00089 + t_00090
t_00092 = 1/5 * t_00091
t_00093 = t_00080 + t_00086 + t_00087 + t_00088 + t_00089 + t_00090 + t_00092
t_00094 = M_{220000} * t_00093
t_00095 = 1/3 * t_00004 * t_00004
t_00096 = 1/12 * M_{020000} * t_00004
t_00097 = 1/12 * t_00004
t_00098 = t_00096 + t_00097
t_00099 = 1/5 * t_00098
t_00100 = t_00095 + t_00096 + t_00097 + t_00099
t_00101 = M_{240000} * t_00100
t_00102 = 1/4 * M_{020000} * t_00004
t_00103 = 1/4 * t_00004
t_00104 = 1/2 * t_00004 * t_00004
t_00105 = t_00102 + t_00103 + t_00104
t_00106 = 1/5 * t_00105
t_00107 = t_00102 + t_00103 + t_00104 + t_00106
t_00108 = M_{321000} * t_00107
t_00109 = 1/2 * t_00000 * M_{040000}
t_00110 = M_{121000} * t_00048
t_00111 = 3 * M_{022000} * t_00067
t_00112 = 3/2 * t_00000 * t_00000 * M_{030100}
t_00113 = 1/3 * t_00004 * M_{040000}
t_00114 = 2 * t_00004
t_00115 = 1/2 + t_00003 + t_00114
t_00116 = M_{121000} * t_00115
t_00117 = t_00004 * M_{202000}
t_00118 = t_00004 * M_{210100}
t_00119 = 5/3 * t_00055
t_00120 = t_00014 * M_{100010}
t_00121 = 2/3 * M_{020000} * M_{002000} * M_{040000}
t_00122 = 1/2 * M_{020000} * M_{040000} * M_{100010}
t_00123 = M_{002000} * t_00035
t_00124 = M_{010100} * t_00035
t_00125 = t_00037 + t_00038 + t_00039 + t_00045
t_00126 = 3 * t_00125
t_00127 = t_00042 + t_00043 + t_00049 + t_00050 + t_00126
t_00128 = M_{022000} * t_00127
t_00129 = t_00000 * t_00000
t_00130 = t_00038 + t_00039 + t_00129 + t_00045 + t_00046
t_00131 = M_{030100} * t_00130
t_00132 = t_00042 + t_00043 + t_00049 + t_00050
t_00133 = M_{103000} * t_00132
t_00134 = 2 * t_00132
t_00135 = t_00037 + t_00046
t_00136 = 2 * t_00135
t_00137 = t_00134 + t_00136
t_00138 = M_{111100} * t_00137
t_00139 = t_00135 * M_{120010}
t_00140 = t_00014 * M_{000200}
t_00141 = t_00014 * M_{001010}
t_00142 = t_00140 + t_00141
t_00143 = 2 * t_00081
t_00144 = t_00056 + t_00143
t_00145 = t_00142 * t_00144
t_00146 = t_00014 * M_{010001}
t_00147 = t_00141 + t_00146
t_00148 = 1/2 * t_00022 * t_00147
t_00149 = 1/6 + t_00043 + t_00061
t_00150 = M_{020000} * M_{040000} * M_{000200} * t_00149
t_00151 = 1/6 + t_00043 + t_00061 + t_00064
t_00152 = M_{020000} * M_{040000} * M_{001010} * t_00151
t_00153 = 1/6 * M_{020000} * M_{040000} * t_00063 * M_{010001}
t_00154 = t_00069 + t_00070
t_00155 = 3 * M_{004000} * t_00154
t_00156 = 3 * t_00154
t_00157 = t_00068 + t_00073 + t_00074
t_00158 = 2 * t_00157
t_00159 = t_00156 + t_00158
t_00160 = 3 * M_{012100} * t_00159
t_00161 = 3 * t_00157 * M_{020200}
t_00162 = 1/2 * t_00000 * t_00000 * t_00000
t_00163 = t_00068 + t_00073 + t_00074 + t_00162
t_00164 = 3 * M_{021010} * t_00163
t_00165 = 1/2 * t_00000 * t_00000 * t_00000 * M_{030001}
t_00166 = 2 * M_{010100} * t_00014
t_00167 = 5/3 * M_{020000} * M_{010100} * M_{040000}
t_00168 = M_{121000} * t_00022
t_00169 = M_{020000} * M_{002000} * M_{040000}
t_00170 = 3 * t_00000 * t_00000 * M_{022000}
t_00171 = M_{220000} + t_00168 + t_00169 + t_00170
t_00172 = 1/2 * t_00171
t_00173 = 1/2 * M_{020000} * M_{010100} * M_{040000}
t_00174 = t_00053 + t_00054 + t_00109 + t_00110 + t_00111 + t_00112 + t_00173
t_00175 = 1/3 * t_00174
t_00176 = t_00053 + t_00109 + t_00110 + t_00111 + t_00112 + t_00113 + t_00116 + t_00117 + t_00118 + t_00119 + t_00120 + t_00121 + t_00122 + t_00123 + t_00124 + t_00128 + t_00131 + t_00133 + t_00138 + t_00139 + t_00145 + t_00148 + t_00150 + t_00152 + t_00153 + t_00155 + t_00160 + t_00161 + t_00164 + t_00165 + t_00166 + t_00167 + t_00172 + t_00175
t_00177 = 1/4 * M_{220000} * t_00176
t_00178 = 1/2 * t_00011 * t_00083
t_00179 = 1/6 * M_{020000} * t_00011
t_00180 = t_00178 + t_00179
t_00181 = 1/4 * M_{240000} * t_00180
t_00182 = 1/4 * t_00011 * t_00011 * M_{321000}
t_00183 = 1/4 * M_{121000} * t_00171
t_00184 = 2/3 * M_{121000} * t_00174
t_00185 = 1/3 * t_00024
t_00186 = M_{010100} * t_00022
t_00187 = 2 * M_{101000}
t_00188 = 5/3 * M_{020000}
t_00189 = t_00021 + t_00186 + t_00082 + t_00185 + t_00187 + t_00188
t_00190 = 1/4 * t_00189
t_00191 = t_00185 + t_00190
t_00192 = M_{020000} * M_{141000} * t_00191
t_00193 = 1/4 * t_00029
t_00194 = 2/3 * t_00027
t_00195 = t_00026 + t_00194
t_00196 = 1/2 * t_00195
t_00197 = t_00193 + t_00196
t_00198 = M_{020000} * t_00197 * M_{222000}
t_00199 = 1/4 * t_00011
t_00200 = 1/6 * t_00027
t_00201 = t_00199 + t_00200
t_00202 = M_{020000} * t_00201 * M_{230100}
t_00203 = M_{020000} * M_{020000} * M_{123000}
t_00204 = 7/4 * M_{020000} * M_{020000} * M_{131100}
t_00205 = 1/4 * M_{020000} * M_{020000} * M_{140010}
t_00206 = t_00177 + t_00181 + t_00182 + t_00183 + t_00184 + t_00192 + t_00198 + t_00202 + t_00203 + t_00204 + t_00205
t_00207 = M_{020000} * t_00206
t_00208 = M_{101000} * t_00206
t_00209 = t_00207 + t_00208
t_00210 = 6/5 * t_00209
t_00211 = t_00014 * M_{040000}
t_00212 = 3 * M_{121000} * t_00014
t_00213 = t_00211 + t_00212
t_00214 = 2/3 * t_00004
t_00215 = 1/12 * M_{020000}
t_00216 = 1/12 + t_00215
t_00217 = 1/5 * t_00216
t_00218 = 1/12 + t_00214 + t_00215 + t_00217
t_00219 = t_00213 * t_00218
t_00220 = 2 * M_{121000} * t_00014
t_00221 = t_00014 * M_{202000}
t_00222 = t_00014 * M_{210100}
t_00223 = t_00220 + t_00221 + t_00222
t_00224 = 1/4 * M_{020000}
t_00225 = 1/4 + t_00043 + t_00224
t_00226 = 1/5 * t_00225
t_00227 = 1/4 + t_00043 + t_00224 + t_00226
t_00228 = t_00223 * t_00227
t_00229 = 1/4 * t_00011 * t_00011 * M_{240000}
t_00230 = 1/4 * M_{040000} * t_00171
t_00231 = M_{020000} * t_00011 * M_{141000}
t_00232 = 3 * M_{020000} * M_{020000} * M_{042000}
t_00233 = t_00229 + t_00230 + t_00231 + t_00232
t_00234 = M_{020000} * t_00233
t_00235 = 2 * t_00014 * t_00055
t_00236 = t_00234 + t_00235
t_00237 = 1/3 * t_00236
t_00238 = t_00014 * t_00055
t_00239 = M_{101000} * t_00233
t_00240 = t_00054 + t_00120
t_00241 = t_00014 * t_00240
t_00242 = t_00238 + t_00239 + t_00241
t_00243 = 3/5 * t_00242
t_00244 = 1/3 * M_{040000} * t_00174
t_00245 = 1/3 * M_{020000} * t_00024 * M_{060000}
t_00246 = M_{020000} * t_00029 * M_{141000}
t_00247 = 2 * M_{020000} * M_{020000} * M_{042000}
t_00248 = M_{020000} * M_{020000} * M_{050100}
t_00249 = t_00244 + t_00245 + t_00246 + t_00247 + t_00248
t_00250 = 3/4 * M_{020000} * t_00249
t_00251 = 6/5 * M_{101000} * t_00249
t_00252 = 1/6 + t_00061
t_00253 = 3/4 * M_{020000} * M_{040000} * M_{040000} * t_00252
t_00254 = 1/2 * t_00081
t_00255 = 1/6 + t_00061 + t_00254
t_00256 = 1/5 * t_00255
t_00257 = 1/3 + t_00043 + t_00057
t_00258 = 3/4 * t_00257
t_00259 = 1/6 + t_00005 + t_00061 + t_00254 + t_00256 + t_00258
t_00260 = M_{020000} * M_{121000} * M_{040000} * t_00259
t_00261 = 2/3 * M_{020000}
t_00262 = 2/3 + t_00261
t_00263 = 3/5 * M_{020000} * M_{040000} * M_{202000} * t_00262
t_00264 = 1/6 * t_00048
t_00265 = 1/8 * M_{020000}
t_00266 = 1/8 + t_00264 + t_00265
t_00267 = 1/5 * t_00266
t_00268 = 1/8 + t_00264 + t_00265 + t_00267
t_00269 = M_{020000} * M_{040000} * M_{210100} * t_00268
t_00270 = 13/12 * M_{020000} * M_{040000} * t_00055
t_00271 = 3/5 * M_{020000} * M_{040000} * t_00240
t_00272 = 1/4 * M_{020000} * M_{020000} * M_{002000} * M_{040000} * M_{040000}
t_00273 = 3/8 * M_{020000} * M_{020000} * M_{010100} * M_{040000} * M_{040000}
t_00274 = 3/20 * M_{020000} * M_{020000} * M_{040000} * M_{040000} * M_{100010}
t_00275 = 1/4 * M_{040000} * t_00252
t_00276 = 1/4 * t_00257
t_00277 = 5/6 * t_00004
t_00278 = 1/6 + t_00061 + t_00276 + t_00277
t_00279 = M_{121000} * t_00278
t_00280 = t_00081 * M_{202000}
t_00281 = 1/2 * t_00000 * M_{210100}
t_00282 = 13/12 * t_00055
t_00283 = 1/2 * M_{020000} * M_{002000} * M_{040000}
t_00284 = 7/8 * M_{020000} * M_{010100} * M_{040000}
t_00285 = M_{002000} * t_00091
t_00286 = M_{220000} * t_00011
t_00287 = M_{020000} * M_{040000}
t_00288 = 2 * M_{020000} * M_{121000}
t_00289 = 2/3 * M_{040000} * t_00024
t_00290 = 2 * M_{121000} * t_00029
t_00291 = 4 * M_{020000} * M_{022000}
t_00292 = 2 * M_{020000} * M_{030100}
t_00293 = 2/3 * t_00014
t_00294 = t_00286 + t_00287 + t_00288 + t_00289 + t_00290 + t_00291 + t_00292 + t_00293
t_00295 = 1/2 * M_{010100} * t_00294
t_00296 = 1/2 * t_00067
t_00297 = 1/2 * t_00000 * t_00004
t_00298 = 1/3 * M_{020000} * t_00004
t_00299 = 2 * t_00000 * t_00004
t_00300 = 1 + M_{020000} + t_00001 + t_00299
t_00301 = 1/2 * t_00300
t_00302 = t_00005 + t_00298 + t_00301
t_00303 = 1/4 * t_00302
t_00304 = 1/2 + t_00003 + t_00056
t_00305 = 1/3 * t_00304
t_00306 = 7/6 * M_{020000}
t_00307 = 7/6 + t_00305 + t_00306
t_00308 = 1/4 * M_{020000} * t_00307
t_00309 = 1/4 * t_00307
t_00310 = 1/3 * t_00000 * t_00304
t_00311 = t_00045 + t_00296 + t_00297 + t_00303 + t_00308 + t_00309 + t_00310
t_00312 = M_{022000} * t_00311
t_00313 = 1/4 * t_00000 * t_00000
t_00314 = 1/4 * t_00000 * t_00022
t_00315 = 1/6 * M_{020000} * t_00022
t_00316 = 1/6 * t_00022
t_00317 = t_00000 * t_00022
t_00318 = t_00129 + t_00317
t_00319 = 1/6 * t_00318
t_00320 = t_00315 + t_00316 + t_00319
t_00321 = 1/4 * t_00320
t_00322 = 1/3 * M_{020000} * t_00000
t_00323 = 1/3 * t_00000
t_00324 = 2 * t_00000 * t_00252
t_00325 = t_00322 + t_00323 + t_00324
t_00326 = 1/2 * t_00325
t_00327 = t_00313 + t_00314 + t_00321 + t_00326
t_00328 = M_{030100} * t_00327
t_00329 = 5/6 * M_{020000}
t_00330 = 5/6 + t_00329
t_00331 = 1/4 * M_{020000} * t_00330
t_00332 = 1/4 * t_00330
t_00333 = t_00005 + t_00298 + t_00331 + t_00332
t_00334 = M_{103000} * t_00333
t_00335 = t_00043 + t_00056
t_00336 = 1/4 * M_{020000} * t_00335
t_00337 = 1/4 * t_00335
t_00338 = 2/3 * M_{020000} * t_00048
t_00339 = 2/3 * t_00048
t_00340 = 2 * t_00004 * t_00004
t_00341 = 2 * t_00000 * t_00081
t_00342 = t_00338 + t_00339 + t_00340 + t_00341
t_00343 = 1/2 * t_00342
t_00344 = t_00301 + t_00315 + t_00316 + t_00336 + t_00337 + t_00343
t_00345 = M_{111100} * t_00344
t_00346 = t_00004 * t_00022
t_00347 = t_00129 + t_00299 + t_00346
t_00348 = 1/6 * t_00347
t_00349 = t_00319 + t_00348
t_00350 = M_{120010} * t_00349
t_00351 = 5/3 + t_00188
t_00352 = 1/2 * t_00351
t_00353 = 1/4 + t_00224 + t_00352
t_00354 = t_00142 * t_00353
t_00355 = 2 * t_00000
t_00356 = 4 * M_{020000}
t_00357 = 4 + t_00355 + t_00356
t_00358 = 1/6 * t_00147 * t_00357
t_00359 = 3/2 * M_{020000} * M_{040000} * t_00081 * M_{000200}
t_00360 = 1/24 * M_{020000}
t_00361 = 1/24 + t_00264 + t_00360
t_00362 = 3 * M_{020000} * M_{040000} * M_{001010} * t_00361
t_00363 = 4 + t_00356
t_00364 = 1/8 * M_{020000} * M_{040000} * M_{010001} * t_00363
t_00365 = t_00005 + t_00298
t_00366 = 1/4 * M_{020000} * t_00365
t_00367 = 1/4 * t_00365
t_00368 = t_00366 + t_00367
t_00369 = 3 * M_{004000} * t_00368
t_00370 = t_00301 + t_00315 + t_00316
t_00371 = 1/4 * M_{020000} * t_00370
t_00372 = 1/4 * t_00370
t_00373 = 2 * t_00004 * t_00067
t_00374 = 2/3 * M_{020000} * t_00067
t_00375 = 2/3 * t_00067
t_00376 = 2 * t_00000 * t_00365
t_00377 = t_00373 + t_00374 + t_00375 + t_00376
t_00378 = 1/2 * t_00377
t_00379 = t_00371 + t_00372 + t_00378
t_00380 = 3 * M_{012100} * t_00379
t_00381 = 1/3 * M_{020000} * t_00000 * t_00000
t_00382 = 1/3 * t_00000 * t_00000
t_00383 = t_00315 + t_00316
t_00384 = 2 * t_00000 * t_00383
t_00385 = t_00381 + t_00382 + t_00384
t_00386 = 3/2 * M_{020200} * t_00385
t_00387 = 1/24 * M_{020000} * t_00318
t_00388 = 1/24 * t_00318
t_00389 = t_00000 * t_00000 * t_00004
t_00390 = t_00022 * t_00067
t_00391 = 2 * t_00000 * t_00067
t_00392 = t_00000 * t_00300
t_00393 = t_00389 + t_00390 + t_00391 + t_00392
t_00394 = 1/6 * t_00393
t_00395 = t_00387 + t_00388 + t_00394
t_00396 = 3 * M_{021010} * t_00395
t_00397 = t_00000 * t_00000 * t_00000
t_00398 = t_00000 * t_00318
t_00399 = t_00397 + t_00398
t_00400 = 1/8 * M_{030001} * t_00399
t_00401 = 1/3 * t_00171
t_00402 = 3/4 * t_00174
t_00403 = t_00054 + t_00120 + t_00122 + t_00275 + t_00279 + t_00280 + t_00281 + t_00282 + t_00283 + t_00284 + t_00285 + t_00295 + t_00312 + t_00328 + t_00334 + t_00345 + t_00350 + t_00354 + t_00358 + t_00359 + t_00362 + t_00364 + t_00369 + t_00380 + t_00386 + t_00396 + t_00400 + t_00401 + t_00402
t_00404 = 1/5 * M_{040000} * t_00403
t_00405 = 1/4 + t_00224
t_00406 = M_{002000} * t_00405
t_00407 = M_{101000} + t_00023 + t_00224 + t_00406
t_00408 = 1/3 * t_00024 * t_00407
t_00409 = 1/12 * M_{020000} * t_00024
t_00410 = t_00408 + t_00409
t_00411 = 1/5 * M_{060000} * t_00410
t_00412 = 1/4 * t_00176
t_00413 = t_00053 + t_00109 + t_00110 + t_00111 + t_00112 + t_00113 + t_00116 + t_00117 + t_00118 + t_00119 + t_00120 + t_00121 + t_00122 + t_00123 + t_00124 + t_00128 + t_00131 + t_00133 + t_00138 + t_00139 + t_00145 + t_00148 + t_00150 + t_00152 + t_00153 + t_00155 + t_00160 + t_00161 + t_00164 + t_00165 + t_00166 + t_00167 + t_00172 + t_00175 + t_00412
t_00414 = 1/5 * t_00413
t_00415 = t_00412 + t_00414
t_00416 = M_{121000} * t_00415
t_00417 = 1/4 * t_00180
t_00418 = t_00029 * t_00407
t_00419 = 1/4 * M_{020000} * t_00029
t_00420 = 5/6 * t_00011 * t_00024
t_00421 = t_00178 + t_00179 + t_00417 + t_00418 + t_00419 + t_00420
t_00422 = 1/5 * t_00421
t_00423 = 1/2 * t_00180
t_00424 = 1/3 * t_00011 * t_00024
t_00425 = t_00423 + t_00424
t_00426 = 1/2 * t_00425
t_00427 = t_00422 + t_00426
t_00428 = M_{141000} * t_00427
t_00429 = 1/8 * t_00011 * t_00011
t_00430 = 1/3 * t_00011 * t_00027
t_00431 = t_00429 + t_00430
t_00432 = 1/5 * t_00431
t_00433 = 1/4 * t_00011 * t_00011
t_00434 = t_00430 + t_00433
t_00435 = 1/2 * t_00434
t_00436 = t_00432 + t_00435
t_00437 = M_{222000} * t_00436
t_00438 = 1/4 * t_00011 * t_00011 * M_{230100}
t_00439 = 1/2 * M_{022000} * t_00171
t_00440 = 1/4 * M_{030100} * t_00171
t_00441 = 4/3 * M_{022000} * t_00174
t_00442 = 2/3 * M_{030100} * t_00174
t_00443 = 2/3 * t_00407
t_00444 = 1/2 * t_00024
t_00445 = M_{101000} + t_00023 + t_00082 + t_00190 + t_00329 + t_00443 + t_00444
t_00446 = 1/5 * t_00445
t_00447 = 1/2 * t_00189
t_00448 = t_00185 + t_00447
t_00449 = 1/2 * t_00448
t_00450 = t_00446 + t_00449
t_00451 = 3 * M_{020000} * M_{042000} * t_00450
t_00452 = 1/6 * t_00024
t_00453 = 1/3 * t_00407
t_00454 = 5/6 * t_00024
t_00455 = t_00215 + t_00453 + t_00454
t_00456 = 1/5 * t_00455
t_00457 = t_00452 + t_00456
t_00458 = 3 * M_{020000} * M_{050100} * t_00457
t_00459 = 1/6 * t_00011
t_00460 = t_00193 + t_00459
t_00461 = 1/5 * t_00460
t_00462 = 1/2 * t_00029
t_00463 = t_00028 + t_00459 + t_00462
t_00464 = 1/2 * t_00463
t_00465 = t_00461 + t_00464
t_00466 = 3 * M_{020000} * M_{123000} * t_00465
t_00467 = 1/3 * t_00011
t_00468 = 11/12 * t_00011
t_00469 = t_00196 + t_00468
t_00470 = 1/5 * t_00469
t_00471 = 2 * t_00000 * M_{002000}
t_00472 = 2 * t_00000 * M_{010100}
t_00473 = t_00011 + t_00187 + t_00356 + t_00471 + t_00472
t_00474 = 1/6 * t_00473
t_00475 = t_00467 + t_00470 + t_00474
t_00476 = 3 * M_{020000} * M_{131100} * t_00475
t_00477 = t_00200 + t_00459
t_00478 = 1/5 * t_00477
t_00479 = t_00187 + t_00356 + t_00471 + t_00472
t_00480 = 1/24 * t_00479
t_00481 = t_00478 + t_00480
t_00482 = 3 * M_{020000} * M_{140010} * t_00481
t_00483 = 2 * M_{020000} * M_{020000} * M_{024000}
t_00484 = 33/4 * M_{020000} * M_{020000} * M_{032100}
t_00485 = 7/4 * M_{020000} * M_{020000} * M_{040200}
t_00486 = 11/4 * M_{020000} * M_{020000} * M_{041010}
t_00487 = 1/4 * M_{020000} * M_{020000} * M_{050001}
t_00488 = 1/3 * t_00233
t_00489 = 3/4 * t_00249
t_00490 = 1/5 * t_00206
t_00491 = t_00177 + t_00181 + t_00182 + t_00183 + t_00184 + t_00192 + t_00198 + t_00202 + t_00203 + t_00204 + t_00205 + t_00404 + t_00411 + t_00416 + t_00428 + t_00437 + t_00438 + t_00439 + t_00440 + t_00441 + t_00442 + t_00451 + t_00458 + t_00466 + t_00476 + t_00482 + t_00483 + t_00484 + t_00485 + t_00486 + t_00487 + t_00488 + t_00489 + t_00490
t_00492 = M_{020000} * t_00491
t_00493 = t_00215 + t_00453
t_00494 = 1/5 * M_{040000} * t_00493
t_00495 = 1/3 * t_00011 * M_{121000}
t_00496 = 2/3 * M_{020000} * M_{022000}
t_00497 = 1/3 * M_{020000} * M_{030100}
t_00498 = t_00494 + t_00495 + t_00496 + t_00497
t_00499 = 1/2 * t_00000 * t_00498
t_00500 = 1/20 * M_{020000} * t_00035
t_00501 = 1/8 * M_{020000} * t_00000 * M_{040000}
t_00502 = 4/15 * t_00000 * t_00014
t_00503 = 1/20 * t_00035
t_00504 = 3/4 * t_00000 * t_00035
t_00505 = t_00499 + t_00500 + t_00501 + t_00502 + t_00503 + t_00504
t_00506 = M_{040000} * t_00505
t_00507 = t_00038 + t_00039
t_00508 = 1/20 * M_{020000} * t_00507
t_00509 = 1/20 * t_00507
t_00510 = 3/4 * t_00000 * t_00507
t_00511 = t_00508 + t_00509 + t_00510
t_00512 = M_{060000} * t_00511
t_00513 = t_00000 * t_00035
t_00514 = t_00080 + t_00086 + t_00087 + t_00088
t_00515 = t_00000 * t_00514
t_00516 = 1/4 * M_{020000} * t_00035
t_00517 = 1/3 * M_{020000} * t_00000 * M_{040000}
t_00518 = 3/4 * t_00000 * t_00014
t_00519 = 1/4 * t_00035
t_00520 = t_00513 + t_00515 + t_00516 + t_00517 + t_00518 + t_00519
t_00521 = 1/5 * t_00520
t_00522 = t_00048 * t_00498
t_00523 = 3 * M_{020000} * M_{022000}
t_00524 = 3/2 * M_{020000} * M_{030100}
t_00525 = 5/6 * M_{020000} * M_{040000}
t_00526 = 13/12 * t_00014
t_00527 = t_00012 + t_00013 + t_00025 + t_00030 + t_00086 + t_00087 + t_00523 + t_00524 + t_00525 + t_00526
t_00528 = 1/5 * M_{020000} * t_00527
t_00529 = 1/4 * M_{020000} * M_{040000} * t_00048
t_00530 = 8/15 * t_00014 * t_00048
t_00531 = 1/5 * t_00527
t_00532 = 2 * t_00004 * t_00035
t_00533 = 2 * t_00000 * t_00091
t_00534 = t_00532 + t_00533
t_00535 = 1/2 * t_00534
t_00536 = t_00513 + t_00515 + t_00516 + t_00517 + t_00518 + t_00519 + t_00521 + t_00522 + t_00528 + t_00529 + t_00530 + t_00531 + t_00535
t_00537 = M_{121000} * t_00536
t_00538 = t_00000 * t_00507
t_00539 = 1/4 * M_{020000} * t_00125
t_00540 = 1/4 * t_00125
t_00541 = t_00538 + t_00539 + t_00540
t_00542 = 1/5 * t_00541
t_00543 = t_00046 + t_00049 + t_00050
t_00544 = 1/4 * t_00543
t_00545 = 5/6 * t_00000 * t_00004
t_00546 = t_00038 + t_00039 + t_00096 + t_00097 + t_00544 + t_00545
t_00547 = 1/5 * M_{020000} * t_00546
t_00548 = 1/5 * t_00546
t_00549 = 2 * t_00004 * t_00507
t_00550 = 2 * t_00000 * t_00098
t_00551 = t_00549 + t_00550
t_00552 = 1/2 * t_00551
t_00553 = 2/3 * t_00004 * t_00044
t_00554 = 3/4 * t_00000 * t_00543
t_00555 = t_00538 + t_00539 + t_00540 + t_00542 + t_00547 + t_00548 + t_00552 + t_00553 + t_00554
t_00556 = M_{141000} * t_00555
t_00557 = 1/4 * M_{020000} * t_00132
t_00558 = 1/4 * t_00132
t_00559 = t_00049 + t_00050
t_00560 = 2 * t_00000 * t_00559
t_00561 = t_00373 + t_00560
t_00562 = 1/2 * t_00561
t_00563 = t_00557 + t_00558 + t_00562
t_00564 = 1/5 * t_00563
t_00565 = t_00049 + t_00050 + t_00102 + t_00103
t_00566 = 1/5 * M_{020000} * t_00565
t_00567 = 1/5 * t_00565
t_00568 = 2 * t_00004 * t_00559
t_00569 = t_00102 + t_00103
t_00570 = 2 * t_00000 * t_00569
t_00571 = t_00568 + t_00570
t_00572 = 1/2 * t_00571
t_00573 = t_00557 + t_00558 + t_00562 + t_00564 + t_00566 + t_00567 + t_00572
t_00574 = M_{222000} * t_00573
t_00575 = 1/2 * t_00000 * t_00000 * t_00004
t_00576 = 1/4 * M_{020000} * t_00135
t_00577 = 1/4 * t_00135
t_00578 = t_00575 + t_00576 + t_00577
t_00579 = 1/5 * t_00578
t_00580 = t_00046 + t_00104
t_00581 = 1/5 * M_{020000} * t_00580
t_00582 = 1/5 * t_00580
t_00583 = 1/2 * t_00000 * t_00004 * t_00004
t_00584 = t_00575 + t_00576 + t_00577 + t_00579 + t_00581 + t_00582 + t_00583
t_00585 = M_{230100} * t_00584
t_00586 = M_{002000} * t_00206
t_00587 = M_{010100} * t_00206
t_00588 = t_00586 + t_00587
t_00589 = 1/5 * M_{020000}
t_00590 = 1/5 + t_00056 + t_00589
t_00591 = t_00588 * t_00590
t_00592 = 1/2 * t_00294
t_00593 = 1/4 * M_{020000} * M_{040000}
t_00594 = 8/15 * t_00014
t_00595 = t_00494 + t_00495 + t_00496 + t_00497 + t_00592 + t_00593 + t_00594
t_00596 = t_00055 * t_00595
t_00597 = 3 * t_00014 * M_{022000}
t_00598 = t_00014 * M_{030100}
t_00599 = t_00597 + t_00598
t_00600 = 2/3 * t_00044
t_00601 = 1/4 * t_00058
t_00602 = 5/6 * t_00000
t_00603 = 1/12 + t_00215 + t_00601 + t_00602
t_00604 = 1/5 * M_{020000} * t_00603
t_00605 = 1/5 * t_00603
t_00606 = 2 * t_00000 * t_00216
t_00607 = t_00322 + t_00323 + t_00606
t_00608 = 1/2 * t_00607
t_00609 = 3/4 * t_00000 * t_00058
t_00610 = t_00600 + t_00604 + t_00605 + t_00608 + t_00609
t_00611 = t_00599 * t_00610
t_00612 = t_00014 * M_{022000}
t_00613 = t_00014 * M_{103000}
t_00614 = 2 * t_00014 * M_{111100}
t_00615 = t_00612 + t_00613 + t_00614
t_00616 = 1/4 * M_{020000} * t_00081
t_00617 = 1/4 * t_00081
t_00618 = 1 + M_{020000} + t_00001 + t_00341
t_00619 = 1/2 * t_00618
t_00620 = t_00616 + t_00617 + t_00619
t_00621 = 1/5 * t_00620
t_00622 = 7/12 * M_{020000}
t_00623 = 7/12 + t_00622
t_00624 = 1/5 * M_{020000} * t_00623
t_00625 = 1/5 * t_00623
t_00626 = 2 * t_00004 * t_00081
t_00627 = 2 * t_00000 * t_00405
t_00628 = t_00338 + t_00339 + t_00626 + t_00627
t_00629 = 1/2 * t_00628
t_00630 = t_00616 + t_00617 + t_00619 + t_00621 + t_00624 + t_00625 + t_00629
t_00631 = t_00615 * t_00630
t_00632 = t_00014 * M_{120010}
t_00633 = t_00598 + t_00614 + t_00632
t_00634 = 1/8 * M_{020000} * t_00022
t_00635 = 1/8 * t_00022
t_00636 = t_00319 + t_00634 + t_00635
t_00637 = 1/5 * t_00636
t_00638 = 1/5 * M_{020000} * t_00335
t_00639 = 1/5 * t_00335
t_00640 = t_00319 + t_00348 + t_00634 + t_00635 + t_00637 + t_00638 + t_00639
t_00641 = t_00633 * t_00640
t_00642 = M_{002000} * t_00233
t_00643 = 2 * t_00014 * t_00142
t_00644 = t_00642 + t_00643
t_00645 = 1/2 * t_00262 * t_00644
t_00646 = t_00014 * t_00142
t_00647 = M_{010100} * t_00233
t_00648 = t_00014 * t_00147
t_00649 = t_00646 + t_00647 + t_00648
t_00650 = 1/10 * M_{020000}
t_00651 = 1/10 + t_00064 + t_00650
t_00652 = t_00649 * t_00651
t_00653 = 1/2 * M_{002000} * t_00048 * t_00249
t_00654 = 1/6 * t_00357
t_00655 = 1/5 + t_00589 + t_00654
t_00656 = M_{010100} * t_00249 * t_00655
t_00657 = t_00011 * M_{121000}
t_00658 = 1/2 * M_{040000} * t_00085
t_00659 = 2/3 * M_{020000} * M_{040000}
t_00660 = 3/2 * t_00014
t_00661 = t_00031 + t_00032 + t_00657 + t_00658 + t_00659 + t_00660
t_00662 = 1/2 * M_{020000} * M_{002000} * M_{040000} * t_00661
t_00663 = 1/2 * t_00498
t_00664 = 1/8 * M_{020000} * M_{040000}
t_00665 = 4/15 * t_00014
t_00666 = M_{040000} * t_00024
t_00667 = 6 * M_{020000} * M_{022000}
t_00668 = 3 * M_{020000} * M_{030100}
t_00669 = 3/2 * M_{020000} * M_{040000}
t_00670 = 3 * M_{121000} * t_00029
t_00671 = 2 * M_{220000} * t_00011
t_00672 = 4 * M_{020000} * M_{121000}
t_00673 = t_00666 + t_00667 + t_00668 + t_00669 + t_00670 + t_00671 + t_00672
t_00674 = 1/6 * t_00673
t_00675 = t_00663 + t_00664 + t_00665 + t_00674
t_00676 = M_{020000} * M_{010100} * M_{040000} * t_00675
t_00677 = 1/2 * t_00004
t_00678 = 7/24 * t_00000
t_00679 = 1/6 + t_00061 + t_00305 + t_00677 + t_00678
t_00680 = 1/5 * M_{020000} * t_00679
t_00681 = 1/5 * t_00679
t_00682 = 1/2 * M_{020000} * t_00307
t_00683 = 1/2 * t_00307
t_00684 = 2 * t_00004 * t_00252
t_00685 = t_00324 + t_00682 + t_00683 + t_00684
t_00686 = 1/2 * t_00685
t_00687 = 1/3 * t_00304 * t_00304
t_00688 = 3/8 * t_00000 * t_00000
t_00689 = 3/4 * t_00302
t_00690 = t_00045 + t_00680 + t_00681 + t_00686 + t_00687 + t_00688 + t_00689
t_00691 = M_{020000} * M_{040000} * M_{022000} * t_00690
t_00692 = 1/4 * t_00000
t_00693 = 1/4 * t_00022
t_00694 = 1/4 * t_00065
t_00695 = t_00254 + t_00692 + t_00693 + t_00694
t_00696 = 1/5 * M_{020000} * t_00695
t_00697 = 1/5 * t_00695
t_00698 = t_00000 * t_00081
t_00699 = t_00022 * t_00252
t_00700 = t_00042 + t_00043 + t_00324 + t_00698 + t_00699
t_00701 = 1/6 * t_00700
t_00702 = 3/4 * t_00320
t_00703 = 3/4 * t_00000 * t_00065
t_00704 = t_00696 + t_00697 + t_00701 + t_00702 + t_00703
t_00705 = M_{020000} * M_{040000} * M_{030100} * t_00704
t_00706 = 1/2 * M_{020000} * t_00330
t_00707 = 1/2 * t_00330
t_00708 = t_00626 + t_00706 + t_00707
t_00709 = 1/2 * t_00708
t_00710 = t_00004 * t_00004
t_00711 = 2/3 * M_{020000} * t_00004
t_00712 = t_00710 + t_00214 + t_00711
t_00713 = 3/5 * t_00712
t_00714 = t_00709 + t_00713
t_00715 = M_{020000} * M_{040000} * M_{103000} * t_00714
t_00716 = 1/4 * M_{020000} * t_00149
t_00717 = 1/4 * t_00149
t_00718 = 1/3 * M_{020000} * t_00022
t_00719 = 1/3 * t_00022
t_00720 = t_00324 + t_00718 + t_00719
t_00721 = 1/2 * t_00720
t_00722 = 3/2 * M_{020000} * t_00000
t_00723 = 3/2 * t_00000
t_00724 = t_00129 + t_00299 + t_00346 + t_00722 + t_00723
t_00725 = 1/6 * t_00724
t_00726 = t_00716 + t_00717 + t_00721 + t_00725
t_00727 = 1/5 * t_00726
t_00728 = 1/2 * t_00262
t_00729 = 7/24 * M_{020000}
t_00730 = 7/24 + t_00043 + t_00728 + t_00729
t_00731 = 1/5 * M_{020000} * t_00730
t_00732 = 1/5 * t_00730
t_00733 = 1/2 * M_{020000} * t_00335
t_00734 = 1/2 * t_00335
t_00735 = 1/8 + t_00265
t_00736 = 2 * t_00000 * t_00735
t_00737 = t_00684 + t_00733 + t_00734 + t_00736
t_00738 = 1/2 * t_00737
t_00739 = M_{020000} * t_00048
t_00740 = t_00022 * t_00081
t_00741 = t_00000 * t_00262
t_00742 = 3/2 + t_00047 + t_00739 + t_00299 + t_00340 + t_00341 + t_00740 + t_00741
t_00743 = 1/6 * t_00742
t_00744 = t_00716 + t_00717 + t_00721 + t_00725 + t_00727 + t_00731 + t_00732 + t_00738 + t_00743
t_00745 = M_{020000} * M_{040000} * M_{111100} * t_00744
t_00746 = 1/24 * M_{020000} * t_00063
t_00747 = 1/24 * t_00063
t_00748 = t_00000 * t_00063
t_00749 = t_00129 + t_00317 + t_00748
t_00750 = 1/24 * t_00749
t_00751 = t_00746 + t_00747 + t_00750
t_00752 = 1/5 * t_00751
t_00753 = t_00064 + t_00264
t_00754 = 1/5 * M_{020000} * t_00753
t_00755 = 1/5 * t_00753
t_00756 = t_00000 * t_00048
t_00757 = t_00004 * t_00063
t_00758 = t_00129 + t_00299 + t_00346 + t_00756 + t_00757
t_00759 = 1/24 * t_00758
t_00760 = t_00746 + t_00747 + t_00750 + t_00752 + t_00754 + t_00755 + t_00759
t_00761 = M_{020000} * M_{040000} * M_{120010} * t_00760
t_00762 = 3 + t_00062 + t_00114
t_00763 = 1/6 * t_00762
t_00764 = t_00707 + t_00763
t_00765 = M_{020000} * M_{040000} * t_00142 * t_00764
t_00766 = 5 * t_00000
t_00767 = 7 * M_{020000}
t_00768 = 7 + t_00766 + t_00767
t_00769 = 1/24 * t_00768
t_00770 = 1/10 + t_00650 + t_00769
t_00771 = M_{020000} * M_{040000} * t_00147 * t_00770
t_00772 = 1/2 * M_{020000} * M_{020000} * t_00004 * M_{040000} * M_{040000} * M_{000200}
t_00773 = 1/24 * t_00022
t_00774 = 1/2 * t_00216
t_00775 = t_00773 + t_00774
t_00776 = 3 * M_{020000} * M_{020000} * M_{040000} * M_{040000} * M_{001010} * t_00775
t_00777 = 1/120 * M_{020000}
t_00778 = 5 * M_{020000}
t_00779 = 5 + t_00778
t_00780 = 1/120 * t_00779
t_00781 = 1/120 + t_00777 + t_00780
t_00782 = 3 * M_{020000} * M_{020000} * M_{040000} * M_{040000} * M_{010001} * t_00781
t_00783 = t_00067 * t_00498
t_00784 = t_00515 + t_00516 + t_00517 + t_00518 + t_00519
t_00785 = 1/5 * M_{020000} * t_00784
t_00786 = 1/4 * M_{020000} * M_{040000} * t_00067
t_00787 = 8/15 * t_00014 * t_00067
t_00788 = 1/5 * t_00784
t_00789 = 2 * t_00035 * t_00067
t_00790 = 2 * t_00000 * t_00784
t_00791 = t_00789 + t_00790
t_00792 = 1/2 * t_00791
t_00793 = t_00783 + t_00785 + t_00786 + t_00787 + t_00788 + t_00792
t_00794 = 3 * M_{022000} * t_00793
t_00795 = 1/2 * t_00000 * t_00000 * t_00035
t_00796 = 1/2 * t_00000 * t_00000 * t_00498
t_00797 = 1/5 * M_{020000} * t_00000 * t_00035
t_00798 = 1/8 * M_{020000} * t_00000 * t_00000 * M_{040000}
t_00799 = 4/15 * t_00000 * t_00000 * t_00014
t_00800 = 1/5 * t_00000 * t_00035
t_00801 = t_00795 + t_00796 + t_00797 + t_00798 + t_00799 + t_00800
t_00802 = 3 * M_{030100} * t_00801
t_00803 = 1/2 * t_00000 * t_00067
t_00804 = 1/4 * t_00071
t_00805 = 1/3 * t_00000 * t_00044
t_00806 = t_00539 + t_00540 + t_00803 + t_00804 + t_00805
t_00807 = 1/5 * M_{020000} * t_00806
t_00808 = 1/5 * t_00806
t_00809 = 2 * t_00067 * t_00507
t_00810 = t_00539 + t_00540
t_00811 = 2 * t_00000 * t_00810
t_00812 = t_00809 + t_00811
t_00813 = 1/2 * t_00812
t_00814 = 1/3 * t_00044 * t_00044
t_00815 = 3/4 * t_00000 * t_00071
t_00816 = t_00807 + t_00808 + t_00813 + t_00814 + t_00815
t_00817 = 3 * M_{042000} * t_00816
t_00818 = 1/4 * t_00000 * t_00000 * t_00000
t_00819 = 1/4 * t_00076
t_00820 = t_00538 + t_00818 + t_00819
t_00821 = 1/5 * M_{020000} * t_00820
t_00822 = 1/5 * t_00820
t_00823 = 1/2 * t_00000 * t_00000 * t_00507
t_00824 = 3/4 * t_00000 * t_00076
t_00825 = t_00821 + t_00822 + t_00823 + t_00824
t_00826 = 3 * M_{050100} * t_00825
t_00827 = 1/4 * M_{020000} * t_00154
t_00828 = 1/4 * t_00154
t_00829 = t_00067 * t_00067
t_00830 = 2 * t_00000 * t_00154
t_00831 = t_00829 + t_00830
t_00832 = 1/2 * t_00831
t_00833 = t_00827 + t_00828 + t_00832
t_00834 = 1/5 * t_00833
t_00835 = t_00069 + t_00070 + t_00557 + t_00558
t_00836 = 1/5 * M_{020000} * t_00835
t_00837 = 1/5 * t_00835
t_00838 = 2 * t_00004 * t_00154
t_00839 = 2 * t_00067 * t_00559
t_00840 = t_00557 + t_00558
t_00841 = 2 * t_00000 * t_00840
t_00842 = t_00838 + t_00839 + t_00841
t_00843 = 1/2 * t_00842
t_00844 = t_00827 + t_00828 + t_00832 + t_00834 + t_00836 + t_00837 + t_00843
t_00845 = 3 * M_{123000} * t_00844
t_00846 = 1/2 * t_00000 * t_00000 * t_00067
t_00847 = 1/4 * M_{020000} * t_00157
t_00848 = 1/4 * t_00157
t_00849 = t_00073 + t_00074
t_00850 = t_00000 * t_00849
t_00851 = t_00846 + t_00847 + t_00848 + t_00850
t_00852 = 1/5 * t_00851
t_00853 = t_00068 + t_00073 + t_00074 + t_00562 + t_00576 + t_00577
t_00854 = 1/5 * M_{020000} * t_00853
t_00855 = 1/5 * t_00853
t_00856 = 2 * t_00004 * t_00849
t_00857 = t_00576 + t_00577
t_00858 = 2 * t_00000 * t_00857
t_00859 = t_00856 + t_00858
t_00860 = 1/2 * t_00859
t_00861 = t_00000 * t_00561
t_00862 = 4 * t_00000 * t_00004 * t_00067
t_00863 = t_00000 * t_00000 * t_00559
t_00864 = t_00861 + t_00862 + t_00863
t_00865 = 1/6 * t_00864
t_00866 = t_00846 + t_00847 + t_00848 + t_00850 + t_00852 + t_00854 + t_00855 + t_00860 + t_00865
t_00867 = 3 * M_{131100} * t_00866
t_00868 = 1/6 * t_00000 * t_00000 * t_00000 * t_00004
t_00869 = 1/24 * M_{020000} * t_00000 * t_00000 * t_00000
t_00870 = 1/24 * t_00000 * t_00000 * t_00000
t_00871 = 1/24 * t_00000 * t_00000 * t_00000 * t_00000
t_00872 = t_00869 + t_00870 + t_00871
t_00873 = 1/5 * t_00872
t_00874 = t_00075 + t_00575
t_00875 = 1/5 * M_{020000} * t_00874
t_00876 = 1/5 * t_00874
t_00877 = t_00868 + t_00869 + t_00870 + t_00871 + t_00873 + t_00875 + t_00876
t_00878 = 3 * M_{140010} * t_00877
t_00879 = t_00014 * M_{004000}
t_00880 = 3 * t_00014 * M_{012100}
t_00881 = t_00879 + t_00880
t_00882 = t_00616 + t_00617
t_00883 = 1/5 * M_{020000} * t_00882
t_00884 = 1/5 * t_00882
t_00885 = 2 * t_00067 * t_00081
t_00886 = 2 * t_00000 * t_00882
t_00887 = t_00374 + t_00375 + t_00885 + t_00886
t_00888 = 1/2 * t_00887
t_00889 = t_00883 + t_00884 + t_00888
t_00890 = 3 * t_00881 * t_00889
t_00891 = 2 * t_00014 * M_{012100}
t_00892 = t_00014 * M_{020200}
t_00893 = t_00014 * M_{021010}
t_00894 = t_00891 + t_00892 + t_00893
t_00895 = t_00619 + t_00634 + t_00635
t_00896 = 1/5 * M_{020000} * t_00895
t_00897 = 1/5 * t_00895
t_00898 = t_00634 + t_00635
t_00899 = 2 * t_00000 * t_00898
t_00900 = t_00381 + t_00382 + t_00899
t_00901 = 1/2 * t_00900
t_00902 = t_00000 * t_00000 * t_00081
t_00903 = t_00000 * t_00618
t_00904 = t_00390 + t_00391 + t_00902 + t_00903
t_00905 = 1/6 * t_00904
t_00906 = t_00896 + t_00897 + t_00901 + t_00905
t_00907 = 3 * t_00894 * t_00906
t_00908 = 3 * t_00014 * M_{021010}
t_00909 = t_00014 * M_{030001}
t_00910 = t_00908 + t_00909
t_00911 = 1/24 * t_00399
t_00912 = 1/30 * M_{020000} * t_00318
t_00913 = 1/30 * t_00318
t_00914 = t_00911 + t_00912 + t_00913
t_00915 = 3 * t_00910 * t_00914
t_00916 = 2 * t_00004 * t_00365
t_00917 = 1/2 * M_{020000} * t_00365
t_00918 = 1/2 * t_00365
t_00919 = t_00916 + t_00917 + t_00918
t_00920 = 3/2 * M_{020000} * M_{040000} * M_{004000} * t_00919
t_00921 = 1/2 * t_00712
t_00922 = t_00716 + t_00717 + t_00921
t_00923 = 1/5 * M_{020000} * t_00922
t_00924 = 1/5 * t_00922
t_00925 = 1/2 * M_{020000} * t_00370
t_00926 = 1/2 * t_00370
t_00927 = 2 * t_00067 * t_00252
t_00928 = 2 * t_00004 * t_00383
t_00929 = t_00716 + t_00717
t_00930 = 2 * t_00000 * t_00929
t_00931 = t_00925 + t_00926 + t_00927 + t_00928 + t_00930
t_00932 = 1/2 * t_00931
t_00933 = M_{020000} * t_00067
t_00934 = t_00022 * t_00365
t_00935 = t_00000 * t_00712
t_00936 = t_00004 * t_00300
t_00937 = t_00042 + t_00043 + t_00068 + t_00933 + t_00373 + t_00376 + t_00934 + t_00935 + t_00936
t_00938 = 1/6 * t_00937
t_00939 = t_00923 + t_00924 + t_00932 + t_00938
t_00940 = 3 * M_{020000} * M_{040000} * M_{012100} * t_00939
t_00941 = 1/10 * M_{020000} * t_00720
t_00942 = 1/10 * t_00720
t_00943 = t_00000 * t_00720
t_00944 = t_00000 * t_00000 * t_00252
t_00945 = t_00022 * t_00383
t_00946 = 1/2 * M_{020000} * t_00000 * t_00000
t_00947 = t_00037 + t_00384 + t_00943 + t_00944 + t_00945 + t_00946
t_00948 = 1/6 * t_00947
t_00949 = t_00941 + t_00942 + t_00948
t_00950 = 3 * M_{020000} * M_{040000} * M_{020200} * t_00949
t_00951 = t_00725 + t_00746 + t_00747
t_00952 = 1/5 * M_{020000} * t_00951
t_00953 = 1/5 * t_00951
t_00954 = 1/12 * M_{020000} * t_00318
t_00955 = 1/12 * t_00318
t_00956 = t_00746 + t_00747
t_00957 = 2 * t_00000 * t_00956
t_00958 = t_00954 + t_00955 + t_00957
t_00959 = 1/2 * t_00958
t_00960 = t_00063 * t_00067
t_00961 = t_00004 * t_00318
t_00962 = t_00000 * t_00724
t_00963 = t_00389 + t_00390 + t_00391 + t_00392 + t_00960 + t_00961 + t_00962
t_00964 = 1/24 * t_00963
t_00965 = t_00952 + t_00953 + t_00959 + t_00964
t_00966 = 3 * M_{020000} * M_{040000} * M_{021010} * t_00965
t_00967 = 1/120 * M_{020000} * t_00749
t_00968 = 1/120 * t_00749
t_00969 = t_00000 * t_00749
t_00970 = t_00397 + t_00398 + t_00969
t_00971 = 1/120 * t_00970
t_00972 = t_00967 + t_00968 + t_00971
t_00973 = 3 * M_{020000} * M_{040000} * M_{030001} * t_00972
t_00974 = t_00827 + t_00828
t_00975 = 1/5 * M_{020000} * t_00974
t_00976 = 1/5 * t_00974
t_00977 = 2 * t_00067 * t_00154
t_00978 = 2 * t_00000 * t_00974
t_00979 = t_00977 + t_00978
t_00980 = 1/2 * t_00979
t_00981 = t_00975 + t_00976 + t_00980
t_00982 = 15 * M_{024000} * t_00981
t_00983 = t_00832 + t_00847 + t_00848
t_00984 = 1/5 * M_{020000} * t_00983
t_00985 = 1/5 * t_00983
t_00986 = 2 * t_00067 * t_00849
t_00987 = t_00847 + t_00848
t_00988 = 2 * t_00000 * t_00987
t_00989 = t_00986 + t_00988
t_00990 = 1/2 * t_00989
t_00991 = t_00000 * t_00000 * t_00154
t_00992 = t_00000 * t_00831
t_00993 = 2 * t_00000 * t_00067 * t_00067
t_00994 = t_00991 + t_00992 + t_00993
t_00995 = 1/6 * t_00994
t_00996 = t_00984 + t_00985 + t_00990 + t_00995
t_00997 = 15 * M_{032100} * t_00996
t_00998 = 1/2 * t_00000 * t_00000 * t_00849
t_00999 = 1/5 * M_{020000} * t_00000 * t_00849
t_01000 = 1/5 * t_00000 * t_00849
t_01001 = t_00998 + t_00999 + t_01000
t_01002 = 15 * M_{040200} * t_01001
t_01003 = 1/6 * t_00000 * t_00000 * t_00000 * t_00067
t_01004 = t_00846 + t_00869 + t_00870
t_01005 = 1/5 * M_{020000} * t_01004
t_01006 = 1/5 * t_01004
t_01007 = t_00869 + t_00870
t_01008 = t_00000 * t_01007
t_01009 = t_01003 + t_01005 + t_01006 + t_01008
t_01010 = 15 * M_{041010} * t_01009
t_01011 = 1/120 * M_{020000} * t_00000 * t_00000 * t_00000 * t_00000
t_01012 = 1/120 * t_00000 * t_00000 * t_00000 * t_00000
t_01013 = 1/120 * t_00000 * t_00000 * t_00000 * t_00000 * t_00000
t_01014 = t_01011 + t_01012 + t_01013
t_01015 = 15 * M_{050001} * t_01014
t_01016 = t_00094 + t_00101 + t_00108 + t_00210 + t_00219 + t_00228 + t_00237 + t_00243 + t_00250 + t_00251 + t_00253 + t_00260 + t_00263 + t_00269 + t_00270 + t_00271 + t_00272 + t_00273 + t_00274 + t_00492 + t_00506 + t_00512 + t_00537 + t_00556 + t_00574 + t_00585 + t_00591 + t_00596 + t_00611 + t_00631 + t_00641 + t_00645 + t_00652 + t_00653 + t_00656 + t_00662 + t_00676 + t_00691 + t_00705 + t_00715 + t_00745 + t_00761 + t_00765 + t_00771 + t_00772 + t_00776 + t_00782 + t_00794 + t_00802 + t_00817 + t_00826 + t_00845 + t_00867 + t_00878 + t_00890 + t_00907 + t_00915 + t_00920 + t_00940 + t_00950 + t_00966 + t_00973 + t_00982 + t_00997 + t_01002 + t_01010 + t_01015
t_01017 = 120 * t_01016
A = t_00002
B = t_00079
C = t_01017
```
<!-- END EMBEDDED UNIT ARTIFACT -->

## Appendix B. Complete layer-separated arbitrary-variance arithmetic DAG

Here `Q0` is the first forward Gram,
`X_nu` is evaluated at `N(0,Q0)`, `Q1=X_200000`, and `Y_nu` is evaluated at
`N(0,Q1)`.  Thus `Q2=Y_200000` remains explicit.

<!-- BEGIN EMBEDDED LAYER-SEPARATED ARTIFACT -->
```text
# GENERATED FILE -- do not edit by hand.
# Generator: compiler/generate_artifacts.py
# Grammar: dependency-first deterministic arithmetic DAG.
# Each t_N is defined before use.  There are no random/tangent/response nodes.
# Moment alphabet: X_nu=E_{N(0,Q0)}[...] and Y_nu=E_{N(0,Q1)}[...]
# Exponent order is (phi,phi',phi'',phi''',phi^(4),phi^(5)).
t_00000 = X_{020000} * Q0
t_00001 = X_{200000} + t_00000
t_00002 = Y_{020000} * t_00001
t_00003 = Y_{200000} + t_00002
t_00004 = X_{200000} * 1/2
t_00005 = X_{020000} * 1/2 * Q0
t_00006 = t_00004 + t_00005
t_00007 = 1/3 * t_00006
t_00008 = t_00004 + t_00005 + t_00007
t_00009 = Y_{220000} * t_00008
t_00010 = Y_{020000} * 2
t_00011 = Y_{002000} * t_00001
t_00012 = Y_{010100} * t_00001
t_00013 = Y_{101000} + t_00010 + t_00011 + t_00012
t_00014 = 1/2 * X_{220000} * Q0 * t_00013
t_00015 = Y_{020000} * X_{121000} * Q0 * Q0
t_00016 = t_00014 + t_00015
t_00017 = Y_{020000} * t_00016
t_00018 = Y_{101000} * t_00016
t_00019 = t_00017 + t_00018
t_00020 = 4/3 * t_00019
t_00021 = Y_{020000} * Y_{020000} * X_{040000} * 1/2 * Q0 * Q0
t_00022 = Y_{020000} * X_{040000} * Y_{101000} * 2/3 * Q0 * Q0
t_00023 = Y_{020000} * 1/2
t_00024 = Y_{002000} * t_00006
t_00025 = X_{200000} * 2
t_00026 = X_{020000} * 2 * Q0
t_00027 = t_00025 + t_00026
t_00028 = 1/2 * Y_{010100} * t_00027
t_00029 = Y_{101000} + t_00023 + t_00024 + t_00028
t_00030 = Q0 * t_00029
t_00031 = Y_{020000} * 1/2 * Q0
t_00032 = t_00030 + t_00031
t_00033 = X_{040000} * 1/3 * Q0 * t_00032
t_00034 = X_{121000} * Q0 * Q0 * t_00013
t_00035 = Y_{020000} * 2 * X_{022000} * Q0 * Q0 * Q0
t_00036 = Y_{020000} * X_{030100} * Q0 * Q0 * Q0
t_00037 = Y_{020000} * X_{040000} * 1/2 * Q0 * Q0
t_00038 = 1/3 * t_00016
t_00039 = t_00014 + t_00015 + t_00033 + t_00034 + t_00035 + t_00036 + t_00037 + t_00038
t_00040 = Y_{020000} * t_00039
t_00041 = 1/2 * t_00001 * t_00001
t_00042 = X_{020000} * 1/6 * Q0 * t_00001
t_00043 = X_{200000} * 1/6 * t_00001
t_00044 = t_00041 + t_00042 + t_00043
t_00045 = Y_{040000} * t_00044
t_00046 = X_{020000} * 1/2 * Q0 * t_00001
t_00047 = X_{200000} * 1/2 * t_00001
t_00048 = t_00046 + t_00047 + t_00041
t_00049 = 1/3 * t_00048
t_00050 = t_00001 * t_00006
t_00051 = X_{200000} * 3/2
t_00052 = X_{020000} * 3/2 * Q0
t_00053 = t_00051 + t_00052
t_00054 = X_{020000} * 1/3 * Q0 * t_00053
t_00055 = X_{200000} * 1/3 * t_00053
t_00056 = t_00046 + t_00047 + t_00041 + t_00049 + t_00050 + t_00054 + t_00055
t_00057 = Y_{121000} * t_00056
t_00058 = Y_{002000} * t_00016
t_00059 = Y_{010100} * t_00016
t_00060 = t_00058 + t_00059
t_00061 = X_{200000} * 1/3
t_00062 = 1/2 * t_00027
t_00063 = X_{020000} * 1/3 * Q0
t_00064 = t_00061 + t_00062 + t_00063
t_00065 = t_00060 * t_00064
t_00066 = Y_{020000} * X_{040000} * 1/2 * Y_{002000} * Q0 * Q0 * t_00001
t_00067 = X_{200000} * 1/6
t_00068 = X_{020000} * 1/6 * Q0
t_00069 = X_{200000} * 3
t_00070 = X_{020000} * 3 * Q0
t_00071 = t_00069 + t_00070
t_00072 = 1/6 * t_00071
t_00073 = t_00067 + t_00068 + t_00072
t_00074 = Y_{020000} * X_{040000} * Y_{010100} * Q0 * Q0 * t_00073
t_00075 = t_00046 + t_00047
t_00076 = t_00001 * t_00075
t_00077 = X_{020000} * 1/3 * Q0 * t_00075
t_00078 = X_{200000} * 1/3 * t_00075
t_00079 = t_00076 + t_00077 + t_00078
t_00080 = Y_{022000} * 3 * t_00079
t_00081 = X_{020000} * 1/6 * Q0 * t_00001 * t_00001
t_00082 = X_{200000} * 1/6 * t_00001 * t_00001
t_00083 = 1/6 * t_00001 * t_00001 * t_00001
t_00084 = t_00081 + t_00082 + t_00083
t_00085 = 3 * Y_{030100} * t_00084
t_00086 = t_00009 + t_00020 + t_00021 + t_00022 + t_00040 + t_00045 + t_00057 + t_00065 + t_00066 + t_00074 + t_00080 + t_00085
t_00087 = 6 * t_00086
t_00088 = Y_{020000} * X_{022000} * Q0 * Q0 * Q0
t_00089 = Y_{020000} * 1/3
t_00090 = t_00061 + t_00063
t_00091 = Y_{002000} * t_00090
t_00092 = Y_{101000} + t_00089 + t_00028 + t_00091
t_00093 = 1/2 * Q0 * t_00092
t_00094 = Y_{020000} * 1/6 * Q0
t_00095 = t_00093 + t_00094
t_00096 = X_{040000} * 1/4 * Q0 * t_00095
t_00097 = 1/2 * X_{121000} * Q0 * Q0 * t_00013
t_00098 = Y_{020000} * 1/2 * X_{030100} * Q0 * Q0 * Q0
t_00099 = Y_{020000} * X_{040000} * 1/3 * Q0 * Q0
t_00100 = 3/4 * t_00016
t_00101 = t_00088 + t_00096 + t_00097 + t_00098 + t_00099 + t_00100
t_00102 = 1/5 * t_00101
t_00103 = t_00088 + t_00096 + t_00097 + t_00098 + t_00099 + t_00100 + t_00102
t_00104 = Y_{220000} * t_00103
t_00105 = 1/3 * t_00006 * t_00006
t_00106 = X_{020000} * 1/12 * Q0 * t_00006
t_00107 = X_{200000} * 1/12 * t_00006
t_00108 = t_00106 + t_00107
t_00109 = 1/5 * t_00108
t_00110 = t_00105 + t_00106 + t_00107 + t_00109
t_00111 = Y_{240000} * t_00110
t_00112 = X_{020000} * 1/4 * Q0 * t_00006
t_00113 = X_{200000} * 1/4 * t_00006
t_00114 = 1/2 * t_00006 * t_00006
t_00115 = t_00112 + t_00113 + t_00114
t_00116 = 1/5 * t_00115
t_00117 = t_00112 + t_00113 + t_00114 + t_00116
t_00118 = Y_{321000} * t_00117
t_00119 = 1/2 * Y_{040000} * t_00001
t_00120 = Y_{121000} * t_00053
t_00121 = Y_{022000} * 3 * t_00075
t_00122 = 3/2 * Y_{030100} * t_00001 * t_00001
t_00123 = 1/3 * Y_{040000} * t_00006
t_00124 = 2 * t_00006
t_00125 = t_00004 + t_00005 + t_00124
t_00126 = Y_{121000} * t_00125
t_00127 = Y_{202000} * t_00006
t_00128 = Y_{210100} * t_00006
t_00129 = 5/3 * t_00060
t_00130 = Y_{100010} * t_00016
t_00131 = Y_{020000} * X_{040000} * Y_{002000} * 2/3 * Q0 * Q0
t_00132 = Y_{020000} * X_{040000} * 1/2 * Y_{100010} * Q0 * Q0
t_00133 = Y_{002000} * t_00039
t_00134 = Y_{010100} * t_00039
t_00135 = t_00041 + t_00049 + t_00042 + t_00043
t_00136 = 3 * t_00135
t_00137 = t_00046 + t_00047 + t_00054 + t_00055 + t_00136
t_00138 = Y_{022000} * t_00137
t_00139 = t_00001 * t_00001
t_00140 = t_00139 + t_00049 + t_00050 + t_00042 + t_00043
t_00141 = Y_{030100} * t_00140
t_00142 = t_00046 + t_00047 + t_00054 + t_00055
t_00143 = Y_{103000} * t_00142
t_00144 = 2 * t_00142
t_00145 = t_00041 + t_00050
t_00146 = 2 * t_00145
t_00147 = t_00144 + t_00146
t_00148 = Y_{111100} * t_00147
t_00149 = Y_{120010} * t_00145
t_00150 = Y_{000200} * t_00016
t_00151 = Y_{001010} * t_00016
t_00152 = t_00150 + t_00151
t_00153 = 2 * t_00090
t_00154 = t_00062 + t_00153
t_00155 = t_00152 * t_00154
t_00156 = Y_{010001} * t_00016
t_00157 = t_00151 + t_00156
t_00158 = 1/2 * t_00027 * t_00157
t_00159 = 1/2 * t_00001
t_00160 = t_00067 + t_00159 + t_00068
t_00161 = Y_{020000} * X_{040000} * Y_{000200} * Q0 * Q0 * t_00160
t_00162 = t_00067 + t_00159 + t_00068 + t_00072
t_00163 = Y_{020000} * X_{040000} * Y_{001010} * Q0 * Q0 * t_00162
t_00164 = Y_{020000} * X_{040000} * 1/6 * Y_{010001} * Q0 * Q0 * t_00071
t_00165 = t_00077 + t_00078
t_00166 = 3 * Y_{004000} * t_00165
t_00167 = 3 * t_00165
t_00168 = t_00076 + t_00081 + t_00082
t_00169 = 2 * t_00168
t_00170 = t_00167 + t_00169
t_00171 = 3 * Y_{012100} * t_00170
t_00172 = 3 * Y_{020200} * t_00168
t_00173 = 1/2 * t_00001 * t_00001 * t_00001
t_00174 = t_00076 + t_00173 + t_00081 + t_00082
t_00175 = 3 * Y_{021010} * t_00174
t_00176 = 1/2 * Y_{030001} * t_00001 * t_00001 * t_00001
t_00177 = Y_{010100} * 2 * t_00016
t_00178 = Y_{020000} * X_{040000} * Y_{010100} * 5/3 * Q0 * Q0
t_00179 = Y_{121000} * t_00027
t_00180 = Y_{020000} * X_{040000} * Y_{002000} * Q0 * Q0
t_00181 = Y_{022000} * 3 * t_00001 * t_00001
t_00182 = Y_{220000} + t_00179 + t_00180 + t_00181
t_00183 = 1/2 * t_00182
t_00184 = Y_{020000} * X_{040000} * 1/2 * Y_{010100} * Q0 * Q0
t_00185 = t_00119 + t_00120 + t_00058 + t_00059 + t_00184 + t_00121 + t_00122
t_00186 = 1/3 * t_00185
t_00187 = t_00119 + t_00120 + t_00058 + t_00121 + t_00122 + t_00123 + t_00126 + t_00127 + t_00128 + t_00129 + t_00130 + t_00131 + t_00132 + t_00133 + t_00134 + t_00138 + t_00141 + t_00143 + t_00148 + t_00149 + t_00155 + t_00158 + t_00161 + t_00163 + t_00164 + t_00166 + t_00171 + t_00172 + t_00175 + t_00176 + t_00177 + t_00178 + t_00183 + t_00186
t_00188 = X_{220000} * 1/4 * Q0 * t_00187
t_00189 = 1/2 * Q0 * t_00013 * t_00092
t_00190 = Y_{020000} * 1/6 * Q0 * t_00013
t_00191 = t_00189 + t_00190
t_00192 = 1/4 * X_{240000} * Q0 * t_00191
t_00193 = 1/4 * X_{321000} * Q0 * Q0 * t_00013 * t_00013
t_00194 = X_{121000} * 1/4 * Q0 * Q0 * t_00182
t_00195 = X_{121000} * 2/3 * Q0 * Q0 * t_00185
t_00196 = 1/3 * Q0 * Q0 * t_00032
t_00197 = Q0 * Q0 * t_00092
t_00198 = Y_{020000} * 1/3 * Q0 * Q0
t_00199 = 4/3 * Q0 * t_00032
t_00200 = t_00197 + t_00198 + t_00199
t_00201 = 1/4 * Q0 * t_00200
t_00202 = t_00196 + t_00201
t_00203 = Y_{020000} * X_{141000} * t_00202
t_00204 = Y_{020000} * X_{222000} * Q0 * Q0 * Q0 * t_00013
t_00205 = Y_{020000} * 1/2 * X_{230100} * Q0 * Q0 * Q0 * t_00013
t_00206 = Y_{020000} * Y_{020000} * X_{123000} * Q0 * Q0 * Q0 * Q0
t_00207 = Y_{020000} * Y_{020000} * X_{131100} * 7/4 * Q0 * Q0 * Q0 * Q0
t_00208 = Y_{020000} * Y_{020000} * 1/4 * X_{140010} * Q0 * Q0 * Q0 * Q0
t_00209 = t_00188 + t_00192 + t_00193 + t_00194 + t_00195 + t_00203 + t_00204 + t_00205 + t_00206 + t_00207 + t_00208
t_00210 = Y_{020000} * t_00209
t_00211 = Y_{101000} * t_00209
t_00212 = t_00210 + t_00211
t_00213 = 6/5 * t_00212
t_00214 = Y_{040000} * t_00016
t_00215 = Y_{121000} * 3 * t_00016
t_00216 = t_00214 + t_00215
t_00217 = X_{200000} * 1/12
t_00218 = 2/3 * t_00006
t_00219 = X_{020000} * 1/12 * Q0
t_00220 = t_00217 + t_00219
t_00221 = 1/5 * t_00220
t_00222 = t_00217 + t_00218 + t_00219 + t_00221
t_00223 = t_00216 * t_00222
t_00224 = 2 * Y_{121000} * t_00016
t_00225 = Y_{202000} * t_00016
t_00226 = Y_{210100} * t_00016
t_00227 = t_00224 + t_00225 + t_00226
t_00228 = X_{200000} * 1/4
t_00229 = X_{020000} * 1/4 * Q0
t_00230 = t_00228 + t_00159 + t_00229
t_00231 = 1/5 * t_00230
t_00232 = t_00228 + t_00159 + t_00229 + t_00231
t_00233 = t_00227 * t_00232
t_00234 = 1/4 * X_{240000} * Q0 * Q0 * t_00013 * t_00013
t_00235 = X_{040000} * 1/4 * Q0 * Q0 * t_00182
t_00236 = Y_{020000} * X_{141000} * Q0 * Q0 * Q0 * t_00013
t_00237 = Y_{020000} * Y_{020000} * 3 * X_{042000} * Q0 * Q0 * Q0 * Q0
t_00238 = t_00234 + t_00235 + t_00236 + t_00237
t_00239 = Y_{020000} * t_00238
t_00240 = 2 * t_00016 * t_00060
t_00241 = t_00239 + t_00240
t_00242 = 1/3 * t_00241
t_00243 = t_00016 * t_00060
t_00244 = Y_{101000} * t_00238
t_00245 = t_00059 + t_00130
t_00246 = t_00016 * t_00245
t_00247 = t_00243 + t_00244 + t_00246
t_00248 = 3/5 * t_00247
t_00249 = X_{040000} * 1/3 * Q0 * Q0 * t_00185
t_00250 = Y_{020000} * 1/3 * X_{060000} * Q0 * Q0 * t_00032
t_00251 = Y_{020000} * Y_{020000} * 2 * X_{042000} * Q0 * Q0 * Q0 * Q0
t_00252 = Y_{020000} * Y_{020000} * X_{050100} * Q0 * Q0 * Q0 * Q0
t_00253 = t_00236 + t_00249 + t_00250 + t_00251 + t_00252
t_00254 = Y_{020000} * 3/4 * t_00253
t_00255 = Y_{101000} * 6/5 * t_00253
t_00256 = t_00067 + t_00068
t_00257 = Y_{020000} * X_{040000} * Y_{040000} * 3/4 * Q0 * Q0 * t_00256
t_00258 = 1/2 * t_00090
t_00259 = t_00067 + t_00068 + t_00258
t_00260 = 1/5 * t_00259
t_00261 = t_00061 + t_00159 + t_00063
t_00262 = 3/4 * t_00261
t_00263 = t_00067 + t_00007 + t_00068 + t_00258 + t_00260 + t_00262
t_00264 = Y_{020000} * X_{040000} * Y_{121000} * Q0 * Q0 * t_00263
t_00265 = X_{200000} * 2/3
t_00266 = X_{020000} * 2/3 * Q0
t_00267 = t_00265 + t_00266
t_00268 = Y_{020000} * X_{040000} * Y_{202000} * 3/5 * Q0 * Q0 * t_00267
t_00269 = X_{200000} * 1/8
t_00270 = 1/6 * t_00053
t_00271 = X_{020000} * 1/8 * Q0
t_00272 = t_00269 + t_00270 + t_00271
t_00273 = 1/5 * t_00272
t_00274 = t_00269 + t_00270 + t_00271 + t_00273
t_00275 = Y_{020000} * X_{040000} * Y_{210100} * Q0 * Q0 * t_00274
t_00276 = Y_{020000} * X_{040000} * 13/12 * Q0 * Q0 * t_00060
t_00277 = Y_{020000} * X_{040000} * 3/5 * Q0 * Q0 * t_00245
t_00278 = Y_{020000} * Y_{020000} * X_{040000} * X_{040000} * Y_{002000} * 1/4 * Q0 * Q0 * Q0 * Q0
t_00279 = Y_{020000} * Y_{020000} * X_{040000} * X_{040000} * Y_{010100} * 3/8 * Q0 * Q0 * Q0 * Q0
t_00280 = Y_{020000} * Y_{020000} * X_{040000} * X_{040000} * Y_{100010} * 3/20 * Q0 * Q0 * Q0 * Q0
t_00281 = 1/4 * Y_{040000} * t_00256
t_00282 = 1/4 * t_00261
t_00283 = 5/6 * t_00006
t_00284 = t_00067 + t_00068 + t_00282 + t_00283
t_00285 = Y_{121000} * t_00284
t_00286 = Y_{202000} * t_00090
t_00287 = 1/2 * Y_{210100} * t_00001
t_00288 = 13/12 * t_00060
t_00289 = Y_{020000} * X_{040000} * 1/2 * Y_{002000} * Q0 * Q0
t_00290 = Y_{020000} * X_{040000} * Y_{010100} * 7/8 * Q0 * Q0
t_00291 = Y_{002000} * t_00101
t_00292 = Y_{020000} * X_{040000} * Q0 * Q0
t_00293 = X_{220000} * Q0 * t_00013
t_00294 = Y_{020000} * 2 * X_{121000} * Q0 * Q0
t_00295 = X_{040000} * 2/3 * Q0 * t_00032
t_00296 = 2 * X_{121000} * Q0 * Q0 * t_00013
t_00297 = Y_{020000} * 4 * X_{022000} * Q0 * Q0 * Q0
t_00298 = Y_{020000} * 2 * X_{030100} * Q0 * Q0 * Q0
t_00299 = 2/3 * t_00016
t_00300 = t_00292 + t_00293 + t_00294 + t_00295 + t_00296 + t_00297 + t_00298 + t_00299
t_00301 = 1/2 * Y_{010100} * t_00300
t_00302 = 1/2 * t_00075
t_00303 = 1/2 * t_00001 * t_00006
t_00304 = X_{020000} * 1/3 * Q0 * t_00006
t_00305 = X_{200000} * 1/3 * t_00006
t_00306 = X_{020000} * Q0 * t_00001
t_00307 = X_{200000} * t_00001
t_00308 = 2 * t_00001 * t_00006
t_00309 = t_00306 + t_00307 + t_00308
t_00310 = 1/2 * t_00309
t_00311 = t_00304 + t_00305 + t_00310
t_00312 = 1/4 * t_00311
t_00313 = X_{200000} * 7/6
t_00314 = t_00004 + t_00005 + t_00062
t_00315 = 1/3 * t_00314
t_00316 = X_{020000} * 7/6 * Q0
t_00317 = t_00313 + t_00315 + t_00316
t_00318 = X_{020000} * 1/4 * Q0 * t_00317
t_00319 = X_{200000} * 1/4 * t_00317
t_00320 = 1/3 * t_00001 * t_00314
t_00321 = t_00049 + t_00302 + t_00303 + t_00312 + t_00318 + t_00319 + t_00320
t_00322 = Y_{022000} * t_00321
t_00323 = 1/4 * t_00001 * t_00001
t_00324 = 1/4 * t_00001 * t_00027
t_00325 = X_{020000} * 1/6 * Q0 * t_00027
t_00326 = X_{200000} * 1/6 * t_00027
t_00327 = t_00001 * t_00027
t_00328 = t_00139 + t_00327
t_00329 = 1/6 * t_00328
t_00330 = t_00325 + t_00326 + t_00329
t_00331 = 1/4 * t_00330
t_00332 = X_{020000} * 1/3 * Q0 * t_00001
t_00333 = X_{200000} * 1/3 * t_00001
t_00334 = 2 * t_00001 * t_00256
t_00335 = t_00332 + t_00333 + t_00334
t_00336 = 1/2 * t_00335
t_00337 = t_00323 + t_00324 + t_00331 + t_00336
t_00338 = Y_{030100} * t_00337
t_00339 = X_{200000} * 5/6
t_00340 = X_{020000} * 5/6 * Q0
t_00341 = t_00339 + t_00340
t_00342 = X_{020000} * 1/4 * Q0 * t_00341
t_00343 = X_{200000} * 1/4 * t_00341
t_00344 = t_00304 + t_00305 + t_00342 + t_00343
t_00345 = Y_{103000} * t_00344
t_00346 = t_00159 + t_00062
t_00347 = X_{020000} * 1/4 * Q0 * t_00346
t_00348 = X_{200000} * 1/4 * t_00346
t_00349 = X_{020000} * 2/3 * Q0 * t_00053
t_00350 = X_{200000} * 2/3 * t_00053
t_00351 = 2 * t_00006 * t_00006
t_00352 = 2 * t_00001 * t_00090
t_00353 = t_00349 + t_00350 + t_00351 + t_00352
t_00354 = 1/2 * t_00353
t_00355 = t_00325 + t_00326 + t_00310 + t_00347 + t_00348 + t_00354
t_00356 = Y_{111100} * t_00355
t_00357 = t_00027 * t_00006
t_00358 = t_00139 + t_00357 + t_00308
t_00359 = 1/6 * t_00358
t_00360 = t_00329 + t_00359
t_00361 = Y_{120010} * t_00360
t_00362 = X_{200000} * 5/3
t_00363 = X_{020000} * 5/3 * Q0
t_00364 = t_00362 + t_00363
t_00365 = 1/2 * t_00364
t_00366 = t_00228 + t_00229 + t_00365
t_00367 = t_00152 * t_00366
t_00368 = X_{200000} * 4
t_00369 = 2 * t_00001
t_00370 = X_{020000} * 4 * Q0
t_00371 = t_00368 + t_00369 + t_00370
t_00372 = 1/6 * t_00157 * t_00371
t_00373 = Y_{020000} * X_{040000} * Y_{000200} * 3/2 * Q0 * Q0 * t_00090
t_00374 = X_{200000} * 1/24
t_00375 = X_{020000} * 1/24 * Q0
t_00376 = t_00374 + t_00270 + t_00375
t_00377 = Y_{020000} * X_{040000} * Y_{001010} * 3 * Q0 * Q0 * t_00376
t_00378 = t_00368 + t_00370
t_00379 = Y_{020000} * X_{040000} * Y_{010001} * 1/8 * Q0 * Q0 * t_00378
t_00380 = t_00304 + t_00305
t_00381 = X_{020000} * 1/4 * Q0 * t_00380
t_00382 = X_{200000} * 1/4 * t_00380
t_00383 = t_00381 + t_00382
t_00384 = 3 * Y_{004000} * t_00383
t_00385 = t_00325 + t_00326 + t_00310
t_00386 = X_{020000} * 1/4 * Q0 * t_00385
t_00387 = X_{200000} * 1/4 * t_00385
t_00388 = 2 * t_00006 * t_00075
t_00389 = X_{020000} * 2/3 * Q0 * t_00075
t_00390 = X_{200000} * 2/3 * t_00075
t_00391 = 2 * t_00001 * t_00380
t_00392 = t_00388 + t_00389 + t_00390 + t_00391
t_00393 = 1/2 * t_00392
t_00394 = t_00386 + t_00387 + t_00393
t_00395 = 3 * Y_{012100} * t_00394
t_00396 = X_{020000} * 1/3 * Q0 * t_00001 * t_00001
t_00397 = X_{200000} * 1/3 * t_00001 * t_00001
t_00398 = t_00325 + t_00326
t_00399 = 2 * t_00001 * t_00398
t_00400 = t_00396 + t_00397 + t_00399
t_00401 = 3/2 * Y_{020200} * t_00400
t_00402 = X_{020000} * 1/24 * Q0 * t_00328
t_00403 = X_{200000} * 1/24 * t_00328
t_00404 = t_00001 * t_00001 * t_00006
t_00405 = t_00027 * t_00075
t_00406 = 2 * t_00001 * t_00075
t_00407 = t_00001 * t_00309
t_00408 = t_00404 + t_00405 + t_00406 + t_00407
t_00409 = 1/6 * t_00408
t_00410 = t_00402 + t_00403 + t_00409
t_00411 = 3 * Y_{021010} * t_00410
t_00412 = t_00001 * t_00001 * t_00001
t_00413 = t_00001 * t_00328
t_00414 = t_00412 + t_00413
t_00415 = Y_{030001} * 1/8 * t_00414
t_00416 = t_00059 + t_00130 + t_00132 + t_00281 + t_00285 + t_00286 + t_00287 + t_00288 + t_00289 + t_00290 + t_00291 + t_00301 + t_00322 + t_00338 + t_00345 + t_00356 + t_00361 + t_00367 + t_00372 + t_00373 + t_00377 + t_00379 + t_00384 + t_00395 + t_00401 + t_00411 + t_00415
t_00417 = Q0 * t_00416
t_00418 = 1/3 * Q0 * t_00182
t_00419 = 3/4 * Q0 * t_00185
t_00420 = t_00417 + t_00418 + t_00419
t_00421 = X_{040000} * 1/5 * Q0 * t_00420
t_00422 = Y_{020000} * 1/4
t_00423 = t_00228 + t_00229
t_00424 = Y_{002000} * t_00423
t_00425 = Y_{101000} + t_00422 + t_00028 + t_00424
t_00426 = 1/3 * Q0 * t_00032 * t_00425
t_00427 = Y_{020000} * 1/12 * Q0 * t_00032
t_00428 = t_00426 + t_00427
t_00429 = X_{060000} * 1/5 * Q0 * t_00428
t_00430 = 1/2 * X_{121000} * Q0 * Q0 * t_00187
t_00431 = Q0 * Q0 * t_00013 * t_00425
t_00432 = Y_{020000} * 1/4 * Q0 * Q0 * t_00013
t_00433 = 5/6 * Q0 * t_00013 * t_00032
t_00434 = 5/4 * Q0 * t_00191
t_00435 = t_00431 + t_00432 + t_00433 + t_00434
t_00436 = 1/5 * Q0 * t_00435
t_00437 = 1/3 * Q0 * Q0 * t_00013 * t_00032
t_00438 = 1/2 * Q0 * Q0 * t_00191
t_00439 = t_00437 + t_00438
t_00440 = 1/2 * t_00439
t_00441 = t_00436 + t_00440
t_00442 = X_{141000} * t_00441
t_00443 = 1/2 * X_{222000} * Q0 * Q0 * Q0 * t_00013 * t_00013
t_00444 = 1/4 * X_{230100} * Q0 * Q0 * Q0 * t_00013 * t_00013
t_00445 = 1/2 * X_{022000} * Q0 * Q0 * Q0 * t_00182
t_00446 = 1/4 * X_{030100} * Q0 * Q0 * Q0 * t_00182
t_00447 = 4/3 * X_{022000} * Q0 * Q0 * Q0 * t_00185
t_00448 = 2/3 * X_{030100} * Q0 * Q0 * Q0 * t_00185
t_00449 = 2/3 * Q0 * Q0 * Q0 * t_00425
t_00450 = Y_{020000} * 1/6 * Q0 * Q0 * Q0
t_00451 = t_00197 + t_00198
t_00452 = Q0 * t_00451
t_00453 = 1/2 * Q0 * Q0 * t_00032
t_00454 = t_00201 + t_00449 + t_00450 + t_00452 + t_00453
t_00455 = 1/5 * Q0 * t_00454
t_00456 = 1/3 * Q0 * Q0 * Q0 * t_00032
t_00457 = 1/2 * Q0 * Q0 * t_00200
t_00458 = t_00456 + t_00457
t_00459 = 1/2 * t_00458
t_00460 = t_00455 + t_00459
t_00461 = Y_{020000} * 3 * X_{042000} * t_00460
t_00462 = 1/3 * Q0 * Q0 * Q0 * t_00425
t_00463 = Y_{020000} * 1/12 * Q0 * Q0 * Q0
t_00464 = 5/6 * Q0 * Q0 * t_00032
t_00465 = t_00462 + t_00463 + t_00464
t_00466 = 1/5 * Q0 * t_00465
t_00467 = 1/6 * Q0 * Q0 * Q0 * t_00032
t_00468 = t_00466 + t_00467
t_00469 = Y_{020000} * 3 * X_{050100} * t_00468
t_00470 = Y_{020000} * 2 * X_{123000} * Q0 * Q0 * Q0 * Q0 * t_00013
t_00471 = Y_{020000} * X_{131100} * 7/2 * Q0 * Q0 * Q0 * Q0 * t_00013
t_00472 = Y_{020000} * 1/2 * X_{140010} * Q0 * Q0 * Q0 * Q0 * t_00013
t_00473 = Y_{020000} * Y_{020000} * 2 * X_{024000} * Q0 * Q0 * Q0 * Q0 * Q0
t_00474 = Y_{020000} * Y_{020000} * 33/4 * X_{032100} * Q0 * Q0 * Q0 * Q0 * Q0
t_00475 = Y_{020000} * Y_{020000} * 7/4 * X_{040200} * Q0 * Q0 * Q0 * Q0 * Q0
t_00476 = Y_{020000} * Y_{020000} * 11/4 * X_{041010} * Q0 * Q0 * Q0 * Q0 * Q0
t_00477 = Y_{020000} * Y_{020000} * 1/4 * X_{050001} * Q0 * Q0 * Q0 * Q0 * Q0
t_00478 = 1/3 * t_00238
t_00479 = 3/4 * t_00253
t_00480 = 1/5 * t_00209
t_00481 = t_00188 + t_00192 + t_00193 + t_00194 + t_00195 + t_00203 + t_00204 + t_00205 + t_00206 + t_00207 + t_00208 + t_00421 + t_00429 + t_00430 + t_00442 + t_00443 + t_00444 + t_00445 + t_00446 + t_00447 + t_00448 + t_00461 + t_00469 + t_00470 + t_00471 + t_00472 + t_00473 + t_00474 + t_00475 + t_00476 + t_00477 + t_00478 + t_00479 + t_00480
t_00482 = Y_{020000} * t_00481
t_00483 = 1/3 * Q0 * t_00425
t_00484 = Y_{020000} * 1/12 * Q0
t_00485 = t_00483 + t_00484
t_00486 = X_{040000} * 1/5 * Q0 * t_00485
t_00487 = X_{121000} * 1/3 * Q0 * Q0 * t_00013
t_00488 = Y_{020000} * 2/3 * X_{022000} * Q0 * Q0 * Q0
t_00489 = Y_{020000} * 1/3 * X_{030100} * Q0 * Q0 * Q0
t_00490 = t_00486 + t_00487 + t_00488 + t_00489
t_00491 = 1/2 * t_00001 * t_00490
t_00492 = X_{020000} * 1/20 * Q0 * t_00039
t_00493 = Y_{020000} * X_{040000} * 1/8 * Q0 * Q0 * t_00001
t_00494 = 4/15 * t_00001 * t_00016
t_00495 = X_{200000} * 1/20 * t_00039
t_00496 = 3/4 * t_00001 * t_00039
t_00497 = t_00491 + t_00492 + t_00493 + t_00494 + t_00495 + t_00496
t_00498 = Y_{040000} * t_00497
t_00499 = t_00042 + t_00043
t_00500 = X_{020000} * 1/20 * Q0 * t_00499
t_00501 = X_{200000} * 1/20 * t_00499
t_00502 = 3/4 * t_00001 * t_00499
t_00503 = t_00500 + t_00501 + t_00502
t_00504 = Y_{060000} * t_00503
t_00505 = t_00001 * t_00039
t_00506 = t_00088 + t_00096 + t_00097 + t_00098
t_00507 = t_00001 * t_00506
t_00508 = X_{020000} * 1/4 * Q0 * t_00039
t_00509 = Y_{020000} * X_{040000} * 1/3 * Q0 * Q0 * t_00001
t_00510 = 3/4 * t_00001 * t_00016
t_00511 = X_{200000} * 1/4 * t_00039
t_00512 = t_00505 + t_00507 + t_00508 + t_00509 + t_00510 + t_00511
t_00513 = 1/5 * t_00512
t_00514 = t_00053 * t_00490
t_00515 = Y_{020000} * 3 * X_{022000} * Q0 * Q0 * Q0
t_00516 = X_{121000} * 3/2 * Q0 * Q0 * t_00013
t_00517 = Y_{020000} * 3/2 * X_{030100} * Q0 * Q0 * Q0
t_00518 = Y_{020000} * X_{040000} * 5/6 * Q0 * Q0
t_00519 = 13/12 * t_00016
t_00520 = t_00014 + t_00015 + t_00033 + t_00096 + t_00515 + t_00516 + t_00517 + t_00518 + t_00519
t_00521 = X_{020000} * 1/5 * Q0 * t_00520
t_00522 = Y_{020000} * X_{040000} * 1/4 * Q0 * Q0 * t_00053
t_00523 = 8/15 * t_00016 * t_00053
t_00524 = X_{200000} * 1/5 * t_00520
t_00525 = 2 * t_00006 * t_00039
t_00526 = 2 * t_00001 * t_00101
t_00527 = t_00525 + t_00526
t_00528 = 1/2 * t_00527
t_00529 = t_00505 + t_00507 + t_00508 + t_00509 + t_00510 + t_00511 + t_00513 + t_00514 + t_00521 + t_00522 + t_00523 + t_00524 + t_00528
t_00530 = Y_{121000} * t_00529
t_00531 = X_{020000} * 1/4 * Q0 * t_00135
t_00532 = X_{200000} * 1/4 * t_00135
t_00533 = t_00001 * t_00499
t_00534 = t_00531 + t_00532 + t_00533
t_00535 = 1/5 * t_00534
t_00536 = t_00050 + t_00054 + t_00055
t_00537 = 1/4 * t_00536
t_00538 = 5/6 * t_00001 * t_00006
t_00539 = t_00042 + t_00043 + t_00537 + t_00106 + t_00107 + t_00538
t_00540 = X_{020000} * 1/5 * Q0 * t_00539
t_00541 = X_{200000} * 1/5 * t_00539
t_00542 = 2 * t_00006 * t_00499
t_00543 = 2 * t_00001 * t_00108
t_00544 = t_00542 + t_00543
t_00545 = 1/2 * t_00544
t_00546 = 2/3 * t_00006 * t_00048
t_00547 = 3/4 * t_00001 * t_00536
t_00548 = t_00531 + t_00532 + t_00533 + t_00535 + t_00540 + t_00541 + t_00545 + t_00546 + t_00547
t_00549 = Y_{141000} * t_00548
t_00550 = X_{020000} * 1/4 * Q0 * t_00142
t_00551 = X_{200000} * 1/4 * t_00142
t_00552 = t_00054 + t_00055
t_00553 = 2 * t_00001 * t_00552
t_00554 = t_00388 + t_00553
t_00555 = 1/2 * t_00554
t_00556 = t_00550 + t_00551 + t_00555
t_00557 = 1/5 * t_00556
t_00558 = t_00054 + t_00055 + t_00112 + t_00113
t_00559 = X_{020000} * 1/5 * Q0 * t_00558
t_00560 = X_{200000} * 1/5 * t_00558
t_00561 = 2 * t_00006 * t_00552
t_00562 = t_00112 + t_00113
t_00563 = 2 * t_00001 * t_00562
t_00564 = t_00561 + t_00563
t_00565 = 1/2 * t_00564
t_00566 = t_00550 + t_00551 + t_00555 + t_00557 + t_00559 + t_00560 + t_00565
t_00567 = Y_{222000} * t_00566
t_00568 = 1/2 * t_00001 * t_00001 * t_00006
t_00569 = X_{020000} * 1/4 * Q0 * t_00145
t_00570 = X_{200000} * 1/4 * t_00145
t_00571 = t_00568 + t_00569 + t_00570
t_00572 = 1/5 * t_00571
t_00573 = t_00050 + t_00114
t_00574 = X_{020000} * 1/5 * Q0 * t_00573
t_00575 = X_{200000} * 1/5 * t_00573
t_00576 = 1/2 * t_00001 * t_00006 * t_00006
t_00577 = t_00568 + t_00569 + t_00570 + t_00572 + t_00574 + t_00575 + t_00576
t_00578 = Y_{230100} * t_00577
t_00579 = Y_{002000} * t_00209
t_00580 = Y_{010100} * t_00209
t_00581 = t_00579 + t_00580
t_00582 = X_{200000} * 1/5
t_00583 = X_{020000} * 1/5 * Q0
t_00584 = t_00582 + t_00062 + t_00583
t_00585 = t_00581 * t_00584
t_00586 = 1/2 * t_00300
t_00587 = Y_{020000} * X_{040000} * 1/4 * Q0 * Q0
t_00588 = 8/15 * t_00016
t_00589 = t_00586 + t_00486 + t_00487 + t_00488 + t_00489 + t_00587 + t_00588
t_00590 = t_00060 * t_00589
t_00591 = Y_{022000} * 3 * t_00016
t_00592 = Y_{030100} * t_00016
t_00593 = t_00591 + t_00592
t_00594 = 2/3 * t_00048
t_00595 = 1/4 * t_00064
t_00596 = 5/6 * t_00001
t_00597 = t_00217 + t_00595 + t_00219 + t_00596
t_00598 = X_{020000} * 1/5 * Q0 * t_00597
t_00599 = X_{200000} * 1/5 * t_00597
t_00600 = 2 * t_00001 * t_00220
t_00601 = t_00332 + t_00333 + t_00600
t_00602 = 1/2 * t_00601
t_00603 = 3/4 * t_00001 * t_00064
t_00604 = t_00594 + t_00598 + t_00599 + t_00602 + t_00603
t_00605 = t_00593 * t_00604
t_00606 = Y_{022000} * t_00016
t_00607 = Y_{103000} * t_00016
t_00608 = 2 * Y_{111100} * t_00016
t_00609 = t_00606 + t_00607 + t_00608
t_00610 = X_{020000} * 1/4 * Q0 * t_00090
t_00611 = X_{200000} * 1/4 * t_00090
t_00612 = t_00306 + t_00307 + t_00352
t_00613 = 1/2 * t_00612
t_00614 = t_00610 + t_00611 + t_00613
t_00615 = 1/5 * t_00614
t_00616 = X_{200000} * 7/12
t_00617 = X_{020000} * 7/12 * Q0
t_00618 = t_00616 + t_00617
t_00619 = X_{020000} * 1/5 * Q0 * t_00618
t_00620 = X_{200000} * 1/5 * t_00618
t_00621 = 2 * t_00006 * t_00090
t_00622 = 2 * t_00001 * t_00423
t_00623 = t_00349 + t_00350 + t_00621 + t_00622
t_00624 = 1/2 * t_00623
t_00625 = t_00610 + t_00611 + t_00613 + t_00615 + t_00619 + t_00620 + t_00624
t_00626 = t_00609 * t_00625
t_00627 = Y_{120010} * t_00016
t_00628 = t_00592 + t_00608 + t_00627
t_00629 = X_{020000} * 1/8 * Q0 * t_00027
t_00630 = X_{200000} * 1/8 * t_00027
t_00631 = t_00329 + t_00629 + t_00630
t_00632 = 1/5 * t_00631
t_00633 = X_{020000} * 1/5 * Q0 * t_00346
t_00634 = X_{200000} * 1/5 * t_00346
t_00635 = t_00329 + t_00629 + t_00630 + t_00359 + t_00632 + t_00633 + t_00634
t_00636 = t_00628 * t_00635
t_00637 = Y_{002000} * t_00238
t_00638 = 2 * t_00016 * t_00152
t_00639 = t_00637 + t_00638
t_00640 = 1/2 * t_00639 * t_00267
t_00641 = t_00016 * t_00152
t_00642 = Y_{010100} * t_00238
t_00643 = t_00016 * t_00157
t_00644 = t_00641 + t_00642 + t_00643
t_00645 = X_{200000} * 1/10
t_00646 = X_{020000} * 1/10 * Q0
t_00647 = t_00645 + t_00072 + t_00646
t_00648 = t_00644 * t_00647
t_00649 = 1/2 * Y_{002000} * t_00053 * t_00253
t_00650 = 1/6 * t_00371
t_00651 = t_00582 + t_00650 + t_00583
t_00652 = Y_{010100} * t_00253 * t_00651
t_00653 = X_{040000} * 1/2 * Q0 * t_00095
t_00654 = Y_{020000} * X_{040000} * 2/3 * Q0 * Q0
t_00655 = 3/2 * t_00016
t_00656 = t_00034 + t_00035 + t_00036 + t_00653 + t_00654 + t_00655
t_00657 = Y_{020000} * X_{040000} * 1/2 * Y_{002000} * Q0 * Q0 * t_00656
t_00658 = 1/2 * t_00490
t_00659 = Y_{020000} * X_{040000} * 1/8 * Q0 * Q0
t_00660 = 4/15 * t_00016
t_00661 = X_{040000} * Q0 * t_00032
t_00662 = Y_{020000} * 6 * X_{022000} * Q0 * Q0 * Q0
t_00663 = 3 * X_{121000} * Q0 * Q0 * t_00013
t_00664 = Y_{020000} * 3 * X_{030100} * Q0 * Q0 * Q0
t_00665 = Y_{020000} * X_{040000} * 3/2 * Q0 * Q0
t_00666 = X_{220000} * 3/2 * Q0 * t_00013
t_00667 = Y_{020000} * 3 * X_{121000} * Q0 * Q0
t_00668 = t_00016 + t_00661 + t_00662 + t_00663 + t_00664 + t_00665 + t_00666 + t_00667
t_00669 = 1/6 * t_00668
t_00670 = t_00658 + t_00659 + t_00660 + t_00669
t_00671 = Y_{020000} * X_{040000} * Y_{010100} * Q0 * Q0 * t_00670
t_00672 = 1/2 * t_00006
t_00673 = 7/24 * t_00001
t_00674 = t_00067 + t_00315 + t_00672 + t_00068 + t_00673
t_00675 = X_{020000} * 1/5 * Q0 * t_00674
t_00676 = X_{200000} * 1/5 * t_00674
t_00677 = X_{020000} * 1/2 * Q0 * t_00317
t_00678 = X_{200000} * 1/2 * t_00317
t_00679 = 2 * t_00006 * t_00256
t_00680 = t_00334 + t_00677 + t_00678 + t_00679
t_00681 = 1/2 * t_00680
t_00682 = 1/3 * t_00314 * t_00314
t_00683 = 3/8 * t_00001 * t_00001
t_00684 = 3/4 * t_00311
t_00685 = t_00049 + t_00675 + t_00676 + t_00681 + t_00682 + t_00683 + t_00684
t_00686 = Y_{020000} * X_{040000} * Y_{022000} * Q0 * Q0 * t_00685
t_00687 = 1/4 * t_00001
t_00688 = 1/4 * t_00027
t_00689 = 1/4 * t_00073
t_00690 = t_00687 + t_00688 + t_00689 + t_00258
t_00691 = X_{020000} * 1/5 * Q0 * t_00690
t_00692 = X_{200000} * 1/5 * t_00690
t_00693 = t_00001 * t_00090
t_00694 = t_00027 * t_00256
t_00695 = t_00046 + t_00047 + t_00693 + t_00334 + t_00694
t_00696 = 1/6 * t_00695
t_00697 = 3/4 * t_00330
t_00698 = 3/4 * t_00001 * t_00073
t_00699 = t_00691 + t_00692 + t_00696 + t_00697 + t_00698
t_00700 = Y_{020000} * X_{040000} * Y_{030100} * Q0 * Q0 * t_00699
t_00701 = X_{020000} * 1/2 * Q0 * t_00341
t_00702 = X_{200000} * 1/2 * t_00341
t_00703 = t_00621 + t_00701 + t_00702
t_00704 = 1/2 * t_00703
t_00705 = t_00006 * t_00006
t_00706 = X_{020000} * 2/3 * Q0 * t_00006
t_00707 = X_{200000} * 2/3 * t_00006
t_00708 = t_00705 + t_00706 + t_00707
t_00709 = 3/5 * t_00708
t_00710 = t_00704 + t_00709
t_00711 = Y_{020000} * X_{040000} * Y_{103000} * Q0 * Q0 * t_00710
t_00712 = X_{020000} * 1/4 * Q0 * t_00160
t_00713 = X_{200000} * 1/4 * t_00160
t_00714 = X_{020000} * 1/3 * Q0 * t_00027
t_00715 = X_{200000} * 1/3 * t_00027
t_00716 = t_00714 + t_00715 + t_00334
t_00717 = 1/2 * t_00716
t_00718 = X_{020000} * 3/2 * Q0 * t_00001
t_00719 = X_{200000} * 3/2 * t_00001
t_00720 = t_00139 + t_00357 + t_00308 + t_00718 + t_00719
t_00721 = 1/6 * t_00720
t_00722 = t_00712 + t_00713 + t_00717 + t_00721
t_00723 = 1/5 * t_00722
t_00724 = X_{200000} * 7/24
t_00725 = 1/2 * t_00267
t_00726 = X_{020000} * 7/24 * Q0
t_00727 = t_00724 + t_00159 + t_00725 + t_00726
t_00728 = X_{020000} * 1/5 * Q0 * t_00727
t_00729 = X_{200000} * 1/5 * t_00727
t_00730 = X_{020000} * 1/2 * Q0 * t_00346
t_00731 = X_{200000} * 1/2 * t_00346
t_00732 = t_00269 + t_00271
t_00733 = 2 * t_00001 * t_00732
t_00734 = t_00730 + t_00731 + t_00679 + t_00733
t_00735 = 1/2 * t_00734
t_00736 = X_{020000} * Q0 * t_00053
t_00737 = X_{200000} * t_00053
t_00738 = t_00027 * t_00090
t_00739 = t_00001 * t_00267
t_00740 = t_00736 + t_00737 + t_00308 + t_00738 + t_00351 + t_00352 + t_00739
t_00741 = 1/6 * t_00740
t_00742 = t_00712 + t_00713 + t_00717 + t_00721 + t_00723 + t_00728 + t_00729 + t_00735 + t_00741
t_00743 = Y_{020000} * X_{040000} * Y_{111100} * Q0 * Q0 * t_00742
t_00744 = X_{020000} * 1/24 * Q0 * t_00071
t_00745 = X_{200000} * 1/24 * t_00071
t_00746 = t_00001 * t_00071
t_00747 = t_00139 + t_00327 + t_00746
t_00748 = 1/24 * t_00747
t_00749 = t_00744 + t_00745 + t_00748
t_00750 = 1/5 * t_00749
t_00751 = t_00072 + t_00270
t_00752 = X_{020000} * 1/5 * Q0 * t_00751
t_00753 = X_{200000} * 1/5 * t_00751
t_00754 = t_00001 * t_00053
t_00755 = t_00006 * t_00071
t_00756 = t_00139 + t_00754 + t_00357 + t_00308 + t_00755
t_00757 = 1/24 * t_00756
t_00758 = t_00744 + t_00745 + t_00748 + t_00750 + t_00752 + t_00753 + t_00757
t_00759 = Y_{020000} * X_{040000} * Y_{120010} * Q0 * Q0 * t_00758
t_00760 = 1/2 * t_00341
t_00761 = t_00069 + t_00070 + t_00124
t_00762 = 1/6 * t_00761
t_00763 = t_00760 + t_00762
t_00764 = Y_{020000} * X_{040000} * Q0 * Q0 * t_00152 * t_00763
t_00765 = X_{200000} * 7
t_00766 = 5 * t_00001
t_00767 = X_{020000} * 7 * Q0
t_00768 = t_00765 + t_00766 + t_00767
t_00769 = 1/24 * t_00768
t_00770 = t_00645 + t_00646 + t_00769
t_00771 = Y_{020000} * X_{040000} * Q0 * Q0 * t_00157 * t_00770
t_00772 = Y_{020000} * Y_{020000} * X_{040000} * X_{040000} * 1/2 * Y_{000200} * Q0 * Q0 * Q0 * Q0 * t_00006
t_00773 = 1/24 * t_00027
t_00774 = 1/2 * t_00220
t_00775 = t_00773 + t_00774
t_00776 = Y_{020000} * Y_{020000} * X_{040000} * X_{040000} * Y_{001010} * 3 * Q0 * Q0 * Q0 * Q0 * t_00775
t_00777 = X_{200000} * 1/120
t_00778 = X_{020000} * 1/120 * Q0
t_00779 = X_{200000} * 5
t_00780 = X_{020000} * 5 * Q0
t_00781 = t_00779 + t_00780
t_00782 = 1/120 * t_00781
t_00783 = t_00777 + t_00778 + t_00782
t_00784 = Y_{020000} * Y_{020000} * X_{040000} * X_{040000} * 3 * Y_{010001} * Q0 * Q0 * Q0 * Q0 * t_00783
t_00785 = t_00075 * t_00490
t_00786 = t_00507 + t_00508 + t_00509 + t_00510 + t_00511
t_00787 = X_{020000} * 1/5 * Q0 * t_00786
t_00788 = Y_{020000} * X_{040000} * 1/4 * Q0 * Q0 * t_00075
t_00789 = 8/15 * t_00016 * t_00075
t_00790 = X_{200000} * 1/5 * t_00786
t_00791 = 2 * t_00075 * t_00039
t_00792 = 2 * t_00001 * t_00786
t_00793 = t_00791 + t_00792
t_00794 = 1/2 * t_00793
t_00795 = t_00785 + t_00787 + t_00788 + t_00789 + t_00790 + t_00794
t_00796 = Y_{022000} * 3 * t_00795
t_00797 = 1/2 * t_00001 * t_00001 * t_00039
t_00798 = 1/2 * t_00001 * t_00001 * t_00490
t_00799 = X_{020000} * 1/5 * Q0 * t_00001 * t_00039
t_00800 = Y_{020000} * X_{040000} * 1/8 * Q0 * Q0 * t_00001 * t_00001
t_00801 = 4/15 * t_00001 * t_00001 * t_00016
t_00802 = X_{200000} * 1/5 * t_00001 * t_00039
t_00803 = t_00797 + t_00798 + t_00799 + t_00800 + t_00801 + t_00802
t_00804 = 3 * Y_{030100} * t_00803
t_00805 = 1/2 * t_00001 * t_00075
t_00806 = 1/4 * t_00079
t_00807 = 1/3 * t_00001 * t_00048
t_00808 = t_00805 + t_00806 + t_00531 + t_00532 + t_00807
t_00809 = X_{020000} * 1/5 * Q0 * t_00808
t_00810 = X_{200000} * 1/5 * t_00808
t_00811 = 2 * t_00075 * t_00499
t_00812 = t_00531 + t_00532
t_00813 = 2 * t_00001 * t_00812
t_00814 = t_00811 + t_00813
t_00815 = 1/2 * t_00814
t_00816 = 1/3 * t_00048 * t_00048
t_00817 = 3/4 * t_00001 * t_00079
t_00818 = t_00809 + t_00810 + t_00815 + t_00816 + t_00817
t_00819 = 3 * Y_{042000} * t_00818
t_00820 = 1/4 * t_00001 * t_00001 * t_00001
t_00821 = 1/4 * t_00084
t_00822 = t_00820 + t_00821 + t_00533
t_00823 = X_{020000} * 1/5 * Q0 * t_00822
t_00824 = X_{200000} * 1/5 * t_00822
t_00825 = 1/2 * t_00001 * t_00001 * t_00499
t_00826 = 3/4 * t_00001 * t_00084
t_00827 = t_00823 + t_00824 + t_00825 + t_00826
t_00828 = 3 * Y_{050100} * t_00827
t_00829 = X_{020000} * 1/4 * Q0 * t_00165
t_00830 = X_{200000} * 1/4 * t_00165
t_00831 = t_00075 * t_00075
t_00832 = 2 * t_00001 * t_00165
t_00833 = t_00831 + t_00832
t_00834 = 1/2 * t_00833
t_00835 = t_00829 + t_00830 + t_00834
t_00836 = 1/5 * t_00835
t_00837 = t_00077 + t_00078 + t_00550 + t_00551
t_00838 = X_{020000} * 1/5 * Q0 * t_00837
t_00839 = X_{200000} * 1/5 * t_00837
t_00840 = 2 * t_00006 * t_00165
t_00841 = 2 * t_00075 * t_00552
t_00842 = t_00550 + t_00551
t_00843 = 2 * t_00001 * t_00842
t_00844 = t_00840 + t_00841 + t_00843
t_00845 = 1/2 * t_00844
t_00846 = t_00829 + t_00830 + t_00834 + t_00836 + t_00838 + t_00839 + t_00845
t_00847 = 3 * Y_{123000} * t_00846
t_00848 = 1/2 * t_00001 * t_00001 * t_00075
t_00849 = X_{020000} * 1/4 * Q0 * t_00168
t_00850 = X_{200000} * 1/4 * t_00168
t_00851 = t_00081 + t_00082
t_00852 = t_00001 * t_00851
t_00853 = t_00848 + t_00849 + t_00850 + t_00852
t_00854 = 1/5 * t_00853
t_00855 = t_00076 + t_00081 + t_00082 + t_00569 + t_00570 + t_00555
t_00856 = X_{020000} * 1/5 * Q0 * t_00855
t_00857 = X_{200000} * 1/5 * t_00855
t_00858 = 2 * t_00006 * t_00851
t_00859 = t_00569 + t_00570
t_00860 = 2 * t_00001 * t_00859
t_00861 = t_00858 + t_00860
t_00862 = 1/2 * t_00861
t_00863 = t_00001 * t_00554
t_00864 = 4 * t_00001 * t_00006 * t_00075
t_00865 = t_00001 * t_00001 * t_00552
t_00866 = t_00863 + t_00864 + t_00865
t_00867 = 1/6 * t_00866
t_00868 = t_00848 + t_00849 + t_00850 + t_00852 + t_00854 + t_00856 + t_00857 + t_00862 + t_00867
t_00869 = 3 * Y_{131100} * t_00868
t_00870 = 1/6 * t_00001 * t_00001 * t_00001 * t_00006
t_00871 = X_{020000} * 1/24 * Q0 * t_00001 * t_00001 * t_00001
t_00872 = X_{200000} * 1/24 * t_00001 * t_00001 * t_00001
t_00873 = 1/24 * t_00001 * t_00001 * t_00001 * t_00001
t_00874 = t_00871 + t_00872 + t_00873
t_00875 = 1/5 * t_00874
t_00876 = t_00568 + t_00083
t_00877 = X_{020000} * 1/5 * Q0 * t_00876
t_00878 = X_{200000} * 1/5 * t_00876
t_00879 = t_00870 + t_00871 + t_00872 + t_00873 + t_00875 + t_00877 + t_00878
t_00880 = 3 * Y_{140010} * t_00879
t_00881 = Y_{004000} * t_00016
t_00882 = 3 * Y_{012100} * t_00016
t_00883 = t_00881 + t_00882
t_00884 = t_00610 + t_00611
t_00885 = X_{020000} * 1/5 * Q0 * t_00884
t_00886 = X_{200000} * 1/5 * t_00884
t_00887 = 2 * t_00075 * t_00090
t_00888 = 2 * t_00001 * t_00884
t_00889 = t_00389 + t_00390 + t_00887 + t_00888
t_00890 = 1/2 * t_00889
t_00891 = t_00885 + t_00886 + t_00890
t_00892 = 3 * t_00883 * t_00891
t_00893 = 2 * Y_{012100} * t_00016
t_00894 = Y_{020200} * t_00016
t_00895 = Y_{021010} * t_00016
t_00896 = t_00893 + t_00894 + t_00895
t_00897 = t_00629 + t_00630 + t_00613
t_00898 = X_{020000} * 1/5 * Q0 * t_00897
t_00899 = X_{200000} * 1/5 * t_00897
t_00900 = t_00629 + t_00630
t_00901 = 2 * t_00001 * t_00900
t_00902 = t_00396 + t_00397 + t_00901
t_00903 = 1/2 * t_00902
t_00904 = t_00001 * t_00001 * t_00090
t_00905 = t_00001 * t_00612
t_00906 = t_00405 + t_00406 + t_00904 + t_00905
t_00907 = 1/6 * t_00906
t_00908 = t_00898 + t_00899 + t_00903 + t_00907
t_00909 = 3 * t_00896 * t_00908
t_00910 = 3 * Y_{021010} * t_00016
t_00911 = Y_{030001} * t_00016
t_00912 = t_00910 + t_00911
t_00913 = 1/24 * t_00414
t_00914 = X_{020000} * 1/30 * Q0 * t_00328
t_00915 = X_{200000} * 1/30 * t_00328
t_00916 = t_00913 + t_00914 + t_00915
t_00917 = 3 * t_00912 * t_00916
t_00918 = 2 * t_00006 * t_00380
t_00919 = X_{020000} * 1/2 * Q0 * t_00380
t_00920 = X_{200000} * 1/2 * t_00380
t_00921 = t_00918 + t_00919 + t_00920
t_00922 = Y_{020000} * X_{040000} * 3/2 * Y_{004000} * Q0 * Q0 * t_00921
t_00923 = 1/2 * t_00708
t_00924 = t_00712 + t_00713 + t_00923
t_00925 = X_{020000} * 1/5 * Q0 * t_00924
t_00926 = X_{200000} * 1/5 * t_00924
t_00927 = X_{020000} * 1/2 * Q0 * t_00385
t_00928 = X_{200000} * 1/2 * t_00385
t_00929 = 2 * t_00075 * t_00256
t_00930 = 2 * t_00006 * t_00398
t_00931 = t_00712 + t_00713
t_00932 = 2 * t_00001 * t_00931
t_00933 = t_00927 + t_00928 + t_00929 + t_00930 + t_00932
t_00934 = 1/2 * t_00933
t_00935 = X_{020000} * Q0 * t_00075
t_00936 = X_{200000} * t_00075
t_00937 = t_00027 * t_00380
t_00938 = t_00001 * t_00708
t_00939 = t_00006 * t_00309
t_00940 = t_00076 + t_00388 + t_00935 + t_00936 + t_00937 + t_00391 + t_00938 + t_00939
t_00941 = 1/6 * t_00940
t_00942 = t_00925 + t_00926 + t_00934 + t_00941
t_00943 = Y_{020000} * X_{040000} * 3 * Y_{012100} * Q0 * Q0 * t_00942
t_00944 = X_{020000} * 1/10 * Q0 * t_00716
t_00945 = X_{200000} * 1/10 * t_00716
t_00946 = X_{200000} * 1/2 * t_00001 * t_00001
t_00947 = t_00001 * t_00716
t_00948 = t_00001 * t_00001 * t_00256
t_00949 = t_00027 * t_00398
t_00950 = X_{020000} * 1/2 * Q0 * t_00001 * t_00001
t_00951 = t_00946 + t_00399 + t_00947 + t_00948 + t_00949 + t_00950
t_00952 = 1/6 * t_00951
t_00953 = t_00944 + t_00945 + t_00952
t_00954 = Y_{020000} * X_{040000} * 3 * Y_{020200} * Q0 * Q0 * t_00953
t_00955 = t_00744 + t_00745 + t_00721
t_00956 = X_{020000} * 1/5 * Q0 * t_00955
t_00957 = X_{200000} * 1/5 * t_00955
t_00958 = X_{020000} * 1/12 * Q0 * t_00328
t_00959 = X_{200000} * 1/12 * t_00328
t_00960 = t_00744 + t_00745
t_00961 = 2 * t_00001 * t_00960
t_00962 = t_00958 + t_00959 + t_00961
t_00963 = 1/2 * t_00962
t_00964 = t_00075 * t_00071
t_00965 = t_00006 * t_00328
t_00966 = t_00001 * t_00720
t_00967 = t_00404 + t_00405 + t_00406 + t_00964 + t_00965 + t_00407 + t_00966
t_00968 = 1/24 * t_00967
t_00969 = t_00956 + t_00957 + t_00963 + t_00968
t_00970 = Y_{020000} * X_{040000} * 3 * Y_{021010} * Q0 * Q0 * t_00969
t_00971 = X_{020000} * 1/120 * Q0 * t_00747
t_00972 = X_{200000} * 1/120 * t_00747
t_00973 = t_00001 * t_00747
t_00974 = t_00412 + t_00413 + t_00973
t_00975 = 1/120 * t_00974
t_00976 = t_00971 + t_00972 + t_00975
t_00977 = Y_{020000} * X_{040000} * 3 * Y_{030001} * Q0 * Q0 * t_00976
t_00978 = t_00829 + t_00830
t_00979 = X_{020000} * 1/5 * Q0 * t_00978
t_00980 = X_{200000} * 1/5 * t_00978
t_00981 = 2 * t_00075 * t_00165
t_00982 = 2 * t_00001 * t_00978
t_00983 = t_00981 + t_00982
t_00984 = 1/2 * t_00983
t_00985 = t_00979 + t_00980 + t_00984
t_00986 = Y_{024000} * 15 * t_00985
t_00987 = t_00849 + t_00850 + t_00834
t_00988 = X_{020000} * 1/5 * Q0 * t_00987
t_00989 = X_{200000} * 1/5 * t_00987
t_00990 = 2 * t_00075 * t_00851
t_00991 = t_00849 + t_00850
t_00992 = 2 * t_00001 * t_00991
t_00993 = t_00990 + t_00992
t_00994 = 1/2 * t_00993
t_00995 = t_00001 * t_00001 * t_00165
t_00996 = t_00001 * t_00833
t_00997 = 2 * t_00001 * t_00075 * t_00075
t_00998 = t_00995 + t_00996 + t_00997
t_00999 = 1/6 * t_00998
t_01000 = t_00988 + t_00989 + t_00994 + t_00999
t_01001 = 15 * Y_{032100} * t_01000
t_01002 = 1/2 * t_00001 * t_00001 * t_00851
t_01003 = X_{020000} * 1/5 * Q0 * t_00001 * t_00851
t_01004 = X_{200000} * 1/5 * t_00001 * t_00851
t_01005 = t_01002 + t_01003 + t_01004
t_01006 = 15 * Y_{040200} * t_01005
t_01007 = 1/6 * t_00001 * t_00001 * t_00001 * t_00075
t_01008 = t_00848 + t_00871 + t_00872
t_01009 = X_{020000} * 1/5 * Q0 * t_01008
t_01010 = X_{200000} * 1/5 * t_01008
t_01011 = t_00871 + t_00872
t_01012 = t_00001 * t_01011
t_01013 = t_01007 + t_01009 + t_01010 + t_01012
t_01014 = 15 * Y_{041010} * t_01013
t_01015 = X_{020000} * 1/120 * Q0 * t_00001 * t_00001 * t_00001 * t_00001
t_01016 = X_{200000} * 1/120 * t_00001 * t_00001 * t_00001 * t_00001
t_01017 = 1/120 * t_00001 * t_00001 * t_00001 * t_00001 * t_00001
t_01018 = t_01015 + t_01016 + t_01017
t_01019 = 15 * Y_{050001} * t_01018
t_01020 = t_00104 + t_00111 + t_00118 + t_00213 + t_00223 + t_00233 + t_00242 + t_00248 + t_00254 + t_00255 + t_00257 + t_00264 + t_00268 + t_00275 + t_00276 + t_00277 + t_00278 + t_00279 + t_00280 + t_00482 + t_00498 + t_00504 + t_00530 + t_00549 + t_00567 + t_00578 + t_00585 + t_00590 + t_00605 + t_00626 + t_00636 + t_00640 + t_00648 + t_00649 + t_00652 + t_00657 + t_00671 + t_00686 + t_00700 + t_00711 + t_00743 + t_00759 + t_00764 + t_00771 + t_00772 + t_00776 + t_00784 + t_00796 + t_00804 + t_00819 + t_00828 + t_00847 + t_00869 + t_00880 + t_00892 + t_00909 + t_00917 + t_00922 + t_00943 + t_00954 + t_00970 + t_00977 + t_00986 + t_01001 + t_01006 + t_01014 + t_01019
t_01021 = 120 * t_01020
A = t_00003
B = t_00087
C = t_01021
```
<!-- END EMBEDDED LAYER-SEPARATED ARTIFACT -->
