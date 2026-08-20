# Finite causal descriptions of dense feature learning

## A unified mathematical synthesis of the repository as of 19 August 2026

This document is a reconstruction of the scientific program, not a directory-by-directory paraphrase. It reads the dated master monograph together with the maintained reports under studies/, uses one notation wherever the models genuinely agree, and keeps different model classes visibly separate when transferring a conclusion would be invalid. The three residual-network workstreams are now indexed together under [`studies/resnet_pde/`](studies/resnet_pde/).

The short verdict is:

> The project has an explicit, autonomous, finite-source operator PDE whose internal gradient structure is exact and whose low-order numerical predictions are strong. It also has rigorous fixed-order mean-field derivative compilers and a rich non-Taylor rational-resummation program in a quadratic laboratory. What it does **not** yet have is the theorem joining those pieces: convergence of the finite-source PDE hierarchy, identification of its infinite-source limit with the ordered width-then-depth limit of the dense trained network, and a horizon-uniform approximation theorem.

That distinction is the organizing principle below.

### Evidence labels

Every substantive claim is classified as one of the following.

- **Exact finite system:** an algebraic identity before any width, depth, time-step, or truncation limit.
- **Proved limit:** a limit theorem with its stated hypotheses checked or explicitly imported.
- **Exact formal jet:** every separately fixed derivative coefficient is determined exactly, but no positive-time limiting curve is thereby constructed.
- **Conditional theorem:** the conclusion follows if named regularity, compactness, uniqueness, or identification hypotheses hold.
- **Empirical:** a numerical result under a finite discretization and a stated protocol.
- **Open:** a conjecture or proof obligation.
- **Disproved in scope:** an exact counterexample defeats the stated generalization, not necessarily the central canonical conjecture.

This language matters. In this project, an exact formula for every fixed Taylor coefficient, a convergent finite-source PDE hierarchy, and a correct finite-time limit of the original network are three different accomplishments.

---

## 1. The single research question behind the four top-level programs

Take a fully dense neural network trained in a feature-learning scaling. Width is large, depth may also be large, and every parameter block is trained. Tensor-program and mean-field methods can often describe any fixed computation or fixed collection of derivatives. Dynamical mean-field theory can often describe training using histories and two-time kernels. The project asks for something stronger and more operational:

> Can the trained network, on a fixed data set and compact training horizon, be approximated arbitrarily well by an autonomous causal PDE with only finitely many fields over a fixed finite-dimensional source space, with coefficients derived from the architecture and initialization rather than fitted to the realized trajectory?

"Finite" does not mean finitely many spatial grid points. It means that after choosing an accuracy, the continuum state has a fixed number of field types and a fixed finite-dimensional source coordinate; no width-sized matrices, ever-growing response trees, or full two-time histories survive. "Causal" means that the state at time \(t\) determines its future. "Autonomous" rules out an oracle that encodes the already-computed target trajectory in a forcing term. Three restart notions must not be conflated:

1. **Internal mathematical restart:** the *full declared PDE state* determines its own continuation, with no hidden clock or saved history. For a well-posed autonomous equation this is largely definitional; its substantive role here is only to enforce the anti-oracle contract.
2. **Numerical serialization restart:** saving that full discretized state, starting a fresh solver process, and reproducing the uninterrupted run. This checks the implementation for undeclared history, but not the dense-to-PDE identification.
3. **Dense-state restart:** map a physically reachable dense snapshot, or a declared quotient of it, into the finite PDE state and approximate every subsequent continuation. This is the scientifically strong restart theorem, and it is open.

The weak restart statements in this report refer to items 1--2, not to restart from output/Gram readouts alone and not to item 3.

There are three logically distinct reductions in the repository:

1. **Dense residual network to an operator PDE.** Replace the neuron index by an immutable Gaussian source label, project the trained dense operator onto finitely many Hermite coordinates, and evolve a conditional law by a Liouville PDE along continuous depth.
2. **Finite network derivatives to Gaussian normal forms.** At fixed depth, batch size, derivative order, and number of optimization steps, eliminate random matrices by exact Wick--Stein “peeling” and retain a finite computation graph of Gaussian expectations.
3. **A divergent formal jet to a rational non-Taylor dynamics.** In a special quadratic model, transform the exact output jet into a candidate Stieltjes moment sequence. If all Hankel inequalities and the global identification bridge hold, Gaussian/Radau quadrature yields nested rational kernels and scalar flows.

The other programs and substudies are stress tests of these reductions. Within `resnet_pde`, `dense_response` exposes the chronology and transpose-response structure but retains dense matrices, while `pde_convergence` tests whether the Hermite hierarchy actually converges and identifies the missing compactness estimates. `quadratic_nonclosure` proves that one prescribed positive Taylor/Wick closure fails and warns against confusing all-order formal coefficients with a positive-time dynamics.

The conceptual flow is therefore

\[
\boxed{
\text{exact dense mechanics}
\longrightarrow
\begin{cases}
\text{finite-source operator PDE},\\
\text{fixed-order peeled derivative DAG},
\end{cases}
\longrightarrow
\text{convergence/identification or non-Taylor resummation}.
}
\]

No arrow across the final gap is presently a theorem in the central dense residual setting.

---

## 2. Stable notation and the model boundary

Let \(n\) be hidden width, \(L\) or \(H\) the number of hidden layers, \(r,q\in\{1,\dots,m\}\) data indices, \(s\in[0,1]\) continuous depth, and \(t\ge0\) training time. Write

\[
Q^x_{rq}=x_r^\top x_q
\]

for the input Gram matrix after whatever fixed input normalization is part of the model. The activation is \(\phi\); the dated residual-network reports call it \(\sigma\). We use \(G^\ell_{rq}=n^{-1}\langle h_r^\ell,h_q^\ell\rangle\) for hidden Grams, \(P^\ell_{rq}=n^{-1}\langle p_r^\ell,p_q^\ell\rangle\) for adjoint Grams, \(f_r\) for outputs, \(e_r=f_r-y_r\) for residuals, and \(\mathcal L=\frac12\sum_r e_r^2\) unless a study explicitly uses average loss without the factor \(1/2\).

To prevent historically overloaded letters from blurring distinct objects, this synthesis uses \(k_{\rm resp}\) for dense-response grade, \(r_H\) for source-Hermite degree, \(\Theta^{\rm F}\) for the fixed-depth tangent kernel, \(\kappa_Q(y)\) for the quadratic output-coordinate kernel, and \(\mathscr R_Q(x)\) for its Stieltjes transform. Output jets are \(J_k=F^{(k)}(0)\), keeping them distinct from the residual network's readout scale \(A\). Symbols such as \(R_\omega\) that occur in numerical protocols remain sample counts, not Hermite orders or resolvents.

Three architecture families must not be silently merged.

### Family R: the canonical continuous-depth residual network

The central PDE program uses

\[
h_r^0=Ux_r,
\qquad
z_r^\ell=W_\ell h_r^\ell,
\qquad
h_r^{\ell+1}=h_r^\ell+\frac{\gamma}{L}\phi(z_r^\ell),
\qquad
f_r=\frac1n a^\top h_r^L.
\]

Initialization is

\[
U_{ij}\sim N(0,1),\qquad
a_i\sim N(0,A^2),\qquad
(W_\ell)_{ij}\sim N\!\left(0,\frac{\sigma_w^2}{n}\right),
\]

and the Euclidean-µP multipliers are

\[
\eta_U=n,\qquad \eta_a=n,\qquad \eta_{W_\ell}=L.
\]

The intended ordered limit is

\[
n\to\infty\quad\text{at each fixed }L,
\qquad\text{then}\qquad L\to\infty.
\]

This order is part of the conjecture. Interchanging it with a joint limit, a time limit, or a Hermite-cutoff limit would be a different theorem.

### Family F: fixed-depth fully connected µP networks

The peeling program typically uses raw iid Gaussian matrices and writes the effective matrices explicitly. For a three-hidden-layer example,

\[
z^1=\frac{W^1x}{\sqrt{d_0}},\qquad
z^2=\frac{W^2h^1}{\sqrt n},\qquad
z^3=\frac{W^3h^2}{\sqrt n},\qquad
f=\frac1n v^\top h^3,
\qquad h^\ell=\phi(z^\ell),
\]

with all raw entries iid \(N(0,1)\). For the average batch loss

\[
\mathcal J=\frac1m\sum_{r=1}^m(f_r-y_r)^2,
\]

all raw blocks are updated by

\[
\theta^+=\theta-n\eta\nabla_\theta\mathcal J.
\]

Equivalently, the effective learning rates for \(W^1/\sqrt{d_0},W^2/\sqrt n,W^3/\sqrt n,v/n\) are \(n\eta/d_0,\eta,\eta,\eta/n\). Here \(m,d_0,H\), the derivative order, and the number of optimizer steps are fixed before \(n\to\infty\).

Family F is a local, fixed-depth calculus. Family R is the continuous-depth target. The peeling results illuminate the response algebra needed by Family R, but they do not by themselves prove the \(L\to\infty\) homogenization or the PDE identification.

### Family Q: the quadratic theorem laboratory

The exact compiler and Stieltjes program use the one-sample two-hidden-layer specialization

\[
z_i=\frac1{\sqrt n}\sum_{j=1}^n W_{ij}u_j^2,
\qquad
f_n=\frac1n\sum_{i=1}^n a_i z_i^2,
\qquad
a_i,W_{ij},u_j\overset{\mathrm{iid}}{\sim}N(0,1),
\]

and the feature-ascent generator

\[
D_n=n\nabla f_n\cdot\nabla.
\]

Here the gradient is taken over all three trainable blocks \((a,W,u)\); it is not a readout-only or frozen-feature flow.

This unbounded polynomial model is deliberately chosen because Wick contraction becomes exact integer combinatorics. It is a theorem laboratory, not a benign approximation of the bounded-activation residual benchmark: its vector field can blow up, its Gaussian population flow is not automatically well posed for positive time, and several conclusions depend crucially on the square activation.

### The central standard-regime contract

The main residual-PDE conjecture assumes:

- a fixed finite data set and input dimension while width and then depth grow;
- fully dense, untied iid Gaussian layers, with every parameter block trained;
- residual increment \(\gamma/L\) and the stated Euclidean-µP metric;
- the fixed activation \(\tanh\) in the canonical claim;
- no normalization, low-rank factorization, frozen block, symmetry restriction, or trajectory-fitted basis;
- compact training horizons for the first theorem.

Uniformity is sought over the explicit compact neighborhood

\[
\mathcal U=
\left\{
(X,y,\sigma_w,A,\gamma):
\begin{array}{l}
\|X^\top X-I_3\|_{\mathrm{op}}\le0.05,\\
\|y-(0.8,-0.55,0.35)\|_2\le0.05,\\
|\sigma_w-0.65|\le0.05,\quad
|A-1|\le0.05,\quad
|\gamma-1|\le0.05
\end{array}
\right\}.
\]

The radius (0.05) is a declared first theorem laboratory, not a natural constant of the dynamics. It makes "one compiler works without fine-tuning" quantitatively falsifiable, keeps the input Gram uniformly near a nondegenerate point, and forces every existence, regularity, and stability constant to be controlled on more than one trajectory. No PDE derivation uses the numerical value (0.05), and the fourteen transfer experiments are not a uniform sampling or cover of this continuum set. A theorem could use another explicitly bounded nondegenerate compact class; it would then have to restate all uniform constants for that class.

Existence and uniqueness of the ordered trained target, well-posedness of each finite PDE, and regularity/uniqueness of an infinite-source operator flow are theorem obligations, not background assumptions. Broader smooth bounded activations are a proposed extension and have empirical examples, but are not part of this precise canonical claim.

Odd activation and symmetric initialization are additional assumptions for the parity reduction, not for the abstract finite-PDE construction. ReLU is outside the classical differentiable derivations unless a weak-derivative or Gaussian-boundary theory is supplied. Smooth-depth matrix fields, tied weights, RMS normalization, frozen layers, and shallow square networks are informative boundary models but cannot be used as proofs of the standard-regime claim.

---

## 3. Exact mechanics: what any valid closure must reproduce

For Family R, define the terminal adjoint \(p_r^L=a\), the gated adjoint \(\beta_r^\ell=\phi'(z_r^\ell)\odot p_r^{\ell+1}\), and propagate backward by

\[
p_r^\ell=\left(I+\frac\gamma L W_\ell^\top\operatorname{diag}\phi'(z_r^\ell)\right)p_r^{\ell+1}.
\]

With the Euclidean-µP metric, gradient flow gives the exact finite-network identities

\[
\dot W_\ell=-\frac\gamma n\sum_q e_q\,\beta_q^\ell(h_q^\ell)^\top,
\qquad
\dot a=-\sum_qe_qh_q^L,
\qquad
\dot U=-\sum_qe_qp_q^0x_q^\top.
\]

Differentiating the outputs yields

\[
\dot f_r=-\sum_q\Theta_{rq}e_q,
\]

where

\[
\Theta_{rq}
=G^L_{rq}
+Q^x_{rq}P^0_{rq}
+\frac{\gamma^2}{L}\sum_{\ell=0}^{L-1}G^\ell_{rq}G^{\beta,\ell}_{rq}.
\]

Each term is a parameter-gradient Gram. Hence \(\Theta\succeq0\) and

\[
\dot{\mathcal L}=-e^\top\Theta e\le0.
\]

These are **exact finite-system** statements. Any candidate PDE that changes these factors, loses the shared-transpose contribution, or fails to inherit positive semidefinite dissipation is describing another dynamics.

### Why current Grams are not an exact state

Integrating the middle-weight equation gives, schematically,

\[
W_\ell(t)h_r^\ell(t)
=W_\ell(0)h_r^\ell(t)
-\gamma\int_0^t\sum_qe_q(\tau)
\,\beta_q^\ell(\tau)
\,G^\ell_{qr}(\tau,t)\,d\tau,
\]

with the two-time overlap

\[
G^\ell_{qr}(\tau,t)
=\frac1n\langle h_q^\ell(\tau),h_r^\ell(t)\rangle.
\]

The transpose action has an analogous formula. Two networks can therefore have the same current hidden Grams but different cross-time overlaps and different future velocities. Worse, \(W_\ell h\) and \(W_\ell^\top\beta\) use the same matrix; treating them as independent Gaussian multiplications deletes the Stein/Onsager response created by this shared transpose.

This is the core nonclosure mechanism. It explains why:

- output plus current Gram matrices are not an exact dense restart state;
- a DMFT description naturally retains two-time kernels;
- a valid finite causal closure must either encode the relevant history in extra fields or prove that the reachable histories lie near a finite-dimensional manifold;
- empirical agreement of a low-order closure does not settle state sufficiency.

---

## 4. The dense-response precursor: exposing chronology without eliminating width

dense_response develops a chronological response expansion for the exact dense residual mechanics. Its scientific role is diagnostic: it shows which forward, reverse, and shared-transpose responses a successful closure must retain.

To see what the grades mean, differentiate one residual step in training time. With

\[
v_r^\ell=\partial_t h_r^\ell,\qquad
D_r^\ell=\operatorname{diag}\phi'(z_r^\ell),\qquad
A_r^\ell=\gamma D_r^\ell W_\ell,
\]

the exact forward velocity obeys

\[
v_r^{\ell+1}
=\left(I+\frac1L A_r^\ell\right)v_r^\ell
+\frac1L F_r^\ell,
\]

where \(F_r^\ell\) collects the direct parameter-training source. The transpose transport uses

\[
(A_r^\ell)^\top=\gamma W_\ell^\top D_r^\ell.
\]

Expanding the ordered product in variation of constants produces words

\[
A_r^{j_k}\cdots A_r^{j_1},
\qquad 0\le j_1<\cdots<j_k<\ell.
\]

Their word length \(k\), equivalently the number of chronologically ordered layer responses, is the **response grade**. One implementation writes

\[
q_{r\leftarrow q}^{0,\ell+1}
=q_{r\leftarrow q}^{0,\ell}+L^{-1}F_{r\leftarrow q}^\ell,
\qquad
q_{r\leftarrow q}^{k,\ell+1}
=q_{r\leftarrow q}^{k,\ell}+L^{-1}A_r^\ell q_{r\leftarrow q}^{k-1,\ell},
\]

with the reverse-depth analogue

\[
r_{r\leftarrow q}^{k,\ell}
=r_{r\leftarrow q}^{k,\ell+1}
+L^{-1}(A_r^\ell)^\top r_{r\leftarrow q}^{k-1,\ell+1}.
\]

Thus this is a Duhamel/ordered-word expansion in **depth**, not a Taylor expansion in training time. At finite \(L\), grades through \(L\) recover the derivative algebra because an increasing word cannot visit more than \(L\) layer sites.

If the local operators and sources are bounded over a compact training horizon \([0,T]\), depth chronology gives a factorial remainder. For example,

\[
\left\|v-
\sum_{k=0}^{k_{\rm resp}}\bar q^{(k)}\right\|
\le B_{v,T}\,\mathfrak R_{k_{\rm resp}}(\Lambda_T),
\qquad
\mathfrak R_{k_{\rm resp}}(\Lambda_T)
\le e^{\Lambda_T}
\frac{\Lambda_T^{k_{\rm resp}+1}}{(k_{\rm resp}+1)!},
\]

with an analogous reverse-field bound and

\[
\Lambda_T
=\sup_{\substack{r\\0\le t\le T}}
\frac1L\sum_{\ell=0}^{L-1}
\|A_r^\ell(t)\|_{\rm op}.
\]

Thus truncating the response order can be accurate even over a relatively long training horizon when \(B_{v,T}\), its reverse analogue, and \(\Lambda_T\) remain controlled. This is a useful mechanism: ordered depth chronology, rather than an arbitrary polynomial fit, supplies the small tail. But \(\Lambda_T\) is a **pathwise trained-network quantity**, not currently an a priori constant. The early value near \(1.981\) was measured after the trajectory was generated. A width/depth-uniform theorem would have to prove the required bounds uniformly in \((n,L)\), with the declared probability and parameter uniformity. The bound itself is not uniform in training horizon; long-time accuracy in the reports is empirical.

But the construction retains every dense \(W_\ell\). The response order may be finite while the state dimension still scales like \(n^2L\). Moreover, the factorial tail for a forced linearized hierarchy does not control the error made when truncated responses are substituted back through the nonlinear trained source. The missing estimate is a coupled stability bound, not merely a tail bound.

Nor is the implemented long-horizon hierarchy an orthogonal Galerkin projection in neuron space. It keeps the full \(n\)-vectors and every \(W_\ell\), and deletes chronological words above \(k_{\rm resp}\). The forward and reverse families are stored separately but share the same matrices, fields, adjoints, and residuals; they are not probabilistically independent. Two genuine basis projections appear elsewhere and should not be conflated with this truncation: the early audit fits a scalar response surface on the triangle \(0\le u\le s\le1\) to total-degree Legendre products as a snapshot diagnostic, while the proposed but unimplemented width-free response compiler uses shifted-Legendre depth coefficients with forward/backward boundary lifts.

There are two historical variants and they should not be plotted on one convergence ladder.

- The **early audit** uses \(h^0=\tanh(Ux)\), different initialization variances, and a truncated depth-adjoint product inside parameter flow. It is an exploratory truncated-adjoint model with a separate response-surface diagnostic, not the later canonical dense network.
- The **long-horizon program** switches to the canonical linear input lift \(h^0=Ux\), \(\sigma_w=0.65\), and a coupled forward/reverse training-response hierarchy. It is closer to Family R but still a finite-matrix surrogate.

### 4.1 Early depth-adjoint audit

The implemented early model is

\[
h_r^0=\phi_g(Ux_r),\qquad
h_r^{\ell+1}=h_r^\ell+\frac1L\phi_g(W_\ell h_r^\ell),
\qquad
\phi_g(z)=\frac{\tanh(gz)}g,
\]

with \(U_{ij}\sim N(0,1/d_0)\), \(W_{\ell,ij}\sim N(0,1/n)\), and \(a_i\sim N(0,1)\). It compares iid layers with a smooth Fourier Gaussian matrix field and a coherent nonnormal rank-one stress. The approximation expands only the discrete depth adjoint

\[
Q_\ell=Q_{\ell+1}+\frac1L W_\ell^\top(D_\ell Q_{\ell+1})
\]

into chronological depth grades \(0,\ldots,M\), then uses the truncated \(Q\) inside parameter flow.

The four primary trajectories used

\[
n=24,\quad L=40,\quad d_0=6,\quad m=3,\quad
T=1.6,
\]

Heun step \(0.025\), saved step \(0.05\), and smooth/iid/nonnormal/aligned-input cases. A broader sweep covered \(n=16,24,32\), \(L=16,\ldots,64\), \(m=2,3,4\), activation gains \(0.7\)–\(1.4\), and comparable label scales.

At \(M=4\), primary output/Gram sup errors ranged from

\[
1.86\times10^{-7}/3.01\times10^{-7}
\]

in the iid generic case to

\[
2.97\times10^{-5}/3.92\times10^{-4}
\]

in the nonnormal case. Across twelve order-four sweep runs, worst output/Gram errors were \(3.38\times10^{-4}\) and \(8.70\times10^{-4}\), despite order-one Gram motion. Positive-time restart also remained near \(10^{-5}\).

The proved nonnormal-safe factorial bound was much looser than the observations. More importantly, the truncated flow is driven by a cross-kernel \(SS_M^\top\), not by the separately reconstructed PSD matrix \(S_MS_M^\top\). Here is the exact distinction. Let \(J=D_\theta f\) be the output Jacobian of the unchanged dense forward network and

\[
\mathsf M=\operatorname{diag}
\bigl(nI_a,nI_U,LI_{W_0},\ldots,LI_{W_{L-1}}\bigr)
\]

be the µP parameter metric. Define

\[
S=J\mathsf M^{1/2},\qquad
S_M=J_M\mathsf M^{1/2},
\]

where \(J_M\) is the sensitivity assembled with the grade-\(M\) adjoint. For the early nonlinear input lift put \(\chi_r=\phi_g'(Ux_r)\odot p_r^0\). Its exact sample rows have the metric-weighted parameter blocks

\[
S_r^{(a)}=\frac{h_r^L}{\sqrt n},\qquad
S_r^{(U)}=\frac{\chi_rx_r^\top}{\sqrt n},\qquad
S_r^{(W_\ell)}=\frac{\beta_r^\ell(h_r^\ell)^\top}{n\sqrt L},
\]

and \(S_M\) replaces the exact adjoint-dependent factors by their grade-\(M\) versions. The diagnostic evolves parameters with the approximate cotangent,

\[
\dot\theta_M=-\mathsf M J_M^\top e,
\]

but evaluates them through the exact forward map \(J\). Therefore

\[
\dot f=J\dot\theta_M=-J\mathsf M J_M^\top e=-SS_M^\top e.
\]

By contrast,

\[
S_MS_M^\top=J_M\mathsf M J_M^\top\succeq0
\]

would govern a reduced dynamics only if \(J_M\) were the exact Jacobian of the same reduced forward map being evolved. The cross-kernel need be neither symmetric nor positive semidefinite, so this approximate trajectory is not proved to be gradient flow. No width limit, iid-depth homogenization, law compression, or all-time stability theorem was tested.

### 4.2 Coupled long-horizon response

The later hierarchy evolves separately stored, grade-truncated forward and adjoint response fields while retaining the exact dense \(W_\ell\). Grade zero contains the direct training source; grades \(k\ge1\) propagate it chronologically through \(D_\ell W_\ell\) or \(W_\ell^\top D_\ell\). The backward source recomputes \(\dot D\) from the truncated forward velocity. At \(k_{\rm resp}=L\), the hierarchy reproduces the exact finite-network time derivative algebraically.

The main protocol used

\[
k_{\rm resp}=0,1,2,3,\quad n=64,\quad L=16,\quad
6\ \text{seeds},\quad
\Delta t=0.02
\]

with RK4, saved step \(0.04\), and horizon doublings \(4,8,16,32\). Width controls used \(n=32,96\), depth controls \(L=8,32\), and additional cases stressed \(\sigma_w=1.2\), nearby data/labels, and restarts at \(t=1\).

Across sixteen primary trajectories, recorded-grid median/max errors were

\[
\begin{array}{c|cc}
k_{\rm resp}&\text{output}&\text{all-depth Gram}\\ \hline
0&8.51\times10^{-3}/1.579\times10^{-2}&
2.501\times10^{-2}/5.189\times10^{-2}\\
1&2.378\times10^{-4}/1.397\times10^{-3}&
1.875\times10^{-3}/3.616\times10^{-3}\\
2&1.418\times10^{-5}/5.711\times10^{-5}&
1.183\times10^{-4}/5.517\times10^{-4}\\
3&9.768\times10^{-7}/6.250\times10^{-6}&
6.083\times10^{-6}/5.925\times10^{-5}.
\end{array}
\]

Median exact feature motion was \(0.6299\). Every exact and grade-truncated trajectory passed the operational plateau gate through \(T=32\), and time-step refinement was below the response-truncation error. Here “plateau” has a specific audit definition. For each candidate horizon \(H\in\{4,8,16,32\}\), set

\[
S_f^{\rm plat}=\max\{1,\|y\|_2,\|f(0)\|_2\},
\qquad
S_G^{\rm plat}=\max\{1,\max_\ell\|G^\ell(0)\|_F\},
\]

and set

\[
M_f^{\rm plat}=\max_{t\le H}\|f(t)-f(0)\|_2,
\qquad
M_G^{\rm plat}=\max_{\substack{t\le H\\\ell}}
\|G^\ell(t)-G^\ell(0)\|_F.
\]

All stored samples on \([H/2,H]\) must have residual below \(10^{-5}S_f^{\rm plat}\); output and every depth Gram must stay within

\[
\delta_f=10^{-6}S_f^{\rm plat}+10^{-4}M_f^{\rm plat},
\qquad
\delta_G=10^{-6}S_G^{\rm plat}+10^{-4}M_G^{\rm plat}
\]

of their terminal values; sampled output/Gram speeds must be below the same \(\delta\)'s; and trapezoidal tail arclengths must be below \(2\delta\). A candidate is validated only if every later available doubling through 32 also passes and its inter-doubling drift stays inside the earlier tolerance. This is substantially more informative than checking one endpoint, but it remains an operational finite-window certificate. At a \(10^{-5}\) prediction tolerance, only thirteen of sixteen runs were resolved by \(k_{\rm resp}\le3\).

The theory controls the pure ordered-propagator tail. For the coupled adjoint it leaves an additional source-replacement defect. Let \(w_r^\ell=\partial_t p_r^\ell\) denote the exact adjoint velocity. Its exact reverse source is

\[
S_r^\ell=(\dot A_r^\ell)^\top p_r^{\ell+1},
\]

whereas the coupled truncation computes \(\dot A_{r,k_{\rm resp}}^\ell\) using \(v_{r,k_{\rm resp}}\). Formally,

\[
E_{A,k_{\rm resp},T}
=\sup_{\substack{t\le T\\r}}
\frac1L\sum_\ell
\left\|
(\dot A_r^\ell-\dot A_{r,k_{\rm resp}}^\ell)^\top
p_r^{\ell+1}
\right\|_n,
\]

and variation of constants gives the conditional bound

\[
\sup_{t,r,\ell}
\|w_r^\ell-w_{r,k_{\rm resp},{\rm coup}}^\ell\|_n
\le B_{w,T}\mathfrak R_{k_{\rm resp}}(\Lambda_T)
+e^{\Lambda_T}E_{A,k_{\rm resp},T}.
\]

Expanding

\[
\dot A_r^\ell
=\gamma\bigl(\dot D_r^\ell W_\ell+D_r^\ell\dot W_\ell\bigr),
\qquad
\dot D_r^\ell
=\operatorname{diag}\!\left(
\phi''(z_r^\ell)\odot
[\dot W_\ell h_r^\ell+W_\ell v_r^\ell]
\right)
\]

shows why the factorial word tail is insufficient: replacing \(v_r^\ell\) creates nonlinear multiplier terms such as

\[
\gamma W_\ell^\top
\left[p_r^{\ell+1}\odot\phi''(z_r^\ell)
\odot W_\ell(v_r^\ell-v_{r,k_{\rm resp}}^\ell)\right].
\]

Controlling those terms needs operator and coordinate bounds plus a coupled stability argument; the reports do not prove \(E_{A,k_{\rm resp},T}\to0\), nor do they bound two fully evolved nonlinear trajectories merely from the forced linear tail. Also, a plateau pass merely says a surrogate settles; even \(k_{\rm resp}=0\) settled. It is not an accuracy or \(\sup_{t\ge0}\) certificate.

The later operator-PDE work explicitly retires an even more compressed \(K/J/N\) description as non-executable: several tags, history variables, Gaussian kernels, and drift maps needed to run it were never emitted. What survives is its causal accounting and response-tail intuition, not a width-independent solver.

**Claim level:** exact response identities plus conditional factorial bounds, with empirical finite-matrix performance; no finite causal PDE theorem and no elimination of microscopic matrices.

---

## 5. The explicit operator--Hermite PDE

The central constructive advance is to replace a neuron coordinate by an immutable Gaussian source label. Let

\[
\xi=(b_0,\alpha_0)\sim\mu=N(0,I_{d_0+1})
\]

store a row of the initialized input map together with its initialized readout. Let \(\{\psi_\nu\}\) be multivariate Hermite polynomials in \(\xi\). At total-degree cutoff \(r_H\), the number of retained source modes is

\[
P_{r_H}=\binom{d_0+1+r_H}{r_H}.
\]

The continuum hidden field is \(h_r(s,t,\xi)\), while the adjoint can be queried at an independently named source point \(p_r(s,t,\eta)\). The trained depth operator is represented, at every \((s,t,\xi)\), by a conditional law \(\rho_{s,t}^{\xi}(dw)\) over the finite coefficient vector \(w=(w_\nu)_{|\nu|\le r_H}\). Define Hermite coefficients

\[
H_{\nu r}(s,t)=\int\psi_\nu(\xi)h_r(s,t,\xi)\,\mu(d\xi)
\]

and the projected preactivation and gated adjoint

\[
z_r(w)=\sum_\nu w_\nu H_{\nu r},
\qquad
\beta_r(s,t,\xi,w)=\phi'(z_r(w))p_r(s,t,\xi).
\]

The coefficient-particle velocity is

\[
V_\nu(w;s,t,\xi)
=-\gamma\sum_qe_q(t)\,\beta_q(s,t,\xi,w)H_{\nu q}(s,t),
\]

and the law evolves by the finite-dimensional Liouville equation

\[
\partial_t\rho_{s,t}^{\xi}
+\nabla_w\!\cdot\bigl(\rho_{s,t}^{\xi}V\bigr)=0.
\]

Its compiled initialization is

\[
b(\xi,0)=b_0,\qquad
a(\xi,0)=A\alpha_0,\qquad
\rho_{s,0}^{\xi}=N(0,\sigma_w^2I_{P_{r_H}}),
\]

with the coefficient law initially independent of \(\xi\). In characteristics one writes \(w=\sigma_w\varepsilon+c\), \(\varepsilon\sim N(0,I_{P_{r_H}})\), and starts from \(c=0\).

Continuous depth is coupled by

\[
\partial_s h_r(s,t,\xi)
=\gamma\int\phi(z_r(w))\,\rho_{s,t}^{\xi}(dw),
\qquad
h_r(0,t,\xi)=b(t,\xi)\cdot x_r,
\]

and the reverse field solves

\[
-\partial_s p_r(s,t,\eta)
=\gamma\sum_\nu\psi_\nu(\eta)
\int\mu(d\xi)\int
w_\nu\beta_r(s,t,\xi,w)\,\rho_{s,t}^{\xi}(dw),
\qquad
p_r(1,t,\eta)=a(t,\eta).
\]

The input and readout source functions train by the continuum analogues of the exact finite-network gradients,

\[
\partial_tb(t,\xi)=-\sum_qe_qp_q(0,t,\xi)x_q,
\qquad
\partial_ta(t,\xi)=-\sum_qe_qh_q(1,t,\xi),
\]

with the output and retained-PDE Gram readout

\[
f_r(t)=\int a(t,\xi)h_r(1,t,\xi)\,d\mu(\xi),
\qquad
G^{(r_H)}_{rq}(s,t)
=\int h_r(s,t,\xi)h_q(s,t,\xi)\,d\mu(\xi).
\]

The exact placement of \(\xi\) and the conditional law is important: it keeps the initialization coupling that a simple unconditional weight distribution would erase. The same coefficient vector is used in forward and transpose actions, so the construction retains the shared-adjoint geometry rather than drawing an independent reverse operator. The next derivation says precisely what finite-network objects motivate these choices—and exactly where motivation stops short of identification.

### 5.1 The finite-row dictionary and the conjectural law

At finite width, attach to neuron \(i\) its immutable initialization label

\[
\xi_i=\bigl(U_{i\cdot}(0),a_i(0)/A\bigr),
\qquad \xi_i\overset{\rm iid}\sim\mu.
\]

For the source-design matrix \(\Phi_{i\nu}=\psi_\nu(\xi_i)\), define the row coefficients of one middle layer by

\[
C_{i\nu}^\ell=\sum_{j=1}^n(W_\ell)_{ij}\psi_\nu(\xi_j),
\qquad
H_{\nu r}^{n,\ell}=\frac1n\sum_{j=1}^n
\psi_\nu(\xi_j)h_{r,j}^\ell.
\]

The maintained projected operator is

\[
W_{\ell,r_H}=\frac1n(W_\ell\Phi)\Phi^\top,
\qquad
(W_{\ell,r_H}h_r)_i
=\sum_{|\nu|\le r_H}C_{i\nu}^\ell H_{\nu r}^{n,\ell}.
\]

There is a finite-sample qualification. With raw randomly evaluated Hermites,

\[
Q_n=\frac1n\Phi^\top\Phi
\]

is only asymptotically the identity. The exact empirical orthogonal projector is

\[
W_\ell\Phi(\Phi^\top\Phi)^{-1}\Phi^\top
=\frac1nW_\ell\Phi Q_n^{-1}\Phi^\top.
\]

Therefore the simpler displayed projector is exact after empirical basis whitening \(Q_n=I\), as in the PDE quadrature, and otherwise is an asymptotic projection under \(Q_n\to I\). Calling it an exact raw-sample finite-\(n\) projection would be too strong.

Multiplying the exact middle-weight update by \(\Phi\) gives, in the whitened/projected system,

\[
\dot C_{i\nu}^\ell
=-\gamma\sum_qe_q\,\beta_{q,i}^\ell
H_{\nu q}^{n,\ell}.
\]

This formula answers why a law that is initially independent of \(\xi_i\) becomes conditional on it. At \(t=0\), \(W_\ell\) is independent of \((U,a)\), but the row velocity contains \(\beta_{q,i}^\ell\). The latter inherits \(i\)'s label through the forward input row and, most directly, through the terminal condition \(p_{q,i}^L=a_i\). Training therefore correlates the projected middle-weight row with its row label immediately.

The proposed continuum object is the weak limit, at \(\ell/L\to s\), of the empirical joint measure

\[
\nu_{s,t}^{n,L}
=\frac1n\sum_{i=1}^n
\delta_{(\xi_i,C_i^\ell(t))}
\Longrightarrow
\mu(d\xi)\rho_{s,t}^\xi(dw).
\]

This disintegration is the intended answer to “what does \(\rho^\xi\) represent?” It is **not** a proved limit theorem. Replacing the exact dense actions by the projected ones, proving joint empirical convergence in the presence of shared transposes, and then homogenizing trained layers are precisely parts of the dense-identification bridge.

### 5.2 Why one-index parameters are fields and a two-index matrix is an operator law

The distinction is one of index arity, not a theorem that some randomness is “fresh” and other randomness “reused.” Both \(U_i\) and \(a_i\) carry one neuron index. Once that neuron's immutable label is \(\xi_i\), their trained values naturally become source functions \(b(t,\xi)\) and \(a(t,\xi)\). By contrast, \(W_{ij}\) couples a row label \(\xi_i\) to a whole column-indexed query. At finite cutoff the latter query is compressed to the coefficients of the map

\[
u(\cdot)\longmapsto
\sum_{|\nu|\le r_H}w_\nu\langle\psi_\nu,u\rangle_{L^2(\mu)}.
\]

The row label remains explicit, while its action on the column/source variable is represented by \(w\). This is the minimal finite-rank operator analogue of a two-index matrix.

That construction also contains a substantive homogenization assumption. The PDE keeps a depth-local marginal law \(\rho_{s,t}^\xi\); it does not attach one persistent Gaussian identity to a row through all independently initialized layers. It assumes that, after ordered width and depth limits, the slow fields are functions of \(\xi\) and every surviving local operator fluctuation is captured by the conditional row law. A persistent cross-depth latent variable or two-time response not determined by this state would invalidate the closure. The current evidence does not prove its absence.

### 5.3 The transpose formula is the exact projected adjoint

Let

\[
\mathcal H=L^2(\mu),\qquad
\mathcal R=L^2\bigl(\mu(d\xi)\rho_s^\xi(dw)\bigr),
\]

and define the finite-rank row operator

\[
(\mathcal W_{r_H}v)(\xi,w)
=\sum_{|\nu|\le r_H}w_\nu
\int\psi_\nu(\eta)v(\eta)\,\mu(d\eta).
\]

For \(q\in\mathcal R\), Fubini's theorem gives

\[
\begin{aligned}
\langle q,\mathcal W_{r_H}v\rangle_{\mathcal R}
&=\int\mu(d\eta)\,v(\eta)
\sum_\nu\psi_\nu(\eta)
\int\mu(d\xi)\int w_\nu q(\xi,w)\rho_s^\xi(dw).
\end{aligned}
\]

Hence

\[
(\mathcal W_{r_H}^*q)(\eta)
=\sum_\nu\psi_\nu(\eta)
\int\mu(d\xi)\int w_\nu q(\xi,w)\rho_s^\xi(dw),
\]

which is exactly the term in the reverse-depth equation with \(q=\beta_r\). The two source letters are not two independent physical draws: \(\xi\) is the integrated **row** index, corresponding to \(i\) in \((W^\top\beta)_j=\sum_iW_{ij}\beta_i\), and \(\eta\) is the free **column** source corresponding to \(j\). This is the projected row/column asymmetry of the shared transpose.

### 5.4 Initialization, row-noise quadrature, and characteristics

Conditioned on the source cloud,

\[
\operatorname{Cov}(C_{i\nu}^\ell,C_{i\kappa}^\ell\mid\xi_1,\ldots,\xi_n)
=\sigma_w^2(Q_n)_{\nu\kappa}.
\]

Hermite orthonormality gives \(Q_n\to I\), and empirical whitening makes the covariance exactly \(\sigma_w^2I\) in the numerical coordinates. Independence of \(W_\ell(0)\) from \((U,a)\) makes this initial law independent of \(\xi\); the exceptional self-column correlation is lower order in \(n\). Thus

\[
\rho_{s,0}^\xi=N(0,\sigma_w^2I)
\]

is the compiled initialization. Whitening is a finite-cubature correction, not an extra probabilistic assumption required in the ideal Gaussian integral.

The symbol \(R_\omega\) in the solver is often misread. It is the number of quadrature particles \(\varepsilon_r\in\mathbb R^{P_{r_H}}\) for the **retained cylindrical Gaussian law**

\[
\mathcal W_{r_H}^0u
=\sigma_w\sum_{|\nu|\le r_H}
\varepsilon_\nu\langle\psi_\nu,u\rangle.
\]

It does not sample a frozen residual \((I-\Pi_{r_H})\) tail. The infinite isonormal map is useful in the functional analysis of the proposed \(r_H\to\infty\) limit, but the finite solver contains only \(\Pi_{r_H}\); all unretained coordinates are omitted. The same \(\varepsilon_r\) is used across the data queries of one characteristic so that their covariance is correct. Reusing the quadrature table at different depth cells is numerical integration, not a claim that one physical noise path persists across iid layers.

Nor does \(w=\sigma_w\varepsilon+c\) mean that \(\rho\) remains one common Gaussian translate. For each depth cell \(s_\ell\), source point \(\xi_i\), and row-noise particle \(\varepsilon_r\), the code stores

\[
c_{\ell i r\nu}(t),
\]

an array of shape \(N_s\times M_\xi\times R_\omega\times P_{r_H}\), together with the source fields \(b_i(t),a_i(t)\). Each particle follows

\[
\dot c_{\ell i r\nu}
=V_\nu(\sigma_w\varepsilon_r+c_{\ell i r};s_\ell,t,\xi_i).
\]

Because \(V\) contains \(\phi'(z(w))\), it is nonlinear in \(w\); different particles acquire different shifts and the pushforward law is generally non-Gaussian. RK4 evolves these individual characteristics. The Liouville equation is the continuum statement of that particle pushforward, not a Gaussian closure ansatz.

### 5.5 What is exact inside this PDE

For every finite \(r_H\), assuming a regular solution exists, define

\[
\begin{aligned}
G^h_{qk}(s)&=\int h_q(s,\xi)h_k(s,\xi)\,\mu(d\xi),\\
G^p_{qk}(s)&=\int p_q(s,\xi)p_k(s,\xi)\,\mu(d\xi),\\
G^\beta_{qk}(s)&=\int\mu(d\xi)\int
\beta_q(s,\xi,w)\beta_k(s,\xi,w)\,\rho_s^\xi(dw),
\end{aligned}
\]

with training time suppressed, and define only the hidden factor in the trained-operator term by

\[
G^{h,r_H}_{qk}(s)
=\sum_{|\nu|\le r_H}H_{\nu q}(s)H_{\nu k}(s).
\]

The exact same-system tangent kernel is

\[
(\Theta_{r_H})_{qk}
=G^h_{qk}(1)
+(x_q\cdot x_k)G^p_{qk}(0)
+\gamma^2\int_0^1
G^{h,r_H}_{qk}(s)G^\beta_{qk}(s)\,ds.
\]

The first two terms are the readout and input-map blocks; the integral is the trained depth-operator block. Crucially, it contains the **projected** hidden Gram \(G^{h,r_H}\), not the full hidden Gram. Each displayed matrix is a Gram matrix, and the input and operator products are positive semidefinite by the Schur product theorem. Hence \(\Theta_{r_H}\succeq0\).

The asymmetry between \(G^{h,r_H}\) and \(G^\beta\) follows directly from the chosen trainable coordinates. For a coefficient characteristic,

\[
\frac{\delta f_r}{\delta c_\nu(s,\xi,w)}
=\gamma\,\beta_r(s,\xi,w)H_{\nu r}(s).
\]

Taking the parameter-gradient inner product between samples \(r,q\) and summing over the retained coordinate label \(\nu\) gives

\[
\begin{aligned}
\Theta_{rq}^{W,r_H}
&=\gamma^2\int_0^1
\sum_{|\nu|\le r_H}H_{\nu r}(s)H_{\nu q}(s)\\
&\hspace{3.5em}\times
\int\mu(d\xi)\int
\beta_r(s,\xi,w)\beta_q(s,\xi,w)\rho_s^\xi(dw)\,ds\\
&=\gamma^2\int_0^1G_{rq}^{h,r_H}(s)G_{rq}^\beta(s)\,ds.
\end{aligned}
\]

The hidden factor is projected because \(\nu\) indexes the finite set of **trainable coefficient directions**. The row factor is integrated over every characteristic already present in the finite law, so its Gram is unprojected within that system. Projecting \(\beta\) again would change the parameter metric and define a different model; using the full hidden Gram would add directions that the cutoff does not train. “Full” here means full over the finite characteristic law, not full dense-network or infinite-Hermite information. Consequently:

1. the Liouville velocity is the projected gradient velocity;
2. the depth forward and adjoint equations are exact adjoints within the projected Hilbert space;
3. the induced tangent kernel is positive semidefinite;
4. the PDE loss obeys the exact dissipation identity \(\dot{\mathcal L}_{r_H}=-e^\top\Theta_{r_H}e\le0\);
5. the system is autonomous in its own state and uses no dense matrix or past-time history.

These are **exact finite-PDE** statements. They do not prove that the PDE equals the dense-network limit. They also presume enough regularity and well-posedness to justify the integrations by parts and differentiations; global well-posedness of the nonlinear coupled PDE has not been established.

### 5.6 Parity and the real cutoff ladder

For odd \(\phi\) and the symmetric Gaussian source law, the forward/adjoint source fields are odd. Hence their even-degree query coefficients and the corresponding learned coefficient velocities vanish. The frozen isonormal row-noise coordinates at even degree are still nonzero random variables, but they multiply zero query coefficients and remain dynamically inert. In the canonical \(d_0=3\) source dimension \(d_0+1=4\), the meaningful total-degree ladder is

\[
r_H=1,3,5,7,
\qquad
P_{r_H}=5,35,126,330,
\]

with active odd-mode counts \(4,24,80,200\). The earlier apparent \(P=5\to15\to35\) comparison mixed an inert even shell with cubature parity leakage; it is superseded.

---
## 6. What the operator-PDE experiments actually establish

### 6.1 Canonical benchmark

The main synthetic task is deliberately small enough to audit:

\[
m=d_0=3,\qquad X=I_3,\qquad y=(0.8,-0.55,0.35),
\]
\[
\phi=\tanh,\qquad \sigma_w=0.65,\qquad A=\gamma=1.
\]

The primary PDE run used

\[
P=5,\quad N_s=16,\quad M_\xi=256,\quad R_\omega=128,\quad
\Delta t=0.02,\quad T=8,
\]

with scrambled Sobol sampling, moment correction, RK4, and an authenticated restart to \(T=32\). Here \(N_s\) is the depth grid, \(M_\xi\) the immutable-source quadrature size, and \(R_\omega\) the retained Gaussian coefficient-law quadrature count. None is a hidden width, and \(R_\omega\) is not an unretained-tail sample count. The primary dense reference used

\[
n=256,\qquad L=32,\qquad 128\ \text{network seeds}
\]

on the same saved time grid.

Against that finite reference:

- PDE and dense hidden-Gram motions were \(0.6338\) and \(0.6399\), so the experiment is strongly nonlazy.
- The maximum output gap was \(1.0753\times10^{-2}\), much of it initialization ensemble noise.
- The initialization-cancelled Gram-increment gap was \(7.2433\times10^{-3}\), or \(1.143\%\) of PDE feature motion.
- The loss-of-mean-predictor gap was \(1.8457\times10^{-3}\).
- The Gram-increment mismatch was statistically resolved against the finite ensemble; most other gaps were not.

“Resolved” has a narrow bootstrap meaning here. With \(\bar G_{\rm dense}\) the mean of 128 network runs, the diagnostic was

\[
D_G^{\rm inc}
=\max_{t\le8,\,s}
\left\|
[G_{\rm PDE}(s,t)-G_{\rm PDE}(s,0)]
-[\bar G_{\rm dense}(s,t)-\bar G_{\rm dense}(s,0)]
\right\|_F.
\]

The dense seeds were retained in blocks of \(32,32,64\), and both pooled and block-stratified whole-trajectory bootstraps were used. The observed \(D_G^{\rm inc}=0.00724334\) exceeded their 95% dense-sampling thresholds \(0.00501674\) and \(0.00494006\). By contrast, the output gap \(0.010753\) lay below its corresponding thresholds \(0.015347\) and \(0.015683\). Initialization cancellation makes the Gram-increment comparison unusually sensitive. The PDE curve was treated as fixed: QMC scramble error, finite cutoff, depth discretization, and cubature bias were not included in these thresholds. This is therefore a statistically detected mismatch relative to dense Monte Carlo noise, not a total-error confidence statement for the limiting PDE.

The PDE discretization itself was substantially more accurate than the model-to-reference gap. RK4 step halving changed output/Gram by roughly \(7\times10^{-8}\) and \(1.1\times10^{-7}\); depth-grid \(16\to32\) changes were \(2.1\times10^{-4}\) and \(8.5\times10^{-4}\); QMC scramble spreads were \(1.3\times10^{-3}\) and \(2.1\times10^{-3}\). Coordinate-gradient, transpose, energy, kernel, and restart checks were near floating-point precision. The canonical hard plateau gate was

\[
\max_{8\le t\le32}\|f(t)-f(8)\|_2<10^{-10},
\qquad
\max_{8\le t\le32,s}\|G(s,t)-G(s,8)\|_F<10^{-10};
\]

the observed drifts were about \(5.0\times10^{-13}\) and \(4.24\times10^{-13}\). This is a finite-grid settling test for the PDE, not a \(\sup_{t\ge0}\) theorem, and the dense comparison itself stopped at \(T=8\).

These facts support **a useful finite-\(P\) surrogate**. They do not identify the dense ordered limit: the available dense grid is essentially L-shaped, and the observed \(n=256\to512\) and \(L=32\to64\) Cauchy gaps are not statistically resolved.

### 6.2 Transfer without retuning

The generalization study fixed the complete degree-one basis

\[
\{1,u_1,u_2,u_3,a_0/A\},\qquad P=5,
\]

and used \(N_s=16,M_\xi=81,R_\omega=128,\Delta t=0.02,T=32\). Fourteen preregistered configurations changed label direction and scale, input correlations, batch size \(m=2,4,5\), activation (\(\tanh\), normalized erf, atan), and interactions among these choices. Dense screening used \(n=128,L=32,32\) seeds; eight held-out cases used \(n=256,L=32,24\) seeds.

Across all cases, median/max normalized full-curve errors were

\[
\begin{array}{c|cc}
\text{observable}&\text{median}&\text{maximum}\\ \hline
\text{Gram increment}&1.71\%&4.14\%\\
\text{output increment}&1.46\%&1.83\%\\
\text{loss}&0.63\%&1.97\%.
\end{array}
\]

The PDE/dense feature-motion ratio stayed between \(0.977\) and \(1.023\). This is meaningful anti-fine-tuning evidence. Formally, however, the frozen outcome was “boundary or unresolved.” The preregistered equivalence statistic was not a collection of independent TOST tests. For case \(c\) and channel \(k\in\{G,f,\mathcal L\}\), let \(\widehat E_{ck}\) be the normalized full-curve discrepancy. Each whole-trajectory bootstrap formed

\[
Z_b^+=\max_{c,k}
\bigl(\widehat E_{ck}^{*(b)}-\widehat E_{ck}\bigr),
\]

using the same resampled indices within a tier to retain cross-channel dependence. Its 95th percentile was \(0.0594006\), so a simultaneous familywise upper bound is \(\widehat E_{ck}+0.0594006\). The **5.94% is an uncertainty increment, not an observed model error**; since it alone exceeds the desired 5% margin, the strong equivalence gate could not pass.

The transfer plateau protocol also differed from the canonical hard gate. It tested both windows \([8,16]\) and \([16,32]\), for PDE and dense summaries, using endpoint output and Gram drifts below \(10^{-4}\), output and Gram path lengths below \(2\times10^{-4}\), \(\sup\|-\Theta e\|<10^{-5}\), normalized loss drift below \(10^{-6}\), and a memberwise dense 95th-percentile endpoint drift below \(10^{-3}\). Only ten of fourteen cases passed both windows; one passed only the later window, and three remained active at \(T=32\). Six configurations also failed a numerical-resolution gate. Thus “all transfer trajectories plateaued” would be false. The cases are fourteen fixed synthetic tasks, not a statistical population of learning problems.

### 6.3 Is the success merely linear?

The activation-control study compared

\[
\phi_c(z)=\frac{\tanh(cz)}c,\qquad c=0,1,2,4,
\]

where \(\phi_0(z)=z\), and the fixed gain-matched control

\[
\phi_{\mathrm{L2}}(z)=\kappa_2z,\qquad
\kappa_2=\mathbb E[\operatorname{sech}^2(1.3Z)]
=0.5101185599716273.
\]

It kept \(P=5,N_s=16,M_\xi=81,R_\omega=128,\Delta t=0.02,T=8\). Dense references used paired seeds at \(n=128,L=32\), with depth and width diagnostics.

For the confirmatory \(c=2\) case, the dense nonlinear Gram path was \(36.38\%\) away from exact identity dynamics, while the matched nonlinear PDE was \(1.09\%\) away from dense. Equal-loss-progress paths were still \(27.14\%\) apart, ruling out a mere scalar time reparameterization. Thus the PDE is not secretly reproducing the identity network.

The stronger interpretation fails: the fixed gain-matched linear control was only \(3.46\%\) from the nonlinear dense path, inside the project’s \(5\%\) tolerance. The correct verdict is therefore:

> Exact identity/deep-linear dynamics are decisively rejected; a coarse effective-gain linear explanation is not.

A separate scalar stress with \(\phi(z)=\sin(2.5z)/2.5\) gives the cleaner mechanism check. Relative to a linear control, the dense Gram path differs by \(15.95\%\); the high-order PDE is about \(2.50\%\) from dense in Gram and \(2.81\%\) in output. Its loss error is \(5.54\%\), just outside the joint \(5\%\) rule.

### 6.4 Reproductions

The 31 July canonical rerun reproduced the \(P=5,N_s=16,M_\xi=256,R_\omega=128\) PDE and the long plateau numerically, though not byte-for-byte across platforms because whitening and linear-algebra libraries differ. A smaller smoke run with

\[
P=5,\quad N_s=8,\quad M_\xi=64,\quad R_\omega=32,\quad T=2
\]

against \(n=64,L=16,16\) dense seeds gave \(1.05\%\) output and \(3.36\%\) Gram-increment errors. It is an execution check, not independent scientific evidence.

### 6.5 What moment correction, whitening, and parity pairing do

Scrambled Sobol points are low-discrepancy points, not exact Gaussian cubature. The numerical pipeline first maps them to Gaussian coordinates and applies an affine moment correction:

\[
\xi_i^{\rm mc}
=\widehat\Sigma^{-1/2}(\xi_i^{\rm raw}-\widehat m),
\]

so the weighted empirical mean and covariance are exactly \(0\) and \(I\). With \(D_b=\operatorname{diag}(w_1^{\rm b},\ldots,w_{M_\xi}^{\rm b})\) the source-quadrature weights, it then evaluates the raw retained Hermite design \(\Psi\), forms

\[
Q_\Psi=\Psi^\top D_b\Psi,
\qquad
\widetilde\Psi=\Psi Q_\Psi^{-1/2},
\]

and uses \(\widetilde\Psi^\top D_b\widetilde\Psi=I\). The fast row-noise points receive the analogous mean/covariance correction. These steps make the first two Gaussian moments and the retained empirical basis Gram exact. They do not make higher Gaussian moments exact, and independently rewhitening at each cutoff can destroy literal nesting between cutoff spaces.

Parity pairing is complementary, not a replacement. For every source point one includes \(-\xi\), and for each retained row-noise point one includes the parity-transformed coordinate

\[
\varepsilon_\nu\longmapsto(-1)^{|\nu|}\varepsilon_\nu.
\]

A centered, whitened point cloud need not be closed under this full symmetry, which is why the older cubature leaked into theoretically inert even shells. The corrected convergence experiments used symmetry-paired tensor Gauss--Hermite source rules and paired fast points, followed by block orthonormalization compatible with the odd/even split.

### 6.6 The correct empirical conclusion

The data justify all of the following:

- the finite PDE is literal, runnable, autonomous, nonlazy, and internally gradient-consistent;
- the degree-one source model transfers surprisingly well over the tested neighborhood;
- it captures real activation-dependent effects;
- low-order performance is not a numerical time-step artifact.

They do **not** justify:

- \(P\to\infty\) convergence;
- convergence of the dense reference itself;
- equality to the ordered \(n\to\infty\), then \(L\to\infty\) target;
- sufficiency of the current PDE state for nearby dense restarts;
- accuracy uniformly over all training time.

---

## 7. Why the convergence proof has not closed

pde_convergence is best read as a sequence of increasingly accurate diagnoses rather than as a failed proof in one shot.

### 7.0 Phase ledger

| Phase | Main setup | What survived |
|---|---|---|
| 01 proof audit | Intended seven scientific gates. Only two \(P=5,N_s=16,M_\xi=625,R_\omega=256,\Delta t=0.02,T=2\) RK4 trajectories completed, from two scrambles. | The scrambles differed by \(2.85\times10^{-4}\) in output and \(3.35\times10^{-4}\) in Gram. This is a favorable low-order cubature check. No \(P=15/35\) job and none of the seven scientific gates completed. The 128 software tests do not substitute for them. |
| 02 lean salvage | Small width/depth grids; trained-depth variance; same-state attack; \(P=5,15,35\) generator test; fitted-basis and plateau diagnostics. | Favorable finite-grid contraction and \(L^{-1}\) centered variance; no state-sufficiency counterexample; later plateau. The apparent adverse \(5\to15\to35\) cutoff trend is superseded by parity. |
| 03 bridgeability | Exact parity proof; paired cubature; correct \(P=5,35,126\) odd ladder with \(N_s=4,M_\xi=1296,R_\omega=256,\Delta t=0.05\), two seeds to \(t=0.25\) and one to \(0.5\). | Even-shell equality is exact. Outgoing shell forcing contracts strongly, but aggregate low-mode feedback and observable defects grow. |
| 04 scalar stress | One datum, source dimension two; odd degrees through 13; primary \(N_s=4,M_\xi=196,R_\omega=128,\Delta t=0.025,T=2\); bounded sine stress and paired dense \(n=128,L=16\) diagnostic. | Strong genuine activation nonlinearity but tiny cutoff sensitivity. High-order tanh tail ratios disagree across scrambles; no replicated turnover. |
| 05 tail/compactness | Common high-order reference at degree 7, active modes \(200\); \(N_s=1,M_\xi=4096,R_\omega=512,\Delta t=0.025,T=0.25\); separate coupled low/high systems. | Aggregate commutator/Cauchy ratios remain above one. Per-mode amplitudes and near-orthogonal new shells suggest an \(\ell^2\) route. Analytic audit isolates noncompactness and plain-\(L^2\) instability. |

The phase-01 projected energy near one measures the fraction of the current forward field in the retained span. It is not an omitted transpose-response, outgoing-generator, or high-to-low feedback certificate.

### 7.1 Ordered dense limits and depth homogenization

On small grids

\[
n=64,128,256,\qquad L=8,16,32,\qquad T=0.5,
\]

successive width discrepancies contracted with ratios \(0.46\)–\(0.52\), the depth ratio at \(n=256\) was \(0.578\), and across-root fluctuations fit approximately \(n^{-0.61}\). These are favorable finite-grid signs, but geometric extrapolation still leaves percent-scale heuristic tails.

For trained layers at \(n=128,L=8,16,32,64\), the variance of centered depth averages scaled almost exactly like \(L^{-1}\), both forward and backward and at \(t=0.5\). This supports the desired \(L^{-1/2}\) cancellation of iid depth innovations. It does not identify the conditional shared-transpose/Onsager mean about which the cancellation should occur.

A same-state attack perturbed every finite-network middle matrix by

\[
W_\ell\longmapsto W_\ell+\alpha u_\ell v_\ell^\top,
\]

choosing

\[
v_\ell\perp\operatorname{span}\{\Phi_{35},H^\ell\},
\qquad
u_\ell\perp\operatorname{span}\{\beta^\ell\}.
\]

It follows immediately that

\[
\delta W_\ell\Phi_{35}=0,
\qquad
\delta W_\ell H^\ell=0,
\qquad
\delta W_\ell^\top\beta^\ell=0.
\]

Thus the retained row coordinates, current forward and adjoint fields, output, Grams, and tangent kernel were preserved to \(5.3\times10^{-16}\), while a component of the dense matrices invisible to those summaries changed. This was not literally a perturbation of a sampled PDE “isonormal tail”: the finite PDE has no such retained tail. The rank-one direction was selected from a projected local linearized terminal dot-Gram objective, not by globally optimizing future separation.

The altered network produced a \(0.332\%\) continuation gap over horizon \(0.5\). That nonzero number establishes finite-\((n,L)\) strict nonidentity of the summaries for this off-manifold perturbation; it was not attributed to roundoff. But the preregistered asymptotic-falsification target was \(1.5\%\), and the test used only \(n=128,L=16\), one root, and one reduced depth cell, with no width/depth scaling. The result is therefore simultaneously a small finite-network separation and a failed search for a large surviving state-sufficiency counterexample. It is not positive evidence that the PDE state is asymptotically sufficient.

### 7.2 The parity repair

The first cutoff study compared \(P=5,15,35\) and concluded that generator defects worsened. That conclusion was invalid. Under

\[
(\xi,\varepsilon,h,p)\mapsto(-\xi,-\varepsilon,-h,-p)
\]

with odd \(\tanh\) and even \(\tanh'\), the degree-\(k\) source coefficient satisfies

\[
H_{\nu r}=(-1)^{|\nu|+1}H_{\nu r},
\]

so even degrees vanish exactly. The old Sobol cubature was centered and whitened but not paired under the full parity map; training magnified the leakage.

After enforcing parity, \(P=5\) and \(P=15\) agree at \(10^{-17}\). The correct first comparison is degree \(1\to3\), or \(P=5\to35\).

### 7.3 Outgoing tails contract; aggregate feedback does not

On the corrected ladder \(P=5,35,126\), the newly opened outgoing shell residual contracted by a factor of roughly \(31\)–\(34\) at \(t=0.25\). That sounds decisive, but it measures only how strongly a zero high shell is initially forced.

Once the high-order system is trained, its populated high modes can feed back collectively into the low modes. The dynamic state used in the comparison is

\[
Y_{r_H}=(b_{r_H},a_{r_H},c_{r_H});
\]

the fields \(h,p,z,\beta\) are recomputed from it and are not separately counted in the state norm. With base-source weights \(w_i^{\rm b}\), fast row-noise weights \(w_j^{\rm f}\), and \(N_s\) depth cells, the norm is

\[
\|Y\|_{\rm st}^2
=\sum_iw_i^{\rm b}\|b_i\|_2^2
+\sum_iw_i^{\rm b}|a_i|^2
+\frac1{N_s}\sum_{\ell,i,j}
w_i^{\rm b}w_j^{\rm f}\|c_{\ell ij}\|_2^2.
\]

For separately evolved adjacent cutoffs \(r_H<r_H'\), define the new-shell and shared-low-mode pieces

\[
H_{r_H,r_H'}=\|(I-\Pi_{r_H})Y_{r_H'}\|_{\rm st},
\qquad
S_{r_H,r_H'}=\|\Pi_{r_H}Y_{r_H'}-Y_{r_H}\|_{\rm st},
\]

and

\[
E_{r_H,r_H'}=(H_{r_H,r_H'}^2+S_{r_H,r_H'}^2)^{1/2}.
\]

The corresponding observable distance is

\[
O_{r_H,r_H'}
=\max\left\{
\frac{\|f_{r_H'}-f_{r_H}\|_2}{S_f},
\frac{\max_\ell\|G_{r_H'}^\ell-G_{r_H}^\ell\|_F}{S_G}
\right\},
\]

with \(S_f=\|y\|_2=1.0319883720\ldots\) and \(S_G=\|X^\top X\|_F=\sqrt3\). At \(t=0.25\), the **coupled Cauchy** ratios were

\[
\frac{E_{5,7}}{E_{3,5}}=1.32193,
\qquad
\frac{O_{5,7}}{O_{3,5}}=1.63581.
\]

A different test trained one common degree-seven reference \(Y_7(t)\), with 200 active odd modes, and obtained each lower comparison by literal projection of this same state. Its vector-field commutator is

\[
\Delta_{d\to d+2}(Y_7)
=\Pi_dF_{d+2}(\Pi_{d+2}Y_7)-F_d(\Pi_dY_7).
\]

Using the same state norm, it gave

\[
\frac{\|\Delta_{5\to7}(Y_7)\|_{\rm st}}
{\|\Delta_{3\to5}(Y_7)\|_{\rm st}}
=1.3257147.
\]

The output- and depth-Gram directional-derivative defects were normalized by \(S_f,S_G\) and evaluated by centered finite differences with relative step \(2\times10^{-6}\); the largest, from the Gram channel, had ratio \(1.6173852\). Thus the two pairs \(1.3219/1.6358\) and \(1.3257/1.6174\) come from different experiments: separately evolved Cauchy errors versus one-state generator commutators.

These tests used

\[
N_s=1,\quad M_\xi=4096,\quad R_\omega=512,\quad
\Delta t=0.025,\quad T=0.25,
\]

so aggregate contraction had not begun through degree seven in this depth-collapsed discretization. Specifically, \(N_s=1\) means one coefficient-law cell \(c_0\), endpoint fields \(h_0,h_1\), one forward and one reverse depth update with \(\Delta s=1\), and a one-cell quadrature for the tangent-kernel depth integral. It is algebraically similar to one residual block and is not a certified continuous-depth approximation. A degree-five control gave ratios \(1.3732,1.3835,\approx1.39\) at \(N_s=1,2,4\), making a gross one-cell artifact unlikely at that order. The degree-seven calculation was not repeated at \(N_s>1\), so its headline ratios cannot be promoted to continuous-depth evidence.

There is a more hopeful structural fact. In four source coordinates, homogeneous shells of degrees five and seven contain

\[
N_5=\binom83=56,
\qquad
N_7=\binom{10}3=120
\]

modes. If \(A_d\) is an aggregate shell norm, its RMS amplitude per mode is \(A_d/\sqrt{N_d}\). The measured aggregate ratio \(A_7/A_5\) and multiplicity-adjusted ratio were

\[
\begin{array}{c|cc}
\text{channel}&A_7/A_5&(A_7/A_5)\sqrt{56/120}\\ \hline
c&1.26627&0.86503\\
\dot c&1.26655&0.86522\\
h&1.32175&0.90293\\
p&1.41207&0.96463.
\end{array}
\]

The total-state commutator similarly changed from \(1.32571\) to \(0.90564\) after cardinality adjustment. But the readout channel and the two observable-generator channels remained above one even after that adjustment: \(1.11875,1.05832,1.10488\). Consecutive input-field commutators were nearly orthogonal and participation counts increased, arguing against one coherent resonant mode. This is finite-level evidence for a broad possibly square-summable tail, not a proof: there is only one degree-five-to-seven shell ratio, and no asymptotic decay exponent was fitted.

### 7.4 The functional-analytic obstruction

Let

\[
\mathcal H=L^2(\mu_\xi),\qquad
\mathcal R=L^2(\mu_{\xi'}\otimes\mathbb P_\omega).
\]

The frozen row map

\[
I:\mathcal H\to\mathcal R,\qquad Iu=W_\omega(u)
\]

is an isometry. Its transpose \(T_W=I^\ast\) is therefore bounded:

\[
\|T_W\beta\|_{\mathcal H}\le\|\beta\|_{\mathcal R}.
\]

This corrects an earlier overstatement: Malliavin differentiability is not needed merely to *define* the frozen transpose.

But \(T_W\) is not compact. If \(\varepsilon_\nu=W_\omega(\psi_\nu)\), then

\[
T_W\varepsilon_\nu=\psi_\nu,
\]

so no uniform finite-rank approximation exists on the unit ball. Energy dissipation yields cutoff-uniform state bounds and \(1/2\)-Hölder time equicontinuity, but boundedness in source \(L^2\) supplies no spatial compactness.

Plain \(L^2\) is also too weak for local stability. The nonlinear gate

\[
(z,p)\mapsto\phi'(z)p
\]

has variation containing \(p\,\delta z\). With only \(p,\delta z\in L^2\), the product is merely \(L^1\); moreover the terminal adjoint contains an unbounded Gaussian readout coordinate. A cutoff-uniform Grönwall constant does not follow.

A weighted Gaussian Sobolev scale based on the number operator \(N_G\) gives the deterministic tail inequality

\[
\|(I-\Pi_{r_H})u\|_{L^2(\mu)}
\le(1+r_H)^{-\alpha/2}
\|(I+N_G)^{\alpha/2}u\|_{L^2(\mu)}.
\]

The missing theorem is propagation, uniformly in \(r_H\), of such source-mode-coercive regularity for the entire coupled forward/adjoint/Liouville flow. Generic unweighted Sobolev or Orlicz estimates are not enough: an orthonormal coordinate sequence can obey the same unweighted bounds without being compact.

### 7.5 The three bridges

The repository correctly separates three theorems that are sometimes conflated:

1. **Galerkin bridge:** finite-\(P\) PDE solutions converge on \([0,T]\) to a unique infinite-source operator flow. This requires compactness or a quantitative consistency-plus-stability estimate, and well-posedness/uniqueness of the limit.
2. **Dense identification bridge:** the infinite operator flow is the ordered \(n\to\infty\), then \(L\to\infty\) limit of Family R. This requires fixed-\(L\) causal width theory, trained-depth homogenization, and derivation of the conditional shared-transpose mean.
3. **All-time bridge:** compact-horizon approximation upgrades to \(t\in[0,\infty)\). Loss dissipation alone is insufficient near small tangent-kernel eigenvalues; one needs coercivity after entry, residual integrability, a trapping region, or a finite state-arclength estimate uniform in the approximation.

At present, none of the three is complete. The finite-\(P\) PDE can still be useful even if pure Hermite truncations eventually require response coordinates or another fixed basis. What current evidence rules out is claiming monotone aggregate convergence from the available degree ladder.

---

## 8. Mean-field peeling: a rigorous local compiler

The operator PDE is a proposed *state evolution*. Mean-field peeling solves a different problem: for a fixed architecture, fixed depth and batch, fixed derivative order, and fixed number of optimizer steps, can every width-normalized contracted observable be reduced explicitly to deterministic Gaussian expectations?

The answer is now “yes” for several substantial families and “not yet” as one universal compiler theorem.

### 8.1 The local Gaussian mechanism

At a hidden layer, write the effective matrix as \(A^\ell=s_{\ell,n}\theta^\ell\), with raw Gaussian \(\theta^\ell\), and

\[
z_i^\ell(r)=\sum_jA^\ell_{ij}h_j^{\ell-1}(r)+\sigma_b b_i^\ell.
\]

Conditioned on the lower layers, a row \(z_i^\ell=(z_i^\ell(r))_{r=1}^m\) is exactly Gaussian with covariance determined by the empirical lower-layer Gram. In the common \(A_{ij}=n^{-1/2}\theta_{ij}\) convention,

\[
\operatorname{Cov}\!\left(A_{ij},z_i^\ell(r)\mid h^{\ell-1}\right)
=\frac1n h_j^{\ell-1}(r).
\]

This small but nonzero covariance is the source of every Stein/Onsager attachment. Declaring \(A_{ij}\) independent of the preactivation it creates would erase feature learning.

For a product of explicit Gaussian weights times a smooth function of jointly Gaussian preactivations, repeated integration by parts gives a sum over **partial matchings**:

- paired explicit weights contribute ordinary Wick covariances;
- unpaired weights attach to a preactivation and differentiate the nonlinear factor;
- every attachment leaves lower-layer factors that must remain as boundary data for the next peel.

For example,

\[
\mathbb E[X_iX_jF(Z)]
=\operatorname{Cov}(X_i,X_j)\mathbb E[F(Z)]
+\sum_{\alpha,\beta}
\operatorname{Cov}(X_i,Z_\alpha)
\operatorname{Cov}(X_j,Z_\beta)
\mathbb E[\partial_{\alpha\beta}F(Z)].
\]

At finite width, this is exact. The difficult bookkeeping is global:

1. expose every equality partition among neuron indices;
2. keep all explicit powers of \(n\), optimizer multipliers, and downstream sums;
3. peel the highest remaining random-matrix group;
4. retain every fresh Gaussian channel and every cross-covariance generated through that same matrix;
5. only after complete width counting replace empirical covariances by deterministic limits.

The order is essential. A row singled out by a derivative also contributes to its empirical covariance, so leave-one-out or leave-two-out control is needed before deterministic replacement. One-copy expectation calculations and concentration of empirical kernels are separate obligations.

The desired output is a Gaussian-normal-form DAG: no random matrix, growing neuron sum, unnamed Onsager term, or hidden equality class remains. Its nodes are fixed-dimensional Gaussian expectations and deterministic algebra. At fixed batch \(m\), a primitive Gaussian row has dimension \(m\); a derivative-order-\(j\) calculation generally needs a finite multiple \(q_jm\), not necessarily one \(m\)-vector.

### 8.2 What is theorem-level

For each separately fixed computation, the reports distinguish:

- exact finite-width differentiation and Wick--Stein identities;
- an algebraically complete limiting normal form;
- a probability theorem establishing convergence of the finite-width program;
- a depth-uniform finite-state grammar.

The generic order-three program is the cleanest complete case. The imported result is specifically Setup 3.6 and Theorem 3.7, the **Non-Gaussian Master Theorem**, of Golikov--Yang, *[Non-Gaussian Tensor Programs](https://papers.nips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf)*. For a fixed finite tensor program, it assumes independent matrix entries of mean zero and variance \(n^{-1}\), uniform normalized bounds on every higher entry moment, polynomially smooth coordinate nonlinearities—\(C^\infty\) with every partial derivative polynomially bounded—and finite moments of the initial scalar variables. It then gives almost-sure and \(L^p\) convergence, for every finite \(p\), of each scalar program variable to the Gaussian-master-theorem value. Gaussian matrices are a special case, and the program language used here admits the required matrix/transpose reuse and empirical scalar moments.

For each separately fixed depth, batch, and derivative order, the audited derivative computation is first compiled into such a finite program. The theorem then supplies the joint Gaussian/Onsager semantics and, because it gives \(L^{1+\epsilon}\) convergence, uniform integrability and convergence of the annealed coefficient. This is not a theorem about a depth or derivative order growing with width.

The distinction concerning smoothness is precise. Assuming only \(\phi\in C^5\) with polynomial growth through derivative five is sufficient to *write and bound the displayed finite-width order-five algebra*. It does not satisfy the cited theorem's all-derivatives hypothesis. A weaker probability-limit route would therefore still need, for every retained monomial \(Z_n\), a tail estimate such as

\[
\sup_n\mathbb E|Z_n|^{1+\epsilon}<\infty
\]

and convergence in probability. Those two facts imply uniform integrability and hence convergence of expectations. Thus the missing "tail proof" is not the claim that one more derivative exists; it is a width-uniform moment bound for the entire compiled collection. The reports do not supply that weaker bridge under merely finite \(C^5\) control.

The open global theorem is stronger: termination of the peeling grammar for every admissible observable, plus a bound on the number of retained state types independent of depth at fixed derivative order. Existing Tensor Program semantics may leave recursively named nonlinear variables; the proposed compiler wants a fully eliminated, auditable Gaussian DAG. That distinction is real, but the general finite-state theorem has not been proved.

### 8.3 Backward kernels at initialization

For Family F define

\[
G^0_{rq}=\frac{x_r^\top x_q}{d_0},\qquad
G^\ell_{rq}
=\mathbb E[\phi(Z_r^\ell)\phi(Z_q^\ell)],
\qquad
D^\ell_{rq}
=\mathbb E[\phi'(Z_r^\ell)\phi'(Z_q^\ell)],
\]

where \(Z^\ell\sim N(0,G^{\ell-1})\). With normalized adjoints

\[
\delta_i^\ell(r)=n\frac{\partial f_r}{\partial z_i^\ell(r)},
\]

the peeled backward covariance is

\[
\Pi^\ell
=D^\ell\odot D^{\ell+1}\odot\cdots\odot D^H.
\]

For three hidden layers, the limiting fixed-depth tangent kernel becomes

\[
\Theta^{\rm F}
=G^3
+G^2\odot D^3
+G^1\odot D^2\odot D^3
+G^0\odot D^1\odot D^2\odot D^3.
\]

The nontrivial point is not the final product formula; it is that the transpose uses the same matrices as the forward pass. The detailed peel retains all Stein branches until global counting shows which are lower order.

The original three-hidden-layer case study enumerates this expectation-level product directly. Its own four-copy concentration estimate \(\operatorname{Var}(\Pi^\ell_{n,rq})=O(n^{-1})\) and its proposed arbitrary-depth diagram induction were left open. The general separately fixed-\(H\) formula is justified instead by the later tensor-program theorem, under the stated hypothesis that \(\phi\in C^\infty\) and every derivative has polynomial growth. It is not a depth-uniform theorem.

### 8.4 One gradient step: where feature motion first appears

For

\[
\mathcal J=\frac1m\sum_r(f_r-y_r)^2,
\qquad
\theta^+=\theta-n\eta\nabla\mathcal J,
\]

the initialization-averaged loss has limiting linear coefficient

\[
\lim_{n\to\infty}[\eta]\,\mathbb E[\ell_r^+]
=-\frac4m\,y_r\sum_q\Theta^{\rm F}_{rq}y_q.
\]

The hidden-Gram linear coefficient vanishes in the width limit because of centered-readout parity:

\[
\lim_{n\to\infty}[\eta]\,\mathbb E[G_{n,rq}^{\ell,+}]=0.
\]

This does not mean the random coefficient is zero, nor may it be set to zero before differentiating. At quadratic order,

\[
\mathbb E[G_{n,rq}^{\ell,+}]
=G^\ell_{rq}+\eta^2C^\ell_{rq}+o(\eta^2)+o_n(1).
\]

The surviving \(C^\ell\) contains a fresh off-diagonal Gaussian field. Its one-copy mean is zero, but its square contributes at leading order. This is a concrete demonstration that “replace the random matrix by its mean before squaring” is wrong.

Here is the missing mechanism. At layer two, one propagated part of the first feature velocity contains

\[
\frac1n\sum_{i,p'}W^2_{pi}W^2_{p'i}\,\phi'(z_i^1(a))
\sum_c\lambda_cG^0_{ac}\phi'(z_i^1(c))\delta^2_{p'}(c).
\]

Split the equality pattern \(p'=p\) from \(p'\ne p\). The diagonal pattern gives the deterministic Stein response which, together with the direct matrix-update term, produces the chronological response

\[
\sum_c\lambda_cT^1_{ac}\delta_p^2(c).
\]

Every off-diagonal summand is conditionally centered. But there are order \(n^2\) choices of \((i,p')\) against the square of the \(n^{-1}\) normalization. When two copies are formed, the row-distinct Wick pairing matches the two explicit weight pairs and leaves an order-one covariance. The conditional CLT therefore leaves a centered Gaussian innovation \(\Gamma^\ell\), not zero:

\[
u^\ell(a)=\Gamma^\ell(a)+\sum_c\lambda_cT^{\ell-1}_{ac}\delta^\ell(c),
\qquad
\mathbb E[\Gamma^\ell(a)\Gamma^\ell(b)]=V^{\ell-1}_{ab},
\]

where \(V^\ell_{ab}=\mathbb E[g^\ell(a)g^\ell(b)]\). Squaring the velocity gives the surviving term

\[
V^\ell_{ab}\supset D^\ell_{ab}V^{\ell-1}_{ab}.
\]

Finally \(C^\ell_{ab}=V^\ell_{ab}+S^\ell_{ab}+S^\ell_{ba}\), where \(S^\ell_{ab}=\mathbb E[s^\ell(a)h^\ell(b)]\) is the second-displacement cross moment. Thus the fresh field survives in \(C^\ell\) through a variance-order Wick contraction: it is not an Onsager mean, and its survival occurs in the fixed-depth \(n\to\infty\) coefficient limit. This calculation is exact at the contraction level subject to the stated conditional-CLT and moment hypotheses; it is not a positive-time dynamics theorem.

For the deep-linear control, if \(\kappa=2/m\) and \(\sigma=G^0y\),

\[
C^\ell_{rq}
=(1,5,14)_\ell\,\kappa^2\sigma_r\sigma_q,
\qquad \ell=1,2,3.
\]

### 8.5 Two Euler steps are not twice one step

Let \(F(\theta)=-n\nabla\mathcal J(\theta)\). Two steps satisfy the exact finite-width expansion

\[
\theta^{(2)}
=\theta+2\eta F+\eta^2DF[F]+O(\eta^3).
\]

For a hidden Gram \(O=G^\ell_{rq}\), define

\[
\mathcal D_1=DO[F],\qquad
\mathcal D_2=\frac12D^2O[F,F],\qquad
\mathcal D_{\rm rg}=DO[DF[F]].
\]

Then

\[
G^{\ell,(2)}
=G^\ell+2\eta\mathcal D_1
+\eta^2(4\mathcal D_2+\mathcal D_{\rm rg})+O(\eta^3),
\]

while the second-step increment is

\[
G^{\ell,(2)}-G^{\ell,(1)}
=\eta\mathcal D_1
+\eta^2(3\mathcal D_2+\mathcal D_{\rm rg})+O(\eta^3).
\]

The new term \(\mathcal D_{\rm rg}\) comes from recomputing the gradient. Its exact finite-width representation differentiates the forward and backward states, introducing \(u,g,\dot\delta,\dot\xi,\bar z,\bar h\). A multichannel Wick--Stein rule must retain every fresh Gaussian field and every cross-covariance produced through a reused matrix.

For a general nonlinear activation, the reports give exact directional identities and a formal multichannel schema, but not a fully enumerated convergent registry. The deep-linear specialization is complete:

\[
(\mathcal D_{\rm rg})^\ell_{rq}
=(6,14,20)_\ell\kappa^2\sigma_r\sigma_q,
\]
\[
(4\mathcal D_2+\mathcal D_{\rm rg})^\ell
=(10,34,76)_\ell\kappa^2\sigma_r\sigma_q,
\qquad
(3\mathcal D_2+\mathcal D_{\rm rg})^\ell
=(9,29,62)_\ell\kappa^2\sigma_r\sigma_q.
\]

This is both a valuable audit and a qualification: a finite number of training steps can be compiled coefficientwise, but the state registry grows with derivative order and step count. Nothing here authorizes a number of steps of order \(1/\eta\) or a fixed positive-time trajectory.

### 8.6 Generic feature jets: the staged subprojects

The generic_first_stieltjes subtree is a sequence of increasingly broad exact local calculations.

#### Two hidden layers, one sample, order three

For

\[
f_n=\frac1n\sum_i a_i\phi(z_i),\qquad
D_n=n\nabla f_n\cdot\nabla,
\]

the cubic coefficient

\[
B_\phi=\lim_{n\to\infty}\mathbb E[D_n^3f_n]
\]

has an explicit normal form of 17 one-dimensional Gaussian atoms involving derivatives only through \(\phi'''\). In rescaled coordinates, the finite-width skeleton is

\[
D_n^3f_n=4\|H\nabla f_n\|^2+2\,\nabla^3f_n[\nabla f_n,\nabla f_n,\nabla f_n].
\]

Two independent groupings agree; constant, linear, affine, and quadratic controls pass. For \(q_0=1\) and \(\phi(x)=\sin x\),

\[
J_1=\lim\mathbb E[D_nf_n]=1,\qquad
J_{3,\phi}=-1.8869998273\ldots.
\]

Thus even the first nonlinear output-kernel coefficient need not be positive for a generic smooth activation.

The base compiler was checked seedwise at widths \(1,2,5,9\) and several activations; an exploratory Monte Carlo used widths \(16,32,64\) with \(4096,2048,1024\) samples. These are implementation and finite-width checks. The fixed-program \(L^p\) theorem, under the polynomial-smooth envelope, is what elevates the annealed coefficient beyond numerics.

#### Fixed batch and arbitrary fixed depth, order three

For any separately fixed batch size, deterministic positive-semidefinite input Gram, labels, and hidden depth, the response-aware recursion evaluates the corresponding cubic directional coefficient using an \(O(m^2)\) state per layer. One convenient form uses a \(4m\)-dimensional Gaussian block at each forward layer. It covers singular input Grams and retains the label channel explicitly.

For the batch MSE jet,

\[
\begin{aligned}
\mathcal J(t)
={}&\frac{y^\top y}{m}
-\frac{4\eta}{m^2}y^\top\Theta^{\rm F}y\,t
+\frac{8\eta^2}{m^3}y^\top(\Theta^{\rm F})^2y\,t^2\\
&-\left[
\frac{32\eta^3}{3m^4}y^\top(\Theta^{\rm F})^3y
+\frac{8\eta^3}{3}C_{y/m}
\right]t^3
\pmod{t^4}.
\end{aligned}
\]

The last term is the first feature-learning correction beyond frozen NTK. Two extra response contractions vanish only after a whole-program centered-readout parity argument; they cannot be dropped by local symmetry inspection.

#### Order five at two, three, and four hidden layers

For one sample and two hidden layers, the exact flattened output jet

\[
J_1=F'(0),\qquad J_3=F^{(3)}(0),\qquad J_5=F^{(5)}(0)
\]

contains \(3,46,974\) rational moment monomials in the unit-Gram quotient and uses derivatives through \(\phi^{(5)}\). Exact controls include

\[
(J_1,J_3,J_5)_{\rm linear}=(3,48,1464),
\]
\[
(J_1,J_3,J_5)_{\rm quadratic}
=(111,1\,685\,184,77\,400\,633\,120).
\]

At depths \(H=3,4\), layer-tagged term counts are

\[
(4,342,27\,421),\qquad(5,1\,929,462\,776),
\]

while unit-Gram counts are

\[
(4,160,6\,519),\qquad(5,350,17\,641).
\]

Independent frozen compilers agree coefficientwise. The general tagged intermediate representation stores 21 forward covariances, 15 reverse covariances, 15 forward responses, and 15 transpose responses per reused matrix. In the shared-activation unit-Gram quotient, a complete scalar recurrence uses 29 coordinate types across six chronological sweeps of dimensions

\[
7/8/4/4/3/3
\]

and 38 local transition maps.

The six sweeps are not six repetitions of one map. They are alternating nearest-neighbor traversals of six different frozen/moving covariance-and-response registries; an individual sweep can carry several derivative grades. A hat denotes a derivative along the frozen straight parameter line through initialization; no hat denotes the moving feature-ascent flow. Here \(\langle v,w\rangle_n=n^{-1}v^\top w\), and \(E_j,J_j\) name centered frozen- and moving-reverse Gaussian innovations used only to explain the recurrence semantics; they do not remain as random variables in the compiled scalar graph.

| sweep | dimension and propagated coordinates | what is being transported |
|---|---|---|
| F1 | \(7: u,v,w,x,y,j,k\) | Frozen forward covariances \(u=\mathbb E\langle\widehat X_0,\widehat X_2\rangle_n\), \(v=\mathbb E\langle\widehat X_0,\widehat X_4\rangle_n\), \(w=\mathbb E\langle\widehat X_1,\widehat X_1\rangle_n\), \(x=\mathbb E\langle\widehat X_1,\widehat X_3\rangle_n\), \(y=\mathbb E\langle\widehat X_2,\widehat X_2\rangle_n\), plus the mean Stein responses \(j=\mathbb E[\partial_{E_0}\widehat X_3]\), \(k=\mathbb E[\partial_{E_0}\widehat X_5]\). |
| R1 | \(8: e_{02},e_{11},e_{13},e_{22},c_{10},c_{21},c_{30},c_{32}\) | Frozen reverse covariances and the four live transpose-response coefficients in \(\widehat\Delta_1,\widehat\Delta_2,\widehat\Delta_3\). |
| F2 | \(4: q_{02},q_{22},q_{\rm fm},a_2\) | Moving grade-two feature covariances \(\langle X_0,X_2\rangle,\|X_2\|^2,\langle\widehat X_2,X_2\rangle\) and its reverse-innovation response. |
| R2 | \(4: r_{02},r_{22},r_{\rm fm},d_{21}\) | Moving grade-two reverse covariances and the coefficient in \(\Delta_2=J_2+d_{21}X_1\). |
| F3 | \(3: q_{13},a_{30},a_{32}\) | The mixed covariance \(\mathbb E\langle\widehat X_1,X_3\rangle_n\) and responses of \(X_3\) to reverse innovations of grades zero and two. |
| R3 | \(3: r_{13},d_{30},d_{32}\) | The moving reverse covariance \(\langle\widehat\Delta_1,\Delta_3\rangle\) and the two coefficients in \(\Delta_3=J_3+d_{30}X_0+d_{32}X_2\). |

Each sweep visits the \(H\) hidden layers once; the displayed first/top initialization is the corresponding boundary cell, so the factored graph has \(6H\) local transitions and 29 *coordinate types*, not 29 numbers total independent of depth. The order-three recurrence is the closed projection \((w,u,j;e_{11},c_{10})\). The remaining coordinates are needed by the order-five moving-flow and terminal contractions. This is what distinguishes the \(O(H)\) factored DAG from the much larger fully expanded polynomial.

This establishes a literal finite-state recurrence for that observable at each separately fixed \(H\). It does not establish the hoped-for one-forward/one-backward compression, and the fully distributed formula grows from 1,045 terms at \(H=2\) to 462,776 at \(H=4\). A depth-uniform small flattened representation therefore remains open.

#### Multiple observables

The multi-observable extension separates a universal parameter-flow jet from observable-specific heads. For the hidden activation squared RMS, a missing fourth-order contraction \(\Gamma_{04}\) reduces to one additional forward sweep and two dynamic scalars; a third apparent scalar is deterministic depth data. Independent producers agree on 64 backbone and 17 head monomials, two finite-width differentiators agree in 30 layer-cases to \(1.38\times10^{-15}\), and constant/linear/affine controls pass.

The observable head is not just a term count. If \(Q_\ell(s)\) is a hidden squared-RMS feature observable, set \(q_2=Q_\ell''(0)\), \(q_4=Q_\ell^{(4)}(0)\), and write the separately fixed-depth output jet as \(F'(0)=J_{1,H}\), \(F'''(0)=J_{3,H}\). Under the exact physical-time change \(ds/dt=c(1-F(s))\), \(c=2\eta\), annealed parity and formal composition give

\[
\begin{aligned}
Q_{\ell,t}''(0)&=c^2q_2,\\
Q_{\ell,t}'''(0)&=-3c^3J_{1,H}q_2,\\
Q_{\ell,t}^{(4)}(0)&=c^4(q_4+7J_{1,H}^2q_2),\\
Q_{\ell,t}^{(5)}(0)&=-5c^5\bigl[(3J_{1,H}^3+J_{3,H})q_2+2J_{1,H}q_4\bigr].
\end{aligned}
\]

The fifth output coefficient correctly enters only one order later. Computationally, the six-sweep universal backbone costs \(O(H)\); one additional streaming head sweep emits the observable at every layer in another \(O(H)\), with \(O(1)\) dynamic head memory once the backbone is cached. Retaining all layer outputs costs \(O(H)\). This is an exact amortized-DAG statement for this head, not a universal small-head theorem.

Two \(H=2\) normalized-sine panels passed. A 2,550-network panel used widths \(16,32,64,128\). The original three-width \(H=3\) fit was inconclusive because a quadratic-in-\(1/n\) intercept fit saturated its degrees of freedom; a separately frozen \(n=512\) extension resolved that design defect and passed. A broader normalized-sine order-five program used 7,700 networks across the tested depths and passed.

The promoted claim is narrow: separately fixed depth, one sample, unit forward Gram, and the specified squared-activation RMS head. Preactivation RMS, a universal small head for arbitrary observables, and the order-seven recurrence are open.

### 8.7 The exact quadratic compiler

The quadratic_compiler subtree realizes peeling completely for Family Q. A scalar monomial is a decorated bipartite forest:

- row vertices carry powers of \(a_i\);
- column vertices carry half-powers of \(u_j\);
- edges carry factors \(W_{ij}\).

Applying \(D_n\) has three local rewrites: hit \(a\), hit \(u^{2p}\), or hit \(W\). The first two preserve a tree component; a weight hit deletes a bridge and splits one component into two.

Suppose a generated forest has \(r\) original components and \(2P\) weight edges. A Wick pairing produces a quotient covariance graph with \(P\) edges, \(V\) vertices, \(c\) components, and cycle rank \(\beta\):

\[
V=P+c-\beta.
\]

The normalization requires \(V=P+r\) at leading width. Since \(c\le r\) and \(\beta\ge0\), survival forces

\[
c=r,\qquad\beta=0.
\]

Thus leading Wick pairs never join original components, and each quotient is a forest. The expectation factors over components, yielding a memoized connected recursion with exact Leibniz convolution.

This is a genuine theorem for the special quadratic grammar, but the exact coefficient prefix has staged provenance. Exhaustive forest expansion, connected recursion, and an independent equality-partition evaluator certify the full canonical grammar through order 11. The order-13 block-metric result comes from the exact \(\beta=1\) Gaussian-program recurrence. Canonical orders 15 and 17 come from two independently implemented bounded scalar recurrences. All are exact audited computer algebra under proved reductions; they are not outputs of one undifferentiated forest engine. The resulting canonical odd derivatives through order 17 are listed in Section 10.

#### Depth-three raw-square nested detransposition

A newly added depth-three sub-study tests whether the Gaussian-program route remains practical after introducing a second reused hidden matrix. Its one-input network is

\[
X=u^{\odot2},\qquad
Z=n^{-1/2}WX,\qquad Y=Z^{\odot2},\qquad
T=n^{-1/2}VY,\qquad
f_n=n^{-1}A^\top T^{\odot2},
\]

with equal width \(n\), independent standard-Gaussian blocks \((A,V,W,u)\), and the equal-block feature generator \(D_n=n\nabla f_n\cdot\nabla\). This is the unnormalized raw-square model: its initialization Gram chain is \(1,3,27,2187\). It is a severe toy regime—one input, no biases, unbounded activation, and no label, optimizer step size, finite horizon, or positive-time training experiment.

Put

\[
B_3=A\odot T,\quad
R_2=n^{-1/2}V^\top B_3,\quad
B_2=Z\odot R_2,\quad
R_1=n^{-1/2}W^\top B_2.
\]

Before taking width, the exact flow is

\[
\dot A=T^{\odot2},\qquad
\dot V=\frac2{\sqrt n}B_3Y^\top,\qquad
\dot W=\frac4{\sqrt n}B_2X^\top,\qquad
\dot X=16X\odot R_1.
\]

Integrating each matrix before its forward/transpose reuse exposes the memory exactly; for the lower matrix,

\[
\begin{aligned}
Z(t)&=n^{-1/2}W_0X(t)
+4\int_0^tB_2(s)\langle X(s),X(t)\rangle_n\,ds,\\
R_1(t)&=n^{-1/2}W_0^\top B_2(t)
+4\int_0^tX(s)\langle B_2(s),B_2(t)\rangle_n\,ds,
\end{aligned}
\]

with an analogous pair for \(V\). The proposed width-first, fixed-derivative-order reduction then uses three scalar Gaussian polynomial laws: bottom \((u,\xi^W)\), middle \((\eta^W,\xi^V)\), and top \((A,\eta^V)\). Forward and transpose innovations have covariances supplied by the adjacent feature laws, while reuse is retained by causal Stein responses such as

\[
\widehat Z_k=\eta_k^W+
\sum_{j<k}\mathbb E[\partial_{\xi_j^W}X_k]B_{2,j},
\qquad
\widehat R_{1,k}=\xi_k^W+
\sum_{j\le k}\mathbb E[\partial_{\eta_j^W}B_{2,k}]X_j.
\]

These are Gaussian *polynomial* laws: the base innovations are jointly Gaussian, while \(X_k,Z_k,\ldots\) are generally nonlinear polynomials of them. Through grade \(k\), the three laws and their carried variables are:

- \(\mathcal L_1\), bottom: the Gaussian coordinates \((u,\xi^W_0,\ldots,\xi^W_k)\), carrying \(X_j,R_{1,j}\);
- \(\mathcal L_2\), middle: \((\eta^W_0,\ldots,\eta^W_k,\xi^V_0,\ldots,\xi^V_k)\), carrying \(Z_j,Y_j,R_{2,j},B_{2,j}\);
- \(\mathcal L_3\), top: \((A,\eta^V_0,\ldots,\eta^V_k)\), carrying \(T_j,B_{3,j},A_j\).

The two middle innovation families have zero cross-covariance because \(W_0\) and \(V_0\) are independent. Their nonzero covariances are determined self-consistently by adjacent-law moments, for example

\[
\mathbb E_2[\eta^W_k\eta^W_j]=\mathbb E_1[X_kX_j],
\qquad
\mathbb E_1[\xi^W_k\xi^W_j]=\mathbb E_2[B_{2,k}B_{2,j}],
\]

with the analogous \(V\)-pair. Thus at every fixed grade the state is a finite covariance table plus explicit multivariate polynomials; it is not an assumption that the activations themselves remain Gaussian.

The response sums follow by chronological Gaussian integration by parts for the same frozen matrix. Schematically, if a forward multiplication by \(W_0\) acts on a polynomial \(X_k\) that also depends on earlier transpose innovations \(\xi_j^W\), detransposition gives a fresh forward innovation plus

\[
\sum_j \mathbb E[\partial_{\xi_j^W}X_k]\,B_{2,j}.
\]

The integrated equation for \(X\) makes \(X_k\) depend only on \(R_{1,0},\ldots,R_{1,k-1}\), so \(j=k\) has not yet entered and the forward sum is strict: \(j<k\). Conversely, \(B_{2,k}=\sum_{p+q=k}Z_pR_{2,q}\) already contains the current forward innovation \(\eta_k^W\). The transpose multiplication \(W_0^\top B_{2,k}\) therefore has a current-grade response and the sum is weak: \(j\le k\). The same argument applies to \(V_0/V_0^\top\). This strict/weak boundary is forced by the dependency DAG, not chosen as a convention; treating the two actions as independent Gaussians deletes all these response terms.

Each derivative grade then closes in the acyclic order

\[
(A_k,X_k)\to Z_k\to Y_k\to T_k\to B_{3,k}
\to R_{2,k}\to B_{2,k}\to R_{1,k}.
\]

The two exact assemblers—ordinary Taylor coefficients and derivative-normalized coefficients with explicit binomial/multinomial weights—agree through order nine. The full frozen odd prefix is

\[
\begin{aligned}
J_1&=14\,175,\\
J_3&=139\,445\,032\,896,\\
J_5&=4\,298\,284\,752\,832\,899\,360,\\
J_7&=272\,967\,464\,957\,028\,310\,013\,451\,264,\\
J_9&=29\,466\,555\,372\,596\,241\,677\,766\,026\,853\,605\,376.
\end{aligned}
\]

The first three values are frozen internal controls; \(J_7,J_9\) are the new recurrence outputs. Global sign reflection sends \(f(-\theta)=-f(\theta)\), and symmetric Gaussian initialization makes the annealed formal curve odd, explaining why every even recurrence coefficient through eight is exactly zero. I reran both exact routes: all prospective gates passed, in about \(33\) seconds combined; the largest grade-nine polynomial had \(579\) monomials and the middle Wick cache \(37\,219\) entries. Because the assemblers share the same detransposition identities, their agreement audits coefficient normalization and recurrence assembly, not the width-limit theorem independently. The directory does not state a convergence mode or prove the network-to-Gaussian-program limit, and it has no independent finite-width extrapolation. It therefore establishes practical exact execution of the proposed recurrence at this one depth/order; identifying \(J_7,J_9\) as network width limits remains conditional. It says nothing yet about a positive-time curve, convergence radius, all-order sign law, Stieltjes property, or arbitrary-depth complexity.

A subsequent exact-arithmetic audit applies the Section 10 output-coordinate transformation to this recurrence prefix. It obtains

\[
(\mu_0,\mu_1,\mu_2,\mu_3)
\approx
(346.99795737,\ 1.226906684,\ 0.02023946186,\ 0.0004265435132)
\]

and

\[
\det H_1\approx5.517751912>0,
\qquad
\det H_1^+\approx1.136932709\times10^{-4}>0.
\]

Thus \(H_0,H_0^+,H_1,H_1^+\) are all positive definite: every Stieltjes condition decidable from \(J_1,\ldots,J_9\) passes. Direct series reversion and an independent triangular solve of \(F'=\kappa_Q(F)\) agree exactly, and I reran that audit and its three tests. This conclusion is conditional on the depth-three recurrence representing the network limit. It is also only a four-moment pass: \(\mu_4,H_2\) need \(J_{11}\), while \(\mu_5,H_2^+\) need \(J_{13}\). It neither enters nor strengthens the distinct two-hidden-layer canonical moment sequence in Section 10.

The broader quadratic compiler is not a generic MLP compiler. It omits general activations, arbitrary batch/depth, conditional weight--activation attachments outside this grammar, biases, concentration, fluctuation laws, and positive-time evolution. Its chief value is that it turns previously conditional fixed-order coefficients in the older quadratic report into exact annealed formal-jet data.

### 8.8 What peeling contributes to the central PDE question

Peeling supplies the most explicit available local account of shared-matrix response. In the audited fixed-order families, the needed information is not an arbitrary history but a finite registry of forward, reverse, tangent, and fresh Gaussian channels. That makes finite causal closure plausible; a universal terminating normal-form compiler remains open.

It does not yet show that the registry size stays bounded as depth grows, that its Taylor series has positive radius, or that these local coefficients assemble into a global trajectory. The quadratic example proves that the last inference can fail dramatically. In the central residual-PDE branch, the likely use of peeling is therefore as a derivation and consistency tool for Onsager/source terms, not as a direct Taylor solver.

---

## 9. Quadratic nonclosure: what the negative laboratory really proves

quadratic_nonclosure asks whether a particularly simple one-source Taylor/Wick PDE can approximate all-time training in an unbounded square-activation network. The answer for that prescribed family is no. The answer for arbitrary finite causal closures is not known.

The older documents use the convention

\[
h_i^{(1)}=\frac12(z_i^{(1)})^2,\qquad
h_j^{(2)}=\frac12(z_j^{(2)})^2,
\qquad
W_{ji}\sim N(0,\lambda/n),
\]

with canonical \(\lambda=4/3\), output \(f_n=n^{-1}\sum_ja_jh_j^{(2)}\), target one, and µP flow multipliers \(n,1,n\) for first preactivations, middle weights, and readout. The later exact compiler instead uses raw squares, unit variance, and its own induced metric normalization. It contains the corresponding specialized/rescaled decorated-forest grammar, so it validates the relevant fixed-order annealed premise, but the two dynamical conventions should not be identified by a bare time rescaling. Every displayed numerical jet below is tied explicitly to its stated convention.

In the half-square convention, let

\[
q_n=\frac1n\sum_i(h_i^{(1)})^2,\qquad
\mathsf K_n=W\operatorname{diag}(h^{(1)})W^\top,\qquad
\upsilon=a\odot z^{(2)}.
\]

The feature-ascent drift contains

\[
D_+z^{(2)}=q_n\upsilon+2\mathsf K_n\upsilon.
\]

Although \(\mathsf K_n\succeq0\), \(\mathsf K_n\upsilon\) need not be coordinatewise positive. This is why a positive scalar subgrammar can prove a lower bound on the annealed jet but cannot be promoted to a componentwise comparison theorem for the fully trained vector dynamics.

### 9.1 A positive stability theorem that remains useful

Let \(F(\tau)\) be a monotone feature-ascent profile and convert feature time to physical squared-loss time by

\[
\dot\tau=2(1-F(\tau)),\qquad
\mathcal L(t)=(1-F(\tau(t)))^2.
\]

If two target-reaching feature profiles obey

\[
0<\mu\le F'\le\Lambda,\qquad
\|F-\widetilde F\|_\infty\le\varepsilon,
\]

then their clocks and losses satisfy

\[
\sup_{t\ge0}|\widetilde\tau(t)-\tau(t)|
\le\frac{\varepsilon}{\mu},
\]
\[
\sup_{t\ge0}|\widetilde{\mathcal L}(t)-\mathcal L(t)|
\le
2(1-f_0)\left(1+\frac\Lambda\mu\right)\varepsilon.
\]

So a small, residual-compatible feature-profile error does not accumulate indefinitely.

At finite width, with \(C_n=n^{-1}\|a\|^2\),

\[
f_n^2\le C_n\kappa_n,\qquad
\dot C_n=4f_n(1-f_n).
\]

After reaching any fixed positive subtarget \(a_\ast\), this supplies a trajectory-dependent lower bound on \(\kappa_n\), exponential residual decay, and finite remaining feature time.

This is a conditional stability module, not a closure construction. Uniform positive entry, a width-independent burn-in, and a small hierarchy defect have not been proved. Negative-output dead-feature basins exist at finite width.

### 9.2 Exact factorial growth

Let

\[
c_k=\lim_{n\to\infty}
\mathbb E\!\left[\frac{D_{+,n}^kf_n(0)}{k!}\right]
\]

in the fixed-order width-first sense, where \(D_{+,n}\) is the historical half-square model's µP feature-ascent derivation. The current raw-square compiler establishes these annealed coefficients through the exact block-weighted dictionary

\[
f_n=\frac{\lambda}{8}f^\circ,
\qquad
D_{+,n}=\frac18\bigl(\lambda D_a^\circ+\lambda D_u^\circ+D_W^\circ\bigr).
\]

Thus it is the same finite decorated-forest grammar specialized to a different block metric, not the equal-metric Family-Q generator \(D_n\).

The constants follow directly from the half-square normalization. Write the historical first hidden feature as \(h^{(1)}=u^{\odot2}/2\), set

\[
W^\circ=\sqrt{\frac n\lambda}\,W,
\qquad
z^\circ=\frac1{\sqrt n}W^\circ u^{\odot2},
\qquad
f^\circ=\frac1n\sum_i a_i(z_i^\circ)^2.
\]

Then \(W^\circ\) has unit-variance raw entries and

\[
z=Wh^{(1)}=\frac{\sqrt\lambda}{2}z^\circ,
\qquad
h^{(2)}=\frac12z^{\odot2}
=\frac\lambda8(z^\circ)^{\odot2},
\qquad
f=\frac\lambda8f^\circ.
\]

Here is the blockwise chain rule. Define the raw-square block derivations

\[
D_b^\circ=n\nabla_bf^\circ\cdot\nabla_b,
\qquad b\in\{a,u,W^\circ\}.
\]

The \(a,u\) coordinates are unchanged, so

\[
\nabla_af=\frac\lambda8\nabla_af^\circ,
\qquad
\nabla_uf=\frac\lambda8\nabla_uf^\circ.
\]

Their historical metric multipliers are both \(n\), giving \((\lambda/8)D_a^\circ\) and \((\lambda/8)D_u^\circ\). For the middle matrix,

\[
\nabla_Wf
=\frac\lambda8\sqrt{\frac n\lambda}\,\nabla_{W^\circ}f^\circ
=\frac{\sqrt{\lambda n}}8\nabla_{W^\circ}f^\circ,
\qquad
\nabla_W=\sqrt{\frac n\lambda}\nabla_{W^\circ}.
\]

Because the historical middle-matrix multiplier is one, its derivation on a raw-coordinate observable is \((1/8)D_W^\circ\). Equivalently, under feature ascent

\[
\dot W^\circ=\sqrt{\frac n\lambda}\dot W
=\frac n8\nabla_{W^\circ}f^\circ.
\]

Collecting the blocks gives

\[
D_{+,n}=\frac18
\bigl(\lambda D_a^\circ+\lambda D_u^\circ+D_W^\circ\bigr).
\]

Consequently, at every fixed order,

\[
\mathbb E[D_{+,n}^k f]
=\frac{\lambda}{8^{k+1}}
\mathbb E\!\left[
(\lambda D_a^\circ+\lambda D_u^\circ+D_W^\circ)^k f^\circ
\right].
\]

The unweighted raw-square first-derivative contributions of the three blocks are

\[
\mathbb E[D_a^\circ f^\circ]=27,
\qquad
\mathbb E[D_u^\circ f^\circ]=48,
\qquad
\mathbb E[D_W^\circ f^\circ]=36.
\]

Therefore the historical first jet is

\[
J_1^{\rm half}
=\frac\lambda{64}(75\lambda+36),
\qquad
J_1^{\rm half}\big|_{\lambda=4/3}=\frac{17}{6},
\]

whereas the equal-metric raw-square value is \(27+48+36=111\). This gives a direct check of the dictionary and also explains why one cannot convert all quoted jets by multiplying by a single positive constant: the output normalization and the relative parameter metric both change.

A positive subgrammar selects the scalar vector field

\[
\mathscr D_0
=\frac{z^2}{2}\partial_a+qaz\,\partial_z,
\qquad
g=\frac12az^2.
\]

The ray \(z=\sqrt{2q}\,a\) is invariant, and along it

\[
g(\tau)=\frac{q}{(1-q\tau)^3}.
\]

Consequently, for odd \(k\),

\[
\frac1{k!}\mathscr D_0^kg(1,\sqrt{2q};q)
=q^{k+1}\binom{k+2}{2}.
\]

The factorial in the lower bound comes from the Gaussian expectation, not from this invariant-ray coefficient by itself. Put

\[
P_k(a,z;q)=\frac1{k!}\mathscr D_0^kg(a,z).
\]

Every application of \(\mathscr D_0\) raises total polynomial degree by one and flips the parity of the \(a\)-power. Since \(g\) has degree three, an odd \(k\) leaves only even monomials of total degree \(k+3\):

\[
P_k(a,z;q)=\sum_{u+v=m}p_{uv}(q)a^{2u}z^{2v},
\qquad
m=\frac{k+3}{2},
\qquad p_{uv}(q)\ge0.
\]

Let \(A\sim N(0,1)\), \(Z\sim N(0,\lambda q_0)\) be independent. For \(u+v=m\),

\[
\begin{aligned}
\mathbb E[A^{2u}Z^{2v}]
&=(2u-1)!!(2v-1)!!(\lambda q_0)^v\\
&\ge u!\,v!\,(\lambda q_0)^v\\
&\ge \frac{m!}{2^m}(\lambda q_0)^v.
\end{aligned}
\]

To make one bound cover both \(u\)- and \(v\)-heavy endpoints, define

\[
b_\lambda=\frac12\min\{1,\lambda/2\}.
\]

Then

\[
\mathbb E[A^{2u}Z^{2v}]
\ge m!b_\lambda^m(2q_0)^v.
\]

Multiplying by the nonnegative \(p_{uv}(q_0)\), summing, and using the invariant-ray identity

\[
\sum_{u+v=m}p_{uv}(q_0)(2q_0)^v
=q_0^{k+1}\binom{k+2}{2}
\]

produces the claimed factorial bound. The role of each factor is now visible: \(m=(k+3)/2\) is degree/parity counting, \(m!\) is Gaussian even-moment growth, and \(b_\lambda^m\) is the uniform loss incurred in comparing all \((u,v)\) allocations.

In primitive Gaussian coordinates, the full readout and feature-ascent vector field have nonnegative polynomial coefficients. Differentiation preserves this cone, and Gaussian Wick expectation is nonnegative on the surviving even monomials. The selected branch therefore cannot be canceled by the omitted histories. With \(m=(k+3)/2\),

\[
c_k\ge
m!\,b_\lambda^m q_0^{k+1}\binom{k+2}{2},
\qquad
q_0=\frac34,\qquad
b_\lambda=\frac12\min\{1,\lambda/2\}.
\]

Hence

\[
\limsup_{k\to\infty}c_k^{1/k}=\infty.
\]

The formal annealed feature series has radius zero. The same is true of its formal physical-loss jet.

The exact claim is narrower than “training blows up”: the result concerns the separately fixed derivative sequence. It does not prove concentration of the random derivatives, interchange of the width limit with a positive time interval, or existence of a smooth limiting trajectory with this jet. If such a curve exists, it is nonanalytic at initialization.

### 9.3 Failure of the prescribed Taylor source PDE

The proposed one-source transport closure used

\[
U_t=2(1-U(t,0))U_s
\]

with truncated initial profile

\[
F_M(s)=\sum_{k=0}^M c_ks^k.
\]

Because the relevant \(c_k\) are nonnegative and have zero radius,

\[
F_M(s)\to+\infty
\qquad\text{for every }s>0.
\]

For any subtarget \(y\in(0,1)\), its first source hitting coordinate tends to zero, so the physical hitting time tends to zero. The induced losses converge pointwise to the discontinuous step

\[
\mathcal L_\infty(t)=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
\]

Therefore the family is not uniformly Cauchy on any interval containing zero and cannot shadow one common continuous target.

This disproves the prescribed positive Wick--Taylor family. It does not cover a diagonal cutoff \(M(n)\), signed coefficients, rational or other non-Taylor compilers, operator-valued states, or an independently constructed positive-time real-axis dynamics.

### 9.4 Further scoped no-go results

The same formal jet rules out several tempting architectures.

1. A bounded analytic vector field and analytic readout on one Banach space would give a positive Taylor radius by the analytic ODE theorem; it cannot reproduce this jet.
2. On an ordered Banach completion, a positive strongly continuous semigroup that preserves the primitive cone, has its generator defined on every \(D_{+,n}^kf\), and admits a continuous positive extension of the Wick readout has positive Taylor remainders, so its partial sums diverge from below. Positivity of an arbitrary \(C_0\)-semigroup alone is not enough.
3. Any coefficientwise nonnegative polynomial compiler consistent at every fixed order diverges at every positive feature time.
4. Explicit Euler/Wick and the stated positive-stage polynomial schemes inherit the same lower bound.
5. The complete smooth jet cannot select a real-axis curve: adding a flat term such as \(e^{-1/t^2}\) changes positive-time behavior without changing any derivative at zero.

Three further witnesses sharpen the scope.

6. On the exact finite-width symmetric manifold
   \[
   z_i^{(1)}=\zeta,\qquad a_j=a,\qquad W_{ji}=w/n,
   \]
   feature ascent reduces to
   \[
   f=\frac18aw^2\zeta^4,\quad
   a'=\frac18w^2\zeta^4,\quad
   w'=\frac14aw\zeta^4,\quad
   \zeta'=\frac12aw^2\zeta^3.
   \]
   At
   \[
   a(0)=-1,\qquad w(0)=2,\qquad\zeta(0)=\sqrt8,
   \]
   the invariants \(w^2-2a^2=2\) and \(\zeta^2-4a^2=4\) reduce the dynamics to
   \[
   a'=4(1+a^2)^3,
   \qquad
   f=4a(1+a^2)^3.
   \]
   Backward from \(a=-1\), the real solution blows up after feature-time distance
   \[
   B=\int_1^\infty\frac{ds}{4(1+s^2)^3}\le\frac1{64}.
   \]
   A real singularity is also a singularity of the analytic continuation, so the Taylor radius at initialization is at most \(B\). Forward, even reaching \(a=0\)—before the point where \(f=1\)—takes
   \[
   \int_0^1\frac{ds}{4(1+s^2)^3}\ge\frac1{32}.
   \]
   Thus the forward fitting time exceeds the initialization Taylor disk even though residual-gated real-time fitting is regular. This refutes the proof strategy “real target fitting supplies a large enough analytic disk,” not typical-Gaussian mean-field behavior and not real-axis approximation by non-Taylor methods.
7. In the frozen-first-layer subsystem \(u'=qv^2,\ v'=quv\), particles near a Gaussian cutoff \(R_c\) become singular before feature time \(1/(qR_c)\). Convergence of truncated initial laws in Wasserstein distance or finitely many moments therefore does not imply convergence of the evolved laws. This exact warning does not transfer automatically to the fully trained model, whose positive-semidefinite matrix term \(\mathsf K_n(a\odot z)\) has no coordinatewise sign.
8. At formal reuse depth \(r\), the noncommutative compiler can generate \(2^r\) ordered words, suggesting more continuation information than a bounded-filtration commuting-source jet can encode. This becomes a capacity obstruction only if fixed-degree freeness/faithfulness and a branch-separating positive-time continuation theorem are proved. Neither is available, so it is a conditional research direction, not a no-go theorem.

Each statement has escape routes: unbounded generators, scales of spaces, signed/nonlocal evolution, implicit or tamed schemes, and independently certified nonanalytic continuations.

Two topology warnings are also exact. Product \(L^2\) does not control the cubic readout: spikes can converge to zero in \(L^2\times L^2\) while \(\mathbb E[az^2]\) stays fixed. And any Banach function space continuously embedded in \(L^1\) with globally bounded multiplication embeds in \(L^\infty\), so it cannot contain a nondegenerate Gaussian coordinate. A useful theory likely needs weighted scales, restricted reachable sets, or unbounded/renormalized products.

### 9.5 A conditional DMFT claim, not a network theorem

The tagged-site study postulates a Volterra representation

\[
z(t)=\xi(t)+\int_0^t r(s)M(t,s)a(s)z(s)\,ds,
\qquad
\dot a=r z^2,
\]

with a nondegenerate Gaussian process \(\xi\), independent Gaussian \(a(0)\), deterministic causal \(M\), a positive initial response, and an output lower bound involving \(\mathbb E[z^4]\).

On a positive-probability extreme-readout event, comparison with

\[
b'=cv^2,\qquad v'=cm\,bv
\]

forces the putative classical solution to reach any subtarget with zero delay. The comparison is as follows. Continuity and the assumed positive initial response \(M(0,0)>0\) give numbers \(m,\delta_0>0\) such that

\[
M(t,s)\ge m
\qquad(0\le s\le t\le\delta_0).
\]

The needed persistence event follows from a more precise assumption than generic process nondegeneracy. Since \(\xi(0)\) is a nondegenerate Gaussian, \(\mathbb P\{\xi(0)\ge2z_*\}>0\). Almost-sure path continuity gives

\[
\sup_{0\le t\le\delta}|\xi(t)-\xi(0)|\longrightarrow0
\quad\text{a.s. as }\delta\downarrow0.
\]

After shrinking \(\delta_0\) if necessary, the event

\[
\left\{\xi(0)\ge2z_*,\qquad
\sup_{0\le t\le\delta_0}|\xi(t)-\xi(0)|\le z_*\right\}
\subseteq
\left\{\inf_{0\le t\le\delta_0}\xi(t)\ge z_*\right\}
\]

has positive probability.

Call the probability of this cavity-persistence event \(p_\xi>0\). Intersect it with the independent extreme-readout event \(a(0)\ge A\), and define the **joint** probability

\[
p_A:=p_\xi\,\mathbb P\{a(0)\ge A\}>0.
\]

If the macroscopic output has not yet reached a chosen subtarget \(y<1\), then its residual satisfies \(r(t)=1-f(t)\ge c:=1-y\). Positivity of \(M,r,a,z\) on this joint event turns the Volterra equations into the lower integral inequalities

\[
a(t)\ge A+c\int_0^t z(s)^2\,ds,
\qquad
z(t)\ge z_*+cm\int_0^t a(s)z(s)\,ds.
\]

The cooperative comparison system with \(b(0)=A,v(0)=z_*\),

\[
b'=cv^2,\qquad v'=cm\,bv,
\]

therefore gives a componentwise lower solution. It has the invariant

\[
v^2-z_*^2=m(b^2-A^2).
\]

For \(A>z_*/\sqrt m\), writing \(\alpha=(A^2-z_*^2/m)^{1/2}\), one obtains

\[
b'=cm(b^2-\alpha^2),
\qquad
T_A=\frac1{2cm\alpha}
\log\frac{A+\alpha}{A-\alpha}
=O\!\left(\frac{\log A}{A}\right).
\]

Thus the lower solution blows up at a time tending to zero as \(A\to\infty\). The postulated output kernel also satisfies \(\kappa(t)\ge\tfrac14\mathbb E[z(t)^4]\); on the event above, \(\dot f=2r\kappa\ge(c/2)p_Av^4\), whose integral diverges at \(T_A\). The assumption that \(f<y\) until then is impossible. Since arbitrarily large \(A\) still has positive Gaussian probability, no positive delay before reaching \(y\) is compatible with all the postulates. This most naturally indicates that the collection of postulated equations cannot support an output continuous at initialization.

The finite-network calculation checks only an instantaneous response coefficient. It does not derive the Volterra law, prove self-consistency, construct a positive-time solution, or identify a network limit. A discontinuous zero-loss-for-\(t>0\) trace is selected only after adding a separate relaxed monotone/no-overshoot axiom. That step trace is therefore doubly conditional.

### 9.6 Normalized variants

True across-width RMS normalization after both square activations changes the local jet. In the half-square convention at \(\lambda=4/3\), write

\[
F(\tau)=J_1\tau+\frac{J_3}{3!}\tau^3+O(\tau^5).
\]

Then

\[
\begin{array}{c|cc}
\text{model}&J_1&J_3\\ \hline
\text{raw}&17/6&229957/216\\
\text{global readout weight normalization}&17/6&223939/216\\
\text{RMS normalization}&34/9&-273712/729.
\end{array}
\]

The RMS cubic sign reversal shows that the raw positive-cone proof cannot be transferred.

In frozen reductions let \(M_{p,r}=\mathbb E[a^pz^r]\). The exact moment hierarchies escape every finite degree or rectangular cutoff. For RMS normalization set

\[
S_{\rm rms}^2=M_{0,4},
\qquad
f=\frac{M_{1,2}}{S_{\rm rms}}.
\]

Then

\[
\dot M_{p,r}
=\frac p{S_{\rm rms}} M_{p-1,r+2}
+\frac{2r}{S_{\rm rms}}M_{p+1,r}
-\frac{2rf}{S_{\rm rms}^2}M_{p,r+2},
\]

and for readout weight normalization \(q=3/4\), \(f=\tfrac12M_{1,2}\), and

\[
\dot M_{p,r}
=\frac p2M_{p-1,r+2}
-pfM_{p,r}
+rqM_{p+1,r}.
\]

This proves non-invariance of those natural monomial cutoffs. It is not a lower bound on all possible sufficient statistics or a theorem against operator compression. Zero radius has not been proved for the normalized models, and the hidden-row direction-only transfer requires an additional large-fan-in assumption.

### 9.7 The right lesson for the main project

The negative laboratory eliminates a particular strategy:

\[
\text{exact fixed-order positive Wick coefficients}
\not\Rightarrow
\text{convergent positive Taylor closure}.
\]

It does not eliminate the operator PDE, whose activation is bounded, whose state is signed and measure-valued, and whose approximation parameter is source dependence rather than time-Taylor order. Its constructive contribution is methodological: demand a real-axis state equation, a non-oracular compiler, a residual/consistency norm, and a stability theorem, rather than relying on a formal jet alone.

---

## 10. The Stieltjes program: a non-Taylor route through a scalar kernel

The Stieltjes study takes the exact quadratic jet seriously while accepting that its Taylor series diverges. Its question is whether a nonlinear change of coordinate exposes a positive resolvent whose rational approximants remain meaningful on the real training path.

### 10.1 Output-coordinate kernel

Let \(F(s)\) denote the formal feature-ascent output and suppose locally that an actual \(F\) exists and is invertible. Define

\[
\kappa_Q(y)=F'\!\left(F^{-1}(y)\right).
\]

Then \(F'=\kappa_Q(F)\), and, after rescaling physical time so that the learning-rate multiplier is \(\eta=1\), one-sample squared-loss flow is the scalar time change

\[
\frac{dy}{dt}=2(1-y)\kappa_Q(y),\qquad
\mathcal L=(1-y)^2.
\]

Readout reflection makes \(F\) odd, so \(\kappa_Q\) is even. Write

\[
\kappa_Q(y)=J_1+\sum_{r\ge0}g_{r+1}y^{2r+2},
\qquad J_1=111,
\]

and define

\[
\mathscr R_Q(x)=\frac{\kappa_Q(\sqrt x)-J_1}{x}
=\sum_{r\ge0}(-1)^r\mu_rx^r.
\]

Why target this alternating form? The historical record is empirical first and structural second. Exact series reversion of the all-positive raw jet produced

\[
g_1=68.3866569\ldots,
\quad g_2=-6.84424988\ldots,
\quad g_3=2.93513360\ldots,
\quad g_4=-1.59703499\ldots,
\]

and the same alternation continued through every available coefficient. The repository contains no pre-computation derivation of a positive neural operator whose spectral measure had to generate these signs. Thus the Stieltjes ansatz began as an exact finite-prefix pattern discovered **after** the output-coordinate inversion; the later positive-operator representation is an equivalent consequence if all moment gates hold, not an independent neural proof of them.

There are nevertheless principled reasons to test this particular pattern rather than an arbitrary rational fit. The zero-radius obstruction applies to \(F(s)\) in feature time, whereas one-sample squared-loss dynamics depends only on the output-coordinate speed \(\kappa_Q(y)\). Inverting the monotone output can regularize a singular time parametrization. Stieltjes transforms are completely monotone on the positive axis, possess sign-controlled Gaussian/Radau rational approximants, and turn finite moments into certified real-axis bounds. These properties are exactly what the failed positive Taylor closure lacked. They make the conjecture mathematically natural **conditional on the observed signs**, but still post hoc and model-specific until V1 and V3 are proved.

The canonical Stieltjes conjecture is

\[
\mathscr R_Q(x)=\int_0^\infty\frac{\rho(d\lambda)}{1+\lambda x}
\]

for some finite nonnegative measure \(\rho\). Equivalently, for every \(d\),

\[
H_d=(\mu_{i+j})_{i,j=0}^d\succeq0,
\qquad
H_d^+=(\mu_{i+j+1})_{i,j=0}^d\succeq0.
\]

Indeed,

\[
c^\top H_dc=\int p(\lambda)^2\,d\rho,\qquad
c^\top H_d^+c=\int\lambda p(\lambda)^2\,d\rho.
\]

For \(J_k=F^{(k)}(0)\), series reversion gives

\[
\mu_0=\frac{J_3}{2J_1^2},
\]
\[
\mu_1=\frac{4J_3^2-J_1J_5}{24J_1^5},
\]
\[
\mu_2=\frac{J_1^2J_7-26J_1J_3J_5+70J_3^3}{720J_1^8}.
\]

This transformation is the heart of the conjecture. Positive raw derivatives do not automatically give positive \(\mu_r\), because series inversion introduces cancellations.

There are three distinct claims:

1. **V1, existence:** all Hankel conditions hold, hence at least one representing \(\rho\) exists.
2. **V2, determinacy:** the moments select a unique \(\rho\).
3. **V3, neural identification:** the resolvent selected by \(\rho\) equals an independently constructed positive-time infinite-width neural kernel.

V1 does not imply V2, and V1--V2 do not imply V3. Since the raw jet has zero radius, equality of all right derivatives is especially far from global identification.

There is an exact inverse-variable reformulation. With \(G=F^{-1}\),

\[
H_Q(x)=G'(\sqrt x)=\frac1{\kappa_Q(\sqrt x)}
=\sum_{r\ge0}(-1)^rh_rx^r.
\]

The Stieltjes condition for the \(\mu_r\) sequence is equivalent, through the associated continued-fraction transform, to the corresponding moment condition for \(h_r\).

The correspondence is the classical **formal Stieltjes S-fraction**. In the nondegenerate case, a Stieltjes moment series has a unique formal continued fraction with nonnegative coefficients. Write

\[
H_Q(x)
=\frac{h_0}{\displaystyle
1+\frac{\beta_1x}{\displaystyle
1+\frac{\beta_2x}{\displaystyle
1+\frac{\beta_3x}{\ddots}}}},
\qquad h_0=\frac1{J_1}.
\]

Since \(H_Q^{-1}=J_1+x\mathscr R_Q\), elementary inversion gives

\[
\mathscr R_Q(x)
=\frac{\beta_1/h_0}{\displaystyle
1+\frac{\beta_2x}{\displaystyle
1+\frac{\beta_3x}{\ddots}}}.
\]

Thus passing between \(H_Q\) and \(\mathscr R_Q\) prepends or deletes the first positive S-fraction coefficient. Nonnegativity of the \(\beta_j\) is equivalent to positivity of the ordinary and shifted Hankel forms; terminating fractions handle degenerate finite-support cases. This is a statement about **formal moment sequences** and requires no uniqueness of a representing measure. Determinacy enters only when one asks whether the infinite moments select one global resolvent.

If

\[
H_Q(x)=\int_0^\infty\frac{\sigma(d\lambda)}{1+\lambda x},
\]

then integrating \(G'(y)=H_Q(y^2)\) gives the formal real-axis representation

\[
G(y)
=
\int_0^\infty
\frac{\arctan(y\sqrt\lambda)}{\sqrt\lambda}
\,\sigma(d\lambda),
\]

with the \(\lambda=0\) integrand interpreted as \(y\). This is a conditional reconstruction from a representing measure, not an independently established neural inverse curve.

The Hankel conditions also have an exact positive-operator interpretation. Let \(L(\lambda^r)=\mu_r\), quotient polynomials by the null space of \(\langle p,q\rangle=L(pq)\), and complete. Multiplication by \(\lambda\) is a densely defined nonnegative symmetric operator; its Friedrichs extension \(A_{\mathrm{op}}\ge0\) yields

\[
\mathscr R_Q(x)=\langle v,(I+xA_{\mathrm{op}})^{-1}v\rangle,
\qquad
\mu_r=\langle v,A_{\mathrm{op}}^rv\rangle.
\]

Conversely, such a positive operator and cyclic vector give both Hankel families. This is an equivalence at the formal-moment level. The obvious neural transport generator does not supply this operator. Let \(\theta\in\mathbb R^D\) collect the finite network parameters, let \(\gamma_D\) be standard Gaussian measure, and put

\[
X=n\nabla f\cdot\nabla
\]

on the polynomial core of \(L^2(\gamma_D)\). Here \(n\) is the network-width/µP multiplier; \(D\), not \(n\), is the ambient parameter dimension. Gaussian integration by parts gives, for a vector field \(v\),

\[
(v\cdot\nabla)^*
=-v\cdot\nabla-\operatorname{div}v+\theta\cdot v.
\]

Taking \(v=n\nabla f\), and using that the raw-square output is homogeneous of total degree seven, so \(\theta\cdot\nabla f=7f\), yields

\[
X^\ast=-X+n(7f-\Delta f),
\]

with the last term acting by multiplication. Therefore

\[
\frac{X+X^*}{2}=\frac n2(7f-\Delta f)
\]

is not positive: readout reflection \(a\mapsto-a\) changes its sign. The neural Hessian is likewise sign-indefinite. The positive Friedrichs operator above, if it exists, is consequently a reconstructed moment operator, not this obvious feature-ascent generator in disguise.

Finally, zero radius forces any canonical representing measure to have unbounded support. Compact support would make \(\mathscr R_Q\) and \(\kappa_Q\) analytic near zero, and the scalar ODE \(F'=\kappa_Q(F)\) would then have an analytic local solution, contradicting the proved formal jet growth. This implication remains conditional on V1; zero radius alone does not construct a measure.

### 10.2 The exact canonical prefix

The raw-square quadratic compiler gives

\[
\begin{array}{c|r}
k&F^{(k)}(0)\\ \hline
1&111\\
3&1\,685\,184\\
5&77\,400\,633\,120\\
7&7\,315\,868\,433\,079\,296\\
9&1\,181\,161\,141\,825\,400\,561\,664\\
11&291\,982\,832\,387\,585\,872\,335\,470\,592\\
13&102\,853\,512\,279\,246\,664\,353\,620\,526\,022\,656\\
15&49\,079\,184\,579\,077\,107\,476\,764\,629\,402\,991\,788\,032\\
17&30\,555\,969\,894\,096\,099\,495\,444\,855\,650\,521\,777\,374\,167\,040.
\end{array}
\]

The corresponding transformed moments are approximately

\[
(\mu_0,\ldots,\mu_7)
=
(68.38665693,\,
6.844249882,\,
2.935133601,\,
1.597034989,\,
0.9797782744,\,
0.6459122908,\,
0.4467790662,\,
0.3198650334).
\]

Every principal minor of both \(H_3\) and \(H_3^+\) is strictly positive; in particular,

\[
\det H_3=0.0700966182\ldots,\qquad
\det H_3^+=2.85006977\times10^{-5}.
\]

Thus every Stieltjes condition decidable from eight moments passes. The next new leading gate is ordinary \(H_4\), requiring \(\mu_8\) and hence \(F^{(19)}(0)\); the frozen computation stopped at order 17.

Orders 15 and 17 were reproduced by two isolated exact implementations using different sparse representations and Wick engines. This is strong implementation evidence, not machine-checked formal verification: both routes share the same mathematically derived Gaussian-program recurrence.

### 10.3 What the deformation campaigns teach

| Substudy | Setup and result | Correct interpretation |
|---|---|---|
| Relative hidden metric | \(D_\lambda=D_a+\lambda(D_u+D_W)\), \(\lambda\ge0\). Output through order 9; ordinary and shifted \(2\times2\) gates pass over the full ray. The first-hidden norm obeys \(D_\lambda Q_1=8\lambda f\); \(Q_2\) supplies a separate low-order companion. | Exact continuum-valued finite-prefix pass. \(Q_1\) is inherited, not independent confirmation. |
| Two inputs | Equal-norm correlated inputs, \(t=\theta^2\in[0,1]\), equal- and opposite-label symmetry channels. Exact through order 7; \(\mu_0,\mu_1,\mu_2\) and ordinary \(H_1\) pass over the interval. | Finite-prefix, one symmetry-reduced two-input setting; no all-order or shifted-\(H_1\) conclusion. |
| Centered square | \(\phi_c(u)=u^2-c,\ 0\le c\le2\). Exact rational Sturm certificates give positive \(\mu_0,\mu_1,\mu_2,\det H_1\). | A genuine shape deformation that passes only through the available order. |
| Independent block metric | \(D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W\). The full quadrant passes \(\mu_0,\ldots,\mu_3,H_1,H_1^+\) through order 9. | This attractive uniform pattern is later disproved at order 13 on \(\beta=1\). |
| Three inputs | Equicorrelation \(\rho\in[-1/2,1]\), equal labels, symmetric output channel. Exact through order 5, including a triangle invariant; \(\mu_0,\mu_1>0\). | The order-7 job hit its 1,800-second cap. There is no \(\mu_2\) or Hankel determinant, so this is not a Hankel pass. |
| Three hidden raw-square layers | One input, equal widths, candidate nested-detransposition jet through \(J_9\); \(\mu_0,\ldots,\mu_3>0\), \(H_1,H_1^+\succ0\). | Exact four-moment compatibility inside the audited recurrence; the recurrence-to-network width-limit theorem is unstated, and \(H_2,H_2^+\) are unavailable. |
| Smooth activation | Normalized \(\sin x\), same architecture and equal metric: \(J_1=4.037096946\ldots\), \(J_3=-103.2573311\ldots\), \(J_5=29944.43234\ldots\). | \(\mu_0=-3.167761986\ldots\), \(\mu_1=-3.039997378\ldots\). This exactly disproves universality over smooth bounded activations, not the canonical square case. |

The table illustrates why finite prefixes cannot be extrapolated casually: the independent-block metric passed over an entire quadrant through four moments, then failed at the next genuinely new shifted determinant.

### 10.4 Exact counterexamples to the uniform extensions

For this deformation the feature generator is

\[
D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W.
\]

Thus \(\alpha\) multiplies the learning metric of the first hidden coordinate \(u\), \(\beta\) multiplies the middle-weight metric, and the readout coefficient is fixed to one. The canonical raw-square equal-metric model is literally \((\alpha,\beta)=(1,1)\). On the ray \(\beta=1\), the complete order-13 jet gives

\[
\Delta(\alpha)
=\det(\mu_{i+j+1}(\alpha))_{i,j=0}^2
=
\frac{55296\,P_{36}(\alpha)}
{2358125(63+48\alpha)^{33}},
\]

where \(P_{36}\) has negative constant and linear coefficients and positive higher coefficients. Exact interval and convexity certificates prove

\[
\Delta(\alpha)<0
\qquad(0\le\alpha\le0.01).
\]

Therefore \(0<\alpha\le0.01\) supplies strictly positive three-block-training counterexamples: the architecture, initialization, and output are unchanged, and all three blocks still train, but the first-hidden block moves much more slowly. The failure is not an artifact of freezing a layer; \(\alpha=0\) is merely the analytically useful boundary.

There is one positive root

\[
\alpha_\ast=0.017519225541486\ldots.
\]

For the six-moment prefix, \(H_2^+\) is indefinite below \(\alpha_\ast\), singular at it, and all available leading gates pass above it. This is not an all-order phase diagram for \(\alpha>\alpha_\ast\), and there is no order-13 classification over the full \((\alpha,\beta)\) quadrant. Canonical \(\alpha=1\) remains in the passing region.

At the boundary \((\alpha,\beta)=(0,1)\), the first layer freezes. With

\[
m_n=\frac1n\sum_ju_j^4,\qquad v_i=z_i/\sqrt{m_n},
\]

the system reduces, after a positive time/output rescaling, to the conventional shallow raw-square network

\[
g_n=\frac1n\sum_i a_iv_i^2,
\qquad
a_i'=v_i^2,\qquad v_i'=2a_iv_i.
\]

Its shifted \(3\times3\) Hankel determinant is an exact negative rational. Yet each neuron is integrable:

\[
c=a^2-\frac12v^2,\qquad
D''=4cD,\qquad
a=-\frac{D'}{2D},\qquad
v=\frac{v_0}{D}.
\]

This is a crucial qualification: failure of Stieltjes positivity does not imply absence of a low-dimensional characteristic representation. It only kills this positive-resolvent mechanism. For Gaussian initialization, positive-measure characteristics hit poles before any fixed positive feature time, so an ordinary global population expectation is still not constructed.

### 10.5 Hidden observables

For \(Q_1=n^{-1}\sum u_j^2\) and \(Q_2=n^{-1}\sum z_i^2\), express the responses in output coordinates:

\[
N_j(y)=Q_j(F^{-1}(y)),\qquad
\frac{N_j(\sqrt x)-N_j(0)}x
=\sum_{r\ge0}(-1)^r\nu_r^{(j)}x^r.
\]

Two exact recurrences agree through \(Q_2^{(16)}(0)\), while the Ward identity provides \(Q_1^{(18)}(0)\). The first-hidden squared-RMS response has nine moments with \(H_4\succ0,H_3^+\succ0\); the second-hidden response has eight moments with \(H_3\succ0,H_3^+\succ0\). Literal RMS, obtained by square root, also passes every accessible principal minor.

These are exact finite-prefix passes. \(Q_1\) is algebraically inherited from the output and should not be counted as independent confirmation. \(Q_2\) is genuinely separate but remains open at all orders.

### 10.6 Positive variance boundary, but no monotone homotopy proof

Let \(\upsilon=\sigma_{\rm mid}^2\) denote middle-weight initialization variance and normalize

\[
f_\upsilon(s)=\frac{F_\upsilon(s)}\upsilon,\qquad
\widehat\kappa_\upsilon(z)=\frac{\kappa_{Q,\upsilon}(\upsilon z)}\upsilon,
\]

where \(\kappa_{Q,\upsilon}(y)=F_\upsilon'(F_\upsilon^{-1}(y))\) is the unscaled output-coordinate kernel; equivalently \(\kappa_{Q,\upsilon}(y)=\upsilon\widehat\kappa_\upsilon(y/\upsilon)\). At the rescaled boundary \(\upsilon\downarrow0\),

\[
f_0(s)=36s\,e^{72s^2},
\]

and the inverse kernel can be written with Lambert \(W\). This formula comes from an exact variance-sector expansion, not from simply setting the middle matrix to zero in the unscaled network. For \(r\ge0\),

\[
F_\upsilon^{(2r+1)}(0)
=\sum_{P=1}^{2r+2}C_{r,P}\upsilon^P.
\]

Dividing by \(\upsilon\) and taking \(\upsilon\downarrow0\) retains only the one-pair sector \(P=1\), whose exact coefficient is

\[
C_{r,1}=36\frac{(2r+1)!}{r!}72^r.
\]

Therefore

\[
f_0(s)
=\sum_{r\ge0}\frac{C_{r,1}}{(2r+1)!}s^{2r+1}
=36s\sum_{r\ge0}\frac{(72s^2)^r}{r!}
=36s e^{72s^2}.
\]

It is a singular, variance-rescaled boundary flow. The resulting normalized transform \(\mathscr R_{Q,0}\) is genuinely Stieltjes with compact support \([0,e/9]\).

However, the first variation of the measure/moment structure is signed, and a Jacobi continued-fraction coordinate decreases. Thus neither “increase variance by adding a positive measure” nor coordinatewise monotonicity of the Jacobi coefficients can prove the canonical case.

There is intriguing exact combinatorics. The aggregated matrix

\[
\mathsf C=(C_{r,P})_{0\le r\le5,\,1\le P\le12}
\]

has six rows for derivative orders \(1,3,5,7,9,11\) and twelve columns for the powers of \(\upsilon\), equivalently the number of selected middle-covariance/Wick-pair sectors; entries beyond the allowable sector count are zero. All

\[
\sum_{k=1}^6\binom6k\binom{12}k=18,563
\]

square minors are nonnegative, and its six normalized row polynomials have simple negative roots. This is a finite-order statement about the **pre-inversion sector coefficients**, not a Hankel theorem for the nonlinearly transformed \(\mu_r\). A scaled-Pascal witness with a negative inverse moment has total nonnegativity and real negative roots but a repeated root; it therefore refutes that weaker package under nonlinear series inversion, not the stronger package that includes simple roots. The neural simple-root pattern remains suggestive and unproved. Local decorated transition matrices also have negative minors. Any canonical positivity proof must use a nonlocal architecture-specific relation among sectors, not positivity of raw ingredients.

### 10.7 Conditional quadrature and rational dynamics

The first five canonical moments determine a two-node Gaussian rule

\[
\begin{array}{c|cc}
\lambda&0.0272630&0.5519349\\ \hline
\text{weight}&58.89535&9.49131
\end{array}
\]

and a three-node zero-Radau rule

\[
\begin{array}{c|ccc}
\lambda&0&0.2133933&0.6582709\\ \hline
\text{weight}&46.81094&16.54032&5.03540.
\end{array}
\]

If a representing measure exists, Hermite-interpolation error signs give

\[
\mathscr R_{\mathrm G}(x)\le \mathscr R_\rho(x)\le \mathscr R_{\mathrm R}(x),
\qquad x\ge0.
\]

At \(x=1\),

\[
63.4480873\le \mathscr R_\rho(1)\le63.4789321.
\]

The kernel ordering transfers to feature and physical-loss flows through their hitting-time maps. If a unique neural kernel \(\kappa_Q\) exists on \(0\le y\le1\), \(a=\inf\kappa_Q>0\), \(M=\sup\kappa_Q\), and a rational approximation satisfies \(\|\kappa_{Q,N}-\kappa_Q\|_\infty=\epsilon_N<a\), then

\[
\sup_{t\ge0}|\mathcal L_N(t)-\mathcal L(t)|
\le
\frac{M}{ae}
\left[-\log\left(1-\frac{\epsilon_N}{a}\right)\right].
\]

The factor \(1/e\) and the logarithm are not fitted constants. Put \(\delta=\epsilon_N/a<1\). Since \(\kappa_Q\ge a\), uniform additive error implies the relative comparison

\[
(1-\delta)\kappa_Q
\le\kappa_{Q,N}
\le\frac1{1-\delta}\kappa_Q.
\]

Comparison of the scalar hitting-time equations then sandwiches the approximate loss between time-rescaled exact losses:

\[
\mathcal L\!\left(\frac{t}{1-\delta}\right)
\le\mathcal L_N(t)
\le\mathcal L((1-\delta)t).
\]

The exact loss satisfies

\[
\mathcal L'(t)=-4\kappa_Q(y(t))\mathcal L(t),
\qquad
\mathcal L(t)\le e^{-4at}.
\]

Consequently its derivative with respect to log-time obeys

\[
\left|\frac{d\mathcal L}{d\log t}\right|
=4t\kappa_Q(y(t))\mathcal L(t)
\le4Mt e^{-4at}
\le\frac{M}{ae},
\]

where the last step is \(xe^{-x}\le1/e\). The log-distance from \(t\) to either comparison time is at most \(-\log(1-\delta)\), which proves the displayed all-time bound.

Under the canonical Stieltjes representation the positivity assumption is concrete rather than mysterious:

\[
\kappa_Q(y)=111+y^2\mathscr R_Q(y^2),
\qquad
\mathscr R_Q(x)=\int\frac{\rho(d\lambda)}{1+\lambda x}\ge0.
\]

Hence one may take \(a=111\), while \(M\le111+\mu_0\) on \([0,1]\). The quadrature bounds give \(\mathscr R_Q(1)\approx63.45\), so \(\kappa_Q(1)\approx174.45\). The measure's necessarily unbounded support does not make this value infinite: \((1+\lambda)^{-1}\le1\) and \(\rho([0,\infty))=\mu_0<\infty\). All of this remains conditional on V1--V3.

This is the most concrete candidate in the repository for turning initialization-computable finite data into an all-time finite-dimensional closure. It is conditional on all-order positivity, determinacy, and neural identification.

At the exact Lambert-\(W\) boundary, the rational hierarchy was checked on 501 points up to \(y=0.99\). Successive sampled sup log-kernel errors fell from \(1.43\times10^{-1}\) to \(1.43\times10^{-7}\), and the deepest rational rule was about sixty times more accurate than the equal-information Taylor truncation on that grid. This validates the mechanism numerically on the sampled grid of an independently solvable boundary model; it is not a proved uniform rate or evidence for the canonical neural identification.

### 10.8 Numerical evidence and why none of it settles V1--V3

| Campaign | Main settings | Outcome |
|---|---|---|
| First direct Loewner | Widths \(64,128,256\); 96/64/32 antithetic pairs; RK4 \(10^{-3}\) and \(5\times10^{-4}\); nominal nodes \(0.02,0.04,0.06,0.08\). | Used feature time as if it were output. Many paths blew up before the nodes. Null for the intended output-coordinate Loewner test. |
| Corrected common clock | Widths/pairs \(64{:}140,128{:}70,256{:}70\); output nodes \(0.04,0.08,0.12,0.16\); RK4 \(5\times10^{-5}\), horizon \(0.003\); seven-block clipped median-of-means; 5,000 bootstraps. | No robust negative direction, but width-256 \(\mathscr R_Q(0)\) had \(14.18\%\) bias. The robust proxy was not calibrated to the target kernel. |
| Fresh local jets | Widths 128/256, 224 antithetic pairs each; positive-time successor used the same counts, RK4 \(5\times10^{-5}\), horizon \(0.003\), 5,000 bootstraps. | Held-out coefficients were contained, including \(-6.84425\) and \(2.93513\), but tiny Loewner signs reversed across fitting sensitivities. Local calibration pass; global conclusion inconclusive. |
| Canonical global pilot | Float64 RK4; (width, lineages) \(=(256,32),(512,16)\); nodes through \(0.99\); step \(2\times10^{-5}\), horizon \(0.024\); 2,000 lineage bootstraps. | At \(y=0.9\), the conservative band was \(82.67\) times wider than the resolution ceiling. A bitwise gate and a flawed \(y=0\) containment classifier also failed. Even after ignoring those brittle gates, the science remained under-resolved. |
| Bounded-readout DMFT | \(a_0\sim N(0,1)\mid |a_0|\le3\); proposed \(L=64,S=4096\) solver, Euler, proposal mixing, feature horizon \(0.005\). | Low-jet and reciprocal-response contacts passed, but the initialization tolerance and independent DMFT derivative gate did not. No positive-time DMFT curve was run. This is a changed, bounded-law toy model. |
| FP32 Euler | Canonical \(n=8192\), one antithetic lineage; \(h=10^{-5},5\times10^{-6}\). Breadth validation used \(n=4096\), centered/metric/variance cases, \(h=2\times10^{-5},10^{-5}\). | Aggregate kernels looked close, but realized parameter updates entered the FP32 rounding floor. Two of three breadth cases failed and triggered the hard stop. No Stieltjes inference. |
| FP64 successor | Same rounded initial tensors, FP64 evolution; local \(n=4096\) checks, then \(n=4096,8192\), 16 matched antithetic lineages, \(h=10^{-5}\), nodes \(0.5,0.75,0.9,0.95\), 20,000 bootstraps. | All local arithmetic gates passed. At \(n=8192\), moment level M2 was centrally best for canonical/centered/metric and M4 for variance, but no full successive-error sequence was monotone and every 99% paired width-shift interval crossed zero. Descriptive two-width evidence only. |

Unthrottled finite-width feature ascent is an unsafe expectation target. Homogeneity gives a positive-probability arbitrarily early blow-up at every width. That is why later studies use stopped trajectories, antithetic pairs, medians, or physical squared-loss time. Antithetic averaging by itself is variance reduction and need not change an expectation; stopping and median aggregation do change the estimand. Physical-flow averaging targets the residual-weighted effective kernel

\[
\kappa_{{\rm eff},n}(y)
=\frac{\mathbb E[(1-f_n)\kappa_n]}{1-\mathbb E f_n},
\]

not the ordinary feature-ascent expectation. None may be treated as direct evidence for the latter without an identification bridge.

The nonmonotone FP64 absolute-error sequence is not a Stieltjes falsifier. Gaussian and Radau convergents are ordered in separate parity subsequences, and the reference is a finite-width Euler trajectory with its own bias; strict adjacent-order improvement against that reference is not predicted by V1.

### 10.9 The exact status

\[
\boxed{
\begin{gathered}
\text{Canonical equal-metric square activation: all eight known moments pass; all-order V1--V3 open.}\\
\text{Uniform block-metric extension: disproved exactly.}\\
\text{Conventional shallow raw-square Stieltjes claim: disproved exactly.}\\
\text{Smooth-activation-universal extension: disproved exactly.}
\end{gathered}}
\]

The Stieltjes program does not currently prove a finite causal neural dynamics. It supplies a precise non-Taylor mechanism, unusually strong exact finite-order evidence in one canonical model, exact counterexamples that delimit the claim, and a clear list of the missing global bridges.

---

## 11. One cohesive interpretation of the whole project

The repository's scientific workstreams are not proposed answers of equal status. They form a chain of scientific roles; the first three below are substudies of the joint `resnet_pde` program.

### 11.1 The causal anatomy

dense_response establishes the anatomy of the problem. Dense training creates chronological forward response, reverse response, and a shared-transpose Onsager correction. A small current Gram state is not exact, while a fixed response-order expansion can be very accurate. This tells us what must be compressed.

### 11.2 The candidate state

operator_pde makes the bold constructive move: encode the immutable initialization by a Gaussian source label and the trained dense operator by a conditional coefficient law. It is the only thrust that presently produces a literal autonomous PDE with no network-width coordinate at fixed cutoff and with exact internal projected-gradient geometry. This uniqueness concerns PDE construction, not the existence of experiments: `dense_response` and `pde_convergence` also contain executed numerical campaigns. The degree-one PDE is empirically good enough to be scientifically interesting.

### 11.3 The approximation audit

pde_convergence asks whether increasing source resolution makes that PDE arbitrarily accurate. The answer is not yet positive or negative. The parity correction removes one false alarm; the corrected aggregate tests still fail to show contraction. The analytic reason is now clear: energy controls size and time regularity, but not collective source compactness or a cutoff-uniform nonlinear stability constant.

### 11.4 The local calculus

mean_field_peeling supplies a rigorous microscope. In its audited separately fixed-order families it exposes the exact Gaussian innovations and response attachments that an operator closure should reproduce. The successful order-three/order-five compilers show that trained shared-matrix effects are finite and algorithmic locally. A universal terminating compiler and a depth-uniform state bound remain open, which is why this is not yet a global PDE theorem.

### 11.5 The warning laboratory

quadratic_nonclosure proves that local calculability is not enough. Even exact positive fixed-order coefficients can grow factorially and make the natural Taylor closure non-Cauchy. Its broader no-go statements remove analytic, positive-semigroup, and naive moment-topology shortcuts while carefully leaving signed, nonanalytic, operator, and real-axis constructions alive.

### 11.6 The alternative resummation

stieltjes_conjecture explores one such real-axis construction. It transforms the divergent quadratic jet into a possible positive resolvent and rational ODE hierarchy. The canonical finite prefix is remarkably coherent, but exact metric and activation counterexamples show that the phenomenon is architecture-specific. The final neural-identification bridge remains just as important as all-order positivity.

Together, the repository supports a nuanced thesis:

> Dense feature learning has substantial finite causal structure, but that structure is more likely to be an operator/measure state with response-aware source regularity than a small collection of ordinary moments or a positive Taylor jet.

### 11.7 The precise central conjecture

There is a plausible route to an ordered deterministic target, but no imported theorem currently supplies it. At each fixed \(L\), one would first need a causal width theorem jointly for the forward fields, trained adjoints, and repeated row/column actions of every reused \(W_\ell\); a concentration theorem would then make the observable quotient deterministic. Only after that could one prove trained iid-depth homogenization, identify the conditional Onsager mean while showing centered layer innovations cancel at order \(L^{-1/2}\), and pass to the continuous-depth forward/backward system. Standard fixed-computation tensor-program results do not control a whole continuum of training times or this subsequent depth limit.

The evidence for this architecture is finite-grid only: successive width Cauchy ratios \(0.462,0.488,0.518\), a depth ratio \(0.578\), across-root RMS width slopes near \(-0.61\), and trained centered depth variances near \(L^{-1}\). Geometric extrapolation still leaves estimated width tails around \(4.2\%\)–\(5.1\%\) and a depth tail near \(1.75\%\); moreover the conditional shared-transpose mean was not directly tested. Existence and determinism of the target below are therefore genuinely conjectural, not consequences of a familiar fixed-\(L\) theorem that the report merely omitted.

For each static parameter \(\vartheta\in\mathcal U\), first define the deterministic ordered target

\[
\mathcal O_\vartheta
=
\lim_{L\to\infty}\lim_{n\to\infty}
\mathcal O_{n,L}^{\vartheta}
\]

as convergence in probability in

\[
C\!\left([0,T];
\mathbb R^m\times C([0,1];\mathbb S^m)\right),
\]

where \(\mathbb S^m\) is the space of real symmetric \(m\times m\) matrices, and with the finite-\(L\) Gram sequence linearly interpolated in normalized depth. Existence and uniqueness of this target are part of the conjecture.

Let \(\mathcal O_{r_H,\vartheta}\) be the output/Gram readout of the degree-\(r_H\) operator PDE. Fix the canonical, parameter-independent scales

\[
S_f=\|(0.8,-0.55,0.35)\|_2,
\qquad
S_G=\|I_3\|_F=\sqrt3.
\]

For a compact horizon \(T\), use the normalized distance

\[
d_T\bigl((f,G),(\widetilde f,\widetilde G)\bigr)
=
\max\left\{
\sup_{t\le T}\frac{\|f(t)-\widetilde f(t)\|}{S_f},
\sup_{\substack{t\le T\\s\in[0,1]}}
\frac{\|G(s,t)-\widetilde G(s,t)\|_F}{S_G}
\right\}.
\]

Define

\[
E_{r_H}(T)
=
\sup_{\vartheta\in\mathcal U}
d_T(\mathcal O_\vartheta,\mathcal O_{r_H,\vartheta}),
\]

with \(E_{r_H}(T)=\infty\) if the ordered target is not uniquely defined, the compiled degree-\(r_H\) PDE is not uniquely well posed on \([0,T]\), or a readout is undefined.

For \(T=\infty\), the same definition uses \(\sup_{t\ge0}\) and assigns \(E_{r_H}(\infty)=\infty\) unless both paths are uniquely and globally defined. It is not shorthand for “the largest tested finite horizon.”

The natural **cofinal compact-time** claim is

\[
\boxed{
\lim_{r_H\to\infty}
E_{r_H}(T)=0
\quad\text{for every }T<\infty.
}
\]

The current operator-specific report instead states the sharp **accuracy-dependent all-time** claim

\[
\boxed{\inf_{r_H\ge1}E_{r_H}(\infty)=0.}
\]

These statements trade strength on two independent axes. A full-sequence limit as \(r_H\to\infty\) is stronger than an infimum over \(r_H\), because the latter permits only selected sparse successful degrees. For example,

\[
E_{r_H}(\infty)=
\begin{cases}
r_H^{-1},&r_H\in\mathcal S,\\
1,&r_H\notin\mathcal S,
\end{cases}
\]

with \(\mathcal S\) any unbounded sparse subset of the admissible odd degrees, has zero infimum but no full-sequence convergence. Although the Hermite spaces are nested, the nonlinear projected vector fields need not restrict consistently: a new shell can destabilize or alias low-mode feedback before a later shell repairs it. No such permanent degree-resonance pattern has been demonstrated. Strictly speaking every unbounded subsequence of \(\mathbb N\) is cofinal in the order-theoretic sense, so “good noncofinal subsequence” is the wrong phrase.

The other axis is time: uniformity over \(t\ge0\) is stronger than compact-time accuracy. The infimum form expresses the irreducible accuracy-dependent existence claim “for each tolerance, some predeclared finite PDE works for all time”; the full limit is the cleaner Galerkin strengthening. The aggregate noncontraction through degree seven weakens empirical support for the latter but is not the sole logical reason for stating the former. Neither claim is proved, and neither is simply “the weaker version” of the other.

### 11.8 Why this would go beyond existing limit descriptions

A fixed-computation tensor program can characterize any finite list of observables, but it does not automatically provide an autonomous state that can be restarted and evolved for arbitrary time. A conventional DMFT can be causal yet store two-time kernels whose complexity grows with the horizon. A successful theorem here would show that, on the reachable manifold of a standard dense nonlinear µP network, those histories admit finite local compression to any desired accuracy.

The weak restart condition adds only that the **full** compiled state—\((b,a,c)\) for the operator PDE, or the complete law plus response/covariance-kernel state declared by a response compiler—contains every variable needed by the autonomous vector field, including any reconstructed fast Gaussian kernel. It excludes a hidden replay table, undeclared two-time history, or positive-time oracle. It does not demand restart from \((f,G,\Theta)\) alone. A split-run serialization check tests this structural/numerical condition; robust correspondence of compressed positive-time dense snapshots is the stronger open theorem described in Section 1.

That is the potential landmark. The present results clear two preliminary thresholds:

1. a non-oracular finite PDE candidate actually exists and runs;
2. shared-transpose response can be compiled explicitly at fixed order.

They have not cleared the decisive threshold: a quantitative theorem that the finite state is complete for the dense target.

---

## 12. Project-wide claim ledger

| Component | Strongest defensible statement | Status | Main qualification |
|---|---|---|---|
| Finite dense residual mechanics | Exact adjoints, µP gradients, PSD tangent kernel, and loss dissipation | Exact finite system | Does not close the large-width/depth dynamics |
| Chronological response | Factorial tail for bounded ordered propagators; very accurate finite-matrix truncations | Exact/conditional plus empirical | Dense matrices remain; coupled source substitution is not controlled |
| Finite-\(r_H\) operator PDE | Explicit autonomous Liouville/forward/adjoint system with exact projected-gradient geometry | Exact inside the PDE | Well-posedness assumed; equality to dense target unproved |
| Canonical \(r_H=1\) / \(P=5\) PDE | Roughly 1% learned-Gram error on the main benchmark; all fourteen observed point discrepancies under 5% | Empirical | Simultaneous 5% equivalence unresolved; finite references/panel; no arbitrary-accuracy implication |
| Hermite hierarchy | Exact odd-parity reduction; per-mode tails often shrink | Exact parity plus empirical | Aggregate state/observable errors grow through degree seven |
| Infinite-source PDE | Bounded frozen transpose and energy bounds | Exact functional analysis | Transpose is noncompact; plain \(L^2\) stability fails; uniqueness open |
| Generic order-three peeling | Explicit response-aware Gaussian normal form and annealed fixed-order limit under polynomial-smooth assumptions | Proved limit in fixed scope | Fixed depth/batch/order only |
| Order-five and multi-observable peeling | Independently audited exact DAGs/recurrences at several fixed depths | Exact algebra; theorem under stated program hypotheses | No universal grammar or depth-uniform small representation |
| Nonlinear two-step peeling | Exact finite-width directional identities and formal channel schema | Exact identities/formal closure | General nonlinear channel registry and convergence incomplete |
| Quadratic compiler | Exact special-grammar derivative prefix through order 17, from the staged engines described in §8.7 | Exact formal annealed jet | No positive-time curve or concentration theorem |
| Depth-three quadratic recurrence | Exact internal raw-square recurrence through order 9; dual coefficient assemblies agree; all four accessible Stieltjes moments pass | Exact recurrence / conditional network identification | Width-limit mode and theorem unstated; no independent finite-width check; \(H_2,H_2^+\) unavailable |
| Positive quadratic Taylor closure | Zero radius and non-Cauchy induced losses | Disproved in scope | Does not rule out signed/non-Taylor/operator closures |
| Tagged-site quadratic DMFT | Zero-delay consequence under the postulated Volterra system | Conditional | Representation, self-consistency, solution, and relaxed selection unproved |
| Canonical Stieltjes sequence | Eight exact moments; all accessible ordinary/shifted Hankel gates pass | Exact finite-prefix evidence | All-order positivity, determinacy, and neural identification open |
| Uniform metric Stieltjes claim | Negative shifted determinant for a strict positive-metric interval | Disproved exactly | Canonical equal metric remains open |
| Smooth-activation Stieltjes universality | Normalized sine has negative first transformed moments | Disproved exactly | Does not affect canonical square activation |
| Rational quadrature hierarchy | Certified conditional kernel/flow bounds; rapid convergence at exact Lambert boundary | Conditional / exact special case | Canonical global neural bridge absent |
| All-time finite causal PDE theorem | No completed result | Open | Needs coercivity/trapping after compact-time identification |

---

## 13. The shortest credible route to a theorem

The repository has generated many possible continuations. The following ordering best respects what the audits actually found.

### 13.1 Prove the infinite operator flow before more cutoff numerics

Choose a weighted Gaussian source space that controls both Hermite tails and products with the unbounded readout coordinate. Prove local, then compact-time, well-posedness and uniqueness for the coupled forward/adjoint/Liouville system. The norm must be source-mode coercive; generic unweighted bounds will not compactify the isonormal transpose.

A useful target estimate is

\[
\sup_{r_H}\sup_{t\le T}
\|(I+N_G)^{\alpha/2}Y_{r_H}(t)\|<\infty
\]

for a sufficiently rich state \(Y_{r_H}\), together with a product estimate closing \(\phi'(z)p\) in the same scale.

### 13.2 Turn regularity into a forced-stability theorem

For an infinite solution \(Y\), prove

\[
\sup_{t\le T}\|Y_{r_H}(t)-\Pi_{r_H}Y(t)\|
\le
C_T
\int_0^T
\|F_{r_H}(\Pi_{r_H}Y(t))-\Pi_{r_H}F(Y(t))\|\,dt
\]

with \(C_T\) independent of \(r_H\). This cleanly separates consistency from amplification and makes the common-reference commutator the relevant numerical observable.

If pure Hermite fields do not close this estimate, enrich the state with the smallest response coordinates indicated by peeling. The evidence favors a broad nearly orthogonal tail, so an \(\ell^2\)-type response/source norm is more plausible than maximum-coefficient control.

### 13.3 Derive the shared-transpose mean in the dense ordered limit

At fixed \(L\), establish a causal width limit jointly for forward fields, adjoints, and the finite set of response channels needed by the operator state. Then prove trained-depth homogenization around the correct conditional mean, not merely centered variance decay. The \(L^{-1}\) variance slopes are encouraging, but the Onsager mean is the theorem.

Mean-field peeling can help here by generating and auditing the finite-order conditional attachments. Its role should be to identify the correct limiting drift and close leave-out estimates, not to assume an analytic time expansion.

### 13.4 Only then seek the all-time upgrade

Once compact-time convergence is known, prove that all sufficiently accurate models enter a common coercive region. Possible routes are:

- a tangent-kernel lower bound after reaching a positive subtarget;
- residual integrability plus finite state arclength;
- a trapping neighborhood around the zero-loss manifold;
- a loss-to-state observability inequality.

The quadratic residual-clock theorem is a useful template, but its trajectory-dependent constants must become uniform in the residual-network setting.

### 13.5 Keep the Stieltjes program separate and falsifiable

The next new canonical gate is \(F^{(19)}(0)\), which decides ordinary \(H_4\). Computing it is a clean bounded falsification experiment. It should not delay the operator-flow theorem, because even an all-order canonical Stieltjes proof would still need positive-time neural identification and applies to a different architecture.

If the Stieltjes branch continues, the right targets are:

1. an all-order architecture-specific Jacobi or Hankel recurrence;
2. a determinacy criterion;
3. an independently well-posed global quadratic mean-field kernel;
4. equality of that kernel with the resolvent.

More two-width curve comparisons cannot substitute for these bridges.

### 13.6 A decisive next PDE experiment

A useful numerical successor would co-evolve parity-clean degrees \(3,5,7,9\) on a common high-order quadrature, retain state and observable commutator directions, use multiple independent scrambles, and refine source quadrature, row-process sampling, depth grid, and time step independently. Its preregistered decision should concern either:

- contraction of a collective weighted tail; or
- failure of pure Hermite closure under a stable, resolution-certified norm.

Another one-seed adjacent-cutoff comparison would add little.

---

## 14. Supersession and excluded shortcuts

The dated top-level monograph is the correct baseline for the residual-network and operator-PDE state as of 31 July 2026. It already incorporates the parity correction and the degree-seven common-reference aggregate noncontraction. Later maintained work changes its ledger chiefly in the mean-field-peeling and Stieltjes scopes. The current supersession ledger is:

- The quadratic fixed-order annealed coefficients are no longer merely a recovered/conditional “FW” premise; the combined forest, Gaussian-program, and bounded-recurrence engines establish the audited prefix exactly through order 17.
- The quadratic conclusion remains formal-jet level. Concentration and positive-time trajectory identification are still absent.
- For continuity with earlier residual-PDE reports, the early \(P=5\to15\to35\) adverse Hermite trend remains superseded by the exact parity correction. The common-reference aggregate noncontraction already recorded in the monograph remains the authoritative negative evidence.
- Canonical Stieltjes evidence now extends from the first few moments through \(\mu_7\), while the uniform block-metric and smooth-activation extensions are exactly false.
- The shallow raw-square model is non-Stieltjes even though its neuron characteristics are explicitly integrable.

The unified positive story intentionally excludes:

- trajectory-fitted POD bases as an admissible architecture-derived closure;
- exact-curve Bernstein encodings and arbitrary ODE packing, which hide an oracle in coefficients or source syntax;
- the long-horizon \(K/J/N\) “compiler” as an executable PDE, because its state tables and drift DAG were never emitted;
- the invalid even-shell convergence comparison;
- the tagged-site discontinuous step loss as a network conclusion;
- finite moment or finite-width prefix passes as evidence of an all-order theorem;
- plateau at \(T=32\) as proof of a supremum over \(t\ge0\).

---

## 15. Directory and sub-study map

### Top-level baseline

- **FINITE_CAUSAL_NEURAL_PDE_MASTER_MONOGRAPH_v2.2_2026-07-31.md:** the dated integrated baseline; authoritative for the central architecture and proof lattice, superseded by later maintained study reports where noted.
- **studies/resnet_pde/README.md:** current evidence hierarchy and supersession guide for the three residual-network substudies.

### studies/resnet_pde/dense_response

- **early_audit:** older \(h^0=\tanh(Ux)\) model; truncated depth-adjoint expansion, factorial ordered-propagator bound, finite-matrix experiments, continuation witnesses, and no-go arguments against current-Gram/low-rank shortcuts.
- **long_horizon:** canonical linear input lift; coupled \(q/r\) training-response hierarchy through \(T=32\); strong low-order empirical accuracy; formal but non-executable \(K/J/N\) compiler proposal.

### studies/resnet_pde/operator_pde

- **core:** explicit Hermite/isonormal conditional Liouville PDE, projected adjoint/PSD kernel, canonical benchmark, statistical and restart audits.
- **generalization:** fourteen fixed transfer cases under one degree-one PDE without retuning.
- **activation_controls:** identity, gain-matched linear, and nonlinear activation discrimination.
- **rerun_2026-07-31:** canonical reproduction and small execution smoke test; no new claim.

### studies/resnet_pde/pde_convergence

- **01_proof_audit:** ambitious seven-gate protocol; only two low-order numerical jobs completed, so no scientific gate passed.
- **02_lean_salvage:** small-grid width/depth, homogenization, same-state, generator, basis, and plateau diagnostics; contains the superseded even-shell comparison.
- **03_bridgeability:** exact parity repair and the correct odd cutoff ladder; contraction of a lifted boundary-source diagnostic but aggregate feedback noncontraction. Phase 05 shows that the lifted quantity is not the trained high-shell velocity.
- **04_scalar_stress:** high-degree bounded sine/tanh source tests; activation nonlinearity is real, while pure source-Hermite cutoff effects are small and not monotonically resolved.
- **05_tail_and_compactness:** common-reference commutators and final functional analysis; isolates collective source compactness, uniqueness, and cutoff-uniform forced stability as the gap.

### studies/mean_field_peeling

- **CURRENT_RESEARCH_STATE:** current theorem/program ledger and compiler specification.
- **MUP_TRAINING_CASE_STUDY:** backward kernels, one-step feature motion, and the exact two-Euler-step decomposition in a three-hidden-layer µP MLP.
- **generic_first_stieltjes base/compiler:** two-hidden-layer order-three 17-atom normal form, exact finite-width oracles, and probability bridge.
- **b2 and depth:** fixed-batch and arbitrary-separately-fixed-depth order-three extensions.
- **order5:** two-hidden-layer flattened \(J_1,J_3,J_5\) compiler and normalized-sine counterexample.
- **depth_order5:** three/four-layer tagged and unit-Gram order-five compilers.
- **depth_order5_scalar:** 29-coordinate, six-sweep scalar recurrence.
- **depth_order5_observables and multi_observable:** universal parameter backbone with a hidden squared-RMS head and finite-width/nonpolynomial audits.
- **quadratic_compiler:** exact decorated-forest grammar and high-order integer recurrence.
- **quadratic_compiler/depth3_gaussian_program:** raw-square three-hidden-layer nested-detransposition recurrence; exact recurrence values \(J_7,J_9\), two coefficient normalizations, an order-nine resource audit, and a four-moment Stieltjes/Hankel pass, with the network width-limit bridge unstated.
- **campaigns 1--6:** relative metric/hidden response, two-input, centered activation, independent block metric, three-input, and stopped historical order-13 threshold probes. Their Stieltjes consequences are owned by the Stieltjes study.

### studies/quadratic_nonclosure

- **approximate_single_source_stability:** residual-clock stability and conditional all-time error conversion.
- **approximate_single_source_conjecture_resolution:** positive branch and zero-radius/non-Cauchy theorem.
- **adversarial_audit_report:** analytic/semigroup/polynomial/topology no-go scope and anti-oracle criteria.
- **mean_field_single_source_conjecture_audited_resolution:** conditional tagged-site Volterra comparison and relaxed-selection step trace.
- **normalized_mean_field_taylor_closure_audit:** RMS/readout/row-normalized jets and exact frozen moment non-invariance.
- **master report/README:** corrected synthesis; later mean-field compiler supplies the fixed-order annealed premise.

### studies/stieltjes_conjecture

- **CURRENT_RESEARCH_STATE:** sole current integrated authority.
- **theory:** inverse-series formulas, exact moment/Hankel checks, variance boundary, total-nonnegativity/root audits, and quadrature reconstruction.
- **resolution_program:** exact block-metric counterexample, sharp six-moment \(\alpha_\ast\) transition, shallow reduction, canonical orders 15/17, and hidden-norm high-order results.
- **numerics/direct_loewner:** wrong-clock first attempt and corrected but biased robust proxy.
- **numerics/finite_width:** fresh local coefficient calibration and inconclusive positive-time Loewner tests.
- **numerics/global_proxy_campaign:** exact Lambert-boundary validation and under-resolved canonical global pilot.
- **numerics/hybrid_mean_field_campaign:** bounded-readout DMFT Stage 0, failed FP32 Euler qualification, passed local FP64 successor, and unresolved two-width successive-proxy comparisons.
- **archive:** superseded status reports and frozen historical protocols only.

---

## 16. Reproducibility and durability qualifications

The mathematical conclusions above use maintained reports and compact certificates rather than assuming every historical script is currently turnkey.

- The current operator-core local suite passes. Some other exact-equality tests are brittle under the workspace’s NumPy/SciPy versions, which differ from the pinned bundles: discrepancies are at \(10^{-15}\) scale or arise because an older NumPy lacks a newer integration helper.
- The Stieltjes exact-resolution suite passes its 56 tests. A broader numerical run produced 76 passes and four verifier errors because the breadth-panel checker recursively finds both the old FP32 and the newly nested FP64 ATTEMPTS ledgers while requiring exactly one. This is a current path-scoping bug, not evidence against the recorded scientific result.
- Raw long-horizon dense-response arrays, PDE-convergence phase arrays, and the 31 July operator rerun are retained. The original compact operator-core, generalization, and activation-control releases retain processed or sealed evidence but omit their complete raw campaigns. A clean clone can inspect every scoped claim and rerun code, but cannot independently reanalyze each omitted historical raw trajectory without regenerating it.
- Several reports use exact floating-point equality for cross-platform reproducibility gates. The resulting last-bit failures should be separated from failed numerical-resolution or statistical-science gates; both are recorded above where relevant.
- Exact rational/integer computer algebra is far stronger than floating-point agreement, but it is not formal proof verification. Independent implementations sometimes share the same mathematical recurrence.
- The new **depth3_gaussian_program** directory was untracked Git work when first audited. Its protocol hashes match the recorded results but were not externally timestamped, so prospectivity is not independently certified. Both three-test suites pass. The feature-jet fast tests hard-code controls only through order five; I reran both order-nine routes successfully, where the new-order gate is agreement between assemblers sharing the core response identities. I also reran the exact Stieltjes transformation and Hankel audit successfully. The commit containing this synthesis is its first durable in-repository archive.
- The stored **stieltjes_order9_audit.json** is a hand-curated compact result schema, not byte-for-byte stdout from the audit program; every shared exact moment, determinant, hash gate, and verdict agrees. Its protocol's 60-second/512-MiB stopping rule was an external run condition, not an operating-system limit enforced by the script. Floating eigenvalues are diagnostics only; all Hankel decisions use exact rationals.

---

## Final assessment

The project is neither a completed finite-PDE theorem nor a collection of disconnected experiments. It has converged on a coherent architecture for the problem:

1. dense training generates history through shared forward/transpose reuse;
2. fixed-order history can be peeled into finitely many response-aware Gaussian channels;
3. an immutable-source conditional operator law packages those channels into a literal autonomous PDE;
4. low-order instances reproduce nonlazy dense dynamics across a meaningful synthetic panel;
5. the remaining mathematical barrier is collective source compactness, well-posedness, stability, and dense-limit identification;
6. the quadratic laboratory proves that a formal Taylor hierarchy cannot be used as a shortcut;
7. the Stieltjes branch shows how a non-Taylor rational hierarchy might work in a special model, while its exact counterexamples prevent overgeneralization.

The most valuable next result would not be another close finite curve. It would be a compact-time theorem joining a parity-correct finite-source PDE to a uniquely defined infinite operator flow, followed by a derivation of that flow from the ordered dense network. That is the point at which the project’s central claim would become real.
