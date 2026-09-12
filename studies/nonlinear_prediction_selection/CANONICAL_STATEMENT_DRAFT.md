#### C.4.9. Nonlinear prediction selection during a finite added-data episode

This result concerns the whole-circle prediction selected by actual nonlinear
training after a fixed amount of learning from a component whose mixture weight
vanishes. The physical training law is unchanged throughout each run. The
limiting episode is a constrained gradient flow with evolving hidden features;
its initialization is the established fitted reference state, obtained from
the original initialization by a justified initial-layer limit.

##### Model, determining equation and theorem

Use the canonical bias-free network with two tanh hidden layers,

\[
 u=x/\sqrt2\in S^1,\quad h^1_n=\tanh(W^1_nu),\quad
 h^2_n=\tanh(W^2_nh^1_n),\quad f_n=(W^3_n)^Th^2_n/n.
\]

Initialize every entry and block independently, centered Gaussian with stored
variances \((1,1/n,1/n^2)\). Use mobilities \((n,1,n)\), the unhalved mean square,
and physical gradient flow. Keep the actual finite initial Gaussian readout.
Set

\[
 \nu_*={1\over2}\delta_{(\sqrt2e_1,1)}
             +{1\over2}\delta_{(\sqrt2e_2,-1)},\qquad
 \mu_{\epsilon,\alpha,y}=(1-\epsilon)\nu_*+\epsilon\nu_{\alpha,y},
\]
\[
 \nu_{\alpha,y}=\delta_{(\sqrt2u_\alpha,y)},\quad
 u_\alpha=(\cos\alpha,\sin\alpha),\quad
 |\alpha-\pi/4|\le1/1216,\quad 3/8\le y\le5/8.
 \tag{NS1}
\]

This fixed compact parameter rectangle has nonempty interior in location and
label. All its added inputs are nonorthogonal to both reference inputs. Its
labels are admitted for every fixed \(Y\ge1\). All actual mixture flows begin
at the original Gaussian initialization and use that same mixture throughout.

Let \(H_1=L^2(\Omega_1)\) and \(H_2=L^2(\Omega_2)\) be the canonical generated
Gaussian action spaces, with initialized action \(A_0:H_1\to H_2\) and its true
Hilbert adjoint. Their construction is by the joint Gaussian finite-program
law, including the response to every reused forward and transpose call.
The raw state is \(\theta=(w,K,c)\), where
\(w\in L^2(\Omega_1;\mathbb R^2)\), \(K:H_1\to H_2\) is Hilbert–Schmidt,
\(c\in H_2\), and \(A=A_0+K\). Only the increment is Hilbert–Schmidt.
Use the squared metric \(\|\Delta w\|_2^2+\|\Delta K\|_{HS}^2+\|\Delta c\|_2^2\).

The established reference endpoint \(\theta_\dagger\) is explicitly determined
from \((g,A_0,0)\), \(g\sim N(0,I_2)\), by the reference feature equation:
write \(\phi=\tanh\), \(H^1(u)=\phi(w\cdot u)\), \(H^2(u)=\phi(AH^1(u))\),
\(\delta(u)=c\phi'(AH^1(u))\), and \(Q(u)=A^*\delta(u)\). Starting at
\((w,K,c)=(g,0,0)\), solve

\[
 \partial_s w={1\over2}\sum_{a=1}^2 y_a\phi'(w\cdot e_a)Q(e_a)e_a,
 \quad \partial_sK={1\over2}\sum_{a=1}^2y_a\delta(e_a)\otimes H^1(e_a),
 \quad \partial_sc={1\over2}\sum_{a=1}^2y_aH^2(e_a),
\]

where \(y_1=1,y_2=-1\), and stop at the unique first \(s=s_\dagger\le10\)
with \(\langle c,(H^2(e_1)-H^2(e_2))/2\rangle=1\). The global clock construction
in C.4.5 proves well-posedness of this prescription and identifies it with the
physical reference endpoint. Put \(F_*(\sqrt2u)=f_{\theta_\dagger}(u)\).
The zero readout in this population initialization is the limit of the actual
finite readout and imposes no finite-network reset.

For every state used below, define its current raw prediction gradient

\[
 g_\theta(u)=\left(
   \phi'(w\cdot u)Q(u)u,\quad \delta(u)\otimes H^1(u),\quad H^2(u)
                    \right),
\]
\[
 G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad
 M_\theta=G_\theta^*G_\theta,\quad
 \Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
 \tag{NS2}
\]

The inverse exists throughout the asserted episode. The determining evolution
and reconstruction are

\[
 {d\bar\theta_{\alpha,y}\over d\tau}
   =-2\big(f_{\bar\theta_{\alpha,y}}(u_\alpha)-y\big)
                  \Pi_{\bar\theta_{\alpha,y}}g_{\bar\theta_{\alpha,y}}(u_\alpha),
 \qquad \bar\theta_{\alpha,y}(0)=\theta_\dagger,
 \tag{NS3}
\]
\[
 P_{\alpha,y}(\tau,\sqrt2u)
   =\left\langle\bar c(\tau),
      \tanh\big((A_0+\bar K(\tau))\tanh(\bar w(\tau)\cdot u)\big)\right\rangle.
 \tag{NS4}
\]

Every coefficient in (NS3) is computed from the specified current state and
the established initialized action. In particular its projection and all
hidden features are recomputed along the evolution. There is no coefficient
supplied by an unknown changed-law trajectory.

**Theorem.** There exist \(\epsilon_0,\tau_0,a,j>0\), uniform over the parameter
rectangle (NS1), with these properties.

1. Equation (NS3) has a unique strong solution on \([0,\tau_0]\) in a fixed
   neighborhood of \(\theta_\dagger\). It is constructed on the canonical
   initialized carrier with its full retained reference history. It preserves
   the two reference predictions exactly. It determines (NS4) over the whole
   circle.

2. For every \(0<\epsilon<\epsilon_0\), the original-initialization mixture
   population GF exists and is unique through \(T_\epsilon=\tau_0/\epsilon\).
   For every \(0<\tau_-<\tau_0\),
   \[
    \sup_{(\alpha,y)}\sup_{\tau_-\le\tau\le\tau_0}
      \|\theta_{\mu_{\epsilon,\alpha,y}}(\tau/\epsilon)
                    -\bar\theta_{\alpha,y}(\tau)\|_{\rm raw}\longrightarrow0.
    \tag{NS5}
   \]
   The same convergence holds for predictions uniformly over the entire
   circle and for the finite named hidden observations stated below.
   The exclusion of \(\tau=0\) records the genuine initial layer; no pretraining
   stage is imposed on any actual run.

3. With \(R_\nu(f)=\int(f(x)-y)^2\,d\nu(x,y)\), the selected finite-episode
   prediction satisfies
   \[
      R_{\nu_{\alpha,y}}(F_*)
       -R_{\nu_{\alpha,y}}(P_{\alpha,y}(\tau_0))\ge a.
    \tag{NS6}
   \]
   This is risk on the added component itself, without its factor \(\epsilon\).
   For \((v_1,v_2,v_3)=(e_1,e_2,u_\alpha)\), its paired upper-hidden change is
   \[
    {1\over3}\sum_{i=1}^3
      \|H^2_{\bar\theta_{\alpha,y}(\tau_0)}(v_i)
                         -H^2_{\theta_\dagger}(v_i)\|_2^2\ge j.
    \tag{NS7}
   \]
   Both states use the same initialized primitives. The hidden displacement
   therefore measures adaptation caused by the added law after reference fitting.

4. For every separately fixed \(\epsilon\in(0,\epsilon_0)\) and law in (NS1),
   actual finite GF converges in probability to the mixture population
   prediction in \(C([0,T_\epsilon]\times\sqrt2S^1)\), with the joint
   same-layer internal observations needed for paired hidden measurements.
   Consequently, for every such fixed law and every \(\eta>0\),
   \[
    \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
     \Pr\!\left\{\sup_x|f_{n,\mu_\epsilon}(T_\epsilon,x)
                       -P_{\alpha,y}(\tau_0,x)|>\eta\right\}=0.
    \tag{NS8}
   \]
   Train a reference network with the same initial arrays, including readout,
   and define the directly paired finite observable
   \[
    J_{2,n,\epsilon}={1\over3n}\sum_{i=1}^3
      \|h^2_{n,\mu_\epsilon}(T_\epsilon,\sqrt2v_i)
                    -h^2_{n,\nu_*}(T_\epsilon,\sqrt2v_i)\|_2^2.
    \tag{NS9}
   \]
   In the same iterated order it converges in probability to (NS7)'s
   population quantity. In particular the probability that the added-risk
   gain is at least \(a/2\) and \(J_{2,n,\epsilon}\ge j/2\) tends to one.

The constants need not be numerically practical. The theorem asserts one fixed,
nonzero slow-time episode, not a final endpoint for the changed law. It gives
no simultaneous width/contamination rate and no raw-GD extension. The scale
\(\tau=\epsilon t\) follows from the stable reference-residual equations and
the remaining tangential force, as proved below.

##### Proof architecture

The proof first establishes a Gaussian source bound for a small perturbation
of the reference in integrated control mass, uniformly in physical horizon.
A protected Gaussian-row argument then proves strict endpoint conditioning.
Together these facts construct (NS3) and continue the actual mixture through
(NS5). An exact residual identity proves selection on the slow clock.
A fixed-readout hidden contrast and the exact risk derivative yield (NS6)–(NS7).
Finally a same-array, one-reference cutoff comparison identifies actual finite
GF and the paired observations in (NS8)–(NS9).
