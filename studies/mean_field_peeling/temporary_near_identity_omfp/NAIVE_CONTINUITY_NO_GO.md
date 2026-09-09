# Why fixed-\(t\) continuity at the identity is not the needed openness

Let

\[
 \psi_{\varepsilon}(x)
 =s_\varepsilon^{-1}\{x+\varepsilon\varphi(x)\},
\]

and suppose \(\varphi''(x_0)\ne0\).  The Banach state used by the proved
identity-activation theorem has Hilbert \(L^2\) vector blocks.  At the
constant field \(x_0\), the formal second Nemytskii derivative is

\[
 D^2N_{\psi_\varepsilon}(x_0)[v,w]
 =\frac{\varepsilon}{s_\varepsilon}
   \varphi''(x_0)vw.                                  \tag{1}
\]

On a nonatomic probability space choose sets \(E_m\) of probability
\(m^{-1}\) and put \(v_m=\sqrt m\,\mathbf1_{E_m}\).  Then

\[
 \|v_m\|_2=1,\qquad \|v_m^2\|_2=\sqrt m.
\]

Consequently, for every \(\varepsilon\ne0\),

\[
 \sup_{\|v\|_2,\|w\|_2\le1}
 \|D^2N_{\psi_\varepsilon}(x_0)[v,w]\|_2=\infty,       \tag{2}
\]

whereas this second derivative vanishes at \(\varepsilon=0\).  Equivalently,
at finite width \(n\), using normalized Euclidean norm and
\(v_n=\sqrt n\,e_1\), the norm in (2) is at least

\[
 \frac{|\varepsilon\varphi''(x_0)|}{s_\varepsilon}\sqrt n.
\]

Thus the ambient \(C^2\), and hence \(C^4\), norm is not continuous at the
identity.  The already proved Banach transported-defect theorem cannot be
opened to nonzero \(\varepsilon\) by a norm-continuity argument.

There is a second, purely quantifier-level obstruction.  Continuity of a
canonical coefficient \(b_t(\varepsilon)\) for each fixed \(t\), together
with \(b_t(0)\lesssim t^4\), does not imply a common nonzero radius.  The
entire scalar family

\[
 b_t(\varepsilon)=t^4e^{|\varepsilon|t}
\]

has both properties but violates every sub-\(t^5\) bound at each fixed
\(\varepsilon\ne0\).  This is not asserted to be an OMFP coefficient; it
proves that fixed-\(t\) continuity alone has insufficient logical content.

The correct perturbative target must instead be continuity in a
history-uniform **reachable causal-response norm**, or an amplitude expansion
whose convergence radius is controlled by total step variation
\(\sum_s|h_s|\), not by the number of steps.
