# Explicit control and terminal-time moduli for insertion maps

2026-10-07. Bounded author derivation for the remaining interpolation
interfaces of `QUANTITATIVE_INSERTION_WIDTH.md`. The result concerns the
Gaussian linear response, its quadratic/bilinear pairings, and lower
adjoint probes on the original stopped cavity. It does not supply the
nonlinear insertion bootstrap or a complete stochastic success width.
No nonlinear jet result from another current agent is used.

The main conclusion is that the control modulus of every required response
matrix is bounded by an explicit coefficient times
\(\sqrt p\,n^{1/4000}\log(en)^2\) times the control error. The terminal-time
modulus is bounded by another explicit coefficient times
\(\sqrt{pn}\,n^{1/4000}\log(en)^4\). Both coefficients are finite
recurrences in the already displayed source constants and the physical
horizon coefficient. They contain no inverse power of label amplitude.

## 1. Setup and fixed reference

Use the canonical dense model and the original source label allowance.
Write \(\lambda=\gamma/m\), \(Y=\|y\|_2/\sqrt m>0\),
\(S=16Y/\lambda\le1\), and \(\ell=\log(en)\). Delete \(p\) neurons
in one interior layer. Conditional on all retained initialization, let
\(g\in\mathbb R^{2pn}\) concatenate their initialized incoming rows
and outgoing columns, as column vectors. Thus \(g\sim N(0,I_{2pn}/n)\).
The first-layer case omits the unused incoming blocks; the top case omits
the outgoing blocks. The bounds below allow all \(2p\) blocks and so
also cover these smaller Gaussian systems.

The reference is the independently stopped, zero-source cavity. The
learned mobility-coordinate displacement is divided by \(S\), as in
the reduction note's (21). The backward fields are divided by \(S\).
For fixed deterministic scalar controls, write
\[
e_a(t)=\sum_i x_i a_{a,i}(t),\qquad
\bar q_a(t)=\sum_i y_i b_{a,i}(t).
\tag{1}
\]
The control \(b_{a,i}\) is the scaled backward control. It already has
its factor \(S\) removed. The learned row/column errors and the omitted
top prediction offset are separate small sources, not part of the
Gaussian linear maps treated here.

All reference source constants below are the explicit recurrences of
`UNBOUNDED_COMPRESSOR_BRIDGE.md`: \(H_j,P_j,f_j,\tau_j,V_j,A_*,D_*,
\eta,\mathcal B,\mathcal K\). In particular
\(\|h^{(j)}\|_{2,n}\le H_j\),
\(\|\bar\delta^{(j)}\|_{2,n}\le\tau_j\), and reference mixers have
operator norm at most ten. Put \(\Gamma=\sqrt{\mathcal K}\),
\(\tau_* =\max_j\tau_j\), and \(f_* =\max_jf_j\).

The reference has preactivation imaginary parts at most \(7a/16\) under
its cavity pole stop. With \(\beta\) the original half-strip derivative
envelope, use the explicit third-derivative bound
\[
t_3=\max\{1,16\beta/a\}\le\beta^2.
\tag{2}
\]
Cauchy's formula applies to the second derivative on disks of radius
less than \(a/16\); taking the radius limit proves (2). No bound on
activation values is introduced.

The contour has length at most \(T_0\ell\), where one may take
\(T_0=32/\lambda+2c\) for physical radius \(c/\sqrt\ell\). Assume
the original short-contour deterministic gate, so
\(2\int\bar\rho\,|dt|\le1\), \(\bar\rho\le\lambda/8\), and
the variational propagator obeys
\[
J_n\le J_0 n^\kappa,\qquad
J_0=2e^{1/4}(2\mathcal B)^{1/4000},\qquad\kappa=1/4000.
\tag{3}
\]
This is the finite-coefficient bound already derived in reduction (24).

## 2. Raw coefficients with their logarithmic powers separated

Define
\[
M_0=\eta^{-1}[1+\log(2\mathcal B)],\quad
A_0=b+sM_0,\quad B_0=sM_0,\quad
E_0=A_*+SD_*M_0.
\tag{4}
\]
The stopped scaled carrier maximum is at most \(M_0\ell\); forward
and scaled reverse control amplitudes are at most \(A_0\ell,B_0\ell\),
respectively. Also \(M_\delta\le E_0\ell\).

The following recurrence supplies the control-speed coefficient:
\[
T_L^0=2sH_L+2tM_0V_L,\qquad
T_j^0=10sT_{j+1}^0+2s\tau_{j+1}^2H_j+2tM_0V_j,
\]
\[
D_0=\max\{\lambda s\max_jV_j/4,\lambda\max_jT_j^0/8\}.
\tag{5}
\]
Here \(D_0\) is local to this note and is not the integrated source's
trace constant with the same name. Each control has time Lipschitz
constant at most \(D_0\sqrt n\,\ell\). Equation (5) follows from
reduction (23), after bounding every occurrence of \(M_n\) by
\(M_0\ell\). The physical horizon times this Lipschitz coefficient
contains \(T_0D_0\), with the factor \(\lambda\) in \(D_0\)
explicit; the main horizon term \(32/\lambda\) cancels that factor.

Define the linear response coefficients
\[
v_0=J_0\{A_0(2T_0\Gamma\tau_*+E_0)+Sf_*B_0\},\qquad
z_j^0=P_j(Sv_0+A_0),\qquad h_j^0=s z_j^0,
\]
\[
k_L^0=v_0,\qquad d_j^0=s k_j^0+tM_0z_j^0,\qquad
k_j^0=10d_{j+1}^0+S\tau_{j+1}v_0+B_0\quad(j<L).
\tag{6}
\]
Their interpretation is an operator norm, from the concatenated root
vector \(g\) to the indicated *linear variation*, at fixed controls:
\[
\begin{array}{c|c}
\text{map}&\text{operator bound}\\ \hline
\text{scaled mobility displacement}&\sqrt p\,n^\kappa v_0\ell^2\\
z^{(j)},h^{(j)}&\sqrt p\,n^\kappa (z_j^0,h_j^0)\ell^2\\
\bar k^{(j)},\bar\delta^{(j)}&
\sqrt p\,n^\kappa(k_j^0,d_j^0)\ell^3.
\end{array}
\tag{7}
\]
The exact reduction (26)--(27) proves (7). The extra logarithm in the
backward row is introduced once, by multiplying a preactivation variation
by the reference scaled carrier. The recurrence propagates the resulting
term with the bounded factor \(10s\); it does not add one logarithm per
layer.

For a control difference of sup norm at most \(\epsilon\), define
\[
v_c=J_0(2T_0\Gamma\tau_*+E_0+Sf_*),\qquad
z_j^c=P_j(Sv_c+1),\qquad h_j^c=s z_j^c,
\]
\[
k_L^c=v_c,\qquad d_j^c=s k_j^c+tM_0z_j^c,\qquad
k_j^c=10d_{j+1}^c+S\tau_{j+1}v_c+1\quad(j<L),
\]
\[
C_c=\max\{v_c,\max_j(z_j^c,h_j^c,k_j^c,d_j^c)\}.
\tag{8}
\]
At a fixed reference the first-variation equation is linear in the
controls. Subtracting two histories therefore gives the same equations
with control amplitudes \(\epsilon\). Directly from reduction (26)--(27),
\[
\|L(t;\mathrm{controls})-L(t;\mathrm{controls}')\|_{\rm op}
\le C_c\sqrt p\,n^\kappa\ell^2\epsilon
\tag{9}
\]
for every linear map in (7). The first two rows actually require only
\(\ell\); the displayed common \(\ell^2\) bound is convenient.

## 3. Quadratic and bilinear response matrices

Let \(E_i\) select one omitted root block from \(g\), so
\(\|E_i\|_{\rm op}=1\). If \(L_\delta(t)\) is the linear map to an
upper scaled response, its pairing with that omitted outgoing root is
exactly
\[
(E_i g)^\top L_\delta(t)g
=g^\top R_i^\delta(t)g,\qquad
R_i^\delta(t)=\tfrac12[E_i^\top L_\delta(t)+L_\delta(t)^\top E_i].
\tag{10}
\]
For an incoming-root pairing with a lower feature variation, replace
\(L_\delta\) by \(L_h\). The transpose is algebraic also at complex
time. The matrices in (10) can be complex symmetric, while the roots
remain real Gaussian. Their real and imaginary parts are tested separately.

These are precisely the upper-response and lower-feature quadratic forms
in the original two insertion traces. Splitting the concatenation into
root blocks recovers the same-root quadratic form and the independent-root
bilinear forms. Only the selected root's diagonal block contributes to
\(\operatorname{tr}(R_i)/n\); off-diagonal root blocks have zero trace.
Thus centering (10) subtracts exactly the required same-root trace and
does not erase it.

Since symmetrization does not increase these operator bounds,
\[
\|R_i^\delta\|_{\rm op}\le\|L_\delta\|_{\rm op},\qquad
\|R_i^h\|_{\rm op}\le\|L_h\|_{\rm op},\qquad
\|\Delta R_i\|_{\rm op}\le C_c\sqrt p\,n^\kappa\ell^2\epsilon.
\tag{11}
\]
This supplies the quadratic-control modulus missing from reduction
(18b); no new Hessian estimate is needed. A bilinear form extracted as a
separate pair of blocks has the same bound, or can be handled directly
as part of (10).

On \(\|g\|_2\le2\sqrt{2p}\), whose failure is at most \(e^{-pn}\),
the difference of the *centered* forms is at most
\[
(\|g\|_2^2+2p)\|\Delta R_i\|_{\rm op}
\le10C_c p^{3/2}n^\kappa\ell^2\epsilon.
\tag{12}
\]
The \(2p\) term pays for \(|\operatorname{tr}(\Delta R_i)|/n\).
For \(\epsilon=n^{-1/8}\) and target \(n^{-1/10}/4\), the single
explicit gate
\[
40C_c p^{3/2}\ell^2\le n^{99/4000}
\tag{13}
\]
also covers linear control interpolation, whose root-norm multiplier is
only \(2\sqrt{2p}\). This is an ordinary polynomial-versus-logarithm
gate with the complete coefficient retained, not an unspecified eventual
width condition.

## 4. Reference speeds and the linear-response time derivative

The reference RMS speed coefficients are
\[
a_j^z=\lambda S^2V_j/4,\quad a_j^h=s a_j^z,\quad
a_j^W=\lambda S^2\tau_jH_{j-1}/4\ (j\ge2),
\quad a_j^\delta=\lambda T_j^0/8,
\]
\[
a_L^k=\lambda H_L/4,\qquad
a_j^k=a_{j+1}^W\tau_{j+1}+10a_{j+1}^\delta\quad(j<L).
\tag{14}
\]
Thus \(\|\dot z^{(j)}\|_{2,n}\le a_j^z\),
\(\|\dot h^{(j)}\|_{2,n}\le a_j^h\),
\(\|\dot W^{(j)}\|_{\rm op}\le a_j^W\), and
\(\|\dot{\bar\delta}^{(j)}\|_{2,n}\le a_j^\delta\ell\),
\(\|\dot{\bar k}^{(j)}\|_{2,n}\le a_j^k\ell\).
Converting a reference vector speed to a coordinate bound costs exactly
one factor \(\sqrt n\). These estimates follow by differentiating the
actual forward/backward recursions; (14) retains \(S^2\) where available.

The scaled reference vector field has Jacobian norm at most
\[
A_t\ell,\qquad A_t=2\mathcal K+(\lambda/4)S E_0.
\tag{15}
\]
The two terms respectively bound its negative Gram and residual Hessian.
Differentiating the linear variational ODE uses (15), not a derivative
of that Jacobian. Its instantaneous forcing is given by reduction (25).
Consequently its time derivative has operator norm at most
\(\sqrt p\,n^\kappa v_t\ell^3\), where
\[
v_t=A_t v_0+A_0(2\Gamma\tau_*+\lambda E_0/4)
+(\lambda/4)Sf_*B_0.
\tag{16}
\]
No derivative of a control occurs in (16), because the controls enter
the instantaneous forcing through their values.

The following forward recurrences do include control derivatives:
\[
z_1^t=Sv_t+D_0,\qquad h_1^t=s z_1^t+t a_1^z z_1^0,
\]
\[
z_j^t=S(H_{j-1}v_t+a_{j-1}^h v_0)
+a_j^W h_{j-1}^0+10h_{j-1}^t+D_0,
\qquad h_j^t=s z_j^t+t a_j^z z_j^0.
\tag{17}
\]
They bound the time derivatives of the forward linear maps by
\(\sqrt{pn}\,n^\kappa\ell^3(z_j^t,h_j^t)\).
For example, at a hidden layer the exact linear preactivation is
\[
z_{\rm lin}^{(j)}=(S V_{H^{(j)}}/\sqrt n)h^{(j-1)}
+W^{(j)}h_{\rm lin}^{(j-1)}+e_{\rm lin}^{(j)}.
\]
Differentiating this identity gives the four terms in \(z_j^t\) and
the control-speed term. Differentiating
\(h_{\rm lin}=\phi'(z)z_{\rm lin}\) gives the two terms in \(h_j^t\).
The gate term uses \(\|\dot z\|_\infty\le\sqrt n a_j^z\);
propagation of an already differentiated lower-layer map costs only
\(10s\). This explains why the factor \(\sqrt n\) is not raised to
the depth.

For the backward linear maps set
\[
k_L^t=v_t,
\]
\[
k_j^t=a_{j+1}^W d_{j+1}^0+10d_{j+1}^t
+S\tau_{j+1}v_t+S a_{j+1}^\delta v_0+D_0\quad(j<L),
\]
\[
d_j^t=s k_j^t+t a_j^z k_j^0
+(t_3M_0a_j^z+t a_j^k)z_j^0+tM_0z_j^t.
\tag{18}
\]
Their time derivatives have operator norm at most
\(\sqrt{pn}\,n^\kappa\ell^4(k_j^t,d_j^t)\). To check every term,
differentiate the exact identities
\[
\bar k_{\rm lin}^{(j)}=W^{(j+1)\top}\bar\delta_{\rm lin}^{(j+1)}
+(S V_{H^{(j+1)}}^\top/\sqrt n)\bar\delta^{(j+1)}
+\bar q_{\rm lin}^{(j)},
\]
\[
\bar\delta_{\rm lin}^{(j)}
=\phi'_j(z^{(j)})\odot\bar k_{\rm lin}^{(j)}
+\phi''_j(z^{(j)})\odot\bar k^{(j)}\odot z_{\rm lin}^{(j)}.
\]
The second identity produces a changed linear carrier, a changed first
gate, a third-derivative gate term, a changed reference carrier, and a
changed linear preactivation. These are precisely the five contributions
in \(d_j^t\). In particular only the last contribution adds a logarithm
to the forward time bound; all backward propagation is through \(10s\).

## 5. Lower probes and a usable terminal-time grid

The omitted incoming-row probes are restrictions of the augmented forward
Jacobian to a lower preactivation port. Their time modulus can be bounded
without the controls. For the augmented derivative maps used to define
\(P_j,f_j\), put
\[
z_1^J=0,\quad h_1^J=t a_1^zP_1,\qquad
z_j^J=a_{j-1}^h+a_j^W f_{j-1}+10h_{j-1}^J,
\quad h_j^J=s z_j^J+t a_j^zP_j.
\tag{19}
\]
Their derivatives have operator norm at most
\(\sqrt n(z_j^J,h_j^J)\). The direct parameter and additive-port
maps in the first layer are constant in time. At higher layers,
differentiate \(U_Hh/\sqrt n+W Dh+U_e\); this gives (19).
Restriction to a port and taking the transpose preserve the operator
bound, so (19) covers every lower adjoint probe used in the Gaussian event.

Define the fully explicit coefficient
\[
C_t=\max\{v_t,\max_j(z_j^t,h_j^t,k_j^t,d_j^t,z_j^J,h_j^J)\}.
\tag{20}
\]
Every relevant linear map has terminal-time derivative at most
\(C_t\sqrt{pn}\,n^\kappa\ell^4\); by (10), so does every relevant
quadratic response matrix. Their operator moduli on a real contour
segment are therefore bounded by this coefficient times segment length.
For a complex source rectangle, use analytic controls and reference maps
on the pre-stop rectangle, which include the actual network controls.
The linear ODE is then holomorphic and the same derivative identities
hold for complex time. Joining neighboring grid points inside that
rectangle costs at most \(\sqrt2\) times the rectangular mesh size.

This complex assertion does not claim path independence for arbitrary
nonanalytic two-dimensional control fields. At each grid point the
conditional Gaussian union may use a net of one-dimensional control
restrictions along its chosen contour. That net contains the restrictions
of the actual analytic controls to the prescribed accuracy. Off-grid
interpolation uses the derivative bound for those actual controls, after
the uniform grid event is established. This respects their possible
dependence on the omitted Gaussian roots.

For independently stopped real reference paths, freezing preserves their
Lipschitz bounds. For rectangle prefixes, coordinatewise clamping to each
reference's own rectangle is nonexpansive and preserves the corresponding
path-length bound. These extensions use retained initialization only.
They introduce no conditioning on the full network's survival event.
Interpolation for the actual trajectory is used only on its common
pre-stop rectangle, where all the analytic identities hold.

On the root-norm event, both linear differences and centered quadratic
differences are less than \(n^{-1/10}/4\) for mesh size at most
\[
h_t=\min\left\{1,
\frac{n^{-1/10-1/2-\kappa}}
{80p^{3/2}(1+C_t)\ell^4}\right\}.
\tag{21}
\]
For the quadratic bound use \(10p\) from (12), then the \(\sqrt2\)
path-length factor. The coefficient \(10\sqrt2/80\) is less than
\(1/4\). The linear root factor is smaller. A rectangle of real length
\(T_H+2r_t\) and imaginary width \(2r_t\), where
\(T_H=32\ell/\lambda\) and \(r_t=c/\sqrt\ell\), needs at most
\[
N_t\le[2+(T_H+2r_t)/h_t][2+2r_t/h_t]
\tag{22}
\]
grid points, including boundaries. This expression supplies the actual
terminal-grid count for the probability union. It is not replaced by
\(n^C\) before its parameter coefficient is paid.

## 6. Polynomial dependence and claim boundary

Equations (4)--(8), (14)--(20) are finite recurrences involving only sums,
products, maxima, and the explicit constant \(J_0\). The only depth
propagation multipliers are fixed numerical multiples of \(s\), not
\(M_0\), \(T_0\), or a reciprocal gap. In (6), the factor \(M_0\)
enters the backward forcing once; in (18) a further such factor multiplies
a forward time bound once. More precisely, holding the other displayed
source constants fixed, \(C_c\) has degree at most two in \(M_0\),
\(C_t\) has degree at most four, and both have degree at most one in
\(T_0\). Maxima can be bounded by the corresponding sums for this degree
statement. None contains \(1/S\), and \(p\)
occurs only through the displayed square-root and grid/union factors.
The explicit source recurrences have \(\beta^{CL}\) envelopes; the
recurrences here preserve that form because their depth products are
\((10s)^L\) and the forcing terms are a fixed number of products of
source bounds. No unspecified \(C_p\) is used in these conclusions.

For clarity, this is a proof of the linear-Gaussian map interfaces. The
control-grid extension uses (13), the terminal-grid extension uses
(21)--(22), and centered quadratic traces are charged in (12).
The nonlinear source remainders, the all-deletion initialization transfer,
and common-cavity probability composition must still be checked before
asserting an explicit success width for the trained source. Nothing in
this note supplies a compact decoder or resolves its passive-query error.

The complete original sources and required skills are those recorded in
`QUANTITATIVE_INSERTION_WIDTH.md`; their source hashes are unchanged.
That checked note was read as the current algebraic interface. No other
agent's new nonlinear lemma was read or assumed, no source file was
changed, and no experiment or Git operation was performed.
