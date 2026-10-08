# Ordered sample responses: a conditional all-time closure and its cost

This scoped route derives the exact response hierarchy, a finite autonomous
truncation, and an all-time error theorem under explicit response-radius and
control-budget hypotheses. It does not establish those hypotheses uniformly
in width for the full requested deep-network class, nor give subpolynomial
state size under ordinary analytic response bounds.

The hierarchy, control-radius bootstrap, factorial-versus-geometric tail
distinction, and word-count calculation were derived before reading the two
authorized same-study inputs `RESPONSE_MEMORY.md` and
`OBSERVABLE_GEOMETRY.md`. Both files were then read completely. The final
feedback proof uses their residual-weighted Gronwall observation to avoid an
unnecessary additional small-gain restriction. No literature, experiments,
other-study material, or Git operation was used. This is a research candidate,
not promoted theory.

## 1. Canonical model and the meaning of a sample response

There are \(m\) training inputs \(v_b\), fixed labels \(y_b\), width \(n\),
and an arbitrary fixed hidden depth \(L\). A finite passive evaluation panel
may also be present. The network is

\[
z_a^{(1)}=Av_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\qquad
f_a=\frac1n w^\top h_a^{(L)}.
\]

Here the first activation also means \(h_a^{(1)}=\phi(Av_a)\),
\(A\in\mathbb R^{n\times d}\),
\(W^{(\ell)}\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\).
Using normalized inputs \(v_a=x_a/\sqrt d\) gives exactly the first-layer
convention in `OBSERVABLE_GEOMETRY.md`. Set

\[
c_a=y_a-f_a,\qquad
\mathcal L=\frac1m\sum_{a=1}^m c_a^2,\qquad \alpha=\frac2m.
\]

The backward signals are

\[
\delta_a^{(L)}=w\odot\phi'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

Let \(\theta=(A,W^{(2)},\ldots,W^{(L)},w)\). Define the residual-free
sample vector field \(V_b\) through its actual parameter components:

\[
V_bA=\delta_b^{(1)}v_b^\top,\qquad
V_bW^{(\ell)}=\frac1n\delta_b^{(\ell)}h_b^{(\ell-1)\top},\qquad
V_bw=h_b^{(L)}.
\]

For any differentiable scalar observable \(O\),
\(V_bO=DO(\theta)[V_b(\theta)]\). With the stipulated mobilities
\((n,1,\ldots,1,n)\), the dense flow is exactly

\[
\dot\theta=\alpha\sum_b c_bV_b(\theta),\qquad
\dot O=\alpha\sum_b c_bV_bO.
\]

This definition has no residual denominator and remains regular at zero
residual. The field \(V_b\) is the parameter write caused by one unit of
sample \(b\)'s force, including both readout learning and feature learning.
Writing the mobility operator as \(\mathsf M\), one has
\(V_b=\mathsf M\nabla_\theta f_b\), so

\[
K_{ab}=V_bf_a
=\nabla_\theta f_a^\top\mathsf M\nabla_\theta f_b
\]

is the symmetric gradient Gram kernel on the training samples. This section
uses the original dense flow, not the distinct corrected metric runtime in
the later part of `OBSERVABLE_GEOMETRY.md`.

For a word \(\mathbf b=(b_1,\ldots,b_k)\), define

\[
R_{a;\mathbf b}=V_{b_k}\cdots V_{b_1}f_a,
\qquad R_{a;\varnothing}=f_a.
\]

The rightmost differential operator acts first. These are responses to
sequential sample forces, rather than physical-time derivatives. For example,
if \(\Phi_b^s\) is the local flow of \(V_b\), then

\[
R_{a;b_1\ldots b_k}(\theta)
=\left.\partial_{s_1}\cdots\partial_{s_k}
f_a\big(\Phi_{b_1}^{s_1}\circ\cdots\circ
\Phi_{b_k}^{s_k}(\theta)\big)\right|_{s_1=\cdots=s_k=0}.
\]

Thus the listed word is reverse chronological as a sequence of actual state
impulses. It agrees with the prompt's operator convention; reversing its word
gives the convention used for \(C_{O,w}\) in `OBSERVABLE_GEOMETRY.md`.
The force fields themselves change during a response. In particular,

\[
V_cV_bf_a
=D^2f_a[V_c,V_b]+Df_a[DV_b\,V_c],
\]

so a response is not merely a frozen-direction Hessian contraction. Its second
term records how the earlier parameter write changes the subsequent force.

## 2. Exact hierarchy and its first approximation

Appending a driving index gives the exact infinite hierarchy

\[
\dot R_{a;\mathbf b}
=\alpha\sum_{d=1}^m c_dR_{a;\mathbf b d},\qquad
c_d=y_d-R_{d;\varnothing}.
\]

All response coordinates are initialized by their displayed derivatives at the
given \(\theta_0\). Fix \(q\ge1\). The finite order-\(q\) approximation is

\[
\begin{aligned}
\dot{\widehat R}_{a;\mathbf b}
&=\alpha\sum_d\widehat c_d\widehat R_{a;\mathbf b d},
&&|\mathbf b|<q,\\
\dot{\widehat R}_{a;\mathbf b}&=0,
&&|\mathbf b|=q,\\
\widehat c_d&=y_d-\widehat R_{d;\varnothing},
&&\widehat R_{a;\mathbf b}(0)=R_{a;\mathbf b}(\theta_0).
\end{aligned}
\]

The first approximation is freezing the highest response level. Lower levels
are moving, mechanistically specified sample responses. The equations are
autonomous and restartable from their finite state; they use no later dense
weights or recorded prediction trajectory.

If there are \(P\) evaluated outputs, the literal construction retains

\[
P\sum_{k=0}^{q-1}m^k\quad\text{moving scalars},\qquad
Pm^q\quad\text{fixed highest-order coefficients}.
\]

The initial values at lower levels are additional initialization data but need
not be separately retained once evolution begins. Evaluating all these ordered
derivatives of the initialized dense network may itself be costly. No fast
initialization algorithm or further tensor compression is assumed.

To understand the truncation, define the actual accumulated controls
\(u_b(t)=\alpha\int_0^t c_b(s)\,ds\). For a supplied control path let

\[
I_{b_1\ldots b_k}[u](t)
=\int_{0<s_k<\cdots<s_1<t}
du_{b_1}(s_1)\cdots du_{b_k}(s_k),\qquad I_\varnothing=1.
\]

These integrals have the same reverse chronological convention as the response
words. With \(U(t)=\sum_b\int_0^t|du_b|\),

\[
\sum_{|\mathbf b|=k}|I_{\mathbf b}[u](t)|\le\frac{U(t)^k}{k!}.
\]

Replace each differential by its absolute-variation measure and sum the index
choices; the resulting integrand is symmetric on the full time cube, whose
ordered simplices give the factor \(1/k!\). Repeated integration of the
hierarchy shows that its supplied-control truncation evaluates

\[
\widehat R_{a;\mathbf b}[u](t)
=\sum_{k=0}^{q-|\mathbf b|}\sum_{|\mathbf d|=k}
R_{a;\mathbf b\mathbf d}(\theta_0)I_{\mathbf d}[u](t).
\]

Its residual is an ordered integral of the next responses at intermediate
states. This identity proves which coefficients are discarded and is not an
assumption that the hierarchy terminates.

## 3. Conditional all-time theorem for ordinary analytic response bounds

The following assumptions are explicit extra hypotheses. They have not been
deduced here from strip analyticity and the existing small-label cap.

Assume that the unit-force system is well posed for every real supplied
control of total variation at most \(U_*\), and that all these states stay in
a fixed admissible region where solutions continue through finite physical
times whenever the control variation stays strictly below \(U_*\).
Suppose constants \(B,r>0\) satisfy

\[
|R_{a;\mathbf b}(\theta)|\le B\,k!\,r^{-k},\qquad
|\mathbf b|=k\ge1,
\]

for all such states, all words, and all requested outputs. This is a bound on
an entire reachable control ball, not a coefficient sampled from the future
training trajectory. A static analytic tube can certify it, as discussed
below. Assume also that the training kernel at initialization obeys
\(K_0\succeq\lambda I_m\), with \(\lambda>0\).

Put

\[
e_0=\|y-f(0)\|_2,\qquad
U_0=\frac{2\sqrt m\,e_0}{\lambda}.
\]

Require the radius/coercivity inequalities

\[
U_0<U_*<r,\qquad
\frac{mB}{r}\left[(1-U_*/r)^{-2}-1\right]\le\frac\lambda2.
\tag{A}
\]

For zero readout, \(f(0)=0\), so \(e_0=\|y\|_2\). Condition (A) may
hold for sufficiently small fixed labels when the other constants are fixed.
It is not identified with an already supplied small-label condition without
checking its constants. It imposes no width-dependent label shrinkage.

Define

\[
x=\frac{U_0}{r}<1,\qquad
L_K=\frac{2mB}{r^2}(1-x)^{-3},\qquad
\beta=\frac{2L_KU_0}{\lambda},\qquad
\varepsilon_q=\frac{mB(q+1)}r x^q.
\]

**Conditional theorem.** The dense and order-\(q\) response systems both
exist for all physical times, their training residuals obey

\[
\|c(t)\|_2,\ \|\widehat c(t)\|_2
\le e_0e^{-\alpha\lambda t/2},
\]

and their total absolute control variations are at most \(U_0\). Their
training predictions satisfy

\[
\sup_{t\ge0}\|\widehat f(t)-f(t)\|_2
\le\frac{2e_0}{\lambda}\varepsilon_q e^\beta.
\tag{B}
\]

For each passive evaluated output, one also has

\[
\sup_{t\ge0}|\widehat f_a(t)-f_a(t)|
\le Bx^{q+1}
+\frac{B}{r}(1-x)^{-2}
\frac{\varepsilon_q}{L_K}(e^\beta-1).
\tag{C}
\]

All constants in these statements are independent of \(q\). They are
independent of width only when the assumptions supply width-uniform constants.
No additional condition \(\beta<1\) is needed.

### Proof: control budget and coercivity

For a supplied control with variation at most \(U_*\), the controlled series
for a kernel entry uses responses of length \(k+1\). Thus both the exact
kernel and its truncated controlled version obey

\[
\|K[u](t)-K_0\|,\quad
\|\widehat K_q[u](t)-K_0\|
\le\frac{mB}{r}\sum_{k\ge1}(k+1)(U_*/r)^k
\le\frac\lambda2.
\]

The exact series converges because its integral remainder of order \(q\)
is bounded by \(B(q+1)r^{-1}(U_*/r)^q\), which tends to zero. The matrix
norm bound uses \(\|M\|_2\le m\max_{a,b}|M_{ab}|\).
The truncated kernel may be nonsymmetric; its symmetric part is nevertheless
at least \(\lambda I/2\). Both residual equations
\(\dot c=-\alpha Kc\) therefore give the asserted decay as long as their
controls stay within the budget. Integrating this decay gives

\[
\sum_b\int_0^\infty|du_b|
\le\alpha\sqrt m\int_0^\infty\|c(t)\|_2dt
\le U_0<U_*.
\]

A first-exit argument prevents exhaustion of \(U_*\). The dense system
continues by the admissible-region hypothesis. Every truncated response is a
finite controlled polynomial bounded at variation \(U_0\), so the finite
ODE cannot have a finite-time blow-up and also continues globally.

### Proof: source error, changed controls, and feedback

For the same supplied control of variation at most \(U_0\), repeated
integration with a kernel observable leaves a length-\(q\) remainder with
response bound \(B(q+1)!r^{-(q+1)}\). The integral estimate therefore gives

\[
\|K[u](t)-\widehat K_q[u](t)\|\le\varepsilon_q.
\]

For two controls \(u,v\), each of variation at most \(U_0\), interpolation
between them shows

\[
\sum_{|\mathbf b|=k}|I_{\mathbf b}[u]-I_{\mathbf b}[v]|
\le\frac{U_0^{k-1}}{(k-1)!}
\sum_b\int_0^t|du_b-dv_b|.
\]

Indeed, differentiate the product integral along the interpolation. There is
one difference differential and \(k-1\) common differentials. Summing its
possible ordered positions integrates the latter over their complete ordered
simplex around the distinguished time and gives the displayed factor.
Using response coefficients of length \(k+1\) and summing
\(\sum_{k\ge1}k(k+1)x^{k-1}=2(1-x)^{-3}\) yields

\[
\|\widehat K_q[u](t)-\widehat K_q[v](t)\|
\le L_K\sum_b\int_0^t|du_b-dv_b|.
\]

Now let \(e=\widehat f-f\) on the training set and define

\[
E(t)=\alpha\sqrt m\int_0^t\|e(s)\|_2ds.
\]

The difference of the two actual controls has variation at most \(E(t)\),
so \(\|\widehat K-K\|\le\varepsilon_q+L_KE(t)\). Subtracting the output
equations gives

\[
\dot e=-\alpha\widehat Ke+\alpha(\widehat K-K)c,
\qquad e(0)=0.
\]

The homogeneous propagator has norm at most
\(e^{-\alpha\lambda(t-s)/2}\), as follows by differentiating the squared
Euclidean norm and using the symmetric-part bound. Variation of constants and
integration in time therefore imply

\[
E(t)\le\frac{2\alpha\sqrt m}{\lambda}
\int_0^t[\varepsilon_q+L_KE(s)]\|c(s)\|_2ds.
\]

Integrating the scalar differential inequality for the right-hand side gives

\[
E(t)\le\frac{\varepsilon_q}{L_K}
\left[\exp\left(\frac{2\alpha\sqrt mL_K}{\lambda}
\int_0^t\|c(s)\|_2ds\right)-1\right]
\le\frac{\varepsilon_q}{L_K}(e^\beta-1).
\]

This residual-weighted Gronwall bound is finite for every fixed \(\beta\);
using a supremum too early would introduce an unnecessary small-gain condition.
Consequently \(\|\widehat K-K\|\le\varepsilon_qe^\beta\), and the same
propagator estimate, with \(\|c(s)\|_2\le e_0\), proves (B).

For a passive output, the supplied-control output remainder is at most
\(Bx^{q+1}\). The same interpolation argument for length-\(k\) response
coefficients gives output Lipschitz constant
\((B/r)\sum_{k\ge1}kx^{k-1}=(B/r)(1-x)^{-2}\) with respect to control
variation. Combining this with the bound for \(E\) proves (C).

## 4. Which analytic estimates are real inputs

The factorial response bound can be certified without future trajectory data.
For example, suppose a statically specified reachable region has a complex
tube of radius \(\rho\) in a chosen parameter norm. Suppose the unit sample
fields have norm at most \(M\), and each output has magnitude at most \(F\)
throughout that tube. Cauchy's one-variable derivative formula along a vector
of norm at most \(M\) bounds one response derivative across a tube loss
\(\delta\) by \(M/\delta\) times the preceding supremum. Allocate tube
loss \(\rho/k\) at each of \(k\) steps. Then

\[
|R_{a;\mathbf b}|
\le F(kM/\rho)^k
\le F k!(eM/\rho)^k.
\]

The last inequality uses
\(\log k!\ge\int_1^k\log s\,ds\ge k\log k-k\).
Thus \(B=F\) and \(r=\rho/(eM)\) suffice. A slightly smaller tube handles
boundary suprema if the given domain is open. Unit-force displacement bounds
can likewise certify that the entire control ball stays inside the selected
region.

This is a meaningful conditional certificate, but it does not automatically
have width-uniform constants. In a deep initialized network one must control
the normalized force fields, backward signals, complex activation arguments,
and outputs in the chosen norm. Bounded derivatives on a strip do not bound
activation values on the real line. Gaussian coordinates and large weight
blocks therefore cannot simply be put in a fixed coordinatewise box. The
fixed depth is allowed to enter the constants; hidden width dependence is not.
Proving an appropriate normalized tube or a direct moment-based response
bound remains necessary for the full stated class.

## 5. Accuracy versus the number of response words

Assume, conditionally, that all theorem constants are independent of width and
that \(m\ge2\) is fixed. For fixed nonzero labels the ratio \(x=U_0/r\) is
a fixed number in \((0,1)\). The certified error is a constant times
\((q+1)x^q\). Accuracy \(n^{-s}\), for \(s=1/2\) or \(s=1\), is
certified through this bound by choosing

\[
q=\frac{s\log n}{|\log x|}+O(\log\log n).
\]

The literal storage bound then is

\[
m^q=n^{s\log m/|\log x|+o(1)}.
\]

This is polynomial in width with a fixed positive exponent, even if small
fixed labels make that exponent modest. It is not \(n^{o(1)}\). This
calculation is a limitation of the available bound and the literal full-word
construction, not a lower bound for all response representations or even a
proof that this bound is sharp for a particular instance.

The signature factorial \(1/k!\) has already canceled the factorial growth
of ordinary analytic responses. Counting it a second time would incorrectly
predict a \(q\sim\log n/\log\log n\) requirement. Making the label scale
shrink with width could change \(x\); it is not allowed here. When \(m=1\),
there is only one word per length, so \(O(\log n)\) response coordinates do
suffice under the same conditional theorem. That exception does not resolve
the multiple-sample question.

One possible improvement is a proved finite response algebra or low-rank
factorization allowing all required word contractions to be evolved with
polynomial-in-\(q\) storage. Word reorderings generally do not suffice:
sample force fields need not commute. No such factorization is proved here.

## 6. A stronger response bound would give subpolynomial storage

There is a precise constructive alternative, under a substantially stronger
hypothesis. Suppose the same reachable control ball instead satisfies

\[
|R_{a;\mathbf b}(\theta)|\le B\omega^k,
\qquad |\mathbf b|=k\ge1,
\]

with fixed \(B,\omega\), and assume

\[
U_0<U_*,\qquad
mB\omega(e^{\omega U_*}-1)\le\lambda/2.
\]

The same proof applies, now with

\[
\varepsilon_q=mB\omega\frac{(\omega U_0)^q}{q!},\qquad
L_K=mB\omega^2e^{\omega U_0}.
\]

The control and feedback estimates remain all-time; the output remainder is
\(B(\omega U_0)^{q+1}/(q+1)!\). For fixed constants, taking
\(q=O(\log n/\log\log n)\) makes the error \(O(n^{-s})\) for any fixed
\(s>0\). For example a leading coefficient larger than \(s\) in that
choice suffices, because
\(\log q!=q\log q-q+O(\log q)\). The latter estimate follows by bounding
the increasing sum \(\sum_{j=1}^q\log j\) between its adjacent integrals.
The literal word storage is then

\[
m^q=\exp(O(\log n/\log\log n))=n^{o(1)}.
\]

This supplies a conditional all-time theorem with the requested modest state
scale. Its response-growth assumption is stronger than an entire activation,
let alone a bounded strip derivative.

An explicit canonical deep example shows the distinction. Take one neuron,
one training sample, two hidden layers, and linear activation
\(\phi(z)=z\). Write the three scalar parameters as \((a,b,w)\), so
\(f=abw\) and the residual-free unit force is

\[
V=bw\,\partial_a+aw\,\partial_b+ab\,\partial_w.
\]

At \((a,b,w)=(1,1,0)\), its controlled solution at force amount \(u\) is

\[
a(u)=b(u)=\sec u,\qquad w(u)=\tan u,\qquad
f(u)=\tan u\,\sec^2u.
\]

These formulas satisfy the displayed field and initial data directly. They
have a finite singularity at \(u=\pi/2\), although \(\phi'=1\) is bounded
on every complex strip and \(\phi\) is entire. A bound
\(|V^kf(\theta_0)|\le B\omega^k\) for all \(k\) would give an entire
Taylor series for this controlled output, contradicting that singularity.

This issue is not limited to the exactly equal initial hidden weights. If
\(a_0,b_0>0\), the invariants
\(a^2-w^2=a_0^2\) and \(b^2-w^2=b_0^2\) give

\[
\frac{dw}{du}=\sqrt{w^2+a_0^2}\sqrt{w^2+b_0^2},\qquad
u_* =\int_0^\infty
\frac{dw}{\sqrt{w^2+a_0^2}\sqrt{w^2+b_0^2}}<\infty.
\]

The integral is finite near zero because \(a_0b_0>0\), and at infinity
because its integrand is \(O(w^{-2})\). Thus the unit-force output has a
finite real singularity on an event of positive Gaussian initialization
probability. A sufficiently small fixed training label may keep the feedback
path far from that singularity; it does not turn the unit-force response
series into an entire function. This example refutes the inference from
activation analyticity to the stronger response bound, not a general
finite-closure theorem or a high-width complexity claim.

## 7. Result and remaining proof obligations

The finite hierarchy is a transparent autonomous construction: each state
records the effect of a specified sequence of sample writes on an evaluated
output. Initialization uses only the initialized network. Its truncation is
not exact closure, but assumptions (A) and the stated response bounds give a
complete all-time training and passive-output error theorem.

For the requested arbitrary fixed depth and activation class, two decisive
questions remain. First, do the actual existing initialization, gap, and
small-label hypotheses imply suitable width-uniform response-radius and
reachable-region estimates, without strengthening their label restrictions?
Second, can the response words be represented more economically, or can their
growth be improved beyond the ordinary factorial analytic bound? Neither
question is answered by an exact hierarchy or by its finite-order correctness.

The note therefore establishes the conditional theorem and the cost of its
literal witness. It does not establish an unconditional
\(n^{-1/2}\) or \(n^{-1+o(1)}\) all-time approximation with
\(n^{o(1)}\) aggregate state for the full deep model. A probability claim
would additionally require proving that the certificate constants hold on an
initialization event of the stated probability. No Gaussian concentration
claim for those constants is made here.

The author checked the word orientation, mobility normalization, integral
remainders, coercivity bootstrap, absence of an unnecessary small-gain
restriction, passive-output transfer, moving/fixed storage counts, and the
deep-linear controlled singularity. This candidate awaits comparison or
independent checking.
