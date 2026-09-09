# Metric-projection gate stability: negative result

Status: independent, theory-only derivation. Unverified for adoption until a separate audit. This document concerns finite-dimensional and width-varying state/mapping tests only; it makes no assertion about global dynamics, energy, or a prescribed Gaussian trained trajectory.

For every \(R>0\), the proposed uniform Lipschitz bound is false. It fails for a fixed \(2\times2\) positive-definite matrix with fixed spectral bounds. It also fails within the stated canonical lower-mobility family, even along feedforward-consistent states for which the mobility matrix remains exactly fixed and \(\|W^{(2)}\|_{\mathrm{op}}\) remains constant. The Lipschitz bound in \(q\), with the metric fixed, does hold.

The proof first records the projection optimality conditions and the valid \(q\) estimate, then gives an explicit finite-difference counterexample. A second construction embeds it in the canonical family. Section 5 extends the result to complete algebraic network states on fixed normalized primal norm bounds: the full state distance is of order \(1/n\), but the projected layer-2 field difference divided by \(\sqrt n\) is of order \(1/\sqrt n\). All layer indices and normalization factors are explicit.

## 1. Setup and the valid bound in q

Let \(n\geq1\), \(R>0\), and \(0<c\leq C<\infty\). Write

\[
K_R=[-R,R]^n,\qquad \phi(s)=\arctan s,\qquad \phi'(s)=\frac1{1+s^2},\qquad
F_M(z,q)=P_M(\phi'(z)\odot q),
\]

where \(z,q\in\mathbb R^n\), \(M=M^T\), and \(cI\preceq M\preceq CI\). The Euclidean norm on pairs is \(\|(z,q)\|_2=(\|z\|_2^2+\|q\|_2^2)^{1/2}\).

The objective is continuous on the compact, nonempty box, so a minimizer exists. Positive definiteness makes it strictly convex, so that minimizer is unique. For \(u\in K_R\), its optimality condition is

\[
u=P_M(d)
\quad\Longleftrightarrow\quad
\langle M(u-d),v-u\rangle\geq0\quad\text{for every }v\in K_R.
\tag{1}
\]

Necessity follows by differentiating the objective along the feasible segment from \(u\) to \(v\). Sufficiency follows from the exact objective difference

\[
\frac12(v-d)^TM(v-d)-\frac12(u-d)^TM(u-d)
=\langle M(u-d),v-u\rangle+\frac12(v-u)^TM(v-u).
\]

Apply (1) to \(u=P_M(d)\), \(\widetilde u=P_M(\widetilde d)\), using each point as the other's comparison point. Put \(e=u-\widetilde u\) and \(r=d-\widetilde d\). Adding the resulting inequalities and applying Cauchy--Schwarz to \(M^{1/2}r,M^{1/2}e\) gives

\[
e^TMe\leq r^TMe\leq (r^TMr)^{1/2}(e^TMe)^{1/2}.
\]

If \(e\neq0\), division and squaring yield \(e^TMe\leq r^TMr\); for \(e=0\) this inequality also holds. Thus \(c\|e\|_2^2\leq C\|r\|_2^2\), proving

\[
\|P_M(d)-P_M(\widetilde d)\|_2
\leq\sqrt{C/c}\,\|d-\widetilde d\|_2.
\tag{2}
\]

Since \(0<\phi'(s)\leq1\), this yields the dimension-independent estimate

\[
\|F_M(z,q)-F_M(z,\widetilde q)\|_2
\leq\sqrt{C/c}\,\|q-\widetilde q\|_2.
\tag{3}
\]

In particular, the permitted constant \(C/c\) also works. These estimates compare projections in the same metric.

## 2. An explicit fixed-matrix counterexample

The following two-coordinate formula will be used below. Suppose

\[
M=\begin{pmatrix}\alpha&b\\b&m\end{pmatrix}\succ0,
\qquad \beta=b/m,
\qquad S=\alpha-b^2/m>0.
\]

Whenever \(d_1>R\) and \(|d_2+\beta(d_1-R)|<R\), set

\[
u=\bigl(R,\ d_2+\beta(d_1-R)\bigr).
\tag{4}
\]

Then

\[
M(u-d)=\bigl(S(R-d_1),0\bigr).
\]

The first component is negative. Every feasible \(v\) has \(v_1-R\leq0\), so (1) holds, and (4) is exactly \(P_M(d)\). Thus a change in the raw input of the saturated first coordinate enters the free second coordinate with coefficient \(\beta\).

Now fix any \(0<c<C\), and take the single, parameter-independent matrix

\[
M=\begin{pmatrix}m&b\\b&m\end{pmatrix},\qquad
m=\frac{C+c}{2},\quad b=\frac{C-c}{2},\quad
\beta=\frac{C-c}{C+c}\in(0,1).
\tag{5}
\]

Its eigenvalues are exactly \(c,C\). For each real \(t\geq2\), compare inputs

\[
z=(1,0),\qquad \widetilde z_t=(1+1/t,0),\qquad
q_t=\bigl(2Rt,-\beta R(t-1)\bigr).
\tag{6}
\]

The same \(q_t\) is used at both points. At the first point,

\[
d=\phi'(z)\odot q_t=\bigl(Rt,-\beta R(t-1)\bigr),
\qquad F_M(z,q_t)=(R,0)
\tag{7}
\]

by (4). At the second point define

\[
k_t=\frac{1+1/(2t)}{1+1/t+1/(2t^2)}.
\]

Direct substitution gives

\[
\widetilde d_1
=\frac{2Rt}{1+(1+1/t)^2}
=\frac{Rt}{1+1/t+1/(2t^2)}
=Rt-Rk_t,
\qquad \widetilde d_2=d_2.
\]

Here \(0<k_t<1\), because the denominator exceeds the numerator by \(1/(2t)+1/(2t^2)>0\), and \(k_t\to1\). Consequently

\[
\widetilde d_1>R(t-1)\geq R,
\qquad
\widetilde d_2+\beta(\widetilde d_1-R)=-\beta Rk_t\in(-R,0).
\]

Formula (4) therefore proves, without any limiting active-set assumption,

\[
F_M(\widetilde z_t,q_t)=(R,-\beta Rk_t).
\tag{8}
\]

The exact Lipschitz quotient is

\[
\frac{\|F_M(\widetilde z_t,q_t)-F_M(z,q_t)\|_2}
{\|(\widetilde z_t,q_t)-(z,q_t)\|_2}
=\frac{\beta Rk_t}{1/t}
=\beta Rt k_t\longrightarrow\infty.
\tag{9}
\]

Thus there is no finite global Lipschitz constant even for this one fixed matrix and \(n=2\). In particular, no constant depending only on \(c,C,R\), and no \(z\)-constant of the form \(K(c,C)R\), can work. The construction works for every nontrivial spectral interval \(c<C\). For the especially simple choice \(c=1/2,C=3/2\), the matrix is \(\left(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right)\) and \(\beta=1/2\).

The obstruction is visible at (7): the free output is \(u_2=0\), but its raw input \(d_2=-\beta R(t-1)\) is unbounded. The free-coordinate equation permits cancellation between large raw inputs. Bounding a free projected coordinate therefore does not bound its raw input, and changing a saturated coordinate's gate can change a free output.

## 3. Exact fixed-metric boundary and useful limitations

For \(R>0\) and a fixed positive-definite \(M\), the map \(F_M\) is globally Lipschitz on all of \(\mathbb R^n\times\mathbb R^n\) if and only if \(M\) is diagonal.

For the diagonal direction, the objective separates, and

\[
[F_M(z,q)]_i=\operatorname{clip}_{[-R,R]}(\phi'(z_i)q_i).
\]

For a fixed scalar \(q_i\), this is absolutely continuous on every bounded \(z_i\)-interval: \(\phi'(z_i)q_i\) is smooth there, and clipping is Lipschitz. At almost every unsaturated point its derivative in \(z_i\) satisfies

\[
|\phi''(z_i)q_i|
=\left|\frac{\phi''(z_i)}{\phi'(z_i)}\right||\phi'(z_i)q_i|
\leq R,
\qquad
\left|\frac{\phi''(s)}{\phi'(s)}\right|=\frac{2|s|}{1+s^2}\leq1.
\]

At saturated interior points the derivative is zero. Integrating the almost-everywhere bound proves the scalar \(R\)-Lipschitz estimate. Clipping and multiplication by \(\phi'(z_i)\leq1\) give the scalar 1-Lipschitz estimate in \(q_i\). Summing squares coordinatewise and then using the triangle inequality gives

\[
\|F_M(z,q)-F_M(\widetilde z,\widetilde q)\|_2
\leq R\|z-\widetilde z\|_2+\|q-\widetilde q\|_2.
\tag{10}
\]

The corresponding joint product-norm constant is \(\sqrt{R^2+1}\). This includes \(M=I\), \(n=1\), and the case \(c=C\), where the spectral bounds force \(M=cI\).

For the converse, let \(M\) have a nonzero off-diagonal entry. Choose an index \(i\) such that \(M_{Fi}\neq0\), where \(F\) is the complementary index set, and define

\[
v=M_{FF}^{-1}M_{Fi}\neq0,
\qquad S=M_{ii}-M_{iF}M_{FF}^{-1}M_{Fi}>0.
\]

The principal block is positive definite. The positivity of \(S\) follows by evaluating the quadratic form of \(M\) on the vector with \(i\)-coordinate 1 and \(F\)-coordinates \(-v\).

Set \(z_i=1,z_F=0,q_i=2Rt,q_F=-vR(t-1)\) for \(t>1\). Then \(d_i=Rt,d_F=-vR(t-1)\), and \(u_i=R,u_F=0\) satisfies (1), since the gradient has \(i\)-coordinate \(S(R-d_i)<0\) and vanishes on \(F\). Perturb only \(z_i\) to \(1+h\), keeping this \(q\) fixed. For each fixed \(t\), continuity ensures that, on an interval around \(h=0\), \(d_i(h)>R\) and

\[
u_i(h)=R,\qquad u_F(h)=d_F+v(d_i(h)-R)\in(-R,R)^{|F|}.
\]

The same gradient calculation proves this is the projection throughout that interval. Since \(d_i(h)=2Rt/[1+(1+h)^2]\),

\[
u_F'(0)=-Rt\,v.
\]

A global Lipschitz constant would have to be at least \(Rt\|v\|_2\) for every \(t>1\), which is impossible. This proves the converse, including arbitrarily weak but nonzero coupling.

For a fixed width, the failure uses unbounded \(q\). A uniform coordinate bound, rather than merely a bound on \(\|q\|_2/\sqrt n\), restores the following dimension-independent estimate. On a domain with \(\|q\|_\infty,\|\widetilde q\|_\infty\leq Q\), the elementary bound \(|\phi''(s)|\leq1\), coordinatewise multiplication, and (2) give the valid correction

\[
\|F_M(z,q)-F_M(\widetilde z,\widetilde q)\|_2
\leq\sqrt{C/c}\left(Q\|z-\widetilde z\|_2+\|q-\widetilde q\|_2\right).
\tag{11}
\]

Thus the issue is global uniformity in \(q\), not existence of the projection or local Lipschitz continuity. If \(R=0\), the projection is identically zero and all counterexamples disappear. A negative \(R\) does not define a nonempty box.

## 4. Canonical lower-mobility embedding with the layer indices preserved

Use width \(n=2\). The lower-layer state is \(z^{(1)}\), the matrix from layer 1 to layer 2 is \(W^{(2)}\), and the gate being tested is at layer 2:

\[
M^{(2)}=c_1I+W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T,
\quad c_1=\frac{\|\phi(z^{(1)})\|_2^2}{2},
\quad d^{(2)}=\phi'(z^{(2)})\odot q^{(2)}.
\tag{12}
\]

Here \(q^{(2)}\in\mathbb R^2\) denotes the arbitrary signal \(q\) in the question, now labeled by the layer whose gate it multiplies. No restriction on how an upper layer might generate \(q^{(2)}\) is assumed.

Fix

\[
z^{(1)}=(1,1),\qquad c_1=\frac{\pi^2}{16},\qquad
\operatorname{diag}(\phi'(z^{(1)})^2)=\frac14I,
\qquad
W^{(2)}_0=\begin{pmatrix}0&4/\pi\\-2/\pi&2/\pi\end{pmatrix}.
\tag{13}
\]

Let

\[
Q_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
\qquad W^{(2)}(\theta)=W^{(2)}_0Q_\theta.
\]

Since \(Q_\theta Q_\theta^T=I\), the mobility matrix is exactly independent of \(\theta\):

\[
M^{(2)}(\theta)=M^{(2)}
=c_1I+\frac14W^{(2)}_0(W^{(2)}_0)^T
=\begin{pmatrix}
c_1+4/\pi^2&2/\pi^2\\
2/\pi^2&c_1+2/\pi^2
\end{pmatrix}.
\tag{14}
\]

The eigenvalues of the added matrix are \((3\pm\sqrt5)/\pi^2\), obtained from the trace \(6/\pi^2\) and determinant \(4/\pi^4\). Accordingly, fixed exact spectral bounds and a fixed operator norm are

\[
c=\frac{\pi^2}{16}+\frac{3-\sqrt5}{\pi^2}>0,
\qquad C=\frac{\pi^2}{16}+\frac{3+\sqrt5}{\pi^2},
\qquad \|W^{(2)}(\theta)\|_{\mathrm{op}}^2=\frac{4(3+\sqrt5)}{\pi^2}.
\tag{15}
\]

This does not exploit a vanishing \(c_1\), worsening conditioning, increasing width, or growing lower-layer weights.

It already places a fixed coupled metric in the canonical class. Moreover, the following construction also satisfies the additional feedforward relation \(z^{(2)}=W^{(2)}\phi(z^{(1)})\) at every comparison point. Because \(\phi(z^{(1)})=(\pi/4,\pi/4)\), direct multiplication gives

\[
z^{(2)}(\theta)=W^{(2)}(\theta)\phi(z^{(1)})
=(\cos\theta+\sin\theta,\sin\theta),
\qquad z^{(2)}(0)=(1,0).
\tag{16}
\]

For the matrix (14), the coefficient in the projection formula (4) is

\[
\beta=\frac{2/\pi^2}{c_1+2/\pi^2}
=\frac{32}{\pi^4+32}\in(0,1).
\]

For \(t\geq2\), use the same upper signal at both states,

\[
q^{(2)}_t=(2Rt,-\beta R(t-1)),
\]

and compare \(\theta=0\) with \(\theta=1/t\). At zero, (4) gives

\[
P_{M^{(2)}}\bigl(\phi'(z^{(2)}(0))\odot q^{(2)}_t\bigr)=(R,0).
\tag{17}
\]

For the other endpoint put \(s_t=\sin(1/t)\) and \(r_t=\cos(1/t)\). The identity \((r_t+s_t)^2=1+2s_tr_t\) yields the two coordinates of the raw layer-2 input:

\[
(d^{(2)})_1=\frac{Rt}{1+s_tr_t},\qquad
(d^{(2)})_2=-\frac{\beta R(t-1)}{1+s_t^2}.
\tag{18}
\]

Define the nonnegative scalars

\[
A_t=\frac{t s_tr_t}{1+s_tr_t},\qquad
B_t=\frac{(t-1)s_t^2}{1+s_t^2}.
\]

Substitution into the free-coordinate formula gives

\[
(d^{(2)})_2+\beta((d^{(2)})_1-R)=\beta R(B_t-A_t).
\tag{19}
\]

All active-set conditions can be checked for every \(t\geq2\). Indeed \(0<s_tr_t<1/t\), hence

\[
(d^{(2)})_1>\frac{Rt}{1+1/t}=\frac{Rt^2}{t+1}>R,
\qquad 0<A_t<1.
\]

Also \(0<B_t<(t-1)/t^2<1\), using \(0<\sin(1/t)<1/t\). Thus \(|B_t-A_t|<1\) and the value in (19) lies strictly inside \((-R,R)\). Formula (4) applies exactly and proves

\[
P_{M^{(2)}}\bigl(\phi'(z^{(2)}(1/t))\odot q^{(2)}_t\bigr)
=(R,\beta R(B_t-A_t)).
\tag{20}
\]

Differentiability of sine at zero gives \(t\sin(1/t)\to1\); continuity of cosine gives \(\cos(1/t)\to1\). Consequently \(A_t\to1\). The bound \(0<B_t<(t-1)/t^2\) gives \(B_t\to0\). The projected-output distance therefore tends to the strictly positive number \(\beta R\).

Meanwhile

\[
\|z^{(2)}(1/t)-z^{(2)}(0)\|_2
=\sqrt{(r_t+s_t-1)^2+s_t^2},
\qquad
t\|z^{(2)}(1/t)-z^{(2)}(0)\|_2\longrightarrow\sqrt2.
\]

For the last limit, \(t s_t\to1\) and \(t(r_t-1)\to0\), the latter following from differentiability of cosine at zero. The signal difference is zero, so the joint-input Lipschitz quotient has the asymptotic behavior

\[
\frac{\left\|P_{M^{(2)}}(\phi'(z^{(2)}(1/t))\odot q^{(2)}_t)
-P_{M^{(2)}}(\phi'(z^{(2)}(0))\odot q^{(2)}_t)\right\|_2}
{\|(z^{(2)}(1/t),q^{(2)}_t)-(z^{(2)}(0),q^{(2)}_t)\|_2}
\sim\frac{\beta Rt}{\sqrt2}\longrightarrow\infty.
\tag{21}
\]

The metric in (21) is the same fixed matrix at both endpoints and for every \(t\).

The counterexample also persists if the input norm includes the varying matrix \(W^{(2)}\) as a state variable. In the Euclidean norm on its entries,

\[
\|W^{(2)}(1/t)-W^{(2)}(0)\|_F
\leq\|W^{(2)}_0\|_F\|Q_{1/t}-I\|_{\mathrm{op}}
=2\|W^{(2)}_0\|_F\sin(1/(2t))
\leq\frac{\|W^{(2)}_0\|_F}{t}.
\]

Here the rotation identity follows by expanding \((Q_\theta-I)^T(Q_\theta-I)=4\sin^2(\theta/2)I\). The lower state \(z^{(1)}\) is unchanged, the upper signal is unchanged within each comparison, and the changes of both \(z^{(2)}\) and \(W^{(2)}\) tend to zero. The output separation still tends to \(\beta R>0\).

## 5. Complete width-varying algebraic states on fixed normalized primal bounds

The proposed extension is valid. In this section fix \(R=1\), \(\rho=1/4\), and let the integer width \(n\geq4\) vary. The two states at each width share the same \(q^{(2)}\), the same canonical mobility, and the same third-layer weight matrix. Their readout vectors are different but close in the normalized Euclidean norm.

### 5.1 Forward, backward, and norm conventions

All vector norms below are ordinary Euclidean norms \(\|\cdot\|_2\). Matrix norms are the ordinary operator and Frobenius norms. Every normalization is written as an explicit factor \(1/n\) or \(1/\sqrt n\).

Take the single scalar input \(x=1\) and vector \(W^{(1)}=\mathbf1_n\in\mathbb R^n\). Thus \(z^{(1)}=W^{(1)}=\mathbf1_n\) and \(\|z^{(1)}\|_2/\sqrt n=1\). Define the network state by

\[
z^{(1)}=W^{(1)}x,\qquad
h^{(\ell)}=\phi(z^{(\ell)})\quad(\ell=1,2,3),
\qquad
z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\quad(\ell=2,3),
\]
\[
f=\frac1n(W^{(4)})^Th^{(3)},\qquad W^{(4)}\in\mathbb R^n.
\tag{22}
\]

The raw backward fields (with the residual excluded) and the projected field under examination are

\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
d^{(2)}=\phi'(z^{(2)})\odot q^{(2)},
\]
\[
u_R^{(2)}=P_{M^{(2)}}(d^{(2)}),\qquad
M^{(2)}=c_1I+
W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T,
\quad
c_1=\frac{\|h^{(1)}\|_2^2}{n}.
\tag{23}
\]

With the weights held fixed when taking partial derivatives, these conventions give \(\delta^{(3)}=n\nabla_{z^{(3)}}f\), \(q^{(2)}=n\nabla_{h^{(2)}}f\), and \(d^{(2)}=n\nabla_{z^{(2)}}f\). The projection in (23) is applied to this raw backward field with the residual excluded, without an extra factor \(1/n\) inside the projection.

### 5.2 Exact column rotation and unchanged mobility

Put \(c_0=\pi/4\), \(m=n-2\), and

\[
z^{(1)}=\mathbf1_n,\qquad h^{(1)}=c_0\mathbf1_n,\qquad
c_1=c_0^2,\qquad
\operatorname{diag}(\phi'(z^{(1)})^2)=\frac14I_n.
\]
\[
B=\begin{pmatrix}0&4/\pi\\-2/\pi&2/\pi\end{pmatrix},
\qquad
W^{(2)}_0=\operatorname{blockdiag}(B,I_m),
\qquad
a_n=\frac{(0,0,1,\ldots,1)^T}{\sqrt m},\quad b=e_2.
\]

Here \(a_n,b\) are orthonormal vectors. Choose the rotation orientation

\[
Q_\alpha a_n=\cos\alpha\,a_n+\sin\alpha\,b,\qquad
Q_\alpha b=\cos\alpha\,b-\sin\alpha\,a_n,
\]
\[
Q_\alpha=I_n+(\cos\alpha-1)(a_na_n^T+bb^T)
+\sin\alpha(ba_n^T-a_nb^T),
\qquad W^{(2)}(\alpha)=W^{(2)}_0Q_\alpha.
\tag{24}
\]

The rotation fixes the orthogonal complement of this plane, including \(e_1\). Since \(\mathbf1_n=e_1+b+\sqrt m\,a_n\),

\[
Q_\alpha h^{(1)}
=c_0\{e_1+(\cos\alpha+\sqrt m\sin\alpha)b
+(\sqrt m\cos\alpha-\sin\alpha)a_n\}.
\]

Consequently, with

\[
L_n(\alpha)=\cos\alpha+\sqrt m\sin\alpha,\qquad
T_n(\alpha)=\cos\alpha-\frac{\sin\alpha}{\sqrt m},
\]

the forward state is exactly

\[
z^{(2)}(\alpha)
=\left(L_n(\alpha),\frac{L_n(\alpha)-1}{2},
c_0T_n(\alpha),\ldots,c_0T_n(\alpha)\right)^T.
\tag{25}
\]

Orthogonality of \(Q_\alpha\) and the scalar first-layer gate imply

\[
M^{(2)}(\alpha)=M_n
=\operatorname{blockdiag}\left(
\begin{pmatrix}
c_0^2+4/\pi^2&2/\pi^2\\
2/\pi^2&c_0^2+2/\pi^2
\end{pmatrix},
(c_0^2+1/4)I_m\right).
\tag{26}
\]

In particular the mobility is exactly preserved, even though the column rotation mixes a rare column with the bulk. Its rare block is precisely (14). Put

\[
K_2=\max\left\{1,\frac{2\sqrt{3+\sqrt5}}{\pi}\right\},\qquad
\beta=\frac{2/\pi^2}{c_0^2+2/\pi^2}
=\frac{32}{\pi^4+32}\in(0,1).
\]

Then uniformly in \(n,\alpha\),

\[
\|W^{(2)}(\alpha)\|_{\mathrm{op}}=K_2,\qquad
c_0^2 I_n\preceq M_n\preceq(c_0^2+K_2^2/4)I_n.
\tag{27}
\]

These fixed, nondegenerate constants suffice; the exact spectrum consists of \(c_0^2+(3\pm\sqrt5)/\pi^2\) and \(c_0^2+1/4\).

Compare \(\alpha=0\) with \(\alpha_n=1/n\). Define

\[
x_n=L_n(1/n)-1,\qquad T_n=T_n(1/n).
\]

For every \(n\geq4\),

\[
0<x_n<\frac{\sqrt m}{n}<\frac1{\sqrt n},\qquad
\sqrt n\,x_n\longrightarrow1,\qquad
0<T_n<1,
\]
\[
|T_n-1|\leq\frac1{2n^2}+\frac1{n\sqrt m}.
\tag{28}
\]

For positivity of \(x_n\), write
\(x_n=\sin(1/n)\{\sqrt m-\tan(1/(2n))\}>0\).
The upper bound uses \(\sin u<u\) and \(\cos u<1\).
The limit follows from \(n\sin(1/n)\to1\), \(1-\cos(1/n)\leq1/(2n^2)\), and \(m/n\to1\).
The displayed bound on \(T_n-1\) follows from these same trigonometric inequalities, and gives \(T_n>0\) for \(n\geq4\).

The Frobenius size of the weight change has an exact formula:

\[
\|W^{(2)}(1/n)-W^{(2)}(0)\|_F^2
=4\sin^2(1/(2n))\left(1+\frac{20}{\pi^2}\right).
\tag{29}
\]

Indeed \((Q_\alpha-I)(Q_\alpha-I)^T
=4\sin^2(\alpha/2)(a_na_n^T+bb^T)\).
Taking its trace against \((W^{(2)}_0)^TW^{(2)}_0\) gives (29), because
\(\|W^{(2)}_0a_n\|_2^2=1\) and
\(\|W^{(2)}_0b\|_2^2=20/\pi^2\).
Thus the unnormalized Frobenius change is of order \(1/n\), without an extraneous \(\sqrt n\) from bounding the entire weight matrix in Frobenius norm.

Writing \(\Delta\) for perturbed minus base state, (25) also gives

\[
\|\Delta z^{(2)}\|_2^2
=\frac54x_n^2+m c_0^2(T_n-1)^2,\qquad
n\,\frac{\|\Delta z^{(2)}\|_2}{\sqrt n}\longrightarrow\frac{\sqrt5}{2}.
\tag{30}
\]

The bulk term multiplied by \(n\) tends to zero by (28). Since \(|\phi'|\leq1\), \(\|\Delta h^{(2)}\|_2/\sqrt n\leq\|\Delta z^{(2)}\|_2/\sqrt n=O(1/n)\).

### 5.3 Exact projected field and active-set margins

Use the same vector at both states,

\[
q^{(2)}_n=
\left(2\sqrt n,-\beta(\sqrt n-1),\rho,\ldots,\rho\right)^T.
\tag{31}
\]

Its normalized squared Euclidean norm is

\[
\frac{\|q^{(2)}_n\|_2^2}{n}
=4+\beta^2(1-1/\sqrt n)^2+\rho^2(1-2/n)
\leq4+\beta^2+\rho^2.
\tag{32}
\]

At the base state the rare raw input is
\((\sqrt n,-\beta(\sqrt n-1))\), so its projection is \((1,0)\).
Every bulk raw input is \(\rho/(1+c_0^2)<1\), hence remains free.

At \(\alpha=1/n\), (25) gives

\[
(d^{(2)})_1=\frac{\sqrt n}{1+x_n+x_n^2/2},\qquad
(d^{(2)})_2=-\frac{\beta(\sqrt n-1)}{1+x_n^2/4},\qquad
(d^{(2)})_j=\frac{\rho}{1+c_0^2T_n^2}\quad(j\geq3).
\tag{33}
\]

Put

\[
A_n=\frac{\sqrt n(x_n+x_n^2/2)}{1+x_n+x_n^2/2},\qquad
E_n=\frac{(\sqrt n-1)x_n^2/4}{1+x_n^2/4}.
\]

The exact free-coordinate candidate from (4) is

\[
(d^{(2)})_2+\beta((d^{(2)})_1-1)=\beta(E_n-A_n).
\tag{34}
\]

All active-set conditions hold for every \(n\geq4\). To see this, (28) gives

\[
0<A_n<\sqrt n\,x_n<1,\qquad
0<E_n<\frac1{4\sqrt n}<1,\qquad
(d^{(2)})_1=\sqrt n-A_n>\sqrt n-1\geq1.
\]

The strict bound on \(A_n\) uses
\((1+x_n/2)/(1+x_n+x_n^2/2)<1\).
Thus \(|\beta(E_n-A_n)|<\beta<1\).
The rare free coordinate has a uniform distance at least \(1-\beta\) from either box boundary; every bulk coordinate is at most \(\rho\), with distance at least \(1-\rho\) from the upper boundary. The first rare coordinate is at its upper bound and has a strictly negative gradient component as in (4). Because (26) is block diagonal, these blockwise checks establish the full projection:

\[
u_R^{(2)}(0)=\left(1,0,\frac{\rho}{1+c_0^2},\ldots,\frac{\rho}{1+c_0^2}\right)^T,
\]
\[
u_R^{(2)}(1/n)
=\left(1,\beta(E_n-A_n),
\frac{\rho}{1+c_0^2T_n^2},\ldots,\frac{\rho}{1+c_0^2T_n^2}\right)^T.
\tag{35}
\]

Now \(A_n\to1\) by (28), while \(E_n\to0\). Also
\(|\phi''(s)|\leq1\), so the ordinary Euclidean norm of the bulk output difference is at most

\[
\sqrt m\,\rho c_0|T_n-1|
\leq\rho c_0\left(\frac{\sqrt m}{2n^2}+\frac1n\right)
=O(1/n).
\]

It follows that

\[
\|\Delta u_R^{(2)}\|_2\longrightarrow\beta,\qquad
\frac{\|\Delta u_R^{(2)}\|_2}{\sqrt n}\sim\frac{\beta}{\sqrt n}.
\tag{36}
\]

In particular, the normalized projected-field difference is at least
\(\beta/(2\sqrt n)\) for all sufficiently large \(n\).

### 5.4 Realizing the same raw backward field in complete upper layers

Let \(P_{\mathrm{bulk}}=\operatorname{diag}(0,0,1,\ldots,1)\), and set

\[
v_n=\left(2,-\beta(1-1/\sqrt n),0,\ldots,0\right)^T,
\qquad
W^{(3)}_n=\rho P_{\mathrm{bulk}}+\frac{\mathbf1_n v_n^T}{\sqrt n}.
\tag{37}
\]

This matrix is fixed across the two states. Its operator norm is bounded by

\[
\|W^{(3)}_n\|_{\mathrm{op}}
\leq\rho+\|v_n\|_2
\leq K_3:=\rho+\sqrt{4+\beta^2}.
\tag{38}
\]

Here the rank-one summand has operator norm \(\|v_n\|_2\), since
\(\|\mathbf1_n/\sqrt n\|_2=1\). The two summands have disjoint nonzero column sets, so their Frobenius inner product vanishes and

\[
\|W^{(3)}_n\|_F^2=\rho^2(n-2)+\|v_n\|_2^2.
\tag{39}
\]

At each endpoint separately, define the remaining primal variables by

\[
z^{(3)}(\alpha)=W^{(3)}_n\phi(z^{(2)}(\alpha)),\qquad
W^{(4)}_i(\alpha)=1+(z^{(3)}_i(\alpha))^2.
\tag{40}
\]

When computing the backward signals at a state, \(W^{(4)}\) is held fixed as a parameter. One does not differentiate its construction (40) along the family when taking these partial derivatives. Consequently

\[
\delta^{(3)}_i(\alpha)
=W^{(4)}_i(\alpha)\phi'(z^{(3)}_i(\alpha))=1
\quad\hbox{for every }i,
\]
\[
(W^{(3)}_n)^T\mathbf1_n
=\rho P_{\mathrm{bulk}}\mathbf1_n+\sqrt n\,v_n
=q^{(2)}_n.
\tag{41}
\]

This proves the same raw backward field (31) is realized exactly at both algebraic states.

For explicit forward values, put

\[
\tau_n(\alpha)=
\frac{2\phi(L_n(\alpha))
-\beta(1-1/\sqrt n)\phi((L_n(\alpha)-1)/2)}{\sqrt n},
\qquad
H_n(\alpha)=\phi(c_0T_n(\alpha)).
\]

Then

\[
z^{(3)}_i(\alpha)=
\begin{cases}
\tau_n(\alpha),&i=1,2,\\
\tau_n(\alpha)+\rho H_n(\alpha),&i\geq3.
\end{cases}
\tag{42}
\]

At zero, \(\tau_n(0)=2c_0/\sqrt n\).
At either endpoint, using \(|\phi|<\pi/2\),

\[
|\tau_n(\alpha)|\leq\frac{\pi(1+\beta/2)}{\sqrt n},\qquad
\|z^{(3)}(\alpha)\|_\infty\leq
Z:=\frac{\pi(1+\beta/2)}2+\frac{\rho\pi}{2}\quad(n\geq4).
\tag{43}
\]

Thus \(1\leq W^{(4)}_i(\alpha)\leq1+Z^2\).
Furthermore, (38), (30), and \(|\phi'|\leq1\) imply

\[
\frac{\|\Delta z^{(3)}\|_2}{\sqrt n}
\leq K_3\frac{\|\Delta h^{(2)}\|_2}{\sqrt n}=O(1/n),
\qquad
\frac{\|\Delta h^{(3)}\|_2}{\sqrt n}=O(1/n).
\]
\[
\frac{\|\Delta W^{(4)}\|_2}{\sqrt n}
\leq2Z\frac{\|\Delta z^{(3)}\|_2}{\sqrt n}=O(1/n).
\tag{44}
\]

The last inequality uses the exact difference of squares in (40). Thus the readout change is included in the small full primal state distance; it has not been treated as free external data.

### 5.5 Uniform primal bounds and the positive prediction limit

For both endpoints, all the following bounds are independent of \(n\):

\[
\frac{\|W^{(1)}\|_2}{\sqrt n}=1,\qquad
\|W^{(2)}\|_{\mathrm{op}}\leq K_2,\qquad
\|W^{(3)}\|_{\mathrm{op}}\leq K_3,\qquad
\frac{\|W^{(4)}\|_2}{\sqrt n}\leq1+Z^2,\qquad
\|W^{(4)}\|_\infty\leq1+Z^2,
\]
\[
\frac{\|W^{(2)}\|_F}{\sqrt n}\leq K_2,\qquad
\frac{\|W^{(3)}\|_F}{\sqrt n}\leq K_3,
\]
\[
\frac{\|z^{(1)}\|_2}{\sqrt n}=1,\qquad
\frac{\|z^{(2)}\|_2}{\sqrt n}\leq\frac32,\qquad
\frac{\|z^{(3)}\|_2}{\sqrt n}\leq Z,\qquad
\frac{\|h^{(\ell)}\|_2}{\sqrt n}\leq\frac\pi2\quad(\ell=1,2,3),
\]
\[
c_1=c_0^2>0,\qquad
\frac{\|\delta^{(3)}\|_2}{\sqrt n}=1,\qquad
\frac{\|q^{(2)}\|_2}{\sqrt n}\leq\sqrt{4+\beta^2+\rho^2},\qquad
\frac{\|d^{(2)}\|_2}{\sqrt n}\leq\sqrt{4+\beta^2+\rho^2}.
\tag{45}
\]

For the \(z^{(2)}\) bound, (25) and (28) bound every coordinate in absolute value by \(3/2\). For a square \(n\times n\) matrix, the Frobenius norm is at most \(\sqrt n\) times its operator norm, which gives the displayed normalized Frobenius bounds. Also \(\|u_R^{(2)}\|_2/\sqrt n\leq1\).
In fact \(\|h^{(1)}\|_2/\sqrt n=c_0\), and
\(\|h^{(2)}\|_2^2/n\to\phi(c_0)^2>0\) at either endpoint.

For the prediction, define the scalar function \(g(s)=(1+s^2)\phi(s)\). Equations (22), (40), and (42) give the exact formula

\[
f_n(\alpha)=
\frac2n g(\tau_n(\alpha))
+\frac{n-2}{n}g(\tau_n(\alpha)+\rho H_n(\alpha)).
\tag{46}
\]

At both \(\alpha=0\) and \(\alpha=1/n\),
\(\tau_n(\alpha)\to0\) by (43) and \(H_n(\alpha)\to\phi(c_0)\) by (28).
Continuity of \(g\), together with its boundedness on the fixed interval in (43), therefore gives

\[
f_n(0),\ f_n(1/n)\longrightarrow
f_*=(1+k^2)\phi(k)>0,\qquad
k=\rho\phi(c_0).
\tag{47}
\]

Because \(0<\phi(c_0)<c_0<1\) and \(\rho=1/4\), one has
\(0<k<1/4\), and

\[
0<f_*<(1+1/16)/4=17/64<1.
\]

In particular, for all sufficiently large \(n\), both predictions lie in the same fixed interval
\([f_*/2,(1+f_*)/2]\subset(0,1)\).
Their difference is also small. Directly from (22),

\[
|\Delta f|
\leq
\frac{\|\Delta W^{(4)}\|_2}{\sqrt n}
\frac{\|h^{(3)}(1/n)\|_2}{\sqrt n}
+
\frac{\|W^{(4)}(0)\|_2}{\sqrt n}
\frac{\|\Delta h^{(3)}\|_2}{\sqrt n}
=O(1/n).
\tag{48}
\]

No cancellation assumption is needed for this bound.

### 5.6 Failure of a uniform full-state Lipschitz estimate

To specify the claim precisely, include all primal variables, their forward constraints, and the prediction in a state \(S\). One full-state distance, using ordinary Frobenius distances for the two hidden weight matrices, is

\[
\begin{aligned}
D_n(S,\widetilde S)^2
={}&\frac{\|\Delta W^{(1)}\|_2^2+\|\Delta W^{(4)}\|_2^2}{n}
+\|\Delta W^{(2)}\|_F^2+\|\Delta W^{(3)}\|_F^2\\
&+\frac1n\sum_{\ell=1}^3
\left(\|\Delta z^{(\ell)}\|_2^2+\|\Delta h^{(\ell)}\|_2^2\right)
+|\Delta f|^2.
\end{aligned}
\tag{49}
\]

The common input has zero difference. The first-layer state and weights and the third-layer matrix also have zero difference. Equations (29), (30), (44), and (48) give a constant \(K\), independent of \(n\), such that

\[
D_n(S_n(0),S_n(1/n))\leq\frac K n.
\]

Conversely (29) gives
\(n\|\Delta W^{(2)}\|_F\to\sqrt{1+20/\pi^2}>0\).
Therefore \(D_n(S_n(0),S_n(1/n))\) is of order \(1/n\).
Adding
\((\|\Delta q^{(2)}\|_2^2+\|\Delta\delta^{(3)}\|_2^2)/n\)
to (49) does not change it, since both differences vanish exactly.

By (36), the Lipschitz quotient satisfies

\[
\frac{n^{-1/2}\|u_R^{(2)}(S_n(1/n))-u_R^{(2)}(S_n(0))\|_2}
{D_n(S_n(1/n),S_n(0))}
\geq\frac{\beta}{2K}\sqrt n
\longrightarrow\infty.
\tag{50}
\]

The quotient is also bounded above by a constant times \(\sqrt n\) for large \(n\), from the positive lower asymptotic bound in (29) and the finite nonzero limit in (36). Thus its order is exactly \(\sqrt n\).

This is a counterexample on one family of fixed primal bounds, for example bounds chosen to exceed the constants in (27), (43), and (45), together with the fixed prediction interval following (47). It disproves a Lipschitz constant depending only on those bounds and \(R\), uniformly in width. It continues to disprove the estimate if the hidden-matrix differences in (49) are divided by \(\sqrt n\), since that only decreases the input distance. It also disproves the estimate for a distance containing only the primal parameter terms from (49). A product-valued backward field whose output norm includes \(n^{-1/2}\|\Delta u_R^{(2)}\|_2\) as a component inherits the same obstruction.

The normalized bound (32) does not contradict (11): its two rare coordinates grow as \(\sqrt n\), so there is no uniform bound on \(\|q^{(2)}\|_\infty\).

### 5.7 Exact scope limitations

The readout normalization matters for this particular family. To quantify it, let \(\gamma=1-\beta/2>0\). From (42),

\[
n\,\Delta\tau_n
=\sqrt n\left\{2[\phi(1+x_n)-\phi(1)]
-\beta(1-1/\sqrt n)\phi(x_n/2)\right\}
\longrightarrow\gamma.
\]

Indeed \(\phi'(1)=1/2\), \(\phi'(0)=1\), and \(\sqrt n\,x_n\to1\). For a bulk coordinate, (28) gives
\(n[H_n(1/n)-H_n(0)]\to0\).
Therefore \(n\,\Delta z^{(3)}_j\to\gamma\) for every bulk coordinate, all of which have the same value, and their base values tend to \(k>0\).
The difference of squares in (40) gives
\(n\,\Delta W^{(4)}_j\to2k\gamma\) on the bulk.
On the two rare coordinates the readout difference is \(O(n^{-3/2})\), because their preactivations are \(O(n^{-1/2})\) and their changes are \(O(n^{-1})\). Consequently

\[
\sqrt n\,\|\Delta W^{(4)}\|_2\longrightarrow2k\gamma>0.
\]

If the input distance instead contains the unnormalized readout distance \(\|\Delta W^{(4)}\|_2\), the quotient for this family is thus bounded above asymptotically by \(\beta/(2k\gamma)\); the present construction does not refute a Lipschitz claim for that different distance.

The factor in the backward field also matters. If the projection acts on the ordinary Euclidean derivative \(\nabla_{z^{(2)}}f=d^{(2)}/n\), every coordinate of this raw input is eventually inside the box, so the projection equals \(d^{(2)}/n\) exactly. Equations (33) give rare-coordinate raw differences \(-A_n\to-1\) and \(\beta E_n\to0\); the bulk difference has Euclidean norm \(O(1/n)\). Hence \(\|\Delta d^{(2)}\|_2\to1\), and the projected-output difference divided by \(\sqrt n\) is then asymptotic to \(1/(n\sqrt n)\). Its quotient against (49) tends to zero for this family. The counterexample (50) is specifically for the raw backward field in (23), with the residual excluded.

For any other fixed \(R>0\), the same construction can be rescaled by multiplying the two rare entries in (31) by \(R\), multiplying the two nonzero entries of \(v_n\) by \(R\), and choosing \(0<\rho<\min\{R,1/4\}\). The rare projected outputs in (35) become \((R,0)\) and \((R,\beta R(E_n-A_n))\). The uniform constants may depend on this fixed \(R\); the width divergence and the positive bulk prediction limit persist.

## 6. Combined conclusion and audit status

Sections 1--4 retain the original fixed-width result, with canonical layer notation revised throughout. For \(R>0\), a fixed positive-definite metric gives a globally Lipschitz map \((z,q)\mapsto P_M(\phi'(z)\odot q)\) on the whole Euclidean input space exactly when that metric is diagonal. The \(q\)-only estimate \(\sqrt{C/c}\) holds for every fixed metric, and a uniform coordinate bound on \(q\) yields (11).

The original fixed-width construction alone did not test a width-uniform normalized primal norm ball. Section 5 supplies that stronger test: complete, forward- and backward-consistent algebraic network states, bounded upper operator norms and normalized primal norms, bounded \(\|q^{(2)}\|_2/\sqrt n\), positive prediction separated from 0 and 1, and exactly fixed canonical mobility within every pair. The full input distance (49) is of order \(1/n\), while the projected layer-2 field difference divided by \(\sqrt n\) is of order \(1/\sqrt n\).

This is only an admissible algebraic state/mapping counterexample, NOT a prescribed Gaussian trained-trajectory counterexample. It proves no initialization probability, reachability, or actual trained failure. No energy or global-dynamics conclusion is drawn.

The original note and this extension remain unverified for adoption until a separate audit. The SHA-256 checksum of the completed file is reported separately so that the checksum does not alter the file it identifies.
