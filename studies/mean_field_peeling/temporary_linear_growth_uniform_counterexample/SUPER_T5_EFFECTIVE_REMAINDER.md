# A single bounded-slope activation with super-polynomial effective fifth remainder

## 1. Statement

Use the `q=1`, two-hidden-layer network

\[
 H_j=\phi(u_j),\qquad z_i=n^{-1/2}\sum_jW_{ij}H_j,
 \qquad f_n=n^{-1}\sum_i a_i\phi(z_i),
\]

with independent standard-Gaussian initialization and the simultaneous
feature/output ascent update

\[
\begin{aligned}
 a_i^+&=a_i+h\phi(z_i),\\
 W_{ij}^+&=W_{ij}+{h\over\sqrt n}a_i\phi'(z_i)H_j,\\
 u_j^+&=u_j+h\phi'(u_j)n^{-1/2}\sum_iW_{ij}a_i\phi'(z_i).
\end{aligned}
\]

Let `F_k^phi(h)` be the expected-output width limit at fixed `h`, and put

\[
 \Delta_t^\phi(h)=F_{2t}^\phi(h)-F_t^\phi(2h).
\]

For `rho>0`, define the best possible uniform cubic-subtracted fifth
coefficient

\[
 \mathcal B_\phi(t,\rho)
 =\inf_{\kappa\in\mathbb R}\ \sup_{0<h\le\rho/t}
 { |\Delta_t^\phi(h)-\kappa h^3|\over h^5}.
 \tag{1.1}
\]

### Theorem 1.1

For every `rho>0` there is an RMS-normalized activation `phi` such that

\[
 \phi\in C^\infty(\mathbb R),\qquad
 0<c_\phi\le\phi'(x)\le C_\phi<\infty,
 \qquad |\phi(x)|\le C_\phi(1+|x|),
 \tag{1.2}
\]

all fixed-step width-first outputs in (1.1) exist and are finite, and, with
`t_N=N`, `N>=2`,

\[
 \boxed{
 \mathcal B_\phi(t_N,\rho)
 \ge {3\over5}t_N^{N+6}-2.}
 \tag{1.3}
\]

In particular `mathcal B_phi(t_N,rho)/t_N^p -> infinity` for every fixed
power `p`, and hence in particular for `p=5`.

This is a statement about exact fixed-nonzero-step width-first outputs.  It
does not claim that the final activation has a finite literal fifth Taylor
coefficient.  In fact a finite literal coefficient can never be the desired
counterexample: whenever that jet exists, Euler chronology makes it a
polynomial of degree at most four in `t`.

## 2. Exact general-horizon principal symbol

For a smooth finite truncation, the fifth coefficient of `Delta_t` is a
linear combination of the six gradient elementary differentials

\[
\begin{gathered}
 E_1=V[g^5],\quad E_2=U[Hg,g^3],\quad
 E_3=T[T[g,g],g,g],\\
 E_4=T[H^2g,g,g],\quad E_5=T[Hg,Hg,g],\quad
 E_6=\|H^2g\|^2.
\end{gathered}
\]

Direct iteration of the Euler jet gives the respective weights

\[
\begin{aligned}
 W_1&={t^4\over3}-{t^3\over3}+{t\over24},\\
 W_2&={19t^4\over3}-{23t^3\over3}+{35t^2\over12}+{t\over12},\\
 W_3&={13t^4\over3}-6t^3+{35t^2\over12}-{t\over4},\\
 W_4&={43t^4\over3}-27t^3+{203t^2\over12}-{15t\over4},\\
 W_5&={46t^4\over3}-26t^3+{91t^2\over6}-{7t\over2},\\
 W_6&={32t^4\over3}-28t^3+{70t^2\over3}-6t.
\end{aligned}
\tag{2.1}
\]

For completeness, these follow by writing
`x_N-x_0=sum_(r=1)^5 h^r x_r+O(h^6)`, substituting it into one Euler
step, and reducing the terminal Taylor expansion to the six contractions.
Each coefficient is a degree-five polynomial in `N`; replacing `N` by
`2t` and subtracting `32` times its value at `t` cancels degree five and
gives (2.1).  The exact rational recurrence is independently executable in
`general_t_transition_weights.py`.

Choose `p in C_c^infinity((-1/4,1/4))`, with `int p=0` and
`I=int (p'')^2>0`, and put

\[
 P(y)=\int_{-\infty}^y p(s)\,ds.
\]

Both `p` and `P` are compactly supported.  Perturb the activation near one
preactivation by

\[
 \phi_{\rm new}(x)-\phi_{\rm old}(x)
 =\delta wP((x-X)/w),
 \qquad
 \phi_{\rm new}'(x)-\phi_{\rm old}'(x)
 =\delta p((x-X)/w).
 \tag{2.2}
\]

At one node write

\[
 r=\partial_y\widehat f,\qquad
 s=\ell^TG\ell,\qquad v=\ell^TG\nabla f,
 \quad \ell=\nabla x.
\]

At quadratic amplitude and singular excess four, only `E_1,E_2,E_3`
contribute.  Their integrated weights are respectively `5,-1,1`, so (2.1)
gives

\[
 5W_1-W_2+W_3=-{t^4\over3}-{t\over8}.
\]

Thus the complete same-node principal term is

\[
 -\left({t^4\over3}+{t\over8}\right)
 r^2sv^4\gamma(X){\delta^2\over w^3}I.
 \tag{2.3}
\]

This expression is nonpositive at every node and strictly negative at the
lower nodes.  Indeed there

\[
 r_j={b_j\over n},\qquad s_j=n,\qquad v_j=b_jb,
\]

and the conditional width limit gives

\[
 {1\over n}\sum_jb_j^6\longrightarrow15d^3,
 \qquad d=\mathbb E\phi_{\rm old}'(G)^2>0.
\]

Consequently the lower layer contributes

\[
 -15\left({t^4\over3}+{t\over8}\right)
 d^3b^4\gamma(X){\delta^2\over w^3}I.
 \tag{2.4}
\]

The first three values of the node factor are

\[
 -{11\over24},\qquad -{67\over12},\qquad-{219\over8}.
\]

The marked-source Gaussian peel preserves (2.3).  At finite width attach a
formal mark to every occurrence of the new bump before eliminating a reused
Gaussian matrix source.  For every such source `J`, Stein's identity holds
at fixed marks,

\[
 \mathbb E[J V(J,z)]=\mathbb E[\partial_JV(J,z)].
\]

The finite truncation has bounded derivatives, so both sides and their mark
derivatives have a common Gaussian-polynomial dominator.  Differentiation
in the marks therefore commutes with expectation, and
`partial_z partial_J=partial_J partial_z`.  Iterating this exact identity
over the finitely many chronological row/column sources retains every
reused `W/W^T` response while preserving each marked group.  The normalized
contractions have uniform Gaussian moments, so the same marked identity
passes to the established fixed-order width-first OMFP DAG.

Here is the complete remainder grading before the marked groups are
flattened.  If a group uses `R` distinct new Gaussian source classes, has
`k` new bump factors, and total activation-derivative excess

\[
 e=\sum(r-1),
\]

then order five gives `e<=4`, and direct integration on the `R` bump
intervals bounds it by

\[
 C\delta^k\gamma(X)^R w^{R-e}.
\]

After division by the principal scale in (2.5), its two margins are

\[
 m_\delta=k+R-e+1,
 \qquad 2m_\gamma=3R-e+1.                    \tag{2.5a}
\]

Since `k>=R`, both margins are positive for `R>=2`.  For `R=1`, every
`e<=3` group has a positive margin.  At `e=4`, a lone fifth derivative is
an apparent `(k,e)=(1,4)` block, but four integrations by parts against its
smooth Gaussian coefficient remove every negative power of `w`.  The only
true zero-margin case is `(R,k,e)=(1,2,4)`, and its complete grouped value is
exactly (2.3).  The sixth elementary differential `||H^2g||^2` creates
conservative zero blocks after a flattened Stein expansion, but has no true
quadratic `e=4` sector: four Hessian singular factors, hence `k=4`, are
needed to attain `e=4`.  This proves rather than assumes that it is part of
the positive-margin remainder.

The independent all-six exact census confirms this grouping.  The six
response-aware elementary maps contain respectively

\[
 76,\ 383,\ 192,\ 496,\ 770,\ 515
\]

terms and their general-`t` polynomial union has 1045 layer-separated
terms.  Exhausting every old/new atom subset gives zero negative-margin
subsets.  `E_6` alone has 84 conservative zero entries, but its three raw
identity-background principal weights are `(16,16,0)`, whose integrated
combination is `16-16+0=0`.  The complete total/lower/upper integrated
principal polynomials are

\[
 -215t^4-{645\over8}t,\qquad
 -5t^4-{15\over8}t,\qquad
 -210t^4-{315\over4}t,
\]

in exact agreement with (2.3)--(2.4).  The executable certificate is
`audit_general_t_transition_map.py`.

Put

\[
 w=\delta\sqrt{\gamma(X)},\qquad
 S={\delta^2\gamma(X)\over w^3}
 ={1\over\delta\sqrt{\gamma(X)}}.
 \tag{2.5}
\]

Every nonprincipal marked block is `o(S)` by first taking `X` large and
then `delta` small.  Old high-derivative atoms are fixed finite constants;
putting the new interval to the right of all old intervals makes old and new
singular derivatives disjoint within each Gaussian atom.  RMS normalization
changes the old finite moment polynomial by a Gaussian-tail-small additive
amount and the principal term by a positive `1+o(1)` factor.  Therefore,
for every fixed finite old ladder, fixed integer `t`, amplitude ceiling
`epsilon>0`, and target `A>0`, a new transition can be chosen with
`delta<epsilon` so that the normalized smooth truncation satisfies

\[
 [h^5]\Delta_t(h)<-A.
 \tag{2.6}
\]

This is the insertion lemma used below.

## 3. Fixed-step stability uses only `C^1`

For linearly growing activations define

\[
 d_1(\phi,\psi)=
 \sup_x{|\phi(x)-\psi(x)|\over1+|x|}
 +\|\phi'-\psi'\|_\infty.
\]

For a fixed smooth bounded-slope reference `psi`, a fixed number of steps
`k`, and a compact step interval, coupling two finite-width networks at the
same initialization gives

\[
 \sup_n\mathbb E|f_{k,n}^{\phi}(h)-f_{k,n}^{\psi}(h)|
 \le C_{\psi,k,R}d_1(\phi,\psi)
 \tag{3.1}
\]

whenever `d_1` is sufficiently small and the perturbed slopes have a common
bound.  To prove (3.1), use normalized vector norms and `M=W/sqrt(n)`.
Every state after finitely many updates is bounded by a fixed polynomial in

\[
 1+\|a^0\|_n+\|u^0\|_n+\|M^0\|_{op}.
\]

The moments of this quantity are uniform in `n`.  The two activation-node
differences are bounded by the slope bound and by `d_1(1+|x|)`; the two
slope-node differences are bounded by `d_1` plus the fixed reference's
second-derivative bound.  Induction through the finite update schedule and
expectation prove (3.1).  No derivative of the perturbed activation above
order one is used.

## 4. Construction of one activation

Choose the compact bump `(p,P)` from (2.2) and successive disjoint intervals
tending to `+infinity`.  Starting from the identity, let

\[
 \Phi_N(x)=x+\sum_{m\le N}\delta_mw_m
 P((x-X_m)/w_m),
 \qquad
 
 \psi_N={\Phi_N\over\|\Phi_N(G)\|_2}.
\]

At stage `N`, set `t_N=N` and `A_N=t_N^(N+6)`.  Apply (2.6), subject to all
previously imposed amplitude ceilings, so that

\[
 \beta_N:=[h^5]\Delta_{t_N}^{\psi_N}(h)\le-A_N.
 \tag{4.1}
\]

For a smooth truncation, symmetry of the Gaussian readout implies
`F_k(-h)=-F_k(h)`, while equal total time cancels the linear term.  Hence

\[
 \Delta_{t_N}^{\psi_N}(h)
 =\kappa_Nh^3+\beta_Nh^5+o(h^5).
 \tag{4.2}
\]

Choose `h_N` with `0<h_N<=rho/t_N` so small that (4.2), at both `h_N` and
`h_N/2`, has normalized error at most `1/4`.

After these two nonzero rates have been fixed, apply (3.1) to the four
schedules

\[
 (2t_N,h_N),\quad(t_N,2h_N),\quad
 (2t_N,h_N/2),\quad(t_N,h_N).
\]

Reserve a positive tail-amplitude budget making the total eventual change
of each output at most `(h_N/2)^5/16`.  At every later stage there are only
finitely many old budgets, and (2.6) works below an arbitrary amplitude
ceiling; choosing geometrically smaller future amplitudes satisfies all
budgets simultaneously.

The locally finite limiting slope is bounded above and below because the
amplitudes are summable (take `sum delta_m ||p||_infinity<1/2`).  Its
activation `Phi` is `C^infinity` and equals the identity off the disjoint
bump intervals, and `phi=Phi/||Phi(G)||_2` satisfies (1.2).  Include the elementary
normalization estimate in each tail budget; for summable amplitudes,

\[
 d_1(\phi,\psi_N)\le5\sum_{m>N}\delta_m.
 \tag{4.3}
\]

Enumerating all finite schedules and compact step intervals in the same
budgets, (3.1) gives a uniform-in-width three-epsilon argument: every exact
fixed-step expected output of `phi` is the limit of the corresponding
smooth-truncation width limits.  Hence all outputs in (1.1) exist and are
finite.  Width is always sent to infinity at fixed nonzero `h`; no Taylor
jet of the final activation is invoked.

## 5. Two-rate minimax and the super-`t^5` conclusion

Fix an arbitrary `kappa in R` and put

\[
 x={\kappa_N-\kappa\over h_N^2}.
\]

The truncation expansion and the exact-output tail budgets give

\[
\begin{aligned}
 {\Delta_{t_N}^{\phi}(h_N)-\kappa h_N^3\over h_N^5}
   &=x+\beta_N+e_{1,N},\\
 {\Delta_{t_N}^{\phi}(h_N/2)-\kappa(h_N/2)^3\over(h_N/2)^5}
   &=4x+\beta_N+e_{2,N},
\end{aligned}
\]

with `|e_(i,N)|<=1`.  The exact identity

\[
 3\beta_N=4(x+\beta_N)-(4x+\beta_N)
\]

implies

\[
 \max\{|x+\beta_N|,|4x+\beta_N|\}
 \ge {3\over5}|\beta_N|.
\]

Both rates lie in `(0,rho/t_N]`; consequently, uniformly over the arbitrary
choice of `kappa`,

\[
 \mathcal B_\phi(t_N,\rho)
 \ge {3\over5}|\beta_N|-2
 \ge {3\over5}t_N^{N+6}-2.
\]

This proves Theorem 1.1.
