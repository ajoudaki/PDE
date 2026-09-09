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

# Part F. Fixed finite Gaussian programs, common actions and strong differentiation

This part treats every fixed finite hidden depth L. All instruction lists and the number of initialized matrices are fixed before width tends to infinity. Its elementary proofs do not assert uniformity for a depth or transcript length growing with width.

## 1. Finite programs and convergence of their empirical laws

There are \(L\) types of length-\(n\) vectors, one for each hidden layer. Operations combining coordinates may combine only vectors of the same type. For each \(2\le\ell\le L\), let
\[
 A_{\ell,n}:\mathbb R^n_{\ell-1}\longrightarrow\mathbb R^n_\ell
\]
be mutually independent matrices with independent \(N(0,1/n)\) entries.
Their transposes are reused as the reverse actions of these same matrices.

Each layer may have a fixed finite tuple of root vectors. Its coordinate tuples are independent and identically distributed, have finite second moment, and are independent of all matrices. Tuples in different layers are independent. Constants are also allowed. In the network application, the first-layer root is a Gaussian vector \(w_0\in\mathbb R^d\) with covariance \(I_d\); the three root preactivations are \(u_i^T w_0\). Here \(w_0=\sqrt d W^1(0)\) in the isometric bottom coordinates of Part M. Additional independent Gaussian roots may be added to any layer when a proof requires probes or regularization.

A deterministic-coefficient program is a fixed finite ordered list of instructions of the following forms:

1. apply a fixed \(C^1\) function \(F:\mathbb R^m\to\mathbb R\) with bounded first partial derivatives, coordinate by coordinate, to previously available vectors of one layer;
2. multiply a previously available vector by \(A_{\ell,n}\) or \(A_{\ell,n}^T\) for any \(2\le\ell\le L\), with the appropriate types;
3. form a fixed real linear combination of previous same-layer vectors.

The first condition implies a global Lipschitz bound and at most linear growth for each coordinate instruction. The bound may depend on that instruction. Root tuples themselves need not be generated by such functions.

Write
\[
\langle u,v\rangle_n=\frac1n\sum_{\alpha=1}^n u_\alpha v_\alpha,
\qquad \|u\|_n^2=\langle u,u\rangle_n.
\]
For same-layer nodes \(v^1_n,\ldots,v^m_n\), their empirical law is
\[
\widehat\mu_n=\frac1n\sum_{\alpha=1}^n
 \delta_{(v^1_{n,\alpha},\ldots,v^m_{n,\alpha})}.
\]
Here \(\mathcal W_2\) uses the Euclidean distance on \(\mathbb R^m\).

**Theorem F.1 (fixed finite Gaussian program).** Every such program has deterministic joint limiting laws of all its same-layer node tuples, and
\[
\mathcal W_2(\widehat\mu_n,\mu)\longrightarrow0
\quad\hbox{in probability}
\tag{F.2}
\]
along the full width sequence. In particular every within-layer pairwise contraction converges to the corresponding limiting second moment. The scalar laws are given by the source rule in Section 4. Query Grams may be singular. Finite collections of programs sharing the same matrices and roots converge jointly by applying the assertion to their finite union.

We prove this theorem in Sections 2–5. The following elementary facts make explicit the probabilistic mode of convergence used in its proof.

If \(X_\alpha\) are iid and \(E|X_1|<\infty\), their averages converge in probability to their expectation: truncate \(X_\alpha\) at level \(M\), use the variance bound \(O(M^2/n)\) for the bounded variables, and bound the mean absolute truncation error by \(E[|X_1|1_{|X_1|>M}]\). First send \(n\) to infinity and then \(M\) to infinity. This proves the required initial weak convergence and second-moment convergence of root empirical laws.

For probability measures on a finite-dimensional Euclidean space, weak convergence together with convergence of second moments implies \(\mathcal W_2\) convergence. One direct proof is as follows. Continuous truncations of \(|x|^2\) show that the second moments outside sufficiently large balls are uniformly small. Inside a ball partition space into finitely many sets of diameter at most \(\eta\), choosing boundaries of zero limiting measure. Weak convergence makes their masses converge. Couple the common mass within each partition cell, at cost at most \(\eta^2\), and couple the remaining masses arbitrarily. The unmatched mass inside the ball vanishes; its cost is bounded by the squared diameter of the ball times that mass. The tails have arbitrarily small cost by \(|x-y|^2\le2|x|^2+2|y|^2\). Sending the ball radius and then the partition resolution to their limits proves the claim. A countable family of bounded Lipschitz tests determines weak convergence, by approximation on compact balls and tightness. For random measures the same argument applies in probability, or along an almost surely convergent subsubsequence of every subsequence.

Two arrays on the same neuron indices satisfy
\[
\mathcal W_2^2(\widehat\mu_n,\widehat\nu_n)
\le\frac1n\sum_\alpha |X_{n,\alpha}-Y_{n,\alpha}|^2,
\tag{F.3}
\]
using the coupling that pairs equal indices. These facts require no assertion that trained coordinates are independent.

## 2. An explicit Gaussian operator norm bound

**Lemma F.2.** For an \(n\times n\) matrix \(W_n\) with independent \(N(0,1/n)\) entries,
\[
\Pr(\|W_n\|_{\rm op}>10)
\le 2\,9^{2n}e^{-100n/8}\longrightarrow0.
\tag{F.4}
\]

**Proof.** A maximal \(1/4\)-separated subset \(\mathcal N\) of the Euclidean unit sphere is a \(1/4\)-net. Balls of radius \(1/8\) about its points are disjoint and lie in the ball of radius \(9/8\), so volume comparison gives \(|\mathcal N|\le9^n\). For unit \(u,v\), choose \(u_0,v_0\in\mathcal N\) within \(1/4\). Then
\[
|u^TW_nv-u_0^TW_nv_0|
\le\tfrac12\|W_n\|_{\rm op}.
\]
Taking the supremum gives \(\|W_n\|_{\rm op}\le2\max_{u_0,v_0\in\mathcal N}|u_0^TW_nv_0|\). For a fixed pair the displayed scalar is \(N(0,1/n)\). Its exponential moment is \(Ee^{t u_0^TW_nv_0}=e^{t^2/(2n)}\); Markov's inequality optimized at \(t=ns\) yields \(\Pr(|u_0^TW_nv_0|>s)\le2e^{-ns^2/2}\). A union bound at \(s=5\) proves (F.4). The exponent is negative since \(2\log9<12.5\). The same bound applies to transposes, and a finite union bound handles all matrices. ∎

The same argument for a threshold \(t\ge10\) gives
\[
\Pr(\|W_n\|_{\rm op}>t)
\le2\exp\{n(2\log9-t^2/8)\}
\le2e^{-nt^2/16}\le2e^{-t^2/16}.
\tag{F.4a}
\]
Consequently every fixed positive moment is bounded uniformly in width:
\[
\sup_{n\ge1}E\|W_n\|_{\rm op}^p
\le10^p+2p\int_{10}^\infty t^{p-1}e^{-t^2/16}\,dt<\infty.
\tag{F.4b}
\]
The integration formula follows by writing \(X^p=\int_0^Xpt^{p-1}dt\) for nonnegative \(X\) and interchanging nonnegative integrals. Hölder's inequality then gives uniform fixed-order moments for every fixed polynomial in finitely many such operator norms. For a standard Gaussian vector \(g_n\), Jensen's inequality also gives \(E\|g_n\|_n^p\le E|G|^p\) when \(p\ge2\).

A useful consequence identifies normalized traces without a concentration theorem for functions of matrix entries. Let \(T_n\) be any random real \(n\times n\) matrix independent of \(g_n\sim N(0,I_n)\), with \(\sup_nE\|T_n\|_{\rm op}^2<\infty\). Conditional on \(T_n\),
\[
E_g\langle g_n,T_ng_n\rangle_n=\frac1n\operatorname{tr}T_n,
\quad
\operatorname{Var}_g\langle g_n,T_ng_n\rangle_n
=\frac{2}{n^2}\left\|\frac{T_n+T_n^T}{2}\right\|_F^2
\le\frac{2}{n}\|T_n\|_{\rm op}^2.
\tag{F.4c}
\]
To verify the variance, replace \(T_n\) by its symmetric part, diagonalize it orthogonally, and use that the transformed Gaussian coordinates are independent with \(\operatorname{Var}(G^2)=2\). Therefore the difference between this probe and the normalized trace tends to zero in \(L^2\). If the probe is a fixed finite program, Theorem F.1 identifies its deterministic limit and hence the trace limit in probability. A fixed polynomial in the initialized actions and their adjoints satisfies the operator moment hypothesis by (F.4b), and its application to the probe is such a program. Uniform moments of order greater than one upgrade convergence of these normalized traces to convergence of their expectations: split at a large absolute threshold and use the higher-moment bound to make the first-moment tails uniformly small. The same observation supplies uniform integrability of every fixed polynomial expression needed for finite-degree moment calculations.

## 3. Exact adaptive Gaussian conditioning

Let the current transcript consist of all revealed roots and all previously computed vectors. For one matrix \(W\), collect its earlier forward and reverse observations as
\[
WV=Y,\qquad W^TU=Q.
\tag{F.5}
\]
The columns of \(V\) and \(U\) are the respective query inputs, with output columns in \(Y\) and \(Q\). Conditioned on the transcript they are fixed. Empty column lists are allowed; terms involving them are omitted.

It is necessary to justify this conditioning for adaptive inputs. Initially the conditional laws of the matrices are independent Gaussian laws. Suppose this is true, with the linear constraints already observed, at a particular instruction. A coordinate operation is measurable from the transcript and reveals no new randomness. At a matrix call its input is also measurable from the transcript. Conditional on the transcript, the new answer is a linear observation of only the queried matrix. Conditioning a product of the current conditional laws on this observation leaves the other factors unchanged and conditions only the queried factor. Thus induction preserves independence of the residual matrix factors and adds exactly the indicated linear constraint. A freshly revealed independent root likewise does not alter these residual laws. This argument conditions successively, and does not assume that an adaptive input was independent of the matrix before the transcript was fixed.

Suppose first that \(V^TV\) and \(U^TU\) are invertible. Let \(P_V=V(V^TV)^{-1}V^T\), and similarly define \(P_U\). Then
\[
W\mid\mathcal H\ \overset d=
M+P_{U^\perp}\widetilde W P_{V^\perp},
\quad
M=Y(V^TV)^{-1}V^T
 +U(U^TU)^{-1}Q^TP_{V^\perp},
\tag{F.6}
\]
where \(\widetilde W\) is an independent copy of the original matrix.

Here is a direct verification of the Gaussian projection behind (F.6). The compatibility relation is \(U^TY=Q^TV\), because both sides equal \(U^TWV\). It gives \(MV=Y\) and \(M^TU=Q\). The homogeneous solutions of (F.5) are exactly matrices \(K=P_{U^\perp}KP_{V^\perp}\). Both summands defining \(M\) are orthogonal in Frobenius inner product to that subspace. Hence \(M\) is the unique minimum-Frobenius-norm solution. Vectorize \(W\), whose law is an isotropic Gaussian in \(\mathbb R^{n^2}\). In an orthonormal basis adapted to the homogeneous solution subspace its coordinates are independent Gaussians; conditioning on the orthogonal coordinates leaves independent Gaussians on the homogeneous subspace and fixes the other coordinates to those of \(M\). This proves (F.6). It also proves the same assertion with orthogonal projections and minimum-norm solutions when column lists are linearly dependent; the nonsingular formula is the only one whose coefficients we take to a width limit.

For a new forward input \(h\), put
\[
\alpha_n=(V^TV)^{-1}V^Th,
\quad h_\perp=h-V\alpha_n,
\quad
\beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n).
\]
Equation (F.6) becomes
\[
Wh=Y\alpha_n+U\beta_n
 +\|h_\perp\|_nP_{U^\perp}g
\quad\hbox{in conditional law},
\tag{F.7}
\]
with \(g\sim N(0,I_n)\) independent of the transcript. The reverse formula follows by interchanging the two sides.

Assume provisionally that every query Gram has a positive definite limit. Inductively all contractions of old nodes converge. Thus the coefficients in (F.7), and \(\|h_\perp\|_n\), converge in probability to deterministic limits. Inverting a positive definite fixed-size matrix is continuous, for instance by a Neumann-series expansion about its invertible limit.

The projection removed from the fresh noise is negligible:
\[
E[\|P_Ug\|_n^2\mid\mathcal H]
=\frac{\operatorname{rank}U}{n}.
\tag{F.8}
\]
The multiplying variance factor is bounded in probability, so conditional Markov's inequality makes its contribution vanish in normalized mean square. After this removal and replacement of convergent coefficients by their limits, the new coordinate is a deterministic linear combination \(m_\alpha\) of old same-layer nodes plus \(\sigma g_\alpha\).

For a bounded Lipschitz test \(\psi\) of the old tuple and this new coordinate, conditional independence of \(g_\alpha\) gives variance at most \(4\|\psi\|_\infty^2/n\) for its empirical average. Its conditional mean is the old empirical average of the bounded continuous function
\[
x\longmapsto E_G\psi(x,m(x)+\sigma G),
\]
which converges by the induction hypothesis. For the new second moment expand
\[
\frac1n\sum_\alpha(m_\alpha+\sigma g_\alpha)^2
=\|m\|_n^2+\frac{2\sigma}{n}\sum_\alpha m_\alpha g_\alpha
 +\frac{\sigma^2}{n}\sum_\alpha g_\alpha^2.
\]
The middle term has conditional variance \(4\sigma^2\|m\|_n^2/n\), and the last average has variance \(2/n\). All relevant norms are bounded in probability. We obtain weak convergence and second-moment convergence, hence (F.2). Coordinate instructions preserve this convergence because their Lipschitz constants bound the transport cost. This completes the induction under the provisional positive-definiteness assumption.

## 4. Source-response identity and formal derivatives

For every oriented initialized matrix introduce a centered Gaussian source group indexed by its calls. Sources for different orientations, including a matrix and its transpose, are independent groups; they are also independent of the root tuples. Within a forward group for \(W\), the source attached to input \(h\) has covariance with the source attached to input \(v\) equal to \(E[hv]\). Within the reverse group the analogous covariance is \(E[uv]\) for the corresponding reverse inputs. These are uncentered second moments of inputs and centered covariances of sources.

The scalar node of a new forward call is
\[
\mathscr W h=\xi_h+\sum_{s:\,W^Tu_s\text{ already called}}
 u_s\,E[\partial_{\zeta_s}h].
\tag{F.9}
\]
The scalar node of a reverse call is
\[
\mathscr W^*u=\zeta_u+\sum_{r:\,Wv_r\text{ already called}}
 v_r\,E[\partial_{\xi_r}u].
\tag{F.10}
\]
An input is its explicit expression in named source coordinates and roots, obtained by unrolling previous scalar instructions. A derivative in (F.9) or (F.10) differentiates that expression. Previously computed expectations, coefficients, covariance entries, mesh sizes, and any deterministic control values are held fixed. Each named source remains a separate formal argument, including when the joint source covariance is singular. An unavailable source has derivative zero. Derivative paths through other matrices' earlier calls remain part of the expression.

The recursion is causal. At a call, its input and its source derivatives are already defined; their expectations determine the response coefficients. The source covariance extension is the Gram extension of the corresponding input list and is therefore positive semidefinite. A Gaussian group with that extended covariance exists: if the old covariance is \(K\), the new cross-covariance is \(b\), and the new variance is \(v\), positivity implies \(b\in\operatorname{ran}K\) and \(v-b^TK^+b\ge0\). To see the range assertion, test positivity on \((tu,1)\) with \(Ku=0\) and arbitrary \(t\). Completing the square on \(\operatorname{ran}K\) gives the second assertion. Consequently the new coordinate can be represented as \(b^TK^+\xi+\sqrt{v-b^TK^+b}\,G\), with a fresh standard normal \(G\). Here a pseudoinverse is used only to construct one fixed finite Gaussian law; no continuity of pseudoinverses is asserted.

**Lemma F.3 (source rule).** Under the positive-definiteness assumption of Section 3, (F.9) and (F.10) give exactly the scalar laws obtained there.

**Proof.** Consider a forward call and use the notation of (F.7). Write old forward inputs as \(v_r\), old reverse inputs as \(u_s\), and their scalar outputs, by induction, as
\[
y_r=\xi_r+\sum_s D_{rs}u_s,
\qquad D_{rs}=E[\partial_{\zeta_s}v_r],
\]
\[
q_s=\zeta_s+\text{a deterministic linear combination of old }v_r.
\]
All old source lists are padded by zeros for unavailable indices. Let \(\alpha\) be the limiting least-squares coefficient from (F.7), and let \(h_\perp=h-\sum_r\alpha_rv_r\). Orthogonality gives \(E[v_rh_\perp]=0\). Therefore
\[
E[q_sh_\perp]=E[\zeta_sh_\perp].
\tag{F.11}
\]
Let \(G_U=(E[u_su_t])_{st}\), the covariance matrix of \(\zeta\). Gaussian integration by parts gives
\[
E[\zeta h_\perp]=G_U E[\nabla_\zeta h_\perp].
\tag{F.12}
\]
For completeness, the one-dimensional identity \(E[Gf(G)]=E[f'(G)]\) follows by integration by parts against the standard normal density. The boundary term vanishes for a function of at most linear growth with bounded derivative. Represent a possibly singular Gaussian vector as \(\zeta=T G\), apply this identity in each independent standard normal coordinate of \(G\), and sum using \(TT^T=G_U\). Conditioning on independent roots and the other source groups proves (F.12) in the present setting. Every derivative is integrable: at a fixed finite instruction, its norm is bounded by a deterministic finite expression in earlier coefficients and the bounded derivatives of coordinate maps.

The limiting coefficient of \(U\) in (F.7) is consequently
\[
\beta=E[\nabla_\zeta h]-\sum_r\alpha_r E[\nabla_\zeta v_r].
\]
Substitution of the old \(y_r\) decompositions in (F.7) cancels the second term exactly. The answer becomes
\[
\xi_h+\sum_su_sE[\partial_{\zeta_s}h],
\qquad
\xi_h=\sum_r\alpha_r\xi_r+\sigma G,
\quad \sigma^2=E[h_\perp^2].
\]
Since the old \(\xi\) covariance is the Gram of the \(v_r\),
\[
E[\xi_h\xi_r]=E[hv_r],
\quad
E[\xi_h^2]=E\Big(\sum_r\alpha_rv_r\Big)^2+E[h_\perp^2]=E[h^2].
\]
The fresh normal is independent of all old roots and source groups. Thus adjoining it preserves independence of distinct oriented source groups. The reverse calculation is the same after interchanging the two layers. Interleaving calls of different matrices does not alter this calculation, because Section 3 established the conditional independence of their residual factors. ∎

Independence of source groups does not assert that the answers of a matrix and its transpose are independent. Their response terms encode their dependence. Nor does it assert that a source is independent of all later inputs; later scalar inputs can be functions of that source.

## 5. Singular queries without a rank-stability assumption

**Lemma F.4 (regularization of a fixed program).** The conclusions of Theorem F.1 and the formulas (F.9)–(F.10) hold when any of the limiting input Grams is singular.

**Proof.** For every matrix call introduce a new independent standard Gaussian input vector \(\chi\), revealed immediately before that call, and replace its input \(h\) by \(h+\varepsilon\chi\). Each call has a distinct noise vector. The other instructions are unchanged.

At fixed \(\varepsilon>0\), the new noise is independent of the old transcript and of the unperturbed part of the current input. If \(V\) is the list of prior same-orientation inputs, the normalized squared distance from \(h+\varepsilon\chi\) to \(\operatorname{span}V\) is
\[
\|P_{V^\perp}h\|_n^2
 +2\varepsilon\langle P_{V^\perp}h,\chi\rangle_n
 +\varepsilon^2\|P_{V^\perp}\chi\|_n^2.
\]
Conditionally, the cross term has variance \(4\varepsilon^2\|P_{V^\perp}h\|_n^2/n\). The last norm squared has mean \(1-\operatorname{rank}V/n\) and variance at most \(2/n\). Thus every limiting new squared distance is at least \(\varepsilon^2\). Induction gives positive definite limiting query Grams, so Sections 3–4 apply to the perturbed program. Equivalently, in its scalar law the new independent root adds \(\varepsilon^2\) to the Schur complement of the old input Gram.

Couple the perturbed and original finite programs with the same matrices and roots. On the event that all initialized matrix norms are at most 10 and that all of the finitely many fresh noise vectors have normalized norms at most 2, propagate errors instruction by instruction. A coordinate instruction multiplies the previous error by its fixed Lipschitz constant; a linear combination contributes the sum of coefficient magnitudes times previous errors; a matrix call contributes at most ten times the input error plus \(20\varepsilon\). Consequently
\[
\max_{\text{nodes }v}\|v_n^\varepsilon-v_n\|_n
\le C\varepsilon,
\tag{F.13}
\]
where \(C\) is finite and independent of \(n\) and \(0<\varepsilon\le1\). The event has probability tending to one by Lemma F.2 and the elementary second-moment calculation for Gaussian noise norms.

We next show that the scalar recursion itself is continuous at \(\varepsilon=0\); this step concerns covariances and derivatives, not inverses of empirical Grams. Induct on its finitely many instructions. Each scalar node is a \(C^1\) expression in the finite named source list and roots. If earlier deterministic coefficients remain in a compact set, the expression and its first source derivatives have uniform bounds: the expression has at most linear growth in the root and source coordinates, and its derivatives have a finite deterministic bound. This follows directly by applying the coordinate derivative bounds and the linear response formulas in the previous instructions. The values and first derivatives are continuous in their arguments and in the earlier coefficient list.

By induction, the covariance entries for the next source, which are second moments of old scalar inputs, converge as \(\varepsilon\downarrow0\). If positive semidefinite matrices \(K_j\to K\) have fixed size, then \(K_j^{1/2}\to K^{1/2}\). To verify this without a regularity assumption on eigenvalues, their positive square roots are bounded. Every convergent subsequence of these square roots has a positive semidefinite limit \(T\) with \(T^2=K\). A positive semidefinite matrix has a unique positive semidefinite square root: diagonalize it, observe that any such \(T\) commutes with \(K=T^2\), and restrict to its eigenspaces. Hence every subsequential limit is \(K^{1/2}\), which proves convergence.

Represent the full finite source prefix for each \(\varepsilon\) as \(K_\varepsilon^{1/2}G\) using one standard Gaussian vector for each oriented group, independently of the roots. This couples the source prefixes in \(L^2\). The uniform linear-growth bounds and Lipschitz constants for node expressions then give their \(L^2\) convergence. More explicitly, split the node difference into a change of arguments at fixed coefficients, bounded by the common Lipschitz constant, and a change of coefficients at fixed arguments. The latter converges pointwise and is bounded by a constant times one plus the norm of the finite root/source list, an \(L^2\) dominator. First source derivatives converge in probability and are uniformly bounded, so their expectations converge. This proves convergence of the next response coefficient and closes the induction. At zero noise the resulting expression is exactly (F.9)–(F.10) for the original formal program.

Let \(\mu^\varepsilon\) be the perturbed scalar law of a selected tuple and \(\mu^0\) the zero-noise law just constructed. We have \(\mathcal W_2(\mu^\varepsilon,\mu^0)\to0\). By (F.3), (F.13), and the proved fixed-\(\varepsilon\) limit,
\[
\mathcal W_2(\widehat\mu_n,\mu^0)
\le C_m\varepsilon
 +\mathcal W_2(\widehat\mu_n^\varepsilon,\mu^\varepsilon)
 +\mathcal W_2(\mu^\varepsilon,\mu^0)
\]
on an event of probability tending to one. Choose \(\varepsilon\) first, let \(n\to\infty\), and then let \(\varepsilon\downarrow0\). This proves the full-sequence convergence in probability, including singular Grams, and finishes Theorem F.1. ∎

The derivative convention has a precise invariant meaning on singular supports. If a source vector \(\zeta\) has covariance \(G\), and \(u\) is the vector of the associated reverse inputs with \(E[uu^T]=G\), then
\[
E[\zeta f]=G E[\nabla f],\qquad
u^Tv=0\text{ a.s. for every }v\in\ker G.
\tag{F.14}
\]
The second identity follows from \(E[(u^Tv)^2]=v^TGv=0\). If two admissible smooth formal expressions agree on the Gaussian support, their expected derivative vectors differ by an element of \(\ker G\), by the first identity. Their contracted corrections therefore agree. Individual derivative coefficients need not agree. None of this implies that pseudoinverses converge at rank loss.

## 6. Causal scalar feedback

The deterministic-coefficient theorem also identifies programs with the following causal scalar feedback. At finitely many stages, compute inner products of already available same-layer nodes, apply locally Lipschitz functions to the resulting finite scalar list, and use the resulting numbers as coefficients of subsequent linear combinations. Assume all scalar operations are defined on a neighborhood of their deterministic limiting arguments; divisions require a nonzero limiting denominator. Require the actual finite operation to be defined everywhere it is used, or assign an arbitrary measurable fallback outside that neighborhood. Convergence of its arguments makes the exceptional event have probability tending to zero. The physical algorithms themselves use no division. Coefficients may multiply unbounded vector nodes, because their perturbations can be estimated by the vector's normalized \(L^2\) norm.

To prove this extension, construct an oracle program by replacing each scalar feedback value by its limiting deterministic value, computed from earlier scalar nodes. The construction is causal and therefore not an implicit fixed-point definition. Theorem F.1 identifies this oracle. At the next scalar step use
\[
|\langle u,v\rangle_n-\langle\bar u,\bar v\rangle_n|
\le\|u-\bar u\|_n\|v\|_n
 +\|\bar u\|_n\|v-\bar v\|_n.
\tag{F.15}
\]
At the next scalar multiplication use
\[
\|c u-\bar c\bar u\|_n
\le |c|\|u-\bar u\|_n+|c-\bar c|\|\bar u\|_n.
\]
All oracle norms and finitely many oracle coefficients are bounded in probability; initial operator norms are bounded with probability tending to one. Inductively, these inequalities show that actual coefficients converge to oracle coefficients, actual node errors vanish in normalized \(L^2\), and actual norms remain bounded in probability. Local Lipschitzness of scalar operations suffices by restricting to a compact neighborhood of their deterministic limiting arguments. Equation (F.3) transfers every oracle empirical law to the actual program.

## 7. Common generated probability spaces and actual adjoints

We now fix the data and activation parameters. Construct a countable language of finite deterministic-coefficient programs. Include every root coordinate required by the model; constants; rational linear combinations; applications of the initialized matrices in both directions; the finitely many layer activations and fixed integer-level clips; and, for each arity, a countable family of bounded smooth globally Lipschitz functions dense among continuous functions on compact sets. One explicit such family is obtained by taking piecewise polynomial approximations on rational grids, multiplying by smooth compactly supported cutoffs, smoothing with fixed rational-scale mollifiers, and retaining rational coefficients and rational scales. Clipped products may be included in the same family. Close the language under finite composition. Additional countable lists of fixed programs, probes, caps, time meshes, or coefficient values can be included at the start.

This language is countable and admits a causal enumeration with finite stages. Enumerate its root slots, functions, and numerical coefficients first; at stage \(m\), add the finitely many expressions with at most \(m\) instructions using only the first \(m\) listed items, in dependency order. Every finite expression occurs at some stage. Repeated instructions may be treated as separate named copies. Running the scalar construction on this list realizes all its nodes on a product probability space with countably many independent standard Gaussian coordinates, together with the root tuples. Section 4 gives the successive Gaussian extensions, including zero conditional variance. At each layer retain only the sigma-field generated by that layer's node coordinates; call the resulting probability space \((\Omega_\ell,\mu_\ell)\) and put
\[
H_\ell=L^2(\Omega_\ell,\mu_\ell).
\tag{F.24}
\]
One can equivalently take the law of the countable tuple of generated coordinates. Its finite-dimensional marginal laws are those from Theorem F.1: any finite family is part of a finite program, and unused computations change none of the finite-width vectors. Thus different causal enumerations produce the same generated laws up to the coordinate identification. No arbitrary extra Gaussian directions are added to \(H_\ell\).

For every rational combination \(u\) of generated nodes, include its forward and reverse answer nodes. The finite inequality \(\|A_{\ell,n}u_n\|_n\le10\|u_n\|_n\) holds with probability tending to one. Both squared norms have deterministic limits by Theorem F.1, so
\[
\|\mathscr A_{\ell,0}u\|_{H_\ell}\le10\|u\|_{H_{\ell-1}}.
\tag{F.25}
\]
The same holds for every other action orientation. Linearity of the finite matrices and convergence of squared differences give linearity of the assignments: for example the limiting squared norm of the difference between the answer to \(u+v\) and the sum of answers is zero. If two expressions represent the same \(L^2\) input, (F.25) shows that their answers represent the same output. Real linearity on the real span follows either from finite real-coefficient probes or from rational approximation.

The span of generated nodes is dense in \(H_\ell\). Here are the measure-theoretic details. Cylinder sets depending on finitely many coordinates generate its sigma-field. The sets whose indicators can be approximated in \(L^2\) by finite linear combinations of cylinder indicators form a monotone class: under increasing unions or decreasing intersections, indicator convergence in \(L^2\) follows from the continuity of probability measures. They contain the cylinder algebra, hence all generated measurable sets. Simple functions and truncation then approximate every \(L^2\) variable by functions of finitely many coordinates. For a finite Borel probability law on \(\mathbb R^m\), bounded continuous functions are dense in \(L^2\): approximate an indicator by a compact subset inside an open superset whose probability difference is small, and use the continuous distance-ratio function that is one on the compact set and zero outside the open set. Such compact/open approximations follow by first restricting to large boxes and then approximating Borel sets using finite unions of rational boxes; their class is again a monotone class. Finally approximate bounded continuous functions on compact boxes by the included smooth family and control the complement by boundedness and its small probability. All approximants are generated nodes or linear combinations of them.

Consequently (F.25) extends uniquely by \(L^2\) completion to a bounded linear map
\[
A_{\ell,0}:H_{\ell-1}\to H_\ell,\qquad
\|A_{\ell,0}\|\le10,\qquad 2\le\ell\le L.
\tag{F.26}
\]
The reverse assignments extend in the same way. At finite width,
\(\langle v_n,A_{\ell,n}u_n\rangle_n=\langle A_{\ell,n}^Tv_n,u_n\rangle_n\).
Pass to the limiting pairwise contractions for generated \(u,v\); then use their density and the bounds (F.26). This gives
\[
\langle v,A_{\ell,0}u\rangle_{H_\ell}
=\langle A_{\ell,0}^*v,u\rangle_{H_{\ell-1}},\qquad 2\le\ell\le L.
\tag{F.27}
\]
The starred maps are therefore exactly the Hilbert-space adjoints. They are not resampled reverse matrices.

There is no contradiction between these bounded actions and Gaussian initialization. The actions describe all finite generated probes and their joint laws, including adaptive probes. They are not an assertion that every random \(L^2\) input is independent of an initialized action. An adaptive input generally has the response correction in (F.9).

Fixed programs with arbitrary real coefficients and arbitrary globally Lipschitz coordinate instructions are represented on these same spaces. Approximate their coefficients by rationals and their coordinate functions on larger compact sets by the dense family. For a Lipschitz target \(g\), select bounded smooth approximants \(g_m\) with accuracy \(1/m\) on the radius-\(m\) ball and a common envelope \(|g_m(x)|\le C(1+|x|)\). Cutting off \(g\) on the radius-\(2m\) ball, mollifying at a sufficiently small scale, and rationally approximating on that ball gives such a sequence with a slightly enlarged fixed envelope. Choose the countable dense family to include these rational cutoff approximants. At a fixed scalar input, the approximation error tends to zero in \(L^2\) by linear growth and the input's finite second moment. Inductively propagate these errors: every matrix call uses the norm bound 10, and each target coordinate instruction uses its Lipschitz bound to control a change of input before approximating the instruction at the limiting input. The identical finite-array error argument holds in probability by Theorem F.1 and convergence of the required tail second moments. This proves the agreement of the common-space calculation with its fixed-program width limit.

## 8. Hilbert–Schmidt increments and the raw state space

For Hilbert spaces \(H,K\), the Hilbert–Schmidt norm of an operator \(T:H\to K\) is
\[
\|T\|_{\rm HS}^2=\sum_j\|Te_j\|_K^2,
\tag{F.28}
\]
where \((e_j)\) is an orthonormal basis. This value does not depend on the basis: expand each scalar coefficient \(\langle Te_j,f_k\rangle\) in a basis \((f_k)\) of \(K\), use Parseval twice, and interchange the nonnegative double sum. In particular \(\|T\|_{\rm op}\le\|T\|_{\rm HS}\), since for a unit vector completed to an orthonormal basis its image squared norm is one summand of (F.28). The normed space of such operators is complete: a Cauchy sequence has Cauchy matrix coefficients in \(\ell^2\) of two basis indices, whose limit defines an operator by Cauchy–Schwarz and has the limiting Hilbert–Schmidt norm.

For \(u\in K,v\in H\), define
\[
(u\otimes v)q=u\langle v,q\rangle_H.
\]
Parseval gives
\[
\|u\otimes v\|_{\rm HS}=\|u\|_K\|v\|_H,
\quad
(u\otimes v)^*=v\otimes u,
\tag{F.29}
\]
and
\[
\|u\otimes v-\tilde u\otimes\tilde v\|_{\rm HS}
\le\|u-\tilde u\|\|v\|+\|\tilde u\|\|v-\tilde v\|.
\tag{F.30}
\]
For a Hilbert–Schmidt \(T\), expansion in an orthonormal basis also gives
\[
\langle u\otimes v,T\rangle_{\rm HS}=\langle u,Tv\rangle_K.
\tag{F.31}
\]
At width \(n\), using the normalized inner product on both layers, the orthonormal basis is \((\sqrt n\,e_j)_{j=1}^n\); (F.28) is then the ordinary Frobenius norm of the matrix. The rank-one action is \(uv^T/n\). Thus this is the exact population counterpart of the raw matrix metric.

The affine raw parameter space in the isometric first coordinates is
\[
 \mathcal P=L^2(\Omega_1;\mathbb R^d)
 \times\prod_{\ell=2}^L
 (A_{\ell,0}+\mathcal S_2(H_{\ell-1},H_\ell))\times H_L,
                                                        \tag{F.32}
\]
with increment norm
\[
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\sum_{\ell=2}^L\|\Delta A_\ell\|_{\rm HS}^2
                                  +\|\Delta C\|_2^2.     \tag{F.33}
\]
Only the learned action increments are Hilbert--Schmidt. This is
isometric to the original raw metric because \(w=\sqrt d W^1\).
Continuous rank-one velocities have strong integrals: their Riemann
sums are Cauchy by uniform continuity on compact intervals and
completeness. The norm of the integral is bounded by the integral of
the norm, and its derivative is the continuous integrand. Formula
(F.30) passes uniform factor convergence to HS velocity and integral
convergence. For measurable integrable velocities the same statements
follow by approximation by step functions. Thus learned forward and
reverse increments are actual adjoints throughout.

## 9. Strong multiplier continuity and the chain rule

**Lemma F.5 (bounded multiplier).** Suppose \(z_m\to z\) in probability, \(v_m\to v\) in \(L^2\), and \(b\) is bounded and continuous. Then
\[
b(z_m)v_m\longrightarrow b(z)v\quad\hbox{in }L^2.
\tag{F.34}
\]

**Proof.** The term \(b(z_m)(v_m-v)\) has norm at most \(\|b\|_\infty\|v_m-v\|_2\). For the remaining term first restrict to \(|v|\le M\); bounded convergence in probability implies convergence in \(L^2\) of the bounded multiplier difference there. The complement has squared norm at most \(4\|b\|_\infty^2E[|v|^2 1_{|v|>M}]\). Send \(m\) to infinity and then \(M\) to infinity. Bounded convergence in probability used here follows from the elementary estimate \(E|X_m|^2\le\eta^2+K^2\Pr(|X_m|>\eta)\) when \(|X_m|\le K\). ∎

**Lemma F.6 (strong chain rule along curves).** Let \(z:I\to L^2(\Omega)\) be strongly \(C^1\), and let \(\phi\in C^1(\mathbb R)\) have bounded derivative. Then \(\phi(z(t))\) is strongly \(C^1\), with
\[
\frac d{dt}\phi(z(t))=\phi'(z(t))\dot z(t).
\tag{F.35}
\]

**Proof.** Set \(v_h=(z(t+h)-z(t))/h\to\dot z(t)\) in \(L^2\). The scalar fundamental theorem of calculus gives
\[
\frac{\phi(z(t+h))-\phi(z(t))}{h}
=v_h\int_0^1\phi'(z(t)+rh v_h)\,dr.
\]
The multiplier is bounded by \(\|\phi'\|_\infty\). It converges in probability to \(\phi'(z(t))\): \(|hv_h|\to0\) in probability; restrict \(z(t)\) to a large compact interval and use uniform continuity of \(\phi'\) on a slightly larger interval. The proof of Lemma F.5 applies to this bounded convergent multiplier, and yields the derivative. Lemma F.5 applied to \(z(t),\dot z(t)\) also proves continuity of the resulting velocity. ∎

This conclusion is a curve chain rule, and makes no claim that the pointwise nonlinear map is Fréchet differentiable from all of \(L^2\) to \(L^2\). Bounded \(\phi'\) is sufficient for the curve result. A jointly measurable velocity may also be integrated coordinatewise: Fubini and \(E\int_I|v(t)|^2dt<\infty\) give absolutely continuous coordinate paths almost surely, agreeing with the \(L^2\) integral. This permits the ordinary scalar chain rule almost everywhere for an absolutely continuous \(L^2\) curve with integrable squared speed.

For bounded-operator curves \(A(t)\) differentiable in Hilbert–Schmidt or operator norm and strongly differentiable \(h(t)\in H\),
\[
\frac d{dt}[A(t)h(t)]=\dot A(t)h(t)+A(t)\dot h(t).
\tag{F.36}
\]
Subtract the proposed derivative from the difference quotient. The first error is the operator derivative error applied to fixed \(h(t)\); the second is a uniformly bounded operator applied to the strong derivative error of \(h\); and the cross product is bounded by \(\|A(t+h)-A(t)\|\,\|(h(t+h)-h(t))/h\|\), which tends to zero. This proves (F.36).

## 10. Scalar prediction and feature energy are continuously differentiable

Let \(\rho_\ell\in C^2(\mathbb R)\) have bounded first and second
derivatives for each of the finitely many layers. They may have
nonzero offsets and different bounds at different layers. Define
\(Y_i^1=w\cdot u_i\), \(X_i^\ell=\rho_\ell(Y_i^\ell)\),
\(Y_i^\ell=A_\ell X_i^{\ell-1}\) for \(\ell\ge2\), and
\(F_i=\langle C,X_i^L\rangle_L\). Put
\[
 q_i^L=C,\quad d_i^\ell=\rho_\ell'(Y_i^\ell)q_i^\ell,
 \quad q_i^\ell=A_{\ell+1}^*d_i^{\ell+1}\ (\ell<L).
                                                        \tag{F.38}
\]
**Theorem F.7.** The scalar map \(F_i:\mathcal P\to\mathbb R\)
is continuously Fréchet differentiable, with
\[
 dF_i[\Delta\theta]
 =\langle d_i^1,u_i\cdot\Delta w\rangle_1
  +\sum_{\ell=2}^L\langle d_i^\ell,
                         \Delta A_\ell X_i^{\ell-1}\rangle_\ell
  +\langle X_i^L,\Delta C\rangle_L,                       \tag{F.39}
\]
and raw gradient blocks
\[
 \nabla_w F_i=d_i^1u_i,\qquad
 \nabla_{A_\ell}F_i=d_i^\ell\otimes X_i^{\ell-1},\qquad
 \nabla_C F_i=X_i^L.                                     \tag{F.40}
\]
**Proof.** For a fixed \(v,z\in L^2\), a function \(\rho\) with
\(L_1=\|\rho'\|_\infty,L_2=\|\rho''\|_\infty<\infty\), and
an increment \(q\in L^2\), its scalar Taylor remainder obeys both
\(L_2|q|^2/2\) and \(2L_1|q|\) bounds. Hence
\[
 |E[v\{\rho(z+q)-\rho(z)-\rho'(z)q\}]|
 \le \tfrac12L_2M\|q\|_2^2
   +2L_1\|v\mathbf1_{|v|>M}\|_2\|q\|_2
                         =o(\|q\|_2),                   \tag{F.41}
\]
where first \(q\to0\) at fixed \(M\), then \(M\to\infty\).

On a raw neighborhood, forward induction bounds every field
increment by \(O(\eta)\), with \(\eta=\|\Delta\theta\|_{\rm raw}\):
the bottom is linear, every activation is Lipschitz, and
\(\Delta(A X)=\Delta A X+A\Delta X+\Delta A\Delta X\),
with \(\|\Delta A\|_{\rm op}\le\eta\). Start from
\(\Delta F_i=\langle\Delta C,X_i^L\rangle+
\langle C,\Delta X_i^L\rangle+O(\eta^2)\).
At level \(\ell\), apply (F.41) with fixed incoming weight
\(q_i^\ell\) to replace its weighted feature difference by
\(\langle d_i^\ell,\Delta Y_i^\ell\rangle\), at cost
\(o(\eta)\). If \(\ell\ge2\), expand its action difference;
its mixed term is \(O(\eta^2)\), and adjunction changes the
remaining propagated term to
\(\langle q_i^{\ell-1},\Delta X_i^{\ell-1}\rangle\).
This is the induction invariant for the next lower level. At
\(\ell=1\) the bottom projection is exactly linear. Summing the
finitely many remainders proves (F.39). The rank-one identity
(F.31) proves (F.40). Forward continuity, Lemma F.5 at each backward
gate, bounded action continuity and (F.30) prove continuity of every
gradient block. This proves the assertion. \(\square\)

For \(H(\theta_h)=\sum_i p_i X_i^L\), the scalar functional
\(\mathcal E=\|H\|^2/2\) is also continuously Fréchet differentiable.
Indeed \(\Delta H=O(\eta)\), so
\(\Delta\mathcal E=\langle H,\Delta H\rangle+O(\eta^2)\).
Apply the same downward weighted expansion with fixed top weight
\(H\) and coefficients \(p_i\). Its gradient is precisely the
backward rank-one expression with readout replaced by \(H\).
The same multiplier continuity proves continuity of this gradient.
No Fréchet derivative of an \(L^2\)-valued Nemytskii map is used.

In the network of Part M, take \(\rho_\ell=\chi_\ell\).
The original predictors are \(f_i=a^LF_i\), so their raw gradients
are exactly \(a^L\nabla F_i\). Thus a strong solution of the stated
uncut equations is the raw Hilbert gradient flow of
\(\mathcal L=\tfrac12\sum_i(f_i-y_i)^2\), and
\[
 \dot f=-Kr,\qquad
 \dot{\mathcal L}=-\left\|\sum_i r_i\nabla f_i\right\|_{\rm raw}^2
                =-r^TKr,\quad
 K_{ij}=\langle\nabla f_i,\nabla f_j\rangle_{\rm raw}.
                                                        \tag{F.43}
\]
This establishes the true gradient/kernel identities; existence
of the uncut flow is a separate conclusion of Parts G and V.

## 11. Fixed-cap local existence and Euler approximation

For each fixed cap, the normalized backward gates in Part S are
\(C^1\) with bounded first derivatives. Forward induction and
backward substitution therefore make the raw field locally
Lipschitz on any bounded primal ball. Rank-one updates use (F.30),
and physical residual differences use (F.15). No derivative of
an uncut \(L^2\)-valued product is needed.

For an autonomous cap field with norm bound \(M_0\) and Lipschitz
constant \(L_0\) on a ball of radius \(b\), its integral map preserves
that ball and is a contraction for \(tM_0\le b\), \(tL_0<1\).
Uniformly converging Picard iterates give a unique strong \(C^1\)
solution. Bounded raw speed gives a strongly Cauchy finite endpoint,
from which the same construction continues whenever a primal bound
is available. For measurable bounded deterministic controls, the
same contraction gives a strongly absolutely continuous path and
its equation almost everywhere.

The one-step Euler defect is at most \(L_0M_0h^2/2\), by integrating
\(\|F(\theta(t+s))-F(\theta(t))\|\le L_0M_0s\).
Iteration of the discrepancy recurrence gives
\[
 \max_k E_k\le e^{L_0T}
        (E_0+\tfrac12 L_0M_0T\max_kh_k).                  \tag{F.45}
\]
The constants are width independent on a specified primal ball
and the initialized norm event. This compares a fine raw algorithm
to a fixed auxiliary transcript; the finite-program theorem is
never applied directly to a transcript growing with width.

Whenever the incoming tuple already has its joint \(\mathcal W_2\)
limit, or the later reference estimates give uniformly vanishing
incoming second-moment tails, a final value observation \(q\rho'(z)\)
is treated by clipping \(q\), applying Theorem F.1, and removing
the clip using those tails and bounded actions. Mere boundedness
of \(L^2\) norms is not substituted for this tail premise. Whenever a source derivative
of such an unbounded product is needed, the later Parts V and N
supply the stronger derivative-valid truncation argument explicitly.

# Part S. Direct controlled source estimates at all finite depths

Let psi be C2 with ||psi||infty, ||psi'||infty, ||psi''||infty <= 1. Nonconstancy is not required for this lemma. Let L>=2, 0<=e<=1, T>0, and

    a >= 10^12(1+T),   S = T a^(-L),   K_l = a^(l-1),   eps=e/a.

Use the ORIGINAL raw parameters and metric. Normalize only hidden fields:

    Y_l = z_l/a^(l-1),   X_l = h_l/a^l,
    chi_l(y) = y + [1+eps psi(K_l y)]/K_l,
    F_i = <C,X_(L,i)>,   f_i=a^L F_i.

Thus Y_l=A_l X_(l-1), with the normalized first-layer representation Y_(1,i)=<w,u_i>, ||u_i||=1. For deterministic bounded controls ||c(s)||_1<=3, the normalized controlled raw field is

    C'=sum_i c_i X_(L,i),
    A_l'=sum_i c_i d_(l,i) tensor X_(l-1,i)  (2<=l<=L),
    w'=sum_i c_i d_(1,i)u_i,
    q_L=C,   q_l=A_(l+1)^* d_(l+1),
    d_l=D_(l,R)(Y_l,q_l),
    D_(l,R)(y,q)=q+eps psi'(K_l y) tau_R(q).

The clip is C1, |tau_R(q)|<=min(|q|,2R), |tau_R'|<=1, and equals q for |q|<=R. All constants below are uniform over R, positive Euler meshes of total length <=S, and deterministic choices of controls satisfying the displayed bound. Population initialization is C(0)=0. The actual finite-width random readout must be retained before the fixed-cap bridge, as explained at the end.

The bounds used are exactly

    |chi_l(y)-y|<=2/K_l,  |chi_l'|<=2,
    |D(y,q)|<=2|q|,  |D_q|<=2,
    |D_y|<=eps K_l |q|<=K_l |q|,
    |D_y|<=2 eps K_l R.

In particular psi' and psi'' may change sign.

## S.1. Exact finite-program input and local equations

The input theorem required from Part F is this: a fixed finite program built from independent normalized Gaussian adjacent matrices, both orientations of each matrix, independent Gaussian roots, C1 coordinate maps with bounded continuous derivatives, and causal scalar contractions has a canonical scalar Gaussian-source law. A forward answer on input h equals its centered source plus earlier reverse inputs multiplied by their expected named-source derivatives of h. The reverse rule interchanges the two sides and includes current forward calls. Each source covariance is the FULL uncentered input Gram. Distinct oriented Gaussian source groups are independent. Named derivatives freeze all source covariances, scalar contractions, previously produced response coefficients, meshes, and controls; named slots stay distinct at singular covariance. These are the source identities (F.9)--(F.10) and Lemma F.4 proved in Part F above. Fixed caps satisfy all of its coordinate hypotheses because psi is C2 and the four displayed gate derivative bounds hold.

Apply this input chronologically to one finite Euler program. At layer l the exact local equations are

    Y_l = xi_l + Acal_l d_l,
    q_l = zeta_l + Bcal_(l+1) X_l,
    X_l = chi_l(Y_l),   d_l = D_(l,R)(Y_l,q_l).

Here Acal_l is strictly lower triangular in time and Bcal_(l+1) is lower triangular, including its diagonal. At the bottom xi_1 is the repeated initialized Gaussian root and

    Acal_(1,kj)=h_j Gamma diag(c_j),   j<k.

At the top zeta_L=0 and Bcal_(L+1) is the strictly past readout integrator, replicated over the three samples. Its full block-row norm is <=3S.

For internal matrices the exact response coefficients, with sample indices u,v, are

    (Acal_(l+1,kj))_(uv)
       = E partial_(zeta_(l,j,v)) X_(l,k,u)
         + h_j c_(j,v) E[X_(l,k,u) X_(l,j,v)] ,  j<k,

    (Bcal_(l,kj))_(uv)
       = E partial_(xi_(l,j,v)) d_(l,k,u)
         + 1_(j<k) h_j c_(j,v) E[d_(l,k,u) d_(l,j,v)] ,  j<=k.

The learned contractions follow by unrolling the rank-one parameter increments. The response terms are the source rule just stated. These identities hold at the actual coefficient arrays; no comparison covariance or replacement transpose law is introduced.

For a three-by-three block use its induced infinity norm. For a row use the SUM of its block norms. Write a local strict density bound as |Acal_(l,kj)|<=alpha h_j, and a full causal row bound as sum_(j<=k)|Bcal_(l+1,kj)|<=b. Set r=alpha S b.

## S.2. Independent primal bounds

Use initialized adjacent action norms <=10 and initial first-layer projection norms <=2. These bounds follow from the elementary net argument proved in Part F: a one-quarter net on each unit sphere has cardinality at most 9^n, and the net approximation gives ||W||op <= 2 max_(u,v in nets)|u^T Wv|. Since every fixed bilinear form is N(0,1/n), P(||W||op>10)<=2*9^(2n)*exp(-100n/8), which tends to zero. A finite union bound handles all L-1 matrices, the Gaussian law of large numbers handles the three first-layer projection norms, and passage on a countable dense generated family gives the canonical norm bound 10. No precise asymptotic spectral-norm theorem is required. Stop at hidden joint raw displacement D=1. Then current adjacent action norms are <=11 and ||Y_(1,i)||_2<=3. Put F=32^L. The offset causes no problem:

    ||X_(1,i)||_2<=3+2=5<=32,
    ||X_(l,i)||_2<=11*32^(l-1)+2<=32^l.

Consequently, for s<=S and at every Euler node,

    ||C(s)||_2<=3Fs,
    ||q_(l,i)(s)||_2<=Q_l := 32^(L-l) 3FS,
    ||d_(l,i)(s)||_2<=2Q_l,
    ||Y_(l,i)(s)||_2<=F.

Every hidden block speed is <=F||C||_2: for an internal block, the coefficient bound is 3*2*32^(L-l)*32^(l-1)=(3/16)F; the bottom is the same. Thus

    D(s)<=3 sqrt(L) F^2 s^2.

For Euler, sum_j h_j s_j <=s_k^2/2 supplies the same bound and excludes even a first overshooting node: the proposed node's update length only uses earlier states inside the stop. With a>=10^12(1+T),

    D(S)<=3 sqrt(L) (1024/a^2)^L T^2 <1/4,
    max_l Q_l <1/2.

Hence the stop is never reached and ||d_l||_2<=1. These bounds are independent of source coefficient estimates; they may be used inside a chronological source induction without circularity.

## S.3. Same-array Gaussian-part estimate, including the offset

Freeze one actual finite local prefix whose coefficient rows obey alpha,b. Write

    u_l = [1+eps psi(K_l Y_l)]/K_l,  |u_l|<=2/K_l,
    v_l = eps psi'(K_l Y_l) tau_R(q_l),  |v_l|<=|q_l|.

Then X=Y+u and d=q+v. Assume r<=1/8 and put

    Rloc=(I-Acal Bcal)^(-1),   U=Rloc Acal,
    Lloc=(I-Bcal Acal)^(-1),
    Y_G=Rloc xi + U zeta,
    q_G=Lloc zeta + Bcal Rloc xi.

These are centered Gaussian combinations of the original frozen source groups. Triangular inverses exist exactly; the geometric row bounds also give

    |Rloc|row, |Lloc|row<=2,
    |U|row<=2alpha S,   |Bcal U|row<=2r,
    |Lloc Bcal|row<=2b.

Exact elimination, with NO replacement of the actual coefficient arrays, yields

    Y-Y_G = U v + U Bcal u,
    q-q_G = Bcal U v + Lloc Bcal u.

Let m_p(q)=max_(k,i)||q_(k,i)||_p on this finite prefix. It is finite before absorption, since fixed-cap finite programs are finite globally Lipschitz Gaussian expressions. The identities imply

    m_p(q-q_G)<=2r m_p(q)+4b/K_l,
    m_2(q_G)<=(1+2r)Q_l+4b/K_l<=2Q_l+4b/K_l.

Each q_G coordinate is Gaussian with its ACTUAL covariance, so ||q_G||_p<=sqrt(p)||q_G||_2 for p>=2. Absorb 2r m_p(q), retaining the bounded non-Gaussian remainder, to obtain

    m_p(q)<=20(Q_l+b/K_l)sqrt(p),   p>=2.                 (S.1)

For the local curvature multiplier N_k=K_l max_i|q_(k,i)| this gives

    ||N_k||_p <= W_l sqrt(p),
    W_l=60(n_l+b),   n_l=K_l Q_l.                       (S.2)

The factor 3 in W_l merely bounds the norm of the maximum by the sum of the three marginal norms. No random time maximum is used.

The other exact identity and the independent actual bound ||Y||_2<=F likewise give

    max_(k,i)||Y_(k,i)||_p
        <=[F+50alpha S(Q_l+b/K_l)]sqrt(p).               (S.3)

Indeed ||Y-Y_G||_p<=2alpha S m_p(q)+4alpha S b/K_l; use this at p=2 to bound the Gaussian variance by F+2alpha S Q_l+4alpha S b/K_l and then use (S.1). The coefficient 50 exceeds the resulting coefficients 42 for Q_l and 44+4/sqrt(2) for b/K_l. In the box below the bracket is <=2F, hence ||X_(k,i)||_p<=4F sqrt(p).

This calculation isolates why the offset is harmless: its size is 1/K_l, exactly the inverse scale of the possible curvature K_l. The remainder estimate 4b/K_l therefore gives the displayed constants 20 and 60.

## S.4. Derivative rows and production bounds

Set G=diag chi_l'(Y), V=diag D_q(Y,q), and N=diag D_y(Y,q). Their norms obey |G|,|V|<=2 and |N_k|<=K_l max_i|q_(k,i)|. For any named source, the exact Y-Jacobian satisfies

    J=I_xi + Acal [N J + V(I_zeta+Bcal G J)].

The current Bcal diagonal remains in this identity. Strictness of Acal ensures that J at time k depends on this bracket only at strictly earlier times.

Let E_k denote

    E_k=exp[4alpha b S + alpha sum_(r<k)h_r K_l max_i|q_(r,i)|].

For derivatives in the full xi row, take block-row norms in the exact recurrence and let M_j be the running maximum of preceding Jacobian row norms. This gives

    |J_k|row <=1+alpha sum_(j<k) h_j (N_j+4b) M_j.

The discrete product bound product_(j<k)[1+alpha h_j(N_j+4b)]<=E_k proves

    |partial_xi Y_k|row<=E_k.

For one reverse source slot zeta_j, its direct forcing of d_j is bounded by 2, its first effect on Y_k by 2alpha h_j, and all later effects obey the same Volterra recurrence. Therefore

    |partial_(zeta_j)Y_k|<=2alpha h_j E_k,   j<k,
    |partial_(zeta_j)X_k|<=4alpha h_j E_k,
    |partial_xi d_k|row<=(K_l max_i|q_(k,i)|+4b)E_k.     (S.4)

These are pointwise bounds on actual named derivatives.

For completeness, if ||Z||_p<=M sqrt(p) for all p>=2, expansion of exp(Z^2/(4 exp(1)M^2)) and k!>=(k/exp(1))^k gives expectation <=2. Young's inequality then gives, in particular,

    E exp(u|Z|)<=2 exp(2 exp(1)M^2 u^2),   u>=0.

Minkowski applied to the weighted time sum in E_k gives its p-norm <=S W_l sqrt(p). Hence no temporal independence or path-maximum moment is needed. If

    alpha S b<=10^-9,   alpha S W_l<=10^-6,

then

    E E_k <=4,
    [E E_k^2]^(1/2)
      <=sqrt(2) exp[4alpha b S+4 exp(1)alpha^2 S^2 W_l^2].

Taking expectations in (S.4) and adding the learned contractions yields

    alpha_(l+1,new)<=3F^2+16alpha,
    b_(l-1,new)<=512(n_l+b)+3S.                          (S.5)

For the second bound the response row is at most

    sqrt(2)(sqrt(2)W_l+4b)
       exp[4alpha b S+4 exp(1)alpha^2 S^2 W_l^2]
       <512(n_l+b).

The forward learned density is <=3F^2. The reverse learned row is <=3S because ||d_l||_2<=1. All displayed norms bound the absolute values of signed response coefficients; no coefficient signs have been discarded from the actual identities.

## S.5. Explicit depth-independent gain condition

Keep F=32^L and define

    n_l=3F(T/a)(32/a)^(L-l),   nmax=3FT/a,
    B0=nmax+3S<=4FT/a,
    alpha_l=32^l *3F^2,
    b_l=2048^(L-l+1) B0,   1<=l<=L.

Here alpha_l bounds Acal_l and b_l bounds the incoming Bcal_(l+1), so outgoing reverse production at layer l is compared with b_(l-1). The top row 3S and bottom density 3 lie strictly inside their respective radii. Exact algebra gives

    alpha_l S<=3(32768/a)^L T,
    alpha_l S b_l
       <=24576(67108864/a)^L 64^(-l) T^2/a
       <=384(67108864/a)^L T^2/a.

Since a>=10^12(1+T), L>=2, and l>=1, these imply

    alpha_l S<10^-8,
    alpha_l S b_l<10^-10,
    alpha_l S W_l<10^-8.

For the second assertion one may bound by the L=2 case and use sup_(T>=0)T^2/(1+T)^3=4/27: the bound is <2.57*10^-19. Also n_l<=B0<=b_l/2048, so W_l<=61b_l and the last assertion follows. The forward bracket in (S.3) is <=F+25alpha_l S+50alpha_l S b_l<=2F, because Q_l<=1/2 and K_l>=1.

Thus every production estimate is strictly inside the next box:

    3F^2+16alpha_l<=17alpha_l<32alpha_l=alpha_(l+1),
    512(n_l+b_l)+3S<514b_l<2048b_l=b_(l-1).              (S.6)

The constants do not require any upper bound on L, and e enters only through eps=e/a<=1.

## S.6. Full chronological induction, without an unknown-current-row premise

Use the actual stage order at each time k:

    Acal_(2,k),...,Acal_(L,k),
    Bcal_(L,k),...,Bcal_(2,k).

The induction invariant is: every completed time row satisfies its alpha_l,b_l radius; its corresponding q_l fields satisfy (S.1)--(S.2); and the independent primal bounds of Section S.2 hold. At a partially completed current row, the radius bound is asserted only for coefficients already constructed.

At k=0 all forward response rows are empty. C_0=0, so the top backward field and its xi-derivative vanish. Thus Bcal_(L,0)=0, and successive reverse stages give zero current q and reverse responses down to layer 1. Named zero-variance slots are still retained formally. This starts the invariant.

At the next time k, the bottom Y_1,k is already determined by the initialized root and past d_1. Suppose current forward rows have been built through Acal_(l,k), so Y_l,k and X_l,k are available. To construct Acal_(l+1,k), the response derivative of X_l,k in zeta_l,j with j<k uses q_l,r and Bcal_(l+1,r) ONLY FOR r<k. This is an exact consequence of strictness of Acal_l: every occurrence of q in Y_l,k comes through d_l,r with r<k. Apply the local moment estimate to the fully completed prefix through k-1, then apply the source derivative recurrence at current k. The bound 4alpha_l h_j E_k and its expectation require only this past information. The learned contraction uses the already proved primal bounds. Consequently the first estimate of (S.5) constructs Acal_(l+1,k) strictly inside alpha_(l+1). No current Bcal_(l+1,k), q_l,k, or d_l,k estimate has been used. This closes all current forward rows in ascending order.

The current top incoming row is the readout integrator, already bounded by 3S. The current top q_L=C is now available. On the complete local prefix through k, all Acal_L and incoming Bcal_(L+1) rows are therefore known and satisfy their bounds. Sections S.3--S.4 now apply to this prefix and produce Bcal_(L,k) strictly inside b_(L-1). The current q_(L-1) is then available with this newly bounded incoming row. The same complete-prefix calculation produces Bcal_(L-1,k). Continue downward. At every reverse stage, the current Acal_l row was constructed in the forward sweep, and the current incoming Bcal_(l+1) row was constructed in the preceding higher reverse stage. Therefore every hypothesis is established before it is used. The final bottom q_1 estimate completes the invariant.

This proves the actual coefficient box and moment estimates on every finite mesh. It uses no minimum step length and never bootstraps a current unknown row from an estimate that assumes that row.

## S.7. What this gives to the global proof

For every separately fixed finite L,a,T, the constructed incoming and forward fields have marginal subGaussian moments uniformly in mesh, cap, and the bounded deterministic controls. Their formal first source derivatives have integrable envelopes uniformly in mesh and cap. The elementary subGaussian tail consequence of (S.1) supplies constants M,c>0, possibly depending on the fixed L,a,T, such that

    sup_(R,k) ||q_(l,k,i) 1_(|q_(l,k,i)|>u)||_2
        <=M exp(-c u^2).

The fixed-cap Gaussian/Euler bridge passes these estimates to controlled capped population paths. Comparing an arbitrary larger cap with a reference cap R uses

    |D_(l,R')(y,q)-D_(l,R)(y',q')|
       <=2|q-q'|+2eps K_l R|y-y'|
                         +2eps |q'|1_(|q'|>R).

Forward discrepancies are controlled first. Backward substitution therefore introduces one factor R multiplying that forward discrepancy; it does not produce R^L. On any fixed controlled interval the raw difference estimate has the form C exp(CR-cR^2). It yields strong cap removal and uniqueness against any bounded-primal uncut competitor, as proved in full in Part V below. Measurable controls give a strong absolutely continuous controlled path and the equation almost everywhere; continuous autonomous residual feedback gives the required strong C1 physical path.

The finite random readout is not set to zero in either actual training algorithm: at fixed cap its initial RMS discrepancy is O_P(n^-1), propagated by fixed-cap raw Lipschitz stability. Only after this width limit is the population initialization C_0=0 used. The finite-depth true-kernel/velocity/path conclusions still require their ordered observation-truncation and time-compactness bridge, as proved in Part V below; the present source calculation does not silently replace that bridge.

# Part G. Uniform geometry, total control time, and all-time nonaffinity

Throughout this part \(F_*=32^L\) is a numerical norm bound, distinct
from the three normalized predictors \(F_i\). All estimates apply
at each separately fixed finite \(L\ge2\). The sufficient conditions
on \(a\) will not depend on \(L\).

## G.1. The initialized Gram loses only a summable amount with depth

First we prove the elementary three-input geometric bound
\[
                  \Gamma+\mathbf1\mathbf1^T\succeq
                           \delta^2 I_3/4.                 \tag{G.1}
\]
For \(v\in\mathbb R^3\), the left quadratic form is
\((\sum v_i)^2+\|\sum v_iu_i\|^2\). If the nonzero \(v_i\) have
one sign, its first term is at least \(\|v\|^2\), which suffices
as \(\delta<1\). Otherwise change the overall sign and permute
to write \(v=(r_1,r_2,-b)\), \(r_1,r_2\ge0\), \(A=r_1+r_2>0\),
\(b>0\). Set
\[
 D=\frac{r_1(1-\Gamma_{13})+r_2(1-\Gamma_{23})}{A}
                         \in[\delta,2].
\]
Projection of \(\sum v_i u_i\) onto the unit vector \(u_3\)
gives the lower bound
\[
                    (A-b)^2+((1-D)A-b)^2.
\]
The matrix of this two-variable quadratic form has determinant
\(D^2\), trace \(D^2-2D+4\le4\), and positive eigenvalues.
Its smaller eigenvalue is at least determinant/trace, hence
\(\delta^2/4\). Finally \(A^2+b^2\ge r_1^2+r_2^2+b^2\).
This proves (G.1), without requiring an invertible \(\Gamma\).

At initialization the raw preactivation tuple at each layer is
centered Gaussian, with a common marginal standard deviation
\(\sigma_\ell\), where \(\sigma_1=1\) and
\(\sigma_{\ell+1}^2=E[\phi(\sigma_\ell G)^2]\).
This follows either directly by the forward-only case of Part F
or by conditioning each fresh Gaussian matrix on its inputs.
For a centered Gaussian tuple \(Z\) with equal marginal variance
\(\sigma^2\), Gaussian integration by parts gives
\[
 m_\sigma=E\phi(\sigma G)=a+eE\psi(\sigma G),\qquad
 \beta_\sigma=E\phi'(\sigma G)=a+eE\psi'(\sigma G).
\]
Its residual coordinates
\(\phi(Z_i)-m_\sigma-\beta_\sigma Z_i\) are orthogonal to
constants and every \(Z_j\). Indeed
\(E[Z_j\mid Z_i]=\operatorname{Cov}(Z_j,Z_i)Z_i/\sigma^2\);
this identity follows by subtracting the correlated linear
Gaussian component, and is valid for singular tuples. Integration
by parts against a Gaussian density proves the remaining
one-coordinate identity; linear growth makes its boundary term
zero. Consequently
\[
 (E[\phi(Z_i)\phi(Z_j)])_{ij}
 \succeq m_\sigma^2\mathbf1\mathbf1^T+
                   \beta_\sigma^2\operatorname{Cov}(Z).
                                                               \tag{G.2}
\]
In particular, \(m_\sigma,\beta_\sigma\ge a-e\ge a/2\), and
\[
 (a/2)^{\ell-1}\le\sigma_\ell\le4a^{\ell-1}.             \tag{G.3}
\]
For the lower bound use the diagonal of the linear projection
in (G.2). For the upper bound, Minkowski and \(|\psi|\le1\)
give \(\sigma_{\ell+1}\le a\sigma_\ell+2a\). Dividing by
\(a^\ell\) and summing the geometric series yields
\(\sigma_\ell/a^{\ell-1}\le1+2\sum_{j=0}^{\ell-2}a^{-j}
\le1+2a/(a-1)<4\) for \(a\ge4\).

A worst-case lower derivative bound at each layer would lose
a fixed factor at every layer. Boundedness of \(\psi\) improves
this estimate. Another integration by parts gives
\[
 |E\psi'(\sigma G)|=
       \frac{|E[G\psi(\sigma G)]|}{\sigma}\le\frac1{\sigma}.
                                                               \tag{G.4}
\]
Define \(d_\ell=a^{-1}(2/a)^{\ell-1}\). Let \(Q_\ell(0)\)
be the Gram of the normalized initialized features \(X_i^\ell\).
The normalized linear projection coefficient at layer \(\ell\)
is \(\beta_{\sigma_\ell}/a\ge1-d_\ell\); the normalized
constant coefficient at layer 1 is at least \(1-d_1\).
Equation (G.2), after dividing the feature Gram by \(a^{2\ell}\),
therefore gives
\[
 Q_1(0)\succeq(1-d_1)^2(\Gamma+\mathbf1\mathbf1^T),\qquad
 Q_\ell(0)\succeq(1-d_\ell)^2Q_{\ell-1}(0)\quad(\ell\ge2).
\]
For numbers in \([0,1]\), induction gives
\(\prod_{j=1}^m(1-d_j)\ge1-\sum_{j=1}^m d_j\). Since
\(\sum_{\ell\ge1}d_\ell=1/(a-2)\le1/2\), (G.1) proves
\[
                  Q_L(0)\succeq
             \tfrac14(\Gamma+\mathbf1\mathbf1^T)
                          \succeq\lambda I_3,\qquad
                  \lambda=\delta^2/16,                    \tag{G.5}
\]
uniformly in all finite depths.

## G.2. Controlled primal estimates and their exact scale

Let \(\tau_R\) be an odd \(C^1\) clip, identity on \([-R,R]\),
with \(|\tau_R(q)|\le\min\{|q|,2R\}\), \(|\tau_R'|\le1\).
For example integrate a smooth even cutoff equal to one on
\([-R,R]\), between zero and one, and zero outside \([-2R,2R]\).
Set \(\epsilon=e/a\) and
\[
 D_{\ell,R}(Y,q)=q+\epsilon\psi'(K_\ell Y)\tau_R(q).
\]
The normalized controlled equations, for \(\|c(s)\|_1\le3\), are
\[
 \begin{split}
 C'&=\sum_i c_iX_i^L,&
 w'&=\sum_i c_i d_i^1u_i,&
 A_\ell'&=\sum_i c_i d_i^\ell\otimes X_i^{\ell-1},\\
 q_i^L&=C,&q_i^\ell&=A_{\ell+1}^*d_i^{\ell+1},&
 d_i^\ell&=D_{\ell,R}(Y_i^\ell,q_i^\ell).
 \end{split}                                                \tag{G.6}
\]
These use the raw metric. The cap acts only on the nonlinear
part of a backward gate. Its derivatives are bounded at fixed
\(R,L,a\), so Part F gives local controlled solutions.

Put \(S=T_0a^{-L}\) and stop at hidden raw displacement
\(\mathfrak D=1\). Then action norms are at most 11 and the
three first projection norms at most 2 (the looser bound 3
also suffices). Induction using
\(|\chi_\ell(Y)-Y|\le2/K_\ell\), \(|\chi_\ell'|\le2\), and
\(|D_{\ell,R}(Y,q)|\le2|q|\), gives
\[
 \|X_i^\ell\|_2\le32^\ell,\quad
 \|C(s)\|_2\le3F_*s,\quad
 \|q_i^\ell(s)\|_2\le32^{L-\ell}\|C(s)\|_2.
                                                               \tag{G.7}
\]
For the first step \(\|X_i^1\|\le3+2\le32\); each later
step is at most \(11\cdot32^{\ell-1}+2\le32^\ell\).
Backward action and gate growth is at most \(22\le32\).
Every hidden block speed is at most \(F_*\|C\|\): at a matrix
block its coefficient is at most
\(6\cdot32^{L-\ell}32^{\ell-1}=(3/16)F_*\), and the bottom
satisfies the same bound. There are \(L\) hidden blocks, so
\[
             \mathfrak D(s)\le3\sqrt L F_*^2s^2.           \tag{G.8}
\]
The factor 3 is deliberately larger than the integrated factor
\(3/2\). Positive Euler meshes obey the same estimate because
\(\sum_jh_js_j\le s_k^2/2\). Even the first proposed overshooting
node is bounded using only earlier stopped states, so the strict
bound \(\mathfrak D(S)<1/4\) proved below rules out overshooting.
This establishes (G.7)--(G.8) on the entire controlled interval,
independently of source estimates.

Here are the forward perturbation estimates relative to the
same initialized actions and roots. Write
\(\Delta Y_\ell=Y_\ell-Y_\ell(0)\) and similarly for \(X\).
The bottom norm is at most \(\mathfrak D\). At later layers
use
\[
 \Delta Y_\ell=(A_\ell-A_{\ell,0})X_{\ell-1}
                               +A_{\ell,0}\Delta X_{\ell-1}.
 \]
Thus
\(\|\Delta Y_\ell\|\le32^{\ell-1}\mathfrak D+
20\|\Delta Y_{\ell-1}\|\). Summing this geometric recurrence
gives
\[
 \|\Delta Y_\ell\|\le3\cdot32^{\ell-1}\mathfrak D,\qquad
 \|\Delta X_\ell\|\le32^\ell\mathfrak D.                  \tag{G.9}
\]
Indeed the first coefficient is at most
\(\sum_{j\ge0}(20/32)^j=8/3<3\), and \(6<32\).
The bottom also satisfies both inequalities.
In raw preactivation coordinates this implies, for all
samples and \(\ell\le L\),
\[
 \|z_i^\ell(s)-z_i^\ell(0)\|_2
 \le a^{L-1}F_*\mathfrak D(S)
 \le d_L:=\frac{3\sqrt L T_0^2}{a}
                         \left(\frac{32768}{a}\right)^L.
                                                               \tag{G.10}
\]
The harmless factor \(3\cdot32^{\ell-1}\) in (G.9) is at
most \(32^L\); this explains the first inequality.

The top Gram perturbation has every entry bounded by
\(2F_*^2\mathfrak D\). Its operator norm is bounded by the
maximum absolute row sum, hence
\[
 \|Q_L(s)-Q_L(0)\|_{\rm op}
 \le6F_*^2\mathfrak D(S)
 \le18\sqrt L\left(\frac{2^{20}}{a^2}\right)^LT_0^2.
                                                               \tag{G.11}
\]
Let \(J_h:\mathcal P_h\to\mathbb R^3\) be the true normalized
hidden predictor differential and \(U_{h,R}:\mathbb R^3\to
\mathcal P_h\) the normalized capped hidden direction map.
Their individual sample/block factors are bounded by
\(F_*\|C\|\) using the same backward induction, also for the
true gate. Taking the finite sum of squared factor norms gives
\[
 \|J_h\|,\|U_{h,R}\|\le\sqrt{3L}F_*\|C\|,\qquad
 \|J_hU_{h,R}\|\le27L F_*^4 S^2.                         \tag{G.12}
\]
There is no assertion that \(J_hU_{h,R}\) is symmetric.

All required strict inequalities follow from the single
depth-independent condition \(a\ge10^{12}(1+T_0)\).
For completeness, if \(0\le q\le1/4\) then
\(Lq^L\le2q^2\) for \(L\ge2\): the consecutive ratio is
\((L+1)q/L\le3/8<1\). Also \(\sqrt L\le L\).
Use \(q=2^{20}/a^2\). The largest of (G.11) and (G.12)
is at most
\[
                  54\,2^{40}T_0^2/a^4<\lambda/4.         \tag{G.13}
\]
Indeed \(a\ge10^{12}T_0\) and \(T_0=12/\lambda\) make
this at most \( (54\,2^{40}/(144\cdot10^{48}))\lambda^2
<4.13\cdot10^{-37}\lambda^2<\lambda/4\).
Use \(q=1024/a^2\) in (G.8) to obtain
\(\mathfrak D(S)\le6\cdot2^{20}T_0^2/a^4<1/4\).
Consequently
\[
 Q_L(s)\succeq3\lambda I_3/4,\qquad
                \|J_hU_{h,R}\|<\lambda/4.                \tag{G.14}
\]
The same controlled bounds hold for every cap.

## G.3. Capped physical paths and their finite total control time

The physical capped equations are
\[
             \dot\theta=-a^L\sum_i r_i\,G_{i,R},
                                                               \tag{G.15}
\]
where \(G_{i,R}\) has the normalized blocks in (G.6) with
unit control \(c_i=1\). Its readout block is \(X_i^L\).
Define the accumulated control time
\[
                    v(t)=a^L\int_0^t\|r(s)\|_1\,ds.
                                                               \tag{G.16}
\]
On portions where \(r\ne0\), reparametrization by \(v\)
turns (G.15) into (G.6) with \(c=-r/\|r\|_1\), of norm one.
If \(r=0\), the whole capped field is zero; fixed-cap uniqueness
makes its continuation stationary. Equivalently the integral
controlled estimates apply directly with the measure
\(dv=a^L\|r(t)\|_1dt\), so no inverse at zero is required.

While \(v\le S\), the scalar chain rule in Part F gives the
exact residual equation
\[
                  \dot r=-a^{2L}(Q_L+J_hU_{h,R})r.
                                                               \tag{G.17}
\]
Its readout term is the true positive Gram even under a cap.
Using the absolute operator bound for its possibly nonsymmetric
hidden term, (G.14) implies
\[
 \frac d{dt}\|r\|_2^2\le-\lambda a^{2L}\|r\|_2^2,\qquad
 \|r(t)\|_2\le\sqrt3 e^{-\lambda a^{2L}t/2}.             \tag{G.18}
\]
Here \(r(0)=-y\), since the population readout is zero.
Therefore
\[
 v(t)\le a^L\sqrt3\int_0^\infty
                  \sqrt3e^{-\lambda a^{2L}s/2}\,ds
        =\frac6{\lambda a^L}=\frac S2.                    \tag{G.19}
\]
This rules out a first exit at \(v=S\). A finite physical
endpoint has bounded raw speed by (G.7) and (G.15);
its state is strongly Cauchy there, and fixed-cap local
existence continues it. Thus all capped population paths
are global, with (G.7)--(G.19) independent of cap and horizon.

To apply Part S's Euler source estimates to these paths without
an implicit limit assumption, fix a cap and bounded deterministic
control on \([0,S]\). For a step-function control, fixed-cap
Euler convergence follows separately on its finitely many
constant intervals from Part F. For a general measurable bounded
control, choose bounded step controls converging in \(L^1\);
they exist by approximating each integrable coordinate by
simple interval step functions, and projecting onto the closed
\(\ell^1\) ball if needed. The integral difference of the fields
is bounded by \(C\|c-\bar c\|_{L^1}\), in addition to a
fixed-cap Lipschitz state term. Gronwall gives uniform strong
convergence of controlled paths. For each fixed time, an
almost-sure subsequence and Fatou pass Part S's moment bounds.
This argument does not sample an arbitrary measurable control
at Euler nodes. In particular it applies to the deterministic
control extracted from any capped population physical path.
The uniform result of Part S is
\[
 \sup_{R,t\ge0,\ell,i}\|q_{R,i}^\ell(t)\|_p
                            \le M_*\sqrt p,\qquad p\ge2, \tag{G.20}
\]
where \(M_*<\infty\) may depend on fixed \(L,a,\delta\) but
not on cap or physical time. The total interval is always
the same \([0,S]\). These are the sole nonclassical inputs
to cap removal, and Part S proves them explicitly.

Part V now applies: its one-cap-factor comparison uses
(G.20) only on the capped reference, constructs a strong
uncut limit, and proves uniqueness, restart and all actual
finite GF/GD and observation limits. Its fixed-cap
approximations depend only on the already established capped
paths and controlled moments, so the order is not circular.
The bounds (G.14), (G.18), (G.19) pass by strong convergence
to the uncut path and prove (M.15).

## G.4. Persistent nonaffinity for one activation at every depth

For a square-integrable real variable \(X\), define
\[
 \mathcal R_\psi(X)=\inf_{b,c\in\mathbb R}
                             E[\psi(X)-b-cX]^2.
\]
The following stability estimate avoids any variance lower
bound:
\[
 \left|\sqrt{\mathcal R_\psi(X)}
           -\sqrt{\mathcal R_\psi(\widetilde X)}\right|
                            \le2\|X-\widetilde X\|_2.     \tag{G.21}
\]
To prove it, if \(\operatorname{Var}X>0\), the optimal slope is
\(c_X=\operatorname{Cov}(X,\psi(X))/\operatorname{Var}X\).
For an independent copy \(X'\), the covariance numerator is
\(\tfrac12 E[(X-X')(\psi(X)-\psi(X'))]\), while the denominator
is \(\tfrac12E[(X-X')^2]\). Since \(\psi\) is 1-Lipschitz,
\(|c_X|\le1\). If \(X\) is constant choose \(c_X=0\) and
the matching intercept. Test the optimal affine fit for \(X\)
as a competitor for \(\widetilde X\), on the given coupling:
the difference of its residuals is at most
 \(2|X-\widetilde X|\). The triangle inequality gives one
direction of (G.21); interchanging the variables gives the
other. The best fit exists because the span of \(1,X\) is
finite dimensional and closed; the displayed covariance
calculation also constructs it.

There exists an \(r_\psi\) in (M.3). Otherwise \(\psi\) is
affine on every \([-r,r]\) for integer \(r\), since this
finite-dimensional affine subspace is closed in its interval
\(L^2\). Continuity makes each such equality pointwise.
Overlapping intervals force the same two affine coefficients,
so \(\psi\) is affine on \(\mathbb R\), and boundedness would
make it constant, a contradiction. The interval residual is
explicitly
\[
 J_\psi=\int_{-r}^{r}\psi(x)^2dx
       -\frac{(\int_{-r}^{r}\psi(x)dx)^2}{2r}
       -\frac{3(\int_{-r}^{r}x\psi(x)dx)^2}{2r^3}.
                                                               \tag{G.22}
\]
For \(\sigma\ge1\), its Gaussian density on \([-r,r]\) is
at least \(e^{-r^2/2}/(\sigma\sqrt{2\pi})\). Restricting
the regression integral to this interval proves
\[
                      \mathcal R_\psi(\sigma G)
                                      \ge c_\psi/\sigma.
                                                               \tag{G.23}
\]
In particular \(c_\psi\le\mathcal R_\psi(G)\le1\).
By (G.3), at every layer of a depth \(L\) network,
\[
         \mathcal R_\psi(z_i^\ell(0))
                       \ge\eta_L:=c_\psi/(4a^{L-1}).     \tag{G.24}
\]

The raw displacement in (G.10) is smaller than
\(\sqrt{\eta_L}/4\) simultaneously for every \(L\ge2\).
Here is the explicit check. The ratio is at most
\[
 \frac{24\sqrt L T_0^2}{\sqrt{c_\psi}a^{3/2}}
                    \left(\frac{32768}{\sqrt a}\right)^L.
\]
The first bound in (M.4) ensures
\(q=32768/\sqrt a\le1/2\). For \(L\ge2\),
\(\sqrt L q^L\le2q^2\): the ratio of consecutive terms is
at most \(\sqrt{3/2}/2<1\) and the initial coefficient is
\(\sqrt2\le2\). Thus the displayed ratio is at most
\[
 \frac{3\cdot2^{34}T_0^2}{\sqrt{c_\psi}a^{5/2}}
                         \le\frac34<1                  \tag{G.25}
\]
by the second bound in (M.4). Apply (G.21) to the common-space
coupling of a trained preactivation and its own initialization.
Equations (G.10), (G.24)--(G.25) give
\(\mathcal R_\psi(z_i^\ell(t))\ge\eta_L/4\).
Adding the affine part of \(\phi\) to a regression target has
no effect on its residual, and multiplying its nonaffine part
by \(e\) multiplies the residual by \(e^2\). Hence
\[
 \mathcal R_\phi(z_i^\ell(t))
   =e^2\mathcal R_\psi(z_i^\ell(t))
                       \ge e^2c_\psi/(16a^{L-1}),
\]
as claimed. This holds first for every capped path, then for
the uncut path by (G.21) and strong cap convergence.

Parts F, S, G and V prove statements 1, 2 and the regression
portion of statement 3 of Theorem M.1. Part N proves the
remaining motion and kernel assertions with only \(a>e>0\),
which the selected constants satisfy.

# Part V. Population and finite-algorithm bridge at each fixed depth

Fix a finite hidden depth L>=2 and the activation parameters already selected by the theorem. All constants in this chapter may depend on this fixed L, a, e, dataset, and physical observation horizon T. Such dependence does not enter the selection of a,e. Write

    K_l=a^(l-1), eps=e/a,
    chi_l(y)=y+[1+eps psi(K_l y)]/K_l,
    g_l=chi_l',
    D_(l,R)(y,q)=q+eps psi'(K_l y)tau_R(q).

For each fixed l the functions g_l and g_l' are bounded and continuous. The clipped coordinate map has bounded continuous first derivatives, with

    |g_l|<=2, |g_l'|<=eps K_l,
    |D_(l,R)|<=2|q|, |D_q|<=2, |D_y|<=2eps K_l R.       (V.1)

No sign restriction is imposed on psi' or psi''.

We use the normalized hidden fields Y_l=z_l/a^(l-1), X_l=h_l/a^l. The raw matrices and original readout C are unchanged. At the bottom, w=sqrt(d)W^1 and u_i=x_i/sqrt(d) are an isometric notational representation of the original bottom metric: (d/n)||Delta W^1||_F^2=||Delta w||_n^2. Put

    Y_(1,i)=<w,u_i>,
    Y_(l,i)=A_l X_(l-1,i), X_(l,i)=chi_l(Y_(l,i)),
    f_i=a^L<C,X_(L,i)>, p_i=a^L(y_i-f_i).

The physical capped raw vector field is exactly

    V_(R,C)=sum_i p_i X_(L,i),
    V_(R,A_l)=sum_i p_i delta_(l,i) tensor X_(l-1,i),
    V_(R,w)=sum_i p_i delta_(1,i)u_i,                      (V.2)

where

    q_(R,L)=C,
    delta_(R,l)=D_(l,R)(Y_l,q_(R,l)),
    q_(R,l)=A_(l+1)^*delta_(R,l+1), l<L.

Thus physical time is used throughout this chapter. The factor a^L is in p, not in a replacement metric or training step. Reserve b_l=g_l(Y_l)t_l, t_L=C, t_l=A_(l+1)^*b_(l+1), for the TRUE normalized backward fields, even when they are observed at a capped state. The original raw backward fields equal a^(L-l+1)b_l.

We use the Hilbert raw norm on the first vector block, all Hilbert--Schmidt increments, and C. On finitely many blocks it is equivalent to their sum norm, which may be used in estimates by altering constants. Every comparison below takes place either at the same width with identical initialization or on the common population spaces. No cross-width identification of operators is used.

## V.1. Exact inputs and dependency order

The following results have been proved earlier and are the only inputs to this chapter.

(F) Every fixed finite Gaussian program with independent initialized adjacent matrices, both orientations, independent root tuples, C1 coordinate maps with bounded continuous derivatives, and causal scalar contractions has full-sequence within-layer empirical W2 convergence, including all second moments. An initialized forward query on h has the scalar representation

    xi_h + sum_v v E[partial_(zeta_v) h],                 (V.3)

where v ranges over preceding reverse inputs to that matrix. Its reverse rule includes the current forward inputs. Gaussian source covariances are the full actual input Grams; distinct oriented groups are independent. Named slots are differentiated separately at singular covariance, with all coefficients, contractions, controls, and covariances frozen. The construction is continuous under bounded-derivative finite query perturbations, by positive-semidefinite covariance-square-root coupling. The common initialized action norms are <=10 and their reverses are their genuine adjoints. The finite norm event has probability tending to one. These conclusions apply to any finite number of adjacent matrices because their conditioning proof counts instructions rather than layers.

(G) The capped population physical paths are global. First projections, current action norms, C, and physical raw directions have bounds independent of cap on compact horizons. The paths stay in a common primal ball with strict continuation slack.

(S) The direct controlled source estimate and residual-clock bound give, for some M_* and every p>=2,

    sup_(R,t,l,i) ||q_(R,l,i)(t)||_p <= M_* sqrt(p).       (V.4)

Here L,a,e are fixed. This includes q_L=C, uses the actual capped incoming fields, and has already been transferred from controlled Euler programs to physical capped paths. It does not replace the actual residuals by prescribed controls in training.

The chain and adjunction rules from the foundations apply to bounded g_l and to bounded-action curves with Hilbert--Schmidt derivatives.

The proof order below is deliberate. Raw cap removal uses only (G),(S). Fixed-cap Euler bounds and fixed-mesh primary Gaussian laws supply finite primal events before Gaussian probe estimates use them. Probe estimates supply pointwise source rows; these justify appended velocity queries. Only then are uniform-time empirical velocity laws proved. True backward observations require a separate finite truncation argument. Finally same-width cap comparison transfers everything to actual uncut algorithms.

## V.2. One-cap-factor comparison and population cap removal

On a fixed primal ball, forward propagation gives

    sum_(l,i)(||Y_l-Ybar_l||_2+||X_l-Xbar_l||_2)
       +sum_i|p_i-pbar_i| <= C||Theta-Thetabar||raw.       (V.5)

The bottom projection is bounded. Each upper step uses

    A_l X_(l-1)-Abar_l Xbar_(l-1)
       =(A_l-Abar_l)X_(l-1)+Abar_l(X_(l-1)-Xbar_(l-1)),

||A_l-Abar_l||op<=||A_l-Abar_l||HS, and the Lipschitz constant of chi_l. The residual estimate follows by expanding the C,X_L inner product. For rank-one blocks,

    ||u tensor v-ubar tensor vbar||HS
       <=||u-ubar||_2||v||_2+||ubar||_2||v-vbar||_2.       (V.6)

For R'>=R, including infinity,

    |D_(l,R')(y,q)-D_(l,R)(ybar,qbar)|
       <=2|q-qbar|+2eps K_l R|y-ybar|
                       +2eps |qbar|1_(|qbar|>R).         (V.7)

To prove it, first change q inside D_(l,R'), costing 2|q-qbar|. Split the remaining perturbation into

    eps[psi'(K_l y)-psi'(K_l ybar)]tau_R(qbar)
      +eps psi'(K_l y)[tau_(R')(qbar)-tau_R(qbar)].

The first term uses |psi''|<=1 and |tau_R|<=2R; the second vanishes for |qbar|<=R and otherwise has absolute value <=2eps|qbar|.

Here is the full depth recursion. Write alpha=||Theta-Thetabar||raw and E_l=||delta_(R',l)-delta_(R,l)(Thetabar)||_2, maximizing over samples. At the top, (V.7) gives E_L<=C(1+R)alpha+C Tail_L. At the next level,

    ||q_(R',l)-q_(R,l)(Thetabar)||_2<=C alpha+C E_(l+1),
    E_l<=2C E_(l+1)+C(1+R)alpha+C Tail_l.

Solving this finite downward recursion yields

    sum_l E_l <= C(1+R)alpha+C sum_l Tail_l.

Each new R multiplies a forward difference in (V.5), never E_(l+1). Using (V.6) and the actual residual difference therefore gives

    ||V_(R')(Theta)-V_R(Thetabar)||raw
       <=C(1+R)||Theta-Thetabar||raw
                     +C sum_(l,i)||qbar_(R,l,i)1_(|qbar_(R,l,i)|>R)||_2.
                                                               (V.8)

The same bound controls all backward discrepancies. Its tail terms belong only to the reference.

From (V.4), Markov's inequality with moment exponent p=(u/(3M_*))^2, for u large, gives

    sup_(R,t,l,i)||q_(R,l,i)1_(|q_(R,l,i)|>u)||_2
                    <=C exp(-c u^2).                     (V.9)

Indeed E[q^2 1_(|q|>u)]<=u^2(M_*sqrt(p)/u)^p, and the polynomial prefactor can be absorbed into a smaller exponential rate. Integrating (V.8) and applying its iterated integral inequality yields

    sup_(t<=T)||Theta_(R')(t)-Theta_R(t)||raw
      +sup_(t<=T)||V_(R')(Theta_(R')(t))-V_R(Theta_R(t))||raw
                        <=C_T exp(C_T R-cR^2).           (V.10)

The second term follows by substitution in (V.8), absorbing factors 1+R. Paths and raw derivatives are uniformly Cauchy. Their limits satisfy the integral equation Theta(t)=Theta(0)+integral_0^t V(s)ds, with continuous V, and (V.8) against the limit state identifies V=V_infty(Theta). Hence the limit is a strong C1 raw solution. Integer caps and horizons give a single consistent global construction.

Any bounded-primal strong uncut competitor is compared with the same capped reference by (V.8). Its primal bound changes C_T, but no competitor tail is used. The resulting error still vanishes as R tends to infinity. At a reached time t_0 the initial discrepancy from the capped reference is already bounded by (V.10); another exp(C_TR) factor leaves a vanishing error. This proves uniqueness and unique continuation from each reached state, without asserting arbitrary-state local Lipschitzness of the uncut field.

## V.3. Raw Euler bounds and finite primal events, before source estimates

For fixed R and a larger primal ball, (V.1),(V.5),(V.6) make V_R locally Lipschitz with width-independent constants M_0,L_0. The autonomous Euler local defect is <=L_0M_0 h_j^2/2. The error recursion gives

    max_k||Theta_R(t_k)-Theta_R^pi(t_k)||raw
       <=(L_0 M_0 T/2)exp(L_0 T)|pi|.                    (V.11)

Raw interpolation adds <=2M_0|pi|. Stop at the boundary of the larger ball, choose |pi| sufficiently small, and the strict slack excludes first exit. This proves bounded population Euler arrays without source or velocity estimates.

At a fixed auxiliary mesh, (F) gives every primary finite node law and contraction. Exact rank unrolling gives

    max_k||A_(l,k,n)||op
       <=||A_(l,0,n)||op
          +sum_(j,b)h_j|p_(j,b,n)|
                          ||delta_(l,j,b,n)||_n ||X_(l-1,j,b,n)||_n.
                                                               (V.12)

The sum is finite. Every summand converges to its population counterpart, whose total is bounded by the population primal and direction bounds, uniformly over the sufficiently fine meshes in (V.11). First-layer and readout norms converge too; include the full first-layer Gaussian root vector in the fixed program when its norm is needed. Thus, at each fixed sufficiently fine mesh, a deterministic enlarged finite primal ball with slack contains all finite coarse nodes and interpolants with probability tending to one. This argument uses no velocity or source-row estimate.

The actual finite initialization has ||C_(0,n)||_n=O_P(n^-1), since E||C_(0,n)||_n^2=n^-2. For fixed cap and transcript, compare it to a same-matrix auxiliary Euler program with zero readout root. Stopped finite-step Lipschitz stability propagates this vanishing norm, and the preceding slack closes the comparison. Thus the actual fixed-program limit has C_0=0. Every actual finite GF/GD and every same-width reference comparison below retains the original random C_(0,n); no algorithm is reset.

## V.4. Fixed-cap response rows by Gaussian probes

Fix R,T and a sufficiently fine physical Euler mesh. Freeze p, all contractions, covariances, and response coefficients in formal source derivatives. The exact primary source equations are

    Y_(1,k,i)=Y_(1,0,i)+sum_(j<k,b)h_j p_(j,b)Gamma_(ib)delta_(1,j,b),
    C_k=sum_(j<k,b)h_j p_(j,b)X_(L,j,b),

    Y_(l,k,i)=xi_(l,k,i)
                      +sum_(j<k,b)Acal_(l,ki,jb)delta_(l,j,b),
    q_(l-1,k,i)=zeta_(l-1,k,i)
                      +sum_(j<=k,b)Bcal_(l,ki,jb)X_(l-1,j,b),
                                                               (V.13)

for 2<=l<=L, where

    Acal_(l,ki,jb)
       =E partial_(zeta_(l-1,j,b))X_(l-1,k,i)
                         +h_j p_(j,b)E[X_(l-1,k,i)X_(l-1,j,b)],
    Bcal_(l,ki,jb)
       =E partial_(xi_(l,j,b))delta_(l,k,i)
             +1_(j<k)h_j p_(j,b)E[delta_(l,k,i)delta_(l,j,b)].
                                                               (V.14)

They retain every current transpose return. Source variances are bounded by the primal norms of their actual inputs.

Choose one oriented answer family and a fresh independent standard Gaussian vector g in its answer layer. Add epsilon alpha_(j,b)g, |alpha_(j,b)|<=1, at selected answer slots and recompute all subsequent residuals and raw updates. On the enlarged ball the raw discrepancy satisfies

    E_(k+1)<=(1+Ch_k)E_k+Ch_k|epsilon| ||g||_n.           (V.15)

Thus arbitrary bounded forcing at every time gives E_k<=C|epsilon|||g||_n. A single forcing at time j gives <=Ch_j|epsilon|||g||_n at all later states. Current query errors have the direct O(|epsilon|) term; strictly later queries have the O(h_j|epsilon|) term. These estimates follow from (V.1),(V.5),(V.6) and include the recomputed residuals. For small fixed epsilon, first-exit and the finite primal event of Section V.3 keep this perturbed fixed program in the enlarged ball with probability tending to one.

Let V_k be a selected scalar primary output. At fixed mesh and epsilon, (F) passes <g,V_(k,n)^epsilon>_n to E[G V_k^epsilon]. The scalar G is independent of all oriented source groups and original roots. With deterministic coefficients frozen, its only explicit occurrences are the answer additions. Gaussian integration by parts gives

    E[G V_k^epsilon]
        =epsilon sum_(j,b)alpha_(j,b)
                              E partial_(eta_(j,b))V_k^epsilon.    (V.16)

At this fixed transcript the expression has bounded first derivatives and linear growth, so the Gaussian boundary term vanishes and differentiation is integrable. Its expected named derivatives converge as epsilon tends to zero: chronologically couple all finite covariance matrices by their positive square roots; earlier inputs and contractions converge in L2; continuous first derivatives with finite deterministic bounds on a compact coefficient neighborhood pass their expectations by dominated convergence. This uses no covariance derivative or inverse.

The unperturbed <g,V_(k,n)^0>_n tends to zero: conditionally its variance is ||V_(k,n)^0||_n^2/n. Cauchy--Schwarz and (V.15), followed by width then epsilon limits in (V.16), give

    |sum_(j,b)alpha_(j,b)E partial_(eta_(j,b))V_k|<=C.

Choose the deterministic signs of the expected derivatives. A single strictly past insertion gives Ch_j instead. Together with the learned contractions in (V.14), this proves

    |Acal_(l,ki,jb)|<=Ch_j (j<k),
    |Bcal_(l,ki,jb)|<=Ch_j (j<k),
    |Bcal_(l,ki,kb)|<=C.                                  (V.17)

This bounds absolute EXPECTED derivative rows; it has not replaced |E partial V| by E|partial V|.

The current reverse rows have an explicit descending recursion. Put N_(l,k,i)=D_y(Y_(l,k,i),q_(l,k,i)), V_(l,k,i)=D_q(Y_(l,k,i),q_(l,k,i)), and set Bcal_(L+1,ki,kb)=0 for the readout integrator. Then

    Bcal_(l,ki,kb)
      =1_(i=b)E N_(l,k,i)
       +Bcal_(l+1,ki,kb) E[V_(l,k,i)g_l(Y_(l,k,b))],       (V.18)

for l=L,L-1,...,2. Indeed the current Y_l has derivative identity in its own current xi_l, while all strictly past corrections have zero current derivative. Differentiate q_l's current return and then its gate. At the top C_k uses strictly past X_L, so its current xi derivative is zero. Formula (V.18) starts there and keeps the exact signed current returns at every lower level.

## V.5. Pointwise source rows and primary moments

Within layer l let R_l(H) be the sum of absolute derivatives in all primary named sources in that layer through the final mesh time, including its initial root coordinates if desired. Those families are xi_l for l>=2 and zeta_l for l<L; future derivatives vanish. Freeze all coefficients. Using (V.13),(V.17), coordinate differentiation gives, with maxima over the three samples understood,

    Z_(1,k)<=C+C sum_(j<k)h_j D_(1,j),
    Z_(l,k)<=1+C sum_(j<k)h_j D_(l,j), l>=2,
    H_(l,k)<=2 Z_(l,k),
    Cpartial_k<=C sum_(j<k)h_j H_(L,j),
    Q_(l,k)<=1+C H_(l,k)+C sum_(j<k)h_j H_(l,j), l<L,
    D_(l,k)<=C_R Z_(l,k)+2Q_(l,k), l<L,
    D_(L,k)<=C_R Z_(L,k)+2Cpartial_k.                      (V.19)

Here Z,H,Q,D denote the corresponding pointwise derivative-row seminorms, not primal values. Every same-time reverse term is a forward field already defined at that time; there is no algebraic same-time loop. Let U_k be the maximum of Z_(l,k) and Cpartial_k. The last four lines bound the other fields by C(1+U_k+sum_(j<k)h_j U_j). Substitute into the first lines and use

    sum_(j<k)h_j sum_(r<j)h_r U_r
       <=T sum_(r<k)h_r U_r.

It follows that U_k<=C+C sum_(j<k)h_j U_j, hence U_k<=C exp(CT). Returning to (V.19) proves a deterministic bound

    R_l(H_(k,i))<=C_(R,T)                                  (V.20)

for every primary scalar field, uniformly over all sufficiently fine meshes and times.

Replace these derivative seminorms by Lp norms in the same inequalities. Direct Gaussian sources and roots have norms <=C sqrt(p); chi_l has linear growth and D_(l,R) is bounded by 2|q|. Minkowski and the same discrete inequality give

    sup_(pi,k,l,i)||H_(k,i)||_p<=C_(R,T)sqrt(p), p>=2,       (V.21)

for all primary fields and C. No temporal independence or Lp operator estimate for an initialized matrix has been used.

## V.6. Ascending velocity queries, with complete induction and nested truncation

At a physical Euler node let P_(l,i),U_(l,i) denote the instantaneous normalized preactivation and feature velocities in direction V_R(Theta_k). Exactly,

    P_(1,k,i)=sum_b p_(k,b)Gamma_(ib)delta_(1,k,b),
    U_(l,k,i)=g_l(Y_(l,k,i))P_(l,k,i),
    P_(l,k,i)=sum_b p_(k,b)delta_(l,k,b)
                                E[X_(l-1,k,b)X_(l-1,k,i)] + J_(l,k,i),
    J_(l,k,i)=A_(l,k)U_(l-1,k,i),  2<=l<=L.                (V.22)

The feature multiplier is the TRUE derivative g_l, even for a capped update direction. Append all A_(2,0) velocity queries after the complete primary transcript, then all A_(3,0) queries, and continue up to A_(L,0). No appended query feeds training. At level l, the only preceding opposite-orientation inputs for A_l are the primary delta_l fields; earlier appended levels use different matrices, and other level-l velocity queries use the same forward orientation. The source formula therefore is

    J_(l,k,i)=gamma_(l,k,i)
                       +sum_(j<=k,b)Ecal_(l,ki,jb)delta_(l,j,b),
    Ecal_(l,ki,jb)
       =E partial_(zeta_(l-1,j,b))U_(l-1,k,i)
          +1_(j<k)h_j p_(j,b)E[X_(l-1,j,b)U_(l-1,k,i)].    (V.23)

The new forward source gamma_l has covariance with every source of the same orientation equal to the inner product of their actual query inputs, and variance ||U_(l-1,k,i)||_2^2. It is a distinct named argument; its formal derivative in primary zeta_l is zero even if same-family covariance is singular. Sources later than time k have zero derivatives in the time-k input, despite the appended ordering.

Here is the induction invariant before constructing layer l's new action: all lower velocity observations have their joint finite empirical W2 laws, their exact formulas (V.23), Lp bounds <=C sqrt(p), and pointwise bounds

    R_(zeta_(m)) P_(m,k,i)<=C,
    R_(zeta_(m)) U_(m,k,i)<=C(1+|P_(m,k,i)|), m<l,        (V.24)

where only the primary transpose sources of the indicated layer are differentiated. For the bottom, (V.20)--(V.22) give the first inequality, and the exact scalar derivative

    partial_eta[g_m(Y_m)P_m]
        =g_m'(Y_m)P_m partial_eta Y_m
                           +g_m(Y_m)partial_eta P_m       (V.25)

gives the second. Primary moments (V.21) give the base Lp bound.

Assume the invariant through l-1. Its second inequality has an integrable envelope, so the total expected response row in (V.23) is bounded by C. Cauchy--Schwarz bounds the learned row by C sum_j h_j<=CT. The actual L2 norm of U_(l-1), already known before the new action, bounds gamma_l's variance. The formula (V.23), Gaussian moments, (V.21), and Minkowski then give

    sum_(j<=k,b)|Ecal_(l,ki,jb)|<=C,
    ||J_(l,k,i)||_p+||P_(l,k,i)||_p+||U_(l,k,i)||_p
                              <=C sqrt(p).               (V.26)

Differentiate (V.23) only in the primary zeta_l coordinates: all coefficients are frozen and gamma_l has derivative zero. By (V.20) the derivative row of the sum is bounded by the coefficient-row bound times C. The explicit first term in P_l in (V.22) is a deterministic linear combination of primary delta_l, so its row is also bounded by C. This proves the first part of (V.24) for m=l. Applying (V.25) proves its second part. This establishes precisely the invariant needed for the next matrix. Constants may increase with the fixed number of layers; the argument does not assume a future-layer moment estimate.

The formulas just used must be justified before unbounded products enter (F). Replace each multiplier product by g_m(Y_m)tau_M(P_m). It is a bounded-derivative instruction, and its exact named derivative is

    g_m'(Y_m)tau_M(P_m)partial_eta Y_m
             +g_m(Y_m)tau_M'(P_m)partial_eta P_m.          (V.27)

At the first action its derivative row is bounded independently of M by C(1+|P_1|), integrable by the already-proved primary bound. Thus (F) applies for fixed M, and the row and moment estimates in (V.26) hold independently of this observation cap. Dominated convergence as M tends to infinity identifies every expected coefficient in (V.23). Input L2 convergence and bounded initialized actions identify the actual untruncated query; its covariance converges by second-moment convergence and is coupled by covariance square roots.

For clarity, empirical removal uses only second moments. If (Z_n,P_n) converge under an L2 coupling to (Z,P), then

    ||g(Z_n)P_n-g(Z)P||_2
       <=||g||infty||P_n-P||_2+||[g(Z_n)-g(Z)]P||_2 ->0.  (V.28)

For the second term split at |P|<=M: that part is <=Lip(g)M||Z_n-Z||_2, and the remaining part is <=2||g||infty||P1_(|P|>M)||_2. Take n first, then M. The positive-part tail functional T_M(P)=||(|P|-M)_+||_2 is 1-Lipschitz under L2 coupling, and |P|1_(|P|>2M)<=2(|P|-M)_+. Consequently fixed-program W2 convergence makes the empirical input clipping error vanish in the width-then-cap order. Bounded action norms transfer it to the output error.

At a general new level l, retain all previous inner observation caps and one outer cap M in g_(l-1)(Y)P_(l-1). At fixed caps, (F) applies to the entire finite appended program. First remove the previously constructed inner caps while M stays fixed. The established lower-level formulas have convergent deterministic coefficients and covariance-square-root couplings, so the rows of P_(l-1) in the relevant primary zeta_(l-1) coordinates converge in probability and remain bounded, by their expression as bounded rows of primary delta. Formula (V.27) at fixed M therefore passes expected derivatives by dominated convergence. Formula (V.28) and bounded actions pass the corresponding L2 inputs and outputs. Now remove M. The envelope C(1+|P_(l-1)|) from the already established invariant is integrable and independent of M, so dominated convergence gives the untruncated expected response coefficients. The empirical error is removed by the positive-part tail argument. This is the induction step giving both the derivative-valid formula and its joint empirical law. It does not invoke (F) directly for the unbounded product or assume derivative convergence from W2 alone.

The induction reaches L and proves fixed-cap, mesh-uniform marginal C sqrt(p) bounds for every P_l,U_l. All same-family time/sample/source covariances are retained in any finite concatenation of these observations.

## V.7. Deterministic velocity comparison and fixed-cap time limits

For states Theta,Thetabar on one primal ball and raw directions v,vbar in a bounded direction ball, put alpha=||Theta-Thetabar||raw, beta=||v-vbar||raw. Define P_1=v_w u_i, U_l=g_l(Y_l)P_l, and P_l=v_(A_l)X_(l-1)+A_l U_(l-1). Then, for M>=1,

    sum_(l,i)(||P_l-Pbar_l||_2+||U_l-Ubar_l||_2)
      <=C[beta+(1+M)alpha+sum_(l,i)T_M(Pbar_(l,i))].      (V.29)

To verify the exact depth recurrence, the bottom P-error is <=C beta. At every upper layer expand

    P_l-Pbar_l=(v_(A_l)-vbar_(A_l))X_(l-1)
       +vbar_(A_l)(X_(l-1)-Xbar_(l-1))
       +(A_l-Abar_l)Ubar_(l-1)+A_l(U_(l-1)-Ubar_(l-1)).

Its norm is <=C(alpha+beta+||U_(l-1)-Ubar_(l-1)||_2). Moreover

    ||U_l-Ubar_l||_2
       <=2||P_l-Pbar_l||_2+C M||Y_l-Ybar_l||_2
                                         +4T_M(Pbar_l).

The last line follows by clipping Pbar_l at M and using bounded g_l,g_l'. Solve these two finite recurrences upward, using (V.5). Each new M multiplies a forward discrepancy already bounded by C alpha, so there is one M. The constant depends only on the fixed activation and the primal/direction ball, and is independent of R,M.

If ||P||_4<=C, then T_M(P)<=C^2/M. Apply (V.29) with the Euler node as reference, (V.11), the fixed-cap raw Lipschitz bound, and Section V.6 moments. Choosing M=|pi|^(-1/2) gives uniform population hidden-velocity error <=C_(R,T)sqrt(|pi|) between the instantaneous Euler node velocities and the cap-flow velocities. The state error is O(|pi|). The foundations' strong chain rule gives the actual flow velocities used here: at each level the bounded multiplier g_l preserves L2 continuity, and differentiating A_l X_(l-1) gives exactly the stated P recurrence. This does not assume ambient L2-to-L2 Frechet differentiability of chi_l.

At each fixed time, strong L2 convergence has an almost-sure subsequence. Fatou passes all mesh moment bounds to the cap-flow fields and velocities, giving sup_(t<=T)||H_R(t)||_p<=C_(R,T)sqrt(p). Apply (V.29) at two cap-flow times: raw states and directions are Lipschitz at fixed cap, and the fourth-moment tail estimate gives an L2 velocity modulus C_(R,T)|t-s|^(1/2). Only marginal moments are claimed; no random time-maximum bound is used.

## V.8. Fixed-cap finite GF and raw GD

Let Theta_(R,n)^pi be the same-width, same-initialization coarse Euler reference. On the high-probability primal event of Section V.3, compare until exit the actual finite capped GF, or the actual fine raw Euler scheme with deterministic step eta_n=n^-2. The coarse interpolant has vector-field defect <=L_0M_0|pi|, fine Euler has defect <=L_0M_0 eta_n, and GF has zero defect. Gronwall gives

    sup_(t<=T)||Theta_(R,n)(t)-Theta_(R,n)^pi(t)||raw
                           <=C_(R,T)(|pi|+eta_n).         (V.30)

Here eta_n=0 denotes GF. Choosing the mesh below slack excludes first exit and continues finite capped GF through T. The actual fine-Euler direction is V_R evaluated at its preceding fine node; it is not replaced by the field at the interpolated state. Its direction error against the preceding coarse-node field is still <=C_(R,T)(|pi|+eta_n), by bounded within-step displacement and fixed-cap Lipschitzness.

Apply (V.29) at the same width using the coarse node as reference. At fixed pi,M, Section V.6 gives joint empirical W2 convergence of all coarse velocities. Their finitely many empirical positive-part tails converge and are bounded in the limit by C/M. Thus the width-limit upper bound in probability for the velocity discrepancy is

    C_(R,T)[(1+M)|pi|+M^-1].                              (V.31)

Choose M=|pi|^(-1/2) at that fixed mesh, take width first, and then refine pi. This gives a vanishing bound. No empirical fourth moment or growing-transcript Gaussian law was invoked.

For each layer, let mu_(R,n,l)(t) denote the empirical law of the same-layer tuple of all three samples of chosen primary fields and hidden velocities. The corresponding population law is mu_(R,l)(t). At each time couple actual and coarse arrays by neuron index. The triangle inequality is

    sup_t W2(mu_(R,n,l)(t),mu_(R,l)(t))
      <=sup_t||actual finite tuple-coarse finite node tuple||_n
        +max_k W2(coarse finite node law,coarse population node law)
        +sup_t||coarse population node tuple-population flow tuple||_2.
                                                               (V.32)

At fixed mesh the middle term vanishes by the finite appended program theorem. The outer terms vanish after mesh refinement by (V.11),(V.29)--(V.31). Therefore these same-layer laws converge uniformly in physical time in W2, in probability along the full width sequence. Concatenating coordinates at finitely many requested times gives their joint-time W2 laws with the same proof; all within-layer time/sample correlations are preserved. Predictions and loss are continuous functions of the convergent contractions.

The functional T_M is 1-Lipschitz in W2: apply the pointwise Lipschitz function (|x|-M)_+ under any coupling and then the triangle inequality in L2. Thus all empirical fixed-level primary and velocity tails converge uniformly in time at fixed cap. In particular their second moments are asymptotically uniformly integrable over time; this is a width-limit conclusion, not a uniform finite-width high-moment assertion.

## V.9. Descending true-backward observations and every raw kernel block

At fixed cap and fixed finite primary transcript, append the true chain in descending order:

    t_L=C, b_L=g_L(Y_L)t_L,
    t_l=A_(l+1)^*b_(l+1), b_l=g_l(Y_l)t_l, l=L-1,...,1.

For the first gate use g_L(Y_L)tau_M(C), a bounded-derivative instruction. At fixed M, (F) gives its joint law. Formula (V.28) and positive-part tail convergence remove M. The current action A_L^* consists of its initialized adjoint and its explicit learned rank-one sum. Uniform operator bounds and Cauchy--Schwarz transfer the input L2 error through both pieces, so the first true incoming field has the law of the actual population adjoint action. This is the descending induction base.

The induction invariant at level l+1 is joint W2 convergence of all higher true observations and the primary/velocity transcript, hence uniform removal of each of their finite empirical second-moment tails. Retain all inner caps representing this known chain and add an outer cap at t_l in the next product g_l(Y_l)tau_M(t_l). At fixed outer M remove inner caps first using bounded-derivative continuity, their known W2 laws, and bounded current action errors. Then remove M by (V.28) and the newly known second-moment tails of t_l. Apply A_l^* to obtain t_(l-1), transferring the error by its bounded action norm. This proves the invariant at level l. The finite chain reaches the bottom. The argument supplies actual observation laws; it does not claim an untruncated expected-derivative formula without separate domination.

For uniform time passage, at two states on a bounded ball downward substitution gives

    sum_(l,i)(||t_l-tbar_l||_2+||b_l-bbar_l||_2)
      <=C[(1+M)||Theta-Thetabar||raw
                            +sum_(l,i)T_M(tbar_l)].       (V.33)

This is proved by the same gate splitting as (V.29), now followed by bounded adjoint actions. Each M multiplies a forward state difference, so the downward recurrence again has one M. The true backward map is strongly continuous along converging raw states: first use (V.28) at the top, then bounded-action continuity and the same multiplier argument at each lower level. Its time image along a strong cap-flow path is consequently compact in L2. A compact L2 set has uniformly vanishing T_M tails: cover it by finitely many epsilon-balls, use the 1-Lipschitz property of T_M, and remove tails at the finitely many centers.

Apply (V.33) with the population cap flow as reference to pass coarse population true fields uniformly to the flow. At finite width apply it with the same-width coarse fields as reference. At fixed mesh and M the descending observational closure passes their tails. Take width, then mesh at fixed M, then M to infinity using compact population tails. This extends (V.32) and its joint-time form to all true backward observations.

The true ORIGINAL raw kernel blocks are, in the normalized fields used here,

    K^1_(ij)=a^(2L) Gamma_(ij)<b_(1,i),b_(1,j)>,
    K^l_(ij)=a^(2L)<b_(l,i),b_(l,j)><X_(l-1,i),X_(l-1,j)>, 2<=l<=L,
    K^(L+1)_(ij)=a^(2L)<X_(L,i),X_(L,j)>.                 (V.34)

The factor follows either by grad_raw f_i=a^L grad_raw F_i or by multiplying the original backward and feature scalings. Every pairing is within its layer, and all off-diagonal entries are retained. Under an L2 coupling,

    |E[UV]-E[Ubar Vbar]|
       <=||U-Ubar||_2||V||_2+||Ubar||_2||V-Vbar||_2.

Thus uniform-time W2 convergence proves uniform convergence of every block entry. At a capped state this is the true gradient kernel observed there; the clipped dynamics need not use it as their prediction coefficient matrix.

## V.10. Same-width cap comparison for actual finite uncut algorithms

The finite uncut GF vector field is locally Lipschitz in its finite-dimensional raw parameters. Its exact energy identity is

    dE_n/dt=-||dot Theta_n||raw^2.

Hence its raw length on [0,T] is <=sqrt(T E_n(0)). A finite-time escape in finite-dimensional parameter space is impossible, and local solutions extend globally. This argument is for actual uncut GF, not for a clipped surrogate.

Compare actual finite uncut GF to its same-width physical capped GF reference with the same nonzero random C_(0,n). Section V.8 puts that reference, with probability tending to one for every fixed R, in a primal ball chosen independently of R from (G), with fixed slack. Its incoming empirical positive-part tails converge uniformly in time. Since |q|1_(|q|>R)<=2(|q|-R/2)_+, (V.9) supplies their width-limit bound C exp(-cR^2). Until uncut exit, the finite version of (V.8) and Gronwall give a width-limit state and actual-direction error

    epsilon_R=C_T exp(C_T R-cR^2) ->0.                    (V.35)

Choose a large fixed R making this smaller than slack and then take width. The first-exit comparison excludes exit with probability tending to one. Substitution in (V.8) also controls all uncut versus capped-update backward fields.

For actual raw GD set t_k=k eta_n, eta_n=n^-2. Its raw direction on [t_k,t_(k+1)) is V_infty(Theta_n(t_k)); its hidden fields are recomputed from the linearly interpolated raw parameters. Let E(t)=sup_(s<=t)||Theta_n(s)-Theta_(R,n)(s)||raw. Apply (V.8) at t_k against the capped reference at t_k, then add the capped within-step direction variation <=C_(R,T)eta_n. Before exit,

    E(t)<=C(1+R)integral_0^t E(s)ds
       +Ct sup_(s<=T)sum_(l,i)||q_(R,l,i,n)(s)1_(|q_(R,l,i,n)(s)|>R)||_n
       +C_(R,T)t eta_n.                                  (V.36)

The preceding-node discrepancy is bounded by E(s) because t_k<=s. This proves (V.35), the same no-exit conclusion, and the same actual-direction estimate. No width-independent Lipschitz estimate on the uncut field is required. All finite GD iterates are well-defined finite compositions; the comparison proves their required finite-horizon boundedness with probability tending to one.

Take width at fixed cap after its fixed-cap auxiliary-mesh limit, and then let R tend to infinity. Population convergence (V.10), finite comparison (V.35), and the fixed-cap laws give both actual algorithms the same full-sequence prediction, loss, forward-field, and true-backward limits. The latter may be compared directly to capped UPDATE fields by (V.8); Section V.9 separately establishes true-kernel observations on capped trajectories. Formula (V.34) now gives every actual raw kernel block uniformly on the physical horizon. The two algorithms can share their initialized references and all finite unions of observations, so the convergence holds jointly for both algorithms.

## V.11. Velocity cap removal with the necessary tail order

Raw population cap states and directions converge uniformly by (V.10). Their uncut limit has continuous normalized preactivation velocities in L2 by the strong chain rule. Those compact time images have uniformly vanishing T_M tails. Apply (V.29) using the uncut state/direction as reference. First let R tend to infinity at fixed M and then M tend to infinity. This proves uniform strong convergence of all population capped hidden velocities to the uncut hidden velocities. The Lipschitz tail functional shows that sufficiently large population caps inherit the same uniform tail removal. No estimate of the growth of C_(R,T) in the fixed-cap fourth moments is needed.

For the finite uncut algorithm against its same-width capped-flow reference, (V.29) bounds the hidden-velocity error by

    C[beta_(R,n)+(1+M)alpha_(R,n)
                 +sum_(l,i)sup_(t<=T)T_(M,n)(P_(R,l,i,n)(t))],       (V.37)

where alpha and beta are their raw state and ACTUAL direction discrepancies. The constant depends only on the common primal/direction ball and fixed L,a,e, and is independent of R,M. At fixed R,M the empirical reference tails pass to their population counterparts by Section V.8. Now take the width limit, let R tend to infinity at fixed M using (V.35) and the population strong velocity convergence just proved, and finally let M tend to infinity. The expression vanishes.

Neuron-index coupling with the capped laws and population cap limit proves uniform-time same-layer joint W2 convergence for uncut states and velocities, and finite concatenations prove joint-time convergence. For GD the direction is its preceding-node raw direction, and the chain rule is evaluated at its interpolated state with that direction. Its neighboring capped reference times differ by at most eta_n; their continuous moduli make the same estimates apply. Use right directions at nodes, with a terminal-left convention if a terminal node is included. These choices do not affect integrated speeds.

The complete limit order is: (i) fixed transcript and observation caps, width, removal of inner caps while the new outer cap stays fixed, then removal of that outer cap; (ii) fixed training cap and auxiliary mesh, width, auxiliary mesh refinement; (iii) width at fixed training cap and velocity-tail threshold M, training-cap removal at fixed M, and finally M to infinity. This prevents multiplication of an uncontrolled cap-dependent velocity moment by a cap-removal error.

## V.12. W2 path laws, integrated speeds, and fixed generated probes

For each layer define the ORIGINAL hidden path tuple

    Zpath_l(t)=(z_(l,1),h_(l,1),z_(l,2),h_(l,2),z_(l,3),h_(l,3))(t).

Returning from normalized fields multiplies their state and velocity coordinates by the fixed numbers a^(l-1),a^l and therefore preserves every convergence already proved. These population coordinate paths, and the finite hidden fields recomputed along raw interpolation, are almost everywhere absolutely continuous. The chain-rule recursion, bounded current actions and g_l, and bounded raw directions give bounded RMS hidden speeds on the stopped ball. The no-exit comparisons remove stopping with probability tending to one.

For any absolutely continuous vector path x, and its linear interpolation I_h x on a fixed observation grid of maximum interval h, Cauchy--Schwarz on an interval [u,v] gives

    |x(t)-I_hx(t)|
       <=|x(t)-x(u)|+|x(v)-x(u)|
       <=2sqrt(h)(integral_u^v |x'(s)|^2 ds)^(1/2).

Consequently

    ||x-I_hx||infty^2<=4h integral_0^T |x'(s)|^2 ds.       (V.38)

Initial second moments and this speed bound give finite second moments of the path supremum norm. Average (V.38) over finite neurons and over the population coupling. The squared W2 interpolation cost is <=4h times the corresponding integrated RMS speed squared. At a fixed observation grid, the already-proved joint-node W2 laws pass through the Lipschitz interpolation map into the uniform path norm. A triangle inequality between finite paths, their grid interpolants, the population grid interpolant, and population paths, first taking width and then h to zero, proves

    W2(n^-1 sum_alpha delta_(Zpath_(l,n,alpha)), Law(Zpath_l)) ->0

in probability in C([0,T];R^6) with its supremum norm. This argument supplies the path tightness and second moments that cannot be inferred from fixed-time laws alone.

Uniform-time velocity W2 convergence gives uniform convergence of squared RMS speeds and all within-layer cross second moments. The elementary inequalities

    | ||U||_2^2-||V||_2^2 | <=(||U||_2+||V||_2)||U-V||_2

and the product estimate after (V.34) apply under the W2 couplings. The norms have common bounds on the no-exit ball. Multiplying a uniform error by T therefore gives convergence of all integrated squared hidden speeds and their within-layer cross products. These are actual neuron-coordinate velocities, not metric derivatives of marginal probability laws.

For each original raw block, true GF has

    ||dot Theta^(l)(t)||raw^2=(y-f(t))^T K^l(t)(y-f(t)).    (V.39)

Raw GD has the same identity with residual and kernel at its preceding node, since this is its actual raw direction. Uniform convergence of predictions and kernel blocks and eta_n to zero therefore give uniform-time and integrated convergence of all blockwise squared raw speeds. For fixed-cap directions use the corresponding capped-update backward Grams in place of true hidden blocks; these are primary contractions and obey the same conclusion.

Finally, take any fixed finite layer-typed generated probe program, formed from bounded-derivative coordinate maps, scalar contractions, specified generated roots, and either orientation of initialized or current adjacent actions. Include its fixed observations in (F), together with the primary and already identified observation transcript. If an input arises as a strong common-space L2 limit of finite generated probes, approximate it first by such a finite program. The propagation inequality is

    ||A u-Abar ubar||_2
       <=||A-Abar||op ||u||_2+||Abar||op||u-ubar||_2,      (V.40)

and exactly the same holds for adjoints. In same-width and common-population comparisons, operator differences are bounded by raw Hilbert--Schmidt differences and all current operator norms are bounded. Thus each finite instruction preserves vanishing approximation error. Uniform-time versions follow by a finite time net and the strong L2 continuity of the finite probe graph. Both action orientations, same-layer second moments, and finite joint-time laws are retained. Learned population increments converge strongly in Hilbert--Schmidt norm by (V.10); finite learned-increment contractions, when requested as observations, are finite rank unrollings followed by Riemann approximation of already converging bounded contractions.

All probability conclusions are along the full width sequence: every fixed-program theorem is full-sequence convergence in probability, and each subsequent comparison gives a deterministic width-limit error that can be made arbitrarily small in the stated order. The proof neither identifies operators across different widths nor takes a simultaneous infinite-depth or infinite-time limit.

# Part N. Nonzero initial motion and kernel variation at every depth

## Statement and scope

Let \(L\ge2\) be any fixed finite integer. Let \(u_i=x_i/\sqrt d\), \(i=1,2,3\), satisfy \(\|u_i\|=1\) and \(\Gamma_{ij}=\langle u_i,u_j\rangle\le1-\delta\) for \(i\ne j\), where \(\delta>0\). The requested absolute separation \(|\Gamma_{ij}|\le1-\delta\) is a special case. Let \(y_i\in\{-1,1\}\), \(p_i=y_i/3\), and

\[
\phi(z)=a(1+z)+e\psi(z),\qquad
\psi\in C^2(\mathbb R),\quad \psi\text{ bounded and nonconstant},\quad
\max_{k=0,1,2}\|\psi^{(k)}\|_\infty\le1.
\]

For the requested activation class assume \(a\ge4\) and \(0<e\le1\). In fact the proof below needs only

\[
                         0<e<a.                         \tag{N.1}
\]

For this initial-motion statement alone, any one fixed \(e\in(0,1]\) and any one fixed \(a\ge2\) work at every fixed finite depth. The full global theorem uses the larger gain selected in (M.4). Put \(\alpha=a-e>0\), \(B=a+e\). Then

\[
\alpha\le\phi'(z)\le B,\quad |\phi''(z)|\le e,
\quad |\phi(z)|\le a(1+|z|)+e.                          \tag{N.2}
\]

Use the canonical initialized Gaussian actions associated with independent first-layer entries \(N(0,1/d)\), independent higher-layer entries \(N(0,1/n)\), and population readout \(C(0)=0\). The actions and their transposes are the same initialized matrices in both orientations; their population extensions have genuine adjoints. All conclusions below concern these actions, not arbitrary bounded substitutions for them.

Every hidden raw block, every sample preactivation at every hidden layer, and every sample feature at every hidden layer has a nonzero initial acceleration along any canonical strong physical gradient flow from this initialization. More precisely, the accelerations are \(9V^\ell,9U_j^\ell,9T_j^\ell\), with the directions defined below. For the original raw metric and the sum of all true kernel blocks,

\[
p^TK_{\rm total}(t)p
=p^TK_{\rm total}(0)p+18t^2\|V\|_{\rm hidden}^2+o(t^2),
\qquad \|V\|_{\rm hidden}>0.                            \tag{N.3}
\]

The algebraic initialization statement is within the canonical Gaussian construction. Parts G and V have supplied the strong global physical solution needed for its interpretation as acceleration. It does prove the relevant chain rule from the stated strong regularity. No uniform positive numerical lower bound over \(L,e,\psi\) is claimed or needed.

The proof uses constant and linear Gaussian projections for forward positivity, fresh reverse sources for bottom motion, and fresh forward innovations for all upper samples. It never compares the nonlinear network with an affine network, and never needs a sign condition on \(\psi'\) or \(\psi''\).

## N.1. All forward Grams are positive definite

Write \(Z_i^1\) for the first Gaussian projection, with covariance \(\Gamma\), and recursively

\[
h_i^\ell=\phi(Z_i^\ell),\quad
Z_i^\ell=A_\ell h_i^{\ell-1}\ (\ell\ge2),\quad
D_i^\ell=\phi'(Z_i^\ell),\quad
Q_\ell=(E[h_i^\ell h_k^\ell])_{ik}.
\]

At initialization every \(Z^\ell\) is a centered Gaussian tuple. Its coordinates have the same marginal variance: this is true at layer 1 and propagates because the diagonal of the next covariance is \(E[\phi(Z_i^\ell)^2]\).

For any centered Gaussian tuple \(Z\) with equal marginal variance \(s^2>0\), define

\[
\mu_s=E\phi(sG)=a+eE\psi(sG),\qquad
b_s=E\phi'(sG)=a+eE\psi'(sG),
\]

where \(G\sim N(0,1)\). Integration by parts gives \(E[Z_i\phi(Z_i)]=s^2b_s\). The boundary term vanishes by linear growth and Gaussian decay. The Gaussian regression identity \(E[Z_k\mid Z_i]=\operatorname{Cov}(Z_k,Z_i)Z_i/s^2\) remains valid for singular tuples. Consequently

\[
r_i=\phi(Z_i)-\mu_s-b_sZ_i
\]

is orthogonal both to constants and to every coordinate \(Z_k\). Therefore the uncentered feature Gram is exactly

\[
Q=\mu_s^2\mathbf1\mathbf1^T+b_s^2\operatorname{Cov}(Z)
       +(E[r_ir_k])_{ik}.
\]

Since \(\mu_s,b_s\ge\alpha\), this proves

\[
Q_1\succeq\alpha^2(\Gamma+\mathbf1\mathbf1^T),\qquad
Q_\ell\succeq\alpha^2Q_{\ell-1}\quad(\ell\ge2).          \tag{N.4}
\]

Here is a direct quantitative proof that the augmented input Gram is positive, including singular \(\Gamma\). For \(c\in\mathbb R^3\),

\[
c^T(\Gamma+\mathbf1\mathbf1^T)c
=(\sum_i c_i)^2+\|\sum_i c_i u_i\|^2.
\]

When all nonzero coefficients have one sign, the first square is at least \(\|c\|^2\). Otherwise, after changing overall sign and permuting coordinates, write \(c=(r_1,r_2,-b)\) with \(r_1,r_2\ge0\), \(A=r_1+r_2>0\), \(b>0\). Put

\[
D=\{r_1(1-\Gamma_{13})+r_2(1-\Gamma_{23})\}/A\in[\delta,2].
\]

Projection onto \(u_3\) bounds the quadratic form below by

\[
(A-b)^2+((1-D)A-b)^2.
\]

The corresponding \(2\times2\) positive matrix has determinant \(D^2\) and trace \(D^2-2D+4\le4\), so its smaller eigenvalue is at least \(\delta^2/4\). Since \(A^2+b^2\ge\|c\|^2\),

\[
\Gamma+\mathbf1\mathbf1^T\succeq\delta^2I_3/4,
\qquad Q_\ell\succeq\alpha^{2\ell}\delta^2I_3/4>0.       \tag{N.5}
\]

Feasibility implies \(\delta\le2\), which also handles the one-sign case. Thus \(Z^\ell\) has full three-dimensional Gaussian support for every \(\ell\ge2\).

## N.2. Backward sources and every hidden block

Define

\[
H=\sum_i p_i h_i^L,\quad
\beta_i^L=D_i^LH,\quad
q_i^\ell=A_{\ell+1}^*\beta_i^{\ell+1},\quad
\beta_i^\ell=D_i^\ell q_i^\ell\ (\ell<L),\quad
S_\ell=(E[\beta_i^\ell\beta_k^\ell])_{ik}.
\]

The raw hidden directions and sample directions are

\[
V^1=d^{-1}\sum_i p_i\beta_i^1x_i,\qquad
V^\ell=\sum_i p_i\beta_i^\ell\otimes h_i^{\ell-1}
\quad(2\le\ell\le L),                                  \tag{N.6}
\]

\[
U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1,\qquad
T_j^\ell=D_j^\ell U_j^\ell,\qquad
U_j^\ell=V^\ell h_j^{\ell-1}+A_\ell T_j^{\ell-1}
\quad(\ell\ge2).                                      \tag{N.7}
\]

All norms and products are in their own layer probability spaces. In particular

\[
\|V\|_{\rm hidden}^2=d\|V^1\|_2^2+
                         \sum_{\ell=2}^L\|V^\ell\|_{\rm HS}^2.
\]

First \(S_L\succ0\). If \(v^TS_Lv=0\), full support and continuity give

\[
\left[\sum_i p_i\phi(z_i)\right]
\left[\sum_i v_i\phi'(z_i)\right]=0
\quad\text{for every }z\in\mathbb R^3.
\]

The first factor has no open zero set, because its derivative in coordinate \(i\) is \(p_i\phi'(z_i)\ne0\). Thus its nonzero set is dense, and the second factor vanishes identically by continuity. Differentiating in coordinate \(i\) gives \(v_i\phi''(z_i)=0\) for every \(z_i\). Bounded nonconstant \(\psi\) cannot have \(\psi''\equiv0\): such a function would be affine and bounded, hence constant. Since \(e>0\), \(\phi''\not\equiv0\), and \(v=0\).

The exact initialized transpose formulas are

\[
q_i^\ell=\zeta_i^\ell+\sum_k R^\ell_{ik}h_k^\ell,
\qquad \operatorname{Cov}(\zeta^\ell)=S_{\ell+1},        \tag{N.8}
\]

where each reverse source group \(\zeta^\ell\) is centered Gaussian and independent of all forward source groups and first-layer roots. The deterministic response coefficients are

\[
R^{L-1}_{ik}=E[p_kD_i^LD_k^L+
                 \mathbf1_{i=k}H\phi''(Z_i^L)],
\]

\[
R^\ell_{ik}=E[\mathbf1_{i=k}\phi''(Z_i^{\ell+1})q_i^{\ell+1}
                    +D_i^{\ell+1}R^{\ell+1}_{ik}D_k^{\ell+1}]
\quad(\ell<L-1).                                      \tag{N.9}
\]

Section N.4 derives and justifies these formulas. They include both the current curvature term and the next-layer return. Neither return is assumed positive or discarded.

Conditionally on \(Z^\ell\), (N.8) gives

\[
\operatorname{Cov}(\beta^\ell\mid Z^\ell)
=\operatorname{diag}(D^\ell)S_{\ell+1}\operatorname{diag}(D^\ell)
\succeq\alpha^2\lambda_{\min}(S_{\ell+1})I_3.
\]

Backward induction from \(S_L\succ0\) proves

\[
S_\ell\succeq\alpha^2\lambda_{\min}(S_{\ell+1})I_3\succ0
\quad(\ell<L).                                        \tag{N.10}
\]

The same formula applies at layer 1 even if \(Z^1\) is singular. Applying it componentwise in (N.6) and summing gives

\[
d\|V^1\|_2^2\ge\alpha^2\lambda_{\min}(S_2)\sum_i p_i^2>0.
\]

For every matrix block,

\[
\|V^\ell\|_{\rm HS}^2
=\operatorname{tr}(\operatorname{diag}(p)S_\ell
                  \operatorname{diag}(p)Q_{\ell-1})
\ge\lambda_{\min}(S_\ell)\lambda_{\min}(Q_{\ell-1})
                         \sum_i p_i^2>0.                \tag{N.11}
\]

The inequality follows by pairing \(S_\ell\succeq\lambda_{\min}(S_\ell)I\) with the positive matrix \(\operatorname{diag}(p)Q_{\ell-1}\operatorname{diag}(p)\), then using the analogous bound for \(Q_{\ell-1}\).

For the bottom samples,

\[
\|U_j^1\|_2^2\ge\alpha^2\lambda_{\min}(S_2)
                  \sum_i\Gamma_{ji}^2p_i^2
\ge\alpha^2\lambda_{\min}(S_2)p_j^2>0,                 \tag{N.12}
\]

using \(\Gamma_{jj}=1\). This proves every hidden block and every bottom sample is nonzero.

## N.3. Exact return recursion and an innovation at every upper layer

Fix one sample \(j\). Define deterministic coefficients

\[
c^1_{ji}=\Gamma_{ji}p_i,
\qquad
c^\ell_{ji}=p_i(Q_{\ell-1})_{ij}
          +c^{\ell-1}_{ji}E[D_j^{\ell-1}D_i^{\ell-1}]
\quad(2\le\ell\le L).                                \tag{N.13}
\]

No sign of these coefficients is required. Let \(\xi_{T_j^{\ell-1}}\) denote the primitive source of the added forward query \(A_\ell T_j^{\ell-1}\), belonging to the same oriented source group as the three original coordinates \(Z_i^\ell\). The exact recursion is

\[
U_j^\ell=\xi_{T_j^{\ell-1}}+\sum_i c^\ell_{ji}\beta_i^\ell
\qquad(2\le\ell\le L).                               \tag{N.14}
\]

To prove the base case, (N.8) at layer 1 and (N.7) show, differentiating in the named reverse source \(\zeta_i^1\),

\[
\partial_{\zeta_i^1}T_j^1=D_j^1c^1_{ji}D_i^1.
\]

The same-matrix forward response rule therefore reads

\[
A_2T_j^1=\xi_{T_j^1}+\sum_i\beta_i^2
                               c^1_{ji}E[D_j^1D_i^1].
\]

Adding \(V^2h_j^1=\sum_i p_i(Q_1)_{ij}\beta_i^2\) proves (N.14) for \(\ell=2\).

Now suppose (N.14) is proved at some \(2\le\ell<L\). Its primitive forward source belongs to the \(A_\ell\) forward group, which is independent of the \(A_{\ell+1}^*\) reverse group \(\zeta^\ell\). These are distinct named formal slots even if a covariance is singular. Formula (N.8) consequently gives the exact derivative

\[
\partial_{\zeta_i^\ell}T_j^\ell
=D_j^\ell c^\ell_{ji}D_i^\ell.
\]

Applying the forward response rule to \(A_{\ell+1}T_j^\ell\), then adding \(V^{\ell+1}h_j^\ell\), gives (N.14) at \(\ell+1\) with exactly (N.13). This proves (N.14) at every depth, with all transpose returns retained.

Regress the Gaussian source \(\xi_{T_j^{\ell-1}}\) on the three original forward sources \(Z^\ell\). Their covariance is \(Q_{\ell-1}\succ0\). Since oriented source covariances are the full input second moments, the independent regression remainder \(\varepsilon_{\ell j}\) has variance

\[
\sigma_{\ell j}^2
=\inf_{b\in\mathbb R^3}
       \left\|T_j^{\ell-1}-\sum_i b_i h_i^{\ell-1}\right\|_2^2.
                                                               \tag{N.15}
\]

This is linear regression without an intercept: the sources are centered, while their covariance is the **uncentered** input Gram. The conditional-variance bounds below hold for this precise regression because every competitor \(\sum_i b_i h_i^{\ell-1}\) is measurable in the conditioning variables.

At \(\ell=2\), all \(h_i^1\) are measurable in \(Z^1\), so (N.10) yields

\[
\begin{aligned}
\sigma_{2j}^2
&\ge E\operatorname{Var}(T_j^1\mid Z^1)\\
&\ge\alpha^4\lambda_{\min}(S_2)
                     \sum_i\Gamma_{ji}^2p_i^2
\ge\alpha^4\lambda_{\min}(S_2)p_j^2>0.                \tag{N.16}
\end{aligned}
\]

The remainder \(\varepsilon_{2j}\) is independent of \(Z^2\) and of the separate reverse group \(\zeta^2\), if present. By (N.8), all \(\beta_i^2\) are functions of \((Z^2,\zeta^2)\); at \(L=2\) they are functions of \(Z^2\) alone. Thus (N.14), after regression, is

\[
U_j^2=\varepsilon_{2j}+F_{2j}(Z^2,\zeta^2),
\]

with the unused reverse argument omitted at the top. In particular \(\|U_j^2\|_2^2\ge\sigma_{2j}^2\).

For the induction step assume \(2\le\ell<L\) and \(\sigma_{\ell j}^2>0\). Exactly the same regression in (N.14) gives

\[
U_j^\ell=\varepsilon_{\ell j}+F_{\ell j}(Z^\ell,\zeta^\ell),
\]

where \(\varepsilon_{\ell j}\) is independent of the displayed pair. Therefore

\[
\operatorname{Var}(T_j^\ell\mid Z^\ell,\zeta^\ell)
                  =(D_j^\ell)^2\sigma_{\ell j}^2.
\]

Testing (N.15) for the next layer against this conditional variance proves

\[
\sigma_{\ell+1,j}^2\ge E[(D_j^\ell)^2]\sigma_{\ell j}^2
                          \ge\alpha^2\sigma_{\ell j}^2>0.       \tag{N.17}
\]

The new remainder belongs to the next forward source group and is independent of its original forward tuple and separate reverse group; at the top there is no reverse group to condition on. Thus it cannot cancel the other terms of (N.14). Combining (N.16) and (N.17),

\[
\|U_j^\ell\|_2^2\ge\sigma_{\ell j}^2
       \ge\alpha^{2\ell}\lambda_{\min}(S_2)p_j^2>0
\quad(2\le\ell\le L).                                \tag{N.18}
\]

Together with (N.12), this covers every sample and layer. Finally \(\|T_j^\ell\|_2\ge\alpha\|U_j^\ell\|_2>0\). The three samples' new forward sources may be mutually correlated. No step assumes otherwise; one may prove the result with one fixed augmented transcript per sample and then take their finite union.

## N.4. The same-matrix source formulas and unbounded products

Only the finite Gaussian foundation is needed here. This section states its precise specialization, checks the actual query schedule, and proves its derivative-valid extension for every unbounded product used above. Oddness, monotonicity of the perturbation, and affine perturbation estimates play no role.

The actual finite initialization transcript, with normalized finite inner products, is as follows. First reveal the first-layer roots and calculate all three ordinary forward calls at each layer. Next form \(H\), the three top \(\beta_i^L\), and, descending through the layers, the three calls \(A_{\ell+1}^*\beta_i^{\ell+1}\) and the gates \(\beta_i^\ell\). For one fixed sample \(j\), form \(U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1\) and \(T_j^1\). Then ascend through layers \(2,\ldots,L\): make the one added query \(A_\ell T_j^{\ell-1}\), add \(\sum_i p_i\langle h_i^{\ell-1},h_j^{\ell-1}\rangle_n\beta_i^\ell\), and apply the gate to obtain \(T_j^\ell\). These are all the action probes used. Their empirical contractions converge to the \(Q\) coefficients; replacing these finitely many convergent scalar coefficients by their limits changes the normalized vector errors by \(o_P(1)\), because all participating vector norms are bounded in probability. One may therefore use deterministic limiting coefficients in the source calculation.

Here is the needed finite-program statement and why its use is legitimate. For a fixed finite list of independent \(N(0,1/n)\) matrices, reused in both orientations, fixed finite root tuples with finite second moment, and coordinate instructions that are \(C^1\) with bounded first derivatives, same-layer empirical laws and second moments converge. For an initialized forward query on \(h\), and reverse query on \(u\), their scalar source formulas are

\[
Ah=\xi_h+\sum_s u_sE[\partial_{\zeta_s}h],\qquad
A^*u=\zeta_u+\sum_r v_rE[\partial_{\xi_r}u],             \tag{N.19}
\]

where the sums use the previously queried inputs in the opposite orientation. Sources belonging to distinct orientations or matrices are independent; within one group the covariance is the full Gram of its query inputs. Formal derivatives freeze deterministic coefficients and covariance parameters and differentiate distinct named source slots.

The conditioning proof covers any fixed finite number of matrices: condition successively on the current transcript. A coordinate instruction reveals no new matrix randomness. A matrix query conditions only that matrix's residual Gaussian factor on one further linear observation; the other residual factors retain their product conditional law. Induction over the finite instruction list gives the stated conclusion with \(L-1\) matrices.

For explicit verification of (N.19), if old calls are \(AV=Y\), \(A^TU=Q\), Gaussian conditioning gives

\[
A\mid\mathcal H=M+P_{U^\perp}\widetilde A P_{V^\perp},
\quad
M=Y(V^TV)^{-1}V^T+U(U^TU)^{-1}Q^TP_{V^\perp},
\]

initially when the indicated Grams are nonsingular. Indeed \(M\) satisfies the two constraints and is orthogonal to all homogeneous solutions \(P_{U^\perp}KP_{V^\perp}\), so isotropic Gaussian projection proves the conditional law. With \(h_\perp=h-P_Vh\), the new answer is a regression term plus an opposite-orientation response and

\[
                     \|h_\perp\|_nP_{U^\perp}g_n.
\]

The removed Gaussian projection satisfies \(E[\|P_Ug_n\|_n^2\mid\mathcal H]=\operatorname{rank}(U)/n\to0\). The response coefficient is obtained from

\[
E[q_sh_\perp]=E[\zeta_sh_\perp],\qquad
E[\zeta h_\perp]=\operatorname{Cov}(\zeta)
                                  E[\nabla_\zeta h_\perp].
\]

The first identity uses the old-return representation of \(q_s\) and orthogonality to \(V\); the second is Gaussian integration by parts. Substituting the old forward source representations cancels the derivatives of the regression projection, leaving exactly (N.19). The covariance of the resulting new forward source with old sources is \(E[h v_r]\), and its variance is \(E[h^2]\). This proves (N.15), including the fact that conditioning on transpose queries cannot erase its positive innovation.

Singular first-layer roots are allowed and do not need an inverse. In this particular proof all original matrix forward Grams \(Q_\ell\) and backward Grams \(S_\ell\) are positive definite once established; for a separate fixed sample the augmented forward Gram is positive definite by (N.16)–(N.17). Alternatively Part F's singular-query extension uses fresh small input noises, converging finite covariance square roots and bounded action norms; it does not assume continuity of pseudoinverses. No extra probabilistic independence of matrix answers and their inputs is being introduced.

The untruncated coordinate products in the present program are not themselves globally bounded-derivative instructions, so they need a separate justification. Let \(\tau_M\) be smooth, equal to the identity on \([-M,M]\), with \(|\tau_M(q)|\le|q|\), \(|\tau_M'|\le1\), and bounded range. Such clips can be obtained by integrating a smooth cutoff. At the top use

\[
\beta_{i,M}^L=D_i^L\tau_M(H).
\]

Its derivative in the named forward source \(Z_k^L\) is

\[
D_i^L\tau_M'(H)p_kD_k^L
 +\mathbf1_{i=k}\phi''(Z_i^L)\tau_M(H).
\]

This is bounded in absolute value by a fixed constant times \(1+|H|\), independently of \(M\). The top forward fields have all finite moments, so dominated convergence gives the first line of (N.9). The clipped fields converge in \(L^2\), their Grams converge, and coupling the resulting Gaussian reverse sources via finite positive-semidefinite covariance square roots gives convergence of the sources and (N.8) at layer \(L-1\).

Suppose (N.8) has been justified at layer \(\ell+1\). Its explicit expression is a finite Gaussian source plus a deterministic linear combination of linear-growth Gaussian functions. Thus it has all finite moments. Its derivative in \(Z_k^{\ell+1}\) is \(R^{\ell+1}_{ik}D_k^{\ell+1}\). For the next clipped gate \(D_i^{\ell+1}\tau_N(q_i^{\ell+1})\), the required derivative is

\[
\mathbf1_{i=k}\phi''(Z_i^{\ell+1})\tau_N(q_i^{\ell+1})
 +D_i^{\ell+1}\tau_N'(q_i^{\ell+1})R^{\ell+1}_{ik}D_k^{\ell+1}.
\]

At fixed outer cap, remove all earlier caps; then let \(N\to\infty\). The final envelope is a constant times \(1+|q_i^{\ell+1}|\), which is integrable. This proves the second line of (N.9), the next source covariance, and (N.8) at layer \(\ell\). Repeating this explicit finite step proves the whole backward chain with only \(C^2\) regularity.

Here is an explicit coherent clipping program for all added forward queries. Let the backward caps at layers \(1,\ldots,L-1\) be \(N_1,\ldots,N_{L-1}\), and the top cap be \(N_L\). Thus

\[
\beta_i^{L,N}=D_i^L\tau_{N_L}(H),\quad
q_i^{\ell,N}=A_{\ell+1}^*\beta_i^{\ell+1,N},\quad
\beta_i^{\ell,N}=D_i^\ell\tau_{N_\ell}(q_i^{\ell,N}).
\]

Use these same \(\beta_i^{\ell,N}\) both as reverse query inputs and in the block contributions. Give each added forward gate its own cap \(M_\ell\):

\[
U_j^{1,N,M}=\sum_i\Gamma_{ji}p_i\beta_i^{1,N},\qquad
T_j^{\ell,N,M}=D_j^\ell\tau_{M_\ell}(U_j^{\ell,N,M}),
\]

\[
U_j^{\ell,N,M}=A_\ell T_j^{\ell-1,N,M}
                  +\sum_i p_i(Q_{\ell-1})_{ij}\beta_i^{\ell,N}
\quad(\ell\ge2).
\]

At all fixed caps these are legitimate bounded-derivative coordinate instructions and initialized action calls. Their source formulas have the exact form

\[
U_j^{\ell,N,M}=\xi_{T_j^{\ell-1,N,M}}
                     +\sum_i c^{\ell,N,M}_{ji}\beta_i^{\ell,N},
\]

with \(c^{1,N,M}_{ji}=\Gamma_{ji}p_i\). To derive the next coefficient, the previously established backward formula gives

\[
\partial_{\zeta_i^\ell}\beta_k^{\ell,N}
=\mathbf1_{i=k}D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N}).
\]

The current forward primitive source is a different named slot from \(\zeta_i^\ell\), so

\[
\partial_{\zeta_i^\ell}T_j^{\ell,N,M}
=D_j^\ell\tau_{M_\ell}'(U_j^{\ell,N,M})
       c^{\ell,N,M}_{ji}D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N}).
                                                               \tag{N.22}
\]

Consequently, for \(\ell<L\),

\[
c^{\ell+1,N,M}_{ji}=p_i(Q_\ell)_{ij}
 +c^{\ell,N,M}_{ji}E[D_j^\ell\tau_{M_\ell}'(U_j^{\ell,N,M})
                          D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N})].
                                                               \tag{N.23}
\]

This proves the full capped source recurrence, rather than assuming a limit of the uncapped formula. In particular define finite deterministic bounds

\[
C^1_{ji}=|\Gamma_{ji}p_i|,\qquad
C^{\ell+1}_{ji}=|p_i(Q_\ell)_{ij}|+B^2C^\ell_{ji}.
\]

Then \(|c^{\ell,N,M}_{ji}|\le C^\ell_{ji}\), and the derivative in (N.22) is bounded by \(B^2C^\ell_{ji}\), uniformly in **all** caps. No smallness of these constants with depth is required.

First remove the backward caps in the descending dependency order established above, at fixed forward caps. Actual action continuity and the bounded gate comparisons give \(L^2\) convergence of \(q,\beta,U,T\) successively; their source Grams converge as well. Couple the finite source vectors through covariance square roots. Along a coupled subsequence their arguments converge almost surely; continuity and the bound \(B^2C^\ell_{ji}\) pass (N.22)–(N.23) under expectation. Next remove the forward caps in ascending order \(M_1,M_2,\ldots,M_L\), holding later caps fixed. The already identified incoming \(U_j^\ell\) is in \(L^2\), so \(\tau_{M_\ell}(U_j^\ell)\to U_j^\ell\) in \(L^2\). The subsequent initialized answers converge by bounded actions. In (N.22), the outer clip derivative tends to one and its integrand remains bounded by \(B^2C^\ell_{ji}\); (N.23) therefore converges to (N.13) at that layer. This proves the uncapped (N.14) and its bounded formal source derivative at every step. Each resulting \(U_j^\ell,T_j^\ell\) is, from its explicit source expression, a bounded gate times finite sums of Gaussian sources and linear-growth Gaussian functions, so it also has all finite moments.

To identify these limiting formulas with the actual uncut action answers, use bounded initialized action norms and bounded multiplier continuity. If \(z_m\to z\) in probability and \(q_m\to q\) in \(L^2\), then

\[
\|D(z_m)q_m-D(z)q\|_2
\le B\|q_m-q\|_2+\|[D(z_m)-D(z)]q\|_2\to0.
\]

For the second term restrict \(q\) to a bounded set, use bounded convergence in probability there, and then make its \(L^2\) tail small. Matrix action errors are bounded by the action norm times their input errors. Explicitly, a gate clipping error obeys

\[
\|D(z)[q-\tau_M(q)]\|_2
\le2B\|q\mathbf1_{|q|>M}\|_2
\le4B\|(|q|-M/2)_+\|_2\longrightarrow0.
\]

The same inequality holds in empirical normalized norm. Joint \(\mathcal W_2\) convergence of an incoming finite-array field implies convergence of the squared norm of \((|q|-M/2)_+\), since this is a 1-Lipschitz transformation followed by its second moment. Thus the empirical clipping tail is small after taking width to infinity and then \(M\to\infty\). The high-probability uniform bounds on the finitely many initialized matrix norms transfer this error to the next actual answer. Apply this gate/action step in the exact finite schedule above. A triangle inequality, with fixed caps first, identifies the full uncut finite-array law and its second moments, as well as its canonical action answers. The source laws, current responses, and input covariances all survive the ordered removal of the clips.

## N.5. Physical acceleration and the coefficient 18

Let a strong physical gradient-flow solution in the original raw Hilbert metric exist on a right neighborhood of zero. Its current hidden actions are their initialized actions plus Hilbert–Schmidt increments. Denote the residual-free physical backward fields by

\[
b_i^L(t)=D_i^L(t)C(t),\qquad
b_i^\ell(t)=D_i^\ell(t)A_{\ell+1}(t)^*b_i^{\ell+1}(t).
\]

The physical loss is \(\tfrac12\sum_i(f_i-y_i)^2\), so the exact raw updates are

\[
C'=-\sum_i r_i h_i^L,\quad
(\theta_h^1)'=-d^{-1}\sum_i r_i b_i^1x_i,\quad
A_\ell'=-\sum_i r_i b_i^\ell\otimes h_i^{\ell-1}.
\]

Since \(C(0)=0\), the initial predictions vanish, \(r_i(0)=-y_i=-3p_i\), all hidden first derivatives vanish, and

\[
C'(0)=3H,\qquad C(t)/t\longrightarrow3H.
\]

Strong multiplier continuity from Section N.4 and operator-norm continuity of the Hilbert–Schmidt action increments give, successively from the top,

\[
b_i^\ell(t)/t\longrightarrow3\beta_i^\ell.
\]

Substitution in the exact raw updates yields

\[
\theta_h'(t)/t\longrightarrow9V,\qquad
\theta_h(t)=\theta_h(0)+\tfrac92t^2V+o_{\rm raw}(t^2).  \tag{N.20}
\]

For a strong \(C^1\) \(L^2\) curve \(z(t)\) and bounded continuous \(\phi'\), the identity

\[
\frac{\phi(z(t+h))-\phi(z(t))}{h}
=\frac{z(t+h)-z(t)}h
  \int_0^1\phi'(z(t)+s[z(t+h)-z(t)])\,ds
\]

and bounded multiplier continuity prove the strong chain rule. Combining it with the product rule for a strongly differentiable field and an operator differentiable in Hilbert–Schmidt norm proves recursively

\[
(z_j^\ell)'(t)/t\longrightarrow9U_j^\ell,\qquad
(h_j^\ell)'(t)/t\longrightarrow9T_j^\ell.               \tag{N.21}
\]

Since the initial first derivatives are zero, (N.20)–(N.21) are the claimed nonzero strong right second derivatives.

To compute the kernel coefficient without assuming an ambient \(L^2\)-to-\(L^2\) Fréchet derivative of the activation, put

\[
T=\sum_jp_jT_j^L.
\]

Genuine adjunction and (N.6)–(N.7) give the following exact telescoping identity. At a matrix layer,

\[
\sum_jp_j\langle\beta_j^\ell,U_j^\ell\rangle
=\|V^\ell\|_{\rm HS}^2
 +\sum_jp_j\langle q_j^{\ell-1},T_j^{\ell-1}\rangle
=\|V^\ell\|_{\rm HS}^2
 +\sum_jp_j\langle\beta_j^{\ell-1},U_j^{\ell-1}\rangle.
\]

The final bottom sum is \(d\|V^1\|_2^2\), and the top sum is \(\langle H,T\rangle\). Hence

\[
                         \langle H,T\rangle=\|V\|_{\rm hidden}^2.
\]

Writing \(H(t)=\sum_jp_jh_j^L(t)\), (N.21) gives

\[
H(t)=H+\tfrac92t^2T+o_{L^2}(t^2),\qquad
\|H(t)\|_2^2=\|H\|_2^2+9t^2\|V\|_{\rm hidden}^2+o(t^2).
\]

The hidden part \(g_h(t)\) of the raw gradient of \(\sum_i p_i f_i(t)\) satisfies \(g_h(t)/t\to3V\) by the same backward calculation, so

\[
\|g_h(t)\|_{\rm hidden}^2=9t^2\|V\|_{\rm hidden}^2+o(t^2).
\]

The true raw kernel identity is

\[
p^TK_{\rm total}(t)p=\|H(t)\|_2^2+\|g_h(t)\|_{\rm hidden}^2.
\]

Adding its two terms proves (N.3). All \(L\) hidden blocks occur in \(\|V\|_{\rm hidden}^2\), and each is strictly positive by Section N.2. The coefficient 18 and the nonzero accelerations therefore persist at every fixed depth with the same fixed activation. The severe depth-dependent smallness imposed by an affine comparison is unnecessary for this initial-motion conclusion.

# Part A. Uniform activation classes and depth-uniform nonaffinity

Fix the three-input separation parameter \(\delta>0\), and set
\[
\lambda=\delta^2/16,\qquad T_0=12/\lambda.
\]
Let
\[
\mathcal B=\left\{\psi\in C_b^2(\mathbb R):
          \max_{k=0,1,2}\|\psi^{(k)}\|_\infty\le1\right\},
\qquad
\phi(z)=a(1+z)+e\psi(z),\quad 0<e\le1.
\]
Here \(C_b^2(\mathbb R)\) consists of twice continuously differentiable real functions with bounded derivatives of orders zero, one, and two, and carries the displayed maximum norm. Throughout, \(e\) is fixed when comparing depths.

The main theorem supplies, for each fixed finite hidden depth \(L\ge2\), its global strong physical trajectory and the estimate
\[
\max_{i,\ 1\le\ell\le L}\sup_{t\ge0}
 \|z_i^\ell(t)-z_i^\ell(0)\|_2
\le d_L,\qquad
d_L=3\sqrt L\left(\frac{32768}{a}\right)^L\frac{T_0^2}{a}.
                                                               \tag{A.1}
\]
Its function-independent dynamical estimates require
\(a\ge10^{12}(1+T_0)\). This appendix proves exactly how one can choose the remaining gain condition uniformly over classes of functions, and when the nonaffinity lower bound can also be uniform over depth. All constants selected below depend only on \(\delta\) and the specified class, and not on \(L\), the dataset, time, or the fixed \(e\in(0,1]\).

## A.1. Elementary regression estimates

For a square-integrable real random variable \(X\), define
\[
\mathcal R_\psi(X)=\inf_{\alpha,\beta\in\mathbb R}
                       E[\psi(X)-\alpha-\beta X]^2.
\]
The infimum is attained. If \(\operatorname{Var}(X)>0\), direct completion of squares gives an optimal slope
\[
\beta_X=\frac{\operatorname{Cov}(X,\psi(X))}
                     {\operatorname{Var}(X)},\qquad
\alpha_X=E\psi(X)-\beta_XEX.
\]
When \(X\) is almost surely constant, choose \(\beta_X=0\) and
\(\alpha_X=\psi(X)\).

For \(\psi\in\mathcal B\), its Lipschitz constant is at most one. If \(X'\) is an independent copy of \(X\), expansion and independence give
\[
\operatorname{Cov}(X,\psi(X))
=\tfrac12E[(X-X')(\psi(X)-\psi(X'))],
\qquad E[(X-X')^2]=2\operatorname{Var}(X).
\]
Consequently \(|\beta_X|\le1\). In particular optimal slopes need not be positive, but they remain in the fixed interval \([-1,1]\).

For two square-integrable variables \(X,Y\) on a common probability space, use the optimal affine fit at \(Y\) as a competitor at \(X\). The triangle inequality and \(|\beta_Y|\le1\) give
\[
\begin{aligned}
\sqrt{\mathcal R_\psi(X)}
&\le\|\psi(X)-\alpha_Y-\beta_YX\|_2\\
&\le\sqrt{\mathcal R_\psi(Y)}
       +\|\psi(X)-\psi(Y)-\beta_Y(X-Y)\|_2\\
&\le\sqrt{\mathcal R_\psi(Y)}+2\|X-Y\|_2.
\end{aligned}
\]
Interchanging \(X,Y\) proves the useful stability estimate
\[
\left|\sqrt{\mathcal R_\psi(X)}
       -\sqrt{\mathcal R_\psi(Y)}\right|
                         \le2\|X-Y\|_2.                 \tag{A.2}
\]

At a fixed \(X\), the corresponding estimate for changing the function is
\[
\left|\sqrt{\mathcal R_\psi(X)}
       -\sqrt{\mathcal R_\chi(X)}\right|
\le\|\psi(X)-\chi(X)\|_2\le\|\psi-\chi\|_\infty.          \tag{A.3}
\]
Indeed test each regression problem with an optimal affine fit for the other and use the triangle inequality. This estimate does not require bounds on the derivatives.

Finally the affine part of \(\phi\) can be absorbed exactly into the free regression coefficients. Since \(e>0\), the substitutions
\(\widetilde\alpha=(\alpha-a)/e\) and
\(\widetilde\beta=(\beta-a)/e\) range over all real pairs. Thus
\[
\inf_{\alpha,\beta}E[\phi(X)-\alpha-\beta X]^2
                              =e^2\mathcal R_\psi(X).    \tag{A.4}
\]

## A.2. Finite-interval margins and a common gain

For \(r\ge1\), put
\[
J_r(\psi)=\inf_{\alpha,\beta}
                   \int_{-r}^r[\psi(x)-\alpha-\beta x]^2\,dx.
\]
The functions \(1,x\) are orthogonal on this interval and have squared norms \(2r,2r^3/3\). Completing squares therefore gives
\[
J_r(\psi)=\int_{-r}^r\psi(x)^2\,dx
 -\frac1{2r}\left(\int_{-r}^r\psi(x)\,dx\right)^2
 -\frac3{2r^3}\left(\int_{-r}^r x\psi(x)\,dx\right)^2.     \tag{A.5}
\]
In particular the infimum is attained. It is zero exactly when
\(\psi\) equals an affine function almost everywhere on \([-r,r]\); continuity then gives equality everywhere on that interval.

Every bounded nonconstant \(\psi\in C^2(\mathbb R)\) has some \(r\ge1\) with \(J_r(\psi)>0\). Otherwise its restrictions to all intervals \([-n,n]\), for positive integers \(n\), would be affine. These affine functions agree on their overlapping intervals, so their two coefficients agree. Thus \(\psi\) would be affine on all of \(\mathbb R\), and boundedness would make it constant, a contradiction.

Fix any such interval, and define
\[
c_\psi=\frac{e^{-r^2/2}J_r(\psi)}{\sqrt{2\pi}}>0.         \tag{A.6}
\]
For \(G\sim N(0,1)\) and \(\sigma\ge1\), its scaled density on \([-r,r]\) obeys
\[
\frac1{\sigma\sqrt{2\pi}}
        e^{-x^2/(2\sigma^2)}
\ge\frac{e^{-r^2/2}}{\sigma\sqrt{2\pi}}.
\]
Applying this pointwise lower bound to every squared affine-regression error and then taking the infimum proves
\[
                    \mathcal R_\psi(\sigma G)
                                  \ge c_\psi/\sigma.    \tag{A.7}
\]

We record the initialized variance bounds used with (A.7). Write
\(z_i^\ell(0)\overset d=\sigma_\ell G\). All samples have the same marginal variance at a fixed layer, and \(\sigma_1=1\). The recursion of the initialized Gaussian program is
\[
\sigma_{\ell+1}=\|\phi(\sigma_\ell G)\|_2.
\]
Integration by parts gives the coefficient of the projection of
\(\phi(\sigma G)\) onto \(G\):
\[
E[G\phi(\sigma G)]
=\sigma E[\phi'(\sigma G)]\ge(a-e)\sigma.
\]
Its absolute value is bounded by the \(L^2\) norm of the feature, because \(\|G\|_2=1\). Thus
\[
\sigma_\ell\ge(a-e)^{\ell-1}
                          \ge(a/2)^{\ell-1}\ge1,         \tag{A.8}
\]
where \(a\ge4\) and \(e\le1\) suffice. For an upper bound, the triangle inequality gives
\[
\sigma_{\ell+1}
\le a\sqrt{1+\sigma_\ell^2}+e
\le a\sigma_\ell+2a.
\]
Dividing by \(a^\ell\), summing this scalar recurrence, and using \(a\ge4\) gives
\[
\frac{\sigma_\ell}{a^{\ell-1}}
\le1+2\sum_{k=0}^{\ell-2}a^{-k}
\le1+\frac2{1-a^{-1}}\le\frac{11}{3}<4.
\]
Hence
\[
                     1\le\sigma_\ell\le4a^{\ell-1}.      \tag{A.9}
\]
The first-layer upper bound also follows directly from \(\sigma_1=1\).

Select
\[
a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{c_\psi}}\right)^{2/5}\right\}.
                                                               \tag{A.10}
\]
Here is the arithmetic that makes this one gain work at every fixed depth. Put \(q=32768/\sqrt a=2^{15}/\sqrt a\). The first condition in (A.10) gives \(q<1/2\). For \(L\ge2\), the ratio of consecutive terms of \(\sqrt Lq^{L-2}\) is
\[
q\sqrt{\frac{L+1}{L}}\le\tfrac12\sqrt{\tfrac32}<1.
\]
Therefore \(\sqrt Lq^{L-2}\le\sqrt2\), and (A.1) yields
\[
\begin{aligned}
d_La^{(L-1)/2}
&=\frac{3T_0^2}{a^{3/2}}\sqrt Lq^L\\
&\le\frac{3\sqrt2\,2^{30}T_0^2}{a^{5/2}}\\
&\le\frac{3\sqrt2}{64}\sqrt{c_\psi}
 <\frac{\sqrt{c_\psi}}8.
\end{aligned}                                                   \tag{A.11}
\]
The last strict inequality is \(3\sqrt2<8\).

By (A.7)–(A.9), the initialized regression residual at layer \(\ell\) satisfies
\[
\sqrt{\mathcal R_\psi(z_i^\ell(0))}
                    \ge\frac{\sqrt{c_\psi}}{2a^{(\ell-1)/2}}.
\]
For \(\ell\le L\), (A.11) gives
\[
2d_L\le\frac{\sqrt{c_\psi}}{4a^{(L-1)/2}}
       \le\frac{\sqrt{c_\psi}}{4a^{(\ell-1)/2}}.
\]
Apply (A.2) to the coupling of the initialized and trained fields in (A.1), then use (A.4). This proves, for every sample, layer, and time,
\[
\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
\ge \frac{e^2c_\psi}{16a^{\ell-1}}
\ge \frac{e^2c_\psi}{16a^{L-1}}.                         \tag{A.12}
\]

Now let \(\mathcal C\subset\mathcal B\) be any class with a common interval \(r\ge1\) and common margin \(j>0\):
\[
                         J_r(\psi)\ge j
                         \quad(\psi\in\mathcal C).
\]
Set \(c_0=e^{-r^2/2}j/\sqrt{2\pi}\), and use (A.10) with \(c_\psi\) replaced by \(c_0\). The density bound, gain arithmetic, and proof of (A.12) then hold for every \(\psi\in\mathcal C\), with this same \(a\) and the common lower bound
\[
\frac{e^2c_0}{16a^{\ell-1}}\ge\frac{e^2c_0}{16a^{L-1}}.
\]
More generally it is enough for each member to have a possibly different interval witnessing \(c_\psi\ge c_0>0\); the argument uses only the common constant \(c_0\).

These interval classes contain open neighborhoods of many shapes. To check this without a compactness assertion about the class, choose a bounded nonconstant \(\psi_*\) with \(\|\psi_*\|_{C_b^2}<1\), and choose \(r\) with \(J_r(\psi_*)>0\). Testing an optimal affine fit for one function in the other interval problem gives
\[
\left|\sqrt{J_r(\psi_*+u)}-\sqrt{J_r(\psi_*)}\right|
                       \le\|u\|_{L^2[-r,r]}
                       \le\sqrt{2r}\|u\|_\infty.
\]
Thus any positive radius \(\rho\) satisfying
\[
\rho\le\frac{1-\|\psi_*\|_{C_b^2}}2,\qquad
\rho\le\frac{\sqrt{J_r(\psi_*)}}{2\sqrt{2r}}
\]
gives \(\psi_*+u\in\mathcal B\) and
\(J_r(\psi_*+u)\ge J_r(\psi_*)/4\) whenever
\(\|u\|_{C_b^2}<\rho\). Section A.4 below verifies explicitly that such neighborhoods have infinitely many independent directions.

## A.3. Why the broad class cannot have a positive depth-uniform margin

Let \(\psi\) be any nonzero compactly supported \(C^2\) function, normalized into \(\mathcal B\). For every \(\sigma>0\), testing the regression problem with the zero affine function gives
\[
0\le\mathcal R_\psi(\sigma G)
\le E[\psi(\sigma G)^2]
\le\frac1{\sigma\sqrt{2\pi}}\int_{\mathbb R}\psi(x)^2\,dx.
                                                               \tag{A.13}
\]
The integral is finite by compact support and continuity. Thus the Gaussian regression residual tends to zero as \(\sigma\to\infty\).

Keep \(a\ge4\) and \(e\in(0,1]\) fixed, and consider networks with increasing depth. Their initialized marginal variances satisfy (A.8), so \(\sigma_\ell\to\infty\). At initialization, (A.4) and (A.13) therefore give
\[
\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(0))-\alpha-\beta z_i^\ell(0)]^2
=e^2\mathcal R_\psi(\sigma_\ell G)\longrightarrow0.
\]
In particular even this single admissible perturbation admits no positive lower bound uniform over all hidden depths and all times: the proposed bound would already fail at \(t=0\). This explains the depth-dependent margin in the broad theorem. It does not assert that the particular numerical lower bound (A.12) is optimal.

## A.4. A stronger class with a positive depth-uniform margin

Suppose instead that a class \(\mathcal C\subset\mathcal B\) satisfies
\[
\inf_{\psi\in\mathcal C}\inf_{\sigma\ge1}
                  \mathcal R_\psi(\sigma G)\ge\eta_0>0.  \tag{A.14}
\]
Choose the common gain
\[
a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{\eta_0}}\right)^{2/5}\right\}.
                                                               \tag{A.15}
\]
The arithmetic in (A.11), now with \(\eta_0\), gives
\[
d_La^{(L-1)/2}\le\sqrt{\eta_0}/8,
\qquad d_L\le\sqrt{\eta_0}/8<\sqrt{\eta_0}/4.
\]
Since \(\sigma_\ell\ge1\), (A.14) supplies an initialized square-root residual at least \(\sqrt{\eta_0}\). By (A.1)–(A.2), its trained square-root residual is at least
\(\sqrt{\eta_0}-2d_L\ge\sqrt{\eta_0}/2\). Thus (A.4) proves
\[
\inf_{t\ge0}\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
                              \ge e^2\eta_0/4            \tag{A.16}
\]
for every fixed \(L\ge2\), every \(1\le\ell\le L\), every sample, and every member of the class. Neither \(\eta_0\) nor the selected \(a\) changes with depth. The same fixed perturbation amplitude \(e\) is used throughout.

We now construct a nonempty infinite-dimensional open \(C_b^2\) ball satisfying (A.14).

First consider any bounded continuous nonconstant function \(\psi\) with distinct limits \(\ell_-,\ell_+\) at negative and positive infinity. For \(\sigma>0\), the functions \(1,G\) are orthonormal in Gaussian \(L^2\), and
\(\operatorname{span}\{1,\sigma G\}=\operatorname{span}\{1,G\}\). Direct completion of squares gives
\[
\mathcal R_\psi(\sigma G)
=E[\psi(\sigma G)^2]
 -(E[\psi(\sigma G)])^2
 -(E[G\psi(\sigma G)])^2.                               \tag{A.17}
\]
This is strictly positive for every fixed \(\sigma>0\). Indeed a zero residual would give \(\psi(\sigma G)=\alpha+\gamma G\) almost surely. The difference of these continuous functions of \(G\) would then vanish everywhere: if it were nonzero at one point, continuity would make it nonzero on an open interval of positive Gaussian probability. Therefore \(\psi(x)=\alpha+(\gamma/\sigma)x\) on all of \(\mathbb R\). Boundedness forces \(\gamma=0\), contradicting nonconstancy.

The residual in (A.17) is continuous in \(\sigma>0\). For any convergent positive scale sequence, continuity of \(\psi\) gives pointwise convergence of the integrands. Boundedness of \(\psi\) bounds the first two integrands by constants and the last by a constant times \(|G|\), which is integrable. Dominated convergence gives the assertion.

Put
\[
m=(\ell_++\ell_-)/2,\qquad b=(\ell_+-\ell_-)/2\ne0.
\]
For every \(G\ne0\), which holds with probability one,
\(\psi(\sigma G)\to m+b\,\operatorname{sgn}(G)\) as
\(\sigma\to\infty\). Boundedness gives convergence in \(L^2\). The limit of (A.17) is consequently
\[
b^2\bigl(1-(E|G|)^2\bigr)=b^2(1-2/\pi)>0.              \tag{A.18}
\]
Here \(E\operatorname{sgn}(G)=0\) by symmetry and
\[
E|G|=\frac2{\sqrt{2\pi}}
       \int_0^\infty x e^{-x^2/2}\,dx=\sqrt{2/\pi}.
\]
Choose a finite \(M\ge1\) such that the residual for every \(\sigma\ge M\) is at least half its positive limit in (A.18). On the compact interval \([1,M]\), the continuous strictly positive residual attains a strictly positive minimum. The smaller of these two positive bounds proves
\[
                       \inf_{\sigma\ge1}
                          \mathcal R_\psi(\sigma G)>0.   \tag{A.19}
\]
This argument proves positivity of an actual numerical constant associated with a fixed function; it does not assume a compactness property for an infinite function class.

Apply it to
\[
\psi_0(x)=\tfrac14\arctan x.
\]
Its derivatives are
\[
\psi_0'(x)=\frac1{4(1+x^2)},\qquad
\psi_0''(x)=-\frac{x}{2(1+x^2)^2}.
\]
Thus
\[
\|\psi_0\|_\infty=\pi/8,\quad
\|\psi_0'\|_\infty=1/4,\quad
\|\psi_0''\|_\infty=3\sqrt3/32,
\qquad \|\psi_0\|_{C_b^2}=\pi/8<1.
\]
For the second derivative maximum, differentiating
\(x/(1+x^2)^2\) on \(x\ge0\) gives derivative
\((1-3x^2)/(1+x^2)^3\); its unique positive critical point is \(x=1/\sqrt3\), which yields the displayed value.
The tail limits are \(-\pi/8,\pi/8\), so (A.18) has the positive value
\(\pi^2(1-2/\pi)/64\). Define
\[
\eta_b=\inf_{\sigma\ge1}\mathcal R_{\psi_0}(\sigma G)>0,
\qquad
\rho=\min\left\{\frac{1-\pi/8}{2},\frac{\sqrt{\eta_b}}2\right\}>0.
\]
Consider the open ball
\[
\mathcal C_\rho
=\{\psi_0+u:\ u\in C_b^2(\mathbb R),\ \|u\|_{C_b^2}<\rho\}.
\]
It is an open \(C_b^2\) ball contained in \(\mathcal B\), hence also open relative to the normalized admissible class. Indeed its members have norm at most
\(\pi/8+\rho<1\). By (A.3), for every \(\sigma\ge1\),
\[
\sqrt{\mathcal R_{\psi_0+u}(\sigma G)}
\ge\sqrt{\eta_b}-\|u\|_\infty
\ge\sqrt{\eta_b}/2.
\]
Thus this entire ball satisfies (A.14) with the single constant
\[
                              \eta_0=\eta_b/4>0.         \tag{A.20}
\]
In particular all its members are nonconstant. This constant depends only on the displayed fixed center and radius, and is independent of \(\delta\); the gain in (A.15) still depends on \(\delta\) through \(T_0\).

For an explicit verification of infinite dimensionality, let
\[
v(x)=c(1-x^2)^3\mathbf1_{\{|x|<1\}},
\]
where \(c>0\) is small enough that \(\|v\|_{C_b^2}\le1\).
The function and its first two derivatives vanish at the endpoints \(\pm1\), so it is a nonzero compactly supported \(C_b^2\) function. The translates \(v_k(x)=v(x-3k)\), \(k\ge1\), have disjoint supports. For every positive integer \(N\) and any real coefficients with \(\max_{k\le N}|s_k|<\rho\),
\[
\left\|\sum_{k=1}^Ns_kv_k\right\|_{C_b^2}
\le\max_{k\le N}|s_k|<\rho.
\]
The translates are linearly independent, since each is nonzero on a support disjoint from all the others. Hence the ball contains parameter families of arbitrarily large finite dimension, proving it has infinitely many independent directions.

Membership in this ball does not require tail limits or oddness. For example a sufficiently small cosine perturbation belongs to the ball and has oscillating tails and breaks oddness. Its common lower bound follows from the uniform norm estimate (A.3), even though the tail-limit proof applies only to the fixed center. The full activation remains strictly increasing because
\(\phi'=a+e\psi'\ge a-e>0\).

## A.5. Scope of the uniform conclusions

For a class with a common finite-interval margin, the same gain and all main-theorem conclusions hold for every fixed member and every fixed finite depth, with the common lower bound (A.12). For a class satisfying (A.14), the same parameter recipe with \(\eta_0\) instead of \(c_\psi\) improves that bound to (A.16), uniform also in hidden depth.

The finite-width convergence statements retain their original quantifiers: the function, dataset, finite depth, and observation horizon are fixed before width tends to infinity. Sharing constants across a class does not by itself assert uniform finite-width convergence over that infinite class, simultaneous width/depth limits, or a positive margin independent of \(e\) as \(e\downarrow0\). The construction uses the original raw metric and the displayed affine-plus-perturbation activation throughout.
