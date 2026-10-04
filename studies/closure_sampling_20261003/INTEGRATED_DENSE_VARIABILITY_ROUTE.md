# Whole-sphere dense variability: a topology improvement and the remaining mixed response

2026-10-04. Scoped integrated continuation explicitly authorized to use
`dense_cutoff_population_rate_20261001` and the current study. This is a
bounded source audit and proof attempt, not a promotion review. Only this
report is written. No experiment, Git mutation, maintained-book edit, or
population-bias assertion is made.

**Outcome.** The near-root independent-copy theorem in
`GENERAL_SELF_AVERAGING.md` extends to the whole-sphere supremum without
changing its activation, data, or label hypotheses. Its rate remains
\(n^{-1/2}\exp(C\sqrt{\log(e+n)})\). The present study's strict-root
passive-query moments and weighted runtime estimates do not remove that
factor. They control different random directions or start from a smaller
source error. The exact missing global sensitivity is identified below;
it is not imposed as an additional hypothesis of a claimed strict theorem.

## 1. Contract and source scope

Fix hidden depth \(L\ge2\), input dimension \(d\), and a finite dataset,
all independently of width \(n\). Write \(v=x/\sqrt d\). The network is
\[
 z^{(1)}(t,v)=W^{(1)}(t)v,\qquad
 z^{(\ell)}(t,v)=W^{(\ell)}(t)h^{(\ell-1)}(t,v),\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f_n(t,v)=\frac1n w(t)^\top h^{(L)}(t,v).
 \tag{1}
\]
First weights have independent \(N(0,1)\) entries, hidden weights have
independent \(N(0,1/n)\) entries, blocks are independent, and \(w(0)=0\).
Let fixed sample weights \(p_a>0\) sum to one; the original problem has
\(p_a=1/m\). Define \(r_a=f_n(t,v_a)-y_a\),
\(\rho^2=\sum_a p_ar_a^2\), and \(Y^2=\sum_a p_ay_a^2\).
The loss is \(\rho^2\), with mobilities \((n,1,\ldots,1,n)\).

The assumptions are exactly the broad dense theorem's: every activation
is \(C^3\) with bounded first three derivatives, activation values may
grow linearly, the limiting initialized top-feature Gram has a positive
gap on the compatible weighted data quotient, and \(Y\) is below its
fixed positive small-label threshold. Compatible duplication/parity
quotients retain their original weights and physical time. No
orthogonality or forward normalization is added. Zero labels give the
identically zero output and require no probabilistic argument.

The strict target is, for two independently initialized trained copies,
\[
 \Pr\left\{\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}
 |f_n(t,v)-f_n'(t,v)|\le C_\delta n^{-1/2}\right\}\ge1-\delta
 \tag{2}
\]
for every fixed \(\delta>0\) and every sufficiently large \(n\).
The endpoint is the fitted limit, and both models are evaluated at the
same physical time. All constants can depend on the fixed problem and
confidence, but not on width or time.

Complete primary reads for this audit were the prior study's
`GENERAL_SELF_AVERAGING.md`, `SELF_AVERAGING_FEEDBACK_ROUTE.md`,
`SELF_AVERAGING_SENSITIVITY_ROUTE.md`,
`SELF_AVERAGING_ENERGY_ATTEMPT.md`, `DEPTH_EXTENSION_RESULT.md`,
`DEPTH_RESPONSE_MODULUS.md`, and `FINITE_MIXED_MOMENT_ROUTE.md`, and this
study's `INPUT_DIMENSION_REFINEMENT.md`,
`INTRINSIC_STRICT_ROOT_ROUTE.md`, and
`RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md`. The named physical tube and
carrier theorem are inherited internally checked inputs, not re-proved
here from their full deletion proof. Selected source/check passages were
also inspected as locators; their verdicts are not substitutes for the
calculations below. Canonical notation, neural conventions, rigorous
proof, and research evidence/adversarial instructions were applied.

## 2. Proved improvement: the existing rate controls the whole sphere

Let the standard Gaussian root vector be
\[
 G=(W_0^{(1)},\sqrt nW_0^{(2)},\ldots,\sqrt nW_0^{(L)}).
\]
The inherited good set \(\Omega_n\) has probability tending to one and
supplies, uniformly in physical time, bounded hidden operator norms,
\(\|W^{(1)}\|_F/\sqrt n\le C\),
\(\|w\|_2/\sqrt n\le CS\), and
\(\rho(t)\le Ye^{-\kappa t}\), where \(S\) is a fixed multiple of
\(Y\). Its training-carrier maximum is at most
\(CS\sqrt{\log(e+n)}\).

The already proved good-pair comparison gives, for every
\(G,\widetilde G\in\Omega_n\),
\[
 \sup_{t\in[0,\infty],\ v\in S^{d-1}}
 |f_n(G;t,v)-f_n(\widetilde G;t,v)|
 \le \ell_n\|G-\widetilde G\|_2,
 \qquad
 \ell_n=\frac{C}{\sqrt n}e^{K_0\sqrt{\log(e+n)}}.
 \tag{3}
\]
This is the prior feedback proof's equation (15) restricted to unit
inputs. It compares the two actual paths, without interpolating their
initializations through a presumed fitting region.

There is also a deterministic joint modulus in query and time on this
same good set. Define the passive carriers by
\[
 k^{(L)}(t,v)=w(t),\quad
 \delta^{(\ell)}(t,v)=\phi_\ell'(z^{(\ell)}(t,v))\odot k^{(\ell)}(t,v),
 \quad k^{(\ell)}=W^{(\ell+1)\top}\delta^{(\ell+1)}.
\]
Bounded slopes and hidden operator norms imply
\(\|\delta^{(1)}(t,v)\|_2\le CS\sqrt n\) for every real query.
The exact input derivative is
\[
 \nabla_v f_n(t,v)=\frac1nW^{(1)}(t)^\top\delta^{(1)}(t,v).
\]
Consequently \(\|\nabla_v f_n\|_2\le CS\), because
\(\|W^{(1)}\|_{\mathrm{op}}\le\|W^{(1)}\|_F\le C\sqrt n\).
The bound holds on line segments between unit inputs as well. The prior
physical-speed calculation gives \(|\partial_t f_n(t,v)|\le CYe^{-\kappa t}\)
on the unit sphere. Thus, with the deterministic proof coordinate
\(u(t)=1-e^{-\kappa t}\), including \(u(\infty)=1\),
\[
 |f_n(t,v)-f_n(s,v')|
 \le C\bigl(|u(t)-u(s)|+\|v-v'\|_2\bigr).
 \tag{4}
\]
No bounded activation values or query carrier maximum were used here.
Parameter convergence extends (3)--(4) to the fitted endpoint.

Choose a \(1/n\)-net \(V_n\) of the unit sphere with at most
\((1+2n)^d\) points, and take \(u_j=j/n\), \(0\le j\le n\).
The joint grid has
\(N_n\le(n+1)(1+2n)^d\) points. At each grid point, extend the scalar
map from \(\Omega_n\) by the McShane formula
\[
 F_{j,v}(G)=\inf_{H\in\Omega_n}
 \{f_n(H;t(u_j),v)+\ell_n\|G-H\|_2\},
 \tag{5}
\]
then truncate its values to the inherited fixed amplitude interval.
Equation (3) makes this a globally \(\ell_n\)-Lipschitz function agreeing
with the original prediction on \(\Omega_n\). The prior scalar-extension
measurability argument applies unchanged; only finitely many maps occur.

For a standard Gaussian root, the Gaussian concentration inequality in
the prior proof gives
\(\Pr(|F-\mathbb EF|>z)\le2e^{-z^2/(2\ell_n^2)}\).
Hence for two copies and every \(z>0\),
\[
 \Pr\left\{\max_{j,v\in V_n}|F_{j,v}(G)-F_{j,v}(G')|>z\right\}
 \le4N_n e^{-z^2/(8\ell_n^2)}.
 \tag{6}
\]
This deduction uses the triangle inequality around each scalar mean;
it needs only the correct marginal Gaussian laws.

Given \(0<\delta<1\), take
\(z=\ell_n\sqrt{8\log(8N_n/\delta)}\), making (6) at most
\(\delta/2\). For sufficiently large \(n\), the probability that either
root misses \(\Omega_n\) is at most \(\delta/2\). On the remaining
event, approximating both time and query by the grid and using (4) gives
\[
 \sup_{t\in[0,\infty],\ v\in S^{d-1}}
 |f_n(t,v)-f_n'(t,v)|
 \le\ell_n\sqrt{8\log(8N_n/\delta)}+C/n.
 \tag{7}
\]
Since \(d\) is fixed and
\(\log N_n\le C_d\log(e+n)\), the square-root logarithm can be
absorbed into a larger fixed exponential coefficient. Therefore
\[
 \Pr\left\{\sup_{t\in[0,\infty],\ v\in S^{d-1}}
 |f_n(t,v)-f_n'(t,v)|
 \le\frac{C_\delta}{\sqrt n}e^{K\sqrt{\log(e+n)}}\right\}
 \ge1-\delta.
 \tag{8}
\]
This proves a stronger query topology than the displayed integrated-query
theorem. It does not prove (2). Constants are still independent of width
and physical time, with the same broad activation scope.

## 3. Why the passive-query strict-root theorem does not control (2)

In `INPUT_DIMENSION_REFINEMENT.md`, let \(U,E\) be orthonormal bases for
the training-input span and its orthogonal complement. The exact first
weight update gives
\(W^{(1)}(t)E=W_0^{(1)}E=:G_\perp\).
The sigma-field \(\mathcal F\) generated by \(W_0^{(1)}U\), all hidden
initialization, and the data determines the entire training path and is
independent of \(G_\perp\). For fixed training information,
\[
 \nabla_{G_\perp}f_n(t,v)
 =\frac1n\delta^{(1)}(t,v)(E^\top v)^\top.
 \tag{9}
\]
The proved fixed-query carrier moments and half-Hölder increments control
this derivative. The event used in that Gaussian argument belongs to
\(\mathcal F\), so conditioning does not restrict \(G_\perp\).

The result controls
\(f_n(t,v)-\mathbb E[f_n(t,v)\mid\mathcal F]\), uniformly in time and
query at strict root width. It leaves the random conditional mean. For
independent copies, the exact decomposition is
\[
 f_n-f_n'=
 \bigl(f_n-\mathbb E[f_n\mid\mathcal F]\bigr)
 -\bigl(f_n'-\mathbb E[f_n'\mid\mathcal F']\bigr)
 +\mathbb E[f_n\mid\mathcal F]-\mathbb E[f_n'\mid\mathcal F'].
 \tag{10}
\]
The first two terms are controlled by that theorem in its bounded
strip-analytic activation scope. The last is the remaining variation
of trained active first weights and hidden mixers. When the training
span is full dimensional, there is no passive Gaussian matrix at all;
the same theorem then supplies no independent-copy concentration.

The asymmetric endpoint trace in its insertion proof has the form
\(n^{-1}\operatorname{tr}(B_vJB_a^\top)\), where
\(B_v=D_\Theta\delta_v^{(j+1)}\) has a normalized Hilbert--Schmidt
bound. Its Gaussian contraction averages a rank-\(O(n)\) response map.
That is not the prediction gradient transported through training.
Also, the published passive-query moment proof explicitly uses bounded
strip-analytic activations. The broad unbounded dense carrier theorem
does not by itself extend every passive-query assertion to that class.
Neither discrepancy can be silently removed by citing the dimension
refinement.

## 4. Why the weighted runtime improvement does not remove this loss

`RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md` retains the small activity
factor in the comparison exponential. Its actual state estimate is
\[
 E(t)\le u\frac{\epsilon}{\sqrt\lambda}
 (F_{\rm src}+B_{\exp}u\sqrt{\log(en)})
 e^{Au+B_{\exp}u^2\sqrt{\log(en)}},
 \tag{11}
\]
where \(u=Y/\lambda\), the coordinate source error is \(\epsilon=n^{-1}\),
and the constants are fixed by that runtime. The strict prediction rate
comes from
\[
 n^{-1}(1+C\sqrt{\log(en)})e^{C\sqrt{\log(en)}}
 \le C'n^{-1/2}.
\]
It spends half a power of width from the smaller source defect. The
Gaussian concentration calculation for independent dense copies already
starts at \(n^{-1/2}\). Multiplying that scale by the same unbounded
exponential cannot be absorbed into a fixed constant. A smaller fixed
nonzero label RMS makes the coefficient smaller but does not bound
\(e^{cY^2\sqrt{\log n}}\) uniformly in \(n\).

The same distinction applies to compression theorems that choose a more
accurate source approximation or a larger response-memory order. Their
free approximation parameter can compensate for deterministic
amplification. Independent dense initialization has no such error
tolerance parameter.

## 5. Strongest remaining route: a joint prediction-adjoint moment

Use mobility-Euclidean coordinates
\[
 \Theta=(W^{(1)},\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w).
\]
Let \(P\) embed all initialized Gaussian blocks and a zero readout block.
For a query \(v\), define
\(\mathcal F_v=nf_n(v)\), \(g_v=\nabla_\Theta\mathcal F_v\), and
\(H_v=D_\Theta^2\mathcal F_v\). The exact autonomous equations are
\[
 \dot\Theta=-2\sum_a p_ar_ag_a,
 \qquad
 D_\Theta\dot\Theta
 =-\frac2n\sum_a p_ag_ag_a^\top-2\sum_a p_ar_aH_a.
 \tag{12}
\]
For its variational propagator \(J(t,s)\),
\[
 \nabla_Gf_n(t,v)=\frac1nP^\top J(t,0)^\top g_v(t).
 \tag{13}
\]
The physical tube bounds \(\|g_v(t)\|_2\le C\sqrt n\) on the sphere.
It does not control alignment with \(J\).

Fix a terminal time and query, and define the adjoint
\(q(s;t,v)=J(t,s)^\top g_v(t)\). Put
\(\mathsf L(s)=\sqrt{2/n}[\sqrt{p_a}g_a(s)]_a\).
The exact energy identity is
\[
 \|q(s)\|_2^2+2\int_s^t\|\mathsf L(u)^\top q(u)\|_2^2\,du
 =\|g_v(t)\|_2^2
 -4\int_s^t\sum_a p_ar_a(u)q(u)^\top H_a(u)q(u)\,du.
 \tag{14}
\]
In the inherited Hessian decomposition, the potentially large part is
\[
 H_a=H_{0,a}+\sum_\ell Z_{a,\ell}^\top
 \operatorname{diag}(\phi_\ell''(z_a^{(\ell)})\odot k_a^{(\ell)})
 Z_{a,\ell},\qquad Z_{a,\ell}=D_\Theta z_a^{(\ell)},
 \tag{15}
\]
with bounded operator norms for \(H_{0,a}\) and \(Z_{a,\ell}\).
Thus the missing correlation is
\[
 \frac1n\sum_{\ell,i}|k_{a,i}^{(\ell)}(s)|
       |(Z_{a,\ell}(s)q(s;t,v))_i|^2.
 \tag{16}
\]
A sufficient expectation estimate on a fixed good event is
\[
 \mathbb E\!\left[\mathbf1_{\Omega_n}
   \sum_{\ell,i}|k_{a,i}^{(\ell)}(s)|
          |(Z_{a,\ell}(s)q(s;t,v))_i|^2\right]
 \le C\mathbb E[\mathbf1_{\Omega_n}\|q(s;t,v)\|_2^2],
 \tag{17}
\]
uniformly for \(s\le t\) and unit \(v\). Inserting (17) into (14),
using \(|r_a(s)|\le p_a^{-1/2}Ye^{-\kappa s}\), and applying backward
integral Gronwall would bound
\(\mathbb E[\mathbf1_{\Omega_n}\|q(s;t,v)\|_2^2]\le Cn\).
This is a conditional implication. Estimate (17) is not supplied by the
existing marginal carrier or averaged response theorems.

The tempting fourth-moment replacement shows exactly where it stops.
For two states, boundedness and Lipschitz continuity of \(\phi'\) give
\[
 \|[\phi'(z')-\phi'(z)]\odot k\|_{2,n}
 \le C\|k\|_{4,n}\|z'-z\|_{2,n}^{1/2},
 \qquad \|a\|_{p,n}^p=\frac1n\sum_i|a_i|^p.
 \tag{18}
\]
Indeed \(|\Delta\phi'|^4\le C|\Delta z|^2\), followed by counting
Hölder, proves (18). This half-Hölder estimate is enough for passive-query
chaining, but is not linear in a difference between trained states.
Dividing by the initialization perturbation before taking a derivative
does not preserve a finite bound. The actual differential term is
\(\phi''(z)\odot k\odot Zq\), and its square needs a joint moment,
not a marginal fourth moment of \(k\).

Bounded mixing operators do not preserve the missing counting moments.
An orthogonal matrix can map \((1,\ldots,1)^\top\), with
\(\|\cdot\|_{4,n}=1\), to \(\sqrt n e_1\), with
\(\|\cdot\|_{4,n}=n^{1/4}\). Therefore an operator-norm bound alone
does not transfer coordinate moments to \(Zq\).

There is also a concrete algebraic obstruction even if terminal gradient
coordinates are bounded. Let \(u=n^{-1/2}(1,\ldots,1)^\top\), choose an
orthogonal \(Q\) with \(Qu=e_1\), and let
\(k=(\sqrt{\log(e+n)},0,\ldots,0)\). Then
\[
 H=Q^\top\operatorname{diag}(k)Q
   =\sqrt{\log(e+n)}\,uu^\top,
 \qquad g=\sqrt n\,u.
\]
Every fixed empirical moment of \(k\), and every fixed normalized
exponential moment \(n^{-1}\sum_i e^{\eta|k_i|}\), stays bounded.
The coordinates of \(g\) equal one. Nevertheless
\[
 \frac{\|e^{cH}g\|_2}{\sqrt n}
 =e^{c\sqrt{\log(e+n)}}\longrightarrow\infty,
\]
whereas every fixed normalized Schatten norm of \(e^{cH}-I\) tends to
zero. This is not a neural counterexample. It disproves the proposed
inference from only those marginal moments, bounded mixing maps, and
normalized Schatten bounds. A positive proof must use the joint neural
structure of the adjoint and the trained carriers.

## 6. Localization and the all-time/sphere bridge are separate obligations

Even (17) would first yield a good-event fixed-time sensitivity estimate.
Gaussian Poincaré or Gaussian rotation cannot be applied by inserting a
trajectory-dependent indicator into a global Gaussian inequality. The
passive proof avoids that problem because its good event is independent
of the Gaussian matrix being varied. The full initialization good event
has no analogous independence. The near-root proof avoids it by the
globally Lipschitz scalar extension (5); that extension retains \(\ell_n\).

A precise sufficient replacement would be a family of global
Gaussian-Sobolev extensions \(\widehat f_n(G;u,v)\), agreeing with the
actual flow on \(\Omega_n\), equal to zero at \(u=0\), with continuous
sample paths, a fixed common amplitude bound, and, for one fixed
\(p>2(d+1)\),
\[
 \left\|\left\|\nabla_G
  [\widehat f_n(u,v)-\widehat f_n(u',v')]\right\|_2\right\|_{L^p(G)}
 \le \frac{C_p}{\sqrt n}
       (|u-u'|+\|v-v'\|_2)^{1/2}.
 \tag{19}
\]
The functions and their gradients must have the stated global
integrability. Gaussian rotation then bounds centered increments by
the right side times \(C\sqrt p\). On dyadic nets of
\([0,1]\times S^{d-1}\) with at most \(C_d2^{j(d+1)}\) points, the
\(L^p\) norm of the largest scale-\(j\) increment is at most
\[
 \frac{C_p}{\sqrt n}2^{-j/2+j(d+1)/p}.
\]
The series converges. Telescoping, continuity, and the deterministic
initial value give a strict-root bound for the centered full supremum;
Markov, a union bound for two copies, and
\(\Pr(\Omega_n^c)=o(1)\) yield (2).
This verifies the probability/topology implication and identifies its
missing input. It does not assert that extensions satisfying (19)
have been constructed. Fixed-time second moments such as (17) do not
already imply (19).

The most focused new scientific obligation is therefore a stopped
finite-neuron comparison for the coupled primal and terminal-value
adjoint, proving moments of (16) and their increments with legitimate
Gaussian-domain control. Its incoming and outgoing response sources,
network-dependent terminal condition, and undamped Gram-coupling term
must all be retained, as explicitly listed in the prior sensitivity
route's equations (19)--(26a). Marginal carrier moments do not close
those equations. A second-order reinsertion proof must also respect the
actual \(C^3\) assumption, rather than silently demand a Lipschitz third
activation derivative.

## 7. Final status of this bounded route

| Claim | Status |
| --- | --- |
| All-time whole-sphere near-root independent-copy bound (8), including unbounded activation values | Proved from the inherited broad physical/carrier and good-pair theorems |
| Strict-root passive fluctuation after conditioning on the trained active network | Inherited checked result in its bounded strip-analytic scope |
| The passive theorem also concentrates its random conditional center | Not established |
| Weighted runtime constants remove the width-dependent stability amplification itself | False reading of the runtime estimate; its source accuracy absorbs that amplification |
| Existing marginal carrier and Schatten bounds imply the prediction-directed moment (17) | Not implied by those estimates alone |
| Strict all-time whole-sphere dense-versus-independent-dense root width (2) in the requested broad scope | Open |

The broad strict theorem is neither proved nor falsified here. The new
positive result strengthens the topology of the existing near-root
theorem. Removing its remaining factor requires new joint response
information and justified Gaussian localization, rather than a change
to its population center or an extra hypothesis hidden inside a constant.
