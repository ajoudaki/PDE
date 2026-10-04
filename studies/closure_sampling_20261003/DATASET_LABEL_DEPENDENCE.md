# Dataset dependence of the real small-label fitting threshold

2026-10-04. Scoped continuation of `closure_sampling_20261003`.
This is an internally derived deterministic result for the existing dense
network and its existing weighted autonomous compression. It does not
quantify the additional stochastic source hypotheses in the deep analytic
compression theorem. Scientific inputs read: `paper/main.tex`,
`paper/proof_alltime.tex`, `GENERAL_WEIGHTED_COMPARISON.md`, and
`GENERAL_ANALYTIC_COMPRESSION.md`. No other study was consulted.

The useful conclusion is stronger than the activity-only bootstrap:
**an explicit sufficient RMS label bound is proportional to the normalized
initial feature-Gram gap**. A direct Gram perturbation gives a sufficient
power $3/2$, comparison of feature singular values improves that power to
$5/4$, and the exact gradient-flow energy identity improves it to $1$.
These are sufficient bounds, not necessity or optimality assertions.

## 1. Model, normalization, and the explicit threshold

Let \(v_a=x_a/\sqrt d\in S^{d-1}\), \(a=1,\ldots,m\). The depth is
\(L\ge2\), and all hidden widths are \(n\). Set

\[
 z_a^{(1)}=Av_a,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
 h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
 f_a=w^\top h_a^{(L)}/n.
\]

Choose bounds \(B,s,K\ge1\) such that

\[
 \max_\ell\|\phi_\ell\|_\infty\le B,\qquad
 \max_\ell\|\phi_\ell'\|_\infty\le s,\qquad
 \max_{\ell\ge2}\|W_0^{(\ell)}\|_{\rm op}\le K.
 \tag{1}
\]

Assume the activations are \(C^2\), with bounded second derivatives,
and \(w(0)=0\). Being bounded and holomorphic on a complex strip implies all these real
activation assumptions on a narrower strip. The second derivative bound
ensures local uniqueness; its size does not enter the fitting constants.
No bound on \(A_0\) is needed here because the activation values are bounded.

For a neuron vector write \(\|u\|_n=\|u\|_2/\sqrt n\), and for a sample
vector write \(\|c\|_m^2=m^{-1}\sum_a c_a^2\). Define

\[
 c_a=y_a-f_a,\quad \rho=\|c\|_m,\quad Y=\|y\|_m,
 \qquad \mathcal L=\rho^2.
\]

The backward responses are

\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
 \qquad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

With mobilities \((n,1,\ldots,1,n)\), physical gradient flow is

\[
 \dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,\qquad
 \dot W^{(\ell)}=\frac2{mn}\sum_a
        c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad
 \dot w=\frac2m\sum_a c_ah_a^{(L)}.
 \tag{2}
\]

Let \(H_L(t)\in\mathbb R^{n\times m}\) have columns \(h_a^{(L)}(t)\).
The unnormalized-in-samples feature Gram is \(G(t)=H_L(t)^\top H_L(t)/n\).
Assume a known lower bound

\[
 \Gamma_w(0):=G(0)/m\succeq\lambda I_m,\qquad \lambda>0.
 \tag{3}
\]

Thus \(\lambda\) is a gap of \(G/m\), not of \(G\). In particular,

\[
 \lambda\le \frac{\operatorname{tr}\Gamma_w(0)}m\le\frac{B^2}{m}\le B^2.
 \tag{4}
\]

Here are fully specified constants depending only on \(B,s,K,L\):

\[
 R=K+1,\qquad b_\ell=s^{L-\ell+1}R^{L-\ell},
 \]
\[
 F_1=s b_1,\qquad
 F_\ell=s\bigl(B^2b_\ell+R F_{\ell-1}\bigr)\quad(2\le\ell\le L),
 \qquad C_* =\max\{1,B^2b_1,F_L\}.
 \tag{5}
\]

**Proposition.** If

\[
                    Y\le \frac{\lambda}{4\sqrt{C_*}},
 \tag{6}
\]

then (2) exists uniquely for all physical time and converges to an
interpolating parameter state. For all \(t\ge0\),

\[
 \Gamma_w(t)\succeq\frac{9\lambda}{16}I_m,\qquad
 \rho(t)\le Ye^{-\lambda t/2},\qquad
 \int_t^\infty\rho(u)\,du\le\frac{2\rho(t)}\lambda.
 \tag{7}
\]

The displayed decay rate is deliberately weaker than the improved Gram
margin. In the mobility metric,

\[
 \|\dot\theta\|_{\rm mob}^2
 :=\frac{\|\dot A\|_F^2}{n}
   +\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F^2
   +\frac{\|\dot w\|_2^2}{n},
\]

the total remaining path length satisfies

\[
 \int_t^\infty\|\dot\theta(u)\|_{\rm mob}\,du
 \le\frac{2\rho(t)}{\sqrt\lambda},\qquad
 \|w(t)\|_n\le\frac{2Y}{\sqrt\lambda}.
 \tag{8}
\]

Every sphere query, not only every training input, satisfies

\[
 \sup_{x\in\sqrt d S^{d-1}}|f(t,x)-f(\infty,x)|
 \le\left(\frac{4B^2}{\lambda}
               +\frac{16F_LY^2}{\lambda^2}\right)\rho(t).
 \tag{9}
\]

No constant in (5)--(9) hides the sample count, input geometry, width,
or a smallest neuron mass. On the unit input sphere those enter the
fitting condition only through the actual normalized gap \(\lambda\).

## 2. Proof: gradient length controls the hidden displacement

The proof stops the solution at an operator or Gram exit, uses the
gradient-flow energy identity to bound the readout, and obtains a
quadratic hidden displacement. Comparing singular values then gives
strict margins at both proposed exits.

The exact residual equation is

\[
 \dot c=-2\Gamma c,
\]
\[
 \Gamma_{ab}=\frac1m\left[
  \langle h_a^{(L)},h_b^{(L)}\rangle_n
  +\langle\delta_a^{(1)},\delta_b^{(1)}\rangle_n(v_a^\top v_b)
  +\sum_{\ell=2}^L
   \langle\delta_a^{(\ell)},\delta_b^{(\ell)}\rangle_n
   \langle h_a^{(\ell-1)},h_b^{(\ell-1)}\rangle_n\right],
 \tag{10}
\]

where \(\langle u,v\rangle_n=u^\top v/n\). Each term is a Gram
matrix, including the first-layer term, which is the Gram of tensor
products \(\delta_a^{(1)}\otimes v_a\). Therefore
\(\Gamma\succeq\Gamma_w\), without an orthogonality assumption.
The factors in (2) give the exact energy identity

\[
 -\frac{d}{dt}\rho^2
  =\|\dot\theta\|_{\rm mob}^2
  =4\langle c,\Gamma c\rangle_m.
 \tag{11}
\]

Indeed, ordinary gradient flow with the displayed mobilities gives
\(-\dot{\mathcal L}
=\|\dot A\|_F^2/n+\sum_\ell\|\dot W^{(\ell)}\|_F^2
+\|\dot w\|_2^2/n\); differentiating the residual loss using (10)
gives the last equality.

Stop at the first time that either a hidden operator moves
to norm \(R\), or \(\lambda_{\min}(\Gamma_w)\) reaches \(\lambda/4\).
Before this stop, (10)--(11) imply

\[
 -\dot\rho\ge\frac\lambda2\rho,\qquad
 \|\dot\theta\|_{\rm mob}\ge\sqrt\lambda\,\rho,
 \qquad
 \|\dot\theta\|_{\rm mob}
   =\frac{2\rho(-\dot\rho)}{\|\dot\theta\|_{\rm mob}}
   \le\frac{2(-\dot\rho)}{\sqrt\lambda}.
 \tag{12}
\]

These identities are used where \(\rho>0\). If a zero residual is
reached, all velocities are zero and local uniqueness gives a stationary
continuation. The case \(Y=0\) is stationary from the start.

Integrating (12) and using \(w(0)=0\) gives the useful refined bound

\[
 \|w(t)\|_n\le\frac{2(Y-\rho(t))}{\sqrt\lambda}.
 \tag{13}
\]

Before the stop, the backward recursion gives
\(\max_a\|\delta_a^{(\ell)}\|_n\le b_\ell\|w\|_n\).
Cauchy--Schwarz over samples in (2), \(\|v_a\|=1\), and
\(\|h_a^{(\ell)}\|_n\le B\), imply

\[
 \frac{\|\dot A\|_F}{\sqrt n}\le2b_1\rho\|w\|_n,
 \qquad
 \|\dot W^{(\ell)}\|_F\le2B b_\ell\rho\|w\|_n.
 \tag{14}
\]

From \(-\dot\rho\ge\lambda\rho/2\),

\[
 \int_0^t\rho(u)(Y-\rho(u))\,du
 \le\frac2\lambda\int_0^t(-\dot\rho)(Y-\rho)\,du
 =\frac{(Y-\rho(t))^2}{\lambda}\le\frac{Y^2}{\lambda}.
 \tag{15}
\]

Substitution of (13) into (14) consequently yields

\[
 \frac{\|A(t)-A_0\|_F}{\sqrt n}
      \le\frac{4b_1Y^2}{\lambda^{3/2}},\qquad
 \|W^{(\ell)}(t)-W_0^{(\ell)}\|_F
      \le\frac{4B b_\ell Y^2}{\lambda^{3/2}}.
 \tag{16}
\]

Forward subtraction gives a bound uniform in every unit vector \(v\).
At layer one use the first inequality in (16) and the slope bound \(s\).
At a later layer use

\[
 z^{(\ell)}(t)-z^{(\ell)}(0)
  =(W^{(\ell)}(t)-W_0^{(\ell)})h^{(\ell-1)}(0)
    +W^{(\ell)}(t)(h^{(\ell-1)}(t)-h^{(\ell-1)}(0)).
\]

Induction with precisely the constants in (5) proves

\[
 \sup_{\|v\|=1}\|h^{(\ell)}(t,v)-h^{(\ell)}(0,v)\|_n
       \le\frac{4F_\ell Y^2}{\lambda^{3/2}}.
 \tag{17}
\]

Let \(T(t)=H_L(t)/\sqrt{mn}\), a linear map from Euclidean sample
space to Euclidean neuron space. Its initial smallest singular value is
at least \(\sqrt\lambda\). For every sample vector \(u\), the triangle
inequality gives

\[
 \|T(t)u\|_2\ge
 \bigl(\sqrt\lambda-\|T(t)-T(0)\|_{\rm op}\bigr)\|u\|_2,
\]

and (17) bounds the operator difference by its Frobenius norm, at most
\(4F_LY^2/\lambda^{3/2}\). Under (6), this is at most
\(\sqrt\lambda/4\). Hence
\(\Gamma_w(t)=T(t)^\top T(t)\succeq9\lambda I_m/16\), a strict
improvement on the stopped margin.

For the operator boundary, (4)--(6) and \(b_\ell\le b_1\) give

\[
 \|W^{(\ell)}(t)-W_0^{(\ell)}\|_{\rm op}
 \le\frac{B b_\ell\sqrt\lambda}{4C_*}
 \le\frac{B^2b_1}{4C_*}\le\frac14.
 \tag{18}
\]

This too is a strict improvement on the stopped margin. Equations
(12)--(18) bound the whole finite parameter state on the maximal stopped
interval. Local existence and uniqueness follow from the locally
Lipschitz vector field supplied by the \(C^2\) activations.
A finite maximal time would have a limiting
parameter state, by the finite path length in (12), from which local
existence extends. Neither stop occurs, proving global continuation.

Integrating (12) from any \(t\) proves (7)--(8). Finite remaining path
length gives parameter convergence, and residual decay makes the limit
interpolating. For completeness, differentiating the forward recursion
and using (14) gives

\[
 \sup_{\|v\|=1}\|\dot h^{(\ell)}(t,v)\|_n
       \le 2F_\ell\rho(t)\|w(t)\|_n.
\]

Consequently
\(|\dot f(t,x)|\le2B^2\rho+2F_L\rho\|w\|_n^2\).
Use (8) and the activity tail in (7) to obtain (9).

## 3. Why the simpler arguments give powers 3/2 and 5/4

If one uses only residual activity \(S(t)=\int_0^t\rho\), bounded
features imply \(\|w(t)\|_n\le2BS(t)\). Substituting in (14) and
integrating \(S\,dS\) gives

\[
 \frac{\|A-A_0\|_F}{\sqrt n}\le2B b_1S^2,\qquad
 \|W^{(\ell)}-W_0^{(\ell)}\|_F\le2B^2b_\ell S^2,
 \qquad
 \max_a\|h_a^{(L)}-h_a^{(L)}(0)\|_n\le2B F_LS^2.
 \tag{19}
\]

A direct Gram difference bound is \(O(S^2)\). Preserving a gap of
size \(\lambda\) this way requires \(S=O(\sqrt\lambda)\), and
\(S\lesssim Y/\lambda\) gives a sufficient label scale
\(Y=O(\lambda^{3/2})\).

The singular-value argument used above only needs a feature perturbation
of size \(O(\sqrt\lambda)\). Equation (19) therefore permits
\(S=O(\lambda^{1/4})\), yielding \(Y=O(\lambda^{5/4})\).
For example, with the same explicit constant \(C_*\), set

\[
 S_0=\frac{\lambda^{1/4}}{\sqrt{8B C_*}}.
\]

For \(S\le S_0\), (19), (4), and (5) give hidden displacement at
most \(1/4\) and feature singular-value perturbation at most
\(\sqrt\lambda/4\). Thus the activity-only first-exit proof closes if

\[
                Y\le\frac{\lambda^{5/4}}{4\sqrt{8B C_*}},
 \tag{20}
\]

because (12) then bounds actual activity by \(2Y/\lambda\le S_0/2\).
The stronger threshold (6) uses extra structure already present in this
same gradient flow: the readout norm is \(O(Y/\sqrt\lambda)\), rather
than the coarser \(O(Y/\lambda)\) obtained by integrating its speed
against residual activity alone.

## 4. Finite initialized gap, limiting gap, and sample count

For canonical Gaussian initialization define \(Q^{(0)}_{ab}=v_a^\top v_b\)
and recursively

\[
 Q^{(\ell)}_{ab}
   =\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \qquad Z\sim N(0,Q^{(\ell-1)}).
 \tag{21}
\]

Let \(\lambda_\infty=\lambda_{\min}(Q^{(L)}/m)>0\).
For fixed \(d,m,L\), the assigned sources prove \(G(0)\to Q^{(L)}\)
in probability. On the event

\[
 \|G(0)/m-Q^{(L)}/m\|_{\rm op}\le\lambda_\infty/2
 \quad\hbox{and}\quad \max_{\ell\ge2}\|W_0^{(\ell)}\|_{\rm op}\le K,
 \tag{22}
\]

the proposition applies with \(\lambda=\lambda_\infty/2\), so a
deterministic sufficient bound is

\[
                 Y\le\frac{\lambda_\infty}{8\sqrt{C_*}}.
 \tag{23}
\]

The event has probability tending to one for a sufficiently large fixed
\(K\). This statement does not assert a quantitative width threshold or
a uniform theorem for growing sample count.

If instead a source writes \(Q^{(L)}\succeq\gamma I_m\), the normalized
gap is \(\lambda_\infty=\gamma/m\) when \(\gamma\) is the exact
smallest eigenvalue, or at least \(\gamma/m\) when it is a lower bound.
Thus (23) reads \(Y\le\gamma/(8m\sqrt{C_*})\). Omitting the factor
\(m\) would change the physical mean-loss dynamics. The label size here is
RMS, not the Euclidean norm \(\|y\|_2=\sqrt mY\).

The dataset enters quantitatively through this spectral gap. Pairwise
nonproportional sphere inputs and nonconstant bounded activations are a
sufficient positivity criterion from the assigned sources, but positivity
alone gives no numerical lower bound. Nearly coincident inputs can make
the gap arbitrarily small: if two inputs coalesce, their two kernel
columns coincide, and continuity of (21) sends a corresponding eigenvalue
to zero. Duplicate inputs give zero gap outright. Antipodal relations can
also force zero gap for odd activations. These observations describe the
scope of this certificate; zero gap does not by itself imply that every
label vector is unfittable.

Even with bounded activations and favorable geometry,
\(\lambda_\infty\le B^2/m\) by the trace bound. Consequently this
particular worst-label-direction certificate is not sample-uniform.
It makes no assertion that the power of the gap or sample dependence is
necessary for fitting.

## 5. Weighted networks and the separate comparison requirement

For the existing compressed network, replace each neuron norm by
\(\|u\|_{D_\ell}^2=u^\top D_\ell u\), where the positive weights have
total mass one. Replace hidden Frobenius norms by
\(\|D_\ell^{1/2}BD_{\ell-1}^{-1/2}\|_F\), and first-weight norms by
\(\|D_1^{1/2}A\|_F\). The forward/backward equations use the weighted
adjoint and the exact autonomous updates of the assigned comparison note.

All preceding identities persist. In particular the loss dissipation is
the sum of the squared weighted block velocities: this follows by pairing
each weighted gradient with its own velocity. Rank-one Hilbert--Schmidt
norms are products of their weighted vector norms. The feature map in the
singular-value argument is \(D_L^{1/2}H_L/\sqrt m\).
Bounded coordinate activations still have norm at most \(B\) because the
weights sum to one. The initialized compressed operators have norm at
most \(K\), and its normalized initialized feature Gram is exactly the
original one. Therefore the same threshold (6) and all the same bounds
hold independently of selected width and smallest positive mass.

Fitting does not automatically supply a small comparison amplification.
Here is a precise conditional statement separating that question. Suppose
a comparison has nonnegative, continuous and locally absolutely continuous
state error \(d(t)\) and residual error \(u(t)\), as inherited from the
trajectory norms, with \(d(0)=u(0)=0\) and source tolerance \(\epsilon>0\), and
has established

\[
 D^+u\le-\kappa u+B_{\rm cmp}\rho(d+\epsilon),\qquad
 d(t)\le A_1\int_0^t u
                 +A_2\int_0^t\rho(d+\epsilon).
 \tag{24}
\]

Here \(A_1,A_2,B_{\rm cmp}\) are specified comparison constants, and
\(\rho\) is the true reference residual. Integrating the first inequality
and discarding its nonnegative terminal term gives

\[
 d(t)\le\left(A_2+\frac{A_1B_{\rm cmp}}\kappa\right)
                    \int_0^t\rho(d+\epsilon).
 \tag{25}
\]

If

\[
 \Theta:=\left(A_2+\frac{A_1B_{\rm cmp}}\kappa\right)
                      \int_0^\infty\rho<1,
 \tag{26}
\]

taking the time supremum on each finite interval gives
\(\sup_t d(t)\le\Theta\epsilon/(1-\Theta)\).
Without (26), an integrating factor gives the always valid bound
\(\sup_t d(t)\le(e^\Theta-1)\epsilon\).

For the one-reference argument, \(B_{\rm cmp},A_2\) include a factor
\(1+M\), where \(M\) bounds the actual reference carrier coordinates.
The proposition provides \(\kappa=\lambda/2\) and
\(\int\rho\le2Y/\lambda\). If the remaining comparison constants are
bounded independently of the gap, a sufficient absorption condition has
the conservative form

\[
        Y\le c\,\frac{\lambda^2}{(1+\lambda)(1+M)}.
 \tag{27}
\]

This is an additional conditional stability restriction, not a conclusion
of (6). A carrier estimate \(M=O(\sqrt{\log n})\) does not give (27)
for one fixed positive label size at all widths. The existing analytic
compression proof instead permits the resulting exponential factor and
requests more accurate source approximation.

Finally, real fitting/activity control alone does not prove the deep
complex-source theorem or its initialization-only approximation. The
allowed analytic synthesis invokes separate source and carrier results;
those full proofs were outside this assignment's scientific input scope.
Their smallness constants may impose further restrictions, and may have
dataset dependence beyond the explicit real fitting threshold proved
here. Neither (6), (20), nor (23) is asserted to replace those restrictions
or the separate memory-closure defect bounds in the manuscript.
