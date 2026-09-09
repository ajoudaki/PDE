# Local feature learning in all three hidden layers

This lemma concerns the canonical local population flow with arctangent
activation and initially zero output weights. It assumes that the local
flow and its Gaussian operator actions have been constructed. It does
not construct that flow, identify it with a trained finite network, or
assert existence for all time. The small-time conclusions below require
only strong continuity in the natural second-moment spaces, the canonical
integral equations, and bounded initial operator actions.

## Setup and the local statement

For layer \(\ell\), let \(\mathcal H_\ell=L^2(\Omega_\ell)\), with
inner product \(\langle u,v\rangle_\ell=\mathbb E[uv]\). Write
\(\|u\|_\ell^2=\mathbb E[u^2]\). Let
\(W^{(2)}(s):\mathcal H_1\to\mathcal H_2\) and
\(W^{(3)}(s):\mathcal H_2\to\mathcal H_3\) be the bounded operator
actions supplied by the local construction, and let a star denote their
Hilbert-space adjoints. For \(u\in\mathcal H_\ell\) and
\(v\in\mathcal H_{\ell-1}\), define the rank-one operator
\[
 (u\otimes v)x=u\langle v,x\rangle_{\ell-1}.
\]
Its Hilbert--Schmidt norm is \(\|u\|_\ell\|v\|_{\ell-1}\).
This is the population version of \(uv^{\mathsf T}/n\), when finite
vectors have inner product \(u^{\mathsf T}v/n\).

Set \(\phi(x)=\arctan x\), \(d(x)=\phi'(x)=(1+x^2)^{-1}\),
and \(a=\pi/2\). The variable \(s\) is feature time. The local
canonical equations are
\[
 H^{(\ell)}=\phi(Z^{(\ell)}),\qquad
 Z^{(2)}=W^{(2)}H^{(1)},\qquad Z^{(3)}=W^{(3)}H^{(2)},
\]
\[
 D_\ell u=d(Z^{(\ell)})u,\qquad
 \delta^{(3)}=D_3W^{(4)},\qquad
 q^{(2)}=(W^{(3)})^*\delta^{(3)},\qquad
 \delta^{(2)}=D_2q^{(2)},\qquad
 q^{(1)}=(W^{(2)})^*\delta^{(2)},
\]
\[
 \frac{dZ^{(1)}}{ds}=D_1q^{(1)},\quad
 \frac{dW^{(2)}}{ds}=\delta^{(2)}\otimes H^{(1)},\quad
 \frac{dW^{(3)}}{ds}=\delta^{(3)}\otimes H^{(2)},\quad
 \frac{dW^{(4)}}{ds}=H^{(3)}.                              \tag{1}
\]
These equations can equivalently be assumed in integral form. The
states are continuous in their \(L^2\) spaces; the weights are continuous
in operator norm, as also follows from their rank-one integral updates.
All limits below are in these \(L^2\) spaces unless otherwise stated.

Initially \(W^{(4)}_0=0\). The Gaussian initialization supplies
\(Z^{(1)}_0\sim N(0,1)\), the independent Gaussian initial actions
\(W^{(2)}_0,W^{(3)}_0\), and the forward laws
\[
 Z^{(2)}_0\sim N(0,m_1),\qquad Z^{(3)}_0\sim N(0,m_2),\qquad
 m_\ell=\|H^{(\ell)}_0\|_\ell^2>0.                       \tag{2}
\]
Thus, for a standard Gaussian \(G\),
\[
 m_1=\mathbb E\phi(G)^2,\quad
 m_2=\mathbb E\phi(\sqrt{m_1}G)^2,\quad
 m_3=\mathbb E\phi(\sqrt{m_2}G)^2.
\]
The notation \(D_{\ell,0}\) means multiplication by
\(d(Z^{(\ell)}_0)\).

Define the initial backward fields, each on its indicated population,
\[
 \beta_3=H^{(3)}_0d(Z^{(3)}_0)\in\mathcal H_3,\quad
 P_2=(W^{(3)}_0)^*\beta_3\in\mathcal H_2,\quad
 B_2=D_{2,0}P_2\in\mathcal H_2,\quad
 P_1=(W^{(2)}_0)^*B_2\in\mathcal H_1.                    \tag{3}
\]
Define the bounded self-adjoint operators
\[
 \mathcal A^{(2)}_0
 =m_1 I+W^{(2)}_0D_{1,0}^{\,2}(W^{(2)}_0)^*,
\]
\[
 \mathcal A^{(3)}_0
 =m_2 I+W^{(3)}_0D_{2,0}\mathcal A^{(2)}_0
                         D_{2,0}(W^{(3)}_0)^*.           \tag{4}
\]
Finally put
\[
 V_1=D_{1,0}P_1,\qquad
 V_2=\mathcal A^{(2)}_0B_2,\qquad
 V_3=\mathcal A^{(3)}_0\beta_3.                           \tag{5}
\]

As \(s\downarrow0\), the local flow satisfies
\[
 W^{(4)}(s)=sH^{(3)}_0+o(s),\quad
 \delta^{(3)}(s)=s\beta_3+o(s),\quad
 q^{(2)}(s)=sP_2+o(s),
\]
\[
 \delta^{(2)}(s)=sB_2+o(s),\qquad q^{(1)}(s)=sP_1+o(s),  \tag{6}
\]
and, for all three hidden layers,
\[
 \frac{dZ^{(\ell)}}{ds}=sV_\ell+o(s),\qquad
 Z^{(\ell)}(s)-Z^{(\ell)}_0
       =\frac{s^2}{2}V_\ell+o(s^2),
\]
\[
 \frac{dH^{(\ell)}}{ds}=sD_{\ell,0}V_\ell+o(s),\qquad
 H^{(\ell)}(s)-H^{(\ell)}_0
       =\frac{s^2}{2}D_{\ell,0}V_\ell+o(s^2).            \tag{7}
\]
Every \(V_\ell\) and every \(D_{\ell,0}V_\ell\) has strictly
positive \(L^2\) norm. Thus the second-order changes are genuine in
each preactivation and each hidden feature.

## Strong limits without differentiability assumptions on an \(L^2\) map

The following elementary multiplier fact is sufficient. If
\(x_s\to x_0\) in probability, \(v_s\to v_0\) in \(L^2\), and
\(g\) is bounded and continuous, then
\[
 g(x_s)v_s\longrightarrow g(x_0)v_0\quad\text{in }L^2.   \tag{8}
\]
Indeed, the part containing \(v_s-v_0\) is bounded by
\(\|g\|_\infty\|v_s-v_0\|_2\). For the other part, first restrict
to \(|v_0|\le K\), where bounded convergence in probability gives
convergence of its squared expectation, and then let \(K\to\infty\).
The remaining bound is
\(4\|g\|_\infty^2\mathbb E[|v_0|^2\mathbf1_{\{|v_0|>K\}}]\).
Only the fixed reference \(v_0\in L^2\) is used.

The same argument justifies the chain rule along a differentiable
\(L^2\) curve. If \(x(s+h)-x(s)=hv_h\) and \(v_h\to v\) in
\(L^2\), then
\[
 \frac{\phi(x(s+h))-\phi(x(s))}{h}
 =v_h\int_0^1 d\bigl(x(s)+rh v_h\bigr)\,dr
 \longrightarrow d(x(s))v\quad\text{in }L^2.
\]
The integral multiplier is bounded by one and converges in probability
to \(d(x(s))\). This is a chain rule along the given curve, not an
assertion of Frechet differentiability of a Nemytskii map on \(L^2\).

The integral equation for \(W^{(4)}\) and continuity of \(H^{(3)}\)
give \(W^{(4)}(s)/s\to H^{(3)}_0\). Apply (8), then operator-norm
continuity of \(W^{(3)}\), then (8) again, and finally operator-norm
continuity of \(W^{(2)}\). This proves every limit in (6).

All right-hand sides of (1) are continuous by (8), so the integral
equations give strong derivatives. The chain rule above yields the
exact identities
\[
 \frac{dZ^{(2)}}{ds}=\mathcal A^{(2)}(s)\delta^{(2)},\qquad
 \mathcal A^{(2)}(s)
 =\|H^{(1)}(s)\|_1^2 I
       +W^{(2)}(s)D_1(s)^2(W^{(2)}(s))^*,
\]
\[
 \frac{dZ^{(3)}}{ds}=\mathcal A^{(3)}(s)\delta^{(3)},\qquad
 \mathcal A^{(3)}(s)
 =\|H^{(2)}(s)\|_2^2 I
       +W^{(3)}(s)D_2(s)\mathcal A^{(2)}(s)
                         D_2(s)(W^{(3)}(s))^*.           \tag{9}
\]
For example, the first identity uses
\((\delta^{(2)}\otimes H^{(1)})H^{(1)}
=\|H^{(1)}\|_1^2\delta^{(2)}\) and
\(dH^{(1)}/ds=D_1^2(W^{(2)})^*\delta^{(2)}\).
The second follows from
\(dZ^{(3)}/ds=\|H^{(2)}\|_2^2\delta^{(3)}
 +W^{(3)}D_2\,dZ^{(2)}/ds\).

The operators in (9) are uniformly bounded near zero and converge
strongly on every fixed \(L^2\) vector to the operators in (4).
To verify this, apply (8) successively to the bounded gates and use
operator-norm continuity of the weights. No operator-norm convergence
of the gate multiplication operators is needed. Combining this strong
convergence with (6) proves the derivative expansions in (7).
Integration proves the state expansions; a further use of (8) and the
curve chain rule proves the feature expansions.

## Initial transpose conditioning and strict positivity

Here is the initial Gaussian conditioning calculation needed for (3).
For a finite Gaussian matrix \(W\) with entry variance \(1/n\), an
independent nonzero input \(h\), and \(y=Wh\), conditioning on \(h,y\)
gives
\[
 W=\frac{yh^{\mathsf T}}{\|h\|_2^2}
        +\widetilde W P_{h^\perp}
 \quad\text{in conditional law},
\]
where \(\widetilde W\) is an independent matrix with the same entry
variance. If \(u\) is measurable from \(h,y\) and auxiliary randomness
independent of this conditional residual, then
\[
 W^{\mathsf T}u
 =h\,\frac{y^{\mathsf T}u/n}{\|h\|_2^2/n}
  +\sqrt{\|u\|_2^2/n}\,P_{h^\perp}g
 \quad\text{in conditional law},                       \tag{10}
\]
with a fresh standard Gaussian vector \(g\). The removed projection
has conditional normalized mean square \(1/n\). Thus, when the input
contractions have their canonical limits, its scalar transpose law is
\(c h+\sigma G\), with
\(c=\mathbb E[yu]/\mathbb E[h^2]\) and
\(\sigma^2=\mathbb E[u^2]\). The innovation \(G\) is independent
of the existing same-population initial data. Importantly, the
innovation variance is \(\mathbb E[u^2]\), without subtraction of
the response component.

First apply (10) to \(W^{(3)}_0\), input \(H^{(2)}_0\), output
\(Z^{(3)}_0\), and transpose input \(\beta_3\). It gives the joint
same-population law
\[
 P_2=c_3H^{(2)}_0+\sigma_3G^{\mathrm b}_2,\qquad
 c_3=\frac{\mathbb E[Z^{(3)}_0\beta_3]}{m_2}>0,\qquad
 \sigma_3^2=\mathbb E[\beta_3^2]>0,                      \tag{11}
\]
where \(G^{\mathrm b}_2\sim N(0,1)\) is independent of
\(Z^{(2)}_0\). Both inequalities follow because
\(z\phi(z)d(z)>0\) for \(z\ne0\), and the Gaussian variance
\(m_2\) is positive. Consequently
\[
 B_2=d(Z^{(2)}_0)
       \bigl(c_3\phi(Z^{(2)}_0)+\sigma_3G^{\mathrm b}_2\bigr),
\]
\[
 \sigma_2^2:=\mathbb E[B_2^2]
 =\mathbb E\left[d(Z^{(2)}_0)^2
          \bigl(c_3^2\phi(Z^{(2)}_0)^2+\sigma_3^2\bigr)\right]>0.
                                                                    \tag{12}
\]

For the second application, condition on the bottom initialization,
\(Z^{(2)}_0=W^{(2)}_0H^{(1)}_0\), and the entire independent initial
matrix \(W^{(3)}_0\). The field \(B_2\) is then fixed and introduces
no further information about the conditional residual of
\(W^{(2)}_0\). Formula (10) therefore gives
\[
 P_1=c_2H^{(1)}_0+\sigma_2G^{\mathrm b}_1,\qquad
 c_2=\frac{\mathbb E[Z^{(2)}_0B_2]}{m_1}
 =\frac{c_3}{m_1}
       \mathbb E[Z^{(2)}_0d(Z^{(2)}_0)\phi(Z^{(2)}_0)]>0. \tag{13}
\]
Here \(G^{\mathrm b}_1\) is standard Gaussian, independent of
\(Z^{(1)}_0\); the successive fresh innovations can be chosen as
independent groups in the canonical initial source construction.
The factor \(c_3\) in (13) retains the return through the third-layer
matrix. Treating \(B_2\) as an independent centered multiplier would
lose this term.

Only initial finite Gaussian queries are involved in (10)--(13).
Their contractions converge by conditional Gaussian averaging: the
forward activation averages are bounded; in the transpose step the
rank-one projection error vanishes in normalized \(L^2\); bounded
gates preserve that convergence. Pairwise contractions then converge
by Cauchy--Schwarz. This calculation uses no trained-state limit.

By (12)--(13), \(P_1\ne0\), \(B_2\ne0\), and \(\beta_3\ne0\)
in their \(L^2\) spaces. Moreover,
\[
 \mathcal A^{(2)}_0\succeq m_1I,\qquad
 \mathcal A^{(3)}_0\succeq m_2I.                         \tag{14}
\]
For any nonzero \(v\), the first inequality implies
\(\|\mathcal A^{(2)}_0v\|\ge m_1\|v\|\), by taking its inner
product with \(v\); the second gives the corresponding bound with
\(m_2\). Finally, multiplication by \(d(Z^{(\ell)}_0)\) has zero
kernel because \(d(z)>0\) for every finite \(z\). These observations
prove the strict positivity asserted after (7).

## Physical time, kernel blocks, and squared speeds

Let \(f(s)=\langle W^{(4)}(s),H^{(3)}(s)\rangle_3\).
Equation (6) gives \(f(s)=m_3s+o(s)\). In a sufficiently small
neighborhood of zero, \(f(s)<1\), so define physical time by
\[
 \frac{ds}{dt}=2(1-f(s)),\qquad s(0)=0.
\]
Equivalently,
\(t(s)=\int_0^s[2(1-f(u))]^{-1}\,du\). It follows that
\[
 s(t)=2t+o(t),\qquad 1-f(s(t))=1+o(1).                  \tag{15}
\]
This is precisely the residual factor for squared loss \((f-1)^2\).
In particular, with the left-hand sides evaluated at feature time
\(s(t)\),
\[
 Z^{(\ell)}-Z^{(\ell)}_0=2t^2V_\ell+o(t^2),\qquad
 H^{(\ell)}-H^{(\ell)}_0=2t^2D_{\ell,0}V_\ell+o(t^2).
\]

Define the four population kernel blocks at physical time \(t\) by
\[
 \kappa_1(t)=\|D_1q^{(1)}\|_1^2,\quad
 \kappa_2(t)=\|H^{(1)}\|_1^2\|\delta^{(2)}\|_2^2,\quad
 \kappa_3(t)=\|H^{(2)}\|_2^2\|\delta^{(3)}\|_3^2,\quad
 \kappa_4(t)=\|H^{(3)}\|_3^2,
\]
where every right-hand side is evaluated at \(s=s(t)\). Put
\[
 \gamma_1=\|D_{1,0}P_1\|_1^2>0,\qquad
 \gamma_2=m_1\|B_2\|_2^2>0,\qquad
 \gamma_3=m_2\|\beta_3\|_3^2>0.
\]
Then
\[
 \kappa_\ell(t)=4\gamma_\ell t^2+o(t^2)\quad(\ell=1,2,3),
 \qquad \kappa_4(t)=m_3+o(1).                           \tag{16}
\]
In particular all three hidden kernel blocks are strictly positive
at every sufficiently small positive time. These coefficients are
finite using only the second moments established above. For example,
\[
 \gamma_1=\mathbb E\left[d(Z^{(1)}_0)^2
           \bigl(c_2^2\phi(Z^{(1)}_0)^2+\sigma_2^2\bigr)\right]>0.
\]

To state the squared-speed consequence precisely, use the \(L^2\)
norm for the vector blocks \(Z^{(1)},W^{(4)}\) and the
Hilbert--Schmidt norm for the two matrix velocities. Let
\(\mathcal J_\ell(T)\) be the integral from \(0\) to \(T\) of the
squared velocity of block \(\ell\). Equation (1) and the time change
give the exact identity
\[
 \mathcal J_\ell(T)
 =\int_0^T4(1-f(s(t)))^2\kappa_\ell(t)\,dt.
\]
Therefore
\[
 \mathcal J_\ell(T)=\frac{16}{3}\gamma_\ell T^3+o(T^3)
       \quad(\ell=1,2,3),\qquad
 \mathcal J_4(T)=4m_3T+o(T).                            \tag{17}
\]
The initial matrix actions need not be Hilbert--Schmidt; only their
rank-one velocities and subsequent increments use that norm.

The hidden features themselves have positive squared-speed integrals
as well. Equations (7) and (15) give
\[
 \frac{dZ^{(\ell)}}{dt}=4tV_\ell+o(t),\qquad
 \frac{dH^{(\ell)}}{dt}=4tD_{\ell,0}V_\ell+o(t),
\]
and hence
\[
 \int_0^T\left\|\frac{dZ^{(\ell)}}{dt}\right\|_\ell^2dt
       =\frac{16}{3}\|V_\ell\|_\ell^2T^3+o(T^3),
\]
\[
 \int_0^T\left\|\frac{dH^{(\ell)}}{dt}\right\|_\ell^2dt
       =\frac{16}{3}\|D_{\ell,0}V_\ell\|_\ell^2T^3+o(T^3).
                                                                    \tag{18}
\]
All six leading coefficients in (18) are strictly positive. These
are local statements conditional on the canonical flow/action
construction; they make no assertion about the extent of its horizon.

## The kernel changes and the activation remains genuinely nonlinear

The expansions also prove nonconstancy of the total kernel.
Equations (4)--(5) and adjunction give
\[
 \langle\beta_3,\mathcal A^{(3)}_0\beta_3\rangle_3
 =m_2\|\beta_3\|_3^2+m_1\|B_2\|_2^2+\|D_{1,0}P_1\|_1^2
 =\gamma_1+\gamma_2+\gamma_3>0.
\]
Since \(H^{(3)}(s)=H^{(3)}_0+
(s^2/2)D_{3,0}V_3+o(s^2)\), expanding its squared norm gives
\[
 \kappa_4(s)=m_3+s^2(\gamma_1+\gamma_2+\gamma_3)+o(s^2).
\]
In feature time the sum of the three hidden kernel contributions
has the same positive \(s^2\) coefficient. In physical time,
\[
 \kappa(t)
 =m_3+8(\gamma_1+\gamma_2+\gamma_3)t^2+o(t^2).           \tag{19}
\]
Hence \(\kappa\) is not constant on any sufficiently small initial
interval. The gradient identity also gives
\(L(t)=1-4m_3t+o(t)\), and \(L(t)<1\) for small positive \(t\).

For each layer the initial preactivation is a nondegenerate
Gaussian. Its variance is positive. The mean-square error of the
best affine approximation to the activation is
\[
 \inf_{\alpha,\beta\in\mathbb R}
 E_\ell[(\phi(Z^{(\ell)})-\alpha Z^{(\ell)}-\beta)^2]
 =
 \operatorname{Var}(\phi(Z^{(\ell)}))
 -\frac{\operatorname{Cov}(Z^{(\ell)},\phi(Z^{(\ell)}))^2}
        {\operatorname{Var}(Z^{(\ell)})}.               \tag{20}
\]
Initially (20) is strictly positive. Otherwise \(\arctan z\)
would agree with an affine function with probability one under a
full-support Gaussian law; continuity would make them agree for
every real \(z\), which is false. The first and second moments
in (20) are continuous along the constructed mean-square paths,
because \(\phi\) is bounded and Lipschitz. Thus the variance and
(20) remain strictly positive on a common positive initial
interval for all three hidden layers.
