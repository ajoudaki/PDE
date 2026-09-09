# A globally smooth ReLU-like activation with super-polynomial uniform remainder

This note applies the already audited full-`L=2` insertion theorem in
`SUPER_T5_EFFECTIVE_REMAINDER.md` to a ReLU-like base.  It does not infer a
smooth result by continuity from the hard ReLU kink.

### Theorem

Fix

\[
 0\le\lambda<1,\qquad \tau>0,\qquad \epsilon>0,
 \qquad \rho>0.
\]

Here

\[
 \mathcal B_\phi(t,\rho)=
 \inf_{\kappa\in\mathbb R}\sup_{0<h\le\rho/t}
 { |F_{2t}^\phi(h)-F_t^\phi(2h)-\kappa h^3|\over h^5}.
\]

There is an RMS-normalized activation `tilde phi` such that

\[
 \widetilde\phi\in C^\infty(\mathbb R),\qquad
 |\widetilde\phi(x)|\le C(1+|x|),\qquad
 \|\widetilde\phi'\|_\infty<\infty,
\tag{0.1}
\]

all its fixed-finite-schedule width-first outputs exist and are finite,

\[
 d_1\!\left(\widetilde\phi,
 {b_{\lambda,\tau}\over\|b_{\lambda,\tau}(G)\|_2}
 \right)<\epsilon,                                      \tag{0.2}
\]

and, for every integer `N>=2`,

\[
 \mathcal B_{\widetilde\phi}(N,\rho)
 \ge {3\over5}N^{N+6}-2\ge N^N.                         \tag{0.3}
\]

Thus the uniform remainder coefficient is `Omega(N^N)` and, in particular,
is not `o(N^5)`.

## 1. Smooth affine-tail base

Define

\[
 \vartheta(x)=\begin{cases}0,&x\le0,\\ e^{-1/x},&x>0,\end{cases}
 \qquad
 S(x)=\frac{\vartheta(x+1)}
 {\vartheta(x+1)+\vartheta(1-x)}.
\tag{1.1}
\]

Then `S in C^infinity`, `0<=S<=1`,

\[
 S(x)=0\ (x\le-1),\qquad S(x)=1\ (x\ge1),
 \qquad S(-x)=1-S(x).
\]

For `0<=lambda<1` and `tau>0`, put

\[
 b_{\lambda,\tau}(x)
 =\lambda x+(1-\lambda)\int_{-\infty}^xS(y/\tau)\,dy.
\tag{1.2}
\]

Since `int_{-1}^1 S=1`,

\[
 b_{\lambda,\tau}(x)=\lambda x\quad(x\le-\tau),
 \qquad
 b_{\lambda,\tau}(x)=x\quad(x\ge\tau).
\tag{1.3}
\]

Thus `lambda=0` gives a smooth ReLU and `0<lambda<1` gives a smooth leaky
ReLU.  The raw base is globally smooth, nondecreasing, linearly growing,
and has bounded derivatives of every fixed order.

## 2. Remote compact perturbations

Choose a nonzero `p in C_c^infinity((-1/4,1/4))` satisfying `int p=0`, and
let

\[
 P(y)=\int_{-\infty}^yp(s)\,ds.
\]

Then `P` is also compactly supported.  One completely explicit choice is

\[
 P(y)=\begin{cases}
 \exp[-1/(1-16y^2)],&|y|<1/4,\\
 0,&|y|\ge1/4,
 \end{cases}
 \qquad p=P'.
\tag{2.0}
\]

It has `int p=P(+infinity)-P(-infinity)=0` and is nonzero.  On mutually
disjoint intervals with `X_m->+infinity`, define

\[
 \Phi(x)=b_{\lambda,\tau}(x)
 +\sum_{m\ge2}\delta_mw_m
 P\!\left(\frac{x-X_m}{w_m}\right),
 \qquad
 \widetilde\phi(x)=\frac{\Phi(x)}{\|\Phi(G)\|_2}.
\tag{2.1}
\]

The sum is locally finite, so `Phi` is `C^infinity` at every real point.
Moreover,

\[
 \Phi'(x)=b_{\lambda,\tau}'(x)
 +\sum_m\delta_mp\!\left(\frac{x-X_m}{w_m}\right).
\tag{2.2}
\]

At most one summand in (2.2) is nonzero.  Choose

\[
 \sup_m\delta_m\|p\|_\infty\le\frac12.
\tag{2.3}
\]

All bump intervals lie in the right affine tail, where the base slope is
one.  Hence `Phi'` is bounded, and it remains nonnegative.  If `lambda>0`,
then `inf Phi'>=min(lambda,1/2)>0`.  Also

\[
 |\Phi(x)|\le C(1+|x|).
\]

For linearly growing activations write

\[
 d_1(f,g)=\sup_x\frac{|f(x)-g(x)|}{1+|x|}
          +\|f'-g'\|_\infty.
\tag{2.4}
\]

Disjointness gives, provided `w_m<1` and `X_m>1`,

\[
 d_1(\Phi,b_{\lambda,\tau})
 \le \sup_m\left\{
 \delta_m\|p\|_\infty+
 \frac{\delta_mw_m\|P\|_\infty}
      {1+X_m-w_m/4}\right\}.                  \tag{2.5}
\]

If the right side is `eta`, then
`||Phi(G)-b(G)||_2<=eta||1+|G|||_2`.  Once this is at most
`||b(G)||_2/2`, elementary normalization gives

\[
 d_1\!\left(
 {\Phi\over\|\Phi(G)\|_2},
 {b_{\lambda,\tau}\over\|b_{\lambda,\tau}(G)\|_2}
 \right)
 \le C_{\lambda,\tau}\eta,                  \tag{2.6}
\]

where, for example,

\[
 C_{\lambda,\tau}
 =\frac2{\|b(G)\|_2}
 +\frac{2d_1(b,0)\|1+|G|\|_2}{\|b(G)\|_2^2}.
\]

Thus the final activation can be made arbitrarily close in weighted `C^1`
to the ordinary smooth ReLU/leaky-ReLU base.

## 3. Choice of the ladder and exact violation

Fix `rho>0`.  Start the insertion recursion of
`SUPER_T5_EFFECTIVE_REMAINDER.md` from (1.2), rather than from the identity.
This is legitimate because every new support lies to the right of the
previous supports, where the current raw activation is exactly affine with
strictly positive slope one.  The arbitrary-old-ladder principal symbol and
all old/new subset margins in that theorem therefore apply unchanged.

At stage `N`, take `t_N=N` and impose the target

\[
 [h^5]\Delta_{t_N}^{\psi_N}(h)\le-t_N^{N+6}.
\tag{3.1}
\]

The insertion lemma permits (3.1) below every prescribed amplitude ceiling:
choose `X_N` sufficiently far out and then choose `delta_N` sufficiently
small, with `w_N=delta_N sqrt(gamma(X_N))`.  Impose simultaneously

\[
 \delta_N\|p\|_\infty<2^{-N}\eta
\]

and all finitely many previously reserved fixed-step `C^1` tail budgets.
The choices terminate at every finite stage.  After fixing the two rates
`h_N` and `h_N/2`, the exact two-rate minimax argument gives

\[
 \boxed{
 \mathcal B_{\widetilde\phi}(N,\rho)
 \ge {3\over5}N^{N+6}-2,
 \qquad N\ge2.}
\tag{3.2}
\]

For `N>=2`, `(3/5)N^6-2/N^N>=1`; multiplying by `N^N` proves the second
inequality in (0.3) with the explicit `Omega(N^N)` constant one.

All fixed-step width-first outputs are finite: the activation and its slope
are linearly/boundedly controlled, and the finite-schedule coupling uses only
the `d_1` tail.  RMS normalization is already included in (2.1) and in the
insertion theorem's normalization estimate.

Therefore, for every `epsilon>0`, there is an RMS-normalized
`C^infinity`, linearly growing activation satisfying

\[
 d_1(\widetilde\phi,
 b_{\lambda,\tau}/\|b_{\lambda,\tau}(G)\|_2)<\epsilon
\]

and whose uniform cubic-subtracted fifth remainder grows faster than every
polynomial, in particular faster than `t^5` and at least on the order of
`t^t` along the displayed integer sequence.

The construction has an unbounded global hierarchy of higher derivatives:
the widths `w_m` tend rapidly to zero.  Thus this theorem does not claim that
ordinary softplus or the unperturbed base (1.2) itself violates the uniform
property.
