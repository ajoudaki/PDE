# General-data independent-copy concentration: a proved near-root bound

2026-10-03. Continuation of this study's finite-network concentration
investigation. The new question extends AUTONOMOUS_SELF_AVERAGING.md to
the scope of DEPTH_EXTENSION_RESULT.md; it does not change the population
bias question or import another study. No experiments or manuscript edits.

**Status.** The theorem below gives an unconditional, fixed-confidence
independent-copy bound of order
\(n^{-1/2}\exp\{C\sqrt{\log(e+n)}\}\), with the full physical-time
supremum inside the query integral. It is a proved weaker result, not
a strict \(C_\delta n^{-1/2}\) theorem. The strict theorem in this
general scope remains unresolved. An unconditional expectation of the
original all-time error, or literal variance over every initialization,
is not claimed.

The finite-network carrier theorem and physical tube used here are the
internally checked results assembled in DEPTH_EXTENSION_RESULT.md.
SELF_AVERAGING_FEEDBACK_ROUTE.md reconstructs the deterministic
two-initialization estimate. The probabilistic extension argument below
does not require a rate for the probability of the good event.

## 1. Model, assumptions, and conclusion

Fix \(L\ge2\) hidden layers, width \(n\), input dimension \(d\), and
a finite training set \((x_a,y_a)_{a=1}^m\), with
\(v_a=x_a/\sqrt d\). The dense network is
\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
 f_n(t,x)=w(t)^\top h^{(L)}(t,x)/n.
 \tag{1}
\]
Its loss is \(m^{-1}\sum_a(f_n(t,x_a)-y_a)^2\), and its gradient-flow
mobilities are \((n,1,\ldots,1,n)\). Initialize the first weights with
independent \(N(0,1)\) entries, every hidden matrix with independent
\(N(0,1/n)\) entries, and \(w(0)=0\). All blocks are independent.
The activations are \(C^3\) with globally bounded first three
derivatives. Activation values may grow linearly.

Use exactly the fixed-data and small-label hypotheses of
DEPTH_EXTENSION_RESULT.md: a positive limiting initial readout-feature
Gram gap on the compatible weighted data quotient, and sufficiently
small fixed label RMS \(Y\). Its activation/parity criteria specify when
this gap follows automatically for fixed sphere data. No input
orthogonality, algorithmic clipping, or added response hypothesis is
imposed here. Constants can depend on depth, the fixed data and gap,
activation bounds, and the fixed small-label threshold. They cannot
depend on width or physical time.

The formulas below display uniform sample weights. For a compatible
duplicate or parity quotient, apply the proof to its fixed positive
weights \(p_a\), replacing \(m^{-1}\sum_a\) by \(\sum_a p_a\) and
the residual RMS by \((\sum_a p_a r_a^2)^{1/2}\). The tangent gap and
matrix norms are then understood after conjugation by
\(\operatorname{diag}(\sqrt{p_a})\), as explicitly derived in
SELF_AVERAGING_FEEDBACK_ROUTE.md. This retains the original predictions
and physical time.

Let \(f_n'\) be a second, independently initialized and trained copy of
(1). For a fixed probability law \(\mu\) with
\(\int\|x\|_2^2\,d\mu(x)<\infty\), define
\[
 \mathcal E_\mu(f,g)
 =\left(\int\sup_{t\in[0,\infty]}|f(t,x)-g(t,x)|^2\,d\mu(x)\right)^{1/2}.
 \tag{2}
\]
The endpoint \(t=\infty\) means the fitted limit on the events used in
the theorem.

**Theorem.** There are fixed \(C,K>0\) such that, for every
\(\delta>0\), for all sufficiently large \(n\) depending on \(\delta\),
\[
 \Pr\left\{\mathcal E_\mu(f_n,f_n')
 \le {C_{\delta,\mu}\over\sqrt n}
             e^{K\sqrt{\log(e+n)}}\right\}\ge1-\delta.
 \tag{3}
\]
The same conclusion holds around a deterministic finite-width center
\(c_n(t,x)\) constructed below. That center is not identified with the
mean of autonomous training or with the population predictor.
In particular, for every fixed \(\varepsilon>0\), (3) implies
\(C_{\delta,\mu,\varepsilon}n^{-1/2+\varepsilon}\), including the
entire training trajectory and its fitted limit.

## 2. A deterministic estimate between two good initializations

Write the independent standard Gaussian roots as
\[
 G=(W_0^{(1)},H_0^{(2)},\ldots,H_0^{(L)}),\qquad
 H_0^{(\ell)}=\sqrt n W_0^{(\ell)}.
 \tag{4}
\]
Thus \(G\) is a standard Gaussian vector in
\(N_n=nd+(L-1)n^2\) dimensions; the zero readout is not a random
coordinate. Let \(\Omega_n\) be the deterministic set of roots on which
the previously proved physical tube, exponential fitting, and carrier
maximum hold, with fixed constants:
\[
 \rho(t)\le Ye^{-\kappa t},\qquad
 \max_{\ell,a,i}\sup_{t\ge0}|k_{a,i}^{(\ell)}(t)|
 \le M_n=C_0Y\sqrt{\log(e+n)}.
 \tag{5}
\]
Here
\(k_a^{(L)}=w\),
\(k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\),
and
\(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}\).
The physical tube includes bounded hidden operator norms, bounded
first-weight Frobenius norm divided by \(\sqrt n\), bounded training
feature RMS, backward RMS \(CY\), and a uniform positive training
tangent gap. The established finite-network theorem gives
\(\Pr(G\in\Omega_n)\to1\).

For two roots \(G,\widetilde G\in\Omega_n\), let
\[
 D(t)=
 {\|W^{(1)}-\widetilde W^{(1)}\|_F\over\sqrt n}
 +\sum_{\ell=2}^L\|W^{(\ell)}-\widetilde W^{(\ell)}\|_F
 +{\|w-\widetilde w\|_2\over\sqrt n}.
 \tag{6}
\]
The following estimate holds globally for pairs in this set:
\[
 \sup_{t\ge0}D(t)\le C e^{CY(1+M_n)}D(0),\qquad
 D(0)\le C_L\|G-\widetilde G\|_2/\sqrt n.
 \tag{7}
\]
For clarity, the argument is included. Forward subtraction bounds each
training feature difference in RMS by \(CD\). Descending backward
subtraction bounds each response difference in RMS by
\(C(1+M_n)D\), using a gate difference times a carrier from just
one reference path. Fixed depth adds these factors rather than
raising \(M_n\) to a depth-dependent power.

Let \(e=\widetilde r-r\). The exact residual equation is
\[
 \dot e=-2\widetilde\Gamma e
        -2(\widetilde\Gamma-\Gamma)r,\qquad e(0)=0,
 \tag{8}
\]
where \(\dot r=-2\Gamma r\). The initial residuals agree because
both initial readouts vanish. Product expansion of the parameter-gradient
Gram gives
\(\|\widetilde\Gamma-\Gamma\|_{\rm op}\le C(1+M_n)D\).
The uniform tangent gap and the norm inequality for (8) yield
\[
 \int_0^t\|e(s)\|_m\,ds
 \le C(1+M_n)\int_0^t\rho(s)D(s)\,ds.
 \tag{9}
\]
Subtracting the parameter equations gives
\[
 D(t)\le D(0)+C\int_0^t\|e(s)\|_m\,ds
             +C(1+M_n)\int_0^t\rho(s)D(s)\,ds.
 \tag{10}
\]
Insert (9), use \(\int_0^\infty\rho\le Y/\kappa\), and apply
scalar Gronwall. This proves (7). The estimates compare the two actual
fitting paths; they do not require their interpolation in parameter
space to be a fitting path.

For \(B(x)=1+\|x\|_2/\sqrt d\), forward query subtraction implies
\[
 \sup_t|f_n(G;t,x)-f_n(\widetilde G;t,x)|
 \le B(x)\ell_n\|G-\widetilde G\|_2,\qquad
 \ell_n={C e^{K_0\sqrt{\log(e+n)}}\over\sqrt n}.
 \tag{11}
\]
Both the exponent and \(C\) in (11) are deterministic. The physical
speeds also give, on \(\Omega_n\),
\[
 |f_n(t,x)|\le CYB(x),\qquad
 |\partial_t f_n(t,x)|\le CYB(x)e^{-\kappa t}.
 \tag{12}
\]
Indeed each trained hidden matrix moves at Frobenius speed \(CY\rho\),
the first matrix at normalized Frobenius speed \(CY\rho\), and the
readout at RMS speed \(C\rho\). Propagate the first two speeds through
the query forward pass, then differentiate \(w^\top h^{(L)}(x)/n\).
Only bounded slopes, operator bounds, and RMS bounds are used.

The linear dependence on \(B(x)\) in both (11) and (12) is why a second
query moment suffices.

## 3. Extension off the good set is a proof device

The event probability in (5) need not have an \(O(1/n)\) complement.
It would therefore be invalid to discard this complement in an
unconditional variance computation for the actual flow.
Instead extend the scalar observable from the good set.

Compactify physical time by \(u=1-e^{-\kappa t}\), with \(u=1\)
representing the fitted endpoint. Equation (12) makes
\(u\mapsto f_n(G;t(u),x)\) \(CB(x)\)-Lipschitz on \([0,1]\) for
every \(G\in\Omega_n\).
Use the \(n+1\) grid values \(u_j=j/n\), \(0\le j\le n\).
For each \(j,x\), extend the scalar function at \(u_j\) by
\[
 F_{j,x}(G)
 =\inf_{H\in\Omega_n}
     \{f_n(H;t(u_j),x)+B(x)\ell_n\|G-H\|_2\},
 \tag{13}
\]
and truncate its values to the interval
\([-CYB(x),CYB(x)]\) from (12).
This value truncation is applied only to the auxiliary scalar extension,
never to the network or any training signal.
Equation (11) proves that (13) agrees with the actual prediction on
\(\Omega_n\) and is \(B(x)\ell_n\)-Lipschitz on all of
\(\mathbb R^{N_n}\). Truncation preserves both properties.

For sufficiently large \(n\), the set is nonempty. Fix a countable
dense subset of \(\Omega_n\); its infimum gives exactly (13),
by (11). It also proves joint measurability in \(G,x\): finite-width
predictions at finite times are continuous in the query, and endpoint
predictions are their pointwise limits. Thus all subsequent expectations
and query integrals are well-defined.

Put \(c_{n,j}(x)=\mathbb E F_{j,x}(G)\), and interpolate these values
linearly in \(u\) to define \(c_n(t(u),x)\).
This construction is deterministic and uses only width-\(n\) flows.
No population limit or population-bias estimate is used.

## 4. Gaussian concentration and the full time supremum

For completeness, the needed Gaussian fact is:
if \(G\) is standard Gaussian and \(F\) is globally \(l\)-Lipschitz,
\[
 \Pr\{|F(G)-\mathbb EF(G)|>s\}\le
             2e^{-s^2/(2l^2)}.
 \tag{14}
\]
Here is a dimension-independent proof. The Gaussian Ornstein--Uhlenbeck
semigroup satisfies, for positive smooth \(h\),
\[
 \operatorname{Ent}(h)
 =\int_0^\infty
       \mathbb E{|\nabla P_t h|^2\over P_t h}\,dt
 \le {1\over2}\mathbb E{|\nabla h|^2\over h}.
 \tag{15}
\]
The equality follows by differentiating
\(\mathbb E[P_t h\log P_t h]\), Gaussian integration by parts, and
the limits at zero and infinity. For the inequality use
\(\nabla P_t h=e^{-t}P_t\nabla h\), weighted Cauchy--Schwarz
inside \(P_t\), invariance of Gaussian expectation, and
\(\int_0^\infty e^{-2t}dt=1/2\).
Apply (15) to \(h=e^{\lambda F}\). If
\(\psi(\lambda)=\log\mathbb E e^{\lambda F}\), this gives
\(\lambda\psi'(\lambda)-\psi(\lambda)\le\lambda^2l^2/2\).
Integration from zero gives
\(\log\mathbb E e^{\lambda(F-\mathbb EF)}\le\lambda^2l^2/2\).
Chernoff's bound proves (14); smoothing and bounded truncation extend
the argument to Lipschitz functions.

Apply (14) separately to the \(n+1\) extensions in (13), and take a
union bound. Integrating that tail yields
\[
 \mathbb E\max_{0\le j\le n}
       |F_{j,x}(G)-c_{n,j}(x)|^2
 \le C B(x)^2\ell_n^2\log(e+n).
 \tag{16}
\]
For example split the squared-tail integral at
\(2B(x)^2\ell_n^2\log(2n+2)\); the remainder is at most
\(2B(x)^2\ell_n^2\).

On \(\Omega_n\), the original prediction between neighboring grid
points differs from the linear interpolation of its two grid values
by at most \(CB(x)/n\). Comparing this interpolation with \(c_n\)
and then using (16) proves
\[
 \mathbb E\left[
  \mathbf1_{\Omega_n}\sup_{t\in[0,\infty]}
      |f_n(t,x)-c_n(t,x)|^2\right]
 \le C B(x)^2\left[\ell_n^2\log(e+n)+n^{-2}\right].
 \tag{17}
\]
The expression in brackets is understood as zero off \(\Omega_n\);
no fitted endpoint is required there.
Tonelli gives the identical integrated bound with factor
\(\int B(x)^2\,d\mu(x)\).
Markov's inequality, together with
\(\Pr(\Omega_n^c)\to0\), proves a fixed-confidence bound around
\(c_n\). The factor \(\sqrt{\log(e+n)}\) is absorbed into
\(C e^{K_1\sqrt{\log(e+n)}}\).
Apply this bound to both copies, take a union bound, and use the
triangle inequality in (2). This proves (3).

Independence is the intended ensemble interpretation, but the final
union-bound deduction works for any coupling with the two correct
marginal initialization laws.

## 5. The exact gap to strict root width

The only power of width in (3) is \(n^{-1/2}\); the remaining factor
is subpolynomial but unbounded. It must not be hidden in \(C_\delta\).
Small labels make its exponent smaller but do not turn it into a
width-independent constant at fixed nonzero labels.

The strict Gaussian sensitivity target can be written exactly. In
mobility-Euclidean coordinates
\(\Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\),
let \(P\) embed the initialized random blocks, let
\(J(t,s)=D_{\Theta(s)}\Theta(t)\), and let
\(g_x(t)=\nabla_\Theta[nf_n(t,x)]\). Then
\[
 \nabla_G f_n(t,x)=P^\top J(t,0)^\top g_x(t)/n.
 \tag{18}
\]
A global or correctly localized bound of size \(CnB(x)^2\) for
\(\mathbb E\|P^\top J^\top g_x\|_2^2\), supplemented by a compatible
time-increment estimate, would give the strict target. It is not a
consequence of the currently proved normalized Hilbert--Schmidt
response bound.

For instance, abstractly take unit vectors \(u,v\), let
\(R=a_nuv^\top\), and let \(g=\sqrt n\,u\), where
\(a_n=e^{c\sqrt{\log(e+n)}}\).
Then \(\|R\|_{\rm HS}/\sqrt n\to0\), while
\(\|R^\top g\|_2/\sqrt n=a_n\to\infty\).
Even every fixed normalized Schatten norm of \(R\) tends to zero.
This demonstrates the failed inference, not a counterexample in the
dense neural model. A genuine negative neural result has not been
proved.

The exact adjoint energy and second-variation attempts are recorded
separately in SELF_AVERAGING_SENSITIVITY_ROUTE.md and
SELF_AVERAGING_ENERGY_ATTEMPT.md. Their missing estimate concerns
alignment between a trained backward carrier and the square of a
prediction sensitivity. It is more specific than a marginal carrier
moment and remains open here.

## 6. Consequences and limits

At the previously proved order
\(q_n=\lceil n^{1/4}e^{a\sqrt{\log(e+n)}}\rceil\),
the closure initialized together with the first dense copy has strict
\(C_\mu/\sqrt n\) tracking error. Combining that result with (3)
gives the same near-root bound between this closure and an independently
initialized dense copy. It does not improve (3) to strict root width.

The moving trained state remains \(n^{5/4+o(1)}\) instead of
quadratic, for fixed depth and data. The fixed Gaussian mixers still
have quadratic storage and are applied exactly; this is not a
total-storage or runtime theorem.

Independent-copy concentration cancels any common finite-width bias.
Even a strict improvement of (3) would not prove a quantitative
dense-to-population bias bound. At a fixed time and query, when the
second moment exists, the literal identity is
\(\mathbb E|f_n-f_n'|^2=2\operatorname{Var}(f_n)\).
The requested \(n^{-1/2}\) scale refers to prediction spread or
standard deviation; the corresponding variance scale would be
\(n^{-1}\). The present theorem has the same fixed-confidence
qualification as the preceding compression theorem.
