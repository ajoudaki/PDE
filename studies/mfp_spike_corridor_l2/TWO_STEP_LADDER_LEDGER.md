# Exact two-step OMFP ledger for a transported-tail ladder

> **Superseding audit.**  The response and truncation estimates below contain
> unclosed steps.  `ADVERSARIAL_REAUDIT.md` gives the authoritative status:
> this is a promising candidate and exact obligation ledger, not a proved
> counterexample.

## 1. Target and conclusion

This note studies the strongest finite-step negative target

\[
 \Delta_1(h)=F_2(h)-F_1(2h).                     \tag{1.1}
\]

If a fixed activation admits a sequence \(h_n\downarrow0\) for which
\(F_2(h_n)\to+\infty\) while \(F_1(2h_n)\) stays bounded, then no estimate

\[
 |\Delta_t(h)-\kappa_t h^3|\le C t^5|h|^5,
 \qquad |h|\le\rho/t,                            \tag{1.2}
\]

can hold for all `t`: it already fails at `t=1`.

The two-step ledger below identifies how a two-scale oscillatory ladder could
have exactly this behavior.  The construction is smooth, positive, linearly
bounded, and has every initialization Gaussian derivative moment finite.  The
adaptive response, signed-output, and infinite-block truncation estimates are
not all proved; see the superseding audit.

## 2. Scales

Choose \(R_n\uparrow\infty\) recursively and put

\[
 t_n=e^{R_n},\qquad h_n=t_n^{-1},\qquad
 S_n=t_n,                                        \tag{2.1}
\]

\[
 L_{0,n}=t_n^2,\qquad L_{1,n}=e^{S_n},\qquad
 T_n=h_nL_{1,n}=e^{S_n-R_n}.                     \tag{2.2}
\]

Let

\[
 p_n=e^{-R_n^2/2},\qquad \delta_n=e^{-R_n}.      \tag{2.3}
\]

Polynomial factors in `R_n` are suppressed in the scale table, but not in a
limit: every displayed vanishing statement remains valid after multiplication
by any fixed power of `R_n`.  The elementary comparisons used repeatedly are

\[
 t_n^k p_n^a\delta_n^{-b}\longrightarrow0
 \quad(a>0;\ k,b<\infty),                        \tag{2.4}
\]

and

\[
 p_nT_n=\exp\{S_n-R_n-R_n^2/2\}\longrightarrow\infty.  \tag{2.5}
\]

## 3. Smooth asymmetric oscillatory shells

There is a smooth one-periodic function \(P_\delta\), with
\(|P_\delta|\le1\), whose derivative \(g_\delta=P_\delta'\) has mean zero and
the following properties:

\[
 g_\delta=1
 \quad\hbox{on a set of period measure at least }1-3\delta,           \tag{3.1}
\]

\[
 -2\delta^{-1}\le g_\delta\le1,                                    \tag{3.2}
\]

and, for every fixed `m`,

\[
 \|P_\delta^{(m)}\|_\infty\le C_m\delta^{-m}.                       \tag{3.3}
\]

To construct it, start with a piecewise-linear periodic primitive which rises
with slope one on a proportion \(1-2\delta\) and resets with constant negative
slope on the remaining proportion; convolve periodically with a nonnegative
Gevrey-2 mollifier of width \(\delta/4\).  Mean zero is preserved, (3.1)--(3.3)
follow directly, and the mollified reset remains negative.  We call the set in
(3.1) the positive phase and the reset its complement.

Let `chi` be a fixed nonnegative Gevrey-2 cutoff, equal to one on the middle
third of `[-1,1]`.  On mutually disjoint shells, define an unnormalized
activation `Phi` by

\[
 \Phi(x)=x+\epsilon R_n
 P_{\delta_n}(\omega_{0,n}x+\theta_{0,n})
 \quad(x\hbox{ in the core of }I_{R,n}),          \tag{3.4}
\]

\[
 \Phi(x)=x+\epsilon S_n
 P_{\delta_n}(\omega_{1,n}x+\theta_{1,n})
 \quad(x\hbox{ in the core of }I_{S,n}),          \tag{3.5}
\]

where

\[
 \omega_{0,n}=\frac{L_{0,n}}{\epsilon R_n},
 \qquad
 \omega_{1,n}=\frac{L_{1,n}}{\epsilon S_n}.      \tag{3.6}
\]

Take `I_R,n` of fixed width around `R_n`, take `I_S,n` to be a small fixed
relative-width interval around `S_n`, and choose the phases below.  Around the
fine second landing interval place a plateau

\[
 \Phi(x)=T_n\quad(x\in I_{T,n}),                 \tag{3.7}
\]

where `I_T,n` has a small fixed relative width around `T_n`.  Outside all
shells put \(\Phi=1\), and join all pieces by nonnegative Gevrey cutoffs over
intervals comparable to their shell scales.  Choose \(0<\epsilon<10^{-3}\).
The interpolation can be taken positive, so

\[
 1/2\le \Phi(x)\le C(1+|x|).                     \tag{3.8}
\]

Finally normalize

\[
 \phi=\Phi/\|\Phi(G)\|_2.                        \tag{3.9}
\]

The norm in (3.9) lies in a fixed interval about one after `R_1` is large.
It changes only fixed numerical factors in (2.2), which may equivalently be
absorbed when choosing the frequencies.

On a positive phase in `I_R,n`, \(\phi'\asymp L_{0,n}\); on a positive phase
in `I_S,n`, \(\phi'\asymp L_{1,n}\).  Reset slopes have the opposite sign and
magnitude at most the corresponding `L/delta`.

## 4. Activation audit

The activation is positive, smooth, and linearly bounded by (3.8).  At
derivative order `m>=1`, the oscillatory contribution on a shell of scale `X`
and positive slope `L` is at most

\[
 C_m\delta_n^{-m}\frac{L^m}{X^{m-1}}.            \tag{4.1}
\]

For every fixed `m,q`, the `R_n`-shell contribution to the Gaussian moment is
bounded by

\[
 C_{m,q}R_n^{C_{m,q}}
 \exp\{(2mq+C_{m,q})R_n-R_n^2/2\},               \tag{4.2}
\]

and the `S_n`-shell contribution is bounded by

\[
 C_{m,q}S_n^{C_{m,q}}
 \exp\{mqS_n+C_{m,q}R_n-cS_n^2\}.                \tag{4.3}
\]

The terminal plateau and all interpolation ramps give still smaller Gaussian
tails.  Taking the blocks sufficiently separated makes the sums of
(4.2)--(4.3) finite.  Hence

\[
 \boxed{\mathbb E|\phi^{(m)}(G)|^q<\infty
 \quad\text{for every fixed }m,q.}               \tag{4.4}
\]

In particular, all Gaussian integrals defining the local cubic and fifth jets
are finite.  This does not control the adaptive query at `S_n`; that is the
point of the construction.

## 5. Exact two-step OMFP ledger

For one fine step of size `h=h_n`, the established DAG is

\[
 U\sim N(0,1),\quad B\sim N(0,d),\quad
 d=\mathbb E\phi'(G)^2,                           \tag{5.1}
\]

\[
 u_1=U+hB\phi'(U),\quad h_r=\phi(u_r),\quad
 Q_{rs}=\mathbb E[h_rh_s],                       \tag{5.2}
\]

\[
 \rho_{10}=h\mathbb E[\phi'(u_1)\phi'(u_0)],
 \qquad L_{10}=\rho_{10}+hQ_{01},                \tag{5.3}
\]

\[
 z_0=\xi_0,\qquad
 c_0=A\phi'(z_0),\qquad
 a_1=A+h\phi(z_0),\qquad
 z_1=\xi_1+L_{10}c_0,                            \tag{5.4}
\]

where `A` is standard Gaussian and the centered Gaussian pair `xi` has
covariance `Q`.

For the second step put

\[
 c_1=a_1\phi'(z_1),\qquad K_{rs}=\mathbb E[c_rc_s],                  \tag{5.5}
\]

\[
\begin{aligned}
 \sigma_{10}&=\mathbb E\left[
 h\phi'(z_0)\phi'(z_1)
 +L_{10}Aa_1\phi''(z_0)\phi''(z_1)\right],\\
 \sigma_{11}&=\mathbb E[a_1\phi''(z_1)],
\end{aligned}                                                        \tag{5.6}
\]

\[
 b_1=\chi_1+(\sigma_{10}+hK_{01})h_0+\sigma_{11}h_1,                \tag{5.7}
\]

where the centered Gaussian pair `chi` has covariance `K`.  Then

\[
 u_2=u_1+hb_1\phi'(u_1),\qquad Q_{r2}=\mathbb E[h_r\phi(u_2)],       \tag{5.8}
\]

\[
 \rho_{21}=h\mathbb E[\phi'(u_2)\phi'(u_1)],                       \tag{5.9}
\]

\[
 \rho_{20}=h\mathbb E\left[
 \phi'(u_2)\phi'(u_0)
 \{1+h\phi''(u_1)b_1+h\sigma_{11}\phi'(u_1)^2\}
 \right],                                                           \tag{5.10}
\]

\[
 L_{20}=\rho_{20}+hQ_{02},\qquad
 L_{21}=\rho_{21}+hQ_{12},                                         \tag{5.11}
\]

\[
 z_2=\xi_2+L_{20}c_0+L_{21}c_1,qquad
 a_2=A+h\{\phi(z_0)+\phi(z_1)\}.                                  \tag{5.12}
\]

Finally

\[
 F_2(h)=\mathbb E[a_2\phi(z_2)].                                   \tag{5.13}
\]

Equations (5.1)--(5.13) list every reused-row and reused-column response term;
there is no scalar frozen-feature substitution in what follows.

## 6. First-step estimates and transport

Let

\[
 \varepsilon_n=
 C\left(
   p_nL_{0,n}^2\delta_n^{-1}
  +e^{-cS_n^2}L_{1,n}^2\delta_n^{-1}
 \right).                                         \tag{6.1}
\]

By (2.4), \(\varepsilon_n\to0\).  The shell construction and periodic
averaging give

\[
 d\le\varepsilon_n+o(1),                         \tag{6.2}
\]

and

\[
 \|\phi(u_1)-\phi(U)\|_2=o(1),\qquad
 Q_{01}=1+o(1),\quad Q_{11}=1+o(1).              \tag{6.3}
\]

Indeed `u_1=U` off the derivative shells.  On their union, linear growth and
independence of `B,U` give

\[
 \mathbb E[(1+|u_1|)^2;\,U\text{ active}]
 \le C\{p_nR_n^2+h^2d^2+e^{-cS_n^2}S_n^2\}=o(1). \tag{6.4}
\]

The displacement within the first shell has RMS

\[
 hL_{0,n}\sqrt d
 \le C t_n^3\sqrt{p_n/\delta_n}=o(1),             \tag{6.5}
\]

so the same periodic-cell estimate gives

\[
 \mathbb E\phi'(u_1)^2=O(\varepsilon_n),
 \qquad \rho_{10}=o(h).                          \tag{6.6}
\]

Consequently

\[
 L_{10}=h\{1+o(1)\},qquad
 \|\xi_1-\xi_0\|_2=o(1).                        \tag{6.7}
\]

Choose a compact interval \(J\Subset(0,\infty)\), sufficiently narrow, and
choose the `S_n` shell so that for `A in J` and a positive first-shell phase,

\[
 z_1\in I_{S,n}^{\rm core}                       \tag{6.8}
\]

apart from a relative probability `o(1)`.  This follows from

\[
 z_1=\xi_1+h\{1+o(1)\}A L_{0,n}
 =A S_n\{1+o(1)\}.                               \tag{6.9}
\]

The phase `theta_1,n` can be chosen so that a fixed fraction of this smooth
transported law lies in a positive second-shell phase.  Denote the resulting
event by `E_n`.  Periodic averaging and (3.1) give

\[
 \mathbb P(E_n)\ge c_0p_n                         \tag{6.10}
\]

for a numerical \(c_0>0\), while on `E_n`

\[
 a_1\ge c_1>0,qquad c_1\ge c_1L_{1,n}.           \tag{6.11}
\]

In the second inequality the first `c_1` on the left denotes the DAG variable
and the numerical constant on the right can be renamed; equivalently,
\(a_1\phi'(z_1)\ge c_*L_{1,n}\).

The reset part of the first shell sends positive `A` to the negative side and
negative `A` to a scale `S_n/delta_n`, outside `I_S,n`.  Thus it cannot create
a sign-reversed copy of `E_n`.

## 7. The response audit

The positive square in (5.5) has the scale

\[
 c p_nL_{1,n}^2
 \le K_{11}\le C p_nL_{1,n}^2\delta_n^{-1}+o(1). \tag{7.1}
\]

Therefore

\[
 \|\chi_1\|_2\asymp L_{1,n}\sqrt{p_n/\delta_n}.  \tag{7.2}
\]

The mixed Gram needs no cancellation: Cauchy--Schwarz and (6.2), (7.1) give

\[
 h|K_{01}|
 \le C p_n t_n L_{1,n}\delta_n^{-1},             \tag{7.3}
\]

and the ratio of (7.3) to (7.2) is
\(O(t_n\sqrt{p_n/\delta_n})=o(1)\).

The two terms containing \(\phi''(z_1)\) must be integrated before absolute
values.  Conditional on all variables except `A`, (6.9) gives
\(|\partial_Az_1|\asymp S_n\) on the transported core.  Since

\[
 \phi''(z_1)=\frac1{\partial_Az_1}
 \partial_A\{\phi'(z_1)\},                       \tag{7.4}
\]

one integration by parts in `A` transfers the derivative to the Gaussian
density, the fixed cutoff of `J`, and the slowly varying prefactor.  Boundary
terms vanish by the Gevrey cutoff.  Using
\(|\phi'|\le C L_{1,n}/\delta_n\) on `I_S,n` gives

\[
 |\sigma_{11}|
 \le C\frac{p_nL_{1,n}}{S_n\delta_n}+o(1),        \tag{7.5}
\]

and

\[
 |\sigma_{10}|
 \le C L_{1,n}\left{
   \frac{p_nt_n^2}{R_n\delta_n^2}
  +\frac{p_nt_n}{\delta_n}
 \right}+o(1).                                  \tag{7.6}
\]

The first term in braces comes from
\(L_{10}Aa_1\phi''(z_0)\phi''(z_1)\), using
\(|\phi''(z_0)|\le Ct_n^4/(R_n\delta_n^2)\),
`L_10~1/t_n`, and the extra `1/S_n=1/t_n` in (7.4).  The second comes from the
first term of `sigma_10`.  Dividing (7.5)--(7.6) by (7.2) and using (2.4)
shows

\[
 |\sigma_{10}|+|\sigma_{11}|=o(\sqrt{K_{11}}).   \tag{7.7}
\]

Since `h_0,h_1` are bounded in every fixed `L^q` by (6.3), (5.7) now yields

\[
 \|b_1-\chi_1\|_2=o(\sqrt{K_{11}}).              \tag{7.8}
\]

This is the exact aggregate-response estimate required at two steps.  The
large positive square `K_11` remains; every signed response is lower order.

## 8. Lower-layer second update and the fine landing

Only lower particles in derivative shells move in (5.8).  Combining (6.2),
(7.1), and (7.8) gives the crude active-population RMS displacement

\[
 \|h b_1\phi'(u_1)\|_2
 \le C t_nL_{1,n}p_n\delta_n^{-1}.               \tag{8.1}
\]

Relative to the selected top jump `T_n=L_1,n/t_n`, this is

\[
 \frac{t_nL_{1,n}p_n\delta_n^{-1}}{T_n}
 =t_n^2p_n\delta_n^{-1}=o(1).                    \tag{8.2}
\]

More is true because `Phi=1` between the `S_n` and `T_n` blocks.  Conditional
on a first-shell lower particle, the dominant `chi_1` displacement has a
Gaussian density at scale

\[
 D_n=t_nL_{1,n}\sqrt{p_n/\delta_n},qquad
 D_n/T_n=t_n^2\sqrt{p_n/\delta_n}=o(1).           \tag{8.3}
\]

Direct shell-probability integration therefore gives

\[
 \|\phi(u_2)-1\|_2=o(1),qquad
 Q_{02}=Q_{12}=Q_{22}=1+o(1),                    \tag{8.4}
\]

and

\[
 \rho_{21}=o(h),qquad \rho_{20}=o(h).           \tag{8.5}
\]

For completeness, the worst apparently dangerous part of (5.10) is the
first-shell contribution containing `phi''(u_1)b_1`.  On landing in the
`S_n` shell, the `b_1`-density contributes the reciprocal factor
\((L_{1,n}\sqrt{p_n/\delta_n})^{-1}\).  After the two explicit factors of `h`
in (5.10), its ratio to `h` is bounded by

\[
 C R_n^C t_n^5\sqrt{p_n}\delta_n^{-C}=o(1),      \tag{8.6}
\]

by (2.4).  Landings in the `R_n` shell are smaller; the terminal plateau has
zero derivative; later blocks are controlled by the recursive tail condition
of Section 10.  This proves (8.5), rather than assuming it.

Equations (5.11), (8.4), and (8.5) imply

\[
 L_{20}=h\{1+o(1)\},\qquad L_{21}=h\{1+o(1)\}.   \tag{8.7}
\]

Moreover the fresh field and the old-source term obey

\[
 \xi_2=O_{L^2}(1),\qquad L_{20}c_0=O(t_n),        \tag{8.8}
\]

both negligible compared with `T_n`.  On `E_n`, (5.12) therefore gives

\[
 z_2=T_n\{a_1+o_{\mathbb P}(1)\}.                \tag{8.9}
\]

Choose `I_T,n` to contain the compact range on the right of (8.9).  Shrinking
`E_n` by a relative `o(1)` if necessary,

\[
 \phi(z_2)\ge cT_n,qquad a_2\ge c>0.            \tag{8.10}
\]

## 9. Signed fine/coarse comparison

The positive event gives

\[
 \mathbb E[a_2\phi(z_2);E_n]\ge c p_nT_n.        \tag{9.1}
\]

All possible negative terminal-plateau hits are lower order:

1. bulk initial `z_0` has zero derivative and cannot reach `I_T,n` except by a
   Gaussian tail of order \(e^{-cT_n^2}\);
2. `A<0` on a positive first phase is sent to the negative half-line;
3. a reset first phase is sent to scale `S_n/delta_n`, disjoint from `I_S,n`;
4. initialization directly in `I_S,n` has probability `e^{-cS_n^2}` and hence
   contributes at most \(e^{-cS_n^2+C S_n}=o(p_nT_n)\);
5. later blocks satisfy Section 10.

The same partition, using linear growth off `I_T,n`, bounds the entire negative
part by `o(p_nT_n)`.  Hence

\[
 \boxed{F_2(h_n)\ge c p_nT_n\longrightarrow+\infty.}                \tag{9.2}
\]

For one coarse step `2h_n`, a positive first phase lands near `2S_n`, while a
reset lands at scale `2S_n/delta_n`; both are disjoint from `I_S,n`.  A direct
initial `I_S,n` hit is charged by `e^{-cS_n^2}`.  The one-step version of the
preceding partition therefore gives

\[
 \boxed{\sup_n|F_1(2h_n)|<\infty.}               \tag{9.3}
\]

Every local Gaussian jet coefficient, including `kappa_1`, is finite by
(4.4).  Thus \(\kappa_1h_n^3\to0\), and (9.2)--(9.3) yield

\[
 \frac{|\Delta_1(h_n)-\kappa_1h_n^3|}{h_n^5}
 \longrightarrow\infty.                         \tag{9.4}
\]

This is much stronger than super-`t^5` growth: under linear growth alone, no
punctured small-step interval estimate exists even at fixed `t=1`.

## 10. Width-first truncation bridge

Let `phi^(N)` retain only the first `N` ladder blocks.  It has bounded
derivatives of every order, so the established fixed-step finite-width theorem
identifies its one- and two-step limits with (5.1)--(5.13).

The block centers are chosen recursively.  After blocks `1,...,N-1` have been
fixed, their one- and two-step finite-width nodes at each of the finitely many
meshes `h_1,...,h_(N-1)` are functions of finitely many Gaussian matrices with
a finite global Lipschitz envelope.  Hence their tails are sub-Gaussian with
some explicit finite constants `C_(N-1,k)`.  Choose `R_N` so large that, for
every `k<N`, every node used at one or two steps, and every monomial degree up
to `4N`, the contribution from entering block `N` is at most

\[
 2^{-N}e^{-T_k}.                                  \tag{10.1}
\]

This is possible because a new `S_N`-block derivative contributes
\(e^{qS_N}\), whereas the old truncated node tail at `S_N` is bounded by
\(e^{-S_N^2/C_{N-1,k}}\); terminal values are handled by
\(e^{-T_N^2/C_{N-1,k}}\).  The same choice also enforces (4.2)--(4.3).

Summing (10.1) proves uniform integrability of every one- and two-step Gram,
response coefficient, and terminal output, uniformly in width and in the
truncation index.  Therefore

\[
 \lim_{N\to\infty}\lim_{m\to\infty}F^{(N)}_{r,m}(h_k)
 =\lim_{m\to\infty}F_{r,m}(h_k),\qquad r=1,2,    \tag{10.2}
\]

and the common value is the infinite-block DAG used above.  The order in
(10.2) is width first at each fixed nonzero `h_k`; no finite-width Taylor
expansion or width/learning-rate interchange is used.

The recursion terminates at each stage because only finitely many earlier
meshes and finitely many one/two-step nodes occur.  It defines one fixed
activation after taking the locally finite union of all blocks.

## 11. Adversarial audit

1. **Literal fifth coefficient.**  No super-`t^5` Taylor coefficient is
   asserted.  The exact fifth coefficient remains quartic in `t`.  The failure
   is nonlocal in `h` and comes from moving Gaussian tails.
2. **Single-spike cancellation.**  A single narrow second spike would lose a
   factor `L_1^{-1}` in transported mass.  The oscillatory shell supplies
   order `L_1` branches and avoids this cancellation.
3. **Readout-sign cancellation.**  The asymmetric reset sends the
   sign-reversed initial rows outside the second shell; Section 9 separately
   bounds every negative terminal-plateau route.
4. **Reused matrices.**  All response coefficients `sigma`, `rho`, and mixed
   Gram `K_01` appear in Sections 5--8.  The positive square `K_11` is retained,
   and the signed `phi''` responses are integrated by parts before absolute
   values.
5. **Lower adaptive query.**  It is not bounded by an initialization Gaussian
   moment.  Its transported scale `D_n` is computed in (8.3), and shell-hitting
   probabilities prove (8.4)--(8.6).
6. **Infinite activation.**  Section 10 supplies a diagonal truncation and
   uniform-integrability condition; merely observing (4.4) would not close the
   fixed-step width-first bridge.
7. **Quantifiers.**  The activation is fixed after the recursive construction.
   The sequence `h_n` is then chosen from its fixed block scales.  Failure along
   this one sequence is enough to refute a bound on every
   `0<|h|<=rho` at `t=1`.
