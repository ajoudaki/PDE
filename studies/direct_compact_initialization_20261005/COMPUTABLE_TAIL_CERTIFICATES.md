# Computable finite-state tail certificates and rational initialization

2026-10-06. Scoped author proof, not an independent review or a promotion.
The results below are conditional certificates for specified finite systems.
They do not construct a direct initializer or establish a compact width bound.

Scientific inputs read completely: `docs/notation.qmd` (SHA-256
`78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`)
and the explicitly assigned
`studies/closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`
(SHA-256
`ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2`).
No linked study dependencies or other study reports were read. Only the
explicit autonomous equations and their directly rederived energy identity
are used from the second input; none of its compression or probability
theorems is imported. The rigorous-math skill was read. The user-required
canonical-notation skill and its linked neural-network reference were
inaccessible at the specified path, including after an escalation attempt;
the supervisor authorized proceeding under the explicit presentation rules
and maintained notation contract. No experiments or Git mutations occurred.

## 1. The two finite systems and their actual outputs

Fix sample count \(m\ge1\), input dimension \(d\ge1\), training data

\[
 v_a=x_a/\sqrt d,\qquad \|v_a\|_2=1,\qquad
 y=(y_1,\ldots,y_m)^T\in\mathbb R^m,
 \qquad Y=\|y\|_2/\sqrt m.
\]

Queries range over \(x\in\sqrt d\,\mathbb S^{d-1}\), so their normalized
input \(v=x/\sqrt d\) also has norm one. Time is physical time throughout.
Both hidden activations are pointwise \(\tanh\). The conventional residual
is \(r_a=f(x_a)-y_a\); we use its negative
\(c_a=-r_a=y_a-f(x_a)\), matching the assigned optimizer equations. Set
\(\rho=\|c\|_2/\sqrt m\). The loss is \(\rho^2\), with no factor \(1/2\).

The dense system has width \(n\ge1\), parameters
\(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\), and output

\[
 h^{(1)}(x)=\tanh(Av),\qquad
 h^{(2)}(x)=\tanh(Wh^{(1)}(x)),\qquad
 f_n(x)=w^Th^{(2)}(x)/n.
\]

It follows squared-mean-loss gradient flow with mobilities \((n,1,n)\):

\[
 \begin{split}
 \delta_a^{(2)}&=\tanh'(Wh_a^{(1)})\odot w,
 &\delta_a^{(1)}&=\tanh'(Av_a)\odot W^T\delta_a^{(2)},\\
 \dot A&={2\over m}\sum_a c_a\delta_a^{(1)}v_a^T,
 &\dot W&={2\over mn}\sum_a c_a\delta_a^{(2)}h_a^{(1)T},\\
 \dot w&={2\over m}\sum_a c_a h_a^{(2)}.
 \end{split}                                                    \tag{1}
\]

Zero initialization of \(w\) is allowed and is the application of interest;
the tail certificate is valid at any later state, without a Gaussian
assumption or a small-label assumption.

The compact system has fixed widths \(N_1,N_2\ge1\), fixed symmetric positive
definite matrices \(H_1,H_2\), and raw moving state

\[
 A\in\mathbb R^{N_1\times d},\quad
 B\in\mathbb R^{N_2\times N_1},\quad
 w\in\mathbb R^{N_2},\quad c\in\mathbb R^m.
\]

For this system only, write
\(\langle u,z\rangle_{H_i}=u^TH_i z\) and
\(\|u\|_{H_i}=(u^TH_i u)^{1/2}\). Its forward features and normalized
training matrices are

\[
 \begin{split}
 h^{(1)}(x)&=\tanh(Av),& h^{(2)}(x)&=\tanh(Bh^{(1)}(x)),\\
 F&=[h^{(2)}(x_1),\ldots,h^{(2)}(x_m)],&
 V&=F/\sqrt m,\quad Q=F^TH_2F,\quad q=Q/m=V^TH_2V.
 \end{split}                                                    \tag{2}
\]

On the open set \(q\succ0\), define the *effective* readout by

\[
 \widehat w=w+FQ^{-1}(y-c-F^TH_2w),\qquad
 f_C(x)=\widehat w^TH_2h^{(2)}(x).                                \tag{3}
\]

Multiplication by \(F^TH_2\) gives \(F^TH_2\widehat w=y-c\). Thus the
stored \(c\) is exactly this model's own negative residual, including when
the raw readout \(w\) differs from \(\widehat w\).

Its training signals, surrogate Gram, and autonomous dynamics are

\[
 \begin{split}
 B^*&=H_1^{-1}B^TH_2,\\
 \delta_a^{(2)}&=\tanh'(Bh_a^{(1)})\odot\widehat w,\\
 \delta_a^{(1)}&=\tanh'(Av_a)\odot B^*\delta_a^{(2)},\\
 K_{ab}&=\langle h_a^{(2)},h_b^{(2)}\rangle_{H_2}
  +\langle\delta_a^{(2)},\delta_b^{(2)}\rangle_{H_2}
       \langle h_a^{(1)},h_b^{(1)}\rangle_{H_1}
  +\langle\delta_a^{(1)},\delta_b^{(1)}\rangle_{H_1}v_a^Tv_b,\\
 \dot A&={2\over m}\sum_a c_a\delta_a^{(1)}v_a^T,\qquad
 \dot B={2\over m}\sum_a c_a\delta_a^{(2)}h_a^{(1)T}H_1,\\
 \dot w&={2\over m}\sum_a c_a h_a^{(2)},\qquad
 \dot c=-{2\over m}Kc.
 \end{split}                                                    \tag{4}
\]

These are the assigned corrected compact equations, with both hidden
matrices trained. They are not asserted to be the gradient flow of (3).
In particular, replacing \(\widehat w\) by the raw \(w\) in (4) would define
a different system. The intended initialization is \(w(0)=0,c(0)=y\),
which makes \(\widehat w(0)=0\) whenever \(q(0)\succ0\).

There is an exact dense embedding, only on intervals of positive \(q\).
Set \(N_1=N_2=n\), \(H_1=H_2=I/n\), \(B=W\), and impose
\(e=y-c-F^Tw/n=0\). Then (3) gives \(\widehat w=w\), and (4)'s raw
velocities are exactly (1). On this constraint its Gram is the dense
tangent Gram, so
\[
 \dot e=-\dot c-\frac{d}{dt}(F^Tw/n)
        =2Kc/m-2Kc/m=0.
\]
Equivalently, augment any dense solution by its actual
\(c=y-F^Tw/n\); the augmented curve satisfies every equation of (4) while
\(q\succ0\). Uniqueness of the compact vector field preserves this
constraint for an initial state on it. This identity does not require a
dense computation to form \(Q^{-1}\): the dense equations, energy
identity, and certificate are evaluated directly from (1) and \(Q=F^TF/n\).

## 2. Explicit tests at a finite time

Suppose the appropriate system is defined through a finite time \(T\).
For the compact system, \(H_1,H_2\succ0\) and \(q(t)\succ0\) are required
through \(T\). No continuation beyond \(T\) is assumed.

The following unified notation is used only to state the constants. In the
dense case put \(N_1=N_2=n\), \(H_1=H_2=I_n/n\), \(B=W\), and
\(Q=F^TF/n\). Define a norm on raw parameter increments
\(\theta=(A,B,w)\) by

\[
 \|\theta\|_{\rm par}^2
 =\operatorname{tr}(A^TH_1A)
  +\|H_2^{1/2}BH_1^{-1/2}\|_F^2+w^TH_2w.                       \tag{5}
\]

For the dense system this is exactly
\(\|A\|_F^2/n+\|W\|_F^2+\|w\|_2^2/n\), and involves no corrected
readout or independently initialized residual state.

All quantities in the following display use the current raw state at \(T\)
or fixed data. Let

\[
 \begin{gathered}
 \alpha_i=\lambda_{\min}(H_i)>0,\quad
 \beta_i=\lambda_{\max}(H_i),\quad
 \gamma_i=\sqrt{\beta_i/\alpha_i},\quad b_i=\sqrt{N_i\beta_i},\\
 M_B=\|H_2^{1/2}B(T)H_1^{-1/2}\|_{\rm op}+1,\qquad
 L=\gamma_2\sqrt{b_1^2+\gamma_1^2M_B^2},\\
 \lambda_T=\lambda_{\min}(q(T))>0,\quad
 g=\lambda_T/4,\quad
 R=\min\{1,\sqrt{\lambda_T}/(2L)\},\quad
 \rho_T=\|c(T)\|_2/\sqrt m,\\
 M_w=\|w(T)\|_{H_2}+R,\qquad J=Y+\rho_T.
 \end{gathered}                                                 \tag{6}
\]

There is no division by zero in \(L\), since \(b_1>0\).
Certified positive lower bounds for \(\alpha_i,\lambda_T\) and upper
bounds for \(\beta_i\) and the norms can also be used conservatively.
In particular, replacing the transformed operator norm in \(M_B\) by
its Frobenius norm increases the derivative bound and gives another
valid certificate. In the dense specialization this requires only
\(\|W(T)\|_F\), not a width-\(n\) spectral calculation.

For dense gradient flow define

\[
 C_n={b_2+M_wL\over\sqrt g}.
                                                                    \tag{7}
\]

In this dense specialization \(b_1=b_2=\gamma_1=\gamma_2=1\),
\(M_B=\|W(T)\|_{\rm op}+1\), and
\(M_w=\|w(T)\|_2/\sqrt n+R\).

For the compact system define

\[
 \begin{split}
 D_T&=g^{-1}+2b_2^2g^{-2},\qquad
 D_P=b_2D_T+g^{-1/2},\\
 M_{\widehat w}&=M_w+J/\sqrt g,\\
 C_C&={b_2\{2+L(D_PM_w+D_TJ)\}+M_{\widehat w}L\over\sqrt g}.
 \end{split}                                                    \tag{8}
\]

Here \(D_T\) is a coefficient in a matrix derivative bound, not a time.
For a requested tolerance \(\eta>0\), the strict finite-state certificate is

\[
 H_1,H_2\succ0,\qquad \lambda_T>0,\qquad
 {\rho_T\over\sqrt g}<R,\qquad
 2C\rho_T<\eta,                                                  \tag{9}
\]

where \(C=C_n\) or \(C_C\) for the corresponding model. The dense \(H_i\)
conditions hold automatically.

**Certificate theorem.** If the first three conditions of (9) hold, the
specified system extends uniquely to every \(t\ge T\), has bounded raw
parameters, and satisfies

\[
 q(t)\succeq gI_m,\qquad
 \rho(t)\le\rho_Te^{-2g(t-T)},\qquad
 \int_t^\infty\|\dot\theta(s)\|_{\rm par}\,ds
       \le {\rho(t)\over\sqrt g}.                              \tag{10}
\]

Its raw parameters and sphere predictions converge. The limiting
predictions interpolate the training labels and satisfy

\[
 \begin{split}
 \sup_{x\in\sqrt d\mathbb S^{d-1}}
      |f(\infty,x)-f(t,x)|&\le C\rho(t),\\
 \sup_{s\in[t,\infty]}\sup_{x\in\sqrt d\mathbb S^{d-1}}
      |f(s,x)-f(t,x)|&\le2C\rho(t).
 \end{split}                                                    \tag{11}
\]

Thus the last condition of (9) certifies the requested sphere-uniform
tail, including the endpoint and every intermediate physical time. The
constants are deliberately coarse; their dependence on width or metric
conditioning is unrestricted.

## 3. Proof of the certificate

The proof first bounds all remaining raw parameter motion by the current
residual. The feature derivative bound keeps the training Gram positive
through that motion. A separate argument then controls the effective
compact readout, using the exact state relation (3).

For either system each term of \(K-Q\) is a Gram matrix: for example the
middle term in (4) is the Gram of
\(H_2^{1/2}\delta_a^{(2)}\otimes H_1^{1/2}h_a^{(1)}\).
The last term is the Gram of
\(H_1^{1/2}\delta_a^{(1)}\otimes v_a\). Hence \(K\succeq Q\).
For dense gradient flow, use (4)'s formula with \(H_i=I/n\) and with
\(\delta^{(2)}=\tanh'\odot w\); differentiating (1)'s actual training
outputs gives \(\dot c=-2Kc/m\).

For the compact system this residual equation is part of (4) and is its
actual residual equation by (3). Expanding the squared velocities in (5)
gives, in either case,

\[
 \begin{split}
 \|\dot\theta\|_{\rm par}^2
 &=\frac4{m^2}\sum_{a,b}c_ac_b
   \left[
    \langle h_a^{(2)},h_b^{(2)}\rangle_{H_2}
    +\langle\delta_a^{(2)},\delta_b^{(2)}\rangle_{H_2}
       \langle h_a^{(1)},h_b^{(1)}\rangle_{H_1}
    +\langle\delta_a^{(1)},\delta_b^{(1)}\rangle_{H_1}v_a^Tv_b
   \right]\\
 &=\frac4{m^2}c^TKc=-\frac{d}{dt}\rho^2.
 \end{split}                                                    \tag{12}
\]

For example, the transformed compact matrix velocity is
\(H_2^{1/2}\dot B H_1^{-1/2}
=(2/m)\sum_a c_a(H_2^{1/2}\delta_a^{(2)})(H_1^{1/2}h_a^{(1)})^T\),
which supplies precisely the middle cross-sample term. The identity is
about the raw \(w\), not \(\widehat w\).

Whenever \(q\succeq gI\) and \(\rho>0\), (12) gives

\[
 -\rho'\ge2g\rho,\qquad
 \|\dot\theta\|_{\rm par}^2=2\rho(-\rho')
       \le(-\rho')^2/g,\qquad
 \|\dot\theta\|_{\rm par}\le-\rho'/\sqrt g.                    \tag{13}
\]

If \(c=0\), all velocities in the relevant equations vanish, so the same
conclusions hold with zero right sides. Integration of (13) bounds path
length between any two such times \(t\le s\) by
\((\rho(t)-\rho(s))/\sqrt g\), and integration of
\(\rho'\le-2g\rho\) gives the exponential estimate.

We next justify the gap condition without assuming it after \(T\).
For a diagonal matrix \(D\) whose diagonal entries have absolute value at
most one,

\[
 \|H_i^{1/2}DH_i^{-1/2}\|_{\rm op}\le\gamma_i.
\]

Both \(|\tanh|\le1\) and \(|\tanh'|\le1\). Consequently
\(\|h^{(i)}(x)\|_{H_i}\le b_i\). On the raw-parameter unit ball around
\(\theta(T)\), the operator norm of \(B\) between the two weighted neuron
spaces is at most \(M_B\). Differentiating the hidden feature map in an
arbitrary raw-parameter direction \(\dot\theta\) gives

\[
 \begin{split}
 \|\dot h^{(1)}(x)\|_{H_1}
 &\le\gamma_1\|H_1^{1/2}\dot A\|_F,\\
 \|\dot h^{(2)}(x)\|_{H_2}
 &\le\gamma_2\left[
   b_1\|H_2^{1/2}\dot B H_1^{-1/2}\|_F
   +M_B\gamma_1\|H_1^{1/2}\dot A\|_F\right]\\
 &\le L\|\dot\theta\|_{\rm par}.
 \end{split}                                                    \tag{14}
\]

The last step is the two-term Cauchy--Schwarz inequality. Integrating
along the straight segment between two points in the unit ball gives
the same Lipschitz bound on feature differences, uniformly over the
query sphere. The operator norm of a normalized training feature
difference is bounded by its weighted Frobenius norm, which is the RMS
of the \(m\) feature differences. Hence

\[
 \|V(\theta)-V(\theta(T))\|_{\mathbb R^m\to H_2}
       \le L\|\theta-\theta(T)\|_{\rm par}.                    \tag{15}
\]

If \(\|\theta-\theta(T)\|_{\rm par}\le R\), then for every unit sample
vector \(u\),

\[
 \|V(\theta)u\|_{H_2}
 \ge\|V(\theta(T))u\|_{H_2}-LR
 \ge\sqrt{\lambda_T}/2.
\]

Thus \(q(\theta)\succeq gI\) on this entire closed ball. Before any exit
from it, (13) gives displacement at most
\(\rho_T/\sqrt g<R\). An exit at radius \(R\) is therefore impossible.

Here continuation is also justified: the vector fields are smooth on
their domains. In the compact case the fixed \(H_i\) stay positive, the
inverse of \(q\) stays bounded by \(1/g\), the raw parameters remain in a
bounded ball, and \(c\) remains bounded by (12). For fixed finite metrics
the parameter norm (5) is equivalent to the Euclidean coordinate norm.
The state therefore stays in a compact subset of the open smooth domain.
The vector field and its derivative are bounded on a slightly larger
neighborhood. A finite terminal time would make the solution Cauchy
(bounded velocity) and give a limit in that domain; the local existence
theorem, proved by contraction of the integral equation on a sufficiently
short interval, extends it past that time. This contradicts maximality.
The dense system has the same argument without an inverse-domain
restriction. Local uniqueness follows from the same contraction, or
from the difference inequality for a locally Lipschitz vector field.

This proves global continuation and the gap bound. Sending \(s\) to
infinity in the path-length inequality proves (10). Finite path length
makes \(\theta(t)\) Cauchy, so it converges. Equations (14)--(15) give
sphere-uniform feature convergence and a limiting gap at least \(g\).
Also \(\rho(t)\to0\).

For the dense system, subtract the two bilinear readouts at \(t\) and
infinity. The readout norm is bounded by \(M_w\), the feature norm by
\(b_2\), and the feature difference by \(L\) times the remaining path
length. Therefore

\[
 \sup_x|f_n(\infty,x)-f_n(t,x)|
 \le(b_2+M_wL)\int_t^\infty\|\dot\theta\|_{\rm par}
 \le C_n\rho(t).                                                \tag{16}
\]

For the compact system, regard \(V\) as an operator from ordinary
Euclidean sample space to the \(H_2\) neuron space, with adjoint
\(V^*=V^TH_2\). Define

\[
 \mathcal T=Vq^{-1},\qquad P=\mathcal T V^*,\qquad
 b=(y-c)/\sqrt m.
\]

Then \(P\) is the orthogonal projection in the \(H_2\) inner product onto
the range of \(V\), and (3) is exactly

\[
 \widehat w=(I-P)w+\mathcal T b.                               \tag{17}
\]

Indeed \(P^2=P=P^*\), since \(q=V^*V\). Also
\(\mathcal T^*\mathcal T=q^{-1}\). Along the trajectory,

\[
 \|V\|\le b_2,\quad \|\mathcal T\|\le g^{-1/2},\quad
 \|P\|\le1,\quad \|b\|_2\le J,\quad
 \|\widehat w\|_{H_2}\le M_{\widehat w}.
\]

All operator norms here use the just-specified spaces. Differentiation
of \(q=V^*V\), \(\mathcal T=Vq^{-1}\), and \(P=\mathcal TV^*\) gives

\[
 \begin{split}
 \|\dot q\|&\le2b_2\|\dot V\|,\\
 \|\dot{\mathcal T}\|
 &\le\{g^{-1}+2b_2^2g^{-2}\}\|\dot V\|=D_T\|\dot V\|,\\
 \|\dot P\|&\le(b_2D_T+g^{-1/2})\|\dot V\|=D_P\|\dot V\|,\\
 \|\dot V\|&\le L\|\dot\theta\|_{\rm par}.
 \end{split}                                                    \tag{18}
\]

In particular \(P,\mathcal T\), and \(\widehat w\) converge. Subtracting
(17) at \(t\) and infinity in the following explicit order yields

\[
 \begin{split}
 \widehat w(\infty)-\widehat w(t)
 ={}&(I-P(\infty))(w(\infty)-w(t))\\
 &+(P(t)-P(\infty))w(t)
   +(\mathcal T(\infty)-\mathcal T(t))b(t)\\
 &+\mathcal T(\infty)(b(\infty)-b(t)).
 \end{split}
\]

Here \(\|b(\infty)-b(t)\|_2=\rho(t)\), because \(c(\infty)=0\).
Using (10) and (18), without replacing \(c\) by any reference residual,
therefore gives

\[
 \|\widehat w(\infty)-\widehat w(t)\|_{H_2}
 \le {\rho(t)\over\sqrt g}
      \{2+L(D_PM_w+D_TJ)\}.                                   \tag{19}
\]

The additional term \(1\) in the brace, compared with raw-readout motion,
accounts for the actual residual state in the algebraic correction.
Subtracting \(f_C=\widehat w^TH_2h^{(2)}\) now gives (11)'s first bound
with exactly \(C_C\) in (8). Since \(\rho(s)\le\rho(t)\) for \(s\ge t\),
the triangle inequality through the endpoint gives its second bound.
Finally \(c(t)\to0\) and the respective exact output identity show that
both limiting networks interpolate the training labels. This completes
the certificate proof.

## 4. Eventual success under the paired trajectory hypotheses

**Eventual-success theorem.** Fix one of the finite systems and its fixed
positive metrics. Suppose it exists globally, its normalized training
Gram satisfies \(q(t)\succeq g_0I\) for some \(g_0>0\), its raw parameters
are bounded, and
\(\rho(t)\le C_0e^{-a_0t}\) for constants \(C_0<\infty,a_0>0\).
Then for each \(\eta>0\), (9) succeeds at every sufficiently large \(T\).
In particular it succeeds at some integer physical time.

To prove this, bounded \(B(T)\) makes \(L(T)\) uniformly bounded above.
The constants \(b_i,\gamma_i\) are fixed. Since
\(\lambda_T\ge g_0\), the radius \(R(T)\) is bounded below by a positive
constant, and \(g(T)\ge g_0/4\). Bounded raw \(w(T)\), \(R(T)\le1\), and
bounded \(\rho(T)\) make \(M_w(T),J(T)\) bounded. Formulas (7)--(8)
then make \(C(T)\) bounded above. Exponential residual decay forces both
\(\rho_T/\sqrt g<R\) and \(2C\rho_T<\eta\) eventually. In fact mere
\(\rho(T)\to0\) suffices under the other hypotheses.

This theorem can be applied separately to paired dense and compact
trajectories with these hypotheses; it does not require a uniform bound
in their widths. If a finite-horizon comparison provides
\(\sup_{t\le T,x}|f_C(t,x)-f_n(t,x)|\le\varepsilon\), and their two
certified tail excursions are at most \(\eta_C,\eta_n\), then

\[
 \sup_{t\in[0,\infty]}\sup_x|f_C(t,x)-f_n(t,x)|
 \le\varepsilon+\eta_C+\eta_n.                               \tag{20}
\]

For \(t\ge T\), this is the triangle inequality through the two values
at \(T\); for \(t\le T\), it is the assumed finite-horizon comparison.
The endpoint is covered by the certified limits.

## 5. Openness and rational perturbations of the compact initializer

The following result keeps the widths, the complete training data,
the optimizer (4), and physical time fixed. The initializer consists of
\(A_0,B_0,H_1,H_2\), with \(H_i\) symmetric; \(w_0=0,c_0=y\) are exact.
Distance between initializer tuples is any ordinary finite-dimensional
Euclidean coordinate distance, with symmetric matrices represented by
their independent entries.

Call an initializer *successful* if \(H_i\succ0\), its solution is defined
on some interval \([0,T_0]\) with \(q(t)\succ0\), and the path-length
condition \(\rho(T_0)/\sqrt{g(T_0)}<R(T_0)\) holds there. No prescribed
tail tolerance is needed in this definition.

**All-time continuity theorem.** At every successful compact initializer,
the prediction map is continuous into the norm

\[
 \|f\|_{\infty,[0,\infty]\times\sqrt d\mathbb S^{d-1}}
 =\sup_{t\in[0,\infty]}\sup_{x\in\sqrt d\mathbb S^{d-1}}|f(t,x)|,
                                                                    \tag{21}
\]

where the value at \(t=\infty\) is the limiting prediction. More precisely,
given \(\varepsilon>0\), every sufficiently close symmetric perturbation
of \(A_0,B_0,H_1,H_2\) has a globally defined, fitting corrected compact
flow, and the two outputs differ in (21) by less than \(\varepsilon\).
Consequently such perturbations can be chosen with all entries of
\(A_0,B_0,H_1,H_2\) rational. The labels and inputs remain the given data;
this statement does not rationalize them or alter their physical clock.

Here is a proof that includes the infinite-time step. Adjoin \(H_1,H_2\)
to the state with zero derivatives. The extended vector field (4) is
continuously differentiable on the open set

\[
 H_1,H_2\succ0,\qquad q(A,B,H_2)\succ0,
\]

because tanh is smooth and the only inverses are those of positive
matrices. The reconstructed output (3) is also continuously differentiable
there, uniformly in \(x\) on the compact query sphere.

On a fixed finite interval \([0,T]\), the successful reference trajectory
has compact image within this open set. Choose a closed neighborhood of
that image still contained in the open set and slightly enlarge it for
derivative bounds. Its vector field has a finite derivative bound \(L_0\).
Stop a perturbed solution before its distance from the reference exceeds
a sufficiently small fixed radius. Every segment joining their states at
the same time then lies in the enlarged neighborhood. The derivative
bound and subtraction of their integral equations give the distance bound

\[
 e(t)\le e(0)+L_0\int_0^t e(s)\,ds
       \le e(0)e^{L_0t}.
\]

The last inequality follows by setting
\(E(t)=e(0)+L_0\int_0^t e(s)ds\) and differentiating
\(e^{-L_0t}E(t)\). Taking \(e(0)\) small enough prevents a first exit
from the neighborhood and gives existence through \(T\). Bounded output
derivatives on the same neighborhood and sphere then give uniform
prediction convergence on \([0,T]\) as initial coordinates converge.
This also proves continuity of all finite-state quantities in (6)--(8)
at time \(T\): matrix norms, positive square roots, and extremal
eigenvalues are continuous on the stated finite-dimensional domains.

By the certificate at \(T_0\), the reference flow has globally bounded
raw parameters, uniform positive gap, and exponential residual decay.
The eventual-success theorem therefore lets us choose a later finite
\(T\) for which both certificate inequalities are strict and
\(2C_C(T)\rho(T)<\varepsilon/3\). Finite-time continuity and continuity
of the test quantities imply that, for all sufficiently close
initializers, their flows exist through \(T\), both test inequalities
still hold, their own certified tail excursion is less than
\(\varepsilon/3\), and their prediction difference from the reference
on \([0,T]\) is less than \(\varepsilon/3\).

Each perturbed flow is consequently global by the certificate theorem.
For every \(t\in[T,\infty]\), the two tail excursions and the difference
at \(T\) sum to less than \(\varepsilon\). The finite interval was
already controlled. This proves (21), including both endpoints.

Finally, symmetric rational matrices are dense in symmetric real
matrices, and rational rectangular matrices are dense in rectangular
real matrices. Positive definiteness is open: if \(H\succeq aI\) with
\(a>0\), any symmetric \(E\) with \(\|E\|_{\rm op}<a\) leaves
\(H+E\succ0\), by its quadratic form. Initial \(q\succ0\) is likewise
open by continuity. Choose the rational tuple within the neighborhood
just proved; it preserves every required positivity condition and the
all-time prediction error. The exact conditions \(w_0=0,c_0=y\) remain
unchanged. This proves rational approximability of the initializer.

## 6. A bounded continuous dense acceptance gate

For a law-integration or rational-search application, the dense test can
be expressed using a bounded continuous gate with no inverse and no
division by a Gram eigenvalue. Fix a requested tail excursion
\(\eta>0\). At time \(T\ge0\), define from dense terminal quantities

\[
 \begin{gathered}
 u=\|w(T)\|_2/\sqrt n,\qquad
 L_F=\sqrt{1+(\|W(T)\|_F+1)^2},\qquad
 \lambda_+=\max\{0,\lambda_{\min}(Q(T)/m)\},\\
 R_F=\min\{1,\sqrt{\lambda_+}/(2L_F)\},\\
 s_1=\sqrt{\lambda_+}R_F-2\rho_T,\qquad
 s_2=\eta\sqrt{\lambda_+}
       -4\rho_T\{1+(u+R_F)L_F\}.
 \end{gathered}                                                   \tag{22}
\]

For a real number \(z\), put \(\chi(z)=\min\{1,\max\{0,z\}\}\) and define

\[
 G_{T,\eta}=\chi((1+T)s_1)\,\chi((1+T)s_2).                        \tag{23}
\]

This is a continuous function taking values in \([0,1]\) of precisely
the two scalar parameter norms, the residual norm, and the smallest
eigenvalue of the \(m\)-by-\(m\) normalized training Gram. It is continuous
also when that eigenvalue is zero; the square root and minimum in (22)
are taken only on a nonnegative argument, and \(L_F\ge1\).

If \(G_{T,\eta}>0\), then \(s_1>0\) implies \(\lambda_+>0\).
Writing \(g=\lambda_+/4\) and \(M_w=u+R_F\), the two strict margin
conditions are exactly
\[
 \rho_T/\sqrt g<R_F,\qquad
 2\{1+M_wL_F\}\rho_T/\sqrt g<\eta.
\]
These are the dense certificate with the permitted Frobenius upper
bound. Therefore the gate is zero unless the actual dense continuation
fits globally and has certified sphere-uniform tail excursion less
than \(\eta\), including its endpoint. No claim is made that a gate
value between zero and one represents a probability.

Along any fixed finite-width dense trajectory covered by the
eventual-success theorem, \(\lambda_+\ge g_0>0\), while \(L_F,u\) stay
bounded and \(\rho_T\to0\). Thus \(\sqrt{\lambda_+}R_F\) is bounded
below by a positive constant, \(s_1\) eventually has a positive uniform
lower bound, and \(s_2\) eventually exceeds
\(\eta\sqrt{g_0}/2>0\). Consequently \(G_{T,\eta}=1\) for every
sufficiently large \(T\). The factor \(1+T\) allows this conclusion for
arbitrarily small but fixed positive Gram gaps and tolerances.
The choice \(\eta=\varepsilon/8\) is admissible without further changes.

For completeness, dense finite-time evolution itself exists globally
for every finite initialization, even before a fitting certificate.
The loss identity gives \(\rho(t)\le\rho(0)\). If
\(u(t)=\|w(t)\|_2/\sqrt n\), the equations give the integrated bounds
\[
 \begin{split}
 u(t)&\le u(0)+2\rho(0)t,\\
 \|\dot W(t)\|_F&\le2\rho(0)u(t),\\
 \|\dot A(t)\|_F/\sqrt n&\le
          2\rho(0)\|W(t)\|_{\rm op}u(t).
 \end{split}
\]
The first bound makes the integral of the second finite on every finite
interval. Their combination makes the integral of the third finite
there as well. Hence no finite-time parameter blowup is possible;
smoothness gives continuation and finite-time continuous dependence.
The gate is therefore a bounded continuous function of finite dense
initial coordinates as well as of the displayed terminal scalars.

## 7. What is computable, and what this does not establish

At a supplied current state, (6)--(9) use finite matrices, tanh evaluations,
arithmetic, square roots, norms, and extremal eigenvalues. For computable
state coordinates and computable fixed data these quantities have
arbitrarily accurate certified approximations. In particular, strict
positive definiteness and the strict inequalities in (9) are
semidecidable by refining bounds until their intervals separate. One can
avoid an exact eigenvalue calculation by using certified rational spectral
bounds and strictly positive lower margins. Equality is not claimed to be
decidable, and a failed strict comparison is not a proof that a trajectory
will fail to fit.

For a computable initializer and computable data, the finite-time state
is computable while it remains in the positive domain: on a compact
neighborhood with certified inverse bounds, the explicit smooth vector
field admits bounds for itself and its derivatives. Successive local
integral-equation approximations, with errors bounded by the contraction
estimate used above, give state enclosures of arbitrarily small radius;
finitely many such neighborhoods cover any valid compact trajectory
segment. Searching over rational neighborhoods, step lengths, and
precision finds a finite cover when one exists. Thus strict tests at
integer times can be certified by finite computations when they pass.
The eventual-success theorem ensures that this process eventually finds
a passing time for the trajectories covered by its hypotheses. This is
an existence and computability claim, with no work or precision bound.

If the fixed data are arbitrary noncomputable reals, the same statements
are exact-real or relative-oracle statements; no unconditional Turing
algorithm is claimed for such data. The same qualification applies to
access to a supplied state.

Rational density and continuity do not by themselves identify a successful
compact initializer, bound its width, bound denominators, compare it with
a dense law, or eliminate a width-\(n\) realization from a construction.
They show that *once an admissible finite successful initializer exists*,
its behavior can be approximated uniformly on the entire physical-time
axis and sphere, including infinity, by a rational initializer using the
same finite architecture and the actual corrected optimizer. Combining
this fact with a direct existence or search theorem requires that
theorem's separate information and computability arguments.
