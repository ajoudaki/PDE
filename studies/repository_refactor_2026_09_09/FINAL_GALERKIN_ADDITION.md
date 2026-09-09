## Finite-source operator transport: exact conditional geometry

This section defines a separate operator-transport model and proves its
internal variational and parity identities for supplied regular solutions.
It does not identify a dense-network limit or assert general existence,
uniqueness, source-cutoff convergence, or a numerical accuracy result.
The state retains a continuous residual-depth coordinate \(s\in[0,1]\).
The integer \(P\) counts source modes, not neurons or residual layers.

### G.1 Sources, state and admissibility

Fix finite data \((x_a,y_a)_{a=1}^m\), \(x_a\in\mathbb R^d\), and
\(\gamma,\sigma_w,A>0\). The input map in this separate residual model
acts as \(W^{\rm in}\cdot x_a\), without an additional input factor;
thus its sample factor below is \(x_a^Tx_b\). No normalization or
orthogonality of these data is imposed. Use half-sum loss
\(\mathcal E=\tfrac12\sum_a(f_a-y_a)^2\), residual \(r_a=f_a-y_a\).

Let \(\theta\sim\mu=N(0,I_{d+1})\). Fix a finite orthonormal family
\((\varphi_j)_{j=1}^P\) in \(L^2(\mu)\), each a polynomial; the
complete-degree normalized Hermite families are one choice. Let
\(\epsilon\sim\nu=N(0,I_P)\), independent of \(\theta\).
The characteristic state consists of endpoint fields
\(W^{\rm in}(t,\theta)\in\mathbb R^d\),
\(W^{\rm out}(t,\theta)\in\mathbb R\), and learned row coefficients
\(c(s,t,\theta,\epsilon)\in\mathbb R^P\). Set

\[
 w=\sigma_w\epsilon+c,\qquad
 W^{\rm in}(0,\theta)=(\theta_1,\ldots,\theta_d),\quad
 W^{\rm out}(0,\theta)=A\theta_{d+1},\quad c(s,0)=0.
 \tag{G.1}
\]

All Gaussian labels are fixed during training. The same \(\epsilon\)
space may couple different depths; no joint physical depth-disorder law
is inferred from this convenient characteristic representation. The
conditional row law is \(\rho_{s,t}^\theta=w(s,t,\theta,\cdot)_\#\nu\).

The identities below hold on any supplied interval \([0,T]\) on which
these fields and the forward/adjoint fields defined next solve their integral
equations, are continuously differentiable in training time and absolutely
continuous in depth, and admit the following sufficient domination: each
field, each first time derivative used below, each depth derivative, and
the mixed depth/time derivative of the forward field is bounded in absolute
value by \(C(1+|\theta|+|\epsilon|)^q\), with finite \(C,q\) uniform
in \(s,t\). Slow fields are independent of \(\epsilon\). The same
condition is required for variations when a variational derivative is used.
These are explicit sufficient hypotheses for the stated identities, not an
existence theorem or a claim that all \(L^2\) states have this regularity.
Gaussian polynomial moments make every product and limit below integrable.

Write \(\mathbb E_\mu\) for slow-field pairing and
\(\mathbb E_{\mu\otimes\nu}\) for row pairing. Define

\[
 H_{ja}(s,t)=\mathbb E_\mu[\varphi_j H_a(s,t)],\qquad
 Z_a=w\cdot H_{\cdot a},\qquad
 \Delta_a=\phi'(Z_a)P_a(s,t,\theta),\quad \phi(z)=\tanh z.
 \tag{G.2}
\]

The forward and adjoint equations are

\[
 \partial_s H_a=\gamma\mathbb E_\nu[\phi(Z_a)],\qquad
 H_a(0,\theta)=W^{\rm in}\cdot x_a,
\]
\[
 -\partial_s P_a=\gamma\sum_j\varphi_j(\theta)
                      \mathbb E_{\mu\otimes\nu}[w_j\Delta_a],
 \qquad P_a(1,\theta)=W^{\rm out}(\theta),
\]
\[
 f_a=\mathbb E_\mu[W^{\rm out}H_a(1)].
 \tag{G.3}
\]

Here \(P_a\) is a residual-depth adjoint field, distinct from the mode
count \(P\) and the orthogonal projection \(\Pi_P\) used below.
For a supplied row state of finite second moment these depth equations are
well defined as linear growth/Lipschitz integral equations in \(L^2(\mu)\).
Indeed, for \(u\in L^2(\mu)\), set

\[
 (W_Pu)(\theta,\epsilon)=\sum_jw_j\mathbb E_\mu[\varphi_j u],\qquad
 (W_P^*v)(\theta)=\sum_j\varphi_j(\theta)
                         \mathbb E_{\mu\otimes\nu}[w_jv].
 \tag{G.4}
\]

Cauchy–Schwarz and orthonormality give
\(\|W_Pu\|_{L^2(\mu\otimes\nu)}\le
\|w\|_{L^2(\mu\otimes\nu)}\|u\|_{L^2(\mu)}\), and the same bound
for its adjoint. The forward depth map has Lipschitz coefficient
\(\gamma\|w(s)\|_{L^2}\), and value bounded by \(\gamma\) because
\(|\tanh|\le1\). Picard's integral iterates converge on short depth
intervals where the integrated coefficient is less than one, and their
differences satisfy the iterated integral bound
\(C(\int b)^k/k!\). A finite subdivision and this bound give uniqueness
and continuation across \([0,1]\) whenever the coefficient is integrable.
The adjoint is a linear integral equation with the same bound, solved from
\(s=1\). This verifies depth solvability only; training-time solvability
in a full state class remains separate.

The training equations in this model are

\[
 \dot c_j=-\gamma\sum_a r_a\Delta_a H_{ja},\qquad
 \dot W^{\rm in}=-\sum_a r_a P_a(0)x_a,\qquad
 \dot W^{\rm out}=-\sum_a r_a H_a(1).
 \tag{G.5}
\]

The state and fixed data determine the right-hand side; no external curve
or unretained history appears. A unique solution, if it exists in a declared
class, can therefore be restarted from this full state. Autonomy alone
supplies no uniqueness theorem.

### G.2 Shared adjoint, weak transport and gradient

Expand the finite sum in (G.4) and apply Fubini. It gives exactly

\[
 \mathbb E_{\mu\otimes\nu}[(W_Pu)v]
 =\sum_j\mathbb E_\mu[\varphi_j u]
                    \mathbb E_{\mu\otimes\nu}[w_jv]
 =\mathbb E_\mu[uW_P^*v].
 \tag{G.6}
\]

Both directions use the same current coefficients. At initialization,
for a smooth scalar function \(g\) with bounded value and derivative,
Gaussian integration by parts in \(\epsilon_j\) gives

\[
 W_P^*g(W_Pu)=\sigma_w^2\Pi_Pu\,
      \mathbb E_\nu[g'(\sigma_w\epsilon\cdot H[u])],
 \qquad H[u]_j=\mathbb E_\mu[\varphi_j u].
 \tag{G.7}
\]

The boundary term vanishes by Gaussian decay. This identity is an
initial-law statement; training does not preserve Gaussian row laws.

For a smooth compactly supported test \(\chi:\mathbb R^P\to\mathbb R\),
the characteristic chain rule yields
\(\partial_t\int\chi\,d\rho_{s,t}^\theta
=\int\nabla\chi\cdot V\,d\rho_{s,t}^\theta\), where
\(V_j=-\gamma\sum_a r_a\phi'(w\cdot H_{\cdot a})P_a H_{ja}\).
Domination justifies differentiation under the integral. This is precisely
the distributional conditional transport equation

\[
 \partial_t\rho_{s,t}^\theta+\nabla_w\cdot(\rho_{s,t}^\theta V)=0.
 \tag{G.8}
\]

To derive the gradient, vary the current state by
\((\delta W^{\rm in},\delta W^{\rm out},\delta c)\).
Differentiation of the forward equation gives

\[
 \partial_s\delta H_a
 =\gamma\mathbb E_\nu\!\left[\phi'(Z_a)
      \left(\delta c\cdot H_{\cdot a}
               +w\cdot\mathbb E_\mu[\varphi\delta H_a]\right)\right].
\]

Take its slow pairing with \(P_a\) and integrate in depth. The part
containing \(w\) cancels \(\langle\partial_sP_a,\delta H_a\rangle\)
by (G.3) and (G.6). The two boundary conditions therefore give the full
variation

\[
 \delta f_a=\mathbb E_\mu[H_a(1)\delta W^{\rm out}]
 +\mathbb E_\mu[P_a(0)x_a\cdot\delta W^{\rm in}]
 +\gamma\int_0^1\mathbb E_{\mu\otimes\nu}
       [\Delta_a H_{\cdot a}\cdot\delta c]ds.
 \tag{G.9}
\]

Every exchange is justified by the stated polynomial domination. For
example a product of finitely many polynomial envelopes is integrable
under \(\mu\otimes\nu\), and the depth interval has finite measure.
Thus (G.9) is a valid directional variational identity in this class;
it is not an unproved Fréchet differentiability assertion on a bare
\(L^2\) ball.

In the product characteristic metric

\[
 \|\delta\Theta\|_{\mathcal X}^2=
 \mathbb E_\mu|\delta W^{\rm in}|^2+
 \mathbb E_\mu|\delta W^{\rm out}|^2+
 \int_0^1\mathbb E_{\mu\otimes\nu}|\delta c|^2ds,
\]

the three functions in (G.9) are the represented output derivatives.
Consequently (G.5) is the negative represented gradient of the half-sum
loss. Substitution into (G.9) proves

\[
 \dot f_a=-\sum_b K_{ab}r_b,
\]
\[
 K_{ab}=\mathbb E_\mu[H_a(1)H_b(1)]
 +(x_a^Tx_b)\mathbb E_\mu[P_a(0)P_b(0)]
 +\gamma^2\int_0^1\left(\sum_j H_{ja}H_{jb}\right)
                  \mathbb E_{\mu\otimes\nu}[\Delta_a\Delta_b]ds.
 \tag{G.10}
\]

For any real coefficients \(v_a\), the three quadratic forms are the
squared norms of \(\sum_a v_aH_a(1)\),
\(\sum_a v_aP_a(0)x_a\), and
\(\gamma\sum_a v_a\Delta_a H_{\cdot a}\), respectively, with the
last integrated over depth. Hence \(K\succeq0\) and

\[
 -\dot{\mathcal E}=r^TKr=\|\dot\Theta\|_{\mathcal X}^2.
 \tag{G.11}
\]

Cauchy–Schwarz now gives displacement at most
\(\sqrt{t\mathcal E(0)}\) and increments at most
\(\sqrt{|t-s|\mathcal E(0)}\) in \(\mathcal X\) on this supplied
path. Replacing the projected pairing \(\sum_jH_{ja}H_{jb}\) in
(G.10) by the full hidden pairing changes the kernel and loses the proved
identity. For full mean-square loss let \(\lambda=2/m\), replace (G.5) by
\(\dot\Theta=-\lambda\sum_a r_a\nabla f_a\), and keep \(K\) as in
(G.10). Then \(\dot f=-\lambda Kr\) and
\(\dot{\mathcal L}=-\lambda^2r^TKr=-\|\dot\Theta\|_{\mathcal X}^2\),
where \(\mathcal L=\lambda\mathcal E\).

### G.3 Exact parity and the active mode counts

For this subsection take complete multivariate Hermite polynomials through
a degree \(D\), orthonormal under \(\mu\). Their parity is
\(\varphi_j(-\theta)=J_{jj}\varphi_j(\theta)\),
\(J_{jj}=(-1)^{\deg\varphi_j}\). This follows directly from the
one-variable generating identity
\(e^{tx-t^2/2}=\sum_{k\ge0}H_k(x)t^k/k!\): replacing \(x,t\) by
\(-x,-t\) gives \(H_k(-x)=(-1)^kH_k(x)\). Products give the
multivariate formula; normalization leaves it unchanged.

The conditional equations are equivariant under

\[
 (W^{\rm in},W^{\rm out},\rho^\theta)
 \mapsto(-W^{\rm in}(-\theta),-W^{\rm out}(-\theta),
                       J_\#\rho^{-\theta}).
 \tag{G.12}
\]

Indeed the transformed forward field is \(-H_a(-\theta)\), so its
mode coefficients are \(-JH_{\cdot a}\). With \(w\mapsto Jw\),
the preactivation changes sign. Oddness of \(\tanh\) and evenness of
its derivative then transform \(P_a,\Delta_a\) into their negatives
at \(-\theta\). In the adjoint expression the extra coefficient signs
combine with \(\varphi_j(-\theta)=J_{jj}\varphi_j(\theta)\), giving
the transformed depth equation. The product \(W^{\rm out}H_a(1)\)
is invariant after the change of variable \(\theta\mapsto-\theta\),
so predictions and residuals are unchanged for arbitrary labels. Finally
\(-\gamma\sum_a r_a\Delta_a H_{ja}\) transforms to \(J_{jj}\)
times its old value at \(-\theta\), as required by row transport.
The endpoint velocities transform in the same way.

Initialization (G.1) is fixed by (G.12). If the conditional initial-value
problem is unique in a class preserved by this transformation, its solution
is fixed by (G.12). Thus the slow fields are odd in \(\theta\), and
\(H_{ja}=0\) for even-degree \(j\). Their coefficient velocities are
zero. In the characteristic description these even coordinates remain
\(\sigma_w\epsilon_j\). The odd-coordinate ODE has no dependence on
the even coordinates, since they are absent from \(Z_a\). With supplied
slow fields its finite-dimensional ODE is locally Lipschitz; its unique
solution consequently depends only on \(\theta\) and the odd Gaussian
coordinates. Independence and centering then imply
\(\mathbb E_{\mu\otimes\nu}[w_j\Delta_a]=0\) for even \(j\).
The even modes make no forward or transpose contribution.

Adding a complete even-degree shell to an odd-degree cutoff therefore
leaves the exact symmetric physical solution unchanged, conditional on
existence and uniqueness in compatible classes. No uniqueness is inferred
from parity. For \(d+1=4\), the total degree-\(k\) multiplicity is
\(\binom{k+3}{3}\): choosing the four nonnegative exponents summing to
\(k\) is equivalent to positioning three separators among \(k+3\)
slots. Summing gives:

| Maximum degree | Full modes | Active odd modes |
|---:|---:|---:|
| 1 | 5 | 4 |
| 2 | 15 | 4 |
| 3 | 35 | 24 |
| 4 | 70 | 24 |
| 5 | 126 | 80 |

These exact counts describe the model, without a cubature or training claim.

### G.4 Bounded transpose, noncompactness and the remaining bridge

The infinite-source comparison already has a useful exact Hilbert fact.
Let \((e_j)\) be an orthonormal basis of a separable real Hilbert space
\(\mathcal H\), and \((\epsilon_j)\) independent standard Gaussians.
Define \(Iu=\sum_j\langle u,e_j\rangle\epsilon_j\) in \(L^2\).
The partial sums are Cauchy and
\(\|Iu\|_{L^2}^2=\sum_j\langle u,e_j\rangle^2=\|u\|^2\).
For \(v\in L^2\), Bessel's inequality gives
\(\sum_j|\mathbb E[\epsilon_jv]|^2\le\|v\|_{L^2}^2\).
It follows that

\[
 I^*v=\sum_j e_j\mathbb E[\epsilon_jv],\qquad\|I^*v\|\le\|v\|_{L^2}.
\]

Extra target labels may be included in the expectation independently.
No derivative of \(v\) is required for this adjoint formula. A learned
row \(c\in L^2(\mathcal H)\) defines
\(R_cu=\langle c,u\rangle\), with
\(R_c^*v=\mathbb E[cv]\) and operator norm at most
\(\|c\|_{L^2(\mathcal H)}\); these assertions follow by
Cauchy–Schwarz and pairing with arbitrary unit \(u\).
Thus \(\sigma_wI+R_c\) and its adjoint are bounded.

Nevertheless \(I^*\epsilon_j=e_j\). For every finite basis projection
\(\Pi_K\),
\(\sup_{\|v\|_{L^2}\le1}\|(1-\Pi_K)I^*v\|=1\), by choosing an
omitted \(\epsilon_j\). Hence bounded energy alone gives no uniform
source-tail decay. Projection convergence is uniform on a fixed compact
set: choose a finite \(\epsilon\)-net there, apply pointwise convergence
to its centers, and use \(\|1-\Pi_K\|\le1\) on the remaining errors.
An energy ball is not that compact set.

There is also an explicit failure of a useful ambient Lipschitz shortcut.
For a standard Gaussian \(a\), the map \((z,p)\mapsto\phi'(z)p\)
on \(L^2\times L^2\) is not locally Lipschitz at \((0,a)\).
Let \(E_N=\{|a|>N\}\), \(z_N=\mathbf1_{E_N}\), and keep \(p=a\).
Then \(\|z_N\|_2\to0\), whereas

\[
 \frac{\|[\phi'(z_N)-\phi'(0)]a\|_2}{\|z_N\|_2}
 \ge |\operatorname{sech}^2(1)-1|N\longrightarrow\infty.
\]

This is an ambient multiplier counterexample, not a statement that these
perturbations are reached by the source-transport dynamics.
The internal identities above leave distinct obligations for general
well-posedness, collective source tails, stability of nonlinear truncation
errors, and identification with trained iid dense depth slices. Neither
an exact projected kernel nor conditional parity supplies those proofs.
