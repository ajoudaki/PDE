# A sub-exponential Osgood construction module for the original three-input L3 flow

2026-09-08. Independent theory-only route. No old proof files were edited and no experiments were run.

## Outcome and precise scope

This note supplies a new analytic module: **uniform sub-exponential incoming-field moments on bounded-primal capped paths suffice for cap-Cauchy construction, strong uniqueness against arbitrary bounded-primal strong competitors, and restart.** Sub-Gaussian tails and a comparison growing exponentially with the cap level are unnecessary for these steps.

The module does not, by itself, prove the required reachable moment hypothesis. It therefore is not a complete proof of the requested activation theorem. The fixed activation is exactly

\[
 \phi(z)=(1-e)z+e\arctan z,\qquad 0<e\le1/2,
\]

in all three hidden layers. There is no offset, gain change, architecture change, extra input spectral assumption, or alteration of the limiting dynamics.

The existing full theorem's listed conclusions concern global strong flow, uniqueness/restart, fixed-finite-horizon GF/GD population limits, and the stated nonaffinity/initial motion observables. Eventual loss convergence to zero is not itself one of those conclusions. The module accordingly uses the physical energy identity and does not require a fitting clock.

## 1. A multiplier bound with an Osgood endpoint

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

## 2. Complete raw-field estimate for the three-hidden-layer architecture

Consider two states on the same canonical neuron/action spaces. Write
D for their raw Hilbert distance. Assume D<=1 and that, for both states,

\[
 \|\sqrt d\,w:\mathbb R^d\to H_1\|_{op},\quad
 \|A\|,\ \|B\|,\ \|C\|_2\le B_0,
 \qquad B_0\ge1.
\]

The first norm is the norm of `u -> sqrt(d) w . u`. The raw first-weight
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

The exact raw GF field is

\[
 F_w=-d^{-1}\sum_i r_i b_i^1x_i,\quad
 F_A=-\sum_i r_i b_i^2\otimes h_i^1,\quad
 F_B=-\sum_i r_i b_i^3\otimes h_i^2,\quad
 F_C=-\sum_i r_i h_i^3.
\]

The normalization of the first block gives
`sqrt(d)||d^-1 b x_i||_2=||b||_2`.
The Hilbert--Schmidt norm of a rank-one action is the product of the
two L2 norms. Subtracting each product, (4) and (6) give respectively

\[
 \|\Delta F_w\|_{raw}\le102KB_0^8pD^\alpha,\quad
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
 \boxed{\quad
 \|F(\Theta)-F(\widetilde\Theta)\|_{raw}
 \le300KB_0^8 p D^{1-1/p}\quad(p\ge2, D\le1).
 \quad}                                                    \tag{7}
\]

All constants are independent of the input Gram and allow singular
Grams. No inverse of that Gram, symmetry, or labels beyond |y_i|=1
was used.

## 3. Osgood uniqueness and quantitative stability

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
 \boxed{\quad
 D(t)\le\exp(2)\left(\frac{\eta}{\exp(2)}\right)^{\exp(-Lt)}.
 \quad}                                                    \tag{9}
\]

For completeness, replace the first two terms in the integral inequality
by eta and define `Z(t)=eta+L int_0^t omega(D(s))ds`. Then D<=Z and
`Z'<=L omega(Z)` because omega is increasing. Separating variables gives
(9). The upper bound staying below one makes the bootstrap legitimate.
The case eta=0 follows by taking eta down to zero. Thus two true strong
flows from the same state coincide if only one has (5) and both have
bounded primal states on the interval. Inhomogeneous L(t) works as well,
with `exp(-int_0^t L(s)ds)` replacing `exp(-Lt)`.

## 4. Uniform sub-exponential cap tails

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

Write `a=1-e` and `g_0(z)=1/(1+z^2)`. Use exactly the original residual clip

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
is clipped; the linear term `a q` is retained exactly. This is the
existing regularization, not a purported gradient of the loss.

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

## 5. Approximate energy closes the primal bootstrap if the moment hypothesis is available

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

## 6. Cap-Cauchy construction without a cap-dependent Gronwall exponential

For caps R and S, repeat the subtraction in Section 2 directly on their
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
pass (5) to the limit. Thus Section 3 gives uniqueness against all
bounded-primal strong competitors, without requiring their tails.
Constructing on each integer horizon and using this uniqueness gives
one global path. The existing path beyond a reached state supplies a
continuation; uniqueness applied against its reference tail bounds gives
unique restart from that reached state.

No smallness restriction on e, no input-Gram inverse, and no comparison
with an affine clock appear in this implication. If its moment premise
were established for one fixed positive e uniformly for every finite T,
this module would settle the strong-flow/uniqueness/restart portion of
the requested theorem for that e.

## 7. What remains to prove, and what this changes

The unresolved analytic premise is:

> For each finite T and finite raw radius B, actual capped GF paths from
> the canonical initialization, up to first exit from that radius, have
> `||C||_p,||q_R^2||_p,||q_R^1||_p <= K(B,T,e,delta) p` for every p>=2,
> with a finite K independent of the cap and the time mesh.

Energy and general bounded-action L2 estimates do not imply this premise.
The earlier Walsh and concentrated-raw-state examples remain valid
obstructions to obtaining it for arbitrary fields. It must use the actual
reachable query structure. The nonlinear-reference agent's new same-array
value lemma supplies even sub-Gaussian moments conditional on finite
strict-forward-density and backward-row bounds; closing those bounds is
one possible way to supply the premise. The present module removes any
need to retain the stronger tail type for the subsequent uniqueness and
cap-Cauchy steps.

For finite GF/GD comparisons, the same deterministic recurrence applies
at finite width with normalized Euclidean norms; true finite GF has an
independent energy bound. A complete population-limit proof would still
need to transfer the reference moment estimates to the finite capped
comparison arrays, control the Euler defect, and verify every original
observable bridge. The fixed-cap finite-program results are available,
but those uniform transfers are not asserted as completed in this note.

Likewise, positive activation-regression error at every finite time is a
separate trained-law assertion. The module proves neither that assertion
nor a nondegenerate innovation at later times. Initial nonzero motion
is already established by the existing geometry calculations, conditional
on the strong construction; it would become an actual statement once the
moment premise is supplied.

Thus the note is a nonperturbative continuation reduction with complete
proof, not a proof of a theta_delta threshold. It narrows the remaining
problem from sub-Gaussian source rows plus cap-exponential comparison to
one reachable sub-exponential moment theorem (and the separate trained
nonaffinity/observable obligations).
