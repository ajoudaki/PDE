# A finite initialized-jet bound gives a width-uniform real Taylor remainder

This scoped proof concerns the original frozen-top neural tangent hierarchy
through its comparison with the actual dense flow. It introduces no replacement
closure. Its purpose is to turn bounds on finitely many initialized state jets
into a small-time prediction remainder without proving that the actual complex
trajectory stays in a width-independent coordinate tube.

The model here is the supervisor's sinusoidal activation family,
\(\phi_\varepsilon(z)=z+\varepsilon\sin z\),
\(\varepsilon\in[1/8,1/4]\), with a linear second activation. It is a different
activation family from the tanh calculation in `AVERAGED_UPPER.md`. The proof
below is conditional only on an explicit finite initialized-jet event. The
same-study Gaussian-forest calculation of `/root/nth_gaussian_tail_lower` is
used in Section 5 after a complete independent check of its proof. Its
probability is kept separate from the deterministic lemma.

Author: `/root/nth_average_upper`, 2026-10-10. Inputs: the supervisor's scoped
assignment; the generic-route author's exact transformed equations, omitted
physical-time jet identity, and proposed label/activation range; required
notation, proof, and research instructions; and, for Section 5, the complete
same-study `INITIAL_JET_MOMENTS.md`. No experiment, archived chapter,
other study, external scientific source, or Git operation was used.

Same-study check: `/root/tanh_nth_generic` independently read Sections 1--6
at SHA-256 `b15e09f083054751ce28bdb0a6a8ec505e3f02dcded245cd3ad4f8dbbff47a69`
and then the complete sharpened Section 7 at SHA-256
`87698c5dcf3f5db71416cea2f84fe2e93be9cbe73eb16da4a3e0b3ce912877ab`,
reporting no gap in either check. Its check treats the initialized-jet
event as the separately checked input documented in Section 5. These are
internal research checks, not independent promotion reviews. This status
record changes no mathematical statement or proof in the checked versions.

## 1. Exact model and a change of coordinates used only in the proof

There are two orthogonal unit inputs \(v_1,v_2\), width \(n\), and labels
\((\eta,0)\), with fixed \(0<\eta\le1\). The network, loss, and mobility are

\[
z_a=W^{(1)}v_a,\quad h_a=\phi_\varepsilon(z_a),\quad
h_a^{(2)}=W^{(2)}h_a,\quad f_a=u^\top W^{(2)}h_a/n,
\]
\[
\mathcal L=\tfrac14\sum_{a=1}^2(f_a-y_a)^2,
\qquad M=\operatorname{diag}(n,1,n).
\]

Initialization is the stated independent Gaussian initialization of
\(W^{(1)},W^{(2)}\), with variances \(1,1/n\), and \(u_0=0\). The deterministic
lemma below also applies to any initialization satisfying its explicit bounds.

Since \(3/4\le\phi_\varepsilon'(z)\le5/4\) for real \(z\), the function

\[
T_\varepsilon(z)=\int_0^z\frac{dw}{\phi_\varepsilon'(w)}
\]

is a smooth increasing bijection of the real line. Define

\[
\zeta_a=T_\varepsilon(z_a)/\sqrt n,\quad
U=u/\sqrt n,\quad W=W^{(2)},\quad
H_\varepsilon=\phi_\varepsilon\circ T_\varepsilon^{-1},
\]
\[
A_{n,\varepsilon}(\zeta)_i
=H_\varepsilon(\sqrt n\,\zeta_i)/\sqrt n,
\qquad \beta_a=(y_a-f_a)/2.
\]

All scalar functions act coordinatewise. The prediction and physical-time
flow become exactly

\[
f_a=U^\top W A_{n,\varepsilon}(\zeta_a),
\tag{1}
\]
\[
\begin{aligned}
\dot\zeta_a&=\beta_a W^\top U,\\
\dot U&=W\sum_{a=1}^2\beta_a A_{n,\varepsilon}(\zeta_a),\\
\dot W&=U\left(\sum_{a=1}^2\beta_a A_{n,\varepsilon}(\zeta_a)\right)^\top.
\end{aligned}
\tag{2}
\]

For example, the original first-layer equation is
\(\dot z_a=\beta_a\phi_\varepsilon'(z_a)\odot W^\top u\), because the
inputs are orthogonal. Multiplication by
\(T_\varepsilon'(z_a)/\sqrt n\) gives the first line of (2). The other
two lines follow by substituting \(u=\sqrt n U\) and
\(h_a=\sqrt n A_{n,\varepsilon}(\zeta_a)\) in the original equations.
Thus this coordinate change preserves physical time and the prediction.
The NTH itself continues to be defined from the original mobility and
the actual initialized tensors.

Write \(D=W-W_0\) and use the product norm

\[
\|(\zeta_1,\zeta_2,U,D)\|
=\|\zeta_1\|_2+\|\zeta_2\|_2+\|U\|_2+\|D\|_F.
\tag{3}
\]

The fixed matrix \(W_0\) is bounded in operator norm, not Frobenius norm.
Let \(\mathcal F_n\) denote the right-hand side of (2) in these variables.

## 2. Uniform scalar and real stability bounds

For real \(\tau\),

\[
H_\varepsilon'(\tau)
=\phi_\varepsilon'(T_\varepsilon^{-1}(\tau))^2
\in[9/16,25/16].
\tag{4}
\]

Since \(H_\varepsilon(0)=0\), the map \(A_{n,\varepsilon}\) is Lipschitz
in the Euclidean norm with constant \(25/16<2\), uniformly in \(n\) and
\(\varepsilon\). It also obeys \(\|A_{n,\varepsilon}(\zeta)\|_2\le2\|\zeta\|_2\).

Fix \(L_0\ge1\), assume \(\|W_0\|_{\rm op}\le L_0\), and restrict the
state norm (3) to a fixed bounded ball. Equations (1)--(4) imply uniform
bounds and a uniform real Lipschitz constant for \(\mathcal F_n\) and for
each prediction. For clarity, on a ball where all vector norms and
\(\|W\|_{\rm op}\) are at most \(L\),

\[
|f_a|\le2L^3,
\]

and the difference of two predictions is bounded by
\(2L^2\) times the sum of the differences in \(U,W,\zeta_a\), using
\(\|\Delta W\|_{\rm op}\le\|\Delta W\|_F\). The residual controls inherit
this Lipschitz bound. Each right-hand side in (2) is a product of these
bounded Lipschitz factors; for the matrix equation use
\(\|ab^\top\|_F=\|a\|_2\|b\|_2\). These estimates prove the assertion
with constants depending only on \(L_0,\eta\) and the chosen ball.

Consequently an initial state of norm at most \(L_0\) has a real solution
on a fixed positive interval, inside a slightly larger fixed ball, with
uniform stability there. To justify uniform existence, stop at a first exit
from that ball. Its uniformly bounded velocity requires a fixed positive
time to cover the fixed distance to the boundary. At each fixed \(n\),
ordinary smooth ODE continuation applies before exit. This argument does
not require a bound on the largest coordinate of the true trajectory.

We also need a scalar complex extension, but only near real scalar points.
There is a uniform disk \(|s|<1/16\) around every real \(\tau_0\) on which
\(H_\varepsilon(\tau_0+s)\) is holomorphic and

\[
|H_\varepsilon(\tau_0+s)-H_\varepsilon(\tau_0)|\le4|s|.
\tag{5}
\]

To prove this, put \(z_0=T_\varepsilon^{-1}(\tau_0)\) and solve
\(z'(s)=1+\varepsilon\cos z(s)\), \(z(0)=z_0\). On
\(|z-z_0|\le1/4\), the vector field has modulus less than two, and its
derivative has modulus less than \(1/3\), uniformly in real \(z_0\) and
the stated \(\varepsilon\) interval. The integral equation on
\(|s|\le1/16\) maps the holomorphic supremum ball
\(\|z-z_0\|_\infty\le1/4\) into the ball of radius \(1/8\), and has
Lipschitz constant at most \(1/48\). Its uniformly convergent Picard
sequence supplies the holomorphic solution. The real solution is
\(T_\varepsilon^{-1}(\tau_0+s)\); uniqueness identifies the extension.
Finally \((\phi_\varepsilon(z(s)))'=\phi_\varepsilon'(z(s))^2\) has modulus
at most four, proving (5).

## 3. Deterministic finite-jet-to-remainder lemma

Let \(R\ge1\), and write the Taylor coefficients of the exact transformed
state at initialization as

\[
\zeta_{a,j}=\frac{\zeta_a^{(j)}(0)}{j!},\qquad
U_j=\frac{U^{(j)}(0)}{j!},\qquad
D_j=\frac{D^{(j)}(0)}{j!}.
\]

Assume the initial norm in (3) is at most \(L_0\),
\(\|W_0\|_{\rm op}\le L_0\), and for some \(M\ge1\), for every
\(1\le j\le R\),

\[
\|\zeta_{1,j}\|_2+\|\zeta_{2,j}\|_2+\|U_j\|_2+\|D_j\|_F\le M,
\qquad
\max_{a,i}\sqrt n\,|\zeta_{a,j,i}|\le M.
\tag{6}
\]

There are constants \(C,D_*\ge1\), depending only on \(L_0,\eta\), such
that for each output \(a\) and each real \(0\le t\le(2D_*M)^{-1}\),

\[
\left|f_a(t)-\sum_{j=0}^R\frac{f_a^{(j)}(0)}{j!}t^j\right|
\le C(D_*M)^{R+1}t^{R+1}.
\tag{7}
\]

The constants are independent of \(n,R,M\), and
\(\varepsilon\in[1/8,1/4]\). No analytic disk for the actual complex
trajectory is assumed or concluded.

**Proof.** Form the finite state polynomial \(P_R(t)\) from the coefficients
through order \(R\). Set \(\rho=(D_*M)^{-1}\), with \(D_*\ge256\).
For complex \(|t|\le\rho\), each state increment in (3) is bounded by
\(2M|t|\), and each unnormalized transformed-coordinate increment is
bounded by the same quantity:

\[
\max_{a,i}\sqrt n\,
|P_{R,\zeta_a,i}(t)-\zeta_{a,0,i}|
\le\sum_{j=1}^R M|t|^j\le2/D_*<1/16.
\tag{8}
\]

Apply (5) coordinatewise. The composed vector
\(A_{n,\varepsilon}(P_{R,\zeta_a}(t))\) is holomorphic on this disk and
its Euclidean increment from initialization is at most four times the
Euclidean increment of \(P_{R,\zeta_a}\). This estimate retains the
Euclidean norm; it does not sum a coordinatewise bound and lose a factor
\(\sqrt n\). All vectors in (2), the operator norm of \(W_0+P_{R,D}\),
and both predictions are consequently bounded by constants depending
only on \(L_0,\eta\). The matrix component of the right-hand side is
bounded in Frobenius norm because it is an outer product.

It follows that the finite-dimensional Banach-valued function
\(\mathcal F_n(P_R(t))\) is holomorphic and has norm at most \(C_0\),
independently of \(n,R,M\), on \(|t|\le\rho\). Its coefficient of
\(t^j\) has norm at most \(C_0\rho^{-j}\) by Cauchy's formula.
Since \(P_R\) contains the actual initialized state jets, its derivative
matches \(\mathcal F_n(P_R)\) through degree \(R-1\). This is the finite
chain-rule identity obtained by differentiating the real ODE at zero;
it does not require convergence of its infinite Taylor series. Hence

\[
\|\dot P_R(t)-\mathcal F_n(P_R(t))\|
\le2C_0\rho^{-R}t^R,
\qquad 0\le t\le\rho/2.
\tag{9}
\]

Choose \(D_*\) larger, if needed, so that \(\rho/2\) lies inside the
uniform real existence interval from Section 2. Both the true state
\(S(t)\) and \(P_R(t)\) remain in the fixed real ball used there. Real
Lipschitz stability, integrated from their common initial state, yields

\[
\|S(t)-P_R(t)\|
\le\frac{2C_0e^{Lt}}{R+1}\rho^{-R}t^{R+1},
\tag{10}
\]

where \(L\) is independent of width. This follows directly by subtracting
the two differential equations and applying the integral Gronwall inequality.
The prediction difference obeys the same estimate up to a fixed Lipschitz
factor.

The prediction evaluated on \(P_R(t)\) is also bounded and holomorphic
on \(|t|\le\rho\). Its Taylor coefficients through degree \(R\) equal
the actual prediction coefficients, because the state jets agree through
that degree. A second Cauchy estimate gives

\[
\left|f_a(P_R(t))-
\sum_{j=0}^R\frac{f_a^{(j)}(0)}{j!}t^j\right|
\le2C_1\rho^{-(R+1)}t^{R+1}
\quad(0\le t\le\rho/2).
\]

Combining this with (10), and using \(\rho\le1\), proves (7). \(\square\)

## 4. Exact role in the original frozen-top comparison

Let \(q\) be the rank retained by the original frozen-top NTH, let
\(\widehat f_1^{(q)}\) be its prediction with its own residual, and set
\(j=2\lfloor q/2\rfloor+1\). Suppose its exact first unmatched physical
coefficient is \(J\), so that

\[
\frac{d^r}{dt^r}(f_1-\widehat f_1^{(q)})(0)=0\quad(r<j),
\qquad
\frac{(f_1-\widehat f_1^{(q)})^{(j)}(0)}{j!}=J.
\tag{11}
\]

Identity (11) must be proved for the actual hierarchy; it is not an
assumption that a common residual clock can be substituted. The generic
route supplies that identity and seeks a lower bound \(|J|\ge L_j>0\).

Apply (7) with \(R=j\). If the actual rank-\(q\) closure also has a
remainder bound \(B_qt^{j+1}\) on \([0,T_q]\), then

\[
|f_1(t)-\widehat f_1^{(q)}(t)-Jt^j|
\le\big[C(D_*M)^{j+1}+B_q\big]t^{j+1}
\]

for \(t\le\min\{(2D_*M)^{-1},T_q\}\). Therefore choosing

\[
\tau=\min\left\{
(2D_*M)^{-1},T_q,
\frac{L_j}{2[C(D_*M)^{j+1}+B_q]}
\right\}
\tag{12}
\]

gives the actual physical-time error lower bound

\[
|f_1(\tau)-\widehat f_1^{(q)}(\tau)|\ge\tfrac12 L_j\tau^j.
\tag{13}
\]

This is a finite-order Taylor comparison of the specified dense and
frozen-top systems. The polynomial \(P_R\) is only a proof device; no
approximation family or coefficient initialization has been changed.

For orientation, if \(q\le C_*\log\log n\), the Gaussian-jet estimate
\(M\le\exp[C(\log\log n)^2]\) would make the dense remainder constant in
(7) at most \(\exp[C'(\log\log n)^3]\). A jet lower bound
\(L_j\ge\exp[-C'(\log\log n)^2]\), together with closure remainder and
horizon bounds of the same polynomial-logarithmic type, would then make
the right-hand side of (13) at least
\(\exp[-C''(\log\log n)^4]\). This is asymptotically larger than
\(n^{-1/2}\), because \((\log\log n)^4=o(\log n)\).

This final scaling paragraph is conditional on the independently supplied
initialized-jet event, first-unmatched-jet lower bound, and closure remainder.
The deterministic implication (6)--(7), and its transfer (11)--(13), are
proved here in full. Section 5 supplies the initialized event and the
closure remainder. The Remez and unmatched-jet arguments must still be
checked before their combined lower-bound conclusion is asserted.

## 5. Consequence of the checked Gaussian initialized-jet bound

The complete proof in `INITIAL_JET_MOMENTS.md` was read and independently
checked by this author, including the later order-specific simultaneous
envelope. The final checked version had SHA-256
`c602af475be2caa08f2d51491286dc323d73d099b4a9a4876f6fcfdc89d1d644`.
The check reconstructed its expression grammar, the Gaussian pairing
quotient, the local derivative-size induction, and the matrix-norm step.
The following points give the actual checks, rather than treating the
artifact's conclusion as an unverified premise.

A monomial formed from initialized deterministic vector gates, multiplication
by \(W_0\) or \(W_0^\top\), coordinatewise products, and normalized pairings
is a forest. A vector output has one rooted component; a scalar output has
only unrooted components. A normalized pairing merges its two roots and
contributes \(1/n\). If the monomial has \(E\) Gaussian matrix edges and
\(S\) unrooted components, its normalization is \(n^{-E/2-S}\).

For an even \(p\)-th moment of a vector coordinate, the \(p\) roots are
identified at the fixed coordinate. For a scalar, the \(p\) copies remain
unrooted. Each Wick pairing leaves at most \(pE/2\) distinct edges in the
quotient, and at most \(pS\) unrooted components. A connected graph has
at most one more vertex than edges, and the rooted component's root is
fixed. Thus the number of free indices is at most \(pE/2+pS\), which
cancels the normalization. The argument respects layer types even for
transpose matrix actions. Its moment bound is
\(B_*\max(1,pE)^{E/2}\), where \(B_*\) is the product of deterministic
gate bounds.

The exact differentiation rules for a trained matrix are
\(D_b(Wv)=u\langle h_b,v\rangle_n+WD_bv\) and
\(D_b(W^\top v)=h_b\langle u,v\rangle_n+W^\top D_bv\), where
\(\langle v,w\rangle_n=v^\top w/n\). They keep the same grammar.
Expanding the actual residual \((y_b-f_b)/2\) also does so. Each derivative
adds a bounded number of operations at one existing Leibniz site, giving
size \(O(r+1)\), gate derivative-order sum \(O(r+1)\), and at most
\([C(r+1)]^{C(r+1)}\) terms after \(r\) derivatives. The gate bounds are
uniform in the stated activation interval. For matrix increments, repeated
differentiation preserves sums of rank-one terms \(vw^\top/n\), whose
Frobenius norms are products of vector RMS norms. Minkowski and Hölder
therefore give the same moment order. These facts verify the stated
moment estimate for physical state jets and all NTH sample words.

Taking even \(p\) of order \(\log n+R\), bounding the initialized first
coordinates by \(C\sqrt{\log n}\), and applying Markov's inequality and
a union bound over \(O(n(R+1)2^R)\) quantities gives the following
usable conclusion. Fix \(A,C_0>0\), a single
\(\varepsilon\in[1/8,1/4]\), and set
\(\ell_n=\log\log(e^e n)\). With probability at least \(1-2n^{-A-2}\),
all raw physical state derivatives and all initialized NTH entries
through orders \(R\le C_0\ell_n\), together with matrix-increment
Frobenius derivatives, are at most

\[
\exp(C_{A,C_0}\ell_n^2).
\tag{14}
\]

In particular, the derivatives of the raw transformed coordinates
\(T_\varepsilon(z_a)\) are covered. Dividing by \(j!\), taking RMS norms,
and increasing the bound by a fixed factor gives exactly (6). This is a
statement for each fixed \(\varepsilon\), with constants uniform on the
interval; it does not assert one common event simultaneously for a
continuum of activation parameters.

The additional initial norm event in Section 3 holds with exponentially
high probability. For each input, a Gaussian exponential-moment bound gives
\(\|z_a(0)\|_2/\sqrt n\le2\) outside an event of probability \(e^{-cn}\).
As \(|T_\varepsilon(z)|\le4|z|/3\), this gives an initial state norm
at most \(16/3\). To check the matrix bound directly, take a
\(1/4\)-net of each unit sphere with at most \(9^n\) points, constructed
by maximal separated points and the volume bound. The operator norm is
at most twice the largest bilinear form over the two nets. Each fixed
bilinear form \(v^\top W_0w\) is \(N(0,1/n)\), so a union bound at
threshold four gives

\[
\mathbb P(\|W_0\|_{\rm op}>8)
\le2\exp[(2\log9-8)n].
\]

Thus one may take \(L_0=8\), uniformly in \(\varepsilon\). Combining
this event, (14), and the deterministic lemma proves the following
unconditional dense-flow consequence: for every fixed \(A,C_0>0\),
every fixed \(\varepsilon\in[1/8,1/4]\), and all sufficiently large \(n\),
with probability at least \(1-n^{-A}\), simultaneously for
\(1\le R\le C_0\ell_n\),

\[
\left|f_a(t)-\sum_{j=0}^R\frac{f_a^{(j)}(0)}{j!}t^j\right|
\le \exp(C\ell_n^3)t^{R+1},
\quad
0\le t\le\exp(-C\ell_n^2).
\tag{15}
\]

Increasing \(C\) accommodates both the coefficient bound and the horizon.
Its dependence is only on \(A,C_0,\eta\), not on width or the fixed choice
of \(\varepsilon\) in the interval.

For completeness, the same event controls the original finite-rank NTH
remainder as well. Let \(H_q\ge1\) bound every initialized retained
tensor, including the zero initial predictions. In the complex max norm
on all retained entries, each hierarchy derivative is bounded by
\(2X^2\) when the state norm is at most \(X\ge1\), since there are two
residual terms with the factor \(1/2\) and \(|y_a|\le1\).
The scalar majorant \(X'=2X^2\), \(X(0)=H_q\), gives a holomorphic
solution bounded by \(2H_q\) on \(|t|\le1/(4H_q)\). This can be
verified directly by the positive Taylor-coefficient recursion for the
quadratic ODE; it has no dependence on the number of retained entries.
The top-rank derivative is zero and satisfies the same majorant.
Cauchy's formula therefore gives, for the actual closure with its own
residual,

\[
\left|\widehat f_a^{(q)}(t)
-\sum_{j=0}^R\frac{(\widehat f_a^{(q)})^{(j)}(0)}{j!}t^j\right|
\le4H_q(4H_q)^{R+1}t^{R+1},
\quad 0\le t\le1/(8H_q).
\tag{16}
\]

By (14), \(H_q\le\exp(C\ell_n^2)\) for \(q\le C_0\ell_n\).
Consequently (16) has the same horizon and \(\exp(C\ell_n^3)\)
remainder scale as (15), when \(R=O(\ell_n)\). Equations (15)--(16)
close the finite-remainder portion of the proposed original-NTH lower
bound. The separate first-unmatched-jet identity and its Remez lower
bound still determine whether (13) yields the intended theorem.

## 6. Order-specific remainder bounds through logarithmic order

The updated initialized-jet statement preserves each derivative's own
envelope while taking a union bound through
\(R_n=\lfloor\log(en)\rfloor\). Let

\[
\ell_n=\log\log(e^e n),\qquad
b_{n,j}=1+\log(j+1)+\ell_n,
\qquad 1\le j\le R_n.
\]

For each fixed activation parameter, and on one event of probability at
least \(1-n^{-A}\), the inputs of (6) through any order \(j\le R_n\)
are bounded by

\[
M_j=\exp\{C_A(j+1)b_{n,j}\}.
\tag{17}
\]

The same event bounds every initialized NTH tensor of rank at most
\(j+1\) by the corresponding envelope. The constant includes the
fixed-factor conversion from raw derivatives to the four norms in (6),
and the exponentially likely initial operator/RMS event. This
simultaneous conclusion follows by choosing the moment exponent using
the largest order \(R_n\), but applying Markov's inequality at
\(eM_{r,p,R_0}\) separately for each \(r\le R_n\). It does not bound
every low-order derivative by the much larger final-order envelope.

Substitution of (17) into the deterministic lemma proves, simultaneously
for \(1\le j\le R_n\),

\[
\left|f_a(t)-\sum_{r=0}^j\frac{f_a^{(r)}(0)}{r!}t^r\right|
\le \exp\{C_A(j+1)^2b_{n,j}\}\,t^{j+1}
\tag{18}
\]

on the interval

\[
0\le t\le\exp\{-C_A(j+1)b_{n,j}\}.
\tag{19}
\]

Constants have been enlarged to absorb the fixed \(C,D_*\) in (7).
The width enters only through \(\ell_n\). The shorter reciprocal
interval \(t\le\exp\{-C_A(j+1)^2b_{n,j}\}\) is therefore also valid.

For a retained rank \(q\) with
\(j=2\lfloor q/2\rfloor+1\le R_n\), (16) and the same initialized
event give

\[
\left|\widehat f_a^{(q)}(t)
-\sum_{r=0}^j\frac{(\widehat f_a^{(q)})^{(r)}(0)}{r!}t^r\right|
\le\exp\{C_A(j+1)^2b_{n,j}\}\,t^{j+1}
\tag{20}
\]

on an interval of the form (19). No tensor or residual in this statement
is replaced by an averaged coefficient or a dense residual.

If the separately proved unmatched-jet bound has the proposed form

\[
|J|\ge\exp\{-C_\eta(j+1)(1+\ell_n)\},
\tag{21}
\]

then (11), (18), and (20) give the following explicit implication. For
a sufficiently large constant \(C'_\eta\), choose

\[
\tau=\exp\{-C'_\eta(j+1)^2b_{n,j}\}.
\]

It lies in both valid intervals and makes the combined remainder at
most \(|J|\tau^j/2\). Therefore

\[
\sup_{0\le t\le\tau}|f_1(t)-\widehat f_1^{(q)}(t)|
\ge\exp\{-C''_\eta(j+1)^3b_{n,j}\}.
\tag{22}
\]

Equation (22) is conditional only on the separate exact identity and jet
lower bound (11), (21); the finite remainder estimates needed for it are
now supplied by the checked Gaussian initialized-jet lemma and the proof
above. It is a bound on the actual physical predictions of the original
two systems on a common interval whose existence has been proved. Since
\(\tau\) tends to zero in the growing-order regime, this also obstructs
accuracy on every fixed positive horizon whenever the closure continues
to that horizon. Failure of such continuation itself prevents an
all-horizon approximation claim.

For example, since \(b_{n,j}\le C\ell_n\) when \(j\le R_n\), (22)
would rule out \(n^{-1/2}\) prediction accuracy for every

\[
q\le c_\eta\left(\frac{\log n}{\log\log(e^e n)}\right)^{1/3},
\]

with a sufficiently small fixed positive \(c_\eta\), on the common
event where the jet lower bounds hold. This order consequence must be
combined with the generic route's probability and activation-selection
quantifiers before it is stated as a final theorem.

## 7. Sharpening by retaining the geometric order envelope

The preceding bounds are valid but discard useful order dependence. The
following sharpening was suggested by the supervisor after the earlier
remainder proof was frozen. It keeps each initialized coefficient's own
bound and improves the remainder exponent from quadratic to linear in the
chosen Taylor degree.

**Geometric-envelope lemma.** In the deterministic setting of Section 3,
replace (6) by the assumptions that, for some \(B\ge2\) and every
\(1\le s\le R\),

\[
\|\zeta_{1,s}\|_2+\|\zeta_{2,s}\|_2+\|U_s\|_2+\|D_s\|_F\le B^s,
\qquad
\max_{a,i}\sqrt n\,|\zeta_{a,s,i}|\le B^s.
\tag{23}
\]

Then there are constants \(C,D_*\ge1\), depending only on \(L_0,\eta\),
such that

\[
\left|f_a(t)-\sum_{s=0}^R\frac{f_a^{(s)}(0)}{s!}t^s\right|
\le C(D_*B)^{R+1}t^{R+1},
\quad 0\le t\le(2D_*B)^{-1}.
\tag{24}
\]

**Proof.** Set \(\rho=(D_*B)^{-1}\). On the complex disk
\(|t|\le\rho\), the normalized state increment and the largest raw
transformed-coordinate increment of its Taylor polynomial satisfy

\[
\sum_{s=1}^R B^s|t|^s
\le\frac{B|t|}{1-B|t|}
\le\frac1{D_*-1}.
\tag{25}
\]

Choose \(D_*\ge256\). This places every scalar activation argument in
the uniform disk (5), and keeps the polynomial state in the same bounded
operator/RMS/Frobenius region as before. The functions
\(\mathcal F_n(P_R(t))\) and \(f_a(P_R(t))\) are therefore holomorphic
and bounded on \(|t|\le\rho\) by constants independent of width and
order. Jet matching and Cauchy's coefficient estimate give exactly (9)
with this new \(\rho\). Real stability and the prediction Cauchy estimate
then give (24), by the proof of (10) and (7). No assumption on the true
complex trajectory is added. \(\square\)

The checked initialized-jet event supplies (23). Indeed, with the common
maximum order \(R_n=\lfloor\log(en)\rfloor\), its coefficient bound at
order \(s\ge1\) is at most

\[
[C_A(s+1)\log(en)]^{C_A(s+1)}.
\]

For \(s\le R\), use \(s+1\le2s\), \(s+1\le R+1\), and increase
the fixed constant to obtain a single base

\[
B_{n,R}=[C_A(R+1)\log(en)]^{C_A}\ge2
\tag{26}
\]

for which each order-\(s\) coefficient in (23) is at most \(B_{n,R}^s\).
Division of derivatives by \(s!\) can only improve this bound. The
fixed-factor sum of the four norms is absorbed into the base. On that
same event, every initialized NTH tensor of rank
\(1\le s\le R+1\) is bounded by \(B_{n,R}^s\): its sample-word
derivative order is \(s-1\), and the zero initial prediction also
satisfies this bound. The constants are uniform for each fixed
\(\varepsilon\in[1/8,1/4]\), with the probability quantifiers already
specified in Section 5.

The original finite-rank NTH admits the same improvement. Fix
\(2\le q\le R+1\), put \(B=B_{n,R}\), and define weighted retained
coordinates

\[
X_s=\widehat K_s/B^s,\qquad 1\le s\le q.
\]

This is only a fixed rescaling for a proof; the tensors, initialization,
top freezing, and residual are those of the prescribed hierarchy. Its
exact equations are

\[
\dot X_{s,a_1\ldots a_s}
=\frac B2\sum_{b=1}^2X_{s+1,a_1\ldots a_s b}
 (y_b-BX_{1,b}),\qquad s<q,
\qquad \dot X_q=0.
\tag{27}
\]

The initial max norm is at most one. In the complex max norm, for
\(X\ge1\), the right-hand side has norm at most
\(B X(1+B X)\le2B^2X^2\), using \(|y_b|\le1\). The positive
coefficient majorant

\[
Z'=2B^2Z^2,\qquad Z(0)=1,
\qquad Z(t)=(1-2B^2t)^{-1}
\]

bounds the norm of the vector-valued power series coefficientwise.
To check that comparison, the constant and quadratic terms in (27)
are bounded by the corresponding positive convolution coefficients;
the linear term \(B X\) is bounded by a quadratic convolution with
initial majorant coefficient one and \(B\ge1\). Induction in the
Taylor recursion proves the bound. Consequently the actual finite
hierarchy solution is holomorphic with \(\max_s\|X_s\|_\infty\le2\)
on \(|t|\le1/(4B^2)\), and its predictions obey
\(|\widehat f_a^{(q)}|=B|X_{1,a}|\le2B\) there.

Cauchy's formula and a geometric tail sum give

\[
\left|\widehat f_a^{(q)}(t)
-\sum_{s=0}^R\frac{(\widehat f_a^{(q)})^{(s)}(0)}{s!}t^s\right|
\le4B(4B^2)^{R+1}t^{R+1},
\quad 0\le t\le1/(8B^2).
\tag{28}
\]

The closure may have rank smaller than \(R\); (28) concerns derivatives
of its finite ODE and does not require retaining rank \(R\). Its own
residual remains explicitly present in (27).

Combining (24), (26), and (28) gives, for both the dense prediction and
the original rank-\(q\) prediction, a Taylor remainder of the form

\[
\exp\{C_A(R+1)[1+\log(R+1)+\ell_n]\}\,t^{R+1}
\tag{29}
\]

on a common interval

\[
0\le t\le
\exp\{-C_A[1+\log(R+1)+\ell_n]\},
\tag{30}
\]

after enlarging \(C_A\). These statements hold simultaneously for
\(1\le R\le R_n\) and \(2\le q\le R+1\), on the same initialized
event, and retain the initial-norm event already proved. Equations
(29)--(30) strengthen the earlier valid but looser estimates
(18)--(20). A high-degree polynomial coefficient inequality can now be
applied to the actual prediction difference with a Taylor degree
\(R\) larger than the first unmatched degree; proving that final
inequality and choosing \(R\) belongs to the generic route.
