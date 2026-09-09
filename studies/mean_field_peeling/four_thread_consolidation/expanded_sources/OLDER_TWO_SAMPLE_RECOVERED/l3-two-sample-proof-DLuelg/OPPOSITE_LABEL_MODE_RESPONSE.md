# R25: exact opposite-label finite Gaussian mode response

Status: finite-law identities and a first-update contribution estimate,
not a continuation or population-limit theorem. This candidate has not
received its fresh isolated audit.

The five requested files were read in full. The scalar Gaussian Euler
law and its formal-source convention are those of
`TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md`, Section 1. The calculations
below give an exact change of coordinates in that law, including its
deterministically selected response coefficients. They do not invoke a
new finite-program identification theorem. Identification with the
fixed-program width limit retains the dependency expressly stated in
that source. The raw matrix identities below also hold at finite width.
No continuous uncut solution, energy identity for internal cuts, or
stronger-than-second-moment tail consequence is presumed.

Only this file is written. No experiments, external theorems, other
agents, or project changes are used.

## 1. Fixed law, populations, and formal coordinates

Fix labels `(1,-1)`, `-1 <= rho < 1`, an arbitrary finite mesh
`k=0,...,M`, step `Delta>0`, and two finite caps `R_1,R_2>=1`. There is
no restriction `M Delta <= 3/2` for the finite algebra in this note.
Here `k Delta` is feature time, and the readout starts identically at
zero. The corresponding finite-width Euler scheme is the normalized
opposite-label feature field with these internal cuts; the physical
finite-width residual is not asserted to stay in one label mode.
Put `C=[[1,rho],[rho,1]]` and let `G` have centered Gaussian law
with covariance `C`.
Fix, in all three layers,

\[
 \phi(z)=1+\frac{\arctan z}{10},\qquad
 \phi'(z)=\frac{1}{10(1+z^2)},\qquad
 \phi''(z)=-\frac{z}{5(1+z^2)^2}.
 \tag{1}
\]

For constants only, write `gamma=1/10` and `a=1+pi/20`, so
`0<phi<a` and `0<phi'<=gamma`. Each scalar cut `tau_R` is smooth and
odd, equals the identity on `[-R,R]`, and obeys
`|tau_R(q)|<=min(|q|,2R)`, `0<=tau_R'<=1`.

Write `P_ell` for the probability space of population `ell`.
Population 1 carries the root pair `G` and the reverse sources
`zeta^(1)`; population 2 carries `xi^(2),zeta^(2)`; population 3
carries `xi^(3)` and the readout. Write `E_ell` for expectation on
population `ell`. A product such as `V^(2) q^(2)_+` is a same-neuron
product on population 2. An expectation on population 3 in a
coefficient multiplying a population-2 field is a deterministic
number, not a product of fields on an identified neuron space.

For any sample pair `X=(X_1,X_2)`, define

\[
 X_+=\frac{X_1+X_2}{2},\quad X_-=\frac{X_1-X_2}{2},\qquad
 T=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
 T^{-1}=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
 \tag{2}
\]

In particular, for every layer and time,

\[
 U^{(\ell)}_k=H^{(\ell)}_{k,+},\quad
 V^{(\ell)}_k=H^{(\ell)}_{k,-},\quad
 p^{(\ell)}_{k,\pm}
 =\frac{\phi'(Z^{(\ell)}_{k1})\pm
             \phi'(Z^{(\ell)}_{k2})}{2},\quad
 d^{(\ell)}_{k,\pm}=\delta^{(\ell)}_{k,\pm}.
 \tag{3}
\]

Thus the gates in (3) are explicitly
`[1/(1+(Z^(ell)_(k1))^2) +/- 1/(1+(Z^(ell)_(k2))^2)]/20`.
The symbol `d` here denotes a backward field, not a variation.
We write `w_k=W^(4)_k`.

Every time/sample source is a separate formal variable, including
zero-variance sources and different time sources having identical
attained values. A partial derivative freezes all already selected
deterministic coefficients and all covariance parameters. It is an
ordinary coordinate derivative of the displayed finite formulas,
taken before evaluation on their possibly singular Gaussian law.
Changing to modes replaces two formal variables by the two invertible
linear combinations (2); it does not take a quotient by the covariance
kernel. In particular,

\[
 \partial_{\zeta_{r,+}}=\partial_{\zeta_{r1}}+
                                      \partial_{\zeta_{r2}},\qquad
 \partial_{\zeta_{r,-}}=\partial_{\zeta_{r1}}-
                                      \partial_{\zeta_{r2}},
 \tag{4}
\]

and the same applies to `xi`. The half factors occur in the output
modes; there is no extra half factor on the right side of (4).

For reference, the sample-coordinate coefficient definitions being
transformed are, for `ell=2,3`,

\[
\begin{aligned}
 A^{(\ell)}_{ka,rb}
 &=E_{\ell-1}\partial_{\zeta^{(\ell-1)}_{rb}}
                         H^{(\ell-1)}_{ka}
   +\frac\Delta2 y_b E_{\ell-1}
                         [H^{(\ell-1)}_{ka}H^{(\ell-1)}_{rb}],
 &&r<k,\\
 B^{(\ell)}_{ka,rb}
 &=E_\ell\partial_{\xi^{(\ell)}_{rb}}\delta^{(\ell)}_{ka}
   +\frac\Delta2\mathbf1_{r<k}y_b E_\ell
                         [\delta^{(\ell)}_{ka}\delta^{(\ell)}_{rb}],
 &&r\le k.
\end{aligned}\tag{5}
\]

These expectations use second moments, not centered covariances of
the generally noncentered nonlinear fields.

## 2. Exact exchange symmetry, including time correlations

Let `P` exchange the samples. The relevant source involution sends

\[
 G\mapsto PG,\quad \xi^{(2)}\mapsto P\xi^{(2)},\quad
 \xi^{(3)}\mapsto P\xi^{(3)},\quad
 \zeta^{(1)}\mapsto-P\zeta^{(1)},\quad
 \zeta^{(2)}\mapsto-P\zeta^{(2)}.
 \tag{6}
\]

The same transformation acts at every time, not separately on
individual time marginals. The resulting formal fields satisfy

\[
 Z^{(\ell)}\mapsto PZ^{(\ell)},\quad
 H^{(\ell)}\mapsto PH^{(\ell)},\quad
 \phi'(Z^{(\ell)})\mapsto P\phi'(Z^{(\ell)}),\quad
 w\mapsto-w,\quad q^{(j)}\mapsto-Pq^{(j)},\quad
 \delta^{(\ell)}\mapsto-P\delta^{(\ell)}.
 \tag{7}
\]

Here `j=1,2` and `ell=1,2,3`, with the bottom backward field defined
using its cut. Oddness of both scalar cuts is essential in (7).

We prove (6)--(7) for the finite construction, without an uncut-flow
uniqueness premise. Initially `G` is exchange invariant and `w_0=0`.
At stage `k`, the bottom fields use strictly past reverse queries.
Then construct in order

\[
 A^{(2)},Z^{(2)},H^{(2)},A^{(3)},Z^{(3)},H^{(3)},
 d^{(3)},B^{(3)},q^{(2)},d^{(2)},B^{(2)},q^{(1)}.
 \tag{8}
\]

The readout `w_k` is already determined by past top features.
If an ordinary pair `X` transforms as `PX` and a reverse source as
`-Pzeta`, the chain rule transforms its derivative matrix as
`D_zeta X -> -P(D_zeta X)P`. The derivative of a backward pair
with respect to a forward source has the same rule. The learned
terms in (5) have the rule as well: their moment matrix commutes
with `P`, whereas `diag(1,-1)` anticommutes with `P`.
Consequently each newly selected deterministic coefficient satisfies

\[
 A^{(\ell)}_{k,r}=-P A^{(\ell)}_{k,r}P,\qquad
 B^{(\ell)}_{k,r}=-P B^{(\ell)}_{k,r}P.
 \tag{9}
\]

The forward and reverse formulas then preserve (7). Their moment
matrices give invariant centered Gaussian extensions of the source
groups. Such covariance matrices are positive semidefinite because
they are matrices of second moments of a finite list of fields.
The centered Gaussian distribution, including a singular one, is
specified by this covariance. This completes the causal induction.
Equivariance is an identity of the full formal expressions, so it
also proves the derivative statement at zero-variance slots.

In modal coordinates the parities under this one involution are:

| Even fields | Odd fields |
|---|---|
| `G_+, xi^(ell)_+, Z^(ell)_+, U^(ell), p^(ell)_+` | `G_-, xi^(ell)_-, Z^(ell)_-, V^(ell), p^(ell)_-` |
| `zeta^(j)_-, q^(j)_-, d^(ell)_-` | `zeta^(j)_+, q^(j)_+, d^(ell)_+, w` |

Every odd field has mean zero. The means of `Z_+,U,p_+,q_-,d_-`
are not forced to vanish, and `E U` is not forced to remain one.
For any two fields on the same population, one even and one odd,
their product has mean zero, at any two times. In particular,

\[
\begin{split}
 E_\ell[U^{(\ell)}_kV^{(\ell)}_r]&=0,\\
 E_\ell[d^{(\ell)}_{k,+}d^{(\ell)}_{r,-}]&=0,\\
 E_j[q^{(j)}_{k,+}q^{(j)}_{r,-}]&=0.
\end{split}\tag{10}
\]

The corresponding centered cross covariances also vanish. An
ordinary pair and a backward pair instead have zero `(+,+)` and
`(-,-)` cross moments; their `(+,-)` and `(-,+)` moments can survive.
For example `E_3[w_k U^(3)_r]=0` but `E_3[w_k V^(3)_r]` need not
vanish. Hence the deterministic predictions satisfy `f_2=-f_1`
and `f_1=E_3[w V^(3)]` in this finite Gaussian law.

More explicitly, any two ordinary sample-pair fields, or any two
backward sample-pair fields, have a time-cross second-moment block
`[[h,c],[c,h]]`. Their centered covariance has the same structure.
An ordinary/backward cross block has structure
`[[u,v],[-v,-u]]`. These assertions concern arbitrary times `k,r`,
not just equal-time variances. They imply equality of the two sample
means for ordinary pairs and opposite means for backward pairs.

The root modes are independent centered Gaussians with variances
`(1+rho)/2,(1-rho)/2`. For `ell=2,3`, the source covariance laws are

\[
\begin{aligned}
 E[\xi^{(\ell)}_{k,+}\xi^{(\ell)}_{r,+}]
     &=E_{\ell-1}[U^{(\ell-1)}_kU^{(\ell-1)}_r],\\
 E[\xi^{(\ell)}_{k,-}\xi^{(\ell)}_{r,-}]
     &=E_{\ell-1}[V^{(\ell-1)}_kV^{(\ell-1)}_r],\\
 E[\zeta^{(\ell-1)}_{k,+}\zeta^{(\ell-1)}_{r,+}]
     &=E_\ell[d^{(\ell)}_{k,+}d^{(\ell)}_{r,+}],\\
 E[\zeta^{(\ell-1)}_{k,-}\zeta^{(\ell-1)}_{r,-}]
     &=E_\ell[d^{(\ell)}_{k,-}d^{(\ell)}_{r,-}].
\end{aligned}\tag{11}
\]

Every mixed `+,-` source covariance, including across different
times, is zero. Thus the entire plus vector and entire minus vector
of each source group are independent. Indeed their joint Gaussian
characteristic function factors because its covariance is block
diagonal; this argument includes singular covariance matrices.
The four original source groups and the root group are independent
by the defining law. Thus all ten modal Gaussian groups (two root
modes and eight source modes) can be chosen mutually independent,
with all within-group temporal correlations retained. A deterministic
zero Gaussian coordinate remains a formal slot.

This source independence is not independence of evolved modes.
For example both `U` and `V` are nonlinear functions of the two
preactivation modes; (10) is orthogonality, not independence.
No factorization of same-population evolved-field products will be
used below.

## 3. Both matrices and all modal coefficient definitions

Direct multiplication, with the half-sum convention (2), gives

\[
 T\begin{pmatrix}u&v\\-v&-u\end{pmatrix}T^{-1}
       =\begin{pmatrix}0&u-v\\u+v&0\end{pmatrix}.
 \tag{12}
\]

Define `A^(ell)_(kr,+-)` and `A^(ell)_(kr,-+)` to be these two
off-diagonal entries, and likewise for `B`. The first sign is the
output mode; the second is the mode multiplied by the coefficient.
The diagonal modal entries are exactly zero for every admissible
time block. Transforming (5), using (4) and (10), yields

\[
\begin{aligned}
 A^{(\ell)}_{kr,+-}
 &=E_{\ell-1}\partial_{\zeta^{(\ell-1)}_{r,-}}U^{(\ell-1)}_k
       +\Delta E_{\ell-1}[U^{(\ell-1)}_kU^{(\ell-1)}_r],\\
 A^{(\ell)}_{kr,-+}
 &=E_{\ell-1}\partial_{\zeta^{(\ell-1)}_{r,+}}V^{(\ell-1)}_k
       +\Delta E_{\ell-1}[V^{(\ell-1)}_kV^{(\ell-1)}_r],
 &&r<k,\\
 B^{(\ell)}_{kr,+-}
 &=E_\ell\partial_{\xi^{(\ell)}_{r,-}}d^{(\ell)}_{k,+}
       +\Delta\mathbf1_{r<k}E_\ell[d^{(\ell)}_{k,+}d^{(\ell)}_{r,+}],\\
 B^{(\ell)}_{kr,-+}
 &=E_\ell\partial_{\xi^{(\ell)}_{r,+}}d^{(\ell)}_{k,-}
       +\Delta\mathbf1_{r<k}E_\ell[d^{(\ell)}_{k,-}d^{(\ell)}_{r,-}],
 &&r\le k,\qquad \ell=2,3.
\end{aligned}\tag{13}
\]

For instance `E U_k U_r=(h+c)/2`, so the transformed learned
entry is `Delta(h+c)/2=Delta E U_k U_r`, not twice this number.
There is no current-time learned transpose term in (13).

At finite width put `u tensor v = uv^T/n`; on the two appropriate
population spaces put `(u tensor v)x=u E[vx]`. Both learned
matrices have the exact increment and unrolling

\[
\begin{aligned}
 W^{(\ell)}_{k+1}-W^{(\ell)}_k
 &=\Delta\bigl(d^{(\ell)}_{k,-}\otimes U^{(\ell-1)}_k
                 +d^{(\ell)}_{k,+}\otimes V^{(\ell-1)}_k\bigr),\\
 W^{(\ell)}_k-W^{(\ell)}_0
 &=\Delta\sum_{r<k}\bigl(d^{(\ell)}_{r,-}\otimes U^{(\ell-1)}_r
                 +d^{(\ell)}_{r,+}\otimes V^{(\ell-1)}_r\bigr),
 \qquad\ell=2,3.
\end{aligned}\tag{14}
\]

In the Gaussian population law, the two actions of (14), using (10),
give exactly the learned terms in (13). At finite width the rank-one
identity (14) holds, but the empirical cross moments need not vanish.
The remaining terms in (13) represent reuse of the initial
matrices. This verifies the proposed forward and transpose algebra
for both matrices, rather than assuming their modal form.

The precise assignment of a potentially large learned coefficient is:

| Coefficient | Learned entry, for `r<k` | Field it multiplies |
|---|---|---|
| `A^(ell)_(kr,+-)` | `Delta E_(ell-1)[U_k U_r]` | backward difference `d^(ell)_(r,-)` |
| `A^(ell)_(kr,-+)` | `Delta E_(ell-1)[V_k V_r]` | backward average `d^(ell)_(r,+)` |
| `B^(ell)_(kr,+-)` | `Delta E_ell[d_(k,+) d_(r,+)]` | feature difference `V^(ell-1)_r` |
| `B^(ell)_(kr,-+)` | `Delta E_ell[d_(k,-) d_(r,-)]` | feature average `U^(ell-1)_r` |

All time indices in the table are retained. The analogous response
entries have the same placement, but symmetry alone imposes no
magnitude or sign bound on those derivative expectations.

## 4. Entire finite modal Euler law, with the actual cuts

For scalar mode values `(b,c)` define the two-component map

\[
 \mathcal T_{R,+}(b,c)=\frac{\tau_R(b+c)+\tau_R(b-c)}2,\qquad
 \mathcal T_{R,-}(b,c)=\frac{\tau_R(b+c)-\tau_R(b-c)}2.
 \tag{15}
\]

These are coupled nonlinear cuts. In general they are not
`tau_R(b),tau_R(c)`. For `j=1,2` use `R_j` and set

\[
\begin{aligned}
 d^{(j)}_{k,+}
 &=p^{(j)}_{k,+}\mathcal T_{R_j,+}(q^{(j)}_{k,+},q^{(j)}_{k,-})
   +p^{(j)}_{k,-}\mathcal T_{R_j,-}(q^{(j)}_{k,+},q^{(j)}_{k,-}),\\
 d^{(j)}_{k,-}
 &=p^{(j)}_{k,+}\mathcal T_{R_j,-}(q^{(j)}_{k,+},q^{(j)}_{k,-})
   +p^{(j)}_{k,-}\mathcal T_{R_j,+}(q^{(j)}_{k,+},q^{(j)}_{k,-}).
\end{aligned}\tag{16}
\]

The bottom field `d^(1)` is used only for its update; the middle
field `d^(2)` is also the transpose input for matrix 2. The complete
forward, readout, and reverse equations are

\[
\begin{aligned}
 Z^{(1)}_{k,+}&=G_++\frac{\Delta(1+\rho)}2\sum_{r<k}d^{(1)}_{r,-},\\
 Z^{(1)}_{k,-}&=G_-+\frac{\Delta(1-\rho)}2\sum_{r<k}d^{(1)}_{r,+},\\
 Z^{(\ell)}_{k,+}&=\xi^{(\ell)}_{k,+}
                         +\sum_{r<k}A^{(\ell)}_{kr,+-}d^{(\ell)}_{r,-},\\
 Z^{(\ell)}_{k,-}&=\xi^{(\ell)}_{k,-}
                         +\sum_{r<k}A^{(\ell)}_{kr,-+}d^{(\ell)}_{r,+},
 &&\ell=2,3,\\
 U^{(\ell)}_k&=\frac{\phi(Z^{(\ell)}_{k,+}+Z^{(\ell)}_{k,-})
                       +\phi(Z^{(\ell)}_{k,+}-Z^{(\ell)}_{k,-})}{2},\\
 V^{(\ell)}_k&=\frac{\phi(Z^{(\ell)}_{k,+}+Z^{(\ell)}_{k,-})
                       -\phi(Z^{(\ell)}_{k,+}-Z^{(\ell)}_{k,-})}{2},
 &&\ell=1,2,3,\\
 w_k&=\Delta\sum_{r<k}V^{(3)}_r,\qquad
 d^{(3)}_{k,+}=w_kp^{(3)}_{k,+},\qquad
 d^{(3)}_{k,-}=w_kp^{(3)}_{k,-},\\
 q^{(j)}_{k,+}&=\zeta^{(j)}_{k,+}
                         +\sum_{r\le k}B^{(j+1)}_{kr,+-}V^{(j)}_r,\\
 q^{(j)}_{k,-}&=\zeta^{(j)}_{k,-}
                         +\sum_{r\le k}B^{(j+1)}_{kr,-+}U^{(j)}_r,
 &&j=1,2.
\end{aligned}\tag{17}
\]

Equations (11), (13), (15)--(17), selected in order (8), are the
entire finite source-response system. In particular, current reverse
returns are retained; forward returns are strictly historical.
The bottom factors are `Delta(1+rho)/2` and `Delta(1-rho)/2`.
At `rho=-1`, `G_+=0` and the first of (17) gives `Z^(1)_(k,+)=0`
exactly. This singular input case requires no inverse Gram matrix.

For completeness the formal derivative equations can be generated
without differentiating a covariance or a coefficient. Let `h` denote
variation in any one formal modal source slot. At each layer put

\[
 c^{(\ell)}_{k,\pm}
 =\frac{\phi''(Z^{(\ell)}_{k1})\pm
               \phi''(Z^{(\ell)}_{k2})}{2}.
\]

Then, at every time,

\[
\begin{aligned}
 hU&=p_+hZ_++p_-hZ_-,&hV&=p_-hZ_++p_+hZ_-,\\
 hp_+&=c_+hZ_++c_-hZ_-,&hp_-&=c_-hZ_++c_+hZ_-.
\end{aligned}\tag{18}
\]

All fields in a line of (18) carry the same layer and time indices.
For the cut at layer `j`, define just for this derivative
`t_+=(tau_Rj'(q_++q_-)+tau_Rj'(q_+-q_-))/2` and
`t_-=(tau_Rj'(q_++q_-)-tau_Rj'(q_+-q_-))/2`. Its differential is

\[
 \begin{pmatrix}h\mathcal T_+\\h\mathcal T_-\end{pmatrix}
 =\begin{pmatrix}t_+&t_-\\t_-&t_+\end{pmatrix}
       \begin{pmatrix}hq_+\\hq_-\end{pmatrix}.
 \tag{19}
\]

Differentiate both products in each line of (16), using (18)--(19).
At the top, `hd^(3)_pm=p^(3)_pm hw+w hp^(3)_pm` and
`hw_k=Delta sum_(r<k) hV^(3)_r`. The remaining derivative recursion is
exactly

\[
\begin{aligned}
 hZ^{(1)}_{k,+}&=hG_++\frac{\Delta(1+\rho)}2\sum_{r<k}hd^{(1)}_{r,-},\\
 hZ^{(1)}_{k,-}&=hG_-+\frac{\Delta(1-\rho)}2\sum_{r<k}hd^{(1)}_{r,+},\\
 hZ^{(\ell)}_{k,+}&=h\xi^{(\ell)}_{k,+}
                     +\sum_{r<k}A^{(\ell)}_{kr,+-}hd^{(\ell)}_{r,-},\\
 hZ^{(\ell)}_{k,-}&=h\xi^{(\ell)}_{k,-}
                     +\sum_{r<k}A^{(\ell)}_{kr,-+}hd^{(\ell)}_{r,+},\\
 hq^{(j)}_{k,+}&=h\zeta^{(j)}_{k,+}
                     +\sum_{r\le k}B^{(j+1)}_{kr,+-}hV^{(j)}_r,\\
 hq^{(j)}_{k,-}&=h\zeta^{(j)}_{k,-}
                     +\sum_{r\le k}B^{(j+1)}_{kr,-+}hU^{(j)}_r.
\end{aligned}\tag{20}
\]

Each source variation in (20) is the Kronecker injection into the
chosen formal slot, even if that slot has zero variance. Equations
(18)--(20) and the product rule explicitly specify every expectation
in (13). Finite caps, bounded activation derivatives, and the finite
causal order make these finite expectations well defined: for example
`|w_k|<=a M Delta`, and each reverse query is a Gaussian coordinate
plus finitely many bounded features with finite deterministic
coefficients. Induction supplies finite derivatives at each stage.
For identity cuts the same fixed finite induction gives derivatives
bounded by polynomials in the finite Gaussian source vector, hence
finite expectations as well. The degree and constants may grow with
the number of mesh steps.
This is a fixed-mesh assertion, not a mesh-uniform response bound.

## 5. Exact contrast factors for the uncut formulas

For `z,z'`, let `alpha=arctan z`, `beta=arctan z'` and define
`sinc(t)=sin(t)/t`, continuously extended at zero. Then

\[
 \frac{\phi'(z)-\phi'(z')}{2}
 =-\sin(\alpha+\beta)\operatorname{sinc}(\alpha-\beta)
                         \frac{\phi(z)-\phi(z')}{2}.
 \tag{21}
\]

Indeed `cos^2 alpha-cos^2 beta=-sin(alpha+beta)sin(alpha-beta)`.
Thus at every layer and time there is the explicit factor
`lambda^(ell)_k=-sin(alpha+beta)sinc(alpha-beta)` with

\[
 p^{(\ell)}_{k,-}=\lambda^{(\ell)}_k V^{(\ell)}_k,
 \qquad |\lambda^{(\ell)}_k|\le1.
 \tag{22}
\]

This proves the strict-monotone relative-gate inequality requested:
`|phi'(z)-phi'(z')|<=|phi(z)-phi(z')|`. Strict monotonicity makes
`phi(z)-phi(z')` nonzero off the diagonal. On the diagonal (21)
is understood continuously and both differences vanish.

A useful curvature version follows by differentiating (1):

\[
 \frac{\phi'''(z)}{\phi'(z)}
       =\frac{6z^2-2}{(1+z^2)^2},\qquad
 \left|\frac{\phi'''(z)}{\phi'(z)}\right|\le2.
\]

Integration with respect to the strictly increasing variable `phi(z)`
therefore gives `|phi''(z)-phi''(z')|<=2|phi(z)-phi(z')|`.
Consequently `c^(ell)_(k,-)=nu^(ell)_k V^(ell)_k` with `|nu|<=2`,
where `nu` is the corresponding divided difference, continuously
extended on the diagonal. Also `|c_+|<=gamma`, since
`|phi''/phi'|=2|z|/(1+z^2)<=1`.

Removing both cuts from the finite formulas gives, exactly,

\[
\begin{aligned}
 d^{(3)}_{k,-}&=w_k\lambda^{(3)}_kV^{(3)}_k,&
 d^{(3)}_{k,+}&=w_kp^{(3)}_{k,+},\\
 d^{(j)}_{k,-}&=p^{(j)}_{k,+}q^{(j)}_{k,-}
             +\lambda^{(j)}_kV^{(j)}_kq^{(j)}_{k,+},&
 d^{(j)}_{k,+}&=p^{(j)}_{k,+}q^{(j)}_{k,+}
             +\lambda^{(j)}_kV^{(j)}_kq^{(j)}_{k,-},\quad j=1,2.
\end{aligned}\tag{23}
\]

For example the learned `B^(3)_(kr,-+)` contains precisely

\[
 \Delta E_3[w_k w_r\lambda^{(3)}_k\lambda^{(3)}_r
                              V^{(3)}_k V^{(3)}_r],\qquad r<k,
 \tag{24}
\]

while learned `B^(3)_(kr,+-)` contains
`Delta E_3[w_k w_r p^(3)_(k,+)p^(3)_(r,+)]` and multiplies
`V^(2)_r`. At matrix 2, the analogous entries use the full sums in
(23), including their mixed products. No independence or positivity
allows deletion of those mixed products.

There is also an exact check on current response blocks at every
finite time. Write

\[
 b^{(3)}_k=E_3[w_k\phi''(Z^{(3)}_{k1})]
          =E_3[w_k c^{(3)}_{k,-}].
\]

Then `B^(3)_(kk,+-)=B^(3)_(kk,-+)=b^(3)_k`. The analogous two
entries for matrix 2 are both

\[
 b^{(2)}_k
 =E_2[\phi''(Z^{(2)}_{k1})\tau_{R_2}(q^{(2)}_{k1})]
  +b^{(3)}_k E_2[(\phi'(Z^{(2)}_{k1}))^2
                                      \tau_{R_2}'(q^{(2)}_{k1})].
 \tag{25}
\]

To check these facts, a current forward source enters its own
preactivation directly, while all strictly past features and `w_k`
are fixed. The only current dependence of `q^(2)_k` on that source
is through `B^(3)_(kk)H^(2)_k`. The sample block `B^(3)_(kk)` is
`diag(b^(3)_k,-b^(3)_k)`. This proves (25), including its factor.
For no cut the first term of (25) is
`E_2[c^(2)_(k,+)q^(2)_(k,-)+c^(2)_(k,-)q^(2)_(k,+)]`.
Its second summand has the exact contrast factor just proved.

## 6. All first-update coefficient values, without merging slots

This section assumes `M>=1`. It computes both nonzero modal
directions of each of `A^(2),A^(3),B^(3),B^(2)`, with the historical
and current blocks of each transpose kept separate. In particular it
gives all four modal transpose directions, not just their sum after
evaluation.

Let `X^(ell)_a=Z^(ell)_(0a)`. These initial pairs are centered Gaussian,
with covariance `C` at layer 1 and covariance
`E_(ell-1)[H^(ell-1)_(0a)H^(ell-1)_(0b)]` at layers 2 and 3.
In this section alone, an unindexed `U,V,p_+,p_-` inside `E_ell`
means the layer-`ell`, time-zero field. Define the following explicit
initial Gaussian integrals:

\[
\begin{aligned}
 K_\ell^+&=E_\ell[U^2],&\kappa_\ell&=E_\ell[V^2],\\
 e_\ell&=\frac1{100}E_\ell\frac1{(1+(X^{(\ell)}_1)^2)^2},&
 f_\ell&=\frac1{100}E_\ell
       \frac1{(1+(X^{(\ell)}_1)^2)(1+(X^{(\ell)}_2)^2)},\\
 t_\ell&=E_\ell[V\phi''(X^{(\ell)}_1)]
 =-\frac1{100}E_\ell
   \frac{X^{(\ell)}_1(\arctan X^{(\ell)}_1-\arctan X^{(\ell)}_2)}
        {(1+(X^{(\ell)}_1)^2)^2}.
\end{aligned}\tag{26}
\]

In particular `E_ell[p_+^2]=(e_ell+f_ell)/2` and
`E_ell[p_-^2]=(e_ell-f_ell)/2`. These are specified one- or
two-dimensional Gaussian expectations determined recursively by
`rho`; they contain no unknown evolved response.

At time zero `w_0` and `d^(3)_0` vanish identically as formal
expressions. Both `B^(3)_(00)` and `B^(2)_(00)` are zero. However

\[
 q^{(2)}_{0a}=\zeta^{(2)}_{0a},\qquad
 \delta^{(2)}_{0a}
      =\phi'(\xi^{(2)}_{0a})\tau_{R_2}(\zeta^{(2)}_{0a})
 \tag{27}
\]

are retained formally. The sources `zeta^(2)_0,zeta^(1)_0` vanish
almost surely, whereas
`partial delta^(2)_(0a)/partial zeta^(2)_(0a)=phi'(X^(2)_a)`
on the attained law. Similarly the first-coordinate update has
nonzero derivatives in its zero-valued `zeta^(1)_0` slots.

After the first Euler update all hidden matrices and bottom values
are still their initial attained values, while `w_1=Delta V^(3)_0`.
Thus, on the Gaussian law,

\[
 \begin{gathered}
 Z^{(\ell)}_{1a}=Z^{(\ell)}_{0a},\quad
 H^{(\ell)}_{1a}=H^{(\ell)}_{0a}\quad(\ell=1,2,3),\\
 \xi^{(\ell)}_{1a}=\xi^{(\ell)}_{0a}\quad(\ell=2,3).
 \end{gathered}
 \tag{28}
\]

The equalities in (28) are not substitutions in the formal program.

### 6.1 The two forward blocks

Direct differentiation of the first-coordinate update gives

\[
\begin{aligned}
 A^{(2)}_{10,+-}&=\Delta K_1^++\frac\Delta2(e_1+\rho f_1),\\
 A^{(2)}_{10,-+}&=\Delta\kappa_1+\frac\Delta2(e_1-\rho f_1).
\end{aligned}\tag{29}
\]

In sample coordinates the response part is
`(Delta/2) C_ab y_b E_1[phi'(G_a)phi'(G_b)]`, which verifies
both angle factors and both half factors in (29).

At the middle layer, differentiating (27) before evaluation gives
`D_zeta2_0 H2_1=diag(phi'(X2)) A2_10 diag(phi'(X2))`.
Its modal entries are therefore

\[
\begin{aligned}
 A^{(3)}_{10,+-}
 &=\Delta K_2^+
   +\frac{e_2+f_2}{2}A^{(2)}_{10,+-}
   +\frac{e_2-f_2}{2}A^{(2)}_{10,-+},\\
 A^{(3)}_{10,-+}
 &=\Delta\kappa_2
   +\frac{e_2-f_2}{2}A^{(2)}_{10,+-}
   +\frac{e_2+f_2}{2}A^{(2)}_{10,-+}.
\end{aligned}\tag{30}
\]

Although the response terms in (29)--(30) multiply fields with
zero attained value in this first forward step, the coefficients
themselves are not zero. They are independent of both cap sizes.

### 6.2 The four transpose directions, historical and current

The top source slots `xi^(3)_0` and `xi^(3)_1` give different
derivatives: the first differentiates `w_1`, the second its current
gate. Thus the complete matrix-3 values are

\[
\begin{array}{c|cc}
 & (+,-)&(-,+)\\ \hline
 B^{(3)}_{10}&\displaystyle\frac\Delta2(e_3+f_3)
             &\displaystyle\frac\Delta2(e_3-f_3)\\[2mm]
 B^{(3)}_{11}&\Delta t_3&\Delta t_3 .
\end{array}\tag{31}
\]

All learned transpose terms at this step vanish because their
historical backward field is zero. Formula (31) still has two
distinct time blocks.

To state matrix 2 exactly with its cut, set

\[
 \beta_+=\frac{e_3+f_3}{2}+t_3,\qquad
 \beta_-=\frac{e_3-f_3}{2}+t_3.
 \tag{32}
\]

Let `eta_+,eta_-` be independent centered Gaussians, independent of
the initial population-2 pair, with variances

\[
 E\eta_+^2=E_3[V^2p_+^2],\qquad
 E\eta_-^2=E_3[V^2p_-^2].
\]

Only when evaluating the law (not differentiating it), (28) and
(31) give the actual first middle queries

\[
 Q_+=q^{(2)}_{1,+}=\Delta(\eta_++\beta_+V^{(2)}_0),\qquad
 Q_-=q^{(2)}_{1,-}=\Delta(\eta_-+\beta_-U^{(2)}_0),\quad
 Q_1=Q_++Q_-,\quad Q_2=Q_+-Q_-.
 \tag{33}
\]

Define three explicit population-2 Gaussian integrals, now including
these two additional independent Gaussian coordinates:

\[
\begin{aligned}
 a_2&=E_2[(\phi'(X^{(2)}_1))^2\tau_{R_2}'(Q_1)],\\
 b_2&=E_2[\phi'(X^{(2)}_1)\phi'(X^{(2)}_2)\tau_{R_2}'(Q_1)],\\
 c_2&=E_2[\phi''(X^{(2)}_1)\tau_{R_2}(Q_1)].
\end{aligned}\tag{34}
\]

The same first two expectations with samples exchanged and `Q_2`
are equal to those displayed, because `tau_R2'` is even and the
exchange sends `Q_1` to `-Q_2`. The counterpart of the third
expectation is its negative. The complete matrix-2 values are

\[
\begin{array}{c|cc}
 & (+,-)&(-,+)\\ \hline
 B^{(2)}_{10}&\displaystyle\frac\Delta2(e_3a_2+f_3b_2)
             &\displaystyle\frac\Delta2(e_3a_2-f_3b_2)\\[2mm]
 B^{(2)}_{11}&c_2+\Delta t_3a_2&c_2+\Delta t_3a_2 .
\end{array}\tag{35}
\]

To verify (35), at the attained law the derivative of `Z2_1` in
`xi2_0` is zero: the possibly intervening derivative in (27)
contains `tau_R2(0)`. The derivative in `xi2_1` is the identity.
The historical derivative is consequently

\[
 D_{\xi^{(2)}_0}\delta^{(2)}_1
 =\operatorname{diag}(\phi'(X^{(2)})\tau_{R_2}'(Q))
     B^{(3)}_{10}\operatorname{diag}(\phi'(X^{(2)})).
\]

The current derivative adds
`diag(phi''(X2) tau_R2(Q))` and replaces `B3_10` by `B3_11`
in this expression. Substituting their separate sample blocks from
(31) proves (35). This also explains why differentiating the
evaluated expression (33) would give the wrong time allocation.

For completeness the first bottom query values are

\[
\begin{aligned}
 q^{(1)}_{1,+}&=\zeta^{(1)}_{1,+}
              +(B^{(2)}_{10,+-}+B^{(2)}_{11,+-})V^{(1)}_0,\\
 q^{(1)}_{1,-}&=\zeta^{(1)}_{1,-}
              +(B^{(2)}_{10,-+}+B^{(2)}_{11,-+})U^{(1)}_0.
\end{aligned}\tag{36}
\]

The two centered Gaussian source modes in (36) are independent
of each other and of `G`, with variances
`E_2[(d^(2)_(1,+))^2]` and `E_2[(d^(2)_(1,-))^2]`. Those middle
fields are exactly (16) evaluated at `X^(2),Q_+,Q_-`. Again these
are second moments, not variances after subtracting a backward mean.
The bottom cut affects the subsequent update, not (29)--(36).

### 6.3 Elementary angle information and the uncut specializations

Write `theta=1-rho`. Initial Gaussian preactivation differences at
layer `ell>=2` have variance `4 kappa_(ell-1)`. Lipschitzness of
`phi` gives

\[
 \kappa_\ell\le\frac{\gamma^{2\ell}}2\theta,\quad
 0\le\frac{e_\ell-f_\ell}{2}=E_\ell[p_-^2]\le\kappa_\ell,
 \quad |t_\ell|=|E_\ell[V c_-]|\le2\kappa_\ell.
 \tag{37}
\]

The base for the first inequality is
`E[(G_1-G_2)^2]=2 theta`; its induction uses
`|phi(z)-phi(z')|<=gamma|z-z'|`. The other two inequalities follow
from (22) and its curvature version. No sign of `t_ell` is needed.
For instance (29)--(30) imply the explicit bounds

\[
\begin{aligned}
 0\le A^{(2)}_{10,+-}&\le\Delta(a^2+\gamma^2),\\
 0\le A^{(2)}_{10,-+}&\le\tfrac32\Delta\gamma^2\theta,\\
 0\le A^{(3)}_{10,-+}
 &\le\Delta\gamma^4\theta
                  \left(2+\frac{a^2+\gamma^2}{2}\right).
\end{aligned}\tag{38}
\]

Here `e_1-rho f_1=(e_1-f_1)+theta f_1` and `f_1<=gamma^2`
give the second line; the third follows by bounding the two gate
moments in (30) by `kappa_2` and `gamma^2`. Thus the large average
forward entry and its small contrast counterpart are already
quantitatively different on this first mesh step.

The top entries obey

\[
 0\le B^{(3)}_{10,+-}\le\Delta\gamma^2,\quad
 0\le B^{(3)}_{10,-+}\le\Delta\kappa_3,\quad
 |B^{(3)}_{11,\pm\mp}|\le2\Delta\kappa_3.
 \tag{39}
\]

For no middle cut, (34) specializes to `a_2=e_2,b_2=f_2` and

\[
 c_2=\Delta(\beta_+t_2+\beta_-s_2),\qquad
 s_2=E_2[U^{(2)}_0\phi''(X^{(2)}_1)].
 \tag{40}
\]

Indeed the Gaussian noise in (33) is centered and independent of
`X^(2)`, so its contribution to this linear expectation is zero.
In particular the uncut values in (35) are

\[
\begin{aligned}
 B^{(2)}_{10,+-}&=\tfrac\Delta2(e_3e_2+f_3f_2),\\
 B^{(2)}_{10,-+}&=\tfrac\Delta2(e_3e_2-f_3f_2),\\
 B^{(2)}_{11,+-}=B^{(2)}_{11,-+}
   &=\Delta(\beta_+t_2+\beta_-s_2+t_3e_2).
\end{aligned}\tag{41}
\]

For example `|s_2|<=a gamma`, and hence

\[
\begin{aligned}
 0\le B^{(2)}_{10,+-}&\le\Delta\gamma^4,\\
 0\le B^{(2)}_{10,-+}&\le\Delta\gamma^2(\kappa_2+\kappa_3),\\
 |B^{(2)}_{11,\pm\mp}|
 &\le\Delta\{2(\gamma^2+2\kappa_3)\kappa_2
                   +3a\gamma\kappa_3+2\gamma^2\kappa_3\}.
\end{aligned}\tag{42}
\]

The second line uses
`e_3e_2-f_3f_2=e_3(e_2-f_2)+f_2(e_3-f_3)`.
Bounds (40)--(42) concern the uncut formulas; the exact cut values
are (34)--(35). No sign assertion for their historical `(-,+)`
entry is obtained by replacing `a_2,b_2` by uncut gate moments.

## 7. A finite-mesh actual contribution estimate missed by row sums

The following bound holds for every first step `Delta>0` and both
finite caps, since the actual first middle query (33) precedes the
middle cut and the first hidden changes have zero attained value:

\[
 \|q^{(2)}_{1,-}\|_{L^2(P_2)}
 \le\Delta\bigl(\sqrt3\,\gamma^2\kappa_2+3a\kappa_3\bigr)
 \le\frac{\Delta\gamma^6}{2}(\sqrt3+3a)(1-\rho).
 \tag{43}
\]

This is an estimate on the actual half-difference of the first
middle reverse query, including its Gaussian source and its complete
historical plus current response, not just a coefficient bound.

To prove it, (37) gives `|beta_-|<=3 kappa_3`, whereas (22) gives

\[
 \|\eta_-\|_2=(E_3[V^2p_-^2])^{1/2}
                      \le(E_3[V^4])^{1/2}.
\]

The initial top preactivation difference is a centered scalar
Gaussian of variance `4 kappa_2`. Its fourth moment is
`3(4 kappa_2)^2` (by the elementary Gaussian integral), and
`|V^(3)_0|<=gamma|X^(3)_1-X^(3)_2|/2`. Therefore

\[
 (E_3[V^4])^{1/2}\le\sqrt3\,\gamma^2\kappa_2.
\]

Apply the triangle inequality to (33), using `||U^(2)_0||_2<=a`,
and then (37). This proves (43) without factoring any evolved-field
product. In the same manner the actual average query satisfies

\[
 \|q^{(2)}_{1,+}\|_2
 \le\Delta\{\gamma\sqrt{\kappa_3}
                    +(\gamma^2+2\kappa_3)\sqrt{\kappa_2}\}.
 \tag{44}
\]

Thus the average query has a bound of order `Delta sqrt(1-rho)`,
and its difference has the stronger order `Delta(1-rho)` in (43).
The coefficient `B^(3)_(10,+-)=Delta E_3[p_+^2]`, which need not
be small as `rho` approaches one, multiplies `V^(2)_0`, not
`U^(2)_0`. The coefficient multiplying the latter in the difference
query is `Delta beta_-`, which is of order `Delta(1-rho)`.
An absolute sample-row estimate charging the large coefficient
against the positive activation bound loses both assignments.

Oddness and one-Lipschitzness of the scalar cut also give
`|mathcal T_(R,+)(b,c)|<=|b|` and
`|mathcal T_(R,-)(b,c)|<=|c|`: subtract `tau_R(-b+c)` for the
first inequality and subtract `tau_R(b-c)` for the second.
These inequalities preserve the actual coupled cuts in (16), but
do not make the two cut outputs independent or separate scalar cuts.

## 8. Exact later-time term left uncontrolled

There is no continuation estimate hidden in (43). To identify the
specific missing response, take the uncut middle field and vary a
historical forward average source `xi^(2)_(r,+)`, holding the
coefficients fixed. With all fields below at layer 2, time `k`, (23)
and (18) give the full identity

\[
\begin{aligned}
 h d_-={}&p_+h q_-+p_-h q_+\\
         &+q_-(c_+h Z_++c_-h Z_-)\\
         &+q_+(c_-h Z_++c_+h Z_-).
\end{aligned}\tag{45}
\]

In the response part of `B^(2)_(kr,-+)`, the last line contains
the two exact expectations

\[
 E_2\!\left[c^{(2)}_{k,-}q^{(2)}_{k,+}
       \partial_{\xi^{(2)}_{r,+}}Z^{(2)}_{k,+}\right],\qquad
 E_2\!\left[c^{(2)}_{k,+}q^{(2)}_{k,+}
       \partial_{\xi^{(2)}_{r,+}}Z^{(2)}_{k,-}\right].
 \tag{46}
\]

The first has the exact factor `c^(2)_(k,-)=nu^(2)_k V^(2)_k`,
`|nu|<=2`. The second requires control of the contrast sensitivity
itself. Both integrands are even under the sample involution, so
neither expectation vanishes by symmetry. The associated sensitivity
in the second term retains its complete history,

\[
 \partial_{\xi^{(2)}_{r,+}}Z^{(2)}_{k,-}
   =\sum_{v<k}A^{(2)}_{kv,-+}
              \partial_{\xi^{(2)}_{r,+}}d^{(2)}_{v,+}.
 \tag{47}
\]

There is no direct injection in (47), since its output mode is minus
and its differentiated source mode is plus. Formula (47) still
does not bound the historical derivative coefficients or the
correlated product in (46). With cuts, (19) inserts the genuine
mixed cut derivatives in the same recursion; their boundedness
alone supplies no replacement estimate for these products.

In particular, neither
`||V^(2)_k q^(2)_(k,+)||_2 <= ||V^(2)_k||_2 ||q^(2)_(k,+)||_2`
nor an analogous factorization with a historical sensitivity has
been proved. They do not follow from the independent Gaussian
source groups. The uncut action identities in
`SHIFTED_ARCTAN_CONTRAST_ROUTE.md` concern an existing gradient
trajectory; internally clipped backward propagation has not been
shown to be a positive contraction of its full gradient. No such
energy premise is used here. Even an applicable second-moment or
action bound would not by itself give the response tails required
for global cut removal.

Established at this sidecar's scope are the finite symmetry and
covariance structure, the entire modal system with formal source
derivatives, the separate first-update coefficients for both learned
matrices and their transposes, and the actual estimate (43).
The first concrete unresolved continuation terms are (46)--(47),
not a claim that sample differences or the initial contrast kernel
vanish. No global theorem, trained-path sign invariant, or tail
bound is asserted.
