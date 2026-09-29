# Dense-driven oracle: recomputed forward and backward passes

Scoped derivation, 2026-09-27. Scientific inputs: `paper/main.tex`,
`paper/comparison_appendix.tex`, and `docs/notation.qmd`. This note concerns an
oracle fed by the exact dense histories. It does not claim stability of an
autonomous response-memory closure. All statements below are deterministic
conditional on the stated dense-path bounds.

Section 7 addresses a subsequently assigned extension, using the supervisor's
one-sample coordinate transform and checking Section 8 of this study's
`DENSE_DRIVEN_ORACLE.md`. That check is an internal scoped check, not an
independent promotion review.

## 1. Oracle and the distinction between actions and passes

At each time, copy the dense first matrix and readout exactly. Replace only
the hidden matrices by their paired projected dense-history reconstructions,
retaining the same initialized matrices. Write

\[
 E^{(\ell)}=\widehat W^{(\ell)}-W^{(\ell)},\qquad
 \|E^{(\ell)}\|_{\rm op}\le\varepsilon_\ell,\qquad
 \|W^{(\ell)}\|_{\rm op}\le A_\ell,\qquad
 R=\|w\|_2/\sqrt n.
\]

Every hat on a response means a fresh network pass through these matrices;
the histories defining the matrices remain dense histories. For the old
clock, with its prescribed prefix and \(b_a=r_a\delta_a/\rho\), orthogonality
gives the exact matrix identity

\[
 E^{(\ell)}=
 \frac{2}{nm}\sum_a\int_0^\tau
 (I-\Pi_P)b_a^{(\ell)}
 \bigl((I-\Pi_P)h_a^{(\ell-1)}\bigr)^T\,d\xi.
\]

Consequently, one admissible \(\varepsilon_\ell\), also bounding the
Frobenius error, is

\[
 \frac2m\sum_a
 \left(\frac1n\int_0^\tau
       \|(I-\Pi_P)b_a^{(\ell)}\|_2^2d\xi\right)^{1/2}
 \left(\frac1n\int_0^\tau
       \|(I-\Pi_P)h_a^{(\ell-1)}\|_2^2d\xi\right)^{1/2}.
\]

The following pass bounds use only the resulting matrix error; source
regularity and its order rate are a separate question. The immediate,
fixed-argument action estimates are

\[
 \frac{\|E^{(\ell)}h^{(\ell-1)}\|_2}{\sqrt n}
 \le\varepsilon_\ell,
 \qquad
 \frac{\|(E^{(\ell)})^T\delta^{(\ell)}\|_2}{\sqrt n}
 \le\varepsilon_\ell\frac{\|\delta^{(\ell)}\|_2}{\sqrt n}.
\]

The first uses \(|\tanh|\le1\). Neither identity by itself bounds a
recomputed backward pass: its multiplication gates have changed.

## 2. All forward responses at any fixed depth

For any input, put
\(a_\ell=\|\widehat h^{(\ell)}-h^{(\ell)}\|_2/\sqrt n\).
The copied first matrix gives \(a_1=0\). Splitting the preactivation
difference using the dense matrix and bounded oracle activation gives

\[
 \widehat z^{(\ell)}-z^{(\ell)}
 =W^{(\ell)}(\widehat h^{(\ell-1)}-h^{(\ell-1)})
   +E^{(\ell)}\widehat h^{(\ell-1)},
\]
\[
 \frac{\|\widehat z^{(\ell)}-z^{(\ell)}\|_2}{\sqrt n}
 \le s_\ell:=\varepsilon_\ell+A_\ell a_{\ell-1},
 \qquad a_\ell\le\min\{2,s_\ell\}.
\]

Here \(\tanh\) is 1-Lipschitz. In particular,

\[
 a_L\le\sum_{j=2}^L\varepsilon_j\prod_{k=j+1}^LA_k,
 \qquad |\widehat f-f|\le R a_L.
\]

These bounds hold simultaneously for all inputs, without an input norm
restriction, because the first matrix is identical and its output is bounded.
They require no feedback or continuation estimate.

## 3. Two hidden layers: a linear backward bound

Let \(L=2\), \(A=A_2\), \(\varepsilon=\varepsilon_2\), and additionally
assume \(B=\|w\|_\infty<\infty\). For tanh,

\[
 c_\phi:=\sup_z|\phi''(z)|=\frac4{3\sqrt3}.
\]

Indeed \(|\phi''|=2|u|(1-u^2)\), \(u=\tanh z\), whose maximum on
\([-1,1]\) occurs at \(|u|=1/\sqrt3\). Define the backward errors
\(d_\ell=\|\widehat\delta^{(\ell)}-\delta^{(\ell)}\|_2/\sqrt n\).
The top backward pass satisfies

\[
 d_2=\frac{\|w\odot[\phi'(\widehat z^{(2)})-
                         \phi'(z^{(2)})]\|_2}{\sqrt n}
 \le c_\phi B\varepsilon.
\]

The first gate is identical. Writing \(D_1=\operatorname{diag}\phi'(z^{(1)})\),

\[
 \widehat\delta^{(1)}-\delta^{(1)}
 =D_1\left[(W^{(2)})^T
             (\widehat\delta^{(2)}-\delta^{(2)})
          +(E^{(2)})^T\widehat\delta^{(2)}\right].
\]

Because \(\|D_1\|_{\rm op}\le1\) and
\(\|\widehat\delta^{(2)}\|_2/\sqrt n\le R\),

\[
 d_1\le A d_2+\varepsilon R
       \le\varepsilon(R+A c_\phi B).
\]

Thus every forward and backward response, including the bottom backward
response, has a width-uniform linear error bound when \(A,R,B\) are uniform.
The constants are uniform over inputs and times on which these bounds hold.
In particular an independently established dense-source
\(\varepsilon=O_T(P^{-q})\) transfers with the same exponent \(q\) to all
these diagnostics. No autonomous stability assumption enters.

### Why zero and small Gaussian readout supply the needed bound

The dense readout equation and bounded activation imply, coordinatewise,

\[
 |\dot w_i|\le\frac2m\sum_a|r_a|\le2\rho,
 \qquad
 B(t)\le B(0)+2\int_0^t\rho(s)\,ds.
\]

Loss dissipation gives \(\rho(t)\le\rho(0)\). With
\(Y=(m^{-1}\sum_a y_a^2)^{1/2}\),
\(\rho(0)\le Y+R(0)\le Y+B(0)\). Exact zero initialization therefore gives
\(B(t)\le2TY\) on \([0,T]\), independently of width. For the stored-readout
law \(w_i(0)\sim N(0,n^{-2})\), the elementary Gaussian tail and a union bound
give

\[
 \Pr\!\left(B(0)>\frac{\sqrt{2\log(2n/\eta)}}n\right)\le\eta.
\]

The displayed threshold is uniformly bounded in \(n\) at each confidence
level and tends to zero. This supplies a uniform high-probability readout
bound; it does not assert an almost-sure deterministic bound on a Gaussian
realization. The stipulated dense operator bounds can also be controlled from
initial operator bounds: the mobility-weighted energy identity yields

\[
 \int_0^T\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F^2dt\le\rho(0)^2,
 \qquad
 A_\ell(t)\le\|W_0^{(\ell)}\|_{\rm op}+\sqrt T\,\rho(0).
\]

The first assertion follows from
\(\dot{\mathcal L}=-\|\dot W^{(1)}\|_F^2/n
-\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F^2-\|\dot w\|_2^2/n\);
the second is the triangle inequality and Cauchy--Schwarz in time.

## 4. Gradient and tangent-kernel diagnostics for two hidden layers

Let \(F\) denote the actual dense gradient vector field, but evaluate it at
the oracle's hybrid parameter state when writing \(F(\widehat\theta)\).
This evaluation recomputes oracle residuals. It is not the derivative of the
oracle reconstruction. Let \(X=\max_a\|x_a\|_2/\sqrt d\), and use the
preceding bounds uniformly over the training inputs. Since the training RMS
prediction error is at most \(R\varepsilon\), direct subtraction gives

\[
 \frac{\|F_w(\widehat\theta)-F_w(\theta)\|_2}{\sqrt n}
 \le2(R+\rho)\varepsilon,
\]
\[
 \|F_{W^{(2)}}(\widehat\theta)-F_{W^{(2)}}(\theta)\|_F
 \le2\varepsilon(R^2+\rho c_\phi B),
\]
\[
 \frac{\|F_{W^{(1)}}(\widehat\theta)-F_{W^{(1)}}(\theta)\|_F}{\sqrt n}
 \le2X\varepsilon
       \left[(A+\varepsilon)R^2+\rho(R+A c_\phi B)\right].
\]

For example, split each residual-response product as
\(\widehat r\,\widehat\delta-r\delta
=(\widehat r-r)\widehat\delta+r(\widehat\delta-\delta)\),
apply Cauchy--Schwarz over samples, and use
\(\|\widehat\delta^{(1)}\|_2/\sqrt n\le(A+\varepsilon)R\).
For the middle matrix, the copied \(h^{(1)}\) cancels the activation-change
term, and \(\|uv^T/n\|_F=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n)\).

The mobility-matched tangent kernel is

\[
 K_{ab}=G_{ab}\frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n
 +\frac{(\delta_a^{(2)})^T\delta_b^{(2)}}n
  \frac{(h_a^{(1)})^Th_b^{(1)}}n
 +\frac{(h_a^{(2)})^Th_b^{(2)}}n.
\]

Subtracting pairings gives the uniform bound

\[
 |\widehat K_{ab}-K_{ab}|
 \le X^2(2A+\varepsilon)R d_1+2R d_2+2a_2.
\]

Hence instantaneous velocities and tangent kernels inherit the same linear
matrix-error rate. A *forced accumulator*
\(\bar\theta(t)=\theta(0)+\int_0^tF(\widehat\theta(s))ds\), whose values are
not fed back into the oracle, inherits the integral of these errors in the
displayed norms. This is a valid additional approximation to the dense path.
If accumulated outer weights instead drive later oracle passes, the first
layer is no longer identical. A changed first gate then multiplies
\((W^{(2)})^T\delta^{(2)}\), and the preceding two-layer proof no longer
supplies the required feedback estimate.

## 5. Exact obstruction at greater depth

Write \(D_\ell=\operatorname{diag}\phi'(z^{(\ell)})\), and define the dense
pre-gate backward carrier

\[
 g_L=w,\qquad
 g_\ell=(W^{(\ell+1)})^T\delta^{(\ell+1)}\quad(\ell<L).
\]

At each layer below the top, exact subtraction gives

\[
 \widehat\delta^{(\ell)}-\delta^{(\ell)}
 =\widehat D_\ell\left[(W^{(\ell+1)})^T
             (\widehat\delta^{(\ell+1)}-\delta^{(\ell+1)})
       +(E^{(\ell+1)})^T\widehat\delta^{(\ell+1)}\right]
       +(\widehat D_\ell-D_\ell)g_\ell.
\]

Define

\[
 \widehat D^{\rm size}_\ell
   =R\prod_{j=\ell+1}^L(A_j+\varepsilon_j),\qquad
 \eta_\ell=\frac{\|(\widehat D_\ell-D_\ell)g_\ell\|_2}{\sqrt n}.
\]

Contraction by each gate shows
\(\|\widehat\delta^{(\ell)}\|_2/\sqrt n\le\widehat D^{\rm size}_\ell\).
Therefore

\[
 d_L=\eta_L,\qquad
 d_\ell\le A_{\ell+1}d_{\ell+1}
       +\varepsilon_{\ell+1}\widehat D^{\rm size}_{\ell+1}+\eta_\ell,
 \qquad \eta_1=0.
\]

This isolates all missing regularity in *dense* carriers, with no need for
oracle carrier moments. Spectral bounds give normalized second-moment bounds
for \(g_\ell\), but those do not control the changed-gate product uniformly.

Here is an explicit counterexample to such a deduction from norms alone.
Take even \(n\), \(u=(1,\ldots,1)^T/\sqrt n\), and a unit vector \(v\)
with half its entries \(1/\sqrt n\) and half \(-1/\sqrt n\); thus
\(u^Tv=0\). Fix \(0<a<1\) and \(c>0\). Choose

\[
 h^{(1)}=a\sqrt n\,u,\qquad
 W^{(2)}=e_1v^T,\qquad W^{(3)}=ue_1^T,\qquad
 w=\sqrt n\,u,
\]
\[
 \widehat W^{(2)}=W^{(2)}+\frac{c}{a\sqrt n}e_1u^T,
 \qquad \widehat W^{(3)}=W^{(3)}.
\]

The first activation is realized by the common constant preactivation
\(\operatorname{arctanh}(a)\). Dense operator norms and \(\|w\|_\infty\)
are one, while the perturbation has both operator and Frobenius norm
\(c/(a\sqrt n)\). Dense \(z^{(2)}=z^{(3)}=0\). With
\(t_c=\tanh c\) and \(q_n=\operatorname{sech}^2(t_c/\sqrt n)\),

\[
 \delta^{(2)}=\sqrt n\,e_1,\qquad
 \widehat\delta^{(2)}=q_n\operatorname{sech}^2(c)\sqrt n\,e_1,
\]
\[
 d_2=|q_n\operatorname{sech}^2(c)-1|\longrightarrow\tanh^2(c)>0.
\]

Moreover,

\[
 \delta^{(1)}=(1-a^2)\sqrt n\,v,
\quad
 \widehat\delta^{(1)}=(1-a^2)q_n\operatorname{sech}^2(c)
                       [\sqrt n\,v+(c/a)u],
\]

so \(d_1\to(1-a^2)\tanh^2(c)>0\), although the output discrepancy is
\(\tanh(t_c/\sqrt n)=O(n^{-1/2})\). The failure already occurs at three
hidden layers, with a rank-one matrix perturbation and a bounded readout.
If the readout is only bounded in normalized Euclidean norm, the same failure
occurs at two hidden layers: omit layer 3 and set \(w=\sqrt n e_1\).

This is an algebraic counterexample to an implication from the stated norm
bounds. It is not a construction of a paired-history reconstruction along
the specified Gaussian gradient flow, and therefore does not disprove a
stronger oracle theorem using additional properties of that trajectory.

## 6. Tail and moment conditions that repair the arbitrary-depth bound

Since \(0\le\phi'\le1\), each gate difference is bounded by both
\(1\) and \(c_\phi|\widehat z_i-z_i|\). For every \(K>0\), splitting
coordinates according to \(|g_{\ell,i}|\le K\) gives

\[
 \eta_\ell\le c_\phi K s_\ell+
 \left(\frac1n\sum_i|g_{\ell,i}|^2
                         \mathbf1_{\{|g_{\ell,i}|>K\}}\right)^{1/2}.
\]

Thus uniform integrability of the squared dense carriers, uniformly in
width, time, and the inputs under consideration, gives a width-uniform
modulus tending to zero as \(s_\ell\to0\). It is sufficient; a mere bounded
second moment is not.

If for some \(p>2\),
\((n^{-1}\sum_i|g_{\ell,i}|^p)^{1/p}\le M_{\ell,p}\), Hölder's inequality
with \(q=2p/(p-2)\) yields

\[
 \eta_\ell\le M_{\ell,p}
       \min\{1,(c_\phi s_\ell)^{1-2/p}\}.
\]

Indeed the normalized \(q\)-moment of a gate difference is bounded by its
normalized second moment to the power \(2/q\), since its absolute value is
at most one. At fixed depth, the backward recursion is linear in these
forcing terms: if all matrix errors are \(O(\varepsilon)\), the resulting
backward error is \(O(\varepsilon^{1-2/p})\), with **no multiplication of
the exponent across layers**. Uniform carrier bounds give the linear rate.
Uniform moment growth \(M_{\ell,p}\le C\sqrt p\) gives instead
\(O(\varepsilon\sqrt{\log(e/\varepsilon)})\), by choosing
\(p\) proportional to \(\log(e/\varepsilon)\). These are extra dense-path
hypotheses, not consequences of spectral bounds.

There is also a useful population statement without a quantitative moment
assumption. Replace finite averages by the corresponding population
expectations. A continuous dense carrier path on compact time is compact
in \(L^2\), hence its squares are uniformly integrable. To see this, cover
the compact set by finitely many \(L^2\) balls of radius \(\alpha\); if
\(g\) is close to a center \(h\), then

\[
 \mathbb E[|g|^2\mathbf1_{|g|>K}]
 \le4\|g-h\|_{L^2}^2+
        2\mathbb E[|h|^2\mathbf1_{|h|>K/2}].
\]

First take \(K\) large for the finitely many centers, then \(\alpha\)
small. The tail bound and backward recursion prove uniform-in-time
population oracle backward convergence at every fixed depth whenever the
hidden operator errors vanish uniformly and the dense carrier paths are
\(L^2\)-continuous. This gives no explicit rate. A finite-width theorem
can use a corresponding uniform-integrability conclusion from a separately
proved strong population approximation; bounded operators alone do not
establish it.

The strongest direct rate statement here is therefore: for two tanh hidden
layers with copied dense outer weights and zero or suitably controlled small
readout initialization, every width-uniform matrix approximation rate transfers
unchanged to recomputed forward responses, all backward responses, predictions,
instantaneous gradient velocities, and the tangent kernel. In particular a
dense-source \(P^{-2}\) bound needs no closure-stability argument to give
\(P^{-2}\) bounds for these oracle observables.

## 7. Stronger special case: evolving outer weights for one sample

There is an additional result for exactly one normalized sample
\(\|x\|_2^2/d=1\), two hidden tanh layers, and identical initial outer
weights. The hidden path \(\widehat W^{(2)}(t)\) is still constructed from
dense histories, but the oracle first matrix and readout now follow their
own gradient equations, using their own predictions and responses.
This is an externally forced system, not the autonomous memory closure.

Write \(u=W^{(1)}x/\sqrt d\) and introduce the scalar function

\[
 G(u)=\int_0^u\frac{ds}{\phi'(s)}
     =\frac u2+\frac{\sinh(2u)}4,
 \qquad v=G(u)-G(u(0)),
\]

coordinatewise. The shift makes \(v(0)=0\) and avoids requiring the
initial transformed coordinate itself to have a finite second moment in a
population formulation. Since \(G'=\cosh^2u\ge1\), \(G\) is a bijection
of \(\mathbb R\); its inverse is 1-Lipschitz. The function
\(H(v)=\tanh(G^{-1}(G(u(0))+v))\) is coordinatewise 1-Lipschitz and bounded
by one: its derivative is \((\phi'(u))^2\le1\).

The normalized one-sample first-layer equation is
\(\dot u=-2r\,\phi'(u)\odot W^T\delta^{(2)}\). Consequently the
transformed outer equations are exactly

\[
 \dot v=-2r W^T\delta^{(2)},\qquad
 \dot w=-2r\,h^{(2)},\qquad
 h^{(2)}=\tanh(WH(v)),\qquad
 \delta^{(2)}=w\odot\phi'(WH(v)).
\]

Here \(W=W^{(2)}\), and the oracle uses \(\widehat W(t)\) and its own
\(v,w\) in the same equations. No reciprocal residual occurs.

An a priori readout bound is available without loss dissipation. For either
system let \(R(t)=\|w(t)\|_2/\sqrt n\). The exact readout equation gives

\[
 \frac{d}{dt}R(t)^2=-4r f
       =y^2-4(f-y/2)^2\le y^2,
 \qquad R(t)\le R_T:=\sqrt{R(0)^2+y^2T},
\]
\[
 |r(t)|\le R_T+|y|,
 \qquad
 \|w(t)\|_\infty
 \le\|w(0)\|_\infty+2T(R_T+|y|).
\]

These bounds apply to the externally forced oracle. Its ordinary loss is
not necessarily decreasing, because the externally supplied hidden path
adds a forcing term to the derivative of that loss.

For the comparison define
\(e_v=\|\widehat v-v\|_2/\sqrt n\) and
\(e_w=\|\widehat w-w\|_2/\sqrt n\). At a common time, use dense bounds
\(A=\|W\|_{\rm op}\), \(R=\|w\|_2/\sqrt n\),
\(B=\|w\|_\infty\), and
\(\varepsilon=\|\widehat W-W\|_{\rm op}\). The preceding Lipschitz
properties give

\[
 a_1\le e_v,\qquad a_2\le A e_v+\varepsilon,
 \qquad e_r:=|\widehat r-r|\le e_w+R a_2,
 \qquad d_2\le e_w+c_\phi B a_2.
\]

Splitting the transformed velocities using dense \(r,W\) then gives

\[
 e_v(t)\le2\int_0^t
  \left[(A+\varepsilon)\widehat R\,e_r
       +|r|\bigl(A d_2+\varepsilon\widehat R\bigr)\right]ds,
\]
\[
 e_w(t)\le2\int_0^t[e_r+|r|a_2]ds.
\]

If \(A\) is bounded on the horizon and \(\varepsilon\le1\), all
coefficients are bounded independently of width by the readout estimates.
Substitution therefore gives

\[
 e_v(t)+e_w(t)\le C_T\int_0^t
        [e_v(s)+e_w(s)+\varepsilon(s)]ds,
 \qquad
 \sup_{t\le T}(e_v+e_w)
 \le C_T e^{C_TT}\int_0^T\varepsilon(s)ds.
\]

The last inequality follows by the integrating-factor proof of Gronwall.
The inverse transform implies
\(\|\widehat u-u\|_2/\sqrt n\le e_v\). Both first-matrix trajectories
move only in the input direction, so their difference satisfies
\(\widehat W^{(1)}-W^{(1)}=(\widehat u-u)x^T/\sqrt d\). Its normalized
Frobenius norm consequently equals \(\|\widehat u-u\|_2/\sqrt n\).

Thus a width-uniform dense-source \(O_T(P^{-2})\) hidden-matrix bound
implies a width-uniform \(O_T(P^{-2})\) approximation by this *evolving-outer,
externally forced oracle* in the first weights, readout, all forward
responses, predictions, and top backward response. The transformed outer
vector field is uniformly Lipschitz on the bounded-readout region; no
stability property of an autonomous history closure is assumed.

The bottom backward response remains a separate observable: its first gate
now changes, and its error contains
\([\phi'(\widehat u)-\phi'(u)]\odot W^T\delta^{(2)}\).
The transformed-coordinate proof does not by itself give a linear bound
for that product. The dense-carrier moment or tail conditions of Section 6
supply such a bound or a convergence modulus. Nor does this scalar
coordinate transform handle general multiple-sample input Gram matrices;
the asserted extension is restricted to the stated one-sample problem.
