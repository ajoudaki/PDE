# Prediction self-averaging: exact adjoint energy and the missing alignment bound

2026-10-03. Bounded continuation of the dense independent-copy concentration
question. This is an internal proof attempt, not a concentration theorem.

**Conclusion.** The known finite carrier budget and normalized Schatten
estimates reduce the prediction-sensitivity problem to a directional
entropy estimate. They do not presently prove that estimate. The negative
Gram term is dissipative in the full adjoint energy; restriction to the
randomized initial parameters introduces cross terms and does not give an
additional cancellation. No strict root-width result is claimed.

Complete sources read: DEPTH_EXTENSION_RESULT.md, DEPTH_RESPONSE_MODULUS.md,
DEPTH_CAVITY_ROUTE.md, UNBOUNDED_ACTIVATION_CANDIDATE.md, and current
AGENTS.md. The current manuscript and FINITE_MIXED_MOMENT_ROUTE.md were
read in the preceding scoped attempt. The already-read canonical notation,
neural-response reference, conjecture-investigation and rigorous-proof
skills were reused. No other study, experiment, Git operation, or
manuscript edit was used.

## 1. Model, random roots, and the quantitative requirement

Fix depth, training sample count, and input dimension. Use canonical
Gaussian initialization, zero initial readout, and small-label dense
gradient flow. Activations are \(C^3\) with bounded first three derivatives;
values may grow linearly. Compatible sphere data and the positive initial
feature-Gram condition are as in DEPTH_EXTENSION_RESULT.md. Fixed positive
sample weights \(p_a\) sum to one; \(p_a=1/m\) is the original case.

Use mobility-Euclidean coordinates
\[
 \Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w).
\]
Let \(G\) collect the independent standard Gaussian initialized coordinates.
The isometry \(P\) embeds them in every parameter block except the readout,
so \(\Theta(0)=PG\). For a training or passive query \(x\), define
\[
 \mathcal F_x=nf_x,\qquad g_x=\nabla_\Theta\mathcal F_x,\qquad
 H_x=D_\Theta^2\mathcal F_x.
\]
For training sample \(a\), write \(g_a=g_{x_a}\), \(H_a=H_{x_a}\), and
\(r_a=f_{x_a}-y_a\). The flow and variational equation are exactly
\[
 \dot\Theta=-2\sum_a p_ar_ag_a,\qquad
 \dot J=A J,\quad J(0)=I,
\]
\[
 A=-\mathsf L\mathsf L^\top-2\sum_a p_ar_aH_a,\qquad
 \mathsf L=\sqrt{2/n}\,[\sqrt{p_a}\,g_a]_a.             \tag{1}
\]
The first term includes differentiation of the actual adaptive residual.

The Gaussian-root gradient is
\[
 \nabla_G f_x(t)=n^{-1}P^\top J(t,0)^\top g_x(t).        \tag{2}
\]
The required sufficient fixed-time estimate is therefore
\[
 \mathbb E\|P^\top J(t,0)^\top g_x(t)\|^2\le C_x n,
 \quad\text{uniformly in }n,t.                        \tag{3}
\]
Gaussian Poincaré states
\(\operatorname{Var}F(G)\le\mathbb E\|\nabla_GF(G)\|^2\)
for globally square-integrable weakly differentiable functions with
square-integrable derivative. It would give variance \(C_x/n\) from
(3). A bound only on a high-probability initialization event does not
verify those global hypotheses or justify differentiating the indicator.

The physical tube already gives \(\|g_x(t)\|^2\le C_xn\) on bounded
query sets. Indeed the hidden gradient blocks are
\(\delta_x^{(\ell)}h_x^{(\ell-1)\top}/\sqrt n\), the first block is
\(\delta_x^{(1)}x^\top/\sqrt d\), and the readout block is \(h_x^{(L)}\).
Forward RMS, backward RMS and bounded hidden operators control their
norms. This does not control their alignment with \(J\).

## 2. Exact backward-adjoint energy

Fix \(t<\infty\) and set
\[
 q_x(s;t)=J(t,s)^\top g_x(t),\qquad 0\le s\le t.
\]
Then \(\partial_s q_x=-A(s)q_x\) and \(q_x(t;t)=g_x(t)\).
Suppressing \(x,t\) within this calculation,
\[
 \frac d{ds}\|q(s)\|^2
 =2\|\mathsf L(s)^\top q(s)\|^2
   +4\sum_a p_ar_a(s)q(s)^\top H_a(s)q(s).             \tag{4}
\]
Equivalently,
\[
 \|q(s)\|^2+2\int_s^t\|\mathsf L(u)^\top q(u)\|^2du
 =\|g_x(t)\|^2
  -4\int_s^t\sum_a p_ar_a(u)q(u)^\top H_a(u)q(u)\,du.  \tag{5}
\]
The Gram term has the favorable sign. The residual Hessian need not.

The full-depth Hessian from DEPTH_CAVITY_ROUTE.md has the decomposition
\[
 H_a=H_{0,a}+\sum_{\ell=1}^L
 Z_{a,\ell}^\top
 \operatorname{diag}\bigl(k_a^{(\ell)}
                    \odot\phi_\ell''(z_a^{(\ell)})\bigr)
 Z_{a,\ell},\qquad Z_{a,\ell}=D_\Theta z_a^{(\ell)}.     \tag{6}
\]
The physical tube gives \(\|H_{0,a}\|_{\rm op}\le C\) and
\(\|Z_{a,\ell}\|_{\rm op}\le C\). The bounded term retains every
readout and adjacent-weight mixed block. These bounds use feature RMS,
not bounded activation values.

The remaining unbounded quadratic form is consequently bounded by
\[
 C\sum_{\ell,i}|k_{a,i}^{(\ell)}(s)|
                  |(Z_{a,\ell}(s)q(s))_i|^2.          \tag{7}
\]
A trace bound averaged over an orthonormal basis does not estimate (7)
for the adaptive backward prediction vector \(q_x(s;t)\).

## 3. An exact entropy bound from the carrier budget

On the completed joint-budget event a fixed \(B\), independent of \(n,t\),
satisfies, with \(S\) proportional to label RMS,
\[
 \sup_s\frac1n\sum_{\ell,i}
       e^{\eta|k_{a,i}^{(\ell)}(s)|/S}\le B.            \tag{8}
\]
The stronger running-maximum budget in the completed source implies (8).

For \(u\in\mathbb R^n\), put \(Q=\|u\|^2\). If \(Q>0\), let
\(\pi_i=u_i^2/Q\) and define its relative entropy by
\[
 \mathcal D(\pi)=\sum_i\pi_i\log(n\pi_i).
\]
Zero terms are zero. Set \(Q\mathcal D(\pi)=0\) when \(Q=0\).
The exact finite variational inequality is
\[
 \sum_i|k_i|u_i^2
 \le\frac{SQ}{\eta}\,[\log B+\mathcal D(\pi)].           \tag{9}
\]
For proof, put \(a_i=\eta|k_i|/S\) and
\(\nu_i=e^{a_i}/\sum_j e^{a_j}\). Nonnegativity of
\(\sum_i\pi_i\log(\pi_i/\nu_i)\), obtained from
\(\log z\le z-1\), gives
\[
 \sum_i\pi_i a_i\le
 \mathcal D(\pi)+\log\left(n^{-1}\sum_i e^{a_i}\right).
\]
Equation (8) now proves (9).

Apply (9) to \(u_{a,\ell}=Z_{a,\ell}q_x(s;t)\). Write
\(Q_{a,\ell}=\|u_{a,\ell}\|^2\), and let \(\pi_{a,\ell}\)
be its coordinate-energy distribution. Equations (6)--(9) give
\[
 |q^\top H_aq|
 \le C\|q\|^2+
 \frac{CS}{\eta}\sum_\ell Q_{a,\ell}
             [\log B+\mathcal D(\pi_{a,\ell})].        \tag{10}
\]
Because \(\sum_\ell Q_{a,\ell}\le C\|q\|^2\), the only new quantity is
\[
 \sum_\ell Q_{a,\ell}\mathcal D(\pi_{a,\ell}).           \tag{11}
\]
Its elementary bound is \(C\log n\,\|q\|^2\). The actual carrier maximum
improves the operator argument to the known subpolynomial amplification,
but does not make (11) uniformly bounded.

**Sufficient estimate, still open.** If
\[
 \sum_\ell Q_{a,\ell}(s;t)\mathcal D(\pi_{a,\ell}(s;t))
        \le C\|q_x(s;t)\|^2                            \tag{12}
\]
uniformly, then (5), (10), and \(\int\rho\le CS\) give
\[
 \sup_{s\le t}\|q_x(s;t)\|^2
 \le\|g_x(t)\|^2
       \exp\{CS+CS^2(1+\log B)/\eta\}\le C_xn.          \tag{13}
\]
No event derivative is involved in this deterministic implication.
An expectation version of (12), weighted by a fixed good event, similarly
gives the corresponding good-event expectation bound by integral
Gronwall, using \(|r_a(s)|\le CYe^{-\kappa s}\).
An additional localization or extension argument would still be needed
before global Poincaré.

Equation (12) is a delocalization condition on the backward prediction
adjoint after forward differentiation. It is not asserted by the completed
carrier budget. Exchangeability does not imply it: a uniformly randomly
located single-coordinate vector is exchangeable and has entropy
\(\log n\).

## 4. Restricting to Gaussian roots does not create a cancellation

Let \(\Pi=PP^\top\), and write \(q=q_s+q_w\), where
\(q_s=\Pi q\) and \(q_w=(I-\Pi)q\). Exact differentiation yields
\[
 \begin{aligned}
 \frac d{ds}\|q_s\|^2
 ={}&2\|\mathsf L^\top q_s\|^2
     +2\langle\mathsf L^\top q_s,\mathsf L^\top q_w\rangle\\
 &+4\sum_a p_ar_a
         (q_s^\top H_aq_s+q_s^\top H_aq_w).            \tag{14}
 \end{aligned}
\]
The cross-Gram term has no sign, and the mixed Hessian remains.
Projection destroys the sign of the full Gram form rather than giving an
extra cancellation.

Zero readout gives \(P^\top g_x(0)=0\): the prediction starts
deterministically at zero. At positive terminal time, backward evolution
couples the readout direction into randomized blocks through the mixed
terms in (6). Dropping them would change the sensitivity problem.

## 5. Why Schatten information alone is insufficient

The abstract matrices
\[
 J_n=\operatorname{diag}(e^{c\sqrt{\log n}},1,\ldots,1)
\]
obey \(n^{-1}\|J_n-I\|_{\rm S_p}^p\to0\) for every fixed finite
Schatten exponent \(p\). A generating diagonal can satisfy a bounded
empirical exponential budget and a \(C\sqrt{\log n}\) maximum.
Nevertheless \(v_n=\sqrt n\,e_1\) satisfies
\[
 n^{-1}\|J_n^\top v_n\|^2=e^{2c\sqrt{\log n}}\to\infty.
\]
Randomly permuting the distinguished coordinate also makes this example
exchangeable. It is not a network counterexample. It demonstrates the
missing information in an argument using only carrier budgets, Schatten
norms, and \(\|g_x\|=O(\sqrt n)\): the relative direction of \(g_x\)
and the large singular directions still matters.

## 6. The all-time supremum needs an additional temporal estimate

Even a global proof of (3) would initially give fixed-time concentration.
There is a sufficient route to the time supremum without a time-net
logarithm. Suppose
\[
 \left(\mathbb E\|\nabla_G\partial_tf_x(t)\|^2\right)^{1/2}
 \le C_x n^{-1/2}b(t),\qquad
 \int_0^\infty b(t)\,dt<\infty,                        \tag{15}
\]
and the differentiability and integrability needed for time integration,
expectation, and weak Gaussian differentiation hold. Poincaré and
Minkowski then give, for independent roots \(G,G'\),
\[
 \begin{aligned}
 \left(\mathbb E\sup_{t\ge0}
       |f_x(t;G)-f_x(t;G')|^2\right)^{1/2}
 &\le\int_0^\infty
   \left(2\operatorname{Var}(\partial_tf_x(t;G))\right)^{1/2}dt\\
 &\le C_x/\sqrt n.                                   \tag{16}
 \end{aligned}
\]
The first inequality uses the common deterministic initial value and
the fundamental theorem of calculus. It does not infer a supremum bound
from marginal variances.

For precision, define \(a_x(t)=P^\top J(t,0)^\top g_x(t)\).
Differentiating both \(J\) and the current gradient gives
\[
 \dot a_x
 =-\frac2n\sum_a p_a(g_a^\top g_x)a_a
  -2\sum_a p_ar_aP^\top J^\top(H_ag_x+H_xg_a).          \tag{17}
\]
Both Hessian-gradient terms have the same sign. They do not cancel.
The first term is training-kernel coupling; the second differentiates
that coupling with respect to initialization.

A sufficient additional input is a uniform bound for the mixed vectors
in (17), together with decay of the training vectors \(a_a(t)\).
The latter could then follow from the preserved training Gram gap and
residual-weighted forcing. The established Schatten trace estimate does
not itself bound
\[
 \mathbb E\|P^\top J^\top(H_ag_x+H_xg_a)\|^2.            \tag{18}
\]
For query-integrated concentration, the constants must also be integrable
in the query law; a proof for finitely many query points does not supply
that conclusion.

## 7. Frozen outcome

Identities (4), (5), (14), and (17) retain the adaptive residual and all
mixed terms. The carrier-budget entropy inequality (9) is proved.
Implication (12) to (13), and the all-time implication (15) to (16), are
conditional mathematical results.

The missing finite-network input is a directional adjoint estimate such
as (12), or a mixed-second-variation estimate strong enough to establish
(15), globally or through justified localization. The completed carrier
and Schatten results do not supply this input on their own. Strict
root-width independent-copy all-time prediction concentration remains open
in this attempt.
