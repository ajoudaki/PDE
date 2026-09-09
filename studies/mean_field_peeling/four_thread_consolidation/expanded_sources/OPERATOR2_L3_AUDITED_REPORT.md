# Rigorous audit of the proposed three-hidden-layer joint mean-field/gradient-flow theorem

## 1. Verdict

The proposed unconditional joint theorem is **not proved by the proposed
argument**.  The exact finite-width equations, every fixed-finite-step
infinite-width operator DAG, and the explicit small-time nondegeneracy
coefficients are derivable and are proved below.  What is missing is a
width-uniform estimate that identifies the actual finite-width dynamics over
a number of steps diverging faster than the width.  The fixed-program Tensor
Program theorem does not provide that estimate, and the attempted all-source
estimate in the earlier draft is false as stated.

This is not a proof that the joint limit is false, nor a claim about the
entire literature.  It proves only that the displayed argument does not
establish the theorem.  Section 6 states a precise sufficient bridge not
proved here.  Until that bridge or an alternative is proved, a complete
proof cannot honestly be extracted from these ingredients.

## 2. Exact model and balanced scaling

Fix \(p,d<\infty\), pairwise distinct vectors
\(x_a\in\mathbb R^d\) with \(\|x_a\|^2=d\), and labels
\(y_a\in\{-1,1\}\).  For width \(n\), let

\[
\begin{aligned}
 U_i^a&=w_i^Tx_a,&H_{1,i}^a&=\phi(U_i^a),\\
 S_{2,j}^a&=\sum_iB_{2,ji}H_{1,i}^a,&H_{2,j}^a&=\phi(S_{2,j}^a),\\
 S_{3,k}^a&=\sum_jB_{3,kj}H_{2,j}^a,&H_{3,k}^a&=\phi(S_{3,k}^a),\\
 f_{n,a}&=\sum_kc_kH_{3,k}^a,&
 L_n&={1\over p}\sum_a(f_{n,a}-y_a)^2,
\end{aligned}                                               \tag{2.1}
\]

with the fixed non-affine analytic activation

\[
                         \phi(z)=\sin z+\cos z.             \tag{2.2}
\]

Initialize independently

\[
 w_i(0)\sim N(0,I_d/d),\quad
 B_{2,ji}(0),B_{3,kj}(0)\sim N(0,1/n),\quad
 c_k(0)\sim N(0,n^{-4}).                                   \tag{2.3}
\]

Use the layer multipliers

\[
 \lambda_{w,n}=n/d,\qquad
 \lambda_{B_2,n}=\lambda_{B_3,n}=1,\qquad
 \lambda_{c,n}=1/n.                                       \tag{2.4}
\]

The task explicitly requires
\(\eta_{0,n}\lambda_{w,n}\to0\).  Since \(d\) is fixed and
\(\lambda_{w,n}=n/d\), every admissible base mesh therefore satisfies
\(n\eta_{0,n}\to0\).  Thus a fixed macroscopic interval contains

\[
 N_n\asymp {1\over\eta_{0,n}},\qquad {N_n\over n}\to\infty. \tag{2.5}
\]

This elementary observation is the source of the growing-program issue.

Put \(C=nc\), \(\langle u,v\rangle_n=n^{-1}u^Tv\),
\(u\otimes_nv=n^{-1}uv^T\), \(G_{ab}=d^{-1}x_a^Tx_b\), and
\(\gamma=2/p\).  Define

\[
\begin{aligned}
 e_a&=f_a-y_a,&D_3^a&=C\odot\phi'(S_3^a),\\
 P_2^a&=B_3^TD_3^a,&D_2^a&=\phi'(S_2^a)\odot P_2^a,\\
 P_1^a&=B_2^TD_2^a.&
\end{aligned}                                               \tag{2.6}
\]

Direct differentiation, including every factor of \(n\), gives the exact
normalized finite-width gradient flow

\[
\boxed{
\begin{aligned}
 \dot w_i&=-{\gamma\over d}\sum_a e_a\phi'(U_i^a)P_{1,i}^a x_a,\\
 \dot B_2&=-\gamma\sum_a e_aD_2^a\otimes_nH_1^a,\\
 \dot B_3&=-\gamma\sum_a e_aD_3^a\otimes_nH_2^a,\\
 \dot C&=-\gamma\sum_a e_aH_3^a.
\end{aligned}}                                               \tag{2.7}
\]

Exact simultaneous GD in these normalized variables is forward Euler for
(2.7) with step \(\eta_{0,n}\).  In particular

\[
 \dot U_i^a=-\gamma\sum_b e_bG_{ab}\phi'(U_i^b)P_{1,i}^b. \tag{2.8}
\]

The four exact scaled NTK blocks are

\[
\begin{aligned}
 \Theta^{(1)}_{ab}
 &=G_{ab}\langle\phi'(U^a)P_1^a,\phi'(U^b)P_1^b\rangle_n,\\
 \Theta^{(2)}_{ab}
 &=\langle H_1^a,H_1^b\rangle_n\langle D_2^a,D_2^b\rangle_n,\\
 \Theta^{(3)}_{ab}
 &=\langle H_2^a,H_2^b\rangle_n\langle D_3^a,D_3^b\rangle_n,\\
 \Theta^{(4)}_{ab}&=\langle H_3^a,H_3^b\rangle_n.          \tag{2.9}
\end{aligned}
\]

Thus, with \(\Theta=\sum_{r=1}^4\Theta^{(r)}\),

\[
 \dot f=-\gamma\Theta e,\qquad
 \dot L=-\gamma^2e^T\Theta e\le0.                         \tag{2.10}
\]

Equations (2.7)--(2.10) are exact finite-width identities.

## 3. What the external Tensor Program theorem actually proves

The only imported result used here is Theorem G.4, with Setup G.2,
Definition G.3 and Assumption L.4, of Yang and Hu, *Tensor Programs IV:
Feature Learning in Infinite-Width Neural Networks* (2021), supplement,
pp. 12--21.  The following paragraph states every hypothesis used from that
result.  No rank-stability hypothesis is being imported: the supplement
mentions rank stability only for alternative versions with less regular
nonlinearities, whereas Theorem G.4 itself uses Assumption L.4.

In the form relevant here, it says the following.  Start with finitely many
mutually independent matrices whose entries are iid
\(N(0,\sigma_A^2/n)\); initial vector families whose coordinate tuples are
iid copies of one fixed jointly Gaussian vector; and initial scalars
converging almost surely to deterministic limits.  A Tensor Program is a
**fixed finite** sequence of matrix or transpose-matrix multiplications,
coordinatewise maps, and normalized empirical moments.  Assumption L.4 is:
(i) a Moment map with no vector argument is continuous in its scalar
arguments; and (ii) every Nonlin or Moment map with at least one vector
argument is pseudo-Lipschitz jointly in its vector and scalar arguments.
Under precisely those assumptions, every program scalar converges almost
surely to its recursively defined deterministic value, and for every fixed
finite vector tuple and pseudo-Lipschitz \(q\),

\[
 {1\over n}\sum_iq(V_{1,i},\ldots,V_{m,i})
 \longrightarrow\mathbb E q(Z_{V_1},\ldots,Z_{V_m}).       \tag{3.1}
\]

For reuse of a matrix and its transpose the recursion is not an independence
rule.  If \(A_{ij}\sim N(0,\sigma_A^2/n)\) and \(AX\) is computed after
transpose products \(A^TY_r\), then

\[
 Z_{AX}=\widehat Z_{AX}+\sigma_A^2
 \sum_rZ_{Y_r}\mathbb E{\partial Z_X\over
                              \partial\widehat Z_{A^TY_r}}. \tag{3.2}
\]

The hatted forward variables are jointly Gaussian with covariance
\(\sigma_A^2\mathbb E[Z_XZ_{X'}]\); transpose hatted variables have the
analogous covariance and form an independent Gaussian family.  The partial
derivative is syntactic, in the actual program expression, with already
computed moment scalars held fixed.  For singular source covariance, Remark
L.2 defines the derivative expectation by a covariance pseudoinverse and
Stein's identity; Theorem G.4 explicitly remains valid with that definition.
Here all syntactic maps are smooth, but the pseudoinverse definition removes
any need to assume nonsingularity of a source Gram.

Every fixed number of Euler steps of (2.7) is such a program: write

\[
 B_{\ell,k}=A_\ell-\gamma\sum_{r<k}\delta_r
 \sum_b e_{r,b}D_{\ell,r}^b\otimes_nH_{\ell-1,r}^b,
 \qquad A_\ell=B_\ell(0),                                  \tag{3.3}
\]

so every current multiplication reduces to \(A_\ell,A_\ell^T\), coordinate
maps and moments.  The initialization hypotheses hold: \((U_i^a)_a\) are
iid \(N(0,G)\) tuples; \(A_2,A_3\) are mutually independent with iid
\(N(0,1/n)\) entries and are independent of the initial vectors; and
\(C(0)=n^{-1}Z_C\), where \(Z_C\) is an iid standard-Gaussian initial
vector and the deterministic scalar \(n^{-1}\) tends to zero.  Every
coordinate map in a fixed unrolling is obtained from products and bounded
trigonometric functions, hence is pseudo-Lipschitz.  Every empirical moment
uses such a map.  The scalar-only maps are arithmetic operations and the
squared-loss derivative, hence are continuous.  Thus both clauses of
Assumption L.4 are verified.  In particular, the rank-stability condition
from a different version of the Master Theorem is neither assumed nor
needed here.

For completeness, let \(X_{\ell,k}^a=H_{\ell-1,k}^a\) and
\(Y_{\ell,k}^a=D_{\ell,k}^a\).  The exact fixed-mesh operator DAG has
Gaussian innovations \(\xi_{\ell,k}^a,\zeta_{\ell,k}^a\) with

\[
 \mathbb E\xi_{\ell,k}^a\xi_{\ell,r}^b
 =\mathbb EX_{\ell,k}^aX_{\ell,r}^b,\qquad
 \mathbb E\zeta_{\ell,k}^a\zeta_{\ell,r}^b
 =\mathbb EY_{\ell,k}^aY_{\ell,r}^b,                       \tag{3.4}
\]

and independent forward/transpose innovation families.  With the program
serialized in forward-then-backward order, put

\[
 \alpha_{\ell;ka,rb}=\mathbb E{\partial X_{\ell,k}^a\over
                  \partial\zeta_{\ell,r}^b}\quad(r<k),
 \qquad
 \beta_{\ell;ka,rb}=\mathbb E{\partial Y_{\ell,k}^a\over
                  \partial\xi_{\ell,r}^b}\quad(r\le k).   \tag{3.5}
\]

Then

\[
\begin{aligned}
 S_{\ell,k}^a
 &=\xi_{\ell,k}^a+
   \sum_{r<k,b}\alpha_{\ell;ka,rb}Y_{\ell,r}^b
   -\gamma\sum_{r<k,b}\delta_re_{r,b}Y_{\ell,r}^b
      \mathbb E[X_{\ell,r}^bX_{\ell,k}^a],\\
 P_{\ell-1,k}^a
 &=\zeta_{\ell,k}^a+
   \sum_{r\le k,b}\beta_{\ell;ka,rb}X_{\ell,r}^b
   -\gamma\sum_{r<k,b}\delta_re_{r,b}X_{\ell,r}^b
      \mathbb E[Y_{\ell,r}^bY_{\ell,k}^a].                \tag{3.6}
\end{aligned}
\]

The current-time coefficients are triangular:

\[
\begin{aligned}
 \beta_{3;ka,kb}&=\delta_{ab}\mathbb E[C_k\phi''(S_{3,k}^a)],\\
 \beta_{2;ka,kb}&=\delta_{ab}\mathbb E[
    \phi''(S_{2,k}^a)P_{2,k}^a+
    \phi'(S_{2,k}^a)^2\beta_{3;ka,ka}].                    \tag{3.7}
\end{aligned}
\]

Thus the fixed-mesh width limit, including all reused-adjoint responses, is
rigorously identified.  The cited theorem proves nothing about a program
whose number of lines grows with \(n\), and it contains no continuous-time
or width-uniform mesh estimate.  In fact the paper explicitly describes its
training horizon as independent of width.

## 4. Why the fixed-step theorem cannot imply the requested diagonal limit

Because of (2.5), the exact GD path on a fixed interval uses
\(N_n/n\to\infty\) steps.  Pointwise convergence for every fixed number of
steps has no implication in that diagonal regime.  The logical obstruction
is witnessed by the deterministic triangular array

\[
 A_{n,\eta}=\mathbf1_{\{n\eta<1\}}.                        \tag{4.1}
\]

For each fixed \(\eta>0\), \(A_{n,\eta}\to0\), and its subsequent
\(\eta\downarrow0\) limit is zero.  For every admissible diagonal with
\(n\eta_n\to0\), however, \(A_{n,\eta_n}=1\) eventually.  Thus no diagonal
argument, even an existential one within this admissible class, follows from
the iterated limits.

The same point can be written with a step count:
\(A_{n,N}=\mathbf1_{\{N>n\}}\).  Every fixed-\(N\) limit is zero, whereas
the required path has \(N_n>n\) eventually.

This is not merely a logical nicety.  In normalized \(L^2\), differentiating
the backpropagation map produces terms such as

\[
 (B_3^TD_3)\odot\phi''(S_2)\,\delta S_2.                  \tag{4.2}
\]

Energy and operator-norm estimates control both nonconstant factors only in
empirical \(L^2\).  Multiplication \(L^2\times L^2\to L^2\) is not bounded.
Using Hölder asks for \(L^4\), then this particular stability route asks for
\(L^8\), and so on.  This exposes the all-source hierarchy that the attempted
proof did not close; it does not rule out a different proof.

### 4.1 The attempted all-source lemma is invalid

The discarded draft needed the following estimate with one constant \(K\)
independent of \(q,T\), uniformly for every \(q\ge2\), small \(T\), and
the discrete meshes used to construct the flow:

\[
 \|P_\ell(t)\|_q\le KT e^{KTq}.                            \tag{4.3}
\]

This mesh-uniform estimate is false.  Take \(p=d=1\), \(x=y=1\), and
consider exactly one Euler step of size \(h>0\).  First set \(C_0=0\)
at finite width.  Then \(e_0=-1,\gamma=2\); every hidden update vanishes
in that step, while

\[
 C_1=2hH_{3,0},\qquad
 D_{3,1}=2hH_{3,0}\phi'(S_{3,0})
         =2h\cos(2S_{3,0}).                              \tag{4.4}
\]

Consequently, with \(A_3=B_{3,0}\), the identity

\[
 P_{2,1}(h)=2hA_3^T\cos(2S_{3,0})                        \tag{4.5}
\]

is exact.  In the fixed-program width limit, \(S_{3,0}\) has the standard
normal law: all preceding activation second moments are one.
For \(Z\sim N(0,1)\), the reused-adjoint response in (3.2) is
\(\mathbb E[-2\sin(2Z)]=0\).  Therefore the limit of (4.5) is exactly
\(h\sigma\Gamma\), where \(\Gamma\sim N(0,1)\) and

\[
 \sigma^2=4\mathbb E\cos^2(2Z)=2(1+e^{-8})>0.             \tag{4.6}
\]

The actual initialization \(C_0=n^{-1}Z_C\) gives the same one-step limit
by Theorem G.4: its initial scalar \(n^{-1}\) converges to zero, and the
recursive limiting program is the one just computed.  The theorem also
passes every fixed \(q\)-th absolute moment.  If (4.3) held for these
one-step limits with \(T=h\), it would imply
\(\sigma\|\Gamma\|_q\le K e^{Khq}\).  First send \(h\downarrow0\) at a
fixed \(q\), then let \(q\to\infty\).  This contradicts
\[
 \|\Gamma\|_q=
 \left(\frac{2^{q/2}\Gamma((q+1)/2)}{\sqrt\pi}\right)^{1/q}
 \longrightarrow\infty.
\]
This countercheck uses only one fixed finite program.  It assumes neither
existence nor differentiability of a continuous width-first flow.  It
refutes the mesh-uniform bound needed by the discarded construction; it
does not by itself rule out a differently stated continuous-only estimate.

The draft's series summation also failed algebraically.  A causal component
with \(m\) time edges and at most \(2m+2\) Gaussian marks gives, at moment
order \(q\), a bound of the form

\[
 { (DT)^m\over m!}
 \bigl(C\sqrt{q(2m+2)}\bigr)^{2m+2}
 \sim {2e\over\sqrt{2\pi}}C^2q\sqrt m\,
       (2eC^2DqT)^m.                                      \tag{4.7}
\]

The factorial is canceled by the Gaussian moment growth; a second factorial
does not remain.  The series is controlled only when \(qT\) is small and
does not yield all-order exponential tails.

More fundamentally, the first-source response forest behind (3.5) freezes
moment scalars and has one differentiated spine.  Repeated finite-width
Gaussian integration by parts does not: it creates higher Malliavin orders,
Faà-di-Bruno branching, derivatives of residual and moment nodes, and
cross-graph index identifications.  A four-line local index ledger cannot
bound those global graphs.  Therefore a limiting first-response estimate
cannot be relabeled as a finite-width all-orders theorem.

Finally, the smooth saturation \(\tau_R(x)=R\tanh(x/R)\) does not satisfy
\(x-\tau_R(x)=0\) on \([-R,R]\).  A tail estimate for
\(x^2\mathbf1_{|x|>R}\) alone therefore does not bound its cutoff defect.
One needs both compact convergence, for example
\(|x-\tau_R(x)|\lesssim |x|^3/R^2\) on a central region, and a separately
proved uniformly integrable tail estimate.

These are failures of the proof, not choices of constants that can be fixed
locally.

## 5. What can nevertheless be proved: the explicit L=3 initial geometry

The Gaussian identities and positivity statements in this section are
unconditional.  Equations (5.9)--(5.10) are the coefficients obtained by
algebraically differentiating the width-first fixed-step DAG and then
letting its mesh tend to zero; they are **candidate** continuous-time jets,
not an assertion that the actual joint finite-width trajectory converges.
They show that initial nondegeneracy is not the obstruction in the proposed
route.  In this section \(O(t^3)\) is purely formal notation for equality of
the algebraically generated coefficients through degree two; it asserts no
analytic remainder bound and no joint limiting trajectory.

For standard jointly Gaussian \((X,Y)\) of correlation \(\rho\),

\[
 \mathbb E[\phi(X)\phi(Y)]
 =\mathbb E[\phi'(X)\phi'(Y)]=e^{\rho-1}.                  \tag{5.1}
\]

Let \(Z_1\sim N(0,G)\) and define

\[
 Q_1=e^{\circ(G-\mathbf1)},\quad Z_2\sim N(0,Q_1),\quad
 Q_2=e^{\circ(Q_1-\mathbf1)},\quad Z_3\sim N(0,Q_2),\quad
 Q_3=e^{\circ(Q_2-\mathbf1)}.                              \tag{5.2}
\]

Here \(\mathbf1\) is the all-ones matrix and exponentiation is entrywise.
These are exactly the three initial
preactivation laws and activation Gram matrices.

Each \(Q_r\) is positive definite.  For \(Q_1\), expand
\(e^{x_a^Tx_b/d}\) into tensor powers.  If coefficients \(v_a\) annihilate
the resulting Gram matrix, then \(\sum_av_aP(x_a)=0\) for every polynomial
\(P\).  For each \(j\), the polynomial

\[
 P_j(x)=\prod_{k\ne j}{(x-x_k)^T(x_j-x_k)\over\|x_j-x_k\|^2}
\]

is one at \(x_j\) and zero at the other data, so \(v_j=0\).  Apply the same
argument to Gram realizations of \(Q_1\) and \(Q_2\) to obtain
\(Q_2,Q_3\succ0\).

Set \(a=\gamma y\), \(H_r=\phi(Z_r)\), and

\[
\begin{aligned}
 C_1&=\sum_\alpha a_\alpha H_3^\alpha,\\
 A_3^\mu&=C_1\phi'(Z_3^\mu),
 &R_3^{\mu\nu}&=\mathbb E[A_3^\mu A_3^\nu],\\
 J_3^{\mu\alpha}
 &=a_\alpha Q_3^{\mu\alpha}
   -\delta_{\mu\alpha}(Q_3a)_\mu.                         \tag{5.3}
\end{aligned}
\]

Let \(\Xi_3\sim N(0,R_3)\), independently of \(Z_2\), and define

\[
\begin{aligned}
 L_2^\mu&=\Xi_3^\mu+\sum_\alpha J_3^{\mu\alpha}H_2^\alpha,\\
 A_2^\mu&=\phi'(Z_2^\mu)L_2^\mu,
 &R_2^{\mu\nu}&=\mathbb E[A_2^\mu A_2^\nu],\\
 J_2^{\mu\alpha}
 &=J_3^{\mu\alpha}Q_2^{\mu\alpha}
   -\delta_{\mu\alpha}\sum_\beta
      J_3^{\mu\beta}Q_2^{\mu\beta}.                      \tag{5.4}
\end{aligned}
\]

Finally let \(\Xi_2\sim N(0,R_2)\), independently of \(Z_1\), and put

\[
 L_1^\mu=\Xi_2^\mu+\sum_\alpha J_2^{\mu\alpha}H_1^\alpha,
 \quad A_1^\mu=\phi'(Z_1^\mu)L_1^\mu,
 \quad R_1^{\mu\nu}=\mathbb E[A_1^\mu A_1^\nu].           \tag{5.5}
\]

These are direct applications of the reused-adjoint formula (3.2).  For
example, since \(\phi''=-\phi\),

\[
 \mathbb E{\partial A_3^\mu\over\partial Z_3^\alpha}
 =a_\alpha Q_3^{\mu\alpha}
  -\delta_{\mu\alpha}(Q_3a)_\mu=J_3^{\mu\alpha};          \tag{5.6}
\]

differentiating the next node gives \(J_2\).

The three \(R_r\) are positive definite.  For \(v\ne0\),

\[
 v^TR_3v=
 \mathbb E\!\left[((a^T\phi(Z_3))(v^T\phi'(Z_3)))^2\right]>0. \tag{5.7}
\]

Indeed \(Q_2\succ0\) gives a full-support Gaussian density, and each factor
is a nonzero real-analytic function; their product cannot vanish almost
everywhere.  For completeness, a nonzero real-analytic function on
\(\mathbb R^p\) has a Lebesgue-null zero set: restrict successively to
one-dimensional lines, use that a nonzero one-variable analytic function
has isolated zeros, and apply Fubini; the exceptional lines on which the
restriction is identically zero are handled inductively by a nonzero Taylor
coefficient.  A full-support nondegenerate Gaussian is absolutely
continuous, so the squared product has strictly positive expectation.
Moreover, independence of \(\Xi_3,Z_2\) gives

\[
 R_2=Q_2\circ R_3+
 \mathbb E[(\phi'(Z_2)\odot J_3\phi(Z_2))
            (\phi'(Z_2)\odot J_3\phi(Z_2))^T]\succ0,       \tag{5.8}
\]

and similarly \(R_1\succeq Q_1\circ R_2\succ0\).  Also
\(G\circ R_1\succ0\), even when \(G\) is singular: if
\(G_{ij}=u_i^Tu_j\) with \(u_i\ne0\), and
\(R_{1,ij}=v_i^Tv_j\) with the \(v_i\) linearly independent, then the
vectors \(u_i\otimes v_i\) are linearly independent.

Consequently the first nonzero hidden NTK jets are

\[
\begin{aligned}
 \Theta^{(1)}(t)&=t^2(G\circ R_1)+O(t^3),\\
 \Theta^{(2)}(t)&=t^2(Q_1\circ R_2)+O(t^3),\\
 \Theta^{(3)}(t)&=t^2(Q_2\circ R_3)+O(t^3),\\
 \Theta^{(4)}(0)&=Q_3.                                    \tag{5.9}
\end{aligned}
\]

All leading matrices are positive definite.  To account for the output
block, write \(h_y=\sum_a y_aH_3^a\), and let \(J_y\) be its derivative
with respect to the three hidden parameter blocks in their scaled Hilbert
metric.  At zero, \(C=0\), \(\dot C=\gamma h_y\), and the hidden velocity
vanishes.  Differentiating once more gives
\(\ddot\theta_{\rm hid}(0)=\gamma^2J_y^*h_y\).  Hence

\[
 {d^2\over dt^2}\|h_y(t)\|_{2}^{2}\Big|_{t=0}
 =2\gamma^2\|J_y^*h_y\|_2^2=2y^TMy,
\]

where the last equality is exactly the layerwise decomposition in
(5.9).  Thus the coefficient of \(t^2\) in
\(y^T\Theta^{(4)}(t)y\) is \(y^TMy\); the three hidden blocks contribute
the same coefficient once more.

The corresponding formal continuous DAG therefore has feature acceleration
in every layer, all four parameter blocks active, a changing kernel, and
decreasing loss at small time.  Specifically, if

\[
 M=G\circ R_1+Q_1\circ R_2+Q_2\circ R_3,
\]

then \(y^TMy>0\), while

\[
 y^T\Theta(t)y=y^TQ_3y+2t^2y^TMy+O(t^3),\qquad
 \dot L(0)=-\gamma^2y^TQ_3y<0.                            \tag{5.10}
\]

Every coefficient is an explicit Gaussian activation integral.  More
generally, if \(Z\sim N(0,Q)\), a literal finite formula for any required
moment is

\[
\begin{aligned}
 \mathbb E\prod_{j=1}^m\phi^{(r_j)}(Z_{i_j})
 &=2^{-m/2}\sum_{\epsilon\in\{-1,1\}^m}
 \cos\!\left(\sum_j\epsilon_j\theta_{r_j}\right)\\
 &\quad\times
 \exp\!\left[-{1\over2}\sum_{j,k}
       \epsilon_j\epsilon_kQ_{i_ji_k}\right],
 \qquad \theta_r=-{\pi\over4}+{r\pi\over2}.             \tag{5.11}
\end{aligned}
\]

At initialization each marginal is standard normal.  Since

\[
 \mathbb E\phi(G_0)=e^{-1/2},\quad
 \mathbb E\phi(G_0)^2=1,\quad
 \mathbb E[G_0\phi(G_0)]=e^{-1/2},
\]

its squared distance from affine functions is

\[
 \inf_{r,s}\mathbb E|\phi(G_0)-rG_0-s|^2=1-{2\over e}>0.  \tag{5.12}
\]

Thus the desired local nonlinear geometry is strictly nondegenerate.  It
does not, by itself, identify the actual joint finite-width trajectory.

## 6. A precise sufficient bridge, not established here

For each integer \(R\ge1\), choose an odd \(C^\infty\), 1-Lipschitz map
\(\chi_R\) which equals the
identity on \([-R,R]\), is constant outside \([-R-2,R+2]\), and satisfies
\(|\chi_R(x)|\le |x|\).  Such a map is obtained by integrating on the
positive half-line a smooth function taking values in \([0,1]\), equal to
one through \(R\), and equal to zero from \(R+2\) onward, followed by odd
reflection.  Replace \(P_1\) in the first-layer update and \(P_2\) in
\(D_2\) by \(\chi_R(P_1)\) and \(\chi_R(P_2)\).  Denote the resulting
finite-width vector field by \(F_{n,R}\).

The following calculation supplies finite-width stability for a fixed
cutoff and isolates what remains missing.  Write
\(Z_1=U,Z_2=S_2,Z_3=S_3\).  On the state ball

\[
 \|B_2\|_{\rm op}+\|B_3\|_{\rm op}
 +\|C\|_{2,n}+\|C\|_\infty+\max_a\sum_{\ell=1}^3
   \|Z_\ell^a\|_{2,n}\le M,                                \tag{6.1}
\]

use the distance

\[
\begin{aligned}
 d_n(\theta,\widetilde\theta)
 &=\|B_2-\widetilde B_2\|_{\rm op}
   +\|B_3-\widetilde B_3\|_{\rm op}
   +\|C-\widetilde C\|_{2,n}\\
 &\quad+\max_a\sum_{\ell=1}^3
       \|Z_\ell^a-\widetilde Z_\ell^a\|_{2,n}.              \tag{6.2}
\end{aligned}
\]

The independent coordinates are \((U,B_2,B_3,C)\); the two deeper
preactivations are algebraic functions of them.  Put

\[
 \rho_n(\theta,\widetilde\theta)
 =\|B_2-\widetilde B_2\|_{\rm op}
  +\|B_3-\widetilde B_3\|_{\rm op}
  +\|C-\widetilde C\|_{2,n}
  +\max_a\|U^a-\widetilde U^a\|_{2,n}.                   \tag{6.3}
\]

The algebraic forward relations, the operator inequality, and Lipschitzness
of \(\phi\) give, on (6.1),

\[
 \rho_n(\theta,\widetilde\theta)
 \le d_n(\theta,\widetilde\theta)
 \le C_M\rho_n(\theta,\widetilde\theta).                 \tag{6.4}
\]

The elementary identities used below are

\[
 \|u\otimes_nv\|_{\rm op}=\|u\|_{2,n}\|v\|_{2,n},\qquad
 \|\chi_R(u)-\chi_R(v)\|_{2,n}
 \le\|u-v\|_{2,n},                                        \tag{6.5}
\]

with every activation derivative bounded by \(\sqrt2\).  Successive
subtraction gives

\[
\begin{aligned}
 \|\delta H_\ell^a\|_{2,n}&\le\sqrt2\|\delta Z_\ell^a\|_{2,n},\\
 |\delta e_a|&\le C_M(\|\delta C\|_{2,n}
                         +\|\delta S_3^a\|_{2,n}),\\
 \|\delta D_3^a\|_{2,n}&\le C_M(\|\delta C\|_{2,n}
                         +\|\delta S_3^a\|_{2,n}),\\
 \|\delta P_2^a\|_{2,n}&\le C_Md_n(\theta,\widetilde\theta),\\
 \|\delta D_2^a\|_{2,n}&\le C_M\bigl(\|\delta P_2^a\|_{2,n}
                              +R\|\delta S_2^a\|_{2,n}\bigr),\\
 \|\delta P_1^a\|_{2,n}&\le C_M(1+R)d_n(\theta,\widetilde\theta).
                                                               \tag{6.6}
\end{aligned}
\]

Let \(F_{n,R}^{\rm ind}\) be the cutoff vector field written in the
independent coordinates \((U,B_2,B_3,C)\).  Substitution of (6.6) into the
four update equations gives, term by term,

\[
\begin{aligned}
 \|\delta\dot C\|_{2,n}+\|\delta\dot B_3\|_{\rm op}
 &\le C_{p,d,M}\rho_n,\\
 \|\delta\dot B_2\|_{\rm op}
   +\max_a\|\delta\dot U^a\|_{2,n}
 &\le C_{p,d,M}(1+R)\rho_n.
\end{aligned}
\]

Consequently the well-typed estimate is

\[
 \|F_{n,R}^{\rm ind}(\theta)-F_{n,R}^{\rm ind}(\widetilde\theta)\|_{\rho_n}
 \le C_{p,d,M}(1+R)\rho_n(\theta,\widetilde\theta).       \tag{6.7}
\]

There is no hidden \(L^2\times L^2\) product in (6.7): the \(U\)-equation
contains \(\chi_R(P_1)\), which is bounded by \(R+2\), and the
\(B_2\)-equation contains \(\chi_R(P_2)\), also bounded by \(R+2\).
One must not differentiate \(S_2,S_3\) as independent state coordinates;
doing that creates a spurious uncontrolled product.  Their path differences
are instead recovered at each time from (6.4).

The ball radius can be chosen independently of \(R\) on a sufficiently
short deterministic interval.  Indeed \(C\) satisfies a coordinatewise
linear differential inequality because \(H_3\) is bounded; then
\(\|D_3\|_2\) is bounded, (2.7) bounds
\(\|B_3-A_3\|_{\rm op}\), the operator inequality bounds \(\|P_2\|_2\),
\(|\chi_R(P_2)|\le|P_2|\) bounds \(\|D_2\|_2\), and (2.7) finally bounds
\(\|B_2-A_2\|_{\rm op}\).  The deeper preactivations \(S_2,S_3\) are
bounded in \(L^2\) by the operator bounds and \(|H_\ell|\le\sqrt2\).
For the first layer, (2.8), \(|G_{ab}|\le1\), and
\(\|\chi_R(P_1^b)\|_{2,n}\le\|P_1^b\|_{2,n}
\le\|B_2\|_{\rm op}\|D_2^b\|_{2,n}\) give
\[
 \|\dot U^a\|_{2,n}
 \le\gamma\sqrt2\sum_b |e_b|\,
          \|B_2\|_{\rm op}\|D_2^b\|_{2,n}.
\]
Integration bounds \(\|U^a(t)\|_{2,n}\) from its initial value, with no
dependence on \(R\).

The needed initialization event is also elementary.  A \(1/4\)-net of the
unit sphere has at most \(9^n\) points, and
\(\|A\|_{\rm op}\le2\max_{u,v}|u^TAv|\) over two such nets.  Since
\(u^TAv\sim N(0,1/n)\),

\[
 \Pr(\|A_\ell\|_{\rm op}>8)\le2\,9^{2n}e^{-8n}\to0.        \tag{6.8}
\]

Also \(\|C(0)\|_\infty=n^{-1}\max_i|Z_i|\to0\) in
probability by a Gaussian union bound, and
\(\max_a\|U^a(0)\|_{2,n}^2\to1\) in probability by the law of large
numbers for the fixed finite family of standard-Gaussian marginals.

Estimate (6.7) gives a width-independent finite-dimensional Euler estimate
\(C_{R,T}|\pi|\) in \(\rho_n\).  A restricted candidate action topology can
then be specified as follows.  Enumerate the finite typed probes generated
from the current core vectors by \(B_2,B_2^T,B_3,B_3^T\), the maps
\(\phi,\phi',\chi_R\), rational linear combinations, normalized inner
products, and coordinatewise products only when both factors have a proved
uniform \(L^\infty\) bound on (6.1).  The \(C\) coordinate is such a bounded
factor; \(U\) and arbitrary matrix images need not be.  This restriction
includes all products in the independent-coordinate cutoff update itself.
If \(\mathcal L_n(P_m)\) is the empirical coordinate law of the
tuple returned by probe \(P_m\), set

\[
 d_{\rm act}(s,s')=
 \sum_{m\ge1}2^{-m}\bigl(1\wedge
 W_2(\mathcal L(P_m),\mathcal L'(P_m))\bigr),             \tag{6.9}
\]

including scalar probes as Dirac laws.  For a fixed mesh, Theorem G.4 gives
convergence of every summand: its pseudo-Lipschitz conclusion gives weak
convergence plus convergence of second moments, hence \(W_2\) convergence;
the weighted tail then gives convergence in \(d_{\rm act}\).  Estimate
(6.7), followed by (6.4), supplies the width-uniform comparison between
meshes for each probe in this restricted algebra.  This follows by
induction on its finite construction: operator multiplication uses
\(\|Bu-\widetilde B\widetilde u\|_2\le
\|B-\widetilde B\|_{\rm op}\|u\|_2+
\|\widetilde B\|_{\rm op}\|u-\widetilde u\|_2\);
coordinate maps use their Lipschitz constants; inner products use
Cauchy--Schwarz; and products use the two \(L^\infty\) bounds.  One
bounded but varying factor would not suffice for the last step, because
\(\widetilde u(b-\widetilde b)\) need not be controlled in \(L^2\)
when \(\widetilde u\) is unbounded.  Extension to larger probe algebras,
including all uncut physical velocity expressions, requires additional
uniform integrability and continuity arguments.

What is not written out here is the completion, realization, and
restartability even of the restricted limiting probe algebra.

Thus a fixed-cutoff joint flow itself remains conditional in this report.
Even granting that construction would still not remove the cutoff from the
actual network.  The following explicit finite-width estimate would supply
the second missing bridge.

To remove the cutoff for the actual networks, it would suffice to prove the
following finite-width theorem on some \([0,T]\).  Define
\(P_{1,R}=B_2^T[\phi'(S_2)\odot\chi_R(P_2)]\), evaluated on the uncut state, and

\[
\begin{aligned}
 Z_{2,n}&=\sup_{t\le T,a}{1\over n}\sum_i
   \exp\!\left({|P_{2,i}^a(t)|^2\over K^2T^2}\right),\\
 Z_{1,n}&=\sup_{t\le T,a,\ R\in\mathbb N_{\ge1}}{1\over n}\sum_i
   \exp\!\left({|P_{1,i}^a(t)|\vee|P_{1,R,i}^a(t)|\over KT}\right).
\end{aligned}                                             \tag{6.10}
\]

The missing assertion is that there are deterministic \(K,T>0\), independent
of \(n\) and of the admissible mesh, for which

\[
 \lim_{A\to\infty}\limsup_{n\to\infty}
 \Pr(Z_{1,n}+Z_{2,n}>A)=0,                               \tag{6.11}
\]

for the actual uncut continuous flows and with the time supremum replaced by
the supremum over every exact-GD mesh under consideration.
The asymmetric classes are natural—\(P_2\) has a Gaussian innovation,
whereas \(P_1\) can contain a product of Gaussian contrasts—but are not
claimed to be logically necessary; any tail bound strong enough below
would do.

On the event \(Z_{1,n}+Z_{2,n}\le A\), (6.10) implies

\[
\begin{aligned}
 \max\{\|P_1\mathbf1_{|P_1|>R}\|_{2,n},
        \|P_{1,R}\mathbf1_{|P_{1,R}|>R}\|_{2,n}\}
 &\le C_A(R+KT)e^{-R/(2KT)},\\
 \|P_2\mathbf1_{|P_2|>R}\|_{2,n}
 &\le C_A(R+KT)e^{-R^2/(4K^2T^2)}.
\end{aligned}                                             \tag{6.12}
\]

Moreover,
\(\|P_1-P_{1,R}\|_{2,n}\le C_M
\|P_2\mathbf1_{|P_2|>R}\|_{2,n}\), and therefore the difference between
the uncut vector field and the cutoff vector field, in the independent
coordinate norm \(\rho_n\), is bounded by the tails in (6.12).  Compare the uncut path
\(\theta_n\) to the cutoff path \(\theta_n^R\) by writing
\[
 F(\theta_n)-F_R(\theta_n^R)
 =[F(\theta_n)-F_R(\theta_n)]
  +[F_R(\theta_n)-F_R(\theta_n^R)].
\]
The first bracket consists of the two cutoff defects just bounded, and
(6.7) controls the second.  Continuous or discrete Gronwall then gives, on
the same event,

\[
 \sup_{t\le T}\rho_n(\theta_n(t),\theta_n^R(t))
 \le C_A(R+KT)
 \exp\!\left(C_{p,d,M}T(1+R)-{R\over2KT}\right).          \tag{6.13}
\]

For \(T^2<1/(4C_{p,d,M}K)\), (6.13) tends to zero as
\(R\to\infty\).  Since \(A\) can then be sent to infinity, the precise
conclusion would be

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\!\left(\sup_{t\le T}
 \rho_n(\theta_n(t),\theta_n^R(t))>\varepsilon\right)=0. \tag{6.14}
\]

Estimate (6.14) would compare the core finite-width trajectories with their
cutoff versions.  To convert it into the requested full joint theorem,
one must additionally construct the fixed-cutoff law-level limits,
transfer this comparison to an \(R\)-independent closing topology, pass
all uncut velocity and kernel expressions using sufficient uniform
integrability, and prove well-posedness and restartability in that
topology.  These conclusions are not asserted to follow from (6.14)
alone, and those remaining arguments are not supplied here.

A possible combinatorial approach is to assign weight one to each \(P_2\)
mark and weight two to each \(P_1\) mark, and seek a bound on the total
weight of each connected finite-width causal component in terms of its
number of strict time edges.  Such a bound would still have to be proved
and converted into (6.11), including summation over components and a
controlled remainder.  In particular, it would need to include all higher
Malliavin orders and derivatives of empirical moment scalars, rather than
only the first-source limiting response spine.  No equivalence between
such a combinatorial statement and (6.11) is asserted here.

The tail estimate (6.11), or an alternative sufficient for (6.14), has not
been proved in the candidate argument.  Nor has the full fixed-cutoff action
completion just described been written out there.
Neither Yang--Hu's fixed-program theorem nor Chen--Yang--Zhao--Gu's 2025
feature-richness theorem supplies it: the latter also proceeds by induction
on a fixed discrete time index.

## 7. Final logical status

The following statements are proved:

1. the finite-width normalized dynamics and all NTK blocks, (2.7)--(2.10);
2. the exact infinite-width Gaussian operator DAG for every fixed finite
   number of steps, including every reused-adjoint response, (3.3)--(3.7);
3. strict positive-definiteness of the three activation Grams and of every
   first nonzero hidden NTK coefficient, together with the explicit Gaussian
   formulas (5.1)--(5.12).

The following statement is **not** proved:

> The original, unmodified exact-GD networks converge jointly, along an
> admissible \((n,\eta_{0,n})\) diagonal, to the uncut autonomous L=3 action
> flow.

Accordingly this report contains no complete rigorous proof of the requested
L=3 theorem.  Calling the result proved from the proposed argument would
require assuming the missing stability and tail estimates in Section 6,
which would be circular under
the user's proof standard.  This report neither proves nor disproves the
theorem.

## Primary sources checked

- Greg Yang and Edward J. Hu, *Tensor Programs IV: Feature Learning in
  Infinite-Width Neural Networks*, ICML 2021, especially supplement Setup
  G.2, Definition G.3, Theorem G.4, Remarks L.1--L.2 and Assumption L.4:
  https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf
- Zixiang Chen, Greg Yang, Qingyue Zhao and Quanquan Gu, *Global Convergence
  and Rich Feature Learning in L-Layer Infinite-Width Neural Networks under
  muP Parametrization*, ICML 2025.  Its proof is discrete-time and inductive
  in a fixed step index; it does not assert the width-uniform continuous-time
  bridge needed here: https://arxiv.org/pdf/2503.09565
