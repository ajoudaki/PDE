# Gaussian initial signed curvature and top response

This is a bounded theoretical sidecar for the fixed activation
\(\phi(z)=1+\varepsilon\arctan z\), \(\varepsilon=1/10\).
No experiments, delegation, or changes to the research contract are used.
The results below concern initialization and the exact first step of the
specified short-bootstrap scalar law. They do not establish a trained-path
sign theorem.

For every centered Gaussian pair with common variance \(q>0\) and covariance
\(-q\le c<q\), the curvature
\(K_\sigma=\mathbb E[V_\sigma\phi''(U)]\) is strictly negative in both label
modes, except that \(K_+=0\) when \(c=-q\). Nevertheless, the full symmetric
matrix in the question has a strictly positive eigenvalue in direction
\((1,\sigma)\) and a strictly negative eigenvalue in direction
\((1,-\sigma)\), with the sole exception that the latter eigenvalue is zero
for \(\sigma=+1,c=-q\). In particular, at the actual model initialization
both label modes give an indefinite matrix.

The proof separates the curvature from the derivative-product term. An
elementary integral representation gives the curvature signs; a different,
strictly decreasing combination of those integrals determines the matrix
eigenvalues. The source-slot calculation then identifies which terms occur
in the historical and current first-step coefficients.

## 1. Elementary integral identities and all exchanges

Write
\[
 f(x)=\arctan x,\qquad h(x)=f'(x)=\frac1{1+x^2},\qquad
 f''(x)=h'(x)=-\frac{2x}{(1+x^2)^2}.
\]
For fixed \(q>0\) and \(t\in[-q,q]\), expectations subscripted by \(t\)
refer to a centered Gaussian pair \((X,Y)\) with variances \(q,q\) and
covariance \(t\). Define
\[
 \begin{split}
 B_q(t)&=\mathbb E_t[h(X)h(Y)],& A_q&=B_q(q)=\mathbb E[h(U)^2],\\
 J_q(t)&=-\mathbb E_t[f(Y)f''(X)],&
 D_q&=A_q-J_q(q),\\
 T_q(t)&=B_q(t)-J_q(t).
 \end{split}                                                    \tag{1}
\]
These definitions include the singular endpoints. For example one may
realize every such pair as
\[
 X=\sqrt q\,N_1,\qquad
 Y=\frac{t}{\sqrt q}N_1+\sqrt{q-t^2/q}\,N_2,
\]
with independent standard normal variables; at either endpoint the second
coefficient is simply zero. No inverse covariance is needed.

The elementary Laplace integrals give
\[
 f(x)=\int_0^\infty e^{-u}\frac{\sin(ux)}u\,du,\quad
 h(x)=\int_0^\infty e^{-u}\cos(ux)\,du,\quad
 f''(x)=-\int_0^\infty u e^{-u}\sin(ux)\,du.                 \tag{2}
\]
For completeness, the first integral vanishes at zero and its derivative
is the second integral, equal to \(\operatorname{Re}[(1-ix)^{-1}]
=(1+x^2)^{-1}\). Differentiating the second integral gives the third.
The first integral is absolutely convergent because
\(|\sin(ux)|/u\le |x|\); differentiation is dominated successively by
\(e^{-u}\) and \(u e^{-u}\). Thus these identities require no external
representation theorem.

The Gaussian characteristic function and the product-to-sum identities
give, including at singular covariance,
\[
 \begin{split}
 \mathbb E_t[\sin(uX)\sin(vY)]
   &=e^{-q(u^2+v^2)/2}\sinh(tuv),\\
 \mathbb E_t[\cos(uX)\cos(vY)]
   &=e^{-q(u^2+v^2)/2}\cosh(tuv).
 \end{split}                                                    \tag{3}
\]
Indeed \(uX\pm vY\) is a centered scalar normal variable of variance
\(q(u^2+v^2)\pm2tuv\). The scalar characteristic function follows directly
by Gaussian integration by parts: if the variance is \(s>0\), its
characteristic function \(g\) satisfies \(g'(r)=-sr g(r)\), \(g(0)=1\);
for \(s=0\) the variable is zero almost surely. This proves the required
formula also when one of these variances vanishes.

Put \(w_q(u,v)=e^{-u-v-q(u^2+v^2)/2}\), for \(u,v>0\). Equations (2)--(3)
yield the exact integrals
\[
 \begin{split}
 B_q(t)&=\int_0^\infty\!\!\int_0^\infty
                   w_q(u,v)\cosh(tuv)\,du\,dv,\\
 J_q(t)&=\int_0^\infty\!\!\int_0^\infty
                   \frac{u}{v}w_q(u,v)\sinh(tuv)\,du\,dv\\
       &=\frac12\int_0^\infty\!\!\int_0^\infty
          \left(\frac uv+\frac vu\right)w_q(u,v)\sinh(tuv)\,du\,dv.
 \end{split}                                                    \tag{4}
\]
Here are explicit absolute-integrability checks for the exchanges. For
the cosine product the bound is \(e^{-u-v}\). For the sine product,
\[
 \mathbb E|\sin(uX)\sin(vY)|\le uv\,\mathbb E|XY|\le uvq,
\]
so the absolute integrand for the nonsymmetric curvature representation
is bounded by \(q u^2e^{-u-v}\). This is integrable over the positive
quadrant and permits expectation, both integrations, and their order to
be exchanged. Swapping \(u,v\) then gives the symmetrized formula.

The following bounds also justify continuity and parameter differentiation
uniformly up to the endpoints:
\[
 \begin{split}
 e^{-q(u^2+v^2)/2+|t|uv}&\le1,\\
 w_q\cosh(tuv),\quad w_q|\sinh(tuv)|&\le e^{-u-v},\\
 \frac uv w_q|\sinh(tuv)|&\le q u^2e^{-u-v}.
 \end{split}                                                    \tag{5}
\]
The last line uses \(|\sinh s|\le |s|e^{|s|}\). In particular,
\(\partial_t B_q\) is dominated by \(uv e^{-u-v}\), and the derivative of
the symmetrized \(J_q\) integrand is dominated by
\((u^2+v^2)e^{-u-v}/2\). All these polynomial-exponential bounds are
integrable. Endpoint derivatives below mean the continuous one-sided
extensions. Every parameter integration below is over a finite interval
and obeys the same bounds.

It follows that \(B_q\) is even and strictly positive, and \(J_q\) is odd
and strictly increasing, since
\[
 J_q'(t)=\frac12\int_0^\infty\!\!\int_0^\infty
                (u^2+v^2)w_q(u,v)\cosh(tuv)\,du\,dv>0.       \tag{6}
\]
In particular \(J_q(q)>0\), and
\(-J_q(q)<J_q(c)<J_q(q)\) whenever \(-q<c<q\).

## 2. Signed curvature in the two label modes

Let \(Z_1=U,Z_2=V\), \(y=(1,\sigma)\), and
\[
 V_\sigma=\frac{\phi(U)+\sigma\phi(V)}2
          =\frac{1+\sigma}2+\frac\varepsilon2(f(U)+\sigma f(V)).
\]
The expectation of \(f''(U)\) is zero by oddness and the centered Gaussian
marginal. Consequently
\[
 K_\sigma:=\mathbb E[V_\sigma\phi''(U)]
       =-\frac1{200}\bigl(J_q(q)+\sigma J_q(c)\bigr).          \tag{7}
\]
Exchangeability of \((U,V)\), together with
\(V_\sigma(V,U)=\sigma V_\sigma(U,V)\), gives
\[
 \mathbb E[V_\sigma\phi''(Z_a)]=y_aK_\sigma.                 \tag{8}
\]
Thus the two label-conjugated diagonal curvature terms are both
\(K_\sigma\). The unconjugated curvature at the second sample has the
opposite sign when \(\sigma=-1\).

Strict monotonicity and oddness of \(J_q\) prove
\[
 \begin{array}{c|c|c}
 \text{mode}&-q<c<q&c=-q\\ \hline
 \sigma=+1&K_+<0&K_+=0\\
 \sigma=-1&K_-<0&K_-=-J_q(q)/100<0.
 \end{array}                                                    \tag{9}
\]
At \(c=-q\), \(V=-U\) almost surely: \(V_+=1\), while
\(V_-=\varepsilon f(U)\). These facts also check (9) directly.
At the excluded endpoint \(c=q\), \(V_-=0\) and \(K_-=0\), whereas
\(K_+=-J_q(q)/100\). No strict assertion is being extended through a
degenerate cancellation.

## 3. The full response has a different sign structure

Derivatives defining the matrix are taken in the ambient coordinates
\((Z_1,Z_2)\) before evaluation on the Gaussian law. In particular,
\(V_+=1\) on the support at \(c=-q\) does not make its ambient partial
derivatives vanish. The same rule applies to every singular case below.

The matrix specified in the question is exactly
\[
 M_{ab}=\frac{y_ay_b}{2}\mathbb E[\phi'(Z_a)\phi'(Z_b)]
        +y_a\mathbf1_{a=b}\mathbb E[V_\sigma\phi''(Z_a)],
\]
and hence, using (7)--(8),
\[
 M=\frac1{200}
 \begin{pmatrix}
 D_q-\sigma J_q(c)&\sigma B_q(c)\\
 \sigma B_q(c)&D_q-\sigma J_q(c)
 \end{pmatrix}.                                                \tag{10}
\]
Its two normalized eigenvectors are \(e_y=(1,\sigma)/\sqrt2\) and
\(e_\perp=(1,-\sigma)/\sqrt2\), with eigenvalues
\[
 \begin{split}
 \lambda_y&=\frac1{200}\{D_q+B_q(c)-\sigma J_q(c)\}
            =\frac1{200}\{D_q+T_q(\sigma c)\},\\
 \lambda_\perp&=\frac1{200}\{D_q-B_q(c)-\sigma J_q(c)\}
            =\frac1{200}\{D_q-T_q(-\sigma c)\}.
 \end{split}                                                    \tag{11}
\]
These formulas alone do not establish the signs: the positive
derivative-product contribution must be compared with the curvature.
The comparison can be proved completely.

First, Gaussian integration by parts applied to the bounded differentiable
function \(f(x)h(x)\) gives
\[
 D_q=\mathbb E[h(U)^2+f(U)f''(U)]
    =\frac1q\mathbb E\left[\frac{U\arctan U}{1+U^2}\right]>0. \tag{12}
\]
The derivative is bounded, the Gaussian density annihilates the boundary
term, and the final integrand is strictly positive except at zero.
A variance-\(q>0\) Gaussian assigns probability zero to zero, proving
strict positivity. Also \(T_q(q)=D_q\) by definition.

Second, differentiating the justified integrals (4) gives
\[
 \begin{split}
 T_q'(t)
  &=\iint w_q\left\{uv\sinh(tuv)
                   -\frac{u^2+v^2}{2}\cosh(tuv)\right\}\,du\,dv\\
  &=-\frac14\iint w_q\left\{(u-v)^2e^{tuv}
                            +(u+v)^2e^{-tuv}\right\}\,du\,dv<0.
 \end{split}                                                    \tag{13}
\]
All double integrals here and below are over \((0,\infty)^2\). The
second summand in braces is strictly positive everywhere in that domain.
Therefore
\[
 T_q(t)>T_q(q)=D_q>0\quad(-q\le t<q).                         \tag{14}
\]
Inserting (14) into (11) proves the complete classification:

| Covariance and labels | \(\lambda_y\) | \(\lambda_\perp\) | Full matrix |
|---|---:|---:|---|
| \(-q<c<q\), either mode | strictly positive | strictly negative | indefinite |
| \(c=-q,\ \sigma=+1\) | \(A_q/100\) | zero | positive semidefinite, rank one |
| \(c=-q,\ \sigma=-1\) | \(D_q/100\) | \(-J_q(q)/100\) | indefinite |

Thus there are no eigenvalue sign-changing regimes within the open
nondegenerate covariance interval: the inertia is always one positive and
one negative. In particular, every nondegenerate pair is a counterexample
to either a positive-semidefinite or a negative-semidefinite assertion
about this full matrix. Negative curvature does not make the full response
negative semidefinite.

For an explicitly signed integral version of the negative eigenvalue,
let \(L_q(t)=-T_q'(t)>0\), with its positive integrand given in (13). Then
\[
 \lambda_\perp=-\frac1{200}\int_{-\sigma c}^{q}L_q(t)\,dt.    \tag{15}
\]
Likewise, in opposite-label mode,
\[
 K_-=-\frac1{200}\int_c^q J_q'(t)\,dt.                       \tag{16}
\]
The cancellation as \(c\uparrow q\) in opposite-label mode is therefore
exact and has a strict sign before the endpoint. It does not require an
absolute row estimate. The positive eigenvalue is the largest eigenvalue
because \(\lambda_y-\lambda_\perp=B_q(c)/100>0\).

For the excluded \(c=q\), the same formulas give eigenvalues
\((D_q/100,-J_q(q)/100)\) for same labels and \((A_q/100,0)\) for opposite
labels. If one additionally lets \(q=0\), outside the question's domain,
then \(U=V=0\), \(K_\sigma=0\), and \(M=yy^T/200\); none of the
strict curvature claims apply there.

## 4. Where the exact model initialization lies

This subsection concerns the infinite-width initial scalar law dictated
by the fixed model, not an arbitrary choice of \(q,c\). Define
\[
 F_s(t)=\mathbb E_t[f(X)f(Y)]
       =\iint e^{-u-v-s(u^2+v^2)/2}
                         \frac{\sinh(tuv)}{uv}\,du\,dv,
 \qquad R(s)=F_s(s),                                         \tag{17}
\]
where the subscript on the expectation now uses common variance \(s>0\).
The absolute expectation exchange is bounded by \(s e^{-u-v}\), using
the sine-product bound from Section 1; the displayed integral is bounded
by \(|t|e^{-u-v}\). Differentiation in \(t\) is dominated by
\(e^{-u-v}\), so \(F_s'(t)=B_s(t)>0\). In particular \(F_s(0)=0\),
\(F_s(t)>0\) for \(t>0\), and \(0<R(s)<\pi^2/4\).

Let \(\rho\in[-1,1)\) be the input correlation. At layer two the Gaussian
preactivation variance and covariance are
\[
 q_2=1+\varepsilon^2R(1),\qquad
 c_2=1+\varepsilon^2F_1(\rho).
\]
At layer three they are precisely
\[
 q=\mathbb E[(H^{(2)}_{01})^2]
     =1+\varepsilon^2R(q_2),\qquad
 c=\mathbb E[H^{(2)}_{01}H^{(2)}_{02}]
     =1+\varepsilon^2F_{q_2}(c_2).                           \tag{18}
\]
The cross terms linear in \(f\) vanish because each preactivation marginal
is centered Gaussian and \(f\) is odd. The independent centered Gaussian
weight action gives these second moments as its covariance entries.

Since \(|F_1(\rho)|\le R(1)<\pi^2/4\), we have \(c_2>0\).
Furthermore
\[
 q_2-c_2=\frac{\varepsilon^2}{2}
                  \mathbb E[(f(G_1)-f(G_2))^2]>0.
\]
Indeed \(G_1-G_2\) has variance \(2(1-\rho)>0\), and strict monotonicity
of \(f\) makes the squared difference positive almost surely. This proof
also covers \(\rho=-1\). Strict increase of \(F_{q_2}\) now proves
\[
                  1<c<q<1+\frac{\pi^2}{400}.                \tag{19}
\]
Thus no covariance degeneracy in Section 3 occurs at the actual top-layer
initialization, even for antiparallel inputs. Both modes have strictly
negative curvature and an indefinite full matrix. Since \(c>0\), (7)
also gives \(K_+<K_-<0\): the opposite-label curvature includes a strict
cancellation that is absent in the same-label mode.

## 5. Actual first nonzero top response coefficients

Here \(\Delta\) is exactly the mesh parameter in equations (1)--(2) of
TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md, whose readout update has coefficient
\(\Delta/2\). This calculation applies for any permitted mesh with at
least one step. It does not silently identify this auxiliary clock and
its prescribed label forcing with the full residual-driven physical
training clock.

Use the bootstrap's exactly zero initial readout, its cuts satisfying
\(\tau(0)=0,\tau'(0)=1\), and its rule that deterministic coefficients
and Gaussian covariance parameters are fixed during formal partial
differentiation. At time zero,
\[
 W^{(4)}_0=\delta^{(3)}_{0a}=0
 \quad\hbox{as formal expressions},\qquad B^{(3)}_{0a,0b}=0.
\]
On the attained law the reverse fields and lower backward fields are
zero as well. The first bottom update and the first two hidden-matrix
updates consequently vanish in value. Equivalently, directly from the
scalar law,
\[
 H^{(1)}_{1a}=H^{(1)}_{0a},\qquad
 H^{(2)}_{1a}=H^{(2)}_{0a},\qquad
 \xi^{(3)}_{1a}=\xi^{(3)}_{0a}\quad\hbox{almost surely}.       \tag{20}
\]
For the last equality the covariance rule gives
\(\mathbb E[(\xi^{(3)}_{1a}-\xi^{(3)}_{0a})^2]
=\mathbb E[(H^{(2)}_{1a}-H^{(2)}_{0a})^2]=0\).
The corresponding equality for \(\xi^{(2)}_1,\xi^{(2)}_0\) follows first
from the equality of the bottom activations; all forward response terms
at this step multiply attained zero backward fields.

Equality (20) is not a license to identify formal source coordinates.
Before differentiating, the exact top expressions are
\[
 Z^{(3)}_{0a}=\xi^{(3)}_{0a},\qquad
 Z^{(3)}_{1a}=\xi^{(3)}_{1a},\qquad
 \delta^{(3)}_{1a}
   =\frac\Delta2\sum_d y_d\phi(\xi^{(3)}_{0d})
                                 \phi'(\xi^{(3)}_{1a}).     \tag{21}
\]
The second equality holds even formally: the past top backward field
\(\delta^{(3)}_0\) is identically zero. Differentiating (21) in distinct
slots gives
\[
 \begin{split}
 \frac{\partial\delta^{(3)}_{1a}}{\partial\xi^{(3)}_{0b}}
    &=\frac\Delta2 y_b\phi'(\xi^{(3)}_{0b})
                                  \phi'(\xi^{(3)}_{1a}),\\
 \frac{\partial\delta^{(3)}_{1a}}{\partial\xi^{(3)}_{1b}}
    &=\Delta\mathbf1_{a=b}
       V_\sigma(\xi^{(3)}_{01},\xi^{(3)}_{02})
                                  \phi''(\xi^{(3)}_{1a}).
 \end{split}                                                    \tag{22}
\]
Only after these differentiations may (20) be used in expectations.
The learned-covariance part of \(B^{(3)}_{1a,0b}\) is zero because it
contains \(\delta^{(3)}_{0b}=0\); the current coefficient has no such
part, by the strict-past indicator in the scalar law. With
\(P_{ab}=\mathbb E[\phi'(Z_a)\phi'(Z_b)]\), the exact first coefficients
are therefore
\[
 \begin{split}
 B^{(3)}_{1a,0b}&=\frac\Delta2 y_b P_{ab},\\
 B^{(3)}_{1a,1b}&=\Delta\mathbf1_{a=b}\,y_a K_\sigma.
 \end{split}                                                    \tag{23}
\]
These are exact step-one identities, not merely leading-order
approximations. At actual initialization every historical entry is
nonzero; both current diagonal entries are nonzero and the current
off-diagonal entries are zero. In the exceptional \(c=-q,\sigma=+1\)
case the current block vanishes, while the historical block remains.

Writing \(Y=\operatorname{diag}(1,\sigma)\), the two blocks are
\[
 B^{(3)}_{1,0}=\frac\Delta2 P Y,\qquad
 B^{(3)}_{1,1}=\Delta K_\sigma Y,
\]
and hence
\[
 YB^{(3)}_{1,0}=\frac\Delta2 YPY,\qquad
 YB^{(3)}_{1,1}=\Delta K_\sigma I,\qquad
 Y\bigl(B^{(3)}_{1,0}+B^{(3)}_{1,1}\bigr)=\Delta M.          \tag{24}
\]
Thus \(M\) is the label-conjugated sum of the historical and current
blocks, divided by \(\Delta\); it is not the current block alone. On
the first-step attained values, (20) lets this sum act on the common
\(H^{(2)}_0=H^{(2)}_1\) in the reverse query. It does not merge their
formal source dependence for later calculations.

In particular, the historical zero-variance reverse source must still
be retained:
\[
 q^{(2)}_{0a}=\zeta^{(2)}_{0a}=0\ \hbox{almost surely},\qquad
 \delta^{(2)}_{0a}
   =\phi'(\xi^{(2)}_{0a})\tau_{R_2}(\zeta^{(2)}_{0a}),\qquad
 \left.\frac{\partial\delta^{(2)}_{0a}}
 {\partial\zeta^{(2)}_{0b}}\right|_{\text{attained law}}
   =\mathbf1_{a=b}\phi'(\xi^{(2)}_{0a}).                    \tag{25}
\]
For example, \(H^{(2)}_{0a}\) has zero derivative in this reverse source,
but the time-one formal map has derivative
\[
 \left.\frac{\partial H^{(2)}_{1a}}
 {\partial\zeta^{(2)}_{0b}}\right|_{\text{attained law}}
 =A^{(2)}_{1a,0b}\phi'(\xi^{(2)}_{1a})\phi'(\xi^{(2)}_{0b}), \tag{26}
\]
which need not vanish. Thus two distinct degeneracies must be respected:
the zero-variance difference of current and historical forward sources in
(20), and the zero-variance historical reverse source in (25). Neither
allows differentiation after deleting or identifying source slots.

The bootstrap uses an exactly zero finite initial readout. The contract
instead prescribes independent initial readout entries with variance
\(n^{-2}\); their initial limiting scalar readout is zero. Equations
(23)--(26) are exact for the stated bootstrap and its source convention;
they are not asserted as exact finite-width identities for the contract's
nonzero random initial readout.

## 6. Claim status and the unproved extension

| Claim | Status | Scope and proof |
|---|---|---|
| Signed curvature (7)--(9) | Proved | All centered Gaussian pairs in the stated range; Sections 1--2. |
| Full matrix eigenvalues and inertia (10)--(15) | Proved | Same class, including each degeneracy explicitly; Section 3. |
| Actual top initialization satisfies (19) | Proved | Fixed activation and input correlation \(\rho<1\), using the initial scalar covariance recursion. |
| First nonzero source coefficients (23)--(24) | Exact under the supplied scalar-law convention | Distinct source slots, frozen deterministic coefficients and covariance parameters, exactly zero bootstrap readout; Section 5. |
| Preservation of these signs on trained paths | Open here | No bridge from the Gaussian initial identities to the trained response system has been established. |

At positive training time, Gaussian source variables do not make the
forward fields themselves jointly centered Gaussian: the scalar law adds
response terms involving past backward fields. The readout is a history
sum, not generally a scalar multiple of the current
\((\phi(Z_1)+\sigma\phi(Z_2))/2\). Formal differentiation also includes
the intervening forward response derivatives, and later \(B^{(3)}\)
coefficients contain the learned-covariance term that vanished at step
one. The elementary Gaussian factorization (3), the odd-marginal
cancellation used in (7), and the two-by-two reduction (24) therefore
cannot simply be carried forward.

Specifically unproved are a corresponding sign for
\(y_a\mathbb E[W^{(4)}_k\phi''(Z^{(3)}_{ka})]\) on every trained attained
law, a sign or spectral control for the full causal family of current and
historical top response coefficients after their response chains are
included, and an argument turning such control into bounds on a finite
training horizon. The initial positive and negative eigenvalues do not
by themselves prove stability or instability of that history-dependent
evolution, all-time bounds, or the full two-label convergence theorem.
No claim from an unrelated route or audit file is superseded by this note.

Source scope and provenance: the exact-model section of
CONTRACT_AND_LEDGER.md, lines 10--81, and the scalar law, source convention,
and base case in TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md, lines 26--150,
are the mathematical source passages used above. Their SHA-256 hashes,
computed on the literal line slices including their line endings, are:

```text
CONTRACT_AND_LEDGER.md:10--81
e633994927965510b9c0605d27ed221b33de485caa7cda2bb9029a6343707d0e
TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md:26--150
907fd403144823a76631119cab844cba037c156491f55b17bd882907387bed38
```

The procedural solve-math-rigorously and investigate-conjectures skills
were read directly from /etc/codex/skills, together with the latter's
research-contract, evidence-ledger, and adversarial-audit references.
Their role was to require complete elementary proofs, preserve the exact
model and source-slot convention, and separate the initial result from
the unproved trained-path extension. No heavy external theorem is used.
