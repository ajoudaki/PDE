# A second forward-history derivative saves a power of learned state

2026-10-03. Scoped internal candidate, awaiting complete skeptical
reconstruction. This route improves the
certificate for the **original** autonomous Legendre closure; it requires
neither sampled histories nor a different reconstruction. Under the supplied
two-layer finite-network carrier theorem, the original closure with

\[
q_n=\left\lceil n^{1/6}\exp\{a\sqrt{\log(e+n)}\}\right\rceil
\]

has all-time same-width prediction error at most \(C_\mu n^{-1/2}\)
for sufficiently large fixed \(a\), and moving state
\(n^{7/6+o(1)}\). Thus any fixed \(0<\varepsilon<1/12\) is available
in a bound \(O(n^{5/4-\varepsilon})\). The fixed initialized mixer
still occupies \(n^2\) numbers. Running order
\(\min\{q,q_n\}\) approximates the original order-\(q\) closure
with this same accuracy and state budget, uniformly over all original
orders. This is an internal candidate, not promotion.

The argument derives the required regularity on the actual closure path.
Its key observation is that zero initial readout makes the first derivative
of the forward history match across the unit prefix. The second weighted
Legendre derivative is therefore an ordinary square-integrable function.
Residual-clock degeneracy at infinite physical time is canceled by the
Legendre weight. The backward history needs only the previously proved
first weighted derivative bound. A carrier maximum enters the new forward
estimate, but its discrepancy from the dense carrier is absorbed through
the same closure-to-dense comparison being proved.

Scientific inputs are the setting and memory construction in
`paper/main.tex`, `paper/results.tex`, `paper/proof_alltime.tex`, and
`paper/proof_tracking.tex`; the authorized prior
`studies/dense_cutoff_population_rate_20261001/Q_ORDER_RESULT.md` and
`NONORTHOGONAL_DIRECT_ROUTE.md`. The prior temporal regularity note was
read only as a diagnostic, and supplies no premise to the proof below:
the prefix argument is self-contained. The finite carrier maximum in
Section 5 is imported
as the precise prior-study theorem stated in `Q_ORDER_RESULT.md`, not
re-proved here. Its original proof/check dependency reconstruction belongs
to the coordinating task. The canonical-notation skill and its neural
reference, and the rigorous-math skill, were applied. No experiment,
manuscript edit, Git mutation, external theorem, or dense-path oracle is
used. After this route had identified the weighted second derivative and
the absorption inequality, the coordinator independently sent the same
construction; the final derivation below incorporates that exchange.

## 1. Model, exact state, and the comparison input

Fix training inputs \(v_a=x_a/\sqrt d\), \(\|v_a\|_2=1\),
\(a=1,\ldots,m\), and fixed labels \(y_a\). Write
\(Y^2=m^{-1}\sum_a y_a^2\). For two hidden layers with activation \(\phi=\tanh\),

\[
\begin{aligned}
z_a^{(1)}&=W^{(1)}v_a,&h_a^{(1)}&=\phi(z_a^{(1)}),\\
z_a^{(2)}&=Wh_a^{(1)},&h_a^{(2)}&=\phi(z_a^{(2)}),\\
f_a&=n^{-1}w^\top h_a^{(2)},&r_a&=f_a-y_a,
\qquad \rho^2=m^{-1}\sum_a r_a^2.
\end{aligned}
\tag{1}
\]

Here \(W^{(1)}\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\).
The loss is \(\mathcal L=\rho^2\). Since
\(\phi'=\operatorname{sech}^2\), the actual responses are

\[
\delta_a^{(2)}=w\odot \phi'(z_a^{(2)}),\qquad
k_a=W^\top\delta_a^{(2)},\qquad
\delta_a^{(1)}=\phi'(z_a^{(1)})\odot k_a.
\tag{2}
\]

Dense flow uses mobilities \((n,1,n)\):

\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\quad
\dot W=-\frac2{mn}\sum_a r_a\delta_a^{(2)}h_a^{(1)\top},
\quad
\dot w=-\frac2m\sum_a r_a h_a^{(2)}.
\tag{3}
\]

The first-layer initialization has independent \(N(0,1)\) entries,
the mixer \(W_0\) has independent \(N(0,1/n)\) entries, and
\(w(0)=0\). Both compared systems share those arrays. Initially suppose
the fixed data have a positive population readout-feature Gram gap; the
compatible duplicate/antipodal quotient from the supplied prior result
extends the conclusion with fixed sample weights.

For the closure, all responses in (1)--(2) are evaluated in its current
reconstruction. Its clock satisfies \(\dot\tau=\rho\), \(\tau(0)=1\).
The shifted Legendre polynomials \(p_j\) satisfy
\(p_j(1)=1\) and
\(\int_0^1p_jp_k=\mathbf1_{j=k}/(2j+1)\). The moving memories are

\[
\bar h_{a,j}^{(1)}=\int_0^\tau h_a^{(1)}(\xi)p_j(\xi/\tau)d\xi,
\qquad
\bar\delta_{a,j}^{(2)}=
\int_0^\tau b_a^{(2)}(\xi)p_j(\xi/\tau)d\xi,
\quad b_a^{(2)}=\frac{r_a}{\rho}\delta_a^{(2)},
\tag{4}
\]

where the forward history on \([0,1]\) is its initial value and the
backward history is zero there. Their autonomous physical-time equations
and reconstruction are exactly

\[
\begin{aligned}
\dot{\bar h}_{a,j}^{(1)}
 &=\rho h_a^{(1)}-\frac\rho\tau
    \left[j\bar h_{a,j}^{(1)}+
      \sum_{i<j}(2i+1)\bar h_{a,i}^{(1)}\right],\\
\dot{\bar\delta}_{a,j}^{(2)}
 &=r_a\delta_a^{(2)}-\frac\rho\tau
    \left[j\bar\delta_{a,j}^{(2)}+
      \sum_{i<j}(2i+1)\bar\delta_{a,i}^{(2)}\right],\\
\widehat W
 &=W_0-\frac2{mn\tau}
    \sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
       \bar\delta_{a,j}^{(2)}\bar h_{a,j}^{(1)\top}.
\end{aligned}
\tag{5}
\]

The first layer and readout follow (3). Initially
\(\bar h_{a,0}^{(1)}=h_a^{(1)}(0)\), and all other memories vanish.
Equation (5) has no division by the residual. The division in (4) only
describes histories where \(\rho>0\). Zero labels give a stationary
system and are henceforth excluded from intermediate divisions.

All finite vector norms below are ordinary Euclidean norms, with every
width normalization displayed. For sample scalars write
\(\|c\|_m^2=m^{-1}\sum_a c_a^2\). The manuscript's all-order fitting
theorem, on its common initialization event and for fixed
\(0<Y\le Y_*\), supplies the following constants independently of
\(n,q,t\):

\[
\begin{gathered}
0<\rho(t)\le Ye^{-\kappa t},\qquad
\int_t^\infty\rho(s)ds\le\rho(t)/\kappa,
\qquad 1\le\tau(t)\le1+Y/\kappa\le2,\\
\|W(t)\|_{\rm op}\le C,\qquad
\max_a\frac{\|k_a(t)\|_2}{\sqrt n}+\frac{\|w(t)\|_2}{\sqrt n}\le CY,\\
\|\dot W(t)\|_F\le CY\rho(t),\qquad
\max_{\ell,a}\frac{\|\dot z_a^{(\ell)}(t)\|_2}{\sqrt n}\le CY\rho(t),\qquad
\frac{\|\dot w(t)\|_2}{\sqrt n}\le2\rho(t),\\
\left\|\frac d{dt}(r/\rho)\right\|_m\le C.
\end{gathered}
\tag{6}
\]

These hold for each actual closure before any dense comparison. Bounded
tanh and the exact readout equation give the additional coordinate bound

\[
\|w(t)\|_\infty\le2\int_0^t\rho(s)ds\le2Y/\kappa.
\tag{7}
\]

This is crucial: differentiating the top backward response needs no
maximum of a top preactivation derivative.

Let \(\Pi_q^A\) be orthogonal projection onto degree-below-\(q\)
polynomials on \([0,A]\). At \(A=\tau(t)\), a star denotes its
endpoint evaluation. The reconstructed physical equation is
\(\dot{\widehat\theta}=F(\widehat\theta)+E\), with only the mixer
defect nonzero:

\[
E_2(t)=\frac{2\rho(t)}{mn}\sum_a
 (b_a^{(2)}-b_a^{(2)*})
 (h_a^{(1)}-h_a^{(1)*})^\top.
\tag{8}
\]

The projection-energy identity in the manuscript gives, at every finite
terminal time,

\[
\int_0^t\|E_2(s)\|_Fds
\le\frac2m\sum_a
 \frac{\|(I-\Pi_q^A)b_a^{(2)}\|_{L^2(0,A)}}{\sqrt n}
 \frac{\|(I-\Pi_q^A)h_a^{(1)}\|_{L^2(0,A)}}{\sqrt n}.
\tag{9}
\]

In particular, (9) controls accumulated absolute velocity error, which
is the input needed for stability, and is not merely a signed final
reconstruction error.

## 2. A second-order Legendre estimate with its exact hypotheses

Set \(\eta_A(\xi)=\xi(A-\xi)\) and

\[
\mathcal L_Au=-\frac d{d\xi}(\eta_Au').
\tag{10}
\]

If \(u\) is \(C^1\) and piecewise \(C^2\) on a finite interval
\([0,A]\), and \(\mathcal L_Au\in L^2\), then

\[
\|(I-\Pi_q^A)u\|_{L^2}
\le\frac{\|\mathcal L_Au\|_{L^2}}{q(q+1)}.
\tag{11}
\]

The vector or Hilbert-space version has the same constant. To prove it,
use the orthonormal modes
\(e_j(\xi)=\sqrt{(2j+1)/A}\,p_j(\xi/A)\), which satisfy
\(\mathcal L_Ae_j=j(j+1)e_j\). Two integrations by parts give

\[
\langle\mathcal L_Au,e_j\rangle
 =\langle u,\mathcal L_Ae_j\rangle
 =j(j+1)\langle u,e_j\rangle.
\]

The endpoint terms vanish because \(\eta_A(0)=\eta_A(A)=0\);
at any interior join they cancel because \(u,u'\) match. Parseval
for \(u\), followed by Bessel for \(\mathcal L_Au\), gives

\[
\sum_{j\ge q}\|\langle u,e_j\rangle\|^2
\le[q(q+1)]^{-2}
  \sum_{j\ge q}\|\langle\mathcal L_Au,e_j\rangle\|^2
\le[q(q+1)]^{-2}\|\mathcal L_Au\|_{L^2}^2.
\]

This proof also applies when \(\eta_Au'\) is weakly absolutely
continuous, has zero endpoint values, and has square-integrable
derivative, by approximation or directly by weak integration by parts.
Only the elementary finite-terminal-time piecewise smooth case is needed
below. In particular, no regularity at the limiting endpoint
\(\tau(\infty)\) is assumed.

## 3. The actual first-layer forward history satisfies (11)

In this section hats are suppressed: all quantities belong to the actual
order-\(q\) closure. Fix a finite physical terminal time \(t\), put
\(A=\tau(t)\), and use primes only for derivatives with respect to
its own clock \(\xi=\tau(s)\). Put \(c_a=r_a/\rho\), and let

\[
K_q=\sup_{s\ge0}\max_a\|k_a(s)\|_\infty.
\tag{12}
\]

This is finite before approximation: (6) gives
\(K_q\le C\sqrt nY\). It is not a new assumption.
Since \(c\) has sample RMS one, and the input Gram
\(G_{ab}=v_a^\top v_b\) is fixed, the first-layer equation gives

\[
(z_a^{(1)})'=-\frac2m\sum_bG_{ab}c_b
                 [\phi'(z_b^{(1)})\odot k_b],
\qquad
\frac{\|(z_a^{(1)})'\|_2}{\sqrt n}\le CY,
\quad
\|(z_a^{(1)})'\|_\infty\le CK_q.
\tag{13}
\]

The clock derivatives of the top response and carrier are

\[
\begin{aligned}
(\delta_a^{(2)})'
 &=w'\odot \phi'(z_a^{(2)})
      +w\odot \phi''(z_a^{(2)})\odot(z_a^{(2)})',\\
k_a'&=W'^\top\delta_a^{(2)}+W^\top(\delta_a^{(2)})'.
\end{aligned}
\tag{14}
\]

By (6)--(7), \(\frac{\|w'\|_2}{\sqrt n}\le2\),
\(\|W'\|_F\le CY\), and
\(\frac{\|(z_a^{(2)})'\|_2}{\sqrt n}\le CY\). Thus bounded \(\phi',\phi''\) give

\[
\frac{\|(\delta_a^{(2)})'\|_2}{\sqrt n}\le C,
\qquad \frac{\|k_a'\|_2}{\sqrt n}\le C.
\tag{15}
\]

No derivative of the velocity defect \(E_2\) occurs in (14).
Only the already proved physical speed of \(W\) is used.
Also \(\|c'\|_m\le C/\rho\) by (6). Differentiating (13) therefore
gives

\[
\begin{aligned}
(z_a^{(1)})''=-\frac2m\sum_bG_{ab}\bigl[
 &c_b' \phi'(z_b^{(1)})\odot k_b\\
 &+c_b \phi''(z_b^{(1)})\odot(z_b^{(1)})'\odot k_b\\
 &+c_b \phi'(z_b^{(1)})\odot k_b'\bigr],
\end{aligned}
\]

and hence

\[
\frac{\|(z_a^{(1)})''\|_2}{\sqrt n}
 \le C\left(\frac Y\rho+1+YK_q\right).
\tag{16}
\]

For the nonlinear middle term use
\(\frac{\|(z_b^{(1)})'\odot k_b\|_2}{\sqrt n}
\le K_q\frac{\|(z_b^{(1)})'\|_2}{\sqrt n}\).
The activation chain rule is

\[
(h_a^{(1)})''=
\phi''(z_a^{(1)})\odot((z_a^{(1)})')^2
 +\phi'(z_a^{(1)})\odot(z_a^{(1)})'',
\]

where the square is coordinatewise. By (13),
\(\frac{\|((z_a^{(1)})')^2\|_2}{\sqrt n}
\le\|(z_a^{(1)})'\|_\infty\frac{\|(z_a^{(1)})'\|_2}{\sqrt n}\).
Consequently

\[
\frac{\|(h_a^{(1)})'\|_2}{\sqrt n}\le CY,
\qquad
\frac{\|(h_a^{(1)})''\|_2}{\sqrt n}
\le C\left(\frac Y\rho+1+YK_q\right).
\tag{17}
\]

The first derivative on the prefix is zero. At \(\xi=1+\),
\(w(0)=0\) implies \(\delta_b^{(2)}(0)=k_b(0)=0\), so (13)
also gives \((h_a^{(1)})'(1+)=0\). The forward history is therefore
\(C^1\) across the join. Its second derivative can jump there; a
jump in the second derivative contributes no point mass to
\(\mathcal L_Ah\). The positive residual on every finite physical
interval and the smooth finite-dimensional ODE give the remaining
piecewise smoothness required by (11).

To estimate the operator in (10), use

\[
\eta_A(\tau(s))
\le A\,[A-\tau(s)]
\le \frac A\kappa\rho(s),\qquad
|\eta_A'|\le A\le2.
\tag{18}
\]

The crucial second inequality uses \(s\le t\) and the tail activity
bound in (6). With \(d\xi=\rho(s)ds\), (17)--(18) give

\[
\begin{aligned}
\frac1n\|\mathcal L_Ah_a^{(1)}\|_{L^2(0,A)}^2
&\le C\int_0^t
 \left[Y^2+\rho(s)^2(1+YK_q)^2+Y^2\right]\rho(s)ds\\
&\le CY^3(1+YK_q)^2.
\end{aligned}
\tag{19}
\]

The last step uses
\(\int_0^\infty\rho\le Y/\kappa\) and
\(\int_0^\infty\rho^3\le Y^3/(3\kappa)\).
There is no contribution from the prefix, where \(h'\equiv0\).
The factor \(\rho^2\) from \(\eta_A^2\) exactly cancels the
\(\rho^{-2}\) produced by differentiation of \(r/\rho\).
Combining (11) and (19) proves the new uniform forward-tail estimate

\[
\frac{\|(I-\Pi_q^A)h_a^{(1)}\|_{L^2(0,A)}}{\sqrt n}
\le CY^{3/2}(1+YK_q)q^{-2}.
\tag{20}
\]

The proof holds at every finite current endpoint \(A=\tau(t)\), with
the same bound. Infinite-time regularity was never substituted for these
finite-interval arguments.

## 4. Backward tail and the new absolute-defect bound

For completeness, the two-layer backward estimate used here can be
reconstructed directly. From (7), (14), and (6), in physical time,

\[
\frac{\|b_a^{(2)}\|_2}{\sqrt n}\le CY,
\qquad
\frac{\|\dot b_a^{(2)}\|_2}{\sqrt n}
\le C\left(Y+\rho\right).
\tag{21}
\]

For a fixed physical cutoff \(T\), freeze this history after \(T\),
calling it \(b_{a,T}^{(2)}\). The ordinary clock \(L^2\) norm of its difference from the original,
divided by \(\sqrt n\), is at most
\(CY^{3/2}e^{-\kappa T/2}\), by bounded amplitude and the tail
clock mass. The zero readout makes the prefix join continuous. For
\(A=\tau(t)\),

\[
\begin{aligned}
\int_0^A\xi(A-\xi)\frac{\|(b_{a,T}^{(2)})'(\xi)\|_2^2}{n}d\xi
&\le C\int_0^{\min(t,T)}\frac{\|\dot b_a^{(2)}(s)\|_2^2}{n}ds\\
&\le CY^2(1+T).
\end{aligned}
\]

The first weighted Legendre derivative estimate, projection contraction,
and \(T=(2/\kappa)\log q\), including \(T=0\) for \(q=1\), yield

\[
\frac{\|(I-\Pi_q^A)b_a^{(2)}\|_{L^2(0,A)}}{\sqrt n}
\le CY\frac{\sqrt{\log(e+q)}}q.
\tag{22}
\]

Equation (22) is the bound proved in `NONORTHOGONAL_DIRECT_ROUTE.md`;
it assumes no input orthogonality and clips no response. Insert
(20) and (22) into the exact product inequality (9), then increase the
finite terminal time. The left side is monotone and all right sides
have the same bound, so

\[
\epsilon_q:=\int_0^\infty\|E_2(s)\|_Fds
\le CY^{5/2}(1+YK_q)
              \frac{\sqrt{\log(e+q)}}{q^3}.
\tag{23}
\]

This is a derived bound on the actual closure defect. Its only unwanted
quantity is the actual carrier maximum \(K_q\), already known to be
finite. It will now be eliminated rather than postulated.

## 5. Dense-only carrier control and absorption

Return to hats for the closure and a subscript \(D\) for dense flow.
Let

\[
D_{n,q}=\sup_{t\ge0}\left[
 \frac{\|\widehat W^{(1)}-W_D^{(1)}\|_F}{\sqrt n}
 +\|\widehat W-W_D\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n}\right].
\tag{24}
\]

The all-order physical bounds imply \(D_{n,q}<\infty\) independently
of the approximation argument. Suppose the given initialization also
satisfies a dense-only maximum bound

\[
\sup_{t\ge0}\left[\max_a\|k_{D,a}(t)\|_\infty
                  +\|w_D(t)\|_\infty\right]\le M,
\qquad M\ge1.
\tag{25}
\]

Forward subtraction using bounded gates and operators gives
\(\max_a\frac{\|\widehat z_a^{(2)}-z_{D,a}^{(2)}\|_2}{\sqrt n}
\le CD_{n,q}\). By bounded dense readout coordinates (7),

\[
\begin{aligned}
\widehat\delta_a^{(2)}-\delta_{D,a}^{(2)}
&=(\widehat w-w_D)\odot \phi'(\widehat z_a^{(2)})
  +w_D\odot[\phi'(\widehat z_a^{(2)})-\phi'(z_{D,a}^{(2)})],\\
\frac{\|\widehat\delta_a^{(2)}-\delta_{D,a}^{(2)}\|_2}{\sqrt n}
&\le CD_{n,q}.
\end{aligned}
\]

The carrier difference consequently obeys

\[
\begin{aligned}
\widehat k_a-k_{D,a}
 &=\widehat W^\top
       (\widehat\delta_a^{(2)}-\delta_{D,a}^{(2)})
   +(\widehat W-W_D)^\top\delta_{D,a}^{(2)},\\
\frac{\|\widehat k_a-k_{D,a}\|_2}{\sqrt n}&\le CD_{n,q}.
\end{aligned}
\]

Since \(\|u\|_\infty\le\|u\|_2\), this yields

\[
K_q\le M+C\sqrt nD_{n,q}.
\tag{26}
\]

The subtraction uses the two systems at the same physical time; their
history clocks need not agree. The absence of an additional \(M\)
factor in (26) uses the two-layer bounded-readout argument. A weaker
bound with \((1+M)D_{n,q}\) would still give the same final exponent.

The manuscript's one-reference damping theorem is deterministic on this
event. Its dense tail is exactly zero at cutoff \(M\), so

\[
D_{n,q}\le A_M\epsilon_q,\qquad
A_M=Ce^{CY M}.
\tag{27}
\]

Here the factor \(Y\) follows by retaining
\(\int\rho_D\le Y/\kappa\) in the integrating factor; using
\(Ce^{CM}\) would also suffice. Put
\(s_q=q^{-3}\sqrt{\log(e+q)}\). Substituting (26) into (23), then
using (27), gives

\[
D_{n,q}\le C A_M Y^{5/2}s_q
       [1+YM+CY\sqrt nD_{n,q}].
\tag{28}
\]

Therefore, whenever

\[
C A_M Y^{7/2}\sqrt n\,
             q^{-3}\sqrt{\log(e+q)}\le\frac12,
\tag{29}
\]

the last term is absorbed, proving

\[
D_{n,q}\le C A_M Y^{5/2}(1+YM)
                 q^{-3}\sqrt{\log(e+q)}.
\tag{30}
\]

This proves a deterministic improvement in an explicit joint order-width
region. It does not first assume a small closure-to-dense discrepancy:
the finite value of \(D_{n,q}\) is enough for the algebraic absorption.
All-order existence and fitting were established before this argument.

The imported finite-network theorem in `Q_ORDER_RESULT.md` supplies
events \(\Omega_n\) with probability tending to one, contained in the
common fitting event, on which (25) holds with

\[
M_n=1+C_0Y\sqrt{\log(e+n)}.
\tag{31}
\]

Its constants and the label threshold depend only on the fixed geometry
and fixed labels, with the same compatible quotient as in that theorem.
It follows that \(A_{M_n}\le C\exp\{K\sqrt{\log(e+n)}\}\).
Choose a fixed \(a>K/3\), increasing it if necessary, and set

\[
q_n=\left\lceil n^{1/6}
                   \exp\{a\sqrt{\log(e+n)}\}\right\rceil.
\tag{32}
\]

The left side of (29) is then at most
\(C\sqrt{\log(e+n)}\exp\{-(3a-K)\sqrt{\log(e+n)}\}\),
which tends to zero. Equation (30) gives

\[
\sqrt nD_{n,q_n}
\le C[1+\sqrt{\log(e+n)}]\sqrt{\log(e+n)}
          \exp\{-(3a-K)\sqrt{\log(e+n)}\}
\le C'.
\tag{33}
\]

Thus, for each \(\delta>0\), there is a width threshold \(N_\delta\)
such that for \(n\ge N_\delta\), with probability at least
\(1-\delta\), the actual same-initialization order-\(q_n\) closure
satisfies \(D_{n,q_n}\le C'n^{-1/2}\). The event is independent of
the selected order and supports (30) simultaneously for every order
satisfying (29). No probability statement over a sequence of independent
widths is asserted.

## 6. Query guarantee, state count, and limitations

The manuscript's forward subtraction bound gives, for every query input,

\[
\sup_{t\ge0}|\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|
\le C(1+\|x\|_2/\sqrt d)D_{n,q}.
\tag{34}
\]

For a fixed query law \(\mu\) with finite second moment, take the
time supremum first and then integrate. With (33),

\[
\left(\int\sup_{t\ge0}
 |\widehat f_{n,q_n}(t,x)-f_{n,D}(t,x)|^2d\mu(x)\right)^{1/2}
\le C_\mu n^{-1/2}.
\tag{35}
\]

This includes the fitted endpoint and in particular every fixed sphere
query law. On a fixed bounded query set, (34) gives the corresponding
uniform absolute prediction bound. The reference in (35) is the actual
finite-width dense trajectory with the same initialized mixer.

To compare directly with the user's original order-\(q\) closure,
define the compressed order

\[
p_{n,q}=\min\{q,q_n\}.
\tag{35a}
\]

For \(q\le q_n\) the compressed and original systems coincide exactly.
For \(q>q_n\), the quantity
\(s_q=q^{-3}\sqrt{\log(e+q)}\) decreases with \(q\), as its
logarithmic derivative is
\(-3/q+[2(e+q)\log(e+q)]^{-1}<0\). Consequently (29)--(33)
hold simultaneously for every \(q\ge q_n\) on the same dense-only
event. The same-realization triangle inequality then gives

\[
\sup_{q\ge1}
\left(\int\sup_{t\ge0}
 |\widehat f_{n,p_{n,q}}(t,x)-\widehat f_{n,q}(t,x)|^2
 d\mu(x)\right)^{1/2}
\le 2C_\mu n^{-1/2}.
\tag{35b}
\]

The shared dense trajectory in this inequality is a proof reference.
Neither closure evaluates it. Both initialize directly from the same
Gaussian arrays and evolve their own moments, residuals, and clocks.

The state in (5) consists of the first matrix, the readout, \(2mnq\)
moment coordinates, and one clock. Hence at (32) the moving state is

\[
2mnq_n+n(d+1)+1=n^{7/6+o(1)}.
\tag{36}
\]

For example, for all sufficiently large widths this is
\(O(n^{29/24})=O(n^{5/4-1/24})\), and every fixed
\(\varepsilon<1/12\) works. The fixed Gaussian \(W_0\) is still
stored exactly, and its forward and transpose actions retain their dense
cost. The algorithm evolves every retained neuron and all its own
responses; there is no selection of neurons, access to a precomputed
dense path, history supplied by an oracle, or modified residual clock.

The unit prefix limits more ambitious blanket smoothness claims.
Generically the backward history has a first-derivative jump at its
start, so \(\mathcal L_Ab\) contains an interior point mass and
the second-order estimate (11) does not apply to it. The forward
history has a second-derivative jump but this does not obstruct its
first application of \(\mathcal L_A\). A further application would
require new interface treatment and higher trajectory estimates. Even
away from the prefix, normalized residual directions can rotate on the
compressed tail of the residual clock, so ordinary globally analytic
clock histories must not be assumed. The present argument bypasses
both obstacles with an exactly justified second weighted derivative
for the forward history and only a frozen-tail first derivative for the
backward history.

Piecewise polynomial, stratified, or interface-enriched memories may
improve rates further, but they would change the algorithm and require
their own autonomous reconstruction, projection-energy identity,
all-order fitting, and feedback control. Those constructions are not
needed for the requested strict power saving. No claim of optimality of
\(n^{7/6+o(1)}\), necessity of the exponential subpolynomial factor,
or extension of this argument to arbitrary depth is made here.
