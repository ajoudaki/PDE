# Direct finite-width/population comparison at strict root width

2026-10-05. Scoped theoretical route. No experiment, simulation, or shared
book/code edit was performed. This note addresses only the canonical
two-hidden-layer tanh gradient flow with fixed orthogonal data, exactly zero
finite readout, squared mean loss, and mobilities \((n,1,n)\). It does not use
agreement of two independently initialized dense networks as a replacement for
comparison with the deterministic population action flow.

## Conclusion

The requested theorem is **not proved by the permitted inputs, and the present
route does not close it**. It is also not disproved. What can be proved is:

1. the growing fitting horizon and the fitted endpoint are not the decisive
   obstruction: an exact residual-damped reduction turns one direct
   finite-to-population tangent-kernel source estimate on
   \(T_n\asymp\log n\) into the requested all-time whole-sphere estimate;
2. stochastic fluctuation and deterministic finite-width bias must be bounded
   separately; even a hypothetical strict dense-versus-dense theorem would not
   control the bias;
3. at initialization, the direct comparison does have the sharp structure:
   the centered whole-sphere onset fluctuation is
   \(O_{\mathbb P}(n^{-1/2})\), while its bias relative to the canonical
   population action is \(O(n^{-1})\);
4. the first unresolved dynamic estimate in the available response route is a
   uniform transported-response moment bound. At the prediction level, a
   sufficient unresolved obligation is the residual-weighted tangent-kernel
   source estimate in (12) below, separately for fluctuation and bias.

Thus the current status is a sharp conditional reduction plus an onset theorem,
not a strict all-time rate theorem.

## 1. Exact target and normalization

Write \(v=x/\sqrt d\in S^{d-1}\). The training inputs
\(v_1,\ldots,v_m\) are orthonormal. With \(\phi=\tanh\), the finite network is

\[
 h_n^{(1)}(t,v)=\phi(W_n^{(1)}(t)v),\qquad
 h_n^{(2)}(t,v)=\phi(W_n^{(2)}(t)h_n^{(1)}(t,v)),
\]
\[
 f_n(t,v)=\frac{(W_n^{(3)}(t))^T h_n^{(2)}(t,v)}{n}.
\tag{1}
\]

Initially, the entries of \(W_n^{(1)}\) are independent \(N(0,1)\), the
entries of \(W_n^{(2)}\) are independent \(N(0,1/n)\), the two blocks are
independent, and

\[
                         W_n^{(3)}(0)=0
\tag{2}
\]

exactly. Put \(r_{n,a}=f_n(t,v_a)-y_a\) and
\(Y=\lVert y\rVert_2/\sqrt m\). The loss is
\(m^{-1}\sum_a r_{n,a}^2\), and all three blocks train in physical time with
mobilities \((n,1,n)\).

Let \(f(t,v)\) be the prediction of the maintained canonical population
action flow from the same Gaussian first-row law, the joint initialized
middle action and its Hilbert adjoint, and zero population readout. The global
orthogonal-data theorem in
`docs/04-continuing-flows.qmd`, Section B.1, uses sum loss with multipliers
\(\kappa_1,\kappa_2,\kappa_3\); the present mean-loss flow is exactly its
specialization \(\kappa_1=\kappa_2=\kappa_3=1/m\). An exactly zero readout is
allowed by its vanishing-readout hypothesis.

Let

\[
 q=\mathbb E\tanh^2(G),\qquad
 \gamma=\mathbb E\tanh^2(\sqrt q\,G)>0,qquad G\sim N(0,1),
\tag{3}
\]

and \(\lambda=\gamma/m\). Oddness and orthogonality make the initialized
population top-feature Gram equal to \(\gamma I_m\). Take the labels in the
supplied small-label regime, in particular small enough for the explicit
dense fitting theorem in
`../integrated_general_compression_20261004/GENERAL_EXPLICIT_FITTING.md`.

The desired statement is: for each fixed \(0<\delta<1\), there should be
constants \(C_\delta,N_\delta<\infty\), depending on the fixed task but not on
\(n\), such that

\[
 \mathbb P\left\{
 \sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
       |f_n(t,v)-f(t,v)|\le \frac{C_\delta}{\sqrt n}
 \right\}\ge 1-\delta,
 \qquad n\ge N_\delta .
\tag{4}
\]

The value at \(t=\infty\) means the actual fitted endpoint of each flow.
The probability is for one fresh initialization at each width, not one event
for infinitely many independently initialized widths.

## 2. The growing horizon and endpoint reduce exactly to one source term

For normalized parameter coordinates, let \(K_n(t;v,u)\) be the finite
tangent kernel, so that

\[
 \partial_t f_n(t,v)=-\frac2m\sum_{a=1}^m
                K_n(t;v,v_a)r_{n,a}(t).
\tag{5}
\]

Let \(K(t;v,u)\) be its population-action counterpart. Define the training
matrices and passive rows

\[
 A_n(t)=\frac1m(K_n(t;v_a,v_b))_{a,b=1}^m,
 \quad A(t)=\frac1m(K(t;v_a,v_b))_{a,b=1}^m,
\]
\[
 a_n(t,v)=\frac1m(K_n(t;v,v_a))_{a=1}^m,
 \quad a(t,v)=\frac1m(K(t;v,v_a))_{a=1}^m.
\tag{6}
\]

The finite fitting proof gives, on its high-probability event, constants
\(g,B,C_{\rm tail}>0\), independent of time and width, such that

\[
 A_n(t)\succeq gI_m,qquad
 \sup_{t,v}\lVert a_n(t,v)\rVert_2\le B,
\tag{7}
\]

and

\[
 \sup_v|f_n(\infty,v)-f_n(t,v)|
 \le C_{\rm tail}e^{-\lambda t/2}.
\tag{8}
\]

For example one may take \(g=\lambda/4\) on the event in that proof.
The same Hilbert-space energy and first-exit argument gives (7)--(8) for
the population flow, deterministically, with enlarged fixed constants. It
uses the same initialized top Gram, bounded tanh gates, small-label hidden
displacements, and the population rank-one/adjoint identities. Alternatively,
pass the gap, residual, and state bounds at each fixed time through the
maintained compact-time population limit, extend them over time by continuity,
and integrate the resulting population velocity bound against the
exponentially decaying residual. This constructs the population endpoint
directly; it does not interchange the limits in width and time.

In particular, enlarge \(C_{\rm tail}\) once so that the deterministic
population tail also satisfies

\[
 \sup_v|f(\infty,v)-f(t,v)|
 \le C_{\rm tail}e^{-\lambda t/2}.
\tag{8a}
\]

Let \(r(t)=(f(t,v_a)-y_a)_{a=1}^m\) be the deterministic population
residual. For \(T<\infty\), define the direct kernel-source error

\[
 \begin{aligned}
 \mathfrak S_n(T)={}&
 \int_0^T\lVert(A_n(t)-A(t))r(t)\rVert_2\,dt\\
 &+\int_0^T\sup_{v\in S^{d-1}}
       |(a_n(t,v)-a(t,v))^T r(t)|\,dt.
 \end{aligned}
\tag{9}
\]

This is a source-production term, not a stability constant.

**Proposition 1 (exact all-time reduction).** On the event (7)--(8),

\[
 \sup_{0\le t\le T}\sup_v|f_n(t,v)-f(t,v)|
 \le 2\left(1+\frac Bg\right)\mathfrak S_n(T).
\tag{10}
\]

Consequently, with

\[
                         T_n=\lambda^{-1}\log n,
\tag{11}
\]

an estimate

\[
 \mathbb P\left\{\mathfrak S_n(T_n)>C_\delta n^{-1/2}\right\}
 \le\delta
\tag{12}
\]

implies (4), after changing \(C_\delta\) and allocating failure probability
to the physical event.

**Proof.** Put \(e(t)=(f_n(t,v_a)-f(t,v_a))_{a=1}^m\). Subtracting the
two exact training residual equations gives

\[
 \dot e=-2A_ne-2(A_n-A)r,qquad e(0)=0.
\tag{13}
\]

The spectral lower bound in (7) gives

\[
 D^+\lVert e\rVert_2
 \le-2g\lVert e\rVert_2+2\lVert(A_n-A)r\rVert_2.
\]

Variation of constants and Tonelli therefore give

\[
 \int_0^T\lVert e(t)\rVert_2\,dt
 \le \frac1g\int_0^T\lVert(A_n-A)r\rVert_2\,dt.
\tag{14}
\]

For a passive query, \(d_v(t)=f_n(t,v)-f(t,v)\) obeys

\[
 \dot d_v=-2a_n(t,v)^Te
           -2(a_n(t,v)-a(t,v))^Tr,qquad d_v(0)=0.
\tag{15}
\]

Integrating (15), using (7) and (14), proves (10). For \(t\ge T_n\),
compare both flows with their values at \(T_n\). Equations (8), (8a), and
(11) make this continuation cost at most \(4C_{\rm tail}n^{-1/2}\) when
each value is compared through its own endpoint. A stronger
integrated-velocity estimate improves this harmless constant but is not
needed. The same comparison includes \(t=\infty\), because the two tail
bounds prove existence and uniform convergence of both endpoints. This
proves the implication from (12) to (4). \(\square\)

The logarithmically growing horizon causes no loss in this reduction. The
reason is the residual damping in (13) and the integrability of the physical
tail; no factor \(T_n\) is introduced.

## 3. Fluctuation and bias are different obligations

Whenever the finite kernels are integrable, decompose

\[
 A_n-A=(A_n-\mathbb EA_n)+(\mathbb EA_n-A),
 \qquad
 a_n-a=(a_n-\mathbb Ea_n)+(\mathbb Ea_n-a).
\tag{16}
\]

Substitution in (9) defines
\(\mathfrak S_n^{\rm fluc}(T)\) and
\(\mathfrak S_n^{\rm bias}(T)\), and gives

\[
 \mathfrak S_n(T)
 \le \mathfrak S_n^{\rm fluc}(T)
      +\mathfrak S_n^{\rm bias}(T).
\tag{17}
\]

A direct proof of (12) therefore needs both

\[
 \mathfrak S_n^{\rm fluc}(T_n)=O_{\mathbb P}(n^{-1/2}),
 \qquad
 \mathfrak S_n^{\rm bias}(T_n)=O(n^{-1/2}).
\tag{18}
\]

The natural expected bias is \(O(n^{-1})\), but no such dynamic estimate is
present in the supplied sources.

Dense-versus-dense agreement cannot replace the second estimate. The logical
failure is already visible for scalar random variables. Let

\[
 X_n=n^{-1/4}+n^{-1/2}Z,qquad
 X_n'=n^{-1/4}+n^{-1/2}Z',
\]

where \(Z,Z'\) are independent standard Gaussians. Then
\(X_n-X_n'=O_{\mathbb P}(n^{-1/2})\) and \(X_n\to0\) in probability, but
\(X_n\) is not \(O_{\mathbb P}(n^{-1/2})\) away from the deterministic limit
zero. This remains an example in the all-time whole-sphere topology by taking
constant functions. It is a no-go for the inference, not a counterexample to
the neural theorem.

The independent-dense certificates in
`../integrated_general_compression_20261004/RESULT.md` in fact remain
\(n^{-1/2+o(1)}\), but even a strict improvement would cancel a common
finite-width bias. Likewise, the compact theorem compares an autonomous
compressed optimizer with the same realized dense trajectory; it does not
identify either one with the deterministic population action flow.

## 4. A direct strict-root theorem at onset, including bias

The initialization itself has no strict-root obstruction. The following
result is for the actual two-layer Gaussian array and the deterministic
population kernel.

For \(u,v\in S^{d-1}\), let

\[
 K_n^0(u,v)=\frac1n h_n^{(2)}(0,u)^T h_n^{(2)}(0,v),
 \qquad K^0(u,v)=K(0;u,v).
\tag{19}
\]

At zero readout this is the entire tangent kernel: all hidden-gradient
blocks vanish.

**Theorem 2 (whole-sphere onset fluctuation and bias).** There is a constant
\(C_d<\infty\) such that, for every fixed training input \(u\),

\[
 \sup_{v\in S^{d-1}}
       |\mathbb E K_n^0(u,v)-K^0(u,v)|\le \frac{C_d}{n},
\tag{20}
\]

and, for every \(0<\delta<1\), there is \(N_{d,\delta}<\infty\) such that,
for \(n\ge N_{d,\delta}\),

\[
 \mathbb P\left\{
 \sup_{v\in S^{d-1}}
 |K_n^0(u,v)-\mathbb E K_n^0(u,v)|
 >\frac{C_d(1+\sqrt{\log(1/\delta)})}{\sqrt n}
 \right\}\le\delta.
\tag{21}
\]

After a union bound over the \(m\) fixed training inputs,

\[
 \sup_v|\mathbb E\partial_t f_n(0,v)-\partial_t f(0,v)|
 \le \frac{C_dY}{n},
\tag{22}
\]

and, with probability at least \(1-\delta\),

\[
 \sup_v|\partial_t f_n(0,v)-\mathbb E\partial_t f_n(0,v)|
 \le \frac{C_dY(1+\sqrt{\log(m/\delta)})}{\sqrt n}.
\tag{23}
\]

**Proof.** Let the rows \(A_i\) of \(W_n^{(1)}(0)\) be independent
\(N(0,I_d)\). Recall that \(v=x/\sqrt d\), so \(A_i\cdot v\) is exactly
the first-layer preactivation in (1). Define

\[
 H_n(v)=\frac1{\sqrt n}
    (\tanh(A_i\cdot v))_{i=1}^n.
\]

Write the rows of \(\sqrt nW_n^{(2)}(0)\) as independent
\(\Xi_j\sim N(0,I_n)\). Then

\[
 K_n^0(u,v)=\frac1n\sum_{j=1}^n
 \tanh(\Xi_j\cdot H_n(u))\tanh(\Xi_j\cdot H_n(v)).
\tag{24}
\]

Conditional on the first layer, each summand has expectation
\(\Psi(\Sigma_n(u,v))\), where

\[
 \Sigma_n(u,v)=
 \begin{pmatrix}
 \lVert H_n(u)\rVert_2^2&H_n(u)^TH_n(v)\\
 H_n(u)^TH_n(v)&\lVert H_n(v)\rVert_2^2
 \end{pmatrix},
\]

and \(\Psi(\Sigma)=\mathbb E[\tanh(Z_1)\tanh(Z_2)]\) for
\((Z_1,Z_2)\sim N(0,\Sigma)\). Its deterministic population counterpart
is \(\Psi(\Sigma(u,v))=K^0(u,v)\), where
\(\Sigma=\mathbb E\Sigma_n\).

First consider \(\Sigma_n-\Sigma\). Symmetrization followed by the scalar
contraction inequality gives

\[
 \mathbb E\sup_v
 \left|\frac1n\sum_i
 \{\tanh(A_i\cdot u)\tanh(A_i\cdot v)
 -\mathbb E[\tanh(A_i\cdot u)\tanh(A_i\cdot v)]\}\right|
 \le C\sqrt{\frac dn}.
\tag{25}
\]

Indeed, after conditioning on the \(A_i\), the multipliers
\(\tanh(A_i\cdot u)\) have magnitude at most one, and contraction reduces
the Rademacher supremum to
\(n^{-1}\lVert\sum_i\varepsilon_iA_i\rVert_2\), whose expectation is at
most \(\sqrt{d/n}\). The diagonal class uses that \(z\mapsto\tanh^2z\)
is two-Lipschitz and the same argument. Changing one row changes either
supremum by at most \(2/n\), so bounded differences upgrades (25) to

\[
 \sup_v\lVert\Sigma_n(u,v)-\Sigma(u,v)\rVert_{\max}
 \le \frac{C(\sqrt d+\sqrt{\log(1/\delta)})}{\sqrt n}
\tag{26}
\]

outside an event of probability \(\delta\).

Next condition on the first layer. On
\(\lVert W_n^{(1)}(0)\rVert_{\rm op}/\sqrt n\le2\), whose failure is
exponentially small for fixed \(d\), the map \(v\mapsto H_n(v)\) is
two-Lipschitz and takes values in the unit ball. To make the product-class
step explicit, put
\(F_v(\xi)=\tanh(\xi\mathbin\cdot H_n(u))
\tanh(\xi\mathbin\cdot H_n(v))\). Conditional symmetrization gives

\[
 \mathbb E_{\Xi}\sup_v\left|\frac1n\sum_j
 \left\{F_v(\Xi_j)-\mathbb E_{\xi}F_v(\xi)\right\}\right|
 \le 2\mathbb E_{\Xi,\varepsilon}\sup_v\left|\frac1n\sum_j
 \varepsilon_jc_j\tanh(\Xi_j\mathbin\cdot H_n(v))\right|.
\]

Here \(c_j=\tanh(\Xi_j\mathbin\cdot H_n(u))\). After the \(\Xi_j\)'s are
fixed, the coordinate maps
\(s\mapsto c_j\tanh s\) vanish at zero and are one-Lipschitz because
\(|c_j|\le1\). The coordinatewise contraction inequality therefore bounds
the last display by

\[
 C\,\mathbb E_Z\sup_v|Z^TH_n(v)|,qquad
 Z\sim N(0,I_n/n).
\tag{27}
\]

Indeed, after contraction
\(Z=n^{-1}\sum_j\varepsilon_j\Xi_j\), which has exactly that Gaussian law.
Thus the fact that the first factor and the score use the same \(\Xi_j\)
causes no independence assumption: it is frozen as a bounded multiplier
before contraction.

Anchor at one \(v_0\). The increment metric of the centered Gaussian
process in (27) is at most
\(2\lVert v-v'\rVert_2/\sqrt n\). The elementary Gaussian comparison
with \(2g\cdot v/\sqrt n\), \(g\sim N(0,I_d)\), bounds (27) by
\(C(1+\sqrt d)/\sqrt n\). Changing one \(\Xi_j\) changes the conditional
empirical supremum by at most \(2/n\); bounded differences gives the
additional \(C\sqrt{\log(1/\delta)/n}\). Together with (26), and the
Gaussian interpolation bound

\[
 |\Psi(\Sigma_1)-\Psi(\Sigma_2)|
 \le C\lVert\Sigma_1-\Sigma_2\rVert_{\max},
\tag{28}
\]

this proves a strict-root high-probability bound for
\(K_n^0-K^0\), uniformly in \(v\).

It remains to separate its bias. All derivatives of tanh are bounded.
Differentiating a Gaussian expectation with respect to covariance once
uses second derivatives of
\((z_1,z_2)\mapsto\tanh z_1\tanh z_2\); differentiating twice uses its
fourth derivatives. Hence \(\Psi\) has a uniformly bounded second
covariance derivative on the positive-semidefinite covariance set reached
here. At singular endpoints, add \(\varepsilon I\), apply the formula on
the positive-definite segment, and let \(\varepsilon\downarrow0\) by
dominated convergence. Taylor's formula gives

\[
 \left|\Psi(\Sigma_n)-\Psi(\Sigma)
       -D\Psi(\Sigma)[\Sigma_n-\Sigma]\right|
 \le C\lVert\Sigma_n-\Sigma\rVert_F^2.
\tag{29}
\]

Now \(\mathbb E\Sigma_n=\Sigma\), and every covariance entry is an
average of bounded independent variables, so
\(\mathbb E\lVert\Sigma_n-\Sigma\rVert_F^2\le C/n\). Taking expectations
in (29) proves (20). The upper-layer empirical average has no conditional
bias. Subtracting (20) from the already obtained high-probability bound
proves (21).

Finally, zero readout gives the exact identities

\[
 \partial_t f_n(0,v)=\frac2m\sum_{a=1}^m y_aK_n^0(v_a,v),
 \qquad
 \partial_t f(0,v)=\frac2m\sum_{a=1}^m y_aK^0(v_a,v).
\tag{30}
\]

Use \(m^{-1}\sum_a|y_a|\le Y\) and a union bound in (20)--(21) to
obtain (22)--(23). \(\square\)

For one nonzero label, the root-width fluctuation scale cannot generally
be improved: conditional on the first layer, the diagonal terms in (24)
are iid, and their variance tends to
\(\operatorname{Var}[\tanh^2(\sqrt q\,G)]>0\). Thus
\(\operatorname{Var}K_n^0(u,u)\ge c/n\) for all sufficiently large \(n\).

## 5. The first unresolved dynamic estimate

The maintained B.1 width proof identifies every fixed proof mesh and then
takes

\[
 n\to\infty\quad\hbox{at fixed mesh},qquad
 \Delta\downarrow0\quad\hbox{afterwards}.
\]

Its fixed Gaussian-program convergence is qualitative. It supplies neither
a rate uniform in a refining mesh nor a rate on the growing horizon (11).
The theorem provides no quantitative finite-width rate.
Therefore it does not imply (12).

The most developed strict-fluctuation route in the permitted material is
`../integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`.
Use the mobility-normalized parameters

\[
 \Theta=(W_n^{(1)},\sqrt n\,W_n^{(2)},W_n^{(3)}),
 \qquad \mathcal F_{n,v}(\Theta)=n f_n(v).
\]

Let \(g_{n,v}(t)=\nabla_\Theta\mathcal F_{n,v}(\Theta(t))\), and let
\(J_n(t,s)=D_{\Theta(s)}\Theta(t)\) be the derivative of the normalized
gradient-flow map. Gaussian sensitivity transports the terminal gradient as

\[
 q_n(s;T,v)=J_n(T,s)^Tg_{n,v}(T).
\tag{31}
\]

Instantaneous response moments are available, but they do not control
(31). For a training input and layer \(\ell\), define the transported
preactivation response

\[
 R_{n,a}^{(\ell)}(s;T,v)
 =D_\Theta z_{n,a}^{(\ell)}(s)[q_n(s;T,v)],
 \qquad
 \lVert U\rVert_{4,n}^4=\frac1n\sum_{i=1}^n|U_i|^4.
\tag{32}
\]

The first missing estimate in that route is a bound of the form

\[
 \sup_{n}\sup_{T\le T_n}\sup_{v}\sup_{s\le T}
 \max_{a,\ell}
 \mathbb E\!\left[
   \mathbf1_{\Omega_n}
   \lVert R_{n,a}^{(\ell)}(s;T,v)\rVert_{4,n}^4
 \right]<\infty,
\tag{33}
\]

with the corresponding same-root trace bounds and query increments.
Here \(\Omega_n\) is a legitimate physical/source localization event.
The reverse observable contains
\(k_{n,a}^{(\ell)}\odot R_{n,a}^{(\ell)}\). Available training-carrier
moments control the first factor, but the original asymmetric insertion
theorem does not control the transported second factor or the terminal
Hessian/third-derivative endpoints generated by (31). A physical RMS stop
or an instantaneous response estimate does not imply (33).

Nor is (33) sufficient by itself: the sensitivity proof also needs the
corresponding same-root trace estimates, passive-query increments, and a
smooth globally valid localization of the stopped Gaussian family. Simply
inserting the indicator of a good event is invalid when differentiating
across its boundary. One must first differentiate a smooth stopped or
extended flow and then remove the localization on the physical event.

Even if (33) closed the centered Gaussian-sensitivity argument, the bias
half of (18) would remain. It requires a quantitative finite-size expansion
of the reused Gaussian actions—equivalently, control of the loop/diagonal
terms left after the population response is subtracted—uniformly in
residual-weighted time up to \(T_n\). The fixed-program theorem proves only
that this bias vanishes at every fixed program length. No \(O(n^{-1})\), or
even \(O(n^{-1/2})\), growing-program bias bound is supplied.

The whole-query source theorem in
`../closure_sampling_20261003/WHOLE_QUERY_RESPONSE_SOURCE.md` does not fill
this gap. It builds initialization-only polynomial source spaces tailored to
one realized dense trajectory and compares a compact optimizer to that same
trajectory. Its \(C\sqrt n\) passive-query magnitude is used only inside an
analytic approximation degree. It is neither a centered concentration
estimate nor a finite-width bias estimate relative to the deterministic
population action.

Orthogonality also does not remove (33) after positive time. It diagonalizes
the initialized population training Gram, but the exact hidden second
derivatives in
`../orthogonal_tanh_time_legendre_20261005/TIME_AND_PREDICTION_ROUTES.md`
already contain cross-label products through the shared nonlinear gates and
middle action.

## 6. Claim ledger

| Claim | Status |
|---|---|
| Global finite GF, exponential fitting, finite endpoint, whole-sphere tail | Supplied for small labels |
| Canonical population action flow on every finite horizon | Maintained theorem |
| Qualitative finite-to-population convergence on each fixed horizon | Maintained theorem |
| Exact reduction from (12) to all-time, whole-sphere, endpoint error | Proved in Proposition 1 |
| Strict onset fluctuation \(O_{\mathbb P}(n^{-1/2})\) | Proved in Theorem 2 |
| Onset finite-width bias \(O(n^{-1})\) | Proved in Theorem 2 |
| Dynamic centered source estimate in (18), through \(T_n\) | Open; (33) is the first missing response estimate in the current route |
| Dynamic finite-width bias estimate in (18), through \(T_n\) | Open |
| Requested theorem (4) | Open, not falsified |

The highest-leverage next proof is therefore not another endpoint argument.
It is a direct bidirectional cavity/insertion estimate for (33), with constants
uniform in accumulated residual activity, followed by a separate finite-size
bias expansion for the same residual-contracted kernel source. Proposition 1
would then supply the growing horizon and endpoint automatically.

## 7. Input and process note

Scientific inputs were the maintained `docs/` edition and the supervisor's
explicitly authorized files and their directly linked relevant
proof/correction artifacts. No other study was searched or read. Repository
HEAD at startup was `3834145d910202a84824d943fe7d7f65714d96f2`; unrelated
working-tree changes were left untouched.

The repository-mandated skill
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` could not
be read: both the ordinary and sandbox-escalated reads returned operating-system
`Permission denied`. Its linked neural-network reference therefore could not
be discovered or read. This note instead follows `AGENTS.md` and
`docs/notation.qmd` directly. The rigorous-math and conjecture-investigation
skills, including their research-contract, adversarial-audit, and proof-search
instructions, were read and applied.
