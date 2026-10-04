# Bounded moving Gram and exact readout energy

2026-09-30. Scoped theoretical candidate and implementation, frozen before
any training run of this candidate. Internally checked, unreviewed; not
established book material. Source scope was the kernel route, cubic scalar
implementation, cubic circle results, and current notation contract. No
other candidate route or study was read. Required research and rigorous
mathematics skills were applied.

**Conclusion.** A symmetric training Gram and the training residual give an
autonomous model with `m+m(m+1)/2` training scalars. It has a positive kernel,
nonincreasing training loss, bounded feature Gram diagonals, and the exact
readout-energy identity. Every initialized passive query then obeys
`|f(x)| <= sqrt(q)`, and training aliases agree exactly. This is a coherent
change to the training dynamics, rather than final-output clipping.

There is a material limitation: the training cubic response is preserved,
but one arbitrary-query cubic term is projected onto the initial training
feature span. Its discarded component is identified explicitly below.
The model is therefore a new candidate for the circle diagnostic, **not a
repair that inherits the previous whole-input cubic theorem**. A query
requires `m+1` passive dynamic scalars; this is not a fixed-size decoder of
the complete input function.

## 1. Contract and fixed coefficients

Use the original zero-readout, two-hidden-layer tanh setting. The residual
is `r=f-y`, the mean squared loss is `||r||^2/m`, and `alpha=2/m`.
The fixed initial feature Gram `K0` and response Gram
`S0[(a,e),(c,f)]` are exactly those of Sections 3--5 of
`KERNEL_SCALAR_ROUTE_20260930.md`. Assume `K0` is positive definite and
`K0_aa<1`. These conditions are directly checkable, and the second holds
for finite tanh preactivations.

The model receives only those fixed scalar contractions and the labels.
It keeps no initialized or evolving neurons, weights, histograms,
populations, quadrature nodes, or reference trajectory. Static storage is
`O(m^4)`, and runtime training state is `O(m^2)`.

For an initialized passive query `x`, additionally supply

\[
k_{0,x,a}=\langle H_x,H_a\rangle,\quad
\kappa_{0,x}=\langle H_x,H_x\rangle<1,\quad
S^x_{ecf}=S_0[(x,e),(c,f)].
\]

The initial augmented feature Gram must be positive semidefinite; this is
automatic when the coefficients come from the same initialized network.
There are `m^3+m+1` static coefficients and `m+1` evolving scalars per
query. Query states never enter the training vector field.

## 2. Closed training equations

Evolve the symmetric matrix `K` and residual `r`, initialized by
`K(0)=K0`, `r(0)=-y`. Calculate the following quantities from current state:

\[
\begin{aligned}
f&=y+r,&
g_a&=\frac{1-K_{aa}}{1-K_{0,aa}},\\
A&=KK_0^{-1},&
w&=K_0^{-1}f,\\
T_{ea}&=-\alpha g_a\sum_{cf}r_c g_c w_f
                  S_0[(a,e),(c,f)],&
C&=K_0^{-1}T,\\
N_{ac}&=g_a g_c\sum_{ef}w_e w_f S_0[(a,e),(c,f)].
\end{aligned}                                                     \tag{1}
\]

The ODE is

\[
\dot r=-\alpha(K+N)r,\qquad
\dot K=KC+C^TK.                                          \tag{2}
\]

Only the upper triangle of `K` is stored. The identity `w=A^T v`, where
`v=K^{-1}f`, lets the vector field avoid inversion of the evolving `K`.
An evolving inverse is required only for prediction or energy evaluation.
The static inverse `K0^-1` has the same conditioning qualification as in
the previous cubic model.

The matched ablation sets every gate `g_a=1` and every query gate below to
one; all other equations and coefficients remain identical. Both variants
have exact energy and Gram positivity. Only the gated variant has a
feature-diagonal bound. No coefficient or gate parameter is fit to a
trajectory or selected from test predictions.

## 3. Positivity, diagonal bounds, energy, and stopping

The matrix `N` is positive semidefinite because, for any `b in R^m`,

\[
b^TNb=\sum_{ae,cf}(b_a g_a w_e)
 S_0[(a,e),(c,f)](b_c g_c w_f)\ge0.                     \tag{3}
\]

The matrix equation in (2) is a congruence flow: if `R'=RC`, `R(0)=I`,
then `K=R^T K0 R`. Thus `K` remains positive definite while the solution
exists. Consequently

\[
\frac{d}{dt}\frac{\|r\|^2}{m}
=-\frac{4}{m^2}r^T(K+N)r\le0.                         \tag{4}
\]

Each diagonal derivative `Kdot_aa=2(AT)_aa` has the factor `g_a`, hence
the slack `1-Kaa` obeys a scalar homogeneous linear equation with its
initial positive value. The diagonal cannot reach one at finite time
when the other coefficients remain bounded.

These facts also give global existence of the training model. Until any
putative finite failure, the residual is bounded by (4), the prediction
`f=y+r` is bounded, `K` is bounded by its positive diagonal bounds, and
`g`, `w`, `T`, and `C` are bounded. The congruence fundamental matrix and
its inverse then stay finite on that finite interval, so the smallest
eigenvalue cannot reach zero. The slack equation cannot reach zero either.
There is no finite-time escape or boundary failure.

Define the surrogate readout coefficients and energy by

\[
v=K^{-1}f,\qquad q=f^TK^{-1}f=v^TKv.                    \tag{5}
\]

Equation (1) gives `T^T w=-alpha N r`. Differentiate `f=Kv` using (2):

\[
\dot v=-\alpha r-Cv.                                  \tag{6}
\]

Indeed `(KC+C^TK)v+K(-alpha r-Cv)` is
`-alpha Kr+C^T f=-alpha(K+N)r`. Therefore

\[
\dot q=2v^TK\dot v+v^T\dot K v
       =-2\alpha r^Tf=-\frac4m\sum_a r_a f_a.           \tag{7}
\]

This is exactly the dense readout-energy identity, now an internal identity
of this model. It does not identify its numerical energy with the dense
trajectory's energy. When `r=0`, all training and passive-query derivatives
vanish. Neither energy nor training loss establishes dense test fidelity.

## 4. Passive queries, their bound, and training aliases

For each query evolve a column `k_x in R^m` and scalar `kappa_x`, initialized
by its initial cross Gram and diagonal. Define

\[
g_x=\frac{1-\kappa_x}{1-\kappa_{0,x}},\qquad
(T_x)_e=-\alpha g_x\sum_{cf}r_c g_c w_f S^x_{ecf}.       \tag{8}
\]

The query equations and output are

\[
\begin{aligned}
\dot k_x&=C^Tk_x+A T_x,\\
\dot\kappa_x&=2k_x^TK_0^{-1}T_x,\\
\widehat f_x&=k_x^TK^{-1}f.
\end{aligned}                                                     \tag{9}
\]

The augmented matrix and generator

\[
\mathcal K_x=\begin{pmatrix}K&k_x\\k_x^T&\kappa_x\end{pmatrix},
\qquad
\mathcal C_x=\begin{pmatrix}C&K_0^{-1}T_x\\0&0\end{pmatrix}
\]

satisfy `Kcal_dot=Kcal Ccal+Ccal^T Kcal`. Thus the augmented Gram remains
positive semidefinite. The query diagonal derivative contains `g_x`, so
its slack remains positive by the same argument as for training. Its
Schur inequality yields

\[
k_x^TK^{-1}k_x\le\kappa_x<1,
\qquad |\widehat f_x|^2\le q\,\kappa_x\le q.            \tag{10}
\]

The query states remain globally bounded by their positive semidefinite
Gram and diagonal bound. These are dynamic geometric bounds; no output
clipping is used. In the ungated ablation the first inequality remains,
but `kappa_x` need not stay below one.

At `x=u_b`, the initial values are `k_x=K0[:,b]`,
`kappa_x=K0_bb`, and `S^x=S0[(b,·),(·,·)]`. Substitution in (8)--(9)
gives exactly the equations for `K[:,b]` and `Kbb`; uniqueness preserves
these identities. The prediction is consequently `f_b=y_b+r_b` exactly.

## 5. What cubic consistency does and does not survive

Scale labels by amplitude `a` and work in the original small-response
regime, where the cumulative residual has size `O(a)`. Let `z`, `J`, and
`M` be the original route's response integrals and feature cross Gram.
Then the leading terms of (1) are

\[
w=-\alpha z+O(a^3),\quad A=I+O(a^2),\quad
g_a=1+O(a^2),\quad T=\dot M+O(a^4\text{ per unit time}).
\]

Equivalently, for residual-controlled expansions the last defect is
`O(R^3 ||r||)` and integrates to `O(R^4)`. Hence

\[
K=K_0+M+M^T+O(a^4),\qquad
N_{ac}=\alpha^2\sum_{ef}z_ez_f S_0[(a,e),(c,f)]+O(a^4).
                                                                    \tag{11}
\]

Thus the training kernel agrees with the original cubic kernel through
quadratic response, and the training output has the same cubic response.
This observation is a local response statement; it is not a fresh proof
of a uniform-in-time error theorem for the candidate.

At a general query, (9) replaces the second-index-query contraction
`S0[(a,x),(c,f)]` by

\[
\sum_e(k_{0,x}^TK_0^{-1})_e S_0[(a,e),(c,f)].            \tag{12}
\]

The reason is structural: the readout is kept in the moving span of the
training features. Define the discarded initialization contraction

\[
E_{x;acf}=S_0[(a,x),(c,f)]
-\sum_e(k_{0,x}^TK_0^{-1})_eS_0[(a,e),(c,f)].            \tag{13}
\]

If `P_{a;cf}=integral r_a J_cf` denotes the original third response
integral, the resulting leading query discrepancy is

\[
\widehat f_x-f_{\rm cub}(x)
=\alpha^3\sum_{acf}P_{a;cf}E_{x;acf}+O(a^5).            \tag{14}
\]

The sign comes from replacing the term
`-alpha^3 sum P S0[(a,x),(c,f)]` in the original decoder. All the other
query cubic contractions agree at this order. The difference vanishes at
training aliases because the projection row then selects the matching
training index. It need not vanish elsewhere. It must not be advertised
as a higher-order correction, hidden in an error bound, or repaired by
silently deleting the old decoder term.

## 6. Frozen implementation and checks

Implementation: `cubic_bounded_gram_repair.py`.

```python
query = GramQueryCoefficients(k0x, K0xx, query_B)
model = BoundedGramModel(labels, K0, S, query, gated=True)
state0 = model.initial_state()
# model.rhs(t, state), model.residual(state), model.predict(state)
# model.blocks, model.size, model.training_size
```

Here `query_B[q,e,c,f] = S0[(query_q,e),(train_c,f)]`; it is the `B`
slice formed during the existing cubic query initializer, not the full
four-term decoder tensor. Both that slice and `K0xx` require only
initialization contractions. No new initial neural derivatives are needed.

The standalone script executes algebraic checks only. For synthetic
positive Gram data, both variants gave energy derivative error
`2.78e-17`, zero training-alias prediction error, alias derivative error
`2.22e-16`, and no negative tangent-kernel eigenvalue. These checks do not
integrate the ODE, validate dense fidelity, or establish numerical
invariance for a particular adaptive solver. Roundoff can violate an
exact geometric invariant, so endpoint checks must include minimum Gram
and kernel eigenvalues, maximum diagonals, query Schur excess, and energy
bound excess. No training experiment was run by this scoped subagent.

## 7. Status and discriminator

Exact internal properties: autonomous closure, `O(m²)` training state,
query independence, positive training kernel, exact energy identity,
bounded gated feature diagonals, bounded query outputs, and exact aliases.

Local consistency: the training cubic response is retained; the precise
arbitrary-query cubic defect is (13)--(14). The state budget and coefficient
provenance are satisfied, but full-function compression has been relaxed
to separately initialized passive queries for this diagnostic.

Open empirical question: whether bounded feature geometry and consistent
readout transport repair the difficult circle shapes. The clean comparison
is the frozen gated construction against its otherwise identical ungated
ablation, the original cubic model, and the same dense endpoints. Failure
to improve can arise from the projected readout closure or from incorrect
feature geometry; it would reject this witness rather than all energy
closures. An apparent improvement with a violated positive-Gram or energy
bound gate is numerically inconclusive.
