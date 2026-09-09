# Typed Renormalization and Width-Regularity Audit

## Verdict

A colored Wick/response calculus can be made exact for every fixed
expression. It has a stable syntax at arbitrary depth and correctly retains
source color, orientation, equality patterns, tail sector, and response
ports. It does not provide a completion theorem.

The decisive failure is absence of subcritical width homogeneity.
Forward/transpose return words of arbitrary length remain order one after
natural Wick counterterms. Width renormalization therefore produces no
truncation tail. In addition, the initially proposed normalized-energy
product and ambient local-stability estimates are false: a one-row tangent
sees a curvature multiplier of order \(\sqrt{\log n}\).

Typed renormalization is retained as a finite-expression compiler and
classified **KILL as an easier compact-time completion**.

## 1. Exact typed width calculus

Let \(\varepsilon=n^{-1/2}\). A symbol records

\[
\tau=(\mathcal G,o,\pi,\mathbf c,\mathbf s),
\]

where \(\mathcal G\) is an indexed expression graph, \(o\) is its output
port, \(\pi\) is its equality partition, \(\mathbf c\) records persistent
source colors and orientations, and \(\mathbf s\) records tail and response
sectors.

The constructors are:

- coordinatewise multipliers;
- \(\Gamma_l\) and the reverse orientation of the same source
  \(\Gamma_l^T\);
- normalized scalar contractions;
- activation jets;
- normalized rank-one updates;
- Malliavin/source-response ports.

For a fully contracted Wick branch \(P\), let \(I(P)\) be its number of free
internal neuron-index classes, \(E_\Gamma(P)\) its number of standardized
matrix atoms, and \(A(P)\) its number of explicit \(n^{-1}\) factors. The
exact width valuation is

\[
n^{I(P)-E_\Gamma(P)/2-A(P)}
=\varepsilon^{h(P)},\qquad
h(P)=E_\Gamma(P)+2A(P)-2I(P).                                     \tag{1}
\]

Negative \(h\) denotes an unrenormalized divergent contraction, \(h=0\) a
leading response, and positive \(h\) a width-deficient term. Counterterms
are exact conditional Gaussian contractions that preserve color,
orientation, and equality data.

For polynomial source expressions, the renormalization is the colored Wick
forest map

\[
M\tau=\sum_{F\in\mathcal F(\tau)}
(-1)^{|F|}\left(\prod_{H\in F}C_H\right)\tau/F.                    \tag{2}
\]

Equation (2) is exact finite-expression normal ordering. It does not state
that the centered result is small.

## 2. Tail and response sectors: what is valid

A useful family distinguishes disorder moments from empirical coordinate
moments:

\[
\|F\|_{\Psi_s^{(q)}}
=\sup_{p\ge2}p^{-s/2}
\left(
\mathbb E\langle |F|^q\rangle_n^{p/q}
\right)^{1/p}.                                                     \tag{3}
\]

If \(q^{-1}=q_1^{-1}+q_2^{-1}\), Hölder gives the typed rule

\[
\|FG\|_{\Psi_{s+t}^{(q)}}
\lesssim
\|F\|_{\Psi_s^{(q_1)}}\|G\|_{\Psi_t^{(q_2)}}.                     \tag{4}
\]

Products in empirical \(L^2\) therefore need empirical \(L^4\) input unless
one factor is coordinatewise bounded. The simpler global-energy norm

\[
\sup_{p\ge2}p^{-s/2}
\left(\mathbb E\|F\|_{2,n}^p\right)^{1/p}
\]

has no product rule. Deterministically,

\[
F=G=\sqrt n\,e_1,\qquad
\|F\|_{2,n}=\|G\|_{2,n}=1,\qquad
\|F\odot G\|_{2,n}=\sqrt n.                                      \tag{5}
\]

This corrects an earlier conflation of the two norms.

A possible response-jet scale is

\[
\|F\|_{\rho,\sigma,s}
=\sum_{r\ge0}\frac{\rho^r}{(r!)^\sigma}
\sup_{p\ge2}p^{-(s+\kappa r)/2}\|D^rF\|_{L^p}.                    \tag{6}
\]

Faà di Bruno and (4) give formal typed composition rules with explicit loss
of radius and tail sector. If one could prove

\[
\|D^rF\|_2\le M\rho^{-r}(r!)^\sigma,                              \tag{7}
\]

then optimizing the derivative order gives the computable chaos tail

\[
\|(I-P_{\le Q})F\|_2
\le M\exp[-c_{\sigma,\rho}Q^{1/(2\sigma)}].                       \tag{8}
\]

For \(\sigma=1\), (8) has the root-exponential scale needed by arctangent.
The unresolved issue is uniform propagation of (7), not the tail deduction
from it.

No universal same-space chaos product can be used. For normalized Hermites,

\[
h_m^2=\frac{\sqrt{(2m)!}}{m!}h_{2m}+\cdots,
\qquad
\frac{\sqrt{(2m)!}}{m!}\sim\frac{2^m}{(\pi m)^{1/4}}.              \tag{9}
\]

The exponential top coefficient defeats every diagonal root-exponential
Hilbert algebra.

## 3. Exact depth-two calibration

At initialization, write

\[
x=\phi(u),\quad z=\Gamma x,\quad
g=A\phi'(z),\quad d=\phi'(u)^2,\quad
q_x=\langle x,x\rangle_n .
\]

Direct differentiation of the trained flow gives

\[
\boxed{
\dot z=q_xg+\Gamma M_d\Gamma^Tg.
}                                                                  \tag{10}
\]

The second term is the first reused forward/transpose response. Let
\(\Gamma_{ij}=\xi_{ij}/\sqrt n\) and

\[
f_j=d_j(\Gamma^Tg)_j,\qquad
\delta_i(f)=\sum_j(\xi_{ij}f_j-\partial_{\xi_{ij}}f_j).
\]

Since \(d\) is independent of \(\Gamma\) at initialization and
\(g=A\phi'(\Gamma x)\), direct differentiation gives

\[
\boxed{
(\Gamma M_d\Gamma^Tg)_i
=\frac1{\sqrt n}\delta_i(f)
+\langle d,\mathbf1\rangle_ng_i
+\frac{A_i\phi''(z_i)}n[\Gamma(d\odot x)]_i .
}                                                                  \tag{11}
\]

The middle term is the exact transpose-contraction counterterm and the last
term is the activation response. No source has been refreshed.

The undifferentiated term has the valid global-energy bound

\[
\|\Gamma M_d\Gamma^Tg\|_{2,n}
\le\|\Gamma\|_{\rm op}^2\|g\|_{2,n},                              \tag{12}
\]

because \(d\) is bounded. This is not a response-jet estimate and says
nothing about coordinatewise products with the unbounded last multiplier in
(11).

Wick centering also does not make the response small. If \(d=1\),
\(g\) is independent standard Gaussian, and \(S=\Gamma\Gamma^T\), then

\[
\mathbb E\frac1n\|(S-I)g\|_2^2
=\mathbb E\,\tau_n((S-I)^2)=1+\frac1n.                            \tag{13}
\]

The first centered return is already leading.

## 4. Exact depth-three alternating cap

At initialization set

\[
d_1=\phi'(u)^2,\qquad e_2=\phi'(z_2),\qquad
b_3=A\phi'(z_3),\qquad b_2=e_2\Gamma_2^Tb_3.
\]

With \(q_l=\langle x_l,x_l\rangle_n\), the exact forward derivatives are

\[
\dot z_2=q_1b_2+\Gamma_1M_{d_1}\Gamma_1^Tb_2,
\]

and

\[
\boxed{
\begin{aligned}
\dot z_3={}&q_2b_3
+q_1\Gamma_2M_{e_2^2}\Gamma_2^Tb_3\\
&+\Gamma_2M_{e_2}\Gamma_1M_{d_1}
\Gamma_1^TM_{e_2}\Gamma_2^Tb_3 .
\end{aligned}
}                                                                  \tag{14}
\]

The last term is the leading alternating
\(\Gamma_1/\Gamma_1^T\) response enclosed by a \(\Gamma_2\) cap. It is not
a laminar one-color tree. Its undifferentiated energy is bounded by current
operator norms and \(\|A\|_{2,n}\), but differentiation introduces
unbounded diagonal curvature multipliers.

In the constant-diagonal specialization,

\[
B=\Gamma_2\Gamma_1\Gamma_1^T\Gamma_2^T,
\]

and

\[
\mathbb E\frac1n\|BA\|_2^2
=\mathbb E\,\tau_n(B^2)\ge
\mathbb E(\tau_nB)^2\ge1.                                        \tag{15}
\]

The multi-color cap is leading, not a renormalization remainder.

## 5. Corrected ambient-stability audit

At depth two,

\[
D_zb_2[\delta z]
=A\odot\phi''(z)\odot\delta z,
\]

so

\[
\|D_zb_2\|_{\ell_n^2\to\ell_n^2}
=\max_i|A_i\phi''(z_i)|.                                         \tag{16}
\]

At initialization, a positive fraction of the independent Gaussian
\(z_i\)'s lie in an interval on which \(|\phi''|\) is bounded below. The
maximum of the corresponding independent \(|A_i|\)'s is order
\(\sqrt{\log n}\). Hence

\[
\|D_zb_2\|_{\rm op}\gtrsim\sqrt{\log n}                            \tag{17}
\]

with high probability.

This is realized by a bounded parameter perturbation. With
\(x=\phi(u)\), choose

\[
\delta\Gamma
=\frac{\sqrt n\,e_ix^T}{\|x\|_2^2}.
\]

Then

\[
\|\delta\Gamma\|_{\rm op}=O(1),\qquad
\delta z=\sqrt n\,e_i,\qquad |\delta z|_n=1,
\]

and the output of (16) has normalized size
\(|A_i\phi''(z_i)|\). Thus the divergence is not caused by enlarging the
field space artificially.

The mixed state-size ball also permits \(A=\sqrt n\,e_i\), for which
\(\|A\|_{2,n}=1\) but \(\|A^2\|_{2,n}=\sqrt n\). Therefore:

- a dimension-uniform ambient bound on \(DF\) is false;
- a uniform ambient local Euler remainder does not follow;
- ambient Grönwall accumulation is false.

What survives is the triangular compact-time bound on state size. A local
\(O(h^2)\) defect can also be verified at initialization in the actual flow
direction by finite Gaussian peeling. For example, if
\(\dot z=LA\) with \(L\) conditionally independent of \(A\), then

\[
\mathbb E_A\|A\odot LA\|_{2,n}^2
=\frac1n\sum_i
\bigl(\|\operatorname{row}_iL\|_2^2+2L_{ii}^2\bigr)
\lesssim\|L\|_{\rm op}^2.                                        \tag{18}
\]

At positive adaptive time, (18) becomes a weighted-return theorem on the
causal defect cone. It is not supplied by width homogeneity.

## 6. No subcriticality

Let

\[
R=\Gamma\Gamma^T-I.
\]

Equation (13) shows that \(R\) has homogeneity zero after its Wick
counterterm. All fixed words

\[
R^m,\qquad \Gamma_2R^m\Gamma_2^T,
\]

and their bounded diagonal decorations remain leading. In fact the spectral
support of \(\Gamma\Gamma^T-I\) reaches order-one values, so powers have no
uniform geometric decay.

Thus every homogeneity interval containing zero contains infinitely many
response types. Wick subtraction removes the first contraction but not the
noncrossing contractions of arbitrary length. There are only three possible
ways to complete the hierarchy:

1. assign positive degree to time integration and sum the chronological
   series;
2. prove a high-order reachable Malliavin/tangent bound;
3. sum the full signed colored traffic series or an equivalent marked
   resolvent.

These are precisely the unresolved completion mechanisms. There is no
regularity-structure analogue of local subcriticality in the width grade.

Adding a layer requires only a finite new syntax:

\[
\mathcal C_l(\tau)
=\Gamma_lM_{a_l}\tau M_{\widetilde a_l}\Gamma_l^T,                 \tag{19}
\]

plus one source color and activation jets. But

\[
h(\mathcal C_l(\tau))=h(\tau)
\]

on leading contractions. The grammar is depth-recursive; the family of
leading types is not finite or width-summable.

## 7. Correct master estimate and claim ledger

A successful typed truncation would require:

1. a uniform reachable acceleration bound;
2. a forced causal tangent estimate

   \[
   \|v(t)\|_{\mathcal E}
   \le C_T\left(
   \|v(0)\|_{\mathcal E_+}
   +\int_0^t\|r(s)\|_{\mathcal E_+}\,ds
   \right);
   \]

3. membership of every width, mesh, and grade defect in
   \(\mathcal E_+\);
4. a computable truncation defect
   \(a_Q(T)+C_Q(T)n^{-1/2}\);
5. stability of 1--4 in a forced tube around every restart state.

Those assumptions would give ordinary Duhamel accumulation. The second and
third are exactly the weighted-return/reachable-response theorem.

The final claim levels are:

- **Established:** width valuation (1), fixed-expression colored Wick
  calculus, depth-two identity (11), depth-three cap (14), bounded-gate
  energy estimates, and triangular state-size bounds.
- **Falsified:** global-energy product closure, dimension-uniform ambient
  derivative/local-defect/stability bounds, smallness of centered return
  words, and subcritical width homogeneity.
- **Conditional:** the jet-tail implication (7)--(8) and a forced causal
  truncation theorem.
- **Open:** uniform positive-time weighted-return stability on the actual
  defect cone.

The machinery organizes the missing theorem but does not reduce it.
