# One activation at every finite hidden depth

## Part M. Model, quantifiers and theorem

All spaces are real. Fix \(0<\delta<1\), a dimension \(d\ge1\),
three inputs \(x_i\in\mathbb R^d\), and three labels \(y_i\in\{-1,1\}\).
Write \(u_i=x_i/\sqrt d\) and assume
\[
 \|u_i\|=1,\qquad \Gamma_{ij}=u_i^Tu_j\le1-\delta
       \quad(i\ne j).                                      \tag{M.1}
\]
In particular the theorem applies when
\(-1+\delta<\Gamma_{ij}<1-\delta\). The stronger one-sided condition
(M.1) is sufficient, and singular input Gram matrices are allowed.
The number of samples is three throughout; depth is the quantity
being generalized.

Choose a nonconstant function \(\psi\in C^2(\mathbb R)\) with
\[
 \max\{\|\psi\|_\infty,\|\psi'\|_\infty,\|\psi''\|_\infty\}\le1.
                                                               \tag{M.2}
\]
Any bounded nonconstant \(C^2\) function with bounded first and
second derivatives can be normalized this way by a scalar factor.
The following finite selection depends only on \(\delta,\psi\).
Choose an integer \(r_\psi\ge1\) with
\[
 J_\psi=\inf_{b,c\in\mathbb R}\int_{-r_\psi}^{r_\psi}
                  [\psi(x)-b-cx]^2\,dx>0,\qquad
 c_\psi=\frac{e^{-r_\psi^2/2}}{\sqrt{2\pi}}J_\psi>0.        \tag{M.3}
\]
Part G proves that such an integer exists. Set
\[
 \lambda=\delta^2/16,\qquad T_0=12/\lambda,\qquad
 a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{c_\psi}}\right)^{2/5}\right\}.
                                                               \tag{M.4}
\]
For any one fixed \(e\in(0,1]\), including \(e=1\), use
\[
                     \phi(z)=a(1+z)+e\psi(z).              \tag{M.5}
\]
Neither \(a\) nor \(e\) depends on the hidden depth, width, time,
dimension, labels or particular admissible input configuration.
The constants are sufficient bounds, with no claim of sharpness.

### M.1. Exact finite algorithms and their metric

For each separately fixed finite integer \(L\ge2\), a width \(n\)
network has raw parameters \(W^1\in\mathbb R^{n\times d}\),
\(W^\ell\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\), and
\(C\in\mathbb R^n\). All initial entries are mutually independent,
with
\[
 W^1_{jk}(0)\sim N(0,1/d),\qquad
 W^\ell_{jk}(0)\sim N(0,1/n),\qquad
 C_j(0)\sim N(0,n^{-2}).                                  \tag{M.6}
\]
Use \(\langle v,q\rangle_n=n^{-1}v^Tq\). The physical fields are
\[
 z_i^1=W^1x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
 z_i^\ell=W^\ell h_i^{\ell-1}\ (\ell\ge2),\quad
 f_i=\langle C,h_i^L\rangle_n,\quad r_i=f_i-y_i,
 \quad\mathcal L=\tfrac12\sum_i r_i^2.                    \tag{M.7}
\]
Coordinate nonlinearities and products occur within one layer.
The true residual-free backward fields are
\[
 b_i^L=\phi'(z_i^L)C,\qquad
 b_i^\ell=\phi'(z_i^\ell)(W^{\ell+1})^Tb_i^{\ell+1}.
                                                               \tag{M.8}
\]
The original raw metric and its exact gradient flow are
\[
 \|\Delta\theta\|_{{\rm raw},n}^2
 =\frac dn\|\Delta W^1\|_F^2+
    \sum_{\ell=2}^L\|\Delta W^\ell\|_F^2+\|\Delta C\|_n^2,
                                                               \tag{M.9}
\]
\[
 \dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\qquad
 \dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T,
 \qquad\dot C=-\sum_i r_i h_i^L.                          \tag{M.10}
\]
Indeed the Euclidean first derivative has factor \(1/n\), which
the inverse metric multiplies by \(n/d\); the matrix derivatives
retain \(1/n\); the readout inverse metric cancels its factor
\(1/n\). Thus all updates have the indicated factors.

Raw GD is simultaneous explicit Euler for exactly (M.10), with
physical step \(\eta_n=n^{-2}\). Its raw parameters are linearly
interpolated at times \(k\eta_n\). At intermediate times hidden
fields are recomputed from these parameters by (M.7). Their
velocities are the derivatives of these recomputed fields, with
the right derivative at nodes and the left derivative at the
final endpoint of an observation interval. GF and GD use the
same actual random initialization (M.6). No coupling across
different widths is required.

Finite GF exists globally: its locally Lipschitz field satisfies
\(\int_0^T\|\dot\theta\|_{{\rm raw},n}^2\le\mathcal L(0)\).
Cauchy--Schwarz bounds displacement by
\(\sqrt{T\mathcal L(0)}\), makes a finite endpoint Cauchy and
allows local continuation there. GD is defined at every finite
step because all its functions are everywhere defined.

### M.2. Population state and an exact normalization for the proof

Part F constructs one neuron probability space \(\Omega_\ell\)
per hidden layer, with \(H_\ell=L^2(\Omega_\ell)\), and initialized
actions \(A_{\ell,0}:H_{\ell-1}\to H_\ell\) of norm at most 10
for \(2\le\ell\le L\), with their genuine adjoints. These are the
canonical joint limits of the finite Gaussian calculations,
including reuse of transposes. Arbitrary bounded actions are
not substitute initializations.

It is convenient to write \(w=\sqrt d W^1\). This is an isometry
of the first raw block, not a change of training metric. The
population initialization is \(w_0\sim N(0,I_d)\), \(C_0=0\), and
the affine state space is
\[
 \mathcal P=L^2(\Omega_1;\mathbb R^d)\times
  \prod_{\ell=2}^L(A_{\ell,0}+\mathcal S_2(H_{\ell-1},H_\ell))
                         \times H_L,\qquad
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\sum_{\ell=2}^L\|\Delta A_\ell\|_{\rm HS}^2
                                           +\|\Delta C\|_2^2.
                                                               \tag{M.11}
\]
Only learned increments are Hilbert--Schmidt. The original first
weight field is \(W^1=w/\sqrt d\). In population (M.7)--(M.10)
replace normalized finite inner products by the appropriate
layer expectations, matrices by their actions and transposes by
their adjoints. In particular \(z_i^1=w\cdot u_i\) and
\(\dot w=-\sum_i r_i b_i^1u_i\).

For proof estimates normalize only hidden fields:
\[
 K_\ell=a^{\ell-1},\quad Y_i^\ell=z_i^\ell/K_\ell,\quad
 X_i^\ell=h_i^\ell/a^\ell,\quad
 \chi_\ell(v)=v+\frac{1+(e/a)\psi(K_\ell v)}{K_\ell}.
                                                               \tag{M.12}
\]
Then \(Y_i^1=w\cdot u_i\), \(Y_i^\ell=A_\ell X_i^{\ell-1}\),
\(X_i^\ell=\chi_\ell(Y_i^\ell)\), and
\(F_i=\langle C,X_i^L\rangle\) satisfies \(f_i=a^LF_i\).
No readout rescaling occurs. Therefore
\(\nabla_{\rm raw}f_i=a^L\nabla_{\rm raw}F_i\) in every block.
Part F proves this identity as a scalar Fréchet derivative.
The normalized backward variables are
\[
 q_i^L=C,\quad d_i^\ell=\chi_\ell'(Y_i^\ell)q_i^\ell,
 \quad q_i^\ell=A_{\ell+1}^*d_i^{\ell+1}\quad(\ell<L).
                                                               \tag{M.13}
\]
The true raw backward fields obey
\(b_i^\ell=a^{L-\ell+1}d_i^\ell\). All scalings are fixed
deterministic constants when taking width or time limits.

For \(v\in H_\ell,h\in H_{\ell-1}\),
\((v\otimes h)q=v\langle h,q\rangle\), of Hilbert--Schmidt norm
\(\|v\|\|h\|\). Its finite matrix is \(vh^T/n\).
A strong solution is a strong \(C^1\) path in (M.11).
Bounded primal quantities on compact intervals means bounded
\(\|w\|_2,\|A_\ell\|_{\rm op},\|C\|_2\) there. Constants for
activation selection use only the three initial projections,
each of norm one, and raw displacements. They never require a
dimension independent bound on \(\|w_0\|_2=\sqrt d\).

### M.3. Observations and the full theorem

The \(L+1\) true raw kernel blocks are
\[
 K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_1,\qquad
 K^\ell_{ij}=\langle b_i^\ell,b_j^\ell\rangle_\ell
             \langle h_i^{\ell-1},h_j^{\ell-1}\rangle_{\ell-1}
       \ (2\le\ell\le L),\qquad
 K^{L+1}_{ij}=\langle h_i^L,h_j^L\rangle_L.                \tag{M.14}
\]
Their sum is the Gram of the raw predictor gradients. Auxiliary
capped update fields used in the proof do not replace these true
kernel observations.

Let \(\mathcal Z^\ell=(z_1^\ell,h_1^\ell,z_2^\ell,h_2^\ell,
z_3^\ell,h_3^\ell)\) and
\(\mathcal U^\ell=(\mathcal Z^\ell,\dot{\mathcal Z}^\ell)\).
An empirical law averages the Dirac masses over neuron rows.
For whole paths use \(C([0,T];\mathbb R^6)\) with the supremum
Euclidean norm. For a normed space \(E\),
\(\mathcal W_2(\mu,\nu)^2\) is the infimum of
\(\int\|v-q\|_E^2\,d\pi\) over couplings of the two laws.
All laws below have the required finite second moments.

An additional generated probe is any fixed finite layer-typed
expression in root coordinates, constants, fields at finitely
many times, deterministic linear combinations, \(C^1\) coordinate
maps with bounded first derivatives, same-layer inner products,
and initialized or current actions and their adjoints. Its
instruction count is fixed before width tends to infinity.
Unbounded true backward and velocity products are separately
covered by Part V's ordered truncation arguments.

**Theorem M.1 (one activation at all finite depths).** With (M.1)--(M.6),
the same constants (M.4) and any one \(e\in(0,1]\) have the following
properties for every separately fixed finite \(L\ge2\).

1. There is a global autonomous strong population raw gradient
   flow. On its canonical action spaces it is unique among
   strong solutions with bounded primal quantities on compact
   intervals. Continuation from every reached state is unique
   in that class. For all physical \(t\ge0\),
   \[
    \|r(t)\|_2\le\sqrt3\,e^{-\lambda a^{2L}t/2},\qquad
    \mathcal L(t)\le\tfrac32e^{-\lambda a^{2L}t},\qquad
    (\langle X_i^L(t),X_j^L(t)\rangle)_{ij}
                                      \succeq3\lambda I_3/4.
                                                               \tag{M.15}
   \]
2. For each finite physical \(T\), actual finite GF and actual
   raw GD with step \(n^{-2}\) converge jointly in probability,
   along the full width sequence, to that same population flow.
   Predictions, loss and every true raw kernel entry converge
   uniformly on \([0,T]\). At each layer the empirical full path
   law of \(\mathcal Z^\ell\) converges in \(\mathcal W_2\) for
   the supremum path norm, and
   \[
    \sup_{t\le T}\mathcal W_2\big(
       \widehat{\operatorname{Law}}_n(\mathcal U_n^\ell(t)),
       \operatorname{Law}(\mathcal U^\ell(t))\big)\longrightarrow0.
                                                               \tag{M.16}
   \]
   Joint same-layer field and velocity laws at any fixed finite
   list of times also converge in \(\mathcal W_2\). Their second
   moments, integrated squared preactivation and feature speeds,
   and every fixed finite same-layer tuple of generated probes
   converge to their population values or laws as appropriate.
3. For every sample, layer and time,
   \[
    \inf_{b,c\in\mathbb R}E_\ell[
       \phi(z_i^\ell(t))-b-cz_i^\ell(t)]^2
                      \ge\frac{e^2c_\psi}{16a^{L-1}}>0.
                                                               \tag{M.17}
   \]
   Every hidden raw parameter block and every sample's hidden
   preactivation and feature at every layer have nonzero strong
   right second derivative at zero. With \(p=y/3\) and
   \(\kappa(t)=p^T(\sum_{\ell=1}^{L+1}K^\ell(t))p\),
   \[
    \kappa(t)=\kappa(0)+18t^2\|V\|_{\rm hidden}^2+o(t^2),
                 \qquad \|V\|_{\rm hidden}>0,             \tag{M.18}
   \]
   where Part N defines and proves positivity of every block of \(V\).

The activation pair and normalized Gram floor are uniform in \(L\).
The width-convergence constants and width required for a specified
accuracy may depend on \(L,d,a,e,\psi,T\) and the fixed data.
There is no assertion for a joint limit \(L=L(n)\to\infty\), or
an interchange of infinite time and infinite width. The margin
in (M.17) may decrease with depth; Part A proves that this is
necessary for some allowed functions and gives infinite-dimensional
subclasses with a positive margin uniform in depth as well.

The proof is internal: Part F constructs the Gaussian laws and
actions, Part S supplies uniform source moments and response
derivatives, Part G gives depth-uniform geometry and the bounded
total control clock, Part V constructs the uncut population path
and all finite algorithm and observation limits, and Part N proves
the initial motion. No external specialized theorem is a premise.
