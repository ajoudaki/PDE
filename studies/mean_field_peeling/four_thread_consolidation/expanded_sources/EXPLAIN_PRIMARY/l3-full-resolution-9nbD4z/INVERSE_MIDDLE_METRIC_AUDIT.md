# Inverse-middle metric and arctangent coordinates

Result: the \(A_2^{-1}\) metric gives an exact finite-pair identity but
does not cancel the middle gate term. Differentiating the metric creates
an additional first-layer multiplier. The natural arctangent coordinate
removes the scalar part but leaves the nonlocal commutator. These are
limitations of the proposed identities, not a counterexample to
Gaussian-initialized population continuation.

All calculations first concern finite-width exact trajectories, with
normalized Euclidean inner products. They also hold for differentiable
forced comparisons after adding the displayed forcing term. No bounded
operator differentiability of the population \(A_2\) is assumed.
The formulas for \(A'\) below refer to the exact untilded trajectory;
the tilded state may be a differentiable oracle comparison.

## 1. Exact finite-pair inverse-metric identity

Abbreviate
\[
 z=z^{(2)},\quad D=\operatorname{diag}\phi'(z),\quad
 q=(W^{(3)})^*\delta^{(3)},\quad\delta=Dq,\quad
 A=m_1I+W^{(2)}D_1^2(W^{(2)})^*.
\]
Compare two trajectories satisfying
\[
 z'=A\delta+\rho,\qquad
 \widetilde z'=\widetilde A\widetilde\delta+\widetilde\rho.
\]
Let \(e=z-\widetilde z\), \(G=A^{-1}\), \(w=Ge\), and
\[
 {\cal E}=\frac12\langle e,Ge\rangle.
\]
The lower moment bound makes \(G\) positive definite and the energy
uniformly equivalent to \(\|e\|_2^2\) on the controlled finite horizon.
Using \(G'=-GA'G\) gives exactly
\[
 \begin{split}
 {\cal E}'={}&
 \langle e,D(q-\widetilde q)\rangle
 +\langle e,(D-\widetilde D)\widetilde q\rangle\\
 &+\langle w,(A-\widetilde A)\widetilde\delta\rangle
 -\frac12\langle w,A'w\rangle
 +\langle w,\rho-\widetilde\rho\rangle.                  \tag{1}
 \end{split}
\]
In particular, the troublesome term has not disappeared. For arctangent
it is precisely
\[
 \langle e,(D-\widetilde D)\widetilde q\rangle
 =-\mathbb E\left[
 \frac{e^2(z+\widetilde z)\widetilde q}
      {(1+z^2)(1+\widetilde z^2)}\right].                 \tag{2}
\]
Its infinitesimal version is
\(\mathbb E[\phi''(z)q\,e^2]\). It would have the favorable sign if
\((z+\widetilde z)\widetilde q\ge0\) coordinatewise, but no such condition
is supplied by the model.

The actual top equations do control the first term in (1).
Under the established primal and readout bounds,
\[
 \|q-\widetilde q\|_2
 \le C_S\left(\|h^{(2)}-\widetilde h^{(2)}\|_2
       +\|W^{(3)}-\widetilde W^{(3)}\|_{\rm HS}
       +\|W^{(4)}-\widetilde W^{(4)}\|_2\right).
                                                               \tag{3}
\]
This follows by differentiating neither state: expand
\(W^*D_3C-\widetilde W^*\widetilde D_3\widetilde C\), use bounded
readouts, \(|\phi''|\le2\), and
\(\|Wh-\widetilde W\widetilde h\|_2
\le\|W\|_{\rm op}\|h-\widetilde h\|_2
 +a\|W-\widetilde W\|_{\rm HS}\).
Since \(\phi\) is one-Lipschitz, (3) bounds the first term of (1) by
a constant times the squared pair distances. Thus using the actual top
does not remove (2), but it does identify which part is harmless.

## 2. What the motion of \(A\) actually contributes

Write \(W=W^{(2)}\) in this subsection and define
\[
 k=WD_1^2h^{(1)},\qquad
 b_1=\frac{\phi''(z^{(1)})}{\phi'(z^{(1)})}
       =-\frac{2z^{(1)}}{1+(z^{(1)})^2},\qquad |b_1|\le1.
\]
The actual lower training equations imply
\[
 \begin{split}
 A'={}&2\langle k,\delta\rangle I
       +\delta\otimes k+k\otimes\delta\\
     &+W\operatorname{diag}
        \bigl(2D_1\phi''(z^{(1)})\delta^{(1)}\bigr)W^*.
                                                               \tag{4}
 \end{split}
\]
Indeed \(m_1'=2\langle k,\delta\rangle\),
\(W'=\delta\otimes h^{(1)}\), and
\((D_1^2)'=2D_1\phi''(z^{(1)})\delta^{(1)}\).
Therefore, if \(v=D_1W^*w\),
\[
 \frac12\langle w,A'w\rangle
 =\langle k,\delta\rangle\|w\|_2^2
  +\langle w,\delta\rangle\langle w,k\rangle
  +\mathbb E[b_1\delta^{(1)}v^2].                        \tag{5}
\]
The first two terms have the expected uniform quadratic bounds.
The last one contains another backward-field multiplier. Coercivity
\(A\ge m_*I\) controls \(\|v\|_2\) in terms of \(\|e\|_2\), but it does
not control \(\mathbb E[|\delta^{(1)}|v^2]\).

The identity \(b_1\delta^{(1)}=(\log D_1)'\) does not by itself fix this:
integrating that term by parts produces a boundary term involving
\((\log D_1)v^2\) and an integral involving
\((\log D_1)vv'\). Neither has been controlled for the actual comparison.
In particular (4) is not an established population operator-norm bound
on \(A'\). Passing (1) to the population inverse metric would itself
require justifying these quadratic-form terms.

## 3. The actual Gaussian top does not give the missing sign

The already constructed canonical local flow satisfies
\[
 q(s)/s\longrightarrow P_2,\qquad z(s)\longrightarrow Z_0,
\]
where, jointly on the middle population,
\[
 Z_0\sim N(0,m_1(0)),\qquad
 P_2=c_3\phi(Z_0)+\sigma_3G,\qquad
 c_3>0,\quad\sigma_3>0,
\]
and \(G\) is an independent standard Gaussian. This is the actual
initial transpose-conditioning law, not an arbitrary operator example;
see LOCAL_FEATURE_LEARNING.md, equations (6) and (11).

The bounded multiplier argument in that note gives
\[
 \frac{\phi''(z(s))q(s)}{s}
       \longrightarrow \phi''(Z_0)P_2
                  \quad\hbox{in }L^2.                  \tag{6}
\]
On \(1\le Z_0\le2\), the derivative \(\phi''(Z_0)\) is strictly negative.
The independent Gaussian innovation makes each event \(P_2<-1\) and
\(P_2>1\), intersected with this interval, have positive probability.
Thus the limiting middle curvature has both signs. Taking the bounded
indicator of either event as a quadratic-form test and using (6) proves
the corresponding positive or negative sign for its averaged small-time
contribution.

This only rules out assigning a favorable sign to the isolated gate
term from actual-top positivity. It does not assert that the full energy
derivative in (1) has either sign, and it is not a counterexample to
trajectory-specific stability.

## 4. Combining the inverse metric with the natural coordinate

Let \(F(x)=x+x^3/3\), so \(F'=1/\phi'\), and put
\[
 V=F(z)-F(\widetilde z),\qquad R=D\widetilde D^{-1},
 \qquad \widetilde B=\widetilde A-\widetilde m_1 I.
\]
For exact pairs the algebraic identity from
PAIR_SPECIFIC_COMMUTATOR.md is
\[
 V'=D^{-1}AD(q-\widetilde q)
   +D^{-1}(A-\widetilde A)D\widetilde q
   +D^{-1}[\widetilde B,R]\widetilde\delta.                \tag{7}
\]
Now put \(u=A^{-1}V\). The proposed combined energy satisfies
\[
 \begin{split}
 \left(\frac12\langle V,A^{-1}V\rangle\right)'
 ={}&\langle u,D^{-1}AD(q-\widetilde q)\rangle\\
 &+\langle u,D^{-1}(A-\widetilde A)D\widetilde q\rangle\\
 &+\langle D^{-1}u,[\widetilde B,R]\widetilde\delta\rangle
 -\frac12\langle u,A'u\rangle.                           \tag{8}
 \end{split}
\]
Although the commutator is skew-symmetric, its two test vectors in (8)
are \(D^{-1}u\) and \(\widetilde\delta\), not equal vectors.
There is no skew-symmetry cancellation. The inverse metric also retains
the term (5), and \(D^{-1}AD\) need not have a uniform operator bound.
When \(A\) is scalar, the nonlocal commutator vanishes; this is exactly
the own-site simplification, not the trained three-layer situation.

There is a narrow integrability obstruction to trying to remove both
factors by another exact coordinate. Freeze a positive matrix \(A\), and
suppose a \(C^2\) coordinate \(\Psi(z)\) sent \(z'=AD(z)q\) to
\(\Psi'=q\) for every \(q\). Necessarily
\[
 D\Psi(z)=D(z)^{-1}A^{-1}.
\]
For \(i\ne j\), the mixed derivatives of its \(i\)-th component would be
\[
 \partial_i\partial_j\Psi_i
       =2z_i(A^{-1})_{ij},\qquad
 \partial_j\partial_i\Psi_i=0.
\]
Thus no such coordinate exists on an open set if \(A^{-1}\) has an
off-diagonal entry. This statement only concerns that exact
mobility-flattening coordinate for frozen \(A\). It does not exclude
a different distance, a history-dependent construction, or a signed
estimate exploiting the full Gaussian flow.

## 5. A domain repair, but not an evolution estimate

The squared natural-coordinate distance in (8) may require sixth moments
that the current global primal bounds do not supply. A genuinely finite
natural-coordinate metric on all of \(L^2\) is
\[
 d_F(z,\widetilde z)
       =\mathbb E|F(z)-F(\widetilde z)|^{2/3}.             \tag{9}
\]
It satisfies the triangle inequality because \(r\mapsto r^{2/3}\) is
subadditive. If \(e=z-\widetilde z\), then
\[
 |F(z)-F(\widetilde z)|
 =|e|\left(1+\frac{z^2+z\widetilde z+\widetilde z^2}{3}\right)
 \ge\frac{|e|^3}{12}.
\]
Consequently
\[
 d_F\ge12^{-2/3}\|e\|_2^2.
\]
Hölder's inequality also gives
\[
 d_F\le C\|e\|_2^{2/3}
       \left[1+(\|z\|_2+\|\widetilde z\|_2)^{4/3}\right].
\]
Thus (9) is finite and induces the \(L^2\) topology. This repairs only
the domain issue: differentiating it formally weights (7) by
\(\operatorname{sgn}(V)|V|^{-1/3}\), while the nonlocal commutator remains.
No uniform signed or Osgood differential inequality for (9) has been
established.

Conclusion: the inverse metric exposes, rather than removes, the
remaining products (2) and (5). A successful use of this route must
control them jointly with the actual lower/top comparison, or find a
new cancellation for the commutator in (8). The present positivity,
action, and frozen-generator bounds do not supply that step.
