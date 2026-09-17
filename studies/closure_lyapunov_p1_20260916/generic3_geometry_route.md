# Generic three-input geometry: initialized counterexample and exact replacements

Status: complete bounded analytical route, 2026-09-16. These are internally
derived results, not an independent review or established-book promotion.
No experiment, numerical integration, auxiliary agent or change to the model
was used. The scientific inputs used are `docs/NOTATION.md`,
`docs/global_nonlinear.md` C.4.7.9.3–4 and C.4.7.10 B/C.1/D.3,
`arbitrary_pair_local.md` Sections 1–4, and the initialization rank result in
`three_four_input_extension.md` Section 2. The required research-contract,
adversarial-audit and rigorous-math instructions were applied.

**Result.** An open set of equally weighted, distinct, non-antipodal circle
triples with labels `(+1,+1,-1)` has a strictly increasing same-class squared
hidden distance for all sufficiently small positive physical times, in
**both** hidden layers of the actual initialized canonical `p=1` population
closure. Universal monotone same-class attraction is therefore false.
This does not disprove eventual class organization or global fitting.

## 1. Exact target and derivative identities

Fix the exact order-one dictionary, its correlated Gaussian marks, the
ridge `eta=1/4096`, the prescribed Cholesky factors and `M(0)=D`,
`w(0)=g`, `c(0)=0`. The populations remain continuum populations and all
expectations are exact. Only three unit directions `u_i` and labels
`y=(1,1,-1)` vary; every sample has probability `1/3`. The physical loss is

\[
 \mathcal L=\frac13\sum_{i=1}^3(f_i-y_i)^2.
\]

Write the hidden state as `theta=(w,M)` in the constant metric
`L2(Omega_1;R2) x R^(3 x 5)`; the matrix metric is Frobenius. Set

\[
 h_i=\tanh(w\cdot u_i),\quad a_i=E_1[b_1h_i],\quad
 z_i=b_2^TMa_i,\quad H_i=\tanh z_i,\quad f_i=E_2[cH_i],
 \qquad s_i=1-h_i^2,\quad S_i=1-H_i^2.
 \tag{1}
\]

Let `J_i` denote the hidden-state derivative of `H_i`, with the adjoint
in this metric. Its exact formula, for `v in L2(Omega_2)`, is

\[
 \begin{split}
 J_i(\delta w,\delta M)
 &=S_i b_2^T\left[\delta M a_i
       +M E_1[b_1s_i(\delta w\cdot u_i)]\right],\\
 J_i^*v
 &=\left(s_i u_i b_1^TM^TE_2[b_2S_iv],
               E_2[b_2S_iv]a_i^T\right).
 \end{split}                                                    \tag{2}
\]

For example, pairing the first line with `v`, transferring the finite
matrix product to its transpose, and moving the lower expectation past
the finite coefficient pairing yields exactly the two terms in the second
line. Thus no unweighted particle metric or independent reverse action is
being used. The lower derivative is

\[
 P_i(\delta w,\delta M)=s_i(\delta w\cdot u_i),\qquad
 P_i^*v=(s_iv u_i,0).
 \tag{3}
\]

The actual closure equations become, with `r_i=f_i-y_i`,

\[
 \theta'=-\frac23\sum_i r_iJ_i^*c,\qquad
 c'=-\frac23\sum_i r_iH_i.
 \tag{4}
\]

For the squared upper distance `D^2_ij=||H_i-H_j||_2^2`, the exact
all-time derivative on this global fixed-order flow is

\[
 (D^2_{ij})'
 =-\frac43\sum_k r_k
 \left\langle (J_i-J_j)^*(H_i-H_j),J_k^*c\right\rangle.
 \tag{5}
\]

The superscript `2` labels the second hidden layer; `D^2_ij` is already
a squared distance. Formula (5) has no pairwise label sign: all residuals,
the common readout and both trainable hidden blocks contribute. Replacing
`J_i-J_j,H_i-H_j` by `P_i-P_j,h_i-h_j` gives the corresponding formula
for `D^1_ij=||h_i-h_j||_2^2`.

These differentiations are valid at initialization and on each bounded
time interval. At fixed order the feature marks are bounded. The vector
field is smooth on bounded sets of `w-g,c,M` in their supremum/matrix
norms, because all derivatives of the real tanh gate used here are bounded
and the remaining operations are finite products and probability
integrals. The given global fixed-order continuation bounds keep this
state bounded on each finite interval. This supplies the twice continuously
differentiable curves needed below; the unbounded frozen `g` enters only
inside bounded gates.

Define the signed aggregate and its hidden derivative

\[
 U(\theta)=\frac13\sum_i y_iH_i(\theta),\qquad
 J_U=\frac13\sum_i y_iJ_i.
 \tag{6}
\]

Every quantity on the right side of the following identities is evaluated
at the prescribed initialization:

\[
 \theta'(0)=0,\qquad c'(0)=2U_0,\qquad
 \theta''(0)=4J_U^*U_0.                                  \tag{7}
\]

Indeed `c(0)=0` kills the hidden velocity. Differentiating (4), every term
except the derivative of `c` still contains `c(0)`; using `r_i(0)=-y_i`
then gives (7). Consequently both initial distance derivatives vanish and

\[
 \begin{split}
 (D^2_{ij})''(0)
 &=8\left\langle (J_i-J_j)^*(H_i-H_j),J_U^*U_0\right\rangle,\\
 (D^1_{ij})''(0)
 &=8\left\langle (P_i-P_j)^*(h_i-h_j),J_U^*U_0\right\rangle.
 \end{split}                                                    \tag{8}
\]

The common-coupling terms in (8), rather than the two labels by themselves,
decide the initial geometry.

## 2. A canonical counterexample family, with both signs proved

The proof first evaluates an auxiliary coincident/antipodal limiting law,
then transfers a **strict** sign to admissible laws. No claim is based only
on the degenerate law.

Take temporarily

\[
 (u_1,y_1)=(e_1,+1),\quad
 (u_2,y_2)=(-e_1,+1),\quad
 (u_3,y_3)=(-e_1,-1).                                  \tag{9}
\]

At every hidden state, oddness in the input gives
`h(-e_1)=-h(e_1)`, `H(-e_1)=-H(e_1)` and also `J(-e_1)=-J(e_1)`.
Write `h=h(e_1)`, `H=H(e_1)`, `J=J(e_1)`. Then `U=H/3`, `J_U=J/3`,
and (7) becomes

\[
 \theta''(0)=\frac49J^*H.
 \tag{10}
\]

Since `D^2_12=4||H||_2^2`, (8) gives

\[
 (D^2_{12})''(0)=\frac{32}{9}\|J^*H\|^2>0.             \tag{11}
\]

Here the strict inequality needs verification in the exact initializer.
By `arbitrary_pair_local.md` Section 1,

\[
 k=\Phi(1)>0,\qquad Z_1=\tanh\xi_1,\qquad H=\tanh(kZ_1).
\]

The coefficient vector `a(e_1)` is nonzero: its pairing with the normalized
lower `tanh g_1` feature is a positive multiple of `E tanh^2 g_1`.
Likewise

\[
 d_H=E_2[b_2H(1-H^2)]\ne0,
\]

because its `Z_1/sqrt(tau+eta)` coordinate is the expectation of
`Z_1 tanh(kZ_1) sech^2(kZ_1)/sqrt(tau+eta)`, strictly positive outside
`Z_1=0`. The `M` component of `J^*H` is `d_H a(e_1)^T`, and its
Frobenius norm is `|d_H||a(e_1)|>0`. This proves (11) without assuming
anything about the lower component's sign.

For the first layer, more of the exact canonical initialization matters.
Use the scalar regression coefficients of `arbitrary_pair_local.md`
Section 1, renamed here `a_*` and `b_*` to distinguish them from the
coefficient vector in (1). On the first coordinate block let

\[
 X=\tanh g_1,\quad Y=\tanh(\zeta_1+\alpha X),\quad
 m(x)=E_{\zeta_1}\tanh(\zeta_1+\alpha x),\quad
 j(g)=a_*\tanh g+b_*m(\tanh g).
 \tag{12}
\]

Here `g_1` is standard Gaussian, `zeta_1` is an independent centered
Gaussian with variance `tau`, and

\[
 v_0=E\tanh^2G,\quad \tau=E\tanh^2(\sqrt{v_0}G),\quad
 \alpha=1-\tau,\quad r=E[XY],\quad \ell=E[Y^2],\quad
 \chi=E[1-Y^2],
\]
\[
 (a_*,b_*)=(\alpha v_0,\alpha r+\tau\chi)
 \left(\begin{pmatrix}v_0&r\\r&\ell\end{pmatrix}
                              +\eta I\right)^{-1}.
\]

These are the exact prescribed initialization contractions, with `G`
standard Gaussian and all variables in their indicated population.

The supplied complete analytic result proves that `j` is odd and
`j'(g)>0` for every finite `g`; no sign of `a_*` is assumed. Define

\[
 \gamma=\frac{E_2[Z_1\tanh(kZ_1)\operatorname{sech}^2(kZ_1)]}
                  {\tau+\eta}>0.
 \tag{13}
\]

For `B=U_2DU_1^*`, the actual initialized filtered action, set
`q_H=B^*[H(1-H^2)]`. Its exact reverse contraction is

\[
 q_H=\gamma(a_*X+b_*Y),\qquad
 E[q_H\mid g_1]=\gamma j(g_1).                           \tag{14}
\]

To check the normalization, the raw upper odd Gram is `tau I_2` and the
first upper contraction row is
`(alpha v_0,alpha r+tau chi)`. The raw expression for the adjoint is
`psi_1^T(G_1+eta I)^(-1) C^T(G_2+eta I)^(-1) E_2[psi_2 H(1-H^2)]`.
Only its upper `Z_1` entry is nonzero. Dividing that entry by `tau+eta`
gives (13), and applying the lower block inverse gives exactly
`(a_*,b_*)`. This proves (14), including the reverse-response term
already included in `b_*`.

The row component of (10) is therefore

\[
 w''(0)=\frac49\operatorname{sech}^2(g_1)q_H e_1.
\]

Since `D^1_12=4E_1 tanh^2(w dot e_1)` and `w'(0)=0`, two derivatives
and then conditioning in (14) yield

\[
 \begin{split}
 (D^1_{12})''(0)
 &=\frac{32}{9}E_1[X\operatorname{sech}^4(g_1)q_H]\\
 &=\frac{32\gamma}{9}
       E[X\operatorname{sech}^4(g_1)j(g_1)]>0.
 \end{split}                                                   \tag{15}
\]

All factors other than `Xj(g_1)` are strictly positive at finite `g_1`.
Oddness and strict increase of `j` show `Xj(g_1)>0` whenever `g_1!=0`;
the Gaussian has no atom at zero. The integrand is bounded and strictly
positive almost surely, which establishes the final strict sign.

Now replace (9) by the actual admissible family

\[
 u_1=e_1,\qquad
 u_2=(-\cos\varepsilon,\sin\varepsilon),\qquad
 u_3=(-\cos 2\varepsilon,-\sin 2\varepsilon),\qquad
 y=(1,1,-1).                                             \tag{16}
\]

For `0<epsilon<pi/6`, the three directions are pairwise distinct and
non-antipodal. The two curvatures in (8) depend continuously on the three
directions. To verify this rather than assume trajectory continuity,
use (1)–(3) at initialization. Their input-dependent gates converge
pointwise as the directions converge and are bounded. Their finitely many
mark contractions converge by dominated convergence. The lower adjoints
then converge in `L2` by bounded feature envelopes, and the matrix
components converge in Frobenius norm. The inner products in (8) therefore
converge as well. The fixed unbounded Gaussian appears only in the bounded
lower gates and creates no domination problem.

The strict signs (11) and (15) consequently imply that some
`epsilon_*>0` exists such that every `0<epsilon<epsilon_*` in (16) has

\[
 (D^1_{12})''(0)>0,\qquad (D^2_{12})''(0)>0.
 \tag{17}
\]

These signs also hold in an open neighborhood of each such triple; the
configuration space can be restricted to distinct non-antipodal triples
because that condition is open. Thus this is an open set of generic
triples, not just an exact symmetry case. For each of those triples,
continuity of the second derivatives and `(D^ell_12)'(0)=0` supply
`t_*>0` such that

\[
 (D^1_{12})'(t)>0,\qquad (D^2_{12})'(t)>0
       \quad(0<t<t_*).
 \tag{18}
\]

The same-label inputs therefore separate initially in both hidden layers
along their own actual initialized trajectories. The proof gives an
analytic existence family and an open robustness statement; it does not
give a numerical value for `epsilon_*` or `t_*`, and none is needed to
refute a universal monotonicity claim.

## 3. Useful exact replacements for pairwise attraction

First, the label-weighted upper aggregate satisfies the universal
initialized identity

\[
 \left.\frac d{dt}\|U(t)\|_2^2\right|_{t=0}=0,\qquad
 \left.\frac{d^2}{dt^2}\|U(t)\|_2^2\right|_{t=0}
          =8\|J_U^*U_0\|^2\ge0.                         \tag{19}
\]

Indeed `U'=J_U theta'` vanishes initially, and
`U''(0)=4J_U J_U^*U_0` by (7). Taking the second derivative of its squared
norm gives (19). It describes the initial hidden acceleration as ascent
of `||U||_2^2`, up to the positive constant in (7). A zero coefficient
does not determine higher orders, and (19) is not an all-time monotonicity
claim. For these unequal class counts,

\[
 U=\frac23\overline H_+ -\frac13\overline H_-;
\]

it is not a fixed multiple of the difference of the two unweighted class
means. This distinction prevents misinterpreting (19) as a class-mean
distance theorem.

Second, exact fitting requires observable separation of opposite labels,
without requiring monotonic distance growth. For any state and any
opposite-label pair, let

\[
 b_{ij}=(2-|r_i|-|r_j|)_+.
\]

The triangle inequality and Cauchy–Schwarz give

\[
 b_{ij}\le |f_i-f_j|
 \le\|c\|_2\|H_i-H_j\|_2
 \le\|c\|_2\|U_2MU_1^*\|_{\rm op}\|h_i-h_j\|_2.
 \tag{20}
\]

The last inequality uses `H_i=tanh((U_2MU_1^*)h_i)` and the
one-Lipschitz tanh gate. Whenever the denominators are positive, (20)
gives lower bounds on the two squared distances by
`b_ij^2/||c||_2^2` and
`b_ij^2/(||c||_2^2 ||U_2MU_1^*||op^2)`, respectively. If a denominator
vanishes, (20) itself says `b_ij=0`; division is unnecessary. At a finite
fitted state these bounds are strictly positive. Uniformly bounded
readout/action norms would also protect opposite-label separation along
an asymptotically fitted sequence. Without those norm bounds, (20) does
not supply a positive limiting distance.

For a same-label pair the exact relation is instead

\[
 E_2[c(H_i-H_j)]=r_i-r_j.                                \tag{21}
\]

Fitting sets one readout projection of the difference to zero; it does
not set the whole difference to zero. This is a statement about what
fitting implies, not a construction of another ambient-state trajectory.

Finally, the initialized Gram result in the assigned three-input source
gives `U_0!=0` for every admissible triple with these labels. Directly
from (4),

\[
 \mathcal L'(0)=-4\|U_0\|_2^2<0.
 \tag{22}
\]

Thus strict initial loss improvement coexists with the strict same-class
distance increase proved above. Monotone clustering is not necessary for
this initial improvement.

## 4. Frozen conclusion and exact gaps

The two mechanisms pursued were (i) the exact initialized distance
curvature and a strict counterexample obtained by continuity from a
calculable limiting law, and (ii) loss/readout identities as replacements
for pairwise geometry. Both have complete statements and proofs above;
no third mechanism or open-ended search is launched.

- **Proved:** equations (5), (7)–(8), (19)–(22), and an open set of actual
  canonical initialized generic three-input trajectories with early
  same-class separation in both hidden layers, (16)–(18).
- **Falsified:** universal monotone same-class attraction in either layer
  for the stated generic three-input class. No frozen-feature model,
  altered initialization, arbitrary stationary state or new metric enters
  this counterexample.
- **Not decided here:** monotone separation of every opposite-label pair;
  eventual same-class clustering under additional hypotheses; generic
  unit-label fitting as `t -> infinity`; all-time readout/action bounds;
  convergence of the full state.
- **No inference across limits:** these results concern the exact fixed
  `p=1` population closure. They add no long-time or arbitrary-law
  identification with the original infinite-width Gaussian action model.

The counterexample removes universal pairwise attraction as an available
mechanism for a generic three-input convergence proof. It does not remove
other possible convergence mechanisms, and (19) alone cannot replace the
missing all-time multi-residual estimate.
