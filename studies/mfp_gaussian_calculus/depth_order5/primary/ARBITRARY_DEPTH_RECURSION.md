# Route S: finite-state arbitrary-depth order-five peel

This note was written after the `H=3,4` primary coefficient maps were frozen.
It describes the mathematical recursion implemented by
`depth_population_jet.py`; it is not a substitute for the emitted terminal
formulas.

## 1. Ordinary Taylor coefficients

Fix hidden depth `H` and write

\[
u^\ell(t)=\sum_{k=0}^5u^\ell_k t^k,\qquad
h^\ell(t)=\phi(u^\ell(t))=\sum_{k=0}^5h^\ell_k t^k,
\]
\[
p^\ell(t)=\phi'(u^\ell(t))=\sum_{k=0}^4p^\ell_k t^k,
\qquad a(t)=\sum_{k=0}^5a_k t^k.
\]

For a scalar series `x`, define the exact composition coefficient

\[
\Phi^{(r)}_k[x]
=\sum_{j=0}^k {\phi^{(r+j)}(x_0)\over j!}
 \sum_{\substack{i_1+\cdots+i_j=k\\i_q\geq1}}
 x_{i_1}\cdots x_{i_j}.
\tag{1}
\]

The `j=0` inner sum is one only at `k=0`.  Thus

\[
h^\ell_k=\Phi^{(0)}_k[u^\ell],\qquad
p^\ell_k=\Phi^{(1)}_k[u^\ell].
\tag{2}
\]

All equations below are identities of scalar coordinate-law polynomials.
Angle brackets denote the fully peeled deterministic expectation.

## 2. One response registry per initialized matrix

For each matrix between layers `ell-1` and `ell`, `2<=ell<=H`, introduce
only during the derivation two centered Gaussian innovation families

\[
(F^\ell_0,\ldots,F^\ell_5),\qquad
(R^\ell_0,\ldots,R^\ell_4).
\]

Their same-orientation covariances are

\[
\mathcal H^\ell_{ks}
=\langle h^{\ell-1}_k h^{\ell-1}_s\rangle,
\qquad 0\leq k,s\leq5,
\tag{3}
\]

\[
\mathcal B^\ell_{ks}
=\langle b^\ell_k b^\ell_s\rangle,
\qquad 0\leq k,s\leq4.
\tag{4}
\]

Here `b^ell` is the back-propagated preactivation source.  The two response
tables are

\[
\alpha^\ell_{ks}
=\left\langle {\partial h^{\ell-1}_k\over\partial R^\ell_s}\right\rangle,
\quad 1\leq k\leq5,\quad0\leq s<k,
\tag{5}
\]

\[
\beta^\ell_{ks}
=\left\langle {\partial b^\ell_k\over\partial F^\ell_s}\right\rangle,
\quad0\leq k\leq4,\quad0\leq s\leq k.
\tag{6}
\]

The derivative with respect to `F^ell_0` is the ordinary Stein derivative of
the base activation at layer `ell`.  Equations (5)--(6), rather than an
independence assumption, retain every transpose response.

## 3. Chronological forward equations

At the first layer,

\[
u^1_0=G_1\sim N(0,Q^0),\qquad
u^1_{k+1}={Q^0\over k+1}b^1_k.
\tag{7}
\]

For `ell>=2`, `u^ell_0=F^ell_0` and, for `1<=k<=5`,

\[
\begin{split}
u^\ell_k={}&F^\ell_k
+\sum_{s=0}^{k-1}\alpha^\ell_{ks}b^\ell_s\\
&+\sum_{d=1}^{k}{1\over d}
  \sum_{p=0}^{d-1}b^\ell_p
  \left\langle
    h^{\ell-1}_{d-1-p}h^{\ell-1}_{k-d}
  \right\rangle .
\end{split}
\tag{8}
\]

The three terms in (8) are respectively the fresh initialized-matrix use,
all earlier transpose responses, and the exact integrated rank-one parameter
updates.  After (8), equation (2) produces `h^ell_k,p^ell_k`.

The output/readout equations are

\[
a_0=A_0\sim N(0,1),\qquad a_{k+1}={h^H_k\over k+1},
\tag{9}
\]

\[
f_k=\left\langle\sum_{r+s=k}a_rh^H_s\right\rangle,
\qquad F_H^{(k)}(0)=k!f_k.
\tag{10}
\]

## 4. Chronological reverse equations

The top source is

\[
b^H_k=\sum_{r+s=k}a_rp^H_s.
\tag{11}
\]

Descending through the matrix feeding layer `ell`, define the transported
source at layer `ell-1` by

\[
\begin{split}
r^{\ell-1}_k={}&R^\ell_k
+\sum_{s=0}^{k}\beta^\ell_{ks}h^{\ell-1}_s\\
&+\sum_{d=1}^{k}{1\over d}
 \sum_{p=0}^{d-1}h^{\ell-1}_{d-1-p}
 \left\langle b^\ell_p b^\ell_{k-d}\right\rangle,
\end{split}
\tag{12}
\]

and then

\[
b^{\ell-1}_k=\sum_{r+s=k}p^{\ell-1}_r r^{\ell-1}_s.
\tag{13}
\]

At fixed `k`, equations (11)--(13) run from `ell=H` down to `2`; then (7)
advances the first-layer series.  This makes (1)--(13) triangular in Taylor
order despite the nonlocal forward/transpose responses.

## 5. Terminal Wick--Stein elimination

No `F,R,A0` variable occurs in the emitted normal form.  Readout powers use
ordinary Wick moments.  At layer one, every activation product is the atom

\[
L_1(\nu)=\mathbb E_{G\sim N(0,Q^0)}
\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.
\tag{14}
\]

For one reverse family, choose an index `i` with `rho_i>0` and set

\[
\mathcal W^\ell_R(\rho)
=\sum_j(\rho_j-\mathbf1_{i=j})\mathcal B^\ell_{ij}
 \mathcal W^\ell_R(\rho-e_i-e_j),
\qquad \mathcal W^\ell_R(0)=1.
\tag{15}
\]

For forward exponents `lambda=(lambda_1,...,lambda_5)` and activation
exponents `nu`, choose `i>=1` with `lambda_i>0`:

\[
\begin{split}
\mathcal W^\ell_F(\lambda;\nu)
={}&\sum_{j=1}^5(\lambda_j-\mathbf1_{i=j})
 \mathcal H^\ell_{ij}
 \mathcal W^\ell_F(\lambda-e_i-e_j;\nu)\\
&+\mathcal H^\ell_{i0}\sum_{r=0}^4\nu_r
 \mathcal W^\ell_F(\lambda-e_i;\nu-e_r+e_{r+1}),
\end{split}
\tag{16}
\]

\[
\mathcal W^\ell_F(0;\nu)=L_\ell(\nu),\qquad
L_\ell(\nu)=\mathbb E_{G\sim N(0,Q^{\ell-1})}
\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.
\tag{17}
\]

Equations (15)--(16) strictly lower Gaussian degree, so elimination
terminates.  A scan of all frozen terminal atoms gives derivative ceilings
`1,3,5` for `A,B,C`.  Thus no multivariate Gaussian atom or auxiliary
covariance survives.

## 6. Finite-state and complexity census

At order five, each initialized matrix needs exactly

| registry | independent entries |
|---|---:|
| symmetric `H`, indices `0,...,5` | 21 |
| symmetric `B`, indices `0,...,4` | 15 |
| triangular `alpha`, `s<k<=5` | 15 |
| triangular `beta`, `s<=k<=4` | 15 |
| **total** | **66** |

Hence the chronological compiler has `66(H-1)` deterministic registry
entries.  For fixed order, it performs one forward and one reverse sweep and
is `O(H)` in depth at the response-state level.  This does **not** imply that
the fully distributed normal form is small.

The observed frozen sizes are

| depth | tagged DAG nodes `(A,B,C)` | tagged flat terms `(A,B,C)` | unit flat terms `(A,B,C)` |
|---:|---:|---:|---:|
| 2 | `(9,112,1105)` | `(3,50,1045)` | `(3,46,974)` |
| 3 | `(13,205,2320)` | `(4,342,27421)` | `(4,160,6519)` |
| 4 | `(17,300,3536)` | `(5,1929,462776)` | `(5,350,17641)` |

The compact tagged DAG grows approximately linearly over these depths; assigning distinct
layer tags and distributing every product causes the much larger flat-map
growth.  The fixed-state recursion therefore emits a finite flattened formula
at every fixed `H`, but it is not a depth-uniform constant-size closed form.

## 7. Deep-linear control

Put `m=H+1`, the number of independently initialized parameter blocks.  The
specialization `phi(x)=x`, `Q0=1` gives the exact independently enumerated
controls

\[
(A_3,B_3,C_3)=(4,160,13888),\qquad
(A_4,B_4,C_4)=(5,400,73240).
\tag{18}
\]

Here the subscripts denote hidden depth.  A separate leading-width
path/Wick enumeration exhausted 22,012 derivative-history states at `H=3`
and 102,582 at `H=4`; (18) is therefore not fitted from Route S.

The direct two-factor flow supplies the `H=1` entry, and the Route S compiler
supplies the exact sequence for `H=2,...,10`:

\[
\begin{array}{c|rrrrrrrrrr}
H&1&2&3&4&5&6&7&8&9&10\\ \hline
A&2&3&4&5&6&7&8&9&10&11\\
B&8&48&160&400&840&1568&2688&4320&6600&9680\\
C&32&1464&13888&73240&276864&841232&2188032&5064336&10702560&21025928
\end{array}
\tag{19}
\]

`A=m` follows directly by summing the `m` parameter-block gradient energies.
Exact finite differences in (19) discover the closed forms

\[
B_H={2m^2(m^2-1)\over3},
\qquad
C_H={m^2(m^2-1)(17m^3-4m^2-38m-4)\over15}.
\tag{20}
\]

Equivalently their depth increments are

\[
B(m)-B(m-1)={4\over3}m(m-1)(2m-1),
\tag{21}
\]

\[
C(m)-C(m-1)={m(m-1)\over15}
(119m^4-262m^3+118m^2-7m-26).
\tag{22}
\]

**Claim status.**  Formula `A=m` is proved.  The values in (18) are exact and
independently proved.  Equations (20)--(22) are exact interpolants of the ten
Route S values and factor correctly, but this note does not yet contain a
symbolic transfer proof that bounds the arbitrary-`H` degree by seven.
Accordingly (20) is a strongly checked arbitrary-depth conjecture, not used as
an audit certificate for the generic `H=3,4` maps.  A proof would require a
finite leading-diagram transfer classification (or an equivalent symbolic
specialization of (1)--(16)) showing that no non-polynomial depth dependence
survives.
