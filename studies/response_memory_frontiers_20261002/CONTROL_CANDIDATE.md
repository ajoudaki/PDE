# Frozen candidate: counterfactual training under arbitrarily switching sample weights

Frozen on 2026-10-02 by the scoped control route. This is a study result,
not established book material. No training experiment has been run for this
candidate. The proposition below has an internal derivation, not an independent
review. It uses the current paper as an explicitly authorized input.

## Recommendation and scientific claim

Use paired response memory as a simulator for choosing finite-amplitude replay
and data-allocation interventions. The distinctive proposed result is that the
memory order needed to track controlled training need not grow with the number
of switches in the data weights. Credit histories can switch arbitrarily fast
and remain poorly reconstructed individually. Their learned interaction is
nevertheless controlled by the product of their bounded projection error and
the small projection error of the smoothly evolving feature history.

The concrete application is retention-constrained adaptation: from one actual
network checkpoint, compare several proposed training continuations, choose a
continuation that improves a new task while limiting old-task prediction drift,
then apply the chosen sample weights to the actual dense network. Each trial
shares the same fixed checkpoint matrices and stores its own short paired
histories. This is a finite-amplitude nonlinear simulation, not a score assigned
to the current gradient.

The following uniform finite-width theorem is the strongest current result.
It does not need a smooth control, a bound on its total variation, a lower bound
on active residual, a successful fit, a small label, or Gaussian initialization.
It does require bounded activation values and derivatives, fixed width, and a
fixed horizon. The practical claim that a *small* order suffices remains open.
The theorem's worst-case stability constant can be too large for operational
certification; no useful numerical certificate is claimed merely from its
existence.

The substantive conjecture is narrower than “MPC works”: in a regime with
substantial hidden-feature motion, low-order paired histories accurately predict
the effect of bursty training interventions even when their credit projections
are inaccurate; this remains useful at burst periods where replacing the
control by its time average gives the wrong continuation. A later policy-ranking
test must additionally show useful decisions. An isolated comparison of two
chronological orders would not establish this claim.

## Source and novelty audit

The paper's footholds are `eq:old-ode`, `eq:old-recon`, `eq:defect`,
`eq:projection-energy`, `eq:e-square`, and the bounded-activation continuation
argument in `app:proof-old`. The extension below changes the drive to bounded
measurable sample weights and proves uniformity over that entire input class.
The paper's small-label all-time theorem is not invoked for switched training.

Nearby work materially limits novelty language:

- [Gu et al., Data Selection via Optimal Control for Language Models, ICLR
  2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ad4891facabf17aa11580686bacfe4e-Paper-Conference.pdf)
  already formulates training-data selection as optimal control, uses training
  dynamics and a costate, and optimizes a downstream objective. Its displayed
  data scores are time-independent for offline corpus selection. Therefore
  “optimal control of training” and “future effects of data” are not novelty
  claims here. The relevant possible contribution is a compact nonlinear trial
  state with a schedule-variation-independent approximation theorem.
- [Aljundi et al., Online Continual Learning with Maximally Interfered Retrieval,
  NeurIPS 2019](https://papers.neurips.cc/paper/9357-online-continual-learning-with-maximal-interfered-retrieval.pdf)
  already selects replay examples by the loss change under a foreseen parameter
  update. A one-step interference score is therefore an inadequate novelty
  baseline. A practical comparison should grant such a baseline actual
  look-ahead, then test whether a longer nonlinear continuation changes the
  decision.
- [Gupta et al., La-MAML, NeurIPS
  2020](https://papers.neurips.cc/paper_files/paper/2020/file/85b9a5ac91cd629bd3afe396ec07270a-Paper.pdf)
  already uses multiple adaptation steps and modulates learning rates through a
  meta-objective to mitigate forgetting. Merely describing a differentiable
  closure as a meta-learner would not add a scientific result. This candidate
  neither asserts new meta-objectives nor assumes intervention derivatives
  converge because trajectories converge.
- [Dietze and Grepl, Reduced Order Model Predictive Control for Parametrized
  Parabolic PDEs](https://arxiv.org/html/2111.00597v2) already develops reduced
  dynamics, control/cost error bounds and certified MPC. Applying a reduced
  model inside MPC, or using Gronwall and constraint tightening, is not itself
  novel. The response-memory-specific content must be the rough-credit/smooth-
  feature mechanism and its uniform controlled-network bound.
- [Dynamical Low-Rank Training of Neural Networks, NeurIPS
  2022](https://proceedings.nips.cc/paper_files/paper/2022/file/7e98b00eeafcdaeb0c5661fb9355be3a-Paper-Conference.pdf)
  is a stronger approximation competitor than Euclidean training of factors:
  it evolves low-rank approximations to gradient flow. A later efficiency claim
  should compare a corresponding dynamical approximation to the learned
  increment around the same checkpoint, including basis and core storage.

This targeted audit does not establish priority or exhaust the literature.
It supports testing a specific extension of the paper; it does not support
calling the entire control application unprecedented.

## Controlled network and exact memory equations

Fix width (n), depth (L\ge2), and a finite training list

\[
 (x_a,y_a)\in\mathbb R^d\times\mathbb R,
 \qquad a=1,\ldots,m.
\]

Use the book's readout (W^{(L+1)}\in\mathbb R^n), which is the paper's
(w). The first weight matrix is (n\times d); the hidden matrices are
(n\times n). With componentwise activations \(\phi_\ell\),

\[
\begin{aligned}
z_a^{(1)}&=W^{(1)}x_a/\sqrt d,&
h_a^{(1)}&=\phi_1(z_a^{(1)}),\\
z_a^{(\ell)}&=W^{(\ell)}h_a^{(\ell-1)},&
h_a^{(\ell)}&=\phi_\ell(z_a^{(\ell)}),\quad 2\le\ell\le L,\\
f_a&=W^{(L+1)\top}h_a^{(L)}/n,&r_a&=f_a-y_a.
\end{aligned}
\]

The backward responses exclude the residual:

\[
\delta_a^{(L)}=W^{(L+1)}\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
 W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

An admissible open-loop control is a measurable function

\[
 u:[0,T]\longrightarrow[0,U]^m,\qquad U<\infty.
\]

The controlled instantaneous loss is
\(\mathcal L_u(t,\theta)=m^{-1}\sum_a u_a(t)r_a(\theta)^2\).
Using the canonical block mobilities \((n,1,\ldots,1,n)\), its parameter
flow, denoted \(F_u(t,\theta)\), is

\[
\begin{aligned}
\dot W^{(1)}&=-\frac2m\sum_a u_a r_a\delta_a^{(1)}x_a^\top/\sqrt d,\\
\dot W^{(\ell)}&=-\frac2{nm}\sum_a u_a r_a\delta_a^{(\ell)}
 h_a^{(\ell-1)\top},\quad 2\le\ell\le L,\\
\dot W^{(L+1)}&=-\frac2m\sum_a u_a r_a h_a^{(L)}.
\end{aligned}                                                   \tag{1}
\]

Define the clock speed by

\[
 \rho_u=\left(\frac1m\sum_a(u_a r_a)^2\right)^{1/2},\qquad
 \dot\tau=\rho_u,\qquad \tau(0)=1.                              \tag{2}
\]

This is the RMS of the weighted drive, not \(\sqrt{\mathcal L_u}\).
That choice makes \(m^{-1}\sum_a(u_a r_a/\rho_u)^2=1\) when
\(\rho_u>0\), uniformly over every admissible control.

At order (q\ge1), retain the paper's raw moments
\(\bar h_{a,j}^{(\ell-1)},\bar\delta_{a,j}^{(\ell)}\in\mathbb R^n\)
for \(0\le j<q\), all samples, and hidden links \(\ell\ge2\).
Let (p_j) be shifted Legendre polynomials with
\(p_j(1)=1\) and \(\int_0^1p_jp_k=\mathbf1_{j=k}/(2j+1)\).
The raw ODE is

\[
\begin{aligned}
\dot{\bar h}_{a,j}^{(\ell-1)}
 &=\rho_u h_a^{(\ell-1)}-\frac{\rho_u}{\tau}
   \left(j\bar h_{a,j}^{(\ell-1)}
      +\sum_{k<j}(2k+1)\bar h_{a,k}^{(\ell-1)}\right),\\
\dot{\bar\delta}_{a,j}^{(\ell)}
 &=u_a r_a\delta_a^{(\ell)}-\frac{\rho_u}{\tau}
   \left(j\bar\delta_{a,j}^{(\ell)}
      +\sum_{k<j}(2k+1)\bar\delta_{a,k}^{(\ell)}\right),\\
\widehat W^{(\ell)}
 &=W_c^{(\ell)}-\frac2{nm\tau}\sum_{a,j<q}(2j+1)
    \bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
\end{aligned}                                                   \tag{3}
\]

Here \(\theta_c\) is the physical network at the start of planning, and
\(W_c^{(\ell)}\) its shared fixed hidden matrices. Every response in (3)
is recomputed from the reconstructed network. The first matrix and readout
follow (1) in that same network. Initialize only the degree-zero forward
moment to its checkpoint feature; all other moments are zero. Thus the
physical initialization is exactly \(\theta_c\), including arbitrary
nonzero checkpoint readout.

For derivations only, put
\(b_a^{(\ell)}=u_a r_a\delta_a^{(\ell)}/\rho_u\) where
\(\rho_u>0\), and put it equal to zero otherwise. The raw algorithm
never divides by \(\rho_u\). The history prefix is constant in (h)
and zero in (b), just as in the original speed-clock construction.
No derivative of (u) occurs anywhere in (1)--(3).

## Proposition: uniformity over measurable open-loop controls

Assume every \(\phi_\ell\in C^{1,1}_{\rm loc}(\mathbb R)\), with both
\(\phi_\ell\) and \(\phi_\ell'\) globally bounded. Fix finite data,
finite checkpoint \(\theta_c\), finite width and depth, and (U,T<\infty).
Then the dense controlled flow and every order-(q) system (3) have unique
Carathéodory solutions on \([0,T]\). There is a finite constant (C_T),
independent of (q) and of the particular measurable control (u), such that

\[
 \sup_{u\in L^\infty([0,T];[0,U]^m)}\;
 \sup_{0\le t\le T}
 \|\widehat\theta_{q,u}(t)-\theta_u(t)\|_2
 \le \frac{C_T}{\sqrt{q(q+1)}}.                               \tag{4}
\]

The parameter norm in (4) is the ordinary product Euclidean/Frobenius norm.
For every fixed bounded input set \(\mathcal X\), the same order holds for
\(\sup_{u,t,x\in\mathcal X}|\widehat f_{q,u}(t,x)-f_u(t,x)|\).
Constants may depend on (n,m,d,L,T,U,\theta_c\), data and activations.
In particular, (4) is not a width-uniform, all-time, or SGD theorem.

### Proof

**1. Local existence and one common physical bound.** At fixed (q), the
raw right-hand side is measurable in physical time. On any compact set with
\(\tau>0\), it is uniformly locally Lipschitz in raw state for
\(u\in[0,U]^m\): the weighted residual norm is Lipschitz, network
responses are locally Lipschitz, and reconstruction divides only by \(\tau\).
The local integral equation is a contraction on a sufficiently short time
interval using that common Lipschitz constant. This gives a unique absolutely
continuous local solution satisfying the ODE almost everywhere. The same
argument applies to the dense equation.

Set \(Y^2=m^{-1}\sum_a y_a^2\),
\(\alpha_\ell=\sqrt n\|\phi_\ell\|_\infty\),
\(s_\ell=\|\phi_\ell'\|_\infty\), and
\(X=\max_a\|x_a\|_2/\sqrt d\).
The common readout equation gives, almost everywhere,

\[
\begin{aligned}
\frac d{dt}\|W^{(L+1)}\|_2^2
 &=-\frac{4n}m\sum_a u_a(f_a-y_a)f_a\\
 &=\frac nm\sum_a u_a y_a^2
   -\frac{4n}m\sum_a u_a(f_a-y_a/2)^2\le nUY^2.
\end{aligned}
\]

Therefore both models satisfy

\[
B_w=\sqrt{\|W_c^{(L+1)}\|_2^2+nUY^2T},\quad
\|W^{(L+1)}\|_2\le B_w,\quad
\rho_u\le R:=U(B_w\alpha_L/n+Y),\quad
1\le\tau\le A:=1+RT.
\]

Put (S=RT). Bounds on the backward responses and hidden matrices are
obtained from the top layer downward. Set \(\beta_L=s_LB_w\), and for
\(\ell=L,L-1,\ldots,2\) set

\[
D_\ell=\|W_c^{(\ell)}\|_F+\frac{2A}{n}\beta_\ell\alpha_{\ell-1},
\qquad \beta_{\ell-1}=s_{\ell-1}D_\ell\beta_\ell.              \tag{5}
\]

To verify (5), the normalized drive has sample RMS one, so

\[
 \frac1m\sum_a\|b_a^{(\ell)}\|_2^2\le\beta_\ell^2.
\]

The moment representation of (3), polynomial projection contraction, and
Cauchy--Schwarz in history and sample show

\[
\|\widehat W^{(\ell)}-W_c^{(\ell)}\|_F
\le\frac2n\sqrt{(S\beta_\ell^2)(A\alpha_{\ell-1}^2)}
\le\frac{2A}{n}\beta_\ell\alpha_{\ell-1}.
\]

For dense flow the integrated update has the smaller bound
\(2S\beta_\ell\alpha_{\ell-1}/n\). Backward recursion then proves
\(\|\delta_a^{(\ell-1)}\|_2\le\beta_{\ell-1}\).
This is a descending induction, with no circular bound. The first layer
obeys \(\|W^{(1)}-W_c^{(1)}\|_F\le2S\beta_1X\).
Thus both physical models stay in a compact set independent of (q,u).
At each fixed (q), bounded histories and \(1\le\tau\le A\) bound all
raw moments as well. A finite maximal endpoint would have a limit and admit
local continuation. Both systems therefore exist through (T).

**2. Pauses of the clock and exact defect identities.** When \(\rho_u=0\),
all products \(u_ar_a\), every moment velocity and every physical velocity
vanish almost everywhere. This does not assert permanent stopping: a later
control may activate a sample with nonzero residual. The state is constant on
every interval on which \(\tau\) is constant. At each fixed (q), the
bounded raw state gives \(\|\dot\theta\|\le K_q\rho_u\), and hence
\(\|\dot h\|\le K'_q\rho_u\). Consequently the forward history is a
well-defined Lipschitz function of the clock after identifying its constant
intervals. The generalized inverse of \(\tau\) supplies a measurable
backward history; choices on zero clock-mass intervals do not affect any
integral. The change-of-variable identity for growing absolutely continuous
integrals identifies (3) with the Legendre moments of these histories.

Let \(\Pi_q\) be polynomial projection on \([0,\tau(t)]\), and put
\(h_a^*=(\Pi_qh_a)(\tau)\), \(b_a^*=(\Pi_qb_a)(\tau)\), with the
layer indices as in (3). The current inserted values need only be measurable
in clock time. Differentiating the finite moment formulas almost everywhere
gives

\[
\begin{aligned}
\dot{\widehat\theta}&=F_u(t,\widehat\theta)+E,\qquad E_1=E_{L+1}=0,\\
E_\ell&=\frac{2\rho_u}{nm}\sum_a
 (b_a^{(\ell)}-b_a^{(\ell)*})
 (h_a^{(\ell-1)}-h_a^{(\ell-1)*})^\top.                       \tag{6}
\end{aligned}
\]

There are no impulse terms at control jumps: neither raw moments nor weights
jump. For either inserted history (v), define its squared projection error
\(D_v=\int_0^\tau\|v-\Pi_qv\|_2^2d\xi\). Differentiating its least-
squares minimum cancels terms paired with the projection residual, yielding

\[
 D_v(t)=\int_0^t\rho_u(s)\|v(s)-v^*(s)\|_2^2ds.             \tag{7}
\]

The prefix errors are zero. The backward join may jump, which is allowed by
(7). Cauchy--Schwarz in physical time gives

\[
 \int_0^t\|E_\ell\|_Fds
 \le\frac2{nm}\sum_a\sqrt{D_{b,\ell,a}(t)D_{h,\ell-1,a}(t)}. \tag{8}
\]

**3. Forward regularity independent of switching and order.** For a forward
history define

\[
 Z_\ell(t)=\frac1m\sum_a\int_0^{\tau(t)}
                 \|\partial_\xi h_a^{(\ell)}\|_2^2d\xi.
\]

The Legendre estimate proved in the paper gives

\[
 \frac1m\sum_aD_{h,\ell,a}\le
 \frac{A^2Z_\ell}{4q(q+1)}.                                  \tag{9}
\]

Endpoint evaluation on degree-below-(q) polynomials has norm
\(q/\sqrt\tau\). The sample RMS bound on (b) therefore bounds its
endpoint projection error by \((q+1)\beta_\ell\). Inserting this in (6),
then using (7) and (9), proves

\[
\begin{aligned}
\int_0^t\rho_u\|E_\ell/\rho_u\|_F^2ds
&\le\frac{4(q+1)^2\beta_\ell^2}{n^2}
             \frac1m\sum_aD_{h,\ell-1,a}\\
&\le\frac{2A^2\beta_\ell^2}{n^2}Z_{\ell-1}.                 \tag{10}
\end{aligned}
\]

The quotient is assigned zero on pauses; the integral ignores them. Put
\(v_1=2\beta_1X\) and
\(v_\ell=2\beta_\ell\alpha_{\ell-1}/n\) for hidden links. These
bound \(\|F_{u,\ell}/\rho_u\|\). Forward differentiation gives

\[
\partial_\xi h_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
\left[(F_{u,\ell}/\rho_u+E_\ell/\rho_u)h_a^{(\ell-1)}
    +\widehat W^{(\ell)}\partial_\xi h_a^{(\ell-1)}\right].
\]

Start with \(Z_1\le S(s_1v_1X)^2=:Z_1^*\). The squared three-term
triangle inequality and (10) inductively give (Z_\ell\le Z_\ell^*), where

\[
Z_\ell^*=3s_\ell^2\left[
 S v_\ell^2\alpha_{\ell-1}^2+
 \left(D_\ell^2+
       \frac{2A^2\beta_\ell^2\alpha_{\ell-1}^2}{n^2}\right)
 Z_{\ell-1}^*\right].                                       \tag{11}
\]

Every displayed constant is independent of (q,u). No backward derivative,
control derivative, or switch count was estimated.

**4. Small source and ordinary stability.** Projection contraction gives
\(m^{-1}\sum_aD_{b,\ell,a}\le S\beta_\ell^2\). Combining this with
(8), (9), and sample Cauchy--Schwarz yields

\[
\int_0^T\|E\|_2dt
\le\frac{B}{\sqrt{q(q+1)}},\qquad
B=\frac An\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}^*}.   \tag{12}
\]

Choose a convex compact physical region containing both trajectories and
their joining segments. Bounded (u), fixed finite width, and locally
Lipschitz activation derivatives give one finite Lipschitz constant
\(\Lambda\) for (F_u(t,\cdot)\) on that region, uniformly in (u,t).
Subtract (1) from (6), integrate, and use an integrating factor to obtain

\[
\sup_{t\le T}\|\widehat\theta_{q,u}(t)-\theta_u(t)\|_2
\le\frac{Be^{\Lambda T}}{\sqrt{q(q+1)}}.
\]

Forward recursion bounds the prediction Jacobian uniformly on the same region
and a bounded input set, which proves the prediction assertion. Taking the
supremum over (u) is legitimate because all constants were chosen before
choosing (u). This completes the internal proof.

## Consequence for a finite menu of interventions

Let \(\mathcal U\) be any fixed finite menu of admissible open-loop controls,
possibly containing arbitrarily many switches. Let \(\varepsilon_q\) bound
the predictor error uniformly over that menu, the horizon, and the bounded
old/new validation inputs. A rigorously validated bound may come from (4);
an observed coarse/fine difference alone is not such a bound.

Use new-task terminal RMSE (J(u)) as the objective, and let

\[
C(u)=\sup_{0\le t\le T}
 \left[\frac1{|V_{\rm old}|}\sum_{x\in V_{\rm old}}
              |f_u(t,x)-f_c(x)|^2\right]^{1/2}
\]

be old-function drift on a fixed validation list. Reverse triangle inequalities
give \(|J-\widehat J|\le\varepsilon_q\) and
\(|C-\widehat C|\le\varepsilon_q\). If (u_q) minimizes \(\widehat J\)
among controls with \(\widehat C\le c-\varepsilon_q\), then

\[
 C(u_q)\le c,\qquad
 J(u_q)\le\min_{u\in\mathcal U:\ C(u)\le c-2\varepsilon_q}J(u)
                         +2\varepsilon_q.                    \tag{13}
\]

The comparator has enough slack to enter the surrogate feasible set, after
which two objective-error terms prove (13). If that set is empty, no decision
is certified. This consequence does not differentiate through training and
does not claim to solve a continuous global optimal-control problem.

The physical dense checkpoint is Markovian: if two histories give exactly the
same entire physical parameter state, the same future open-loop control gives
the same dense continuation. This proposal does not posit extra causal power
in old history beyond the checkpoint. Histories compress *future trial
continuations*. A fresh restart uses the checkpoint as its fixed source and a
new zero-backward prefix. Manipulating hidden moment coordinates while leaving
the physical state unchanged is not asserted to be a realizable dense-network
intervention.

For feedback (u(t)=\pi(\theta(t))), dense and closure generally realize
different controls. The proof above compares identical open-loop functions.
If (\pi) is Lipschitz, a separate bound on (F_{\pi(\theta)}(\theta))
may recover a comparison with an additional feedback Lipschitz constant.
Discontinuous threshold policies are outside that extension. Replanning at
an observed dense checkpoint can use the present theorem for each candidate
open-loop segment; global closed-loop stability is not established here.

## Mechanistic interpretation and limits

For any same-history pair, orthogonality gives

\[
\int b h^\top-\int(\Pi_qb)(\Pi_qh)^\top
      =\int[(I-\Pi_q)b][(I-\Pi_q)h]^\top.                    \tag{14}
\]

If the feature history is exactly polynomial of degree below (q), (14)
vanishes for every square-integrable credit history, however irregular it is.
The feature need not be constant: an affine moving feature already suffices
at (q=2). This is an algebraic illustration, not evidence that trained
network features are affine. The controlled theorem replaces exact
polynomiality by a uniform forward derivative bound and controls its feedback.

The online quantities (D_h,D_b) in (7) require only scalar accumulators per
sample/link in addition to existing moments. Their product gives (12)'s
data-dependent source bound through (8). This is more specific than either
credit reconstruction error by itself or the rank of a final matrix. It is
not by itself a prediction-error bound: propagation remains necessary.

Negative weights are excluded because the readout bound uses nonnegativity.
Unbounded activations, momentum, Adam, minibatch noise, growing data lists,
intervention sensitivities, and arbitrary-width uniformity are not included.
Extending them would require another argument. The learning-speed clock is
used intentionally: a joint clock containing the derivative of (b) is not
well defined as an ordinary absolutely continuous speed for arbitrary jumps.

## Resource accounting

For (B\) simultaneous trial continuations from one checkpoint, hidden fixed
storage is \((L-1)n^2\), shared by every branch. Evolving branch storage is

\[
 B\{2(L-1)mnq+n(d+1)+1\},
\]

plus optional \(O(BLm)\) projection-error accumulators. Dense independent
branches require \(B\{(L-1)n^2+n(d+1)\}\) evolving scalars. The gain in
branch state requires (2mq\ll n\), not merely (q<n\).
Control descriptions and their event stream must also be counted. A periodic
generator uses a phase, period and fixed envelope; a tabulated arbitrary
schedule uses as many stored values as its table contains, or a shared streamed
input. No control table is hidden inside the memory count.

The same fixed dense matrix still acts forward and backward. Per branch and
RHS evaluation the leading work remains
\(O(Lmn^2+Lm^2nq+Lmnq+nmd)\). Numerical integration must resolve the
control switches. Thus memory-order independence of switch count is not
runtime independence of switch count, and the theorem does not promise lower
FLOPs than dense training. Sequential dense trials can also avoid a factor-(B)
storage cost at the price of reduced concurrency; wall-clock benefit is open.

## Frozen diagnostic pilot: at most twelve trajectories, twenty GPU minutes

This is an initial mechanism test, not a full policy-optimization campaign.
Execution requires the supervisor's allocation of GPU 0 after this file is
frozen. All inputs are generated within this study; no other study supplies
data or initial conditions. No scientific configuration may be changed after
seeing its result. A failure is retained.

**Question.** Does low-order response memory remain predictive when increasing
control switching makes the credit projection inaccurate, in a nonlinear
adaptation where averaging the control is insufficient?

**Models and data.** Use (L=2,n=512,d=3\), tanh, canonical independent
Gaussian hidden initialization and exactly zero readout, seed 20261002.
Inputs are \(x(\vartheta)=(\sqrt2\cos\vartheta,\sqrt2\sin\vartheta,1)\)
and labels \(y(\vartheta)=\sin(2\vartheta)+0.4\cos(3\vartheta)\).
Take eight equally spaced interior midpoints in each of the arcs
\([-\pi/2,0]\) and \([0,\pi/2]\), called old and new. The nonzero third
coordinate avoids forced odd symmetry; the correlated geometry and nonlinear
hidden matrices are retained. Passive queries are 256 uniform interior
midpoints per arc. Their labels and initial checkpoint function define the
new objective and old drift respectively.

First train the old set alone until its MSE first reaches (10^{-3}\) or
physical time 80, whichever occurs first. Failure to fit is a failed mechanism
gate; stop. This is trajectory 1. Its actual physical state is the shared
checkpoint for all later continuations. New trials use all sixteen samples,
with weights (u_a=2\lambda(t)\) on old samples and
(u_a=2(1-\lambda(t))\) on new ones, so mean sample weight is one.
Take adaptation horizon (T=24\).

The mean replay envelope is

\[
 \bar\lambda(t)=
 \begin{cases}0.15,&0\le t<12,\\0.35,&12\le t\le24.\end{cases}
\]

For (N\in\{2,8,32\}\) full periods on each half-horizon, let

\[
 \lambda_N(t)=\bar\lambda(t)+0.1\,
  \operatorname{sgn}\sin(2\pi N(t\bmod12)/12).
\]

The value at switch instants is defined by the right-hand interval. Every
control has the same total exposure on each half and stays between 0.05 and
0.45. Two positive group weights also avoid zero-drive complications in the
numerical pilot; the theorem covers those complications analytically.
The envelope is retained at every frequency so fast cycling does not erase
the macroscopic adaptation programme.

Run dense, (q=3\), and (q=7\) for each of the three frequencies:
trajectories 2--10. Run one additional dense continuation with
\(\lambda=\bar\lambda\): trajectory 11, the strongest averaging control.
A tangent predictor frozen at the actual checkpoint, including all mobility
blocks, is evaluated on all switched controls as an inexpensive mechanistic
baseline. It does not count as a fit, but its storage and time are recorded.
One additional trajectory, number 12, is reserved for numerical refinement
of the case with the largest reported closure discrepancy; this selection is
a numerical check, not a scientific replicate. No further fit follows a
favorable or unfavorable result within this pilot.

**Numerics.** Float64 adaptive Heun with a common event list, maximum physical
step (1/64\), absolute/relative local tolerances (10^{-8}\)/(10^{-6}\),
and every accepted step clipped to the next control switch. Preserve both
right-hand and left-hand drive values at events. Report predictions on a common
mesh containing 193 uniform times and all switches. Refine the reserved
trajectory with half maximum step and both tolerances divided by four.
If dense or closure discrepanices are below the numerical sensitivity scale,
call that comparison unresolved, not exact agreement. A hard twenty-minute
aggregate GPU budget overrides incomplete fits. Record every unfinished run.

**Measurements.** Primary error is maximum-over-recorded-time passive-query
RMS between closure and same-control dense flow. Record it for each (N,q\).
Also record maximum hidden activation RMS displacement from the checkpoint,
old prediction drift, new RMSE, the clock-integrated relative credit projection
error \((\sum D_b/\int\sum\|b\|^2d\xi)^{1/2}\), the analogous forward
error, and the source bound (8). Define a zero-energy credit relative error
as not applicable, never as a favorable zero. Dense histories may be recorded
only for these diagnostics; closure evolution cannot read them. Compare the
switched dense continuation with the dense averaged-control continuation on
the identical passive-query/time metric.

**Pass.** Every numerical and mechanism gate passes; hidden activation RMS
movement is at least 0.10 in one hidden layer; maximum error of (q=7\) is
at most 0.02 at all three frequencies; at (N=32\), relative backward
projection error is at least 0.30 at one tested order; and for at least one
of (N=2,8\), averaged-control prediction error is at least twice the
(q=7\) error and at least 0.02. The final requirement excludes a win
explainable solely by high-frequency averaging. Low-order error need not be
monotone in frequency or order.

**Fail.** With all validity gates passed, (q=7\) error exceeds 0.05 at
either (N=8\) or (N=32\), or high-frequency error exceeds four times
the (N=2\) error while its magnitude exceeds 0.02. This rejects the present
small-order practical witness, not the asymptotic proposition.

**Inconclusive.** Anything between these thresholds, insufficient feature
motion, insufficient credit roughness, averaging that already explains every
successful prediction, numerical sensitivity above one quarter of the 0.02
accuracy threshold, or exhausted budget. Stop without a changed testbed.

If the pilot passes, the next proposed test is policy ranking at matched
total replay exposure, against dense rollouts, current-NTK continuation,
short actual look-ahead, time-averaged controls and dynamical low-rank
continuation. Its budget and menu must be separately frozen and authorized.
This pilot cannot establish improved continual-learning performance, broad
generalization, or an efficient controller by itself.

## Claim ledger and hostile audit

| Claim | Status | Strongest surviving issue | Cheapest resolver |
|---|---|---|---|
| Controlled raw moment system, product defect and projection energy | Exact algebra internally checked | Implemented discretization may break event handling | Analytic identities plus directional/RHS check |
| Unique finite-horizon controlled dense/closure solutions for bounded activations | Internally derived under stated assumptions | Measurable controls and clock pauses need independent scrutiny | Fresh proof review of Steps 1--2 |
| Uniform (O(q^{-1})\) tracking with no control-variation dependence | Internally derived, fixed width only | Constants can be enormous; no practical rate inferred | Fresh proof review, then frozen pilot |
| Bounded credit error times smooth-feature error controls learned interaction | Exact identity and derived bound | High-frequency averaging can mimic empirical success | Non-averaging requirement in pilot |
| Small order gives useful finite-amplitude continuation predictions | Open empirical conjecture | Significant feature learning may force much larger (q\) | Pilot pass/fail rule |
| The representation improves intervention decisions under memory limits | Open | Dense sequential look-ahead or dynamical low rank may be as effective | Separately authorized policy-ranking and resource test |
| Uniform result for the same feedback controller | Not claimed | Different states generate different controls; threshold discontinuity | Separate feedback theorem |
| Practical certified retention guarantee | Conditional only via (13) | Worst-case exponential constant can be vacuous | Useful validated local propagation bound; observed error is not one |

The main structural objection is propagation, not existence of a small product
source. A small product source can still be amplified. The main mundane
explanation is control averaging, followed by effectively frozen features.
The pilot attacks both, but cannot rule them out for all tasks. The exact
control class includes much rougher signals than the pilot, while the pilot's
small-order success would concern only one instance and one seed.

## Reading inventory and frozen source hashes

Read in full: `paper/main.tex` and every included mathematical file listed
below; `docs/index.qmd`; `docs/notation.qmd`. No maintained API was used, and
no other study or archived book source was read. Required skills read:
canonical notation plus its neural-response-memory reference; investigate-
conjectures plus research contract, adversarial audit and decisive experiments;
solve-math-rigorously. This scoped assignment replaced author startup reading.

External sources above were read at their relevant method/definition sections,
not audited in full. Search-result-only adjacent sources included MER,
Look-Ahead Selective Plasticity, and Predictive Differential Training; no
mathematical theorem or claim of exclusion rests on those snippets.

```text
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1  paper/results.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be  paper/proof_tracking.tex
07ebf620943f5e8078e4f7647dfa9df893157f16d29c684e758dcd63d33eacd4  paper/proof_finite_time.tex
14cfb87d7f4932131c984781fc0bc03b955f883d4fc909c4794c2be4bcc1bedf  paper/comparison_appendix.tex
f1a5c87937b1c805faa89edee9fb2ad2809de1f873b4e83888ccf5e5cdf673e2  paper/sphere_appendix.tex
f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de  docs/index.qmd
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023  docs/notation.qmd
```
