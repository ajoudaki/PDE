# Two nearby inputs: geometry, label direction, and terminal readout size

This is a scoped, prompt-only derivation. Its scientific inputs are the model
and covariance recursion supplied in the assignment; no book, other study,
external source, or experiment was used. The result is an exact conditioning
example and a necessary norm bound, with a conditional obstruction inside an
explicit bounded parameter set. It is not a compression lower bound or a
failure theorem for unrestricted feature learning. The candidate was frozen
before exchange with other research routes.

Let the input dimension be $d\geq2$, the hidden width be $n$, and the fixed
number of hidden layers be $L\geq1$. The network has no biases and is

\[
\begin{aligned}
z_i^{(1)}&=Av_i,& h_i^{(1)}&=\phi_1(z_i^{(1)}),\\
z_i^{(\ell)}&=W^{(\ell)}h_i^{(\ell-1)},&
h_i^{(\ell)}&=\phi_\ell(z_i^{(\ell)}),\qquad 2\leq\ell\leq L,\\
f_i&=\frac{w^\top h_i^{(L)}}n.
\end{aligned}
\]

Here $A\in\mathbb R^{n\times d}$, $W^{(\ell)}\in\mathbb R^{n\times n}$,
and $w\in\mathbb R^n$; each activation acts coordinatewise. At initialization
the entries are mutually independent, with $A_{jk}\sim N(0,1)$,
$W_{jk}^{(\ell)}\sim N(0,1/n)$, and $w=0$. Assume each activation is bounded
and continuously differentiable, with

\[
K_\ell=\sup_{x\in\mathbb R}|\phi_\ell'(x)|<\infty.
\]

There are exactly two unit inputs, at angular separation $\theta\in(0,\pi)$:

\[
v_1=e_1,\qquad v_2=\cos\theta\,e_1+\sin\theta\,e_2,
\qquad y=(\alpha,-\alpha)^\top,
\]

where the amplitude $\alpha>0$ is fixed independently of $\theta$. It may
be arbitrarily small. We use the supplied limiting initialized Gram recursion

\[
Q^{(0)}_{ij}=v_i^\top v_j,\qquad
Q^{(\ell)}_{ij}
=\mathbb E[\phi_\ell(Z_i)\phi_\ell(Z_j)],
\qquad (Z_1,Z_2)\sim N(0,Q^{(\ell-1)}).
\]

This recursion defines the deterministic matrix used below. The argument does
not additionally prove a finite-width concentration or initialization-limit
theorem. No training dynamics, learning rates, or time rescaling are needed
for these geometric and algebraic claims.

By symmetry both diagonal entries of $Q^{(\ell)}$ agree. Write

\[
Q^{(\ell)}=\begin{pmatrix}q_\ell&c_\ell\\c_\ell&q_\ell\end{pmatrix},
\qquad
q_0=1,\quad c_0=\cos\theta,\quad
q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,
\]

where $Z\sim N(0,1)$. In particular $q_\ell$ is independent of $\theta$.
For the normalized Gram $G=Q^{(L)}/2$, the unit eigenvectors and eigenvalues
are

\[
u_+=\frac{(1,1)^\top}{\sqrt2},\quad
u_-=\frac{(1,-1)^\top}{\sqrt2},\qquad
\lambda_+=\frac{q_L+c_L}{2},\quad
\lambda_-=\frac{q_L-c_L}{2}.
\]

Thus $\lambda:=\lambda_{\min}(G)=\min(\lambda_+,\lambda_-)$.

The antisymmetric eigenvalue has a direct feature-distance interpretation.
Set $D_\ell=q_\ell-c_\ell\geq0$. The equality of the two Gaussian marginals
and the Lipschitz bound on the activation give

\[
\begin{aligned}
D_\ell
&=\frac12\mathbb E[\phi_\ell(Z_1)-\phi_\ell(Z_2)]^2\\
&\leq\frac{K_\ell^2}{2}\mathbb E(Z_1-Z_2)^2
=K_\ell^2D_{\ell-1}.
\end{aligned}
\]

Since $D_0=1-\cos\theta\leq\theta^2/2$, this proves

\[
0\leq\lambda\leq\lambda_-
\leq\frac{1-\cos\theta}{2}\prod_{\ell=1}^L K_\ell^2
\leq\frac{\theta^2}{4}\prod_{\ell=1}^L K_\ell^2.
\]

The sample count remains two throughout. Consequently there is no positive
lower bound on the normalized smallest eigenvalue that depends only on sample
count, depth, and these activation bounds for arbitrary distinct unit inputs.
If $q_L>0$, then $D_L\to0$, so for sufficiently small $\theta$ one has
$c_L>0$, $\lambda=\lambda_-$, and $\lambda_+\to q_L>0$.
Without $q_L>0$, the asserted nondegenerate same-sign direction need not
exist; the next specialization supplies it.

For the concrete choice $\phi_\ell=\tanh$ at every layer, $K_\ell=1$,
and every $q_\ell>0$. Indeed $q_0=1>0$, and a nondegenerate centered
Gaussian is nonzero with probability one, where its squared tanh is positive.
Also $D_\ell>0$ for $\theta>0$: if $D_{\ell-1}>0$, then
$Z_1-Z_2$ is a Gaussian of positive variance and tanh is injective, so the
squared difference in the preceding identity is positive almost surely.
The upper bound is sharp in its power of $\theta$. Define

\[
\chi_\ell=\mathbb E\operatorname{sech}^4(\sqrt{q_{\ell-1}}Z)>0.
\]

Then, as $\theta\downarrow0$, at this fixed depth,

\[
\lambda=\lambda_-
=\frac{\theta^2}{4}\prod_{\ell=1}^L\chi_\ell+o(\theta^2),
\qquad
\lambda_+=q_L-\lambda_-\longrightarrow q_L>0.
\]

To verify the coefficient without invoking a Gaussian differentiation theorem,
fix $q>0$ and $0<\delta<2q$. For independent standard normal variables
$Z,U$, put

\[
X_\delta=\sqrt{q-\delta/2}\,Z+\sqrt{\delta/2}\,U,
\qquad
Y_\delta=\sqrt{q-\delta/2}\,Z-\sqrt{\delta/2}\,U.
\]

These variables have variance $q$ and covariance $q-\delta$. For a
continuously differentiable activation with derivative bounded by $K$,

\[
\frac{\phi(X_\delta)-\phi(Y_\delta)}{\sqrt{2\delta}}
=\frac U2\int_{-1}^1
\phi'\!\left(\sqrt{q-\delta/2}\,Z+s\sqrt{\delta/2}\,U\right)ds
\longrightarrow U\phi'(\sqrt q Z).
\]

The absolute value is at most $K|U|$. Its square is therefore dominated
by the integrable variable $K^2U^2$. Dominated convergence and independence
give

\[
\frac{\mathbb E[\phi(X_\delta)-\phi(Y_\delta)]^2}{2\delta}
\longrightarrow \mathbb E\phi'(\sqrt q Z)^2.
\]

Apply this with $q=q_{\ell-1}$, $\delta=D_{\ell-1}$, and
$\phi=\tanh$. Since $D_{\ell-1}>0$ and tends to zero, it yields
$D_\ell/D_{\ell-1}\to\chi_\ell$. Multiplying the finite number of ratios
and using $D_0/\theta^2\to1/2$ proves the stated asymptotic formula.

The label direction matters even for this same input geometry. In a feature
space with Gram $Q^{(L)}$, the squared minimum normalized readout norm for
labels $y$ is $y^\top Q^{(L)-1}y$, as proved below for any finite feature
matrix. For the two choices $y_-=\alpha(1,-1)^\top$ and
$y_+=\alpha(1,1)^\top$, this gives, for sufficiently small positive $\theta$,

\[
\begin{aligned}
y_-^\top Q^{(L)-1}y_-
&=\frac{\alpha^2}{\lambda_-}
\sim\frac{4\alpha^2}{\theta^2\prod_{\ell=1}^L\chi_\ell},\\
y_+^\top Q^{(L)-1}y_+
&=\frac{\alpha^2}{\lambda_+}
\longrightarrow\frac{\alpha^2}{q_L}.
\end{aligned}
\]

Thus both examples have two inputs and the same label norm, but only the
opposite-sign labels align with the collapsing eigenvalue. These are
statements about the specified initialized limiting feature Gram. If one
also has finite-width Gram convergence, the inverse formulas pass to that
limit at each fixed positive $\theta$ with a positive definite limit.
No joint $n\to\infty$, $\theta\to0$ rate is asserted here.

For the exact terminal statement, let $T$ denote any time or final parameter
state, with arbitrary learned hidden weights. Set

\[
H_T=[h_1^{(L)}(T)\ \ h_2^{(L)}(T)]\in\mathbb R^{n\times2},\qquad
Q_T=\frac{H_T^\top H_T}{n},\qquad G_T=\frac{Q_T}{2},\qquad
\|w\|_n=\frac{\|w\|_2}{\sqrt n}.
\]

For any proposed output vector $b\in\mathbb R^2$, exact realization
$H_T^\top w/n=b$ is possible if and only if
$b\in\operatorname{range}(Q_T)$. When feasible,

\[
\min_{H_T^\top w/n=b}\|w\|_n^2
=b^\top Q_T^+b
=\frac12b^\top G_T^+b,
\]

where $+$ is the Moore--Penrose pseudoinverse. To prove this, first note that

\[
\ker(Q_T)=\ker(H_T),
\]

because $x^\top Q_Tx=\|H_Tx\|_2^2/n$. Taking orthogonal complements gives
$\operatorname{range}(Q_T)=\operatorname{range}(H_T^\top)$, which is exactly
the feasibility condition. If feasible, $w_*=H_TQ_T^+b$ satisfies
$H_T^\top w_*/n=Q_TQ_T^+b=b$. Every other solution is $w_*+u$, with
$H_T^\top u=0$; since $w_*$ lies in the range of $H_T$, these summands are
orthogonal. Therefore $w_*$ minimizes the norm, and

\[
\frac{\|w_*\|_2^2}{n}
=b^\top Q_T^+Q_TQ_T^+b
=b^\top Q_T^+b.
\]

Finally $G_T=Q_T/2$ gives $G_T^+=2Q_T^+$. If feasibility fails, the
pseudoinverse expression alone must not be presented as an attainable
interpolation cost.

In particular, every exact terminal fit to the opposite-sign labels obeys

\[
\|w_T\|_n^2\geq y_-^\top Q_T^+y_-.
\]

Even without equal diagonal entries at time $T$, Cauchy--Schwarz in the
identity

\[
2\alpha=f_1(T)-f_2(T)
=\frac{w_T^\top[h_1^{(L)}(T)-h_2^{(L)}(T)]}{n}
\]

gives the useful directional consequence

\[
\|w_T\|_n
\geq\frac{2\alpha}{\|h_1^{(L)}(T)-h_2^{(L)}(T)\|_2/\sqrt n},
\qquad
\|w_T\|_n^2\geq\frac{\alpha^2}{u_-^\top G_Tu_-}.
\]

The denominators vanish exactly when the two terminal feature vectors
coincide, which makes the opposite-sign fit impossible. If instead
$\max_i|f_i(T)-y_{-,i}|\leq\varepsilon<\alpha$, the same argument gives the
first bound with $\alpha$ replaced by $\alpha-\varepsilon$. Neither
terminal bound permits replacing $Q_T$ by the initialized $Q^{(L)}$
without an additional proved feature-stability estimate.

A bounded parameter set supplies one explicit conditional obstruction.
Suppose at the state under consideration that

\[
\|w_T\|_n\leq R,\qquad
\frac{\|A(T)\|_{\rm op}}{\sqrt n}\leq M_1,\qquad
\|W^{(\ell)}(T)\|_{\rm op}\leq M_\ell\quad(2\leq\ell\leq L),
\]

for finite nonnegative constants independent of $\theta$. Repeatedly applying
the activation Lipschitz bounds in the forward pass gives

\[
\frac{\|h_1^{(L)}(T)-h_2^{(L)}(T)\|_2}{\sqrt n}
\leq B\|v_1-v_2\|_2,
\qquad
B=M_1\left(\prod_{\ell=1}^LK_\ell\right)
\left(\prod_{\ell=2}^LM_\ell\right).
\]

The empty product for $L=1$ is one. Since
$\|v_1-v_2\|_2=2\sin(\theta/2)$, every such network satisfies

\[
|f_1(T)-f_2(T)|\leq2RB\sin(\theta/2).
\]

Exact fitting therefore requires
$\alpha\leq RB\sin(\theta/2)$; fitting within the preceding uniform error
$\varepsilon$ requires
$\alpha-\varepsilon\leq RB\sin(\theta/2)$. For example, a tube around a fixed
initialization defined by

\[
\frac{\|A(T)-A(0)\|_{\rm op}}{\sqrt n}\leq\rho_1,
\qquad
\|W^{(\ell)}(T)-W^{(\ell)}(0)\|_{\rm op}\leq\rho_\ell
\]

implies the displayed bounds with
$M_1=\|A(0)\|_{\rm op}/\sqrt n+\rho_1$ and
$M_\ell=\|W^{(\ell)}(0)\|_{\rm op}+\rho_\ell$, provided the readout bound
also holds. This is a deterministic statement at each fixed realization and
width; no random-matrix estimate is being imported. It says that sufficiently
close opposite-sign data cannot be fitted inside that uniformly bounded set.
It does not show that a training trajectory stays in the set, or prevent it
from learning larger feature separation or a larger readout outside the set.

The conclusions are consequently limited but decisive: sample count alone
cannot control initialized Gram conditioning; the labels' alignment with its
eigenvectors changes the required fixed-feature readout size; and actual
terminal readout bounds are determined by actual terminal features. No claim
is made about required compression dimension, unrestricted fitting failure,
population error, or the behavior of a specified optimizer. This mathematical
candidate has been checked by its author at the level of the displayed
identities and limiting argument; independent review and comparison with the
maintained scientific sources remain the supervisor's responsibility.
