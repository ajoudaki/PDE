
## Gaussian-readout limits and three-input continuation boundaries

The letters A–I and their equation numbers are local to this section.

The three-input results use three hidden layers, half-summed square loss,
zero population readout, and all four trained raw blocks. The two-hidden-layer
theorem below instead uses one sample, an order-one Gaussian stored readout,
and full square loss. The final two-sample theorem uses zero population
readout and unhalved summed loss. Each probability limit fixes the activation,
data, depth and finite physical horizon before width tends to infinity.

The maintained dependencies are [special-data Section III.F](special_data_limits.md#iiif-fixed-finite-gaussian-programs-common-actions-and-strong-differentiation),
for fixed finite Gaussian programs, common spaces, adjunction and scalar
differentiation; [linear Section 9](linear_dynamics.md#9-a-gaussian-source-lemma-with-contained-norm-and-wick-proofs),
for its complete Wick argument; [linear Section 2.A](linear_dynamics.md#2a-compact-operators-and-the-complete-trace-norm-space),
for trace-class completeness; and [special-data Section II](special_data_limits.md#ii-equal-labels-with-three-hidden-layers),
for the two-sample estimates. Their hypotheses are specialized below.
No general all-moment Gaussian-program theorem is a premise. Equations are
numbered locally within each lettered part.

### A. First-order strong/weak coupling along actual affine training

Use three unit directions \(u_i=x_i/\sqrt d\), Gram
\(\Gamma_{ij}=u_i^Tu_j\), and labels \(y_i\in\{-1,1\}\).
Let the canonical first row \(w_0\) have law \(N(0,I_d)\), independently
of initialized adjacent actions \(A_0,B_0\). Their finite matrices have
independent \(N(0,1/n)\) entries. Canonical actions and actual adjoints
are those of III.F. Set
\[
 z_i^1=w\cdot u_i,\quad z_i^2=A\phi_e(z_i^1),\quad
 z_i^3=B\phi_e(z_i^2),\quad f_{e,i}=\langle C,\phi_e(z_i^3)\rangle,
 \qquad \phi_e(z)=(1-e)z+e\arctan z,
 \quad 0\le e\le1/2.
\]
The raw product norm is
\(\|\Delta w\|_2^2+\|\Delta A\|_{HS}^2+
\|\Delta B\|_{HS}^2+\|\Delta C\|_2^2\); only action increments
are Hilbert--Schmidt. The loss is \(\frac12\sum_i(f_i-y_i)^2\),
and \(C(0)=0\).

For a rank-two input Gram choose a nonzero null vector v and let E have
orthonormal columns spanning its orthogonal complement. The complete
tangent kernel is K_e=(<grad f_e,i,grad f_e,j>_raw)_(ij). It has an initially
\(O(e^2)\) strong/weak block. Along the actual evolving affine reference,
that block can have a nonzero first-order coefficient in \(e\).
The proof computes trained marginal variances, then uses Gaussian
integration by parts and the raw gradient identity. This statement does
not require a global nonlinear trajectory.

#### A.1. Setup and local regularity

At e=0 the activation is the identity. Let Theta^0(t) be the actual affine raw gradient flow, with loss (1/2)sum_i(f_i-y_i)^2. Its vector field is polynomial on the raw Hilbert state space of first-layer changes, Hilbert-Schmidt action changes, and readout. Initialized actions are bounded. Thus the ordinary local Banach-space ODE theorem applies and the affine solution is smooth, indeed locally analytic. A different fixed normalization of the empirical loss only rescales time in the calculation below.

Write A=A(0), B=B(0), z_i=z_i^1(0), and

\[
 Z=\sum_i y_i z_i,\qquad k=\Gamma y,\qquad
 M=A^*B^*BA.                                                   \tag{6}
\]

The first-layer metric gives, exactly in the affine model,

\[
 (z_i^1)'=\sum_j (y_j-f_j)\Gamma_{ij}A(t)^*B(t)^*C(t),
\]

\[
 A'=\sum_j(y_j-f_j)(B(t)^*C(t))\otimes z_j^1(t),
\quad B'=\sum_j(y_j-f_j)C(t)\otimes z_j^2(t),
\quad C'=\sum_j(y_j-f_j)z_j^3(t).                              \tag{7}
\]

Here z_j^2=A(t)z_j^1 and z_j^3=B(t)z_j^2. These are the original updates of all four blocks.

At every finite affine Euler transcript, each same-layer field is a centered
linear combination of Gaussian roots and sources. Rank-one updates introduce
deterministic contractions multiplying previously available fields. The
source rule III.F.1--III.F.6 preserves this property with both actual
transpose returns. Euler converges strongly on the local polynomial-ODE
ball by III.F.11, and finite-dimensional characteristic functions pass the
joint centered Gaussian laws to the affine flow. This uses arbitrary
deterministic sample coefficients and requires no sample symmetry.

#### A.2. The second-order trained marginal variances

Equations (7) and C(0)=0 give

\[
 C(t)=tBAZ+O(t^2),
\]

\[
 z_i^1(t)=z_i+\tfrac12t^2 k_i MZ+O(t^3),
\]

\[
 A(t)=A+\tfrac12t^2(B^*BAZ)\otimes Z+O(t^3),
\qquad
 B(t)=B+\tfrac12t^2(BAZ)\otimes(AZ)+O(t^3).                     \tag{8}
\]

The remainders are in L2 for fields and in Hilbert-Schmidt norm for action changes. Initialized contractions satisfy <Z,z_i>=<AZ,Az_i>=k_i. Composing (8), without discarding trained action terms, yields

\[
 z_i^2(t)=Az_i+\tfrac12t^2 k_i
       (AA^*B^*BA+B^*BA)Z+O(t^3),
\]

\[
 z_i^3(t)=BAz_i+\tfrac12t^2 k_i
       (BAA^*B^*BA+BB^*BA+BA)Z+O(t^3).                         \tag{9}
\]

Let q_{ell i}(t)=||z_i^ell(t)||_2^2. Then

\[
 q_{\ell i}(t)=1+d_\ell k_i^2t^2+O(t^3),
 \qquad (d_1,d_2,d_3)=(1,3,6).                               \tag{10}
\]

Here is a check of every nontrivial coefficient in (10). For a fixed initialized polynomial P independent of first-layer roots, the canonical contraction is <z_i,PZ>=k_i tau(P), where tau denotes the limiting normalized finite-matrix trace, not a trace of the infinite-dimensional action. The needed traces are

\[
 \tau(M)=1,\quad
 \tau(A^*AA^*B^*BA)=2,\quad
 \tau(M^2)=3,\quad
 \tau(A^*B^*BB^*BA)=2.                                       \tag{11}
\]

They follow directly from Gaussian fourth moments. For independent normalized square Gaussian A_n,B_n, set Q=B_n^TB_n. Then E tau(Q)=1, E tau(Q^2)=2+1/n, and

\[
 E_{A_n}\tau((A_n^TQA_n)^2)
 =(\tau Q)^2+(1+1/n)\tau(Q^2)\longrightarrow3.
\]

Conditioning on B for the last trace in (11) gives tau(Q^2), with limit 2.
Conditioning on B in the second gives tau((A_n A_n^T)^2), also with limit 2.
Linear Section 9 proves convergence of these fixed two-matrix words and
their variances. The first-row Gaussian roots are independent of both
matrices; its rooted-word argument and linearity in the finitely many
independent first-coordinate roots give the factor k_i. III.F.2 proves
uniform operator moments, hence uniform integrability of these fixed trace
words. Thus the expectation calculations identify the canonical
contractions, including singular sample Grams. The three coefficients are
respectively 1, 2+1, and 3+2+1.

#### A.3. First-order nonlinear null signal at the trained affine state

Assume Gamma has rank two and v belongs to its null space. For every raw state and every e, the exact null decomposition is

\[
 v^Tf_e=eN_{v,e},\quad
 N_{v,e}=\langle C,a^2BA T_1+aBT_2+T_3\rangle,
 \quad T_\ell=\sum_i v_i\arctan z_i^\ell,\quad a=1-e.           \tag{12}
\]

Evaluate its e=0 coefficient at Theta^0(t):

\[
 N_v(t)=\langle C(t),B(t)A(t)\sum_i v_i\arctan z_i^1(t)
       +B(t)\sum_i v_i\arctan z_i^2(t)
       +\sum_i v_i\arctan z_i^3(t)\rangle.                    \tag{13}
\]

Thus N_v(t)=partial_e[v^Tf_e(Theta^0(t))] at e=0. Derivatives of a contribute only linear terms, annihilated by v.

Put m(q)=E(1+qG^2)^(-1), where G is standard Gaussian. Then

\[
                   m'(1)=-E\frac{G^2}{(1+G^2)^2}<0.            \tag{14}
\]

For the three terms of (13) set respectively

\[
 U_1=A(t)^*B(t)^*C(t),\qquad U_2=B(t)^*C(t),\qquad U_3=C(t).
\]

Joint Gaussian integration by parts, including singular joint covariances, gives

\[
 E[U_\ell\arctan z_i^\ell]
       =m(q_{\ell i})E[U_\ell z_i^\ell].                     \tag{15}
\]

At every affine state, sum_i v_i z_i^ell=0 exactly. Therefore sum_i v_i E[U_ell z_i^ell]=0 exactly; this cancellation includes every higher-order term of these covariances. Also (8)-(11) give E[U_ell z_i^ell]=t k_i+O(t^2) for all three layers. Subtract m(1) times the exact zero sum in (15), then apply (10):

\[
  N_v(t)=10m'(1)\left(\sum_i v_i(\Gamma y)_i^3\right)t^3
                  +O(t^4).                            \tag{16}
\]

The Taylor expansion may be differentiated: affine state covariances are smooth and m is smooth near q=1, while (15) is an exact formula there. Thus N_v'(t)=30m'(1)(sum_i v_i k_i^3)t^2+O(t^3).

This is generated by the unequal trained marginal variances in (10). It disappears if one incorrectly freezes the first layer and action maps or assumes all sample variances stay equal.

#### A.4. A separated triple with fast gap one and a nonzero coefficient

Take

\[
 u_1=(1,0),\quad u_2=(0,1),\quad
 u_3=(2^{-1/2},2^{-1/2}),\qquad y=(1,1,1).
\]

Its nonzero Gram eigenvalues are 2 and 1, and it is admissible for every delta<=1-1/sqrt(2). Let q=1/sqrt(2) and use the unnormalized null vector v=(-q,-q,1). Then

\[
 k=(1+q,1+q,1+2q),\qquad
 \sum_i v_i k_i^3=(1+2q)^3-2q(1+q)^3
                =\tfrac72+5q>0.                            \tag{17}
\]

Normalization divides v and every expression linear in v by sqrt(2). Hence (16) is nonzero for this fully realizable geometry. No vanishing fast input eigenvalue is involved.

#### A.5. The complete-kernel mixed term is first order in e

At initialization C=0, all hidden gradient blocks vanish. Therefore K_e(0)=Q_3(e). The Gaussian covariance recursion for phi_e=z+e(atan z-z) gives

\[
 Q_3(e)=\Gamma+6e(m(1)-1)\Gamma+O(e^2).
\]

Consequently the initialized strong/weak block is O(e^2).

Now evaluate the complete K_e at the actual trained affine state Theta^0(t). Write v^T K^{(1)}(t) for its null-row derivative at e=0, whose existence is proved below. No differentiability of the other rows is needed. Since the affine scalar predictor v^Tf_0 is identically zero on the **entire raw state space**, its raw gradient is identically zero. Differentiating (12) and the gradient-Gram identity therefore gives, for every sample vector u,

\[
 v^TK^{(1)}(t)u
 =\langle\nabla N_v(\Theta^0(t)),\nabla(u^Tf_0)(\Theta^0(t))
                                                    \rangle_{raw}.
                                                               \tag{18}
\]

The first-order expansion does not require differentiation of an unbounded
multiplier difference quotient. The exact scalar identity (12) gives
\(\nabla(v^Tf_e)=e\nabla N_{v,e}\). Its finite branched forward computation
uses only \(\phi_e\) and arctangent, with uniformly bounded first two
derivatives. Forward fields converge in \(L^2\) as \(e\downarrow0\).
In each reverse branch subtract the incoming-field difference first,
then use III.F.9 on the remaining fixed \(L^2\) field and bounded gate.
Rank-one gradients converge by III.F.8. The scalar differentiation proof
III.F.10 therefore gives \(\nabla N_{v,e}\to\nabla N_v\) and
\(\nabla(u^Tf_e)\to\nabla(u^Tf_0)\) in the raw metric. Dividing the kernel
pairing by \(e\) proves (18), without a second state derivative of a nonlinear
\(L^2\) map.

Along the true affine GF, (18) and the scalar chain rule imply

\[
 v^TK^{(1)}(t)(y-f_0(t))=N_v'(t)
   =30m'(1)\left(\sum_i v_i k_i^3\right)t^2+O(t^3).             \tag{19}
\]

The weak component of y-f_0 does not contribute, because v^TK^{(1)}v=0, again from the identically zero affine null gradient. Thus (17)-(19) prove that the **strong/weak** coefficient E^T K^{(1)}(t)v is nonzero at all sufficiently small positive t for the displayed triple. At any such fixed t,

\[
 E^TK_e(\Theta^0(t))v=e\,b_1(t)+o(e),\qquad b_1(t)\ne0.        \tag{20}
\]

Equation (20) is a calculation on the actual all-block evolving affine reference, not an assertion that the unknown global nonlinear trajectory equals that reference. It already rules out propagating the initialized O(e^2) coupling as a reference identity. Any differentiable local family of nonlinear flows would have the same first-order coefficient: the derivative through the state is zero for the null row at e=0 because that row is identically zero as a function of state. No such family theorem is assumed for the present conclusion.

Equation (20) is consistent with a correctly scaled Schur method. It does not refute one. A Schur comparison must retain its order-e mixing and the derivative of the moving constraint.


### B. A conditional sub-exponential construction for three inputs

Use the model and half-sum raw loss of A with \(0<e\le1/2\).
Initialized action norms are at most ten by III.F, the initialized
first-row action has norm one, and the initial loss is \(3/2\).
No input separation or Gram invertibility is needed for this implication.

**Conditional theorem.** Suppose that, for every finite physical horizon
and raw displacement radius, the actual nonlinear-residual-capped flows
from canonical initialization, stopped at first exit from that radius,
have all incoming fields bounded by \(Kp\) in \(L^p\), \(p\ge2\),
with finite \(K\) independent of the cap. Then those paths converge,
together with their derivatives in the raw norm, on every compact interval
to a global strong uncut gradient flow. It is unique against every
bounded-primal strong competitor and uniquely restartable at each reached
state. The premise concerns the actual capped recursion; primal energy
alone does not supply it.

The proof gives a one-reference Osgood estimate, uses approximate energy
to prevent capped paths escaping, and removes the caps without an
exponential in their level.

#### B.1. A multiplier bound with an Osgood endpoint

Let `g=phi'`. Then

\[
 0<g\le1,\qquad
 |g(z)-g(\widetilde z)|\le e\min\{1,|z-\widetilde z|\}.
 \tag{1}
\]

Indeed, `g(z)=1-e+e/(1+z^2)`, its oscillation is at most e, and
`|g'(z)|=2e|z|/(1+z^2)^2<=e`.
For real p>=2, Holder and `min(1,|v|)^r<=|v|^2` for r>=2 give

\[
 \begin{split}
 \|q[g(z)-g(\widetilde z)]\|_2
 &\le e\|q\|_{2p}
 \|\min(1,|z-\widetilde z|)\|_{2p/(p-1)}\\
 &\le e\|q\|_{2p}\|z-\widetilde z\|_2^{1-1/p}.
 \end{split}                                                    \tag{2}
\]

In particular, if `||q||_p<=Kp` for all real p>=2, the multiplier error
is at most `2eKp ||z-ztilde||_2^(1-1/p)`. Only the displayed reference
factor q needs these moments; the competing incoming field need only
be in L2, since

\[
 qg(z)-\widetilde qg(\widetilde z)
 =g(\widetilde z)(q-\widetilde q)
 +q[g(z)-g(\widetilde z)].                                  \tag{3}
\]

This asymmetry is essential for the intended uniqueness class.

#### B.2. Complete raw-field estimate for the three-hidden-layer architecture

Consider two states on the same canonical neuron/action spaces. Write
D for their raw Hilbert distance, using the metric of A, and V=w/sqrt(d). Assume D<=1 and that, for both states,

\[
 \|\sqrt d\,V:\mathbb R^d\to H_1\|_{op},\quad
 \|A\|,\ \|B\|,\ \|C\|_2\le B_0,
 \qquad B_0\ge1.
\]

The first norm is the norm of `u -> sqrt(d) V . u`. The raw first-weight
difference bounds its operator difference, so normalized inputs have
`||Delta z_i^1||_2<=D`. Because phi is 1-Lipschitz and fixes zero,

\[
 \|h_i^\ell\|_2\le B_0^\ell,\qquad
 |r_i|\le B_0^4+1\le2B_0^4,
\]

and direct forward subtraction gives

\[
 \|\Delta z_i^1\|_2\le D,\quad
 \|\Delta z_i^2\|_2\le2B_0D,\quad
 \|\Delta z_i^3\|_2\le3B_0^2D,\quad
 |\Delta r_i|\le4B_0^3D.                                  \tag{4}
\]

For the reference state define

\[
 q_i^3=C,\quad b_i^3=g(z_i^3)C,\quad
 q_i^2=B^*b_i^3,\quad b_i^2=g(z_i^2)q_i^2,\quad
 q_i^1=A^*b_i^2,\quad b_i^1=g(z_i^1)q_i^1.
\]

Assume, for one common K>=1, all reference incoming fields satisfy

\[
 \|C\|_p,\ \|q_i^2\|_p,\ \|q_i^1\|_p\le Kp
 \quad(i=1,2,3,\ p\ge2).                                \tag{5}
\]

No such assumption is made on the competing fields. For
`alpha=1-1/p`, use (2)--(4), `e<=1`, D<=1, and B_0,K>=1.
Successive backward subtraction gives the following safe bounds:

\[
\begin{array}{c|ccccc}
\text{field}&b^3&q^2&b^2&q^1&b^1\\ \hline
\|\Delta\text{field}\|_2/(KpD^\alpha)
&7B_0^2&8B_0^3&12B_0^3&13B_0^4&15B_0^4.
\end{array}                                                \tag{6}
\]

For example the first entry is
`D+2eKp(3B_0^2D)^alpha<=7KB_0^2pD^alpha`.
For the second, use
`Delta q^2=(Delta B)^* b^3 + Btilde^* Delta b^3`, with
`||b^3||_2<=B_0`. The third then adds
`2eKp(2B_0D)^alpha<=4KB_0pD^alpha`.
The fourth uses `||b^2||_2<=B_0^2`, and the fifth adds
`2eKpD^alpha`. This proves every entry without a multiplier norm on L2.

In the unscaled first-weight notation V=w/sqrt(d), the exact raw GF field is

\[
 F_V=-d^{-1}\sum_i r_i b_i^1x_i,\quad
 F_A=-\sum_i r_i b_i^2\otimes h_i^1,\quad
 F_B=-\sum_i r_i b_i^3\otimes h_i^2,\quad
 F_C=-\sum_i r_i h_i^3.
\]

The normalization of the first block gives
`sqrt(d)||d^-1 b x_i||_2=||b||_2`.
The Hilbert--Schmidt norm of a rank-one action is the product of the
two L2 norms. Subtracting each product, (4) and (6) give respectively

\[
 \|\Delta F_V\|_{raw}\le102KB_0^8pD^\alpha,\quad
 \|\Delta F_A\|_{HS}\le90KB_0^8pD^\alpha,
\]
\[
 \|\Delta F_B\|_{HS}\le66KB_0^8pD^\alpha,\quad
 \|\Delta F_C\|_2\le30B_0^6D.
\]

For example the A block before collecting constants is at most
`3[4B_0^6 D+24KB_0^8pD^alpha+2B_0^6D]`.
For the B block it is at most
`3[4B_0^6D+14KB_0^8pD^alpha+4B_0^6D]`.
Summing the four block bounds proves

\[
  \|F(\Theta)-F(\widetilde\Theta)\|_{raw}
 \le300KB_0^8 p D^{1-1/p}\quad(p\ge2, D\le1).
                                                      \tag{7}
\]

All constants are independent of the input Gram and allow singular
Grams. No inverse of that Gram, symmetry, or labels beyond |y_i|=1
was used.

#### B.3. Osgood uniqueness and quantitative stability

Take `p=2+log(1/D)`, which is admissible for 0<D<=1. Then
`D^(-1/p)<=exp(1)`. Defining

\[
 L=300\exp(1)KB_0^8,\qquad
 \omega(D)=D\log(\exp(2)/D),
\]

(7) yields `||Delta F||<=L omega(D)`.
The function omega is continuous, increasing on [0,1], and

\[
 \int_{0+}\frac{du}{\omega(u)}=\infty.                    \tag{8}
\]

Suppose a comparison of two absolutely continuous curves yields

\[
 D(t)\le D(0)+\int_0^t\epsilon(s)\,ds
       +L\int_0^t\omega(D(s))\,ds.
\]

Let `eta=D(0)+int_0^T epsilon`. While the right side below stays below
one, comparison with the scalar equation `z'=L omega(z)`, z(0)=eta,
gives

\[
  D(t)\le\exp(2)\left(\frac{\eta}{\exp(2)}\right)^{\exp(-Lt)}.
                                                      \tag{9}
\]

For completeness, replace the first two terms in the integral inequality
by eta and define `Z(t)=eta+L int_0^t omega(D(s))ds`. Then D<=Z and
`Z'<=L omega(Z)` because omega is increasing. Separating variables gives
(9). The upper bound staying below one makes the bootstrap legitimate.
The case eta=0 follows by taking eta down to zero. Thus two true strong
flows from the same state coincide if only one has (5) and both have
bounded primal states on the interval. Inhomogeneous L(t) works as well,
with `exp(-int_0^t L(s)ds)` replacing `exp(-Lt)`.

#### B.4. Uniform sub-exponential cap tails

Choose an odd 1-Lipschitz clip tau_R with
`tau_R(q)=q` on |q|<=R, `|tau_R(q)|<=|q|`, and
`|q-tau_R(q)|<=|q|1_{|q|>R}`. It may be chosen smooth with bounded
range by tapering its derivative from one to zero.
From `||q||_p<=Kp`, Markov with `p=R/(exp(1)K)` gives, for
`R>=2exp(1)K`,

\[
 P(|q|>R)\le\exp[-R/(\exp(1)K)].
\]

Combining this with `||q||_4<=4K` and Cauchy--Schwarz proves

\[
 \|q-\tau_R(q)\|_2
 \le4K\exp[-R/(4\exp(1)K)] =:\varepsilon_R.               \tag{10}
\]

Write `a=1-e` and `g_0(z)=1/(1+z^2)`. Use the nonlinear-residual clip

\[
 D_R(z,q)=a q+e g_0(z)\tau_R(q).
\]

Its q-Lipschitz constant is at most `a+e=1`; the z-dependent
nonlinear part has the bounded clipped factor. The capped recursion is

\[
 b_{R,i}^3=D_R(z_i^3,C),\quad
 q_{R,i}^2=B^*b_{R,i}^3,\quad
 b_{R,i}^2=D_R(z_i^2,q_{R,i}^2),
\]
\[
 q_{R,i}^1=A^*b_{R,i}^2,\qquad
 b_{R,i}^1=D_R(z_i^1,q_{R,i}^1).
\]

The residuals and forward features are unmodified, and F_R substitutes
these backward fields into the raw updates. Only the nonlinear residual
is clipped; the linear term `a q` is retained exactly. The capped field need not itself be a gradient.

Suppose the capped incoming fields C,q_R^2,q_R^1 obey (5). Since
`g(z)q-D_R(z,q)=e g_0(z)[q-tau_R(q)]`, its same-input L2 cap error
is at most `e epsilon_R<=epsilon_R`. Propagating this error through
the actual bounded actions and using the q-Lipschitz constant one gives

\[
 \|b^3-b_R^3\|_2\le\varepsilon_R,\quad
 \|b^2-b_R^2\|_2\le(B_0+1)\varepsilon_R,\quad
 \|b^1-b_R^1\|_2\le3B_0^2\varepsilon_R.
\]

The three gradient-block errors are at most respectively
`18B_0^6 epsilon_R`, `12B_0^6 epsilon_R`, and
`6B_0^6 epsilon_R`. Thus

\[
 \|F_R(\Theta)-F(\Theta)\|_{raw}
 \le40B_0^6\varepsilon_R=:d_R.                            \tag{11}
\]

This uses the moments of the *capped recursion's actual incoming fields*;
it does not assume Lp bounds on the uncut incoming fields at that state.
The action-error propagation in this calculation is only in L2.

#### B.5. Approximate energy closes the primal bootstrap if the moment hypothesis is available

Along a capped path the ordinary scalar loss chain rule is valid, and
with `E_R=F_R-F`,

\[
 L'=\langle-F,F_R\rangle
 =-\|F_R\|^2+\langle E_R,F_R\rangle
 \le-\tfrac12\|F_R\|^2+\tfrac12 d_R^2.                  \tag{12}
\]

This is an inequality proved from the actual capped field. It is not an
incorrect assignment of the true gradient energy identity to that field.
For the zero population readout, L(0)=3/2, so

\[
 \int_0^T\|F_R\|^2dt\le3+T d_R^2,\qquad
 \operatorname{length}_{raw}(\Theta_R|_{[0,T]})
 \le\sqrt{T(3+Td_R^2)}.                                  \tag{13}
\]

Fix T and the prospective raw displacement radius
`R_*=2sqrt(3T)+1`. On this ball, all relevant primal norms are bounded
by `B_0=11+R_*`. If the moment bound (5) holds with a finite K depending
only on this ball and T, uniformly in the cap, then (10)--(11) make
`T d_R^2<=3` for all sufficiently large caps. Up to the first exit from
the ball, (13) then bounds displacement by `sqrt(6T)<R_*`.
No exit occurs. Local Lipschitzness of the fixed capped field supplies
continuation throughout [0,T]. The finitely many smaller cap levels are
irrelevant to the limit.

The missing premise here is therefore very specific: a moment bound for
*reachable capped paths while inside a known raw ball*, not an arbitrary
raw-ball moment theorem (which would be false in general).

#### B.6. Cap-Cauchy construction without a cap-dependent Gronwall exponential

For caps R and S, repeat the subtraction in B.2 directly on their
capped recursions. Exactly,

\[
 D_R(z,q)-D_S(\widetilde z,\widetilde q)
 =a(q-\widetilde q)+e g_0(\widetilde z)
   [\tau_R(q)-\tau_S(\widetilde q)]
 +e\tau_R(q)[g_0(z)-g_0(\widetilde z)].
\]

The multiplier estimate (2) applies to the last term because g_0
has oscillation and Lipschitz constant at most one, and the reference
factor tau_R(q_R) has Lp norm at most Kp. The first two terms have
combined q-difference coefficient at most `a+e=1`. For the clipped
argument difference,

\[
 \|\tau_R(q_R)-\tau_S(q_S)\|_2
 \le\|q_R-q_S\|_2
 +\|\tau_R(q_S)-q_S\|_2+\|q_S-\tau_S(q_S)\|_2.
\]

The last two terms are at most epsilon_R+epsilon_S by the uniform
moments of q_S. The identical backward recurrence adds only an error
`40B_0^6(epsilon_R+epsilon_S)` to (7); enlarge 300 to 400 if desired to
absorb every harmless collection. Therefore

\[
 \|F_R(\Theta_R)-F_S(\Theta_S)\|_{raw}
 \le400\exp(1)KB_0^8\omega(D)
 +40B_0^6(\varepsilon_R+\varepsilon_S).                    \tag{14}
\]

The Osgood estimate (9), with
`eta=40TB_0^6(epsilon_R+epsilon_S)`, proves uniform raw Cauchy convergence
on [0,T]. Formula (14) also makes the derivatives uniformly Cauchy.
Hence the limit is a strong C1 path. Formula (11), continuity of the
uncut scalar gradient, and the integral equation identify its derivative
with the exact uncut raw field. It obeys the exact energy identity.

For every fixed time and p, capped incoming fields converge in L2 to
the actual limiting incoming fields. Almost-sure subsequences and Fatou
pass (5) to the limit. Thus B.3 gives uniqueness against all
bounded-primal strong competitors, without requiring their tails.
Constructing on each integer horizon and using this uniqueness gives
one global path. The constructed path beyond a reached state supplies a
continuation; uniqueness applied against its reference tail bounds gives
unique restart from that reached state.

No amplitude smallness, input-Gram inverse, or affine clock is used.
The moment premise remains a reachable-state hypothesis. Finite GF/GD
identification additionally needs transfer to the finite comparison arrays
and their actual Euler and observable estimates; trained affine-regression
error is a separate assertion. None is inferred from this conditional
construction.


### C. The backward gate is not continuous in the strong Gaussian norm

For the activation of A set \(a=1-e\), \(g(z)=(1+z^2)^{-1}\), and
\(D_e(z,q)=aq+eqg(z)\). The following statements concern this scalar gate
and its norm estimates, not trained trajectories.

#### C.1. Failure of a sub-Gaussian Banach contraction

Define the Orlicz norm

\[
 \|X\|_{\psi_2}=\inf\{s>0:E\exp(X^2/s^2)\le2\}.
\]

Let G be standard Gaussian, take `q=G`, `z_0=1`, and `z_epsilon=1+epsilon G`. Then

\[
 \|z_\varepsilon-z_0\|_{\psi_2}
 =\varepsilon\|G\|_{\psi_2}\longrightarrow0,
\]

and all pairs `(z_epsilon,q)` lie in one bounded sub-Gaussian ball. Nevertheless

\[
 \liminf_{\varepsilon\downarrow0}
 \|q[g(z_\varepsilon)-g(z_0)]\|_{\psi_2}
 \ge\frac1{\sqrt2}.                                      \tag{4}
\]

**Proof.** Fix epsilon>0 and write

\[
 F_\varepsilon(x)=x\{g(1+\varepsilon x)-1/2\}.
\]

As `|x|` tends to infinity, `F_epsilon(x)/x -> -1/2`. For every `s<1/sqrt(2)`, choose `b<1/2` with `b^2/s^2>1/2`. Outside a finite interval, `|F_epsilon(x)|>=b|x|`. Therefore the Gaussian density formula gives

\[
 E\exp(F_\varepsilon(G)^2/s^2)
 \ge\frac1{\sqrt{2\pi}}\int_{|x|>M}
       \exp[(b^2/s^2-1/2)x^2]\,dx=\infty.
\]

This implies `||F_epsilon(G)||_psi2>=1/sqrt(2)` for every epsilon>0, proving (4). In contrast, `F_epsilon(G)->0` in every fixed finite Lp by dominated convergence, because its magnitude is at most `|G|`.

For the actual backward gate `D_e`, the affine terms cancel between the two input states, and (4) becomes a lower bound `e/sqrt(2)` for its output difference. Thus the defect persists for every fixed positive nonlinear amplitude.

This is not a bad neural trajectory or a counterexample to population GF. It rules out a specific proposed construction: a direct Picard contraction on `C([0,T];L^{psi2})` with the ordinary strong sub-Gaussian norm cannot treat this local gate, even before addressing reused random actions. Uniform sub-Gaussian moment bounds on paths must be distinguished from continuity of those paths in the strong sub-Gaussian norm.

#### C.2. The product estimate in the weaker Orlicz norm

Let `||X||_psi1=inf{s>0:E exp(|X|/s)<=2}`. If `||X||_psi2<=K` and `||Y||_psi2<=L`, then

\[
 E\exp(|XY|/(KL))
 \le E\exp\{(X^2/K^2+Y^2/L^2)/2\}\le2,
\]

where the first inequality is `2|ab|<=a^2+b^2` and the second is Cauchy--Schwarz. Consequently

\[
 \|q[g(z)-g(\widetilde z)]\|_{\psi_1}
 \le\|g'\|_\infty\|q\|_{\psi_2}
                      \|z-\widetilde z\|_{\psi_2}.        \tag{5}
\]

No independence is needed. This gives a legitimate norm-loss estimate. It does not close a same-space contraction: on the next multiplication, a `psi1` difference times a `psi2` coefficient naturally has exponent `2/3`, then `1/2`, and so forth. A scale-of-spaces construction would have to control this accumulating loss and the new Gaussian action queries. The displayed estimate does not supply that control from a raw-energy bound.

The issue is sharper than an unavailable formal derivative: even the finite increment in (4) fails continuity in the seemingly natural Gaussian norm. A viable Gaussian-path construction needs a weaker convergence metric with separate moment envelopes, or a carefully controlled analytic scale. The one-step estimate gives no such construction.


### D. Two limitations of signed response and Hessian energy

Write \(\phi_\theta(z)=a z+\theta\arctan z\), \(a=1-\theta\),
\(0<\theta\le1/2\). The first construction is an abstract causal Gaussian
query program. The second uses actual states of the three-layer raw affine
space of A and half-sum square loss. Neither is asserted reachable by
canonical gradient flow.

#### D.1. Smooth bounded-time queries and signed Gaussian projection still permit focusing

The following assumptions together are insufficient for exponential-moment transport:

- a fixed time interval [0,1];
- three sample-query paths with Gram exactly I at every time;
- uniformly bounded smooth query fields;
- uniform H1([0,1];L2) bounds on query paths;
- a causal smooth Gaussian observation using the exact phi_theta, with uniform subGaussian values and uniform H1([0,1];L2) norm;
- covariance-weighted/RKHS norm at most one for its signed expected Gaussian derivative;
- even a uniform H1([0,1];L2) norm of the transported response itself.

Nevertheless the transported response's psi1 norm diverges. Thus temporal H1 regularity and causality do not alone eliminate the query-span focusing.

#### Construction of the query path

Let N>=2 be even, epsilon=1/N, and let the neuron probability space be the four-dimensional unit cube with coordinates `(x,v_1,v_2,v_3)` and uniform measure. Put

\[
 \chi_j(x)=\sqrt2\cos(2\pi jx),\quad 1\le j\le N,
 \qquad b_i(v_i)=\sqrt2\sin(2\pi v_i),\quad 1\le i\le3.
\]

The chi_j are orthonormal in L2. Each b_i has mean zero and L2 norm one; the b_i are mutually orthogonal and orthogonal to every chi_j. All these functions are smooth and bounded. If Gaussian coordinates are desired, compose x and v_i with the standard Gaussian cumulative distribution function applied to four independent Gaussian roots; the same laws result, with smooth bounded functions of those roots.

Fix a smooth bump eta supported in (-1/2,1/2), with eta(0)=1 and 0<=eta<=1. Let

\[
 t_j=(j-1/2)/(2N),\qquad p_j(t)=\eta(4N(t-t_j)).
\]

The supports are disjoint and lie in (0,1/2). Define

\[
 u_1(t)=\frac{b_1+\epsilon\sum_jp_j(t)\chi_j}
 {\sqrt{1+\epsilon^2\sum_jp_j(t)^2}},
 \qquad u_2(t)=b_2,\quad u_3(t)=b_3.
 \tag{1}
\]

At every time these three queries are orthonormal. In particular their spatial correlations are zero, satisfying every pairwise absolute-separation condition with 0<delta<=1. Their L-infinity norms are at most three. The paths are smooth, start and finish at their baseline fields, and have uniformly bounded time H1 norms.

For the derivative estimate, at a point where p_j is the only active pulse, u_1 moves on the unit circle spanned by b_1 and chi_j. Direct differentiation gives

\[
 \|u_1'(t)\|_2^2
 =\frac{\epsilon^2 p_j'(t)^2}{(1+\epsilon^2p_j(t)^2)^2}
 \le\epsilon^2p_j'(t)^2.
\]

Consequently

\[
 \int_0^1\|u_1'(t)\|_2^2\,dt
 \le4\epsilon^2N^2\int\eta'(s)^2ds
 =4\int\eta'(s)^2ds.
 \tag{2}
\]

At the query times,

\[
 u_j:=u_1(t_j)=\frac{b_1+\epsilon\chi_j}{\sqrt{1+\epsilon^2}},
 \qquad
 \langle u_j,u_k\rangle
 =\frac{1+\epsilon^2\mathbf1_{j=k}}{1+\epsilon^2}.
 \tag{3}
\]

#### Gaussian source and causal observation

Let G_0,G_1,...,G_N be independent standard Gaussians. The named source vector with the covariance in (3) is

\[
 X_j=\frac{G_0+\epsilon G_j}{\sqrt{1+\epsilon^2}}.
\]

It may be embedded in the smooth Gaussian source process obtained by using the coefficients in (1). Its marginal variances are one and its mean-square H1 bound equals (2), by equality of covariance Grams.

Set alpha_j=(-1)^j. Since N is even, `sum_j alpha_j=0`. Thus

\[
 S_N=\frac{\sqrt{1+\epsilon^2}}{\epsilon\sqrt N}
           \sum_j\alpha_jX_j
     =\frac1{\sqrt N}\sum_j\alpha_jG_j
 \sim N(0,1).
 \tag{4}
\]

Let lambda be a fixed smooth function with values in [0,1], equal to zero on [0,1/2] and equal to one near t=1. Define the observation

\[
 F_N(t)=\phi_\theta(\lambda(t)S_N).
 \tag{5}
\]

This is causal: before all the queries have been collected its value is zero; when it uses their values all t_j are strictly in the past. Because `|phi_theta(z)|<=|z|` and `|phi_theta'|<=1`,

\[
 \sup_t\|F_N(t)\|_p\le C\sqrt p,
 \qquad
 E\int_0^1|F_N'(t)|^2dt\le\int_0^1|\lambda'(t)|^2dt,
 \tag{6}
\]

with constants independent of N. Its derivative in the whitened Gaussian vector `(G_1,...,G_N)` has Euclidean norm at most one, so even Gaussian-space Lipschitzness is uniform.

#### Exact signed response and focusing

Put

\[
 m_\theta(\lambda)=E\phi_\theta'(\lambda G)\in[a,1],
 \qquad \beta(t)=\lambda(t)m_\theta(\lambda(t)).
\]

The expected named-source derivative is exactly

\[
 d_j(t)=E\partial_{X_j}F_N(t)
 =\frac{\sqrt{1+\epsilon^2}}{\epsilon\sqrt N}
       \alpha_j\beta(t).
\]

Transporting it to the actual query fields gives

\[
 V_N(t)=\sum_jd_j(t)u_j
       =\frac{\beta(t)}{\sqrt N}\sum_{j=1}^N\alpha_j\chi_j.
 \tag{7}
\]

Both the covariance-weighted derivative norm and the transported L2 norm are beta(t): if Sigma is the covariance in (3), then

\[
 d(t)^T\Sigma d(t)=\beta(t)^2=\|V_N(t)\|_2^2\le1.
 \tag{8}
\]

In particular the exact inverse-free Gaussian projection bound is fully respected. Since `|g'|<=1`, differentiation of m_theta gives `|m_theta'|<=theta E|G|<=1/2`. Hence `|beta'|<=3|lambda'|/2`; (7) and orthonormality show that the transported response also has uniformly bounded H1([0,1];L2) norm.

At t=1, beta(1)>=a>=1/2. For `|x-1/2|<=1/(6N)`, each summand satisfies

\[
 \alpha_j\cos(2\pi jx)=\cos(2\pi j(x-1/2))\ge1/2.
\]

That interval has probability 1/(3N), and therefore

\[
 V_N(1)\ge\beta(1)\sqrt{N/2}
 \quad\text{on a set of probability }1/(3N).
 \tag{9}
\]

For every fixed p>2 this yields

\[
 \|V_N(1)\|_p\ge
 \frac{\beta(1)}{\sqrt2\,3^{1/p}}N^{1/2-1/p}\longrightarrow\infty.
 \tag{10}
\]

If the psi1 norm is defined by `E exp(|V|/K)<=2`, (9) gives

\[
 \|V_N(1)\|_{\psi_1}
 \ge\frac{\beta(1)\sqrt{N/2}}{\log(6N)}
 \longrightarrow\infty.
 \tag{11}
\]

There is no uniform integrability of squared magnitudes either: after the threshold in (9) exceeds any fixed cutoff, the squared tail expectation is at least beta(1)^2/6.

#### What the causal time-step factor does and does not add

The final source response only uses strictly past query slots. On mesh intervals of length h=1/(2N), write d_j=h k_j. This is a literal causal step-factor representation, but `|k_j|` has order N^(3/2). Merely displaying h_j in a source derivative is therefore not a uniform density estimate.

If instead one assumes a uniform absolute density bound `|k_j|<=K`, then the uniformly bounded query values would immediately give `|sum h_j k_j u_j|<=3KS`. That stronger assumption does exclude this construction. It is exactly the kind of response estimate that the covariance/RKHS replacement was trying to avoid proving.

The observation uses the exact admissible phi_theta, and all source coordinate maps in this finite construction are smooth with bounded derivatives at each fixed N. Nevertheless the query path was designed rather than derived from the neural GF. Equations (9)-(11) therefore disprove a source-tail theorem based solely on the listed regularity/covariance/causality hypotheses. They do not show focusing of the canonical trained neural queries. A successful replacement theorem must use additional restrictions imposed by the actual training equations.

#### D.2. The positive Hessian term does not close raw-ball response energy

For a finite smooth gradient system, or wherever a variational equation and the required second directional derivatives are justified, let `J` be the sample predictor differential and let v be a homogeneous tangent perturbation. The loss Hessian decomposes as

\[
 D^2L=J^*J+\sum_i r_iD^2f_i,
\]

and the linearized GF energy obeys

\[
 \frac12\frac{d}{dt}\|v\|_{\rm raw}^2
 =-\|Jv\|_2^2-\sum_i r_iD^2f_i[v,v].
 \tag{12}
\]

Thus the first term provides real damping. The second term cannot be bounded below using only the actual network's raw L2 ball, even when the three inputs are perfectly separated. The following example is inside the original canonical raw state space.

#### Original-L3 counterexample to a raw-ball Hessian lower bound

Take d>=3 and three orthogonal RMS-unit inputs, so Gamma=I_3 and every pairwise absolute correlation is zero. Keep all hidden parameters at their canonical initialization. Let q_2>0 be the common second-layer feature variance. Oddness and the fresh initialized Gaussian forward rules give

\[
 \langle h_i^2,h_j^2\rangle=q_2\mathbf1_{i=j},
 \qquad(Z_1^3,Z_2^3,Z_3^3)\sim N(0,q_2I_3).
\]

Here `a^4<=q_2<=1`. For arbitrarily small epsilon>0, choose a measurable set E_epsilon of probability epsilon contained in `{-2<=Z_1^3<=-1}` and depending only on Z_1^3. Such sets exist because this Gaussian interval has positive nonatomic measure. Set

\[
 u_\epsilon=\epsilon^{-1/2}\mathbf1_{E_\epsilon},
 \qquad C=u_\epsilon.
\]

This modifies only the readout and has raw distance exactly one from canonical initialization. Every primal L2 norm and every initialized action norm remains bounded independently of epsilon. Take labels `(1,1,1)` and consider the unit Hilbert--Schmidt perturbation of the final hidden action

\[
 \Delta B=u_\epsilon\otimes \frac{h_1^2}{\sqrt{q_2}},
 \qquad\|\Delta B\|_{\rm HS}=1.
 \tag{13}
\]

The other parameter directions are zero. Orthogonality implies

\[
 \Delta z_1^3=\sqrt{q_2}\,u_\epsilon,
 \qquad\Delta z_2^3=\Delta z_3^3=0.
\]

Along the one-dimensional raw line `B+s Delta B`, differentiating twice under the integral is justified for each fixed epsilon: C and Delta z are bounded fields and phi has bounded first two derivatives. No global twice-Frechet-differentiable Hilbert loss is assumed. The predictor derivatives obey

\[
 |Df_1[\Delta B]|
 =\sqrt{q_2}\,\epsilon^{-1}
       E[\mathbf1_E\phi_\theta'(Z_1^3)]\le\sqrt{q_2},
\]

\[
 D^2f_1[\Delta B,\Delta B]
 =q_2\epsilon^{-3/2}
       E[\mathbf1_E\phi_\theta''(Z_1^3)]
 \ge q_2\frac{4\theta}{25}\epsilon^{-1/2}.
 \tag{14}
\]

The last inequality uses
`phi_theta''(z)=-2theta z/(1+z^2)^2>=4theta/25` for -2<=z<=-1. The other two predictor derivatives vanish. On E the activation is negative, so `f_1=E[C phi_theta(Z_1^3)]<0` and `r_1=f_1-1<-1`. Consequently

\[
 D^2L[\Delta B,\Delta B]
 \le q_2\left[1-\frac{4\theta}{25}\epsilon^{-1/2}\right]
 \longrightarrow-\infty.
 \tag{15}
\]

The positive `J^*J` part in this calculation is at most q_2, whereas negative residual curvature is unbounded. This proves that the full original loss has no raw-ball lower Hessian bound of the form `D^2 L>=-C_R I`, even on the radius-one ball and with Gamma=I.

In a tangent-energy argument based on (12), a uniform bound using only primal L2 sizes therefore cannot hold. One must control the specific reachable readout/cotangent tails, the correlation between those fields and tangent directions, or some smaller admissible tangent class. Equation (15) is not a reachable trajectory counterexample: canonical population C starts at zero, and no claim is made that GF produces these concentrated readouts.


### E. Stationary-state obstruction to every smooth positive metric on a raw ball

For every fixed \(0<e\le1/2\) and \(0<\delta\le1/4\), the model of A
has exact nonzero-loss stationary states in a common raw-radius ball whose
finite-dimensional restricted gradient-flow linearizations have positive
eigenvalues tending to infinity. The radius may depend on \(e,\delta\),
but not on the concentration parameter. Hence no smooth positive
Riemannian metric gives a finite differential one-sided-Lipschitz constant
on that whole ball. The states lie below the canonical initial loss
\(3/2\). This is an ambient-ball obstruction, without a reachability claim.

#### E.1. The useful scalar transform and its limitation

Write `phi(z)=a z+e atan z`, with `a=1-e`, `0<e<=1/2`, and `g=phi'`.
Then `a<=g<=1`. In the toy system

\[
 x'=g(x)A^*y,\qquad y'=A\phi(x),
\]

set `v=T(x)`, where

\[
 T(x)=\int_0^x\frac{ds}{g(s)}.
\]

Both T and its inverse act as globally Lipschitz maps on L2. The curve chain rule gives

\[
 v'=A^*y,\qquad y'=A\phi(T^{-1}(v)).
\]

The last coordinate map has derivative `g(T^-1(v))^2`, bounded by one. Thus the transformed toy system is a globally Lipschitz Hilbert ODE. This is a real cancellation, not merely a formal coordinate analogy.

For normalized sample directions u_i, the actual bottom row is driven by the vector fields

\[
 X_i(w)=g(u_i\cdot w)u_i.
\]

For two nonparallel, nonorthogonal directions with correlation rho,

\[
 [X_i,X_j]
 =\rho\{g_i g_j' u_j-g_jg_i'u_i\}.
\]

At w=0 the bracket vanishes, but its derivative is

\[
 D[X_i,X_j](0)
 =\rho\phi'''(0)(u_j u_j^T-u_i u_i^T)
 =-2e\rho(u_j u_j^T-u_i u_i^T).                       \tag{1}
\]

On their two-dimensional span its eigenvalues are
`+/- 2e |rho| sqrt(1-rho^2)`, both nonzero.
If all X_i were Killing fields for one smooth positive metric, their bracket would also be Killing. A Killing field vanishing at a point has a skew-adjoint derivative in that point's inner product: its linearized local flow preserves that inner product. Such a derivative cannot have a nonzero real eigenvalue. Equation (1) is therefore a contradiction.

This excludes a common rowwise metric which exactly cancels arbitrary incoming controls. It applies in particular to the equilateral admissible triple. It does not assume that actual GF supplies arbitrary controls or claim that a state-dependent full-parameter metric has already been excluded; the stronger construction below addresses the latter possibility on raw balls.

For a full-rank sample Gram Gamma, another manifestation appears in feature coordinates h=phi(z). The mobility is `D Gamma D`, with `D=diag(g(z_i))`. Its inverse has entries

\[
 M_{ij}(h)=\frac{(\Gamma^{-1})_{ij}}{g(z_i)g(z_j)}.
\]

For i!=j, `partial_{h_j} M_{ii}=0`, whereas

\[
 \partial_{h_i}M_{ij}
 =-\frac{(\Gamma^{-1})_{ij}\phi''(z_i)}{g(z_i)^3g(z_j)}.
\]

Thus this inverse metric is not the Hessian of a potential whenever an off-diagonal inverse-Gram entry is nonzero. A direct separable mirror/Bregman transplant of the scalar transform fails its Hessian integrability condition.

#### E.2. An elementary equal-elasticity lemma

For z>0 define

\[
 E(z)=\frac{\phi(z)}{z g(z)}.
\]

For every fixed r in (0,1), there is a finite t>0 with

\[
 E(rt)=E(t).                                             \tag{2}
\]

Indeed, Taylor expansion at zero gives

\[
 E(z)=1+\frac{2e}{3}z^2+O(z^4),
\]

so `E(rt)-E(t)<0` for small t>0. At infinity,

\[
 E(z)=1+\frac{e\pi}{2az}+O(z^{-2}),
\]

so the difference is positive for large t. Continuity proves (2).
All expansions have fixed positive a and e; no uniform t-bound is asserted.

At such a pair put

\[
 r_{new}=\frac{\phi(rt)}{\phi(t)}.
\]

Strict positivity, monotonicity, and strict concavity of phi on (0,infinity) imply
`r<r_new<1`. Equality of elasticities gives the exact useful identity

\[
 \frac{g(rt)}{g(t)}=\frac{r_{new}}r.                    \tag{3}
\]

#### E.3. Three scales and an exact nonzero-loss stationary pattern

Fix `0<delta<=1/4`, put `c=1-delta`, `s=sqrt(1-c^2)`, and choose

\[
 u_+=(c,s),\qquad u_0=(1,0),\qquad u_-=(c,-s),
 \qquad y=(1,-1,1).
\]

Their side/center correlations equal c. Their side/side correlation is 2c^2-1, nonnegative for c>=3/4 and at most c because (2c+1)(c-1)<=0. Thus every absolute off-diagonal correlation is at most 1-delta. Use the preceding lemma three times:

1. Choose t_1 with `E(c t_1)=E(t_1)` and define
   `r_1=phi(c t_1)/phi(t_1)`.
2. Choose t_2 with `E(r_1 t_2)=E(t_2)`, define
   `lambda=t_2/phi(t_1)>0`, and
   `r_2=phi(r_1 t_2)/phi(t_2)`.
3. Choose t_3 with `E(r_2 t_3)=E(t_3)`, define
   `mu=t_3/phi(t_2)>0`, and
   `r_3=phi(r_2 t_3)/phi(t_3)`.

All quantities are fixed and finite for the chosen e and delta, and
`c<r_1<r_2<r_3<1`. Define the scalar composition

\[
 F(z)=\phi(\mu\phi(\lambda\phi(z))),\qquad H=\phi(t_3).
\]

Then

\[
 F(c t_1)=r_3H,\quad F(t_1)=H,\quad
 \frac{F'(c t_1)}{F'(t_1)}=\frac{r_3}{c}.               \tag{4}
\]

The derivative ratio follows by multiplying (3) at the three layers.
Also F is strictly increasing and strictly concave for z>0; direct differentiation of the composition makes every contribution to F'' negative.

Choose the mean readout

\[
 c_0=\frac{2r_3-1}{H(1+2r_3^2)}.
\]

The prediction vector from a constant neuron feature pattern is
`f=c_0 H(r_3,1,r_3)`. Its residual is exactly

\[
 r=f-y=\kappa(1,-2r_3,1),\qquad
 \kappa=-\frac{1+r_3}{1+2r_3^2}<0.                     \tag{5}
\]

For this residual, all the following contractions vanish:

\[
 \sum_i r_i h_i^3=0,\qquad
 \sum_i r_i g(z_i^3)h_i^2=0,
\]
\[
 \sum_i r_i g(z_i^3)g(z_i^2)h_i^1=0,
\]
\[
 \sum_i r_i g(z_i^3)g(z_i^2)g(z_i^1)u_i=0.             \tag{6}
\]

Here the sample values are the three scalar layer pairs just constructed. The side/center ratio of the first scalar product in the second expression is
`r_2 [g(r_2 t_3)/g(t_3)]=r_3`. For the next it is
`r_1 [g(r_1 t_2)/g(t_2)] [g(r_2 t_3)/g(t_3)]=r_3`.
The last vector identity follows from `u_++u_-=2c u_0` and the product derivative ratio `r_3/c` in (4). This proves every cancellation in (6).

#### E.4. Realization inside the original canonical raw state space

Let p in (0,1/2) tend to zero. On each canonical neuron probability space choose an event of probability p and define the normalized centered two-valued field

\[
 f_p=\frac{1_E-p}{\sqrt{p(1-p)}}.
\]

It has mean zero and L2 norm one. Each canonical space is nonatomic because it includes a Gaussian root; events of the prescribed probability exist. Let P_l be the orthogonal projection onto
`span{1,f_p}` in layer l. The identical two values and probabilities identify these two-dimensional spaces isometrically, including their pointwise multiplication algebras.

Let U_21 and U_32 denote the partial isometries mapping the respective orthonormal bases `(1,f_p)` to `(1,f_p)`. Starting from the actual canonical bounded initialized actions A_0 and B_0, set

\[
 A_p=(I-P_2)A_0(I-P_1)+\lambda U_{21},
\]
\[
 B_p=(I-P_3)B_0(I-P_2)+\mu U_{32}.                     \tag{7}
\]

These changes are finite-rank and hence Hilbert--Schmidt. Since initialized norms are at most 10,

\[
 \|A_p-A_0\|_{HS}\le\sqrt2(30+\lambda),\qquad
 \|B_p-B_0\|_{HS}\le\sqrt2(30+\mu).                    \tag{8}
\]

For example expand the first difference as
`-P_2 A_0-A_0 P_1+P_2 A_0 P_1+lambda U_21`; each of the first three terms has HS norm at most `10sqrt(2)`. The complement blocks in (7) remain the original actions. Their actual adjoints are used throughout.

Choose the first-layer parameter to be the constant map
`w=t_1 u_0`, and choose the readout

\[
 C_p=c_0\,1-f_p.                                        \tag{9}
\]

All sample features are constant on each neuron space, with the values in E.3. The prediction depends only on the mean c_0 and is independent of p. The readout has norm `sqrt(c_0^2+1)`, also independent of p.
The raw squared distance from canonical initialization is bounded uniformly in p by

\[
 d+t_1^2+2(30+\lambda)^2+2(30+\mu)^2+c_0^2+1.           \tag{10}
\]

The first term follows from the centered identity-covariance Gaussian initial first map. We may fix d=2 throughout.

Every one of these states is an **exact stationary point of the original full GF**. Indeed, its backward fields are respectively

\[
 b_i^3=g(z_i^3)C_p,\quad
 b_i^2=\mu g(z_i^2)g(z_i^3)C_p,\quad
 b_i^1=\lambda\mu g(z_i^1)g(z_i^2)g(z_i^3)C_p,
\]

with the corresponding copies of C_p on each neuron space. Substituting these into every raw gradient block gives precisely the four cancellations (6). No hidden block is frozen or removed in this calculation. The residual (5) is nonzero. These stationary states even belong to the
initial loss sublevel: their loss is

\[
 L_{crit}=\frac{(1+r_3)^2}{1+2r_3^2}<\frac32=L(0),
\]

where the strict inequality follows from `(2r_3-1)^2>0`. Thus adding
only loss sublevel control does not remove the construction.

#### E.5. Unbounded negative loss curvature at those stationary states

Let

\[
 v_p=1_E/\sqrt p
\]

on the first layer, and vary only the first parameter by
`Delta w=v_p e_2`. This direction has raw norm one and belongs to `span{1,f_p}`.
Keep A_p,B_p,C_p fixed along this variation. Since the two-valued algebra is closed under every coordinate activation and the restricted actions are lambda and mu times its identity, the sample predictor along this curve is exactly

\[
 f_i(\epsilon)=E\left[C_p F(t_1u_i\cdot u_0+
                           \epsilon v_p u_i\cdot e_2)\right].
\]

Consequently its loss second derivative at zero is

\[
 L''(0)
 =\sum_i\left[F'(t_1u_i\cdot u_0)(u_i\cdot e_2)E(C_pv_p)\right]^2
 +E(C_pv_p^2)\sum_i r_i F''(t_1u_i\cdot u_0)(u_i\cdot e_2)^2.
\]

The exact scalar moments are

\[
 E(C_pv_p)=c_0\sqrt p-\sqrt{1-p},\qquad
 E(C_pv_p^2)=c_0-\sqrt{(1-p)/p}.
\]

The center sample's perpendicular projection vanishes. The two side contributions give

\[
 K_*:=\sum_i r_i F''(t_1u_i\cdot u_0)(u_i\cdot e_2)^2
 =2\kappa s^2 F''(ct_1)>0.                              \tag{11}
\]

Strict positivity uses kappa<0, s>0, and F''(ct_1)<0. Therefore

\[
 L''(0)
 \le2s^2F'(ct_1)^2(|c_0|+1)^2
 +K_*\left[c_0-\sqrt{(1-p)/p}\right]
 \longrightarrow-\infty.                              \tag{12}
\]

This is a unit-direction Hessian calculation at an exact stationary point, not an estimate at an arbitrary noncritical state.

#### E.6. Consequence for full-parameter metrics

For each fixed p, allow all first-layer coordinates in the two-dimensional algebra, all 2-by-2 learned action blocks between these algebras, and all readout coordinates there; keep the complement blocks from (7) fixed. This is an invariant finite-dimensional submanifold of the exact GF: activations remain two-valued, backward fields stay in the same subspaces, and rank-one updates stay in the corresponding action blocks.

On this finite-dimensional submanifold the loss and vector field are smooth. At the stationary state, (12) shows that its selfadjoint loss Hessian has a negative eigenvalue tending to minus infinity. Hence the restricted GF linearization has a positive eigenvalue tending to plus infinity, although all states lie in the one fixed raw ball (10).

Suppose a smooth positive Riemannian metric on the full parameter state space made the GF one-sided Lipschitz on that ball with one finite constant L_B. Restrict it to this invariant submanifold. At a stationary point the derivative-of-metric-along-flow term is zero. For an eigenvector of the linearized GF with positive eigenvalue lambda_p, the metric quadratic growth is exactly `2lambda_p` times its squared metric norm. The one-sided bound therefore requires `lambda_p<=L_B`, a contradiction as p tends to zero.

This argument allows metric cross terms between every parameter block. Uniform equivalence to the raw metric is not needed for the eigenvalue contradiction; positivity on each restricted tangent space already suffices. Smoothness is used only for the usual differential one-sided-Lipschitz formulation.

### F. Order-one Gaussian readout: a global two-hidden-layer theorem

#### F.1. Activation class, metric and conclusion

Let \(\phi\in C^2(\mathbb R)\), put \(d=\phi'\), and assume that
\(\phi,d\) are bounded and globally Lipschitz, with \(d(x)>0\).
Assume
\[
 \Theta(x)=\int_0^x d(u)^{-1}du
\]
is a global increasing bijection, is pseudo-Lipschitz of some finite
degree, and \(\Theta(U)\) has every finite moment for \(U\sim N(0,1)\).
Here pseudo-Lipschitz of degree \(k\) means
\(|F(x)-F(y)|\le C(1+|x|^{k-1}+|y|^{k-1})|x-y|\).
With \(\iota=\Theta^{-1}\), require the transformed maps
\(\psi=\phi\circ\iota\) and \(c=d\circ\iota\) to be bounded and globally
Lipschitz. These are the tame-natural-gate hypotheses used here. The
coordinate maps \(\Theta,\psi,c,d\), and the finite products and
compositions of them used in fixed Euler instructions and polynomial
moment tests, are pseudo-Lipschitz of some finite degree, jointly with
their scalar multiplication parameters. Indeed a bounded Lipschitz map
has degree one; the defining inequality, polynomial growth, and the
identity \(FG-\widetilde F\widetilde G=(F-\widetilde F)G+
\widetilde F(G-\widetilde G)\) prove closure under finite sums,
products and compositions, with a possibly larger degree. No assumption
on unnamed extra coordinate maps is imposed. The proof below uses only
the specified bounded-derivative instructions and second-moment laws.

Fix one RMS-unit sample, two hidden layers, a real label \(y\), and a
constant learning-rate multiplier \(\eta\ge0\). The effective first
preactivation \(u\in\mathbb R^n\), stored readout \(a\in\mathbb R^n\),
and adjacent matrix \(g\in\mathbb R^{n\times n}\) have squared metric
\(\|\Delta u\|_2^2/n+\|\Delta a\|_2^2/n+\|\Delta g\|_F^2\). Initialize mutually independently by
\[
 u_{0,i},a_{0,i}\sim N(0,1),\qquad g_{0,ij}\sim N(0,1/n).
\]
These are order-one stored readout coordinates. The predictor and loss are
\[
 f_n=a^T\phi(g\phi(u))/n,
 \qquad \mathcal L_n=(y-f_n)^2.
\]
Physical time is the full-square gradient flow
\(\dot\theta=-\eta\nabla\mathcal L_n\), with all three effective blocks
trained. In a full first-weight representation only the sample direction
moves; its normalized first-row metric induces exactly the metric on \(u\).

**Theorem.** There is a deterministic canonical two-population action
source and a unique global population flow in the class specified in F.3.
It is autonomous and uniquely restartable while retaining its source.
For every fixed \(T<\infty\), along the full width sequence,
\[
 \sup_{0\le t\le T}
 (|f_n-f|+|K_n-K|+|y-f_n-e|+|\mathcal L_n-e^2|)
 \longrightarrow0\quad\hbox{in probability}.
 \tag{F.1}
\]
Write \(e=y-f=-r\) for the signed target error, where the residual
is \(r=f-y\). Here \(K_n\) is the complete raw predictor-gradient squared norm in the
specified metric. Fixed finite same-population current-field laws converge
in \(\mathcal W_2\), and bounded Lipschitz current-field observations
converge uniformly on compact time intervals. Finite and population
states are compared through their laws and action observations; no norm
between different neuron spaces is defined. This theorem asserts neither
exact raw-GD convergence, the full hidden-velocity bundle, nor asymptotic
fitting. Each activation is fixed; constants need not be uniform over the
class.

The proof first constructs one fixed Gaussian source from bounded-derivative
programs, then builds readout-capped flows. Gaussian readout tails remove
the cap. Two separate approximation meshes supply square-tail control
and passage of the raw kernel before physical time is restored.

#### F.2. Exact coordinates and a contained finite-program specialization

At finite width set \(\xi=\Theta(u)\); write \(\Xi\) for its population
coordinate, \(A\) for the population readout and \(G\) for the population
action. All unmarked norms in the following population formulas are
their explicitly typed Hilbert-space norms. Since \(\iota'=d\circ\iota=c\),
\(\psi'=c^2\). Define, with actual population adjoints,
\[
 X=\psi(\Xi),\quad Z=GX,\quad Y=\phi(Z),\quad
 B=A d(Z),\quad Q=G^*B.
\]
The feature-ascent equations and complete kernel are exactly
\[
 A_s=Y,\qquad \Xi_s=Q,\qquad G_s=B\otimes X,
 \tag{F.2}
\]
\[
 f=\langle A,Y\rangle,\qquad
 K=\|Y\|_2^2+\|B\|_2^2\|X\|_2^2+\|c(\Xi)Q\|_2^2.
 \tag{F.3}
\]
The separate finite identities, with \(x=\psi(\xi)\), \(z=gx\),
\(y^{\rm feat}=\phi(z)\), \(b=a d(z)\), and \(q=g^Tb\), are
\[
 a_s=y^{\rm feat},\qquad \xi_s=q,\qquad g_s=bx^T/n,
 \qquad
 K_n=\frac{\|y^{\rm feat}\|_2^2}{n}
 +\frac{\|b\|_2^2\|x\|_2^2}{n^2}
 +\frac{\|c(\xi)q\|_2^2}{n}.
\]
Indeed \(df[dg]=b^T(dg)x/n\). The finite raw first gradient is
\(d(u)q\); multiplication by \(\Theta'(u)=1/d(u)\) gives
the transformed first-coordinate equation.
Thus the coordinate change does not change the optimizer or its metric.
The identities \(X_s=c(\Xi)^2Q\) and
\(Z_s=B\|X\|_2^2+G[c(\Xi)^2Q]\) give \(f_s=K\).
The strong scalar chain rules used here are III.F.9--III.F.10.

The required source is an instance of III.F.1--III.F.7 with two types,
one independent Gaussian matrix, row root \(A_0\), and column root tuple
\((u_0,\Theta(u_0))\). That tuple has finite second moment and is iid
across coordinates and independent of the matrix, precisely as III.F.1
requires; no assertion that it is jointly Gaussian is made. Roots need
not be generated by bounded-derivative instructions. The inverse
\(\iota\) is globally Lipschitz since \(\iota'=c\) is bounded. All of
\(\phi,d,\psi,c\) are \(C^1\) with bounded first derivative by the class
hypotheses. A smooth saturation of the current \(A\) makes
\((A,Z)\mapsto\chi(A)d(Z)\) a \(C^1\) map with bounded partial derivatives.
Nonsmooth initial clipping is included directly in the iid row root tuple.
Thus these fixed programs meet III.F literally.

For clarity, fixed capped Euler with step \(h\) eliminates the learned
matrix as
\[
 z^k=g_0x^k+\sum_{j<k}h b^j (x^j)^Tx^k/n,
 \qquad
 q^k=g_0^Tb^k+\sum_{j<k}h x^j (b^j)^Tb^k/n.
 \tag{F.4}
\]
Construct its companion on the same arrays, replacing each contraction
when encountered by its already-defined population expectation.
These are deterministic causal constants. III.F identifies this fixed
bounded-derivative program, with singular Grams allowed. To restore the
actual feedback, use at each contraction
\[
 |u^Tv/n-E[\bar U\bar V]|
 \le\|u-\bar u_n\|_2\|v\|_2/n
 +\|\bar u_n\|_2\|v-\bar v_n\|_2/n
 +|\bar u_n^T\bar v_n/n-E[\bar U\bar V]|.
 \tag{F.5}
\]
Here \(\bar u_n,\bar v_n\) are finite companion vectors and
\(\bar U,\bar V\) their same-population limits. The last term
vanishes by the companion law. Matrix errors are at most
the initialized operator norm times input RMS errors. Saturated-coordinate
errors obey a fixed Lipschitz bound. Scalar multiplication errors obey
\(\|cu-\bar c\bar u\|_2\le |c|\|u-\bar u\|_2+
|c-\bar c|\|\bar u\|_2\).
Induction over the finite transcript gives vanishing errors, bounded norms,
and all joint \(\mathcal W_2\) laws. No control of higher moments of the
error, no inverse-Gram continuity and no growing transcript are used.

Include the roots, all integer readout clips, rational meshes and the
fixed coordinate maps in the countable language of III.F.7, closed under
finite unions and its dense bounded smooth functions. Its consistent
joint laws define \(H_C=L^2(\Omega_C)\), \(H_R=L^2(\Omega_R)\), and
\(\Gamma:H_C\to H_R\). The finite norm bound ten descends to the dense
program span; the exact finite transpose pairing identifies \(\Gamma^*\).
This is the same completed source for every clip and mesh, chosen before
the label or trajectory. The laws in this construction are second-moment
laws, not an unrestricted all-polynomial-moment assertion.

#### F.3. Global feature flow and Gaussian-envelope uniqueness

Write \(G=\Gamma+P\), with \(P\in\mathfrak S_1(H_C,H_R)\).
The trace class is complete and
\(\|b\otimes x\|_1=\|b\|_2\|x\|_2\), by linear Section 2.A.
Let \(M_\phi=\|\phi\|_\infty\), \(M_d=\|d\|_\infty\). On \(|s|\le S\),
(F.2) gives
\[
 |A(s)-A_0|\le M_\phi|s|,\quad
 \|A(s)\|_2\le\|A_0\|_2+M_\phi|s|,
\]
\[
 \|P(s)\|_1\le M_\phi M_d\bigl(\|A_0\|_2|s|+M_\phi s^2/2\bigr),
 \quad
 \|\Xi(s)\|_2\le\|\Xi_0\|_2+
 M_d\int_0^{|s|}(\|\Gamma\|+\|P\|_1)(\|A_0\|_2+M_\phi\sigma)d\sigma.
 \tag{F.6}
\]
The same estimates hold for finite normalized vectors. They bound
\(A,B,P,Q,\Xi\) by \(C_S\), uniformly over readout clips, on a common
initialization event \(\|g_0\|\le10\),
\(\|a_0\|_2/\sqrt n,\|\xi_0\|_2/\sqrt n\le C\)
whose probability tends to one by III.F.2 and the iid second-moment law.

For the initial readout \(A_{0,M}=\operatorname{clip}_{[-M,M]}A_0\),
saturate the current \(A\) only in \(B\) outside
\(|A|\le M+M_\phi S+1\). The ambient field is locally Lipschitz on
\(H_R\oplus H_C\oplus\mathfrak S_1\). Indeed forward differences are
bounded by the state distance
\[
 D=\|\Delta A\|_2+\|\Delta\Xi\|_2+\|\Delta P\|_1,
\]
with constants from (F.6), and
\[
 \|\Delta B\|_2\le M_d\|\Delta A\|_2
 +(M+M_\phi S+2)\operatorname{Lip}(d)\|\Delta Z\|_2,
\]
\[
 \|\Delta Q\|_2\le\|G\|\|\Delta B\|_2+
 \|\Delta P\|_1\|\widetilde B\|_2,
\]
\[
 \|B\otimes X-\widetilde B\otimes\widetilde X\|_1
 \le\|B-\widetilde B\|_2\|X\|_2+
 \|\widetilde B\|_2\|X-\widetilde X\|_2.
 \tag{F.7}
\]
The integrated field contracts on a sufficiently short interval. The
first bound in (F.6) makes the saturation inactive, and the remaining
bounds continue the solution throughout every slab and in both time
directions. The rank-one trace-norm integrals are strong integrals by
completeness and continuity of their factors.

For two caps \(N\ge M\), put the smaller readout in the gate-difference
term:
\[
 A_Nd(Z_N)-A_Md(Z_M)
 =(A_N-A_M)d(Z_N)+A_M[d(Z_N)-d(Z_M)].
\]
Every other coefficient in (F.7) is bounded independently of \(M,N\).
Gronwall therefore gives, including the derived \(B,Q\) differences,
\[
 \sup_{|s|\le S}(D+\|\Delta B\|_2+\|\Delta Q\|_2)
 \le C_Se^{C_SM}\|A_{0,N}-A_{0,M}\|_2.
 \tag{F.8}
\]
A polynomial factor in \(1+M\) has been absorbed in the exponential.
For standard Gaussian \(A_0\), integration of its density on
\(|x|>M\), or one integration by parts followed by its exponential
tail bound, gives
\[
 \|A_0-\operatorname{clip}_M A_0\|_2
 \le C(1+M)e^{-M^2/4}.
 \tag{F.9}
\]
Thus the capped solutions and their derivatives are Cauchy on each slab.
Their strong limit solves (F.2), has continuous \(A,\Xi\) in \(L^2\)
and \(P\) in trace norm, and retains \(|A-A_0|\le M_\phi S\).

The uniqueness class consists of such integral solutions with
\(A-A_0\in L^\infty(\Omega_R\times[-S,S])\) on every slab.
For a bounded Lipschitz gate \(h\), Hölder gives, for \(p\ge2\),
\[
 \|A_0(h(z)-h(\tilde z))\|_2
 \le C\sqrt p\,[L\|z-\tilde z\|_2]^{1-1/p}
                      (2\|h\|_\infty)^{1/p}.
\]
This uses \(\|A_0\|_{2p}\le C\sqrt p\), without independence of
\(A_0,z,\tilde z\). Choosing \(p\) comparable to
\(\log(C/D)\) gives the modulus \(\omega(D)=CD\sqrt{\log(C/D)}\)
for small \(D>0\). Equations (F.7) imply
\(D(t)\le D(0)+\int_0^{|t|}\omega(D(s))ds\), after enlarging constants.
For a positive initial upper error \(\epsilon\), define
\(Z(t)=\epsilon+\int_0^t\omega(D(s))ds\). Then \(D\le Z\),
\(Z'\le\omega(Z)\), and separation of variables bounds \(Z\).
Because \(\int_{0+}du/[u\sqrt{\log(C/u)}]=\infty\), this bound tends
to zero as \(\epsilon\downarrow0\) at every fixed time. Equal initial
states therefore give equal solutions. The same argument gives continuous
dependence in this class. Keeping the immutable Gaussian mark and action
makes the class and equation closed under restart. Compatible slabs give
one global feature flow.

For kernel continuity, if \(\Xi_j\to\Xi\), \(Q_j\to Q\) in \(L^2\),
then \(c(\Xi_j)Q_j\to c(\Xi)Q\) in \(L^2\): subtract the varying \(Q\),
truncate the remaining fixed \(Q\), and use bounded convergence in
probability. This proves continuity of (F.3). The cutoff scalar chain
rule passes to the limit uniformly on compact intervals by the same
argument and compactness of continuous \(L^2\) paths. Hence \(f_s=K\)
and \(K\ge0\) for the uncut flow as well.

#### F.4. Fixed-cap width passage and the two distinct mesh limits

Fix \(M,S\). The saturated field on the common bound (F.6) has a
width-independent speed and Lipschitz constant. For finite states define
\[
 D_n((a,\xi,g),(\tilde a,\tilde\xi,\tilde g))
 =\|a-\tilde a\|_2/\sqrt n
 +\|\xi-\tilde\xi\|_2/\sqrt n
 +\|g-\tilde g\|_1,
\]
where the last norm is the ordinary matrix nuclear norm. Over one step its integral
error is at most \(L Vh^2/2\); iterating
\(E_{k+1}\le(1+Lh)E_k+LVh^2/2\) gives
\[
 \sup_{|s|\le S}(D_n(U_{n,M},U^h_{n,M})+
                          \|q_{n,M}-q^h_{n,M}\|_2/\sqrt n)
 \le C_{M,S}h.
 \tag{F.10}
\]
The same estimate holds separately in the population source. Nearest-node
observations are included by the bounded time speed. A first-exit argument
on a slightly enlarged ball justifies all Euler bounds; the pointwise
readout update preserves \(|a^k|\le M+\|\phi\|_\infty|kh|\) exactly. At fixed \(h\),
(F.4)--(F.5) identify the entire finite Euler law. Its learned matrix increment \(g^k-g_0\)
is a fixed sum of rank-one maps; its singular values and trace norm are
continuous functions of the two finite Gram matrices by linear (2.A.5).
This supplies the state/action observation passage without subtracting
states at different widths.

A fixed node's \(\mathcal W_2\) law already supplies square-tail uniform
integrability in probability. Explicitly,
\(\|(|q|-R)_+\|_2\) is a 1-Lipschitz functional of its law in
\(\mathcal W_2\); its limiting value tends to zero as \(R\to\infty\),
and
\[
 q^2\mathbf1_{|q|>2R}\le4(|q|-R)_+^2.
\]
A finite union handles all nodes of one fixed mesh. For arbitrary scalars
\(q,v\), splitting into \(|v|\le R/2\) and its complement gives
\[
 q^2\mathbf1_{|q|>R}
 \le4(q-v)^2+2v^2\mathbf1_{|v|>R/2}.
 \tag{F.11}
\]
Use one auxiliary mesh \(\bar h\) in (F.10), then (F.11), to obtain
for every \(\delta>0\)
\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\sup_{|s|\le S}
 \frac1n\sum_{i=1}^n q_{n,M,i}(s)^2\mathbf1_{|q_{n,M,i}(s)|>R}>\delta\right\}=0.
 \tag{F.12}
\]
Indeed choose \(\bar h\) so its squared approximation error is small;
at that fixed mesh take width to infinity and then a large tail cutoff.
This requires no fourth-moment theorem or estimate uniform in mesh length.

Now choose a second comparison mesh \(h\), after fixing a large \(R\)
from (F.12). The bounded Lipschitz observation
\(c(\Xi)^2\operatorname{clip}_R(Q)^2\) passes at fixed \(h\) by F.2.
The population varying-multiplier estimate is
\[
 \|(c(\Xi)-c(\Xi^h))Q^h\|_2^2
 \le \operatorname{Lip}(c)^2R^2\|\Xi-\Xi^h\|_2^2
 +4\|c\|_\infty^2 E[(Q^h)^2\mathbf1_{|Q^h|>R}].
 \tag{F.13}
\]
The finite version replaces the squared norms by Euclidean squared norms
divided by \(n\) and the expectation by \(n^{-1}\sum_i\).
Use (F.11) to transfer the last tail to the exact \(Q\), at cost
\(4\|Q-Q^h\|_2^2\) and a doubled tail at \(R/2\).
First select \(R\) from the established tail statement, then take
\(h\downarrow0\) after its fixed-program width limit. This proves
uniform convergence of \(\|c(\Xi)Q\|_2^2\). The coefficient
\(4\|c\|_\infty^2\) is retained for general shapes. The remaining
kernel terms use bounded \(X,Y,B\) at fixed \(M\). Thus \(f_{n,M}\)
and \(K_{n,M}\) converge uniformly on \([-S,S]\).

#### F.5. Gaussian cap removal and physical time

Compare the finite uncut and level-\(M\) feature flows by (F.8), with
the uncut flow in the larger-readout position. Their common primal bound
is (F.6), independent of \(M\). The expected squared empirical initial
clip error equals its scalar Gaussian expectation. Markov's inequality
and (F.9) therefore give
\[
 \lim_{M\to\infty}\limsup_{n\to\infty}
 \Pr\{\sup_{|s|\le S}(D_n(U_n,U_{n,M})+
                          \|q_n-q_{n,M}\|_2/\sqrt n)>\epsilon\}=0.
 \tag{F.14}
\]
The population version follows directly from (F.8). Formula (F.11)
first transfers (F.12) to the uncut finite \(q_n\): fix a large \(M\)
to make (F.14) small, then remove the tail cutoff at that fixed \(M\).
After this uncut tail statement has been established, (F.13), now comparing
\(\xi_n,\xi_{n,M}\), removes the gate multiplier by choosing its tail level
before sending \(M\to\infty\). This proves uniform feature-time
convergence of \(f_n,K_n\), as well as the fixed joint current-field
\(\mathcal W_2\) laws. All choices are fixed-tolerance choices before
the width limit; no width-dependent transcript theorem is asserted.

Let \(F(s)\) be the feature predictor. Since \(F\in C^1\) and
\(F'=K\ge0\), the scalar equation
\[
 \dot s=2\eta(y-F(s)),\qquad s(0)=0
 \tag{F.15}
\]
has a unique local solution. Independence of the initial readout from the
bounded top feature gives \(F(0)=0\), and at finite width
\(E[f_n(0)^2\mid u_0,g_0]\le M_\phi^2/n\). For \(e=y-F(s)\),
\[
 \dot e=-2\eta eK(s),\quad
 e(t)=y\exp\left[-2\eta\int_0^tK(s(v))dv\right],
 \quad |s(t)|\le2\eta|y|t.
 \tag{F.16}
\]
Thus every finite physical horizon uses a compact feature interval and
the physical flow is global. Its autonomous equations are
\[
 \dot A=2\eta eY,\quad \dot\Xi=2\eta eQ,\quad
 \dot P=2\eta eB\otimes X,\quad \dot e=-2\eta eK,
 \quad f=y-e,\quad \frac d{dt}e^2=-4\eta Ke^2.
 \tag{F.17}
\]
At a restart, the current quadruple and the unchanged source determine
the future. Uniqueness also follows directly by the Osgood estimate for
the state field multiplied by the bounded continuous target error
\(y-f\); its extra scalar difference is locally Lipschitz in the state.
The cases \(y=0\) or \(\eta=0\) give the stationary population flow.

At finite width the initial target error is exactly \(y-f_n(0)\), and
\(|s_n(t)|\le2\eta|y-f_n(0)|t\). On a common compact feature interval,
subtract the scalar clock equations and use the uniform convergence
\(F_n\to F\) and the Lipschitz constant of the fixed limiting \(F\).
Gronwall gives uniform convergence of clocks. Composing with the uniform
feature readouts proves (F.1). It does not justify an interchange with
\(t\to\infty\).

#### F.6. Arctangent and reciprocal-polynomial examples

For \(\phi(x)=\arctan x\),
\[
 \Theta(x)=x+x^3/3,\qquad
 \iota(v)=2\sinh\left(\tfrac13\operatorname{arsinh}(3v/2)\right),
 \quad E\Theta(U)^2=1+2+15/9=14/3.
\]
Here \(\iota'=c\le1\), \(\psi'=c^2\le1\),
\(c'(v)=-2\iota(v)/(1+\iota(v)^2)^3\), and
\(d'(z)=-2z/(1+z^2)^2\) are bounded. Hence every hypothesis holds.
For a fixed positive output scaling \(\phi=\lambda\arctan\), use
\(\Theta=(x+x^3/3)/\lambda\), and scale every occurrence of the
activation and its gate consistently. The theorem is unchanged in scope;
the full kernel does not acquire just one global power of \(\lambda\).

More generally take a strictly positive polynomial \(P\) with
\(\int_{\mathbb R}P(u)^{-1}du<\infty\), and bounded derivative of
\(d=1/P\). Set
\[
 \phi(x)=\int_0^xP(u)^{-1}du,\qquad
 \Theta(x)=\int_0^xP(u)du.
\]
The positive polynomial has a positive minimum, so \(d\) is bounded;
its integrability makes \(\phi\) bounded. The polynomial primitive is
an increasing global bijection and has all Gaussian moments. Also
\(\psi'=d(\iota)^2\), \(c'=d'(\iota)d(\iota)\) are bounded.
Finite compositions/products of these bounded Lipschitz maps with the
polynomial root have a finite pseudo-Lipschitz degree: repeated use of
\(FG-\tilde F\tilde G=(F-\tilde F)G+\tilde F(G-\tilde G)\) and
polynomial growth supplies the defining inequality. This verifies the
stated class interface. In particular every fixed integer \(m\ge1\) gives
\[
 P_m(x)=1+x^{2m},\qquad
 \phi_m(x)=\int_0^x\frac{du}{1+u^{2m}},\qquad
 \Theta_m(x)=x+\frac{x^{2m+1}}{2m+1}.
\]
Indeed \(d_m'=-2m x^{2m-1}/(1+x^{2m})^2\) is continuous and tends to
zero at infinity, hence is bounded. The \(m=1\) theorem is exactly the
order-one Gaussian-readout arctangent theorem. These conclusions remain
separate from bounded-readout theorems and from three-hidden-layer
continuation.

### G. Equal-label global transfer to the sech gate

#### G.1. Exact model and theorem

In the two-sample model of special-data Section II, replace the activation
at all three hidden layers by the one fixed function
\[
 \phi(z)=1+\tfrac1{10}\arctan(\sinh z),\qquad
 p(z)=\phi'(z)=\tfrac1{10}\operatorname{sech}z.
 \tag{G.1}
\]
Precisely, fix \(\|x_a\|^2=d\), \(-1\le\rho=x_1^Tx_2/d<1\), and
\(y_1=y_2=y\in\{-1,1\}\). Use first weights
\(V^{(1)}_{ij}\sim N(0,1/d)\), hidden matrix entries
\(W^{(2)}_{ij},W^{(3)}_{ij}\sim N(0,1/n)\), and stored readout
\(C_i\sim N(0,n^{-2})\), mutually independent. Set
\(z_a^1=V^{(1)}x_a\), \(z_a^2=W^{(2)}h_a^1\),
\(z_a^3=W^{(3)}h_a^2\), \(h_a^\ell=\phi(z_a^\ell)\),
\(f_a=C^Th_a^3/n\). The raw squared metric is
\[
 d\|\Delta V^{(1)}\|_F^2/n+
 \|\Delta W^{(2)}\|_F^2+\|\Delta W^{(3)}\|_F^2+
 \|\Delta C\|_2^2/n.
\]
Canonical first-weight storage is \(W^{(1)}=\sqrt d\,V^{(1)}\).
The loss is \(\mathcal L=\sum_{a=1}^2(f_a-y)^2\);
finite GF is its raw gradient flow, and exact raw GD has step
\(\eta_n=n^{-2}\). Parameters are linearly interpolated for GD,
with the forward pass recomputed and right-interior/left-terminal
velocity convention. Population readout is exactly zero initially.

**Theorem.** All the conclusions of special-data Theorem II.1 hold
for (G.1). The canonical strong population flow is global, unique
against every bounded-primal strong competitor on compact intervals,
and uniquely restartable at every reached full state. Finite GF,
exact raw GD and this population flow converge jointly in probability
along the full width sequence on every fixed \([0,T]\). Observations
include both samples' same-layer hidden preactivation/feature paths in
\(\mathcal W_2(C([0,T]))\), all four raw \(2\times2\) kernel blocks,
forward/backward fields, fixed generated forward/adjoint probes of both
hidden operators, hidden velocities with second moments, squared speeds
uniformly in time, and integrated squared speeds. Action increments are
Hilbert--Schmidt and their scalar norm/cross-time contraction observations
converge. No cross-width operator-norm convergence or cross-layer neuron
pairing is asserted.

With \(g=y(f_1+f_2)/2\),
\[
 f_1=f_2=yg,\quad 0\le g(t)<1,\quad
 1-g(t)\le e^{-25t/9},\quad \mathcal L(t)\le2e^{-50t/9}.
 \tag{G.2}
\]
Every sample/layer has positive affine-regression error at every finite
time, with a positive minimum on each compact interval. Every hidden
parameter block, sample preactivation and feature has positive \(L^2\)
speed for every \(t>0\); the readout speed is positive as well.
Hidden initial speeds vanish, but every initial hidden feature change
and the total label-mode kernel have a nonzero quadratic term.
The theorem covers \(\rho=-1\), either equal-label choice, and a fixed
nonlinearity. It gives no opposite-label global theorem and no
infinite-time/width interchange.

#### G.2. Hypothesis check for construction and finite algorithms

Differentiation gives
\[
 p'(z)=-\tfrac1{10}\operatorname{sech}z\tanh z,
 \quad 0<p\le1/10,\quad |p'|\le1/10\le1/5.
\]
Every higher fixed derivative is bounded: differentiation preserves
finite sums of products of bounded sech and tanh factors. Also
\[
 \int_0^\infty\operatorname{sech}z\,dz
 =2\int_0^1(1+t^2)^{-1}dt<5/3,
\]
since \((1+t^2)^{-1}<1-t^2/2\) for \(0<t<1\).
Thus \(5/6<\phi<7/6\), and \(\phi\) is strictly increasing.
These are precisely the activation inequalities in II.B: its raw
first-layer sensitivities use \(|\phi''|\le1/5\), \(p\le1/10\),
and \(|G_{ab}|\le1\); its middle/top induction uses the same bounds,
\(|\phi|\le7/6\), and smooth clips of both incoming reverse queries.
No inverse activation coordinate occurs in that proof.

Consequently the chronological calculation II.B.3--II.B.6, with (G.1)
substituted throughout, gives on \(0\le s\le S=3/2\)
\[
 V_k\le3067/3200<1,\quad
 U_k\le71063018523/73728000000<97/100,
 \quad |A^{(\ell)}_{ka,rb}|<(3/2)\Delta/2,
 \tag{G.3}
\]
\[
 E\exp((q^j_{ka})^2/16)<2\quad (j=1,2).
 \tag{G.4}
\]
Here \(U,V\) are the absolute backward response row sums and
\(A^{(\ell)}\) the forward-response coefficients defined by II.B.1--2;
\(q^1,q^2\) are the actual two capped incoming queries. The bounds are
uniform in the two caps and proof mesh. At fixed caps all coordinate
instructions have bounded first derivatives after the readout is
saturated outside \(|C|\le(7/6)S\). III.F applies to the Gaussian
sample-pair root, including \((G,-G)\) at \(\rho=-1\), and both reused
initialized matrices. Thus the same source laws and actual adjoints
are identified, without any additional probability import.

II.C.1--2 now constructs the cap flows on common spaces. Its asymmetric
comparison has constant \(C_S(1+R)\) and four reference tail terms
bounded in total by \(32e^{-R^2/256}\), using (G.4). These estimates
use only bounded forward features, bounded/Lipschitz gates, a bounded
reference readout, and genuine adjunction; all have just been verified.
The cap-Cauchy, raw derivative, Hilbert--Schmidt increment and nonsymmetric
competitor/restart arguments of those sections therefore apply verbatim.

The input-reflection isometry of II.A.2 exchanges the two samples for
any common activation; no oddness is required. Deterministic limiting
laws give equal population predictions. The label/readout sign reversal
covers \(y=-1\) and leaves the hidden dynamics unchanged. For \(y=1\),
\(C_s=(h_1^3+h_2^3)/2\ge5/6\), and scalar raw differentiation gives
\[
 g_s=\|\nabla g\|_{raw}^2
 \ge E[(h_1^3+h_2^3)^2/4]\ge25/36.
\]
Hence the feature flow reaches \(g=1\) at a unique
\(s_*\le36/25<3/2\). Its continuous \(g_s\) is bounded on this
constructed interval, so \(1-g(s)\le C(s_*-s)\) and
\(\int_0^{s_*}[4(1-g(s))]^{-1}ds=\infty\).
The physical clock \(s_t=4(1-g)\) is global and strictly positive
at finite times. Differentiating its residual gives (G.2).
At \(\rho=-1\) retain \(z_2^1=-z_1^1\) with its one-field raw
metric, as in II.A.1; no inverse singular Gram is used.

The physical comparisons II.C.3--4 use the full pair of actual finite
residuals, the two reference tails (G.4), and the population clock just
proved. Their fixed-cap Euler error is \(O(\eta_n)\), and recomputed
within-step gate/velocity errors are \(O(\eta_n\sqrt n)\), which vanish
for \(\eta_n=n^{-2}\). The primal first-exit argument and the
width-then-cap limit require no additional activation formula. Finally
II.C.5--6 transfers the stated observations: it clips one incoming
factor at a time, uses its fixed joint \(\mathcal W_2\) law, and removes
the clip with the compact reference path's square tails. That proof
requires exactly bounded/Lipschitz gates and bounded actions, already
checked here. This establishes the full listed algorithm and observable
scope, including nonsymmetric physical competitors.

#### G.3. Nonaffinity and positive motion: the two formula-dependent steps

Two numerical substitutions finish the activity proof. First,
\[
 z_1\ge1,\ z_2\le-1
 \quad\Longrightarrow\quad
 \phi(z_1)-\phi(z_2)
 \ge\tfrac15\arctan(\sinh1)>\pi/20,
 \tag{G.5}
\]
because \(\sinh1=1+1/3!+1/5!+\cdots>1\).
This is the separation threshold in II.D.1. Its lower-layer displacement
dominators have expectations below \(1/5\) and \(1/3\), respectively,
independent of the corresponding Gaussian root/forward source. The top
correction is bounded by \(63/160<2/5\). Their proofs use only (G.3)
and the activation bounds, so (G.5) gives the same strictly positive
feature-Gram lower bounds for each fixed \(\rho<1\).
At \(\rho=-1\), the first separation event is
\(\Pr(G\ge2)>0\); the feature Gram uses uncentered second moments,
retaining the positive constant feature direction.

The same dominators and nondegenerate forward Gaussian marginals give
both unbounded preactivation tails at every reached time, exactly as
II.D.2. For each scalar \(Z\) obtained there,
\[
 \inf_{\alpha,\beta}E[(\phi(Z)-\alpha Z-\beta)^2]
 =\operatorname{Var}(\phi(Z))-
       \frac{\operatorname{Cov}(Z,\phi(Z))^2}{\operatorname{Var}(Z)}>0.
\]
The denominator is positive. Zero error would give an affine identity;
bounded \(\phi\) on an unbounded support forces zero slope, and strict
monotonicity would force \(Z\) constant. Continuity of these moments
along the \(L^2\) path gives positive compact-time minima; joint
\(\mathcal W_2\) convergence transfers smaller bounds to empirical
regression errors. This is the expectation of the squared error.

Second, work in the positive-label convention and fix \(s_0>0\).
On the top forward-source rectangle
\([4,5]\times[-1/10,1/10]\), the correction bound gives
\(|Z_1^3|\ge18/5\), \(|Z_2^3|\le1/2\). For
\(b_a^3=Cp(Z_a^3)\), with \(C\ge(5/6)s_0\),
\[
 \frac{b_1^3}{b_2^3}
 =\frac{\cosh Z_2^3}{\cosh Z_1^3}<1/4,
 \qquad b_2^3>\tfrac45(5/6)s_0/10.
 \tag{G.6}
\]
Indeed the cosh series gives
\(\cosh(1/2)\le1+(1/8)/(1-1/48)=1+6/47<5/4\),
whereas \(\cosh(18/5)\ge1+(18/5)^2/2=187/25>5\).
The swapped rectangle gives the other direction. Both have a positive
Gaussian probability lower bound from the feature-Gram bounds. For any
unit vector \(v\in\mathbb R^2\), choose the rectangle where the larger
\(|v_a|\) multiplies the larger delta. The reverse triangle inequality
gives \(|v^Tb^3|\ge3b_0/(4\sqrt2)\), where
\(b_0=\tfrac45(5/6)s_0/10\). Thus the top backward second-moment
matrix is strictly positive definite.

Each lower reverse source has covariance equal to the full second-moment
matrix of its incoming upper backward pair, and response shift bounded
by \(7/6\). Its four signed Gaussian rectangles outside that bound
supply four nonzero query quadrants. Multiplication by \(p>0\) preserves
their signs, so no nonzero fixed combination of the two backward fields
vanishes. Induction proves positive-definite backward Grams at both lower
layers. The exact trace-product and forward-velocity pairings of II.D.4
then give strictly positive hidden raw block speeds and both samples'
hidden speeds; sample exchange gives equal sample norms, and the positive
clock transfers positivity to every finite physical \(t>0\).
For \(y=-1\), (G.6) is used for the label-aligned fields \(yb_a^3\),
whose Grams and hidden dynamics are unchanged.

For completeness, the initial quadratic coefficients require a separate
argument from positive-time speed. Set \(V=(h_1^3+h_2^3)/2\), let
\(D_0\) be its bounded linearized forward map at initialization, and put
\(B_0=D_0^*V_0\). The initialized top coefficient pair
\(V_0p(Z_a^3(0))\) is positive definite by (G.6) with its positive
factor \(V_0\ge5/6\). The initialized reverse formulas II.D.i1--i3
remain valid: differentiating this bounded top coordinate map uses only
bounded \(\phi,\phi',\phi''\); the next clipped reverse derivative is
dominated by \(C(1+|q^2|)\), and its actual \(q^2\) is Gaussian plus
bounded shift. III.F and dominated convergence therefore identify both
actual transpose laws. Their four signed quadrants show every hidden
block \((B_0)_\ell\ne0\), including the antipodal endpoint.
Let \(\gamma_\ell=\|(B_0)_\ell\|^2>0\), \(\gamma=\sum_\ell\gamma_\ell\).
The strong directional chain rule used in II.D.5 yields
\[
 C(s)=sV_0+o(s),\qquad
 \alpha(s)-\alpha(0)=\tfrac12s^2B_0+o(s^2),
\]
\[
 K_g^{(4)}(s)=\|V_0\|_2^2+\gamma s^2+o(s^2),\qquad
 K_g(s)=\|V_0\|_2^2+2\gamma s^2+o(s^2).
\]
Here \(\alpha\) is the hidden raw state and
\(K_g=\|\nabla g\|_{raw}^2=\tfrac14(y,y)^TK(y,y)\).
Every leading sample/layer feature coefficient is nonzero by the same
initial forward pairing and positivity of its gate. Since \(s(t)=4t+o(t)\),
its leading physical feature change has the form
\(8t^2p(Z_a^\ell(0))T_a^\ell+o(t^2)\), with a nonzero \(L^2\)
coefficient; the readout-mode and total-mode kernel changes are
\(16\gamma t^2+o(t^2)\) and \(32\gamma t^2+o(t^2)\).
This proves initial feature motion and a nonconstant total kernel.
The formula-dependent gate estimates are (G.5)--(G.6);
the remaining arguments use the verified boundedness, smoothness and
positivity properties.


### H. The sech gate under prescribed controls with fixed signs

This result concerns a two-coordinate characteristic with a prescribed
control. It does not require a network initialization, a training loss,
a width limit or a depth limit. Fix \(|\rho|<1\), set
\[
 C_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad
 \phi(z)=1+\tfrac1{10}\arctan(\sinh z),
\]
and let \(u\in L^1([0,T];\mathbb R^2)\) satisfy
\(s_i u_i(t)\ge0\) almost everywhere for two fixed signs
\(s_i\in\{-1,1\}\). There is a unique absolutely continuous solution
of
\[
 \dot z=C_\rho\operatorname{diag}(\phi'(z_1),\phi'(z_2))u(t),
 \qquad z(0)=z_0.
 \tag{H.1}
\]
Its derivative with respect to \(z_0\), holding the control fixed,
exists at every \(z_0\) and satisfies
\[
 \|D_{z_0}z(T)\|_{\rm op}
 \le \sqrt{\frac{1+k}{1-k}}\,e^4(e+U)^{16/(1-k)},
 \quad k=|\rho|,\qquad
 U=\frac1{10}\int_0^T\|u(t)\|_1dt.
 \tag{H.2}
\]
The bound is uniform over the initial point, vanishing control components
and changing component ratios within the fixed sign quadrant.
The exact relative-gate bound is also retained:
\[
 |\phi'(z)-\phi'(\tilde z)|\le|\phi(z)-\phi(\tilde z)|.
 \tag{H.3}
\]
Indeed \(\phi''/\phi'=-\tanh\), so the derivative of
\(\phi'\circ\phi^{-1}\) on the activation range has absolute value
at most one; integration proves (H.3).

**Proof.** The vector field and its spatial derivative are bounded by
an integrable constant times \(\|u(t)\|_1\). The spatial derivative
is Lipschitz in the state with an integrable coefficient because
\(\phi'''\) is bounded. Partitioning the interval until the integral
of that coefficient is small gives a contraction of the path integral
equation on each piece. The speed bound excludes escape and gives the
unique global absolutely continuous path. Differences of initial states
obey the integral Lipschitz estimate. Subtracting the linear variational
equation from their difference quotients, the Lipschitz derivative bounds
the remainder by a constant times the squared initial displacement.
This proves the stated Fréchet differentiability, with fixed control.

Reflect the two coordinates by \(s_1,s_2\), calling the results
\(x,y\), and put \(r=\rho s_1s_2\). Evenness of \(\phi'\) gives
\[
 (x,y)'=C_r(A,B)^T,\qquad
 A=\alpha\operatorname{sech}x,\quad B=\beta\operatorname{sech}y,
 \quad\alpha=|u_1|/10,\quad\beta=|u_2|/10.
\]
For a variational vector \(\zeta\), set
\(E=\zeta^TC_r^{-1}\zeta\). Direct differentiation yields
\[
 E'=2[-A\tanh x\,\zeta_1^2-B\tanh y\,\zeta_2^2]
 \le2hE,\qquad
 h=A f(x)+B f(y),\quad f(v)=(-\tanh v)_+.
\]
Here \(\zeta_i^2\le E\), by completing the square in the quadratic
form, and \(0\le f\le1\). Since the eigenvalues of \(C_r\) lie
between \(1-k\) and \(1+k\), integration proves
\[
 \|D_{z_0}z(T)\|_{\rm op}
 \le\sqrt{\frac{1+k}{1-k}}\exp(I),
 \qquad I=\int_0^Th(t)dt.
 \tag{H.4}
\]

For \(Q\ge1\), choose a continuous nonincreasing cutoff \(\chi\)
on \([0,\infty)\), equal to one up to one and zero from two onwards,
and put
\[
 f_Q(v)=f(v)\chi(v_-/Q),\qquad
 H_Q(v)=\begin{cases}\displaystyle\int_v^0 f_Q(w)dw,&v<0,\\0,&v\ge0.
 \end{cases}
\]
Then \(H_Q\in C^1\), \(H_Q'=-f_Q\), \(0\le H_Q\le2Q\).
The discarded part \(f-f_Q\) is supported where \(v<-Q\).
Using \(\operatorname{sech}v\le2e^{-|v|}\), its contribution to
\(I\) is at most \(2e^{-Q}U\).

If \(r\ge0\), differentiation gives
\((H_Q(x)+H_Q(y))'\le-[f_Q(x)A+f_Q(y)B]\).
Integration and nonnegativity of the final potential imply
\(I\le4Q+2e^{-Q}U\).
If \(r=-k<0\), the exact identity is
\[
 (H_Q(x)+H_Q(y))'
 =-[f_Q(x)A+f_Q(y)B]+k[f_Q(x)B+f_Q(y)A].
 \tag{H.5}
\]
On the central set \(\{|x|,|y|\le2Q\}\) the last bracket is at most
\(A+B\). Also \(w=x+y\) is nondecreasing and
\(w'=(1-k)(A+B)\). This central set lies in \(\{|w|\le4Q\}\),
so
\[
 \int_{\{|x|,|y|\le2Q\}}(A+B)dt\le\frac{8Q}{1-k}.
 \tag{H.6}
\]
To check this also for flat segments and arbitrary integrable controls,
clamp the absolutely continuous \(w\) to \([-4Q,4Q]\).
The derivative is \(w'\) on the open strip and zero outside.
On each boundary level set \(w'=0\) almost everywhere: at a density
point where \(w\) is differentiable, difference quotients through
that level set force the derivative to be zero. Integration therefore
bounds the total closed-strip derivative by the clamped increase \(8Q\).

Outside the central set, \(f_Q(x)\ne0\) implies \(-2Q<x<0\),
so \(|y|>2Q\) and \(f_Q(x)B\le2\beta e^{-2Q}\).
The symmetric term obeys the same bound with \(\alpha\). Thus the
outside contribution of the bracket in (H.5) is at most \(2e^{-2Q}U\).
Integrating (H.5), and using the initial potential bound \(4Q\), gives
\[
 I\le\left(4+\frac{8k}{1-k}\right)Q
       +2k e^{-2Q}U+2e^{-Q}U.
 \tag{H.7}
\]
Set \(Q=2\log(e+U)\ge2\). Both exponential tail factors times
\(U\) are at most one. Hence
\[
 I\le4+\frac{16}{1-k}\log(e+U).
\]
This includes the \(r\ge0\) estimate and proves (H.2) through (H.4).

Consequently a measurable random control and initial point satisfying
the same pathwise sign premise have finite \(q\)-th frozen-control
tangent moment whenever \(E(e+U)^{16q/(1-k)}<\infty\).
No independence from the initial point is needed. This conclusion does
not establish those control moments or fixed signs in a trained network,
and it does not bound variations of the control caused by feedback.


### I. A first-Euler neighborhood obstruction for tiny-readout arctangent

Fix one sample and label both equal to one, three hidden layers, and
\(\phi=\arctan\). Use independent first coordinates
\(z^{(1)}_{0,i}\sim N(0,1)\), adjacent entries
\(W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n)\), and the raw metric
\[
 \|\Delta z^{(1)}\|_2^2/n+\|\Delta W^{(2)}\|_F^2
 +\|\Delta W^{(3)}\|_F^2+\|\Delta W^{(4)}\|_2^2/n.
\]
The finite stored readout in the tiny-readout model has independent
\(N(0,n^{-2})\) entries. The auxiliary first-step state studied here
sets that readout exactly to zero, as in its population oracle; the
nonzero finite Gaussian-readout state is not substituted for it.
The predictor is \(f_n=(W^{(4)})^Th^{(3)}/n\), the residual is
\(r_n=f_n-1\), and the loss is \(r_n^2\). The raw field is
\[
 \dot z^{(1)}=-2r_n\delta^{(1)},\qquad
 \dot W^{(\ell)}=-2r_n\delta^{(\ell)}(h^{(\ell-1)})^T/n
 \quad(\ell=2,3),\qquad
 \dot W^{(4)}=-2r_nh^{(3)},
\]
where the residual-free deltas use the actual transposes and activation
derivatives, as in the finite dynamics convention.

**Proposition.** Fix any auxiliary Euler step
\(0<\Delta<1/(4(\pi/2)^2)\). For every proposed width-independent
local Lipschitz constant, the raw field violates that constant at a pair
consisting of this first-step state and a state at vanishing distance from
it, with probability tending to one. The distance is the transformed
first-coordinate RMS, adjacent operator norms and readout RMS displayed
at the end of the proof. The threshold is selected before the width limit.
This is a fixed-mesh neighborhood statement, with no continuous-trajectory
or Osgood-uniqueness conclusion.

**Proof.** Put \(c=\pi/2\).
For this argument only, set the readout exactly to zero initially, as in the population oracle. Keep exactly the Gaussian first layer and hidden matrices specified above. After one Euler step of size \(\Delta>0\), the hidden parameters have not changed and
\[
W_1^{(4)}=2\Delta\phi(z_0^{(3)}),\quad
\delta_1^{(3)}=2\Delta\phi(z_0^{(3)})\odot\phi'(z_0^{(3)}).
\]
Choose \(0<\Delta<1/(4c^2)\). Then the residual at this state lies in \([-1,-1/2]\), because \(f_{n,1}=2\Delta\|h_0^{(3)}\|_2^2/n\le2\Delta c^2<1/2\).

Conditioning Gaussian rows of \(W_0^{(3)}\) on \(W_0^{(3)}h_0^{(2)}=z_0^{(3)}\) gives the exact conditional law
\[
(W_0^{(3)})^\top\delta_1^{(3)}
\overset d=
\frac{(z_0^{(3)})^\top\delta_1^{(3)}}{\|h_0^{(2)}\|_2^2}h_0^{(2)}
+\frac{\|\delta_1^{(3)}\|_2}{\sqrt n}
\left(I-\frac{h_0^{(2)}(h_0^{(2)})^\top}{\|h_0^{(2)}\|_2^2}\right)\gamma,
\]
where \(\gamma\sim N(0,I_n)\) is independent of that history.

The following elementary averaging details show that this backward field has arbitrarily large coordinates where \(z_0^{(2)}\in[1,2]\). Let \(Z_0^{(1)}\sim N(0,1)\), \(H_0^{(1)}=\phi(Z_0^{(1)})\); let \(Z_0^{(2)}\) be centered Gaussian of variance \(\mathbb E[(H_0^{(1)})^2]>0\), and set \(H_0^{(2)}=\phi(Z_0^{(2)})\). Let \(Z_0^{(3)}\) be centered Gaussian of variance \(\mathbb E[(H_0^{(2)})^2]>0\), and \(D=2\Delta\phi(Z_0^{(3)})\phi'(Z_0^{(3)})\). Conditional laws of large numbers for the two fresh forward calls give
\[
\frac{(z_0^{(3)})^\top\delta_1^{(3)}}{\|h_0^{(2)}\|_2^2}\longrightarrow
\frac{\mathbb E[Z_0^{(3)}D]}{\mathbb E[(H_0^{(2)})^2]}=:b,\qquad
\frac{\|\delta_1^{(3)}\|_2^2}{n}\longrightarrow\mathbb E[D^2]=:\sigma^2>0.
\]
The removed projection has normalized squared norm converging to zero: its conditional expectation is \(1/n\). Conditional averaging over \(\gamma\) therefore proves joint empirical convergence of
\[
\left(z_{0,j}^{(2)},\big[(W_0^{(3)})^\top\delta_1^{(3)}\big]_j\right)
\quad\hbox{to}\quad
\left(Z_0^{(2)},b\phi(Z_0^{(2)})+\sigma G\right),
\]
where \(G\sim N(0,1)\) is independent of \(Z_0^{(2)}\). Every set
\(\{1\le Z_0^{(2)}\le2,\ b\phi(Z_0^{(2)})+\sigma G>A\}\), for fixed \(A>0\), has positive probability and boundary probability zero. Consequently, for every fixed \(A\), with probability tending to one there is an index \(j\) in this set's finite-coordinate counterpart.

Localize to the event that both hidden operator norms are at most a fixed \(M\), and \(\|h_0^{(1)}\|_2/\sqrt n\) is bounded above and bounded away from zero. Its probability tends to one for sufficiently large fixed \(M\). Choose such an index \(j\), take \(A\ge1\), and perturb only the second weight matrix by
\[
\Delta W^{(2)}=\frac{A^{-1}e_j(h_0^{(1)})^\top}{\|h_0^{(1)}\|_2^2}.
\]
This changes \(z^{(2)}\) by exactly \(A^{-1}e_j\) and has operator norm
\[
\|\Delta W^{(2)}\|_{\rm op}=\frac{1}{A\|h_0^{(1)}\|_2}.
\]
On \([1,3]\), \(-\phi''\) is bounded below by a positive constant \(m\). Keeping the old backward field in the gate difference yields a coordinate of magnitude at least
\[
m A^{-1}\big[(W_0^{(3)})^\top\delta_1^{(3)}\big]_j\ge m.
\]
The backward field itself changes by at most \(C/(A\sqrt n)\) in normalized Euclidean norm. Indeed its expression is
\[
(W_0^{(3)})^\top\left[W_1^{(4)}\odot\phi'\!\left(W_0^{(3)}\phi(z^{(2)})\right)\right],
\]
and \(W_1^{(4)}\) is bounded coordinatewise, both activations are Lipschitz, and the operator norm of \(W_0^{(3)}\) is bounded. Therefore
\[
\frac{\|\delta^{(2)}_{\rm perturbed}-\delta^{(2)}_{\rm original}\|_2}{\sqrt n}
\ge\frac{m-C/A}{\sqrt n}.
\]
The residual changes by at most \(C/(A\sqrt n)\), and the normalized norm of the original \(\delta^{(2)}\) is bounded. Since \(|r_{n,1}|\ge1/2\), the second-matrix velocity difference consequently satisfies
\[
\|\dot W^{(2)}_{\rm perturbed}-\dot W^{(2)}_{\rm original}\|_{\rm op}
\ge\frac{c_1-C_1/A}{\sqrt n},
\]
with \(c_1>0\) independent of \(A,n\). Dividing by \(\|\Delta W^{(2)}\|_{\rm op}\) gives a lower bound \(c_2 A-C_2\). The constants depend on the fixed localization and \(\Delta\), not on \(A,n\).

Given any proposed width-independent Lipschitz constant, first choose \(A\) large enough, then let \(n\to\infty\). The perturbation tends to zero and the displayed ratio exceeds that constant with probability tending to one. Thus no width-uniform local-Lipschitz estimate in the state distance
\[
\frac{\|\Delta x^{(1)}\|_2}{\sqrt n}
+\|\Delta W^{(2)}\|_{\rm op}
+\|\Delta W^{(3)}\|_{\rm op}
+\frac{\|\Delta W^{(4)}\|_2}{\sqrt n},\qquad x^{(1)}=z^{(1)}+(z^{(1)})^3/3,
\]
can hold on these neighborhoods. This rules out a width-uniform local Lipschitz estimate on those neighborhoods. It is not a failure of finite-dimensional smoothness, and it does not imply nonuniqueness or failure of the infinite-width limit.

