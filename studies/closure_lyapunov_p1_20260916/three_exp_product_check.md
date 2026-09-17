# Readout-norm product bound: an explicit countersequence

2026-09-16. Bounded analytical check following the frozen independent
routes. No numerical work, other agent's findings, external sources, or
unassigned scientific inputs were used. The allowed additional source was
`generic3_stationary_geometry.md`; its signed-field notation and canonical
upper law are retained.

**Verdict:** for every `0<epsilon<ell<1/3`, the proposed inequality

\[
 A(1+\|c\|_2^2)\ge k(\epsilon,\ell)>0,
 \qquad A=\frac49\left\|\sum_{i=1}^3(1-m_i)V_i\right\|_2^2,
                                                               \tag{1}
\]

is false on the stated family of three signed tanh/sign fields with
positive margins and loss in `[epsilon,ell]`. A countersequence already
uses finite tanh fields with three pairwise nonparallel coefficient
vectors. The full hidden gradient is not controlled by this construction.
It defeats the proposed readout-only quantitative step, not the full
gradient inequality or the requested canonical-trajectory potential.

## 1. Fixed coefficients and limiting margins

Let `Z=(Z_1,Z_2)` have the canonical upper distribution: its coordinates
are independent copies of `tanh(sqrt(v_0)G)`, with `G` standard Gaussian.
Write

\[
       \tau=E[Z_1^2]=E[Z_2^2]>0,
       \qquad E[Z_1Z_2]=0,\qquad |Z_j|<1.
\]

Choose explicitly

\[
 E_*=(\epsilon+\ell)/2,
 \qquad b=\sqrt{\frac{3E_*}{2(1-E_*)}},
 \qquad k=\frac3{3+2b^2}=1-E_*.
                                                               \tag{2}
\]

Since `0<E_*<1/3`, one has `0<b<sqrt(3)/2<1` and `0<k<1`.
Define two three-vectors and three coefficient vectors by

\[
 a=(1-b,1,1+b),\qquad t=(1,-2,1),
 \qquad v_i=(a_i,t_i)\in\mathbb R^2.
                                                               \tag{3}
\]

All three coefficient vectors are nonzero and pairwise nonparallel:

\[
 \det(v_1,v_2)=2b-3,\qquad
 \det(v_1,v_3)=-2b,\qquad
 \det(v_2,v_3)=3+2b,
                                                               \tag{4}
\]

and none vanishes in the stated interval for `b`.

The limiting margins will be `m_i^*=ka_i`, which are strictly positive.
Their loss is exactly

\[
 \frac13\sum_i(1-ka_i)^2
 =1-\frac{(\sum_i a_i)^2}{3\sum_i a_i^2}
 =\frac{2b^2}{3+2b^2}=E_*.
                                                               \tag{5}
\]

Here `sum a_i=3`, `sum a_i^2=3+2b^2`, and `k` is their ratio.
If `e_i^*=1-ka_i`, the same identities give

\[
 \sum_i e_i^*a_i=3-k(3+2b^2)=0,
 \qquad
 \sum_i e_i^*t_i=0-k\{(1-b)-2+(1+b)\}=0.
\]

Therefore

\[
                         \sum_i e_i^*v_i=0.             \tag{6}
\]

This is the multiresidual cancellation. Positivity of all margins does
not prevent it. In fact the third limiting margin exceeds one, whereas
the first two are below one, so the residual coefficients have both signs.

## 2. Actual fields and readout

For `rho>0`, put

\[
 V_{i,\rho}=\tanh(\rho Z\cdot v_i),\qquad
 c_\rho=\frac{k}{\tau\rho}Z_1,
 \qquad m_{i,\rho}=E[c_\rho V_{i,\rho}].              \tag{7}
\]

These are allowed finite tanh fields in the compact upper family. Their
coefficient vectors remain pairwise nonparallel for every `rho>0`.
The readout is odd under simultaneous mark reversal and is bounded for
each fixed `rho`; its exact squared norm is

\[
                         \|c_\rho\|_2^2=\frac{k^2}{\tau\rho^2}.
                                                               \tag{8}
\]

Every margin in (7) is represented by the same actual readout, so the
corresponding Gram block with last entry `||c_rho||_2^2` is automatically
positive semidefinite. No artificial independent margin variables are used.

Here are explicit remainder bounds. For every real `x`,

\[
 |\tanh x-x|\le |x|^3/3.                              \tag{9}
\]

Indeed, integrate `1-sech^2 x=tanh^2 x<=x^2` from zero to `|x|`,
using oddness for the negative half-line. Let `W_i=Z.v_i`. By (3) and
`b<1`, `|W_i|<=3`. Write

\[
 V_{i,\rho}=\rho W_i+R_{i,\rho},
 \qquad |R_{i,\rho}|\le9\rho^3.
                                                               \tag{10}
\]

Because `E[Z_1W_i]=tau a_i`, substitution in (7) yields

\[
 m_{i,\rho}=ka_i+\Delta_{i,\rho},
 \qquad |\Delta_{i,\rho}|\le\frac{9k}{\tau}\rho^2.
                                                               \tag{11}
\]

Thus all three margins are positive for sufficiently small `rho`, and
their loss

\[
                  E_\rho=\frac13\sum_i(1-m_{i,\rho})^2
\]

converges to the strictly interior value `E_*`. Consequently
`epsilon<=E_rho<=ell` for every sufficiently small positive `rho`.
This verifies both constraints in the proposed inequality for the
entire tail of the countersequence.

## 3. Readout speed and the vanishing product

Let `e_{i,rho}=1-m_{i,rho}` and
`S_rho=sum_i e_{i,rho}V_{i,rho}`. Using (6), (10), and (11) gives

\[
 \begin{aligned}
 S_\rho
 &=\rho\sum_i(e_i^*-\Delta_{i,\rho})W_i
           +\sum_i e_{i,\rho}R_{i,\rho}\\
 &=-\rho\sum_i\Delta_{i,\rho}W_i
           +\sum_i e_{i,\rho}R_{i,\rho}.
 \end{aligned}                                                     \tag{12}
\]

For sufficiently small `rho`, (11) gives `|m_{i,rho}|<=3`, hence
`|e_{i,rho}|<=4`. Since `||W_i||_2<=3`, the first term in (12) has
norm at most `81k rho^3/tau`, and the second has norm at most
`108 rho^3`. In particular, with the fixed finite constant

\[
                         B=81k/\tau+108,
\]

one has the exact tail estimate

\[
              \|S_\rho\|_2\le B\rho^3,
 \qquad A_\rho=\frac49\|S_\rho\|_2^2
                       \le\frac49B^2\rho^6.             \tag{13}
\]

Combining (8) and (13) proves

\[
 0\le A_\rho(1+\|c_\rho\|_2^2)
 \le\frac49B^2\left(\rho^6+\frac{k^2}{\tau}\rho^4\right)
 \longrightarrow0.                                    \tag{14}
\]

There can therefore be no strictly positive `k(epsilon,ell)` in (1).
Every sufficiently small member of this sequence satisfies the required
positive margins, the stated fixed positive loss interval, the exact
canonical upper mark law, and pairwise nonparallel finite coefficients.

For comparison with the bounded-readout envelope, let `D_C(epsilon)`
be its minimum with norm bound `C`. Set `rho=k/(sqrt(tau) C)` in the
tail above. Then `||c_rho||_2=C` and (13) gives

\[
                     D_C(\epsilon)\le \mathrm{const}\, C^{-6}
\]

for all sufficiently large `C`, with constants depending only on the
fixed interval and the canonical upper law. This is an upper bound on
the best relaxed readout-speed envelope; it is not a claimed sharp rate.

## 4. Scope of the obstruction

The countersequence uses the current upper fields and an explicit current
readout only. It does not use future information, numerical quadrature,
or a time trajectory. Its limit features are all zero, while the readout
norm diverges and the margins remain positive. Thus ordinary compactness
of the feature family does not provide the proposed quantitative
readout-norm product bound.

No lower field or middle matrix realizing this entire sequence along
the prescribed initialized trajectory has been supplied. More importantly,
the hidden velocities and the full gradient have not been bounded here.
Their additional contribution to loss dissipation might prevent this
cancellation on an actual trajectory. The result therefore disproves
only the stated readout-speed product estimate on the relaxed feature
family. It neither disproves canonical convergence nor excludes a mixed
potential using the full hidden gradient or a reachable-state invariant.

Source freeze: `generic3_stationary_geometry.md` SHA-256
`170447ad239b991762fd4597a0a52318d04b9c4bad750ad95ca4c0e15dd777db`.
Checks included exact moment factors, all three determinants, positive
limiting margins, the interior limiting loss, cancellation of both
linear coefficient coordinates, and the uniform cubic remainder.
No experimental or numerical claim is made.
