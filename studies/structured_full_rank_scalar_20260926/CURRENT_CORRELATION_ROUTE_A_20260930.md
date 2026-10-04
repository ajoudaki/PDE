# Current feature–readout covariance gate closure

2026-09-30. Frozen before this candidate's training. Scoped theory and
instantaneous algebra checks only; unreviewed study material. The four
assigned energy-route, feedback-results, endpoint-diagnostic and bounded-Gram
implementation inputs were read completely. No sibling route, other study,
saved trajectory or external scientific source was read. Required rigorous
mathematics and research-contract/adversarial-audit instructions were used.
The supervisor subsequently authorized the implementation and algebra-check
files named below. No required scientific input is missing.

**Decision.** Freeze one explicit current-correlation candidate. Its state is
the current Gram of training features and readout: training residual `r`,
symmetric feature Gram `K`, and readout energy `q`. A current weighted gate
Gram is reconstructed from **joint** feature–readout correlations, rather
than from feature diagonals and readout norm alone. This is not an
independently evolved exact dense gate Gram. The supervisor explicitly
accepted this derived current channel as within the experiment's scope.

The state has `m+m(m+1)/2+1` training scalars; every passive query has `m+2`.
The ODE is regular at zero readout and uses no matrix inverse, particles,
neurons, response dictionary, Taylor-order extension or learned coefficient.
It preserves positive augmented Grams, nonincreasing training loss, the
canonical readout-energy identity, feature-diagonal bounds, passive-output
bounds, and training aliases. These are exact properties of the surrogate,
**not a dense-fidelity result**. Its practical claim remains the frozen hard
circle target of raw RMS at most 0.05; no result for that claim is available
in this report.

## Exact dense evolution before closure

Write `alpha=2/m`, `r_a=f_a-y_a` and use the normalized neuron inner product
`<v,w>=v^T w/n`. The network is

\[
p_a=\tanh(wx_a),\quad h_a=\tanh(Wp_a),\quad
f_a=\langle c,h_a\rangle,\quad
d_a=1-h_a^2,\quad e_a=1-p_a^2.
\]

The canonical mobilities `(n,1,n)` give exactly

\[
\dot c=-\alpha\sum_b r_bh_b,\qquad
\dot W=-\frac\alpha n\sum_b r_b(c\odot d_b)p_b^T,\qquad
\dot w=-\alpha\sum_b r_b[e_b\odot W^T(c\odot d_b)]x_b^T.
\tag{1}
\]

Consequently, with `X_ab=x_a^T x_b`,

\[
B_{ab}=\langle p_a,p_b\rangle I+
X_{ab}W\operatorname{diag}(e_a\odot e_b)W^T,\qquad
\dot h_a=-\alpha\sum_b r_b\operatorname{diag}(d_a)
B_{ab}\operatorname{diag}(d_b)c.                 \tag{2}
\]

No width limit or independence assumption enters (1)–(2). Each `B_ab` is
symmetric and `B_ab=B_ba`. Its block kernel is positive semidefinite,
as is the full dense tangent kernel.

The exact current gate Gram and energy are

\[
G^{\rm dense}_{ab}=\langle c\odot d_a,c\odot d_b\rangle,
\qquad q=\langle c,c\rangle.
\]

Set `zeta_a=sum_e r_e B_ae(c odot d_e)`, so
`hdot_a=-alpha d_a odot zeta_a`. Direct product differentiation gives

\[
\begin{split}
\dot G^{\rm dense}_{ab}
={}&-2\alpha\sum_e r_e\langle c\odot h_e,d_a\odot d_b\rangle\\
&+2\alpha\langle c^2\odot h_a\odot d_a\odot d_b,\zeta_a\rangle
 +2\alpha\langle c^2\odot h_b\odot d_a\odot d_b,\zeta_b\rangle.
\end{split}                                                     \tag{3}
\]

Thus even this one current matrix introduces mixed feature/readout moments,
cubic readout terms and the current neuron-mixing operators. The exact
training tangent kernel is not determined by `K,q,Gdense`: its first-layer
part also contains the current backward Gram. Equation (3), not a formal
assertion that `G` closes, is the starting point.

## Three explicit approximation steps

**1. Freeze and isotropize the preactivation response.** Replace
`B_ab(t)` by `beta_ab I`, where only the exact initialized arrays determine

\[
\beta_{ab}=\langle p_a^0,p_b^0\rangle+
X_{ab}\frac1n\sum_j e_{a,j}^0 e_{b,j}^0
                         \sum_i(W^0_{ij})^2.                    \tag{4}
\]

This is exactly `tr(B_ab(0))/n`, not an expectation or fitted coefficient.
It discards both current first-layer evolution and initialized anisotropic
mixing. Its matrix is positive semidefinite: the first term is a Gram;
the second is the entrywise product of the input Gram and the Gram of
`e_a^0` weighted by nonnegative column norms. For a vector `v`, positivity
of this product follows by expressing both factors as sums of rank-one
Grams, yielding sums of squared inner products with `v`. The same
construction supplies query rows and a positive augmented beta Gram.

**2. Project a gate multiplication onto Gaussian linear variables.**
For centered jointly Gaussian scalar variables `H,Z,V`, differentiation
of their moment-generating function
`exp(t^T Cov t/2)` gives

\[
E[ZH^2V]=E[ZV]E[H^2]+2E[ZH]E[HV].
\]

Consequently the orthogonal projection of `(1-H^2)V` onto their Gaussian
linear span is

\[
(1-EH^2)V-2E[HV]H.                              \tag{5}
\]

We use (5) as a covariance closure for the actual bounded features and
readout. Actual tanh activations are not Gaussian. Moreover, even for
Gaussian variables this discards the orthogonal cubic component; composing
two projected gates need not equal projecting their product. Those are
explicit lost terms, not a higher-order accuracy claim.

**3. Saturation rescaling.** Let
`s_a=1-K_aa`, `s0_a=1-K0_aa>0`, and `lambda_a=2/s0_a`.
In an abstract inner-product space define the self-adjoint operator

\[
D_a=s_a(I-\lambda_a h_a\otimes h_a),\qquad
(h_a\otimes h_a)v=h_a\langle h_a,v\rangle.        \tag{6}
\]

The raw Gaussian projection would be `s_a I-2 h_a tensor h_a`.
Equation (6) instead multiplies its rank-one coefficient by `s_a/s0_a`.
It agrees with (5) at initialization and makes the whole operator vanish
at `K_aa=1`. This is an imposed nonlinear saturation closure, not an exact
consequence of Gaussianity. No coefficient is chosen using labels,
fitted functions or endpoint errors.

The abstract surrogate equations are

\[
\dot c=-\alpha\sum_b r_bh_b,\qquad
\dot h_a=-\alpha\sum_b r_b\beta_{ab}D_aD_bc.      \tag{7}
\]

The vectors in (6)–(7) prove the finite Gram identities; the implementation
does not store them. This construction replaces the old moving-Gram
response law rather than claiming a perturbative correction to it. It
preserves the exact finite initial `K0`, and hence the initial zero-readout
training kernel, but **does not inherit the prior training or query cubic
response theorem**.

## Autonomous scalar equations

Store `r,K,q`, initially `(-y,K0,0)`, and put `f=y+r`.
The current approximate gate Gram is

\[
G_{ab}=s_as_b\left[q-\lambda_af_a^2-\lambda_bf_b^2
       +\lambda_a\lambda_b f_af_bK_{ab}\right],\qquad
N=\beta\odot G.                                  \tag{8}
\]

Indeed `D_a c=s_a(c-lambda_a f_a h_a)`, whose Gram is (8).
This retains the current readout–feature dependence through `f_a`, its
pairwise interaction through `K_ab`, and `q`; replacing it by a scalar
mean gate times `q` loses these terms.

For a fully explicit polynomial RHS define

\[
R_{ab}=\beta_{ab}s_as_b,\quad
z_a=r_a\lambda_af_a,\quad t=Rr,\quad u=-\alpha t,
\]
\[
A=\alpha\operatorname{diag}(z)R+
\operatorname{diag}\!\left(\alpha\lambda\odot
                  [f\odot t-(R\odot K)z]\right).                 \tag{9}
\]

Expanding `D_aD_b c` in (7) gives `Hdot=HA+c u^T`, where `H` has
columns `h_a`. Therefore

\[
\dot r=-\alpha(K+N)r,\qquad
\dot K=A^TK+KA+uf^T+fu^T,\qquad
\dot q=-2\alpha r^Tf.                               \tag{10}
\]

The consistency identity `A^T f+q u=-alpha N r` follows by substituting
(8)–(9). There is no division by `q`, so (10) is defined at zero readout.
No inverse of a changing Gram is needed.

## Exact surrogate properties and their limits

Let

\[
M=\begin{pmatrix}K&f\\f^T&q\end{pmatrix},\qquad
L=\begin{pmatrix}A&-\alpha r\\u^T&0\end{pmatrix}.
\]

Equations (9)–(10) give `Mdot=L^T M+M L`. A fundamental matrix therefore
represents `M` as a congruence of its positive semidefinite initial value.
Thus `M>=0`; (8) is a Gram and `N>=0`. It follows that

\[
\frac d{dt}\frac{\|r\|^2}{m}
=-\frac4{m^2}r^T(K+N)r\le0,
\qquad \dot q=-\frac4m r^Tf.                         \tag{11}
\]

Every term in `Kdot_aa` has factor `s_a`. Hence its initially positive
slack solves a scalar homogeneous linear equation and cannot vanish on a
finite interval with bounded coefficients. Positivity also gives
`K_aa>=0`, so `0<=K_aa<1`. The residual and `f` are bounded by (11),
`K` is bounded by its diagonals and positivity, and `q` grows at most
linearly on finite intervals because its derivative is bounded. The
polynomial RHS cannot have a finite-time escape. This proves global
finite-time existence of this surrogate, including initially singular
`M`. When `r=0`, every derivative vanishes.

There are two substantive limitations even before empirical comparison:

* `D_a` need not be positive or contractive. Although its derived `G` is
  positive semidefinite, the physical inequality `G_aa<=q` for a true tanh
  gate is **not** proved and can fail. The code reports this excess as a
  descriptive approximation diagnostic, not a numerical validity gate.
* For one training input, the initial zero-readout construction keeps
  `c=v h`. Then `D h=s(1-lambda K)h`, so
  `Kdot=-2 alpha r beta v K s^2(1-lambda K)^2`.
  The extra root `K=1/lambda=s0/2` creates a radial slowdown barrier
  unrelated to tanh saturation. A trajectory starting below this barrier
  cannot cross it in finite time while other coefficients stay bounded.
  Whether the training instances encounter a harmful analogue is open.
  This observation does not change the frozen coefficient.

Also, the initial augmented Gram has rank at most `m` and congruence
preserves this rank. The readout stays in the initial abstract training
feature span. Preserving current correlations does not restore all dense
feature directions. No physical gate-realizability theorem, global dense
approximation theorem or hierarchy convergence is asserted.

## Passive queries and aliases

For each initialized query `x`, store `k_a=<h_a,h_x>`,
`F=<c,h_x>` and `kappa=<h_x,h_x>`. Initial values are the exact initialized
cross Gram, zero output and exact initial diagonal. Supply only `beta_xa`
from (4), with the same initialized arrays, and set
`lambda_x=2/(1-kappa0)`.

Define

\[
R^x_a=\beta_{xa}(1-\kappa)s_a,\quad
t_x=\sum_aR^x_ar_a,\quad p_a=\alpha R^x_a z_a,
\]
\[
u_x=-\alpha t_x,\qquad
\eta_x=\alpha\lambda_x\left(Ft_x-\sum_aR^x_a z_a k_a\right).
\]

Expansion of (7) for this query gives `hdot_x=Hp+eta_x h_x+u_x c` and

\[
\dot k=A^Tk+uF+Kp+\eta_xk+u_xf,\qquad
\dot F=-\alpha r^Tk+p^Tf+\eta_xF+u_xq,
\]
\[
\dot\kappa=2(k^Tp+\eta_x\kappa+u_xF).              \tag{12}
\]

The query is passive: (12) never enters (10). Its enlarged feature–readout
Gram again has a congruence flow; `kappa` has the same slack factor. Thus

\[
0\le\kappa<1,\qquad |F|^2\le q\kappa\le q.        \tag{13}
\]

Each initialized query is globally bounded on finite intervals. With
`x=x_b`, the initial query coefficients equal the corresponding training
row and the equations coincide exactly; uniqueness gives
`k=K[:,b]`, `F=f_b` and `kappa=K_bb` for all times. This does not provide
a fixed-size decoder of the entire input function: `Q` queries cost
`Q(m+2)` dynamic scalars. No query–query state is required for these
per-query statements or predictions.

## Frozen implementation, cost and checks

Implementation: `current_projected_correlation.py`.
Constructor: `initialize_with_queries(w,W,inputs,labels,queries)` returns
the model directly. It uses `w@x`, without an extra input-dimension
scaling. Model methods: `initial_state`, `rhs`, `residual`, `predict`,
`diagnostics`, `readout_energy`, and `coefficient_dict`; fields include
`size`, `training_size`, `blocks`, and JSON-compatible `metadata`.
`from_coefficients(coeff_dict)` reconstructs the same scalar model for
numerical refinement without rerunning neural initialization.

Training coefficient storage is `O(m^2)` and passive coefficient storage
is `O(Qm)`: exact initial Gram, beta, query cross Grams/diagonals and beta
rows, with labels, slack and lambda arrays. The implementation retains
copied full training matrices, copied passive coefficients and triangle
index arrays; the dynamic state stores only one triangle. It retains no
`w`, `W`, hidden features or query inputs. One RHS costs `O(m^3+Qm^2)`
and uses `O(m^2+Qm)` working arrays. The diagnostic eigenvalue checks cost
more than the RHS and are not needed at every solver step.

Initialization is width dependent and disclosed: exact forward evaluation
costs `O((m+Q)n^2)` for the dense middle matrix, plus contraction costs
`O((m^2+Qm)n)` and input-layer products. The provided neural arrays remain
caller-owned. Computing column norms currently allocates a transient
`W*W` array of `n^2` entries; training forward arrays cost `O(mn)` and
queries use transient batches of at most 64 inputs. Constructor copies
temporarily coexist with the initializer's coefficient arrays. Those
transients disappear before the autonomous RHS runs. No width-independent
claim is made for coefficient construction.

`check_current_projected_correlation.py` compares the scalar RHS against
explicit finite-dimensional operators in (6)–(7), including passive
queries, and checks the realized beta trace, zero-readout flow, aliases,
energy, positive Grams/kernels and tangency at the saturation boundary.
After correcting the check's initial expectation that passive outputs
would also have zero derivative at zero readout, all checks passed.
The largest reported discrepancy was `2.22e-16`; the explicit operator
RHS discrepancy was `4.94e-17`. This correction changed only a test
expectation, not the frozen equations or implementation. No ODE was
integrated and no training experiment was run by this scoped agent.

The pending empirical discriminator is the predeclared three-case focus
comparison against the same dense endpoints, at each model's first MSE
0.001 crossing. The primary target is raw circle RMS at most 0.05 on both
hard cases. Passing the exact algebra checks only licenses this bounded
candidate test; it does not predict that outcome.
