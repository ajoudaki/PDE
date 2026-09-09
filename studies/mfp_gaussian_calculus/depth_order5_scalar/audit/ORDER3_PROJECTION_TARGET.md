# Frozen lower-order projection target

This is Section 7.1 of the accepted order-three recursion rewritten in the
current unit-Gram/shared-activation notation.  It was recorded before the
order-five candidate was inspected.

Put

\[
\begin{gathered}
d=M_{020000},\quad u=M_{040000},\quad v=M_{101000},
\quad m=M_{121000},\\
r=M_{010100},\quad s=M_{002000},\quad j=M_{030100},
\quad e=M_{022000},\quad h=M_{220000},\\
b_\ell=d^{H-\ell},\qquad p_\ell=d^{H-\ell+1},\qquad
\tau_\ell=\sum_{i=0}^{\ell}d^i.
\end{gathered}
\]

The duplicate semantic atom called \(w\) in the source is the same
commutative atom \(m=M_{121000}\).

The three forward scalars initialize as

\[
V_1=b_1u,\qquad N_1=b_1m,\qquad J_1=3b_1j,
\]

and for \(2\le\ell\le H\) obey

\[
V_\ell=dV_{\ell-1}+\tau_{\ell-1}^2b_\ell u,
\]

\[
N_\ell=vV_{\ell-1}+\tau_{\ell-1}^2b_\ell m
 +(d+v)N_{\ell-1},
\]

\[
\begin{split}
J_\ell={}&3\tau_{\ell-1}V_{\ell-1}r
3\tau_{\ell-1}^3b_\ell j\\
&+3\tau_{\ell-1}N_{\ell-1}(r+s)
 +(J_{\ell-1}+3N_{\ell-1})d.
\end{split}
\]

For the two reverse scalars set

\[
\beta_{H+1}=0,qquad\chi_{H+1}=1,qquad V_0=0,
\]

and for \(\ell=H,H-1,\ldots,1\),

\[
\begin{split}
\beta_\ell={}&b_\ell V_{\ell-1}s
 +3\tau_{\ell-1}^2b_\ell^2e+d\beta_{\ell+1}
 +\chi_{\ell+1}^2h
 +2\tau_{\ell-1}\chi_{\ell+1}b_\ell m,
\end{split}
\]

\[
\chi_\ell=p_\ell+\tau_{\ell-1}b_\ell(r+s)
 +\chi_{\ell+1}(v+d).
\]

The current notation calls the old third-order correction \(B_H\):

\[
\boxed{
B_H=2(J_H+3N_H)+4\left[V_H+\beta_1
+\sum_{\ell=2}^H(\beta_\ell+p_\ell V_{\ell-1})\right].}
\]

An order-five witness passes the projection gate only if these are literally
its lower-order states/transitions, or if it prints an explicit algebraic
change of state proving equivalence.  Agreement of three terminal \(B_H\)
maps alone is weaker.
