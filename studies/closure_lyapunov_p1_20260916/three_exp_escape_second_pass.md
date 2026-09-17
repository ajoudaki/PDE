# Three-input escape route, second pass: necessary geometry of persistent escape

This second pass was developed only after `three_exp_escape.md` was frozen at
SHA-256 `21788168510295cb46998f28ba339bd08039f614d5fed4aa6b06be2cd2bd09b9`.
The supervisor then supplied the idea of combining the readout radial
identity with the fact that, away from zero and opposite signed fields,
readout stationarity forces the **sum** of signed residuals to vanish
even when individual margins cannot be passed through an unbounded
readout. The results below are post-freeze consequences of that input,
not independent initial discoveries.

The model, scientific source scope, and source hashes are unchanged from
that frozen file. References below to Section 4 or equation (11) mean
that first-pass file. The only additional input was the supervisor's
stated radial-balance idea; no other route's derivation was used. No
experiment or external theorem is used. This file is separate so that
the frozen first pass remains a stable input to its independent audit.

Write `V_i=y_i H_i`, `m_i=y_i f_i`, `alpha_i=1-m_i`, and
`bar alpha=(alpha_1+alpha_2+alpha_3)/3`. Then

\[
 c'=\frac23\sum_i\alpha_i V_i,\qquad
 q':=\frac d{dt}\|c\|_2^2
       =4(\bar\alpha-\mathcal L),\qquad
 \mathcal L=\frac13\sum_i\alpha_i^2.                 \tag{13}
\]

Indeed `2<c,c'>=(4/3)sum alpha_i m_i`, and
`alpha_i m_i=alpha_i-alpha_i^2`. Since `L<=1`,
`bar alpha<=sqrt(L)<=1`.

Let `K` be the compact `L2(Omega_2)` closure of all fields
`tanh(Z dot v)`. The supplied stationary-geometry source proves directly
that its elements are finite tanh ridges or saturated sign ridges, that
this closure is compact, and that at most three nonzero fields in it are
independent after grouping equal/opposite fields. Define the closed
compact bad subset of `K^3` by

\[
 B=\{(V_1,V_2,V_3):\text{some }V_i=0
                         \text{ or some }V_i=-V_j,\ i\ne j\}.
\]

The distance below is the product `L2` distance, for example the maximum
of the three component distances. No parameter coefficient norm is used.

**Proposition 5.** If the actual trajectory has limiting loss
`ell=lim_(t->infinity)L(t)>0`, then for every `epsilon>0`,

\[
 \liminf_{T\to\infty}\frac1T
 \left|\{t\in[0,T]:\operatorname{dist}((V_i(t))_i,B)<\epsilon\}\right|
                         \ge\ell.                    \tag{14}
\]

Thus persistent positive loss forces positive asymptotic time occupation
of every neighborhood of the zero/opposite signed-feature strata. This
holds whether or not the trajectory ever enters `L<1/3`.

**Proof.** Fix `0<a<ell`. On the compact set

\[
 \{(V,\alpha):V\in K^3,\operatorname{dist}(V,B)\ge\epsilon,
              \sum_i\alpha_i^2\le3,\ \bar\alpha\ge a\},
\]

the continuous function `||(2/3)sum alpha_i V_i||_2` has a positive
minimum `gamma`, unless this set is empty. To prove positivity, a zero
would give a linear relation among nonzero fields without opposite
pairs. Grouping equal fields and using the supplied independence result
forces every group coefficient sum to vanish. Their total is
`sum alpha_i=0`, contradicting `bar alpha>=a`. If the set is empty,
the good-geometry/high-mean event considered below is empty as well.

The energy identity `integral_0^infinity ||c'||_2^2<=1` therefore bounds
the total measure of times satisfying both good geometry
`dist(V,B)>=epsilon` and `bar alpha>=a` by `1/gamma^2`.
On the other hand, integrating (13), using `q(0)=0`, `q(T)>=0`, and
`L(t)>=ell`, gives

\[
                      \int_0^T\bar\alpha(t)dt\ge\ell T.
\]

For `E_a={t:bar alpha(t)>=a}`, its upper bound `bar alpha<=1` implies

\[
 \ell T\le aT+(1-a)|E_a\cap[0,T]|,
 \qquad
 |E_a\cap[0,T]|\ge\frac{\ell-a}{1-a}T.
\]

All but a bounded measure of these times have `dist(V,B)<epsilon`.
Dividing by `T`, taking the lower limit, and then sending `a` down to
zero proves (14). The constants may depend on `a,epsilon` and the
fixed geometry; this is harmless because `T` tends to infinity first. ∎

The next refinement uses the existing low-loss compactness argument but
weakens its readout hypothesis from uniform boundedness to one bounded
return sequence.

**Proposition 6.** If the trajectory has once reached `L<1/3` and

\[
                     \liminf_{t\to\infty}\|c(t)\|_2<\infty,
\]

then `L(t)->0`. Equivalently, after such entry a positive limiting loss
would require `||c(t)||_2 -> infinity`, not merely an unbounded limsup.

**Proof.** Suppose there are times `t_n->infinity` with `||c(t_n)||_2<=R`.
The readout equation gives

\[
 \|c'(t)\|_2\le\frac23\sum_i|r_i(t)|\le2\sqrt{\mathcal L(t)}\le2.
\]

Consequently `||c(t)||_2<=R+2` on `[t_n,t_n+1]`. Energy integrability
allows a time `s_n` in this interval with `||c'(s_n)||_2->0`, since the
integral over the entire tail tends to zero. Along a subsequence the
three signed fields converge strongly in `L2`, and the bounded margins
converge as scalars. Let `L(t_0)=ell_0<1/3`. Then for all later times
`m_i>=1-sqrt(3ell_0)>0`.

At the times `s_n`, boundedness of `c` excludes a zero limiting field
and an opposite pair, using respectively
`|m_i|<=||c|| ||V_i||` and
`|m_i+m_j|<=||c|| ||V_i+V_j||`. Equal limiting fields give equal limiting
margins using the corresponding difference bound. Passing to the limit
in `c'=(2/3)sum(1-m_i)V_i` is now legitimate: it is a finite sum of
strongly convergent fields with convergent scalar coefficients.
Grouping equal fields and applying independence forces every limiting
margin to be one. Thus the loss along `s_n` tends to zero, and
monotonicity gives the same conclusion along the full trajectory. ∎

**Discrete alternatives when the readout has bounded returns.** The same
argument, without the `L<1/3` premise, gives the sharper classification

\[
 \liminf_{t\to\infty}\|c(t)\|_2<\infty
 \quad\Longrightarrow\quad
 \mathcal L_\infty\in\{0,\tfrac13,\tfrac23,\tfrac89\}.
                                                               \tag{15}
\]

To verify every alternative, use the same bounded-readout/vanishing-gradient
subsequence as in Proposition 6. A zero limiting field has limiting margin
zero. Group all nonzero limiting fields modulo sign. In a group of size
`n=n_++n_-`, choose one representative field `F`; its margins are `s_i a`
with `s_i=+1` or `-1`. This follows from bounded readout and strong field
convergence, without requiring a readout limit. Readout stationarity and
independence of the group representatives give

\[
 \sum_{i\text{ in group}}s_i(1-s_i a)=0,
 \qquad a=\frac{n_+-n_-}{n}.
\]

That group's contribution to the unhalved three-sample loss is exactly

\[
 \frac13\sum_{i\text{ in group}}(s_i a-1)^2
       =\frac13\left(n-\frac{(n_+-n_-)^2}{n}\right)
       =\frac{4n_+n_-}{3n}.                           \tag{16}
\]

Each zero field contributes `1/3`. A group with only one sign contributes
zero. A two-member opposite group contributes `2/3`. A three-member
mixed-sign group contributes `8/9`. Enumerating partitions of the three
indices therefore gives exactly the possible values
`0,1/3,2/3,8/9,1`. The last is excluded for the initialized trajectory by
its strict loss decrease (11). This is only a necessary classification;
it does not assert that the prescribed trajectory realizes any positive
listed value.

Neither proposition supplies repulsion from the bad set. The strict-saddle
direction in Section 4 can lose its quantitative strength through an
unbounded row right inverse or saturation of the ridge derivative; in
addition, a Hessian direction alone does not identify the sign of its
coordinate along the prescribed solution. The remaining positive-loss
branch below `1/3` is now more precise: the readout must diverge to
infinity, while the trajectory spends at least a fraction `ell` of time
arbitrarily near incompatible signed-feature strata. Its exclusion still
needs a new dynamical invariant or inequality.
