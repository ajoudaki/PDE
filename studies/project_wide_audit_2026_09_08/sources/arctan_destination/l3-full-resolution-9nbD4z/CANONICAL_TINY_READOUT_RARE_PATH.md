# Direct rare-path estimates for the canonical tiny readout

This note proves a finite-width, positive-feature-time extension of the
actual rare derivative, rare energy, and prefix-query estimates to
\(W^{(4)}_0=G^{(4)}/n\). Every fully pruned reference starts from the
**same** \(G^{(4)}/n\) as the full network. There is no comparison with an
evolved zero-readout network, no finite-jet transfer, and no population
continuation claim. The global theorem remains **OPEN**.

The proof first checks the active-data independence and deterministic
bounds directly at this initialization. It then checks the Gaussian
coefficient and off-block arguments, repairs the initial boundary in the
energy identity, and retains the prefix-time factors in the query and
state estimates. The all-set prefix bound below is an interface for
a fractional top-mass weighted-gate estimate; it does not close its distance
histories or carry out that separate application.

## 1. Setup, event, and scoped conclusions

Fix \(S>0\), \(M>0\), \(n\ge2\), and \(0<\eta<1\). All vector norms
are ordinary Euclidean norms; matrix norms are ordinary operator or
Frobenius norms. Every empirical normalization is displayed explicitly.
All transposes are finite matrix transposes \(T\).

Let \(\phi(z)=\arctan z\), \(c=\pi/2\), and
\(F(z)=z+z^3/3\). The canonical hidden initialization consists of the
first-layer vector with independent \(N(0,1)\) coordinates and independent matrices
\(W^{(2)}_0,W^{(3)}_0\), with independent \(N(0,1/n)\) entries. The
vector \(G^{(4)}\) has independent \(N(0,1)\) entries and is independent
of all hidden initialization. Set \(W^{(4)}_0=G^{(4)}/n\).

Fix one deterministic coordinatewise clipping \(\tau\) satisfying
\(|\tau(x)|\le |x|\) and \(|\tau(x)-\tau(y)|\le |x-y|\). In particular
\(\tau(0)=0\). The identity map is the uncut case. Both networks use
this same map. Constants are uniform in this prescribed map; the
probability event is not asserted simultaneously over all maps.

The full flow, in feature time, is
\[
\begin{gathered}
h^{(1)}=\phi(z^{(1)}),\quad z^{(2)}=W^{(2)}h^{(1)},\quad
h^{(2)}=\phi(z^{(2)}),\quad z^{(3)}=W^{(3)}h^{(2)},\quad
h^{(3)}=\phi(z^{(3)}),\\
D_\ell=\operatorname{diag}(\phi'(z^{(\ell)})),\qquad
\delta^{(3)}=D_3W^{(4)},\qquad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad \delta^{(2)}=D_2\tau(q^{(2)}),\\
(z^{(1)})'=D_1(W^{(2)})^T\delta^{(2)},\qquad
(W^{(2)})'=\frac{\delta^{(2)}(h^{(1)})^T}{n},\qquad
(W^{(3)})'=\frac{\delta^{(3)}(h^{(2)})^T}{n},\qquad
(W^{(4)})'=h^{(3)}.
\end{gathered}                                                    \tag{1}
\]
For each \(E\subseteq\{1,\ldots,n\}\), put \(P=P_E\), \(Q=I-P\),
and \(p=|E|/n\). Hats denote its single fully pruned reference: use
\(\widehat h^{(2)}=Q\phi(\widehat z^{(2)})\) and
\(\widehat\delta^{(2)}=Q\widehat D_2\tau(\widehat q^{(2)})\), with the
other definitions and updates in (1). Initialize all parameter blocks
and \(z^{(1)}\) identically. Deleted rows and columns remain stored at
their shared initial values; they are unused and frozen:
\[
P\widehat W^{(2)}=PW^{(2)}_0,\qquad
\widehat W^{(3)}P=W^{(3)}_0P.
                                                               \tag{2}
\]
Erasing the stored matrices themselves would change the distance at
time zero and is not the convention in the cited proofs.

Write \(x^{(1)}=F(z^{(1)})\), and define
\[
\begin{split}
d_E={}&\frac{\|x^{(1)}-\widehat x^{(1)}\|_2}{\sqrt n}
 +\|W^{(2)}-\widehat W^{(2)}\|_{\rm op}
 +\|W^{(3)}-\widehat W^{(3)}\|_{\rm op}
 +\frac{\|W^{(4)}-\widehat W^{(4)}\|_2}{\sqrt n},\\
y_E={}&\frac{\|x^{(1)}-\widehat x^{(1)}\|_2^2}{n}
 +\|W^{(2)}-\widehat W^{(2)}\|_{\rm F}^2
 +\|W^{(3)}-\widehat W^{(3)}\|_{\rm F}^2
 +\frac{\|W^{(4)}-\widehat W^{(4)}\|_2^2}{n}.
\end{split}                                                     \tag{3}
\]
Thus \(d_E\le2\sqrt{y_E}\) and \(d_E(0)=y_E(0)=0\).
For the empty deletion uniqueness gives identical paths, hence
\(d_\varnothing=y_\varnothing=0\) identically.

Define
\[
\begin{gathered}
h(p)=p\log(e/p),\quad h(0)=0,\qquad
\mu(d)=d\sqrt{1+\log_+(1/d)},\quad \mu(0)=0,\\
\Phi(y)=y[1+\tfrac12\log_+(1/y)],\quad \Phi(0)=0.
\end{gathered}
\]
Both \(\mu\) and \(\Phi\) are nondecreasing, and
\(\mu(d_E)^2\le4\Phi(y_E)\).

Take a deterministic grid containing \(0,S\), with gaps at most
\(1/n\) and \(N\le\lceil nS\rceil+1\). Put
\[
b_n=\frac{\log(512n^2N/\eta)}n,\qquad
\epsilon_n=\sqrt{b_n}+b_n+n^{-1/2}.
                                                               \tag{4}
\]
The increased numerical constant allocates the auxiliary events
explicitly below. Set
\[
\begin{split}
\Omega_M&=\{\|W^{(2)}_0\|_{\rm op}\le M,
                  \ \|W^{(3)}_0\|_{\rm op}\le M\},\\
\Omega_4&=\{\|G^{(4)}\|_2/\sqrt n\le2,
                  \ \max_i|G_i^{(4)}|/n\le1\}.
\end{split}
\]
There is an event \(\mathcal A_\eta\), with
\(\mathbb P(\mathcal A_\eta^c)\le\eta\), such that all conclusions
below hold on \(\mathcal A_\eta\cap\Omega_M\cap\Omega_4\),
simultaneously for every \(E\), every time \(s\in[0,S]\), and every
prefix \(t\in[0,S]\). Statements involving second derivatives hold
almost everywhere, which suffices for interpolation and integration.
Every constant denoted \(C\) depends only on \(S,M\).

Define
\[
\begin{gathered}
A_2=\frac{\|h^{(1)}\|_2^2}{n}I+W^{(2)}D_1^2(W^{(2)})^T,\qquad
\alpha_E=\frac{\|\widehat h^{(1)}\|_2^2+
                         \operatorname{Tr}(\widehat D_1^2)}n,\\
\widehat g_E=PW^{(2)}_0(\widehat h^{(1)})',\qquad
\rho_E=(PA_2P-\alpha_EP)\delta^{(2)}
                  +PA_2Q\delta^{(2)}-\widehat g_E,\\
I_E=\frac{\|Pq^{(2)}(0)\|_2^2}{n},\qquad
J_E(t)=t[h(p)+\epsilon_n^2+I_E]
                         +\int_0^t\mu(d_E(s))^2\,ds.
\end{gathered}                                                   \tag{5}
\]
Then \(1/4\le\alpha_E\le c^2+1\), and the direct derivative and
residual bounds are
\[
\begin{split}
\frac{\|P(\widehat q^{(2)})'(s)\|_2+\|\widehat g_E(s)\|_2}{\sqrt n}
 &\le C[\sqrt{h(p)}+\epsilon_n],\\
\frac{\|\rho_E(s)\|_2}{\sqrt n}
 &\le C[\sqrt{h(p)}+\epsilon_n+\mu(d_E(s))],\\
\frac{\|P(q^{(2)})'(s)\|_2}{\sqrt n}
 &\le C\left[\frac{\|P\delta^{(2)}(s)\|_2}{\sqrt n}
                    +\sqrt{h(p)}+\epsilon_n+\mu(d_E(s))\right].
\end{split}                                                     \tag{6}
\]
The retained rare self-feedback in the last line has not been
treated as an independent Gaussian query.

The energy and derivative energies satisfy
\[
\int_0^t\frac{\|P\delta^{(2)}\|_2^2+
                  \|P(q^{(2)})'\|_2^2+\|P(z^{(2)})'\|_2^2}{n}\,ds
                 \le C J_E(t).                                  \tag{7}
\]
In particular, for \(q^{(2)}_{*,i}(t)=\sup_{0\le s\le t}|q^{(2)}_i(s)|\),
\[
\begin{split}
\frac1n\sum_{i\in E}q^{(2)}_{*,i}(t)^2
&\le 2I_E+C\left\{t^2[h(p)+\epsilon_n^2+I_E]
                         +t\int_0^t\mu(d_E(s))^2\,ds\right\},\\
\frac1n\sum_{i\in E}\sup_{0\le s\le t}
                |z_i^{(2)}(s)-z_i^{(2)}(0)|^2
&\le C\left\{t^2[h(p)+\epsilon_n^2+I_E]
                         +t\int_0^t\mu(d_E(s))^2\,ds\right\}.
\end{split}                                                     \tag{8}
\]
The extra initialization contributions are therefore \(CtI_E\)
in (7) and \((2+Ct^2)I_E\) in the first line of (8), not just an
error multiplied by \(t^2\). Without any independence claim about
the actual query,
\[
q^{(2)}(0)=(W^{(3)}_0)^T
           [\phi'(z^{(3)}_0)\odot G^{(4)}/n],\qquad
\frac{\|q^{(2)}(0)\|_2}{\sqrt n}\le\frac{2M}{n},\qquad
I_E\le\frac{4M^2}{n^2}.                                        \tag{9}
\]
Moreover, on the same stated event, the sharper all-set bound is
\[
I_E\le\frac{8M^2}{n^2}
 \left[h(p)+\frac{\log(8n/\eta)}n\right]\quad(E\ne\varnothing).
                                                               \tag{9a}
\]
Its conditional Gaussian proof, which does not require independent
query coordinates and precedes imposition of \(\Omega_4\), is in
section 5. It removes the mass-independent initialization plateau.
For \(\eta=1/n\), \(\epsilon_n\to0\). The initialization error
also vanishes uniformly on \([0,S]\); it is not discarded at time
zero.

## 2. Direct deterministic bounds and independence

On \(\Omega_4\), the integral readout update gives, for both the full
and every reference network,
\[
\|W^{(4)}(s)\|_\infty\le1+cs,\qquad
\frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le\frac2n+cs.
                                                               \tag{10}
\]
Let \(R=1+cS\), \(K_3=M+cSR\), and \(K_2=M+cSK_3R\).
On the appropriate active operator event, (1) implies
\[
\begin{gathered}
\frac{\|\delta^{(3)}\|_2}{\sqrt n}\le R,\qquad
\|W^{(3)}\|_{\rm op}\le K_3,\qquad
\frac{\|\delta^{(2)}\|_2}{\sqrt n}\le K_3R,\qquad
\|W^{(2)}\|_{\rm op}\le K_2,\\
\frac{\|(x^{(1)})'\|_2}{\sqrt n}
 =\frac{\|(W^{(2)})^T\delta^{(2)}\|_2}{\sqrt n}\le K_2K_3R.
\end{gathered}                                                   \tag{11}
\]
For references, replace matrices in the active equations by
\(\widehat W^{(3)}Q\) and, when necessary,
\(Q\widehat W^{(2)}\). A full \(\widehat W^{(2)}\) bound is used
only when its full initial norm is part of the active event.
For example
\(\|(\widehat W^{(3)}Q)'\|_{\rm F}
 \le\|\widehat\delta^{(3)}\|_2\|\widehat h^{(2)}\|_2/n\le cR\).
These are also bounds on Frobenius norms of trained increments,
not on the initial matrices' Frobenius norms.

The finite-dimensional vector field is locally Lipschitz, including
for a Lipschitz clipping. Equations (10)--(11) and the corresponding
\(z^{(1)}\) velocity bound exclude finite-time escape. Thus these
finite-width trajectories exist on every fixed feature horizon.
This assertion supplies no width-uniform stability of their derivatives
with respect to initial conditions.

The exact differentiated identities are
\[
\begin{gathered}
(h^{(1)})'=D_1^2(W^{(2)})^T\delta^{(2)},\qquad
(z^{(2)})'=A_2\delta^{(2)},\qquad
(h^{(2)})'=D_2A_2\delta^{(2)},\\
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
                         +W^{(3)}(h^{(2)})',\\
(\delta^{(3)})'=D_3h^{(3)}+B(z^{(3)})',\qquad
B=\operatorname{diag}(W^{(4)}\odot\phi''(z^{(3)})).
\end{gathered}                                                   \tag{12}
\]
The pruned middle activation derivative has an additional left \(Q\).
Since \(|\phi'|\le1\), \(|\phi''|\le2\), (11)--(12) bound all
displayed velocities divided by \(\sqrt n\) by constants depending
only on \(S,M\). For instance, with \(A=c^2+K_2^2\), one may use
\[
\frac{\|(z^{(3)})'\|_2}{\sqrt n}
       \le c^2R+K_3^2AR=:J_3,\qquad
\frac{\|(\delta^{(3)})'\|_2}{\sqrt n}\le c+2RJ_3.
                                                               \tag{13}
\]
This replaces every use of a zero-based \(cS\) bound in the
Gaussian reference-query proof.

For a fixed \(E\), the active reference path is measurable with
respect to
\[
\mathcal F_E^{\rm in}
 =\sigma(z^{(1)}_0,QW^{(2)}_0,W^{(3)}_0Q,G^{(4)}).
                                                               \tag{14}
\]
It is independent of both \(PW^{(2)}_0\) and \(W^{(3)}_0P\).
This follows directly from the updates: the active lower flow uses
\((Q\widehat W^{(2)})^T\widehat\delta^{(2)}\), and the active top
flow uses \(\widehat W^{(3)}Q\); (2) never feeds either deleted
block back into that flow. The unused preactivation and transpose
queries themselves need not be measurable with respect to (14).

For coefficients allowed to use the full incoming matrix, use
\[
\mathcal F_E^{\rm top}
 =\sigma(z^{(1)}_0,W^{(2)}_0,W^{(3)}_0Q,G^{(4)}),
                                                               \tag{15}
\]
which remains independent of \(W^{(3)}_0P\). The selection events are
\[
\begin{split}
\Omega_E^{\rm in}&=\Omega_4\cap
 \{\|QW^{(2)}_0\|_{\rm op}\le M,\ \|W^{(3)}_0Q\|_{\rm op}\le M\},\\
\Omega_E^{\rm top}&=\Omega_4\cap
 \{\|W^{(2)}_0\|_{\rm op}\le M,\ \|W^{(3)}_0Q\|_{\rm op}\le M\}.
\end{split}                                                     \tag{16}
\]
Select the entire controlled path to be zero outside its applicable
event. Since \(\Omega_4\) depends only on independent \(G^{(4)}\),
both selections preserve the required independence. Full operator
norms are imposed only after conditional Gaussian estimates are
proved. No independence is asserted after conditioning on \(\Omega_M\).

For derivative grids the bounds needed in the cited derivative proof
are still
\[
\frac{\|(\widehat\delta^{(3)})'\|_2}{\sqrt n}\le C,\qquad
\frac{\|(\widehat\delta^{(3)})''\|_2+
                   \|(\widehat h^{(1)})''\|_2}{\sqrt n}\le C\sqrt n.
                                                               \tag{17}
\]
Here is a check that does not assume a full unused query bound on an
active event. Use
\(q_a=Q(\widehat W^{(3)})^T\widehat\delta^{(3)}\). Equations
(11)--(13) bound \(q_a,q_a'\) divided by \(\sqrt n\). The chain rule
for \(Q\widehat D_2\tau(q_a)\) then bounds its derivative divided by
\(\sqrt n\) by \(C\sqrt n\), using
\(\|q_a\|_\infty\le\|q_a\|_2\) and
\(|(\tau(q_{a,i}))'|\le|q_{a,i}'|\) almost everywhere. Only active
middle preactivation derivatives are needed on \(\Omega_E^{\rm in}\).
Differentiating the active mobility gives operator bound \(C\sqrt n\).
Thus \(\widehat z^{(3)\prime\prime}\) divided by \(\sqrt n\) has
bound \(C\sqrt n\). Explicitly,
\[
\begin{split}
\widehat\delta^{(3)\prime\prime}={}&
 [(\phi'(\widehat z^{(3)}))^2
       +2\widehat h^{(3)}\odot\phi''(\widehat z^{(3)})]
                                    \odot\widehat z^{(3)\prime}\\
 &+\widehat W^{(4)}\odot\phi'''(\widehat z^{(3)})
                                    \odot(\widehat z^{(3)\prime})^2
 +\widehat W^{(4)}\odot\phi''(\widehat z^{(3)})
                                    \odot\widehat z^{(3)\prime\prime}.
\end{split}
\]
Use \(|\phi'''|\le8\) and
\(\|v\odot v\|_2/\sqrt n\le\sqrt n(\|v\|_2/\sqrt n)^2\).
For the lower query differentiate \(\widehat x^{(1)\prime}\), then
\(\widehat h^{(1)}=\phi(F^{-1}(\widehat x^{(1)}))\); the latter
scalar function has first derivative at most one and second derivative
at most four in absolute value. This proves (17) on precisely the
events in (16). No second derivative of \(\tau\) is required.

## 3. Gaussian events and the direct derivative/off-block algebra

The elementary probability arguments in the four requested sources
apply to the selected paths just constructed. To make the event
quantifiers explicit, allocate failure at most \(\eta/8\) to each
of the following eight groups:

1. The four deleted-top Gaussian coefficient families in (18) below.
2. The pruned top derivative query.
3. The pruned incoming velocity query.
4. The off-block/residual proof, divided equally among its conditional
   off-block operator event, adaptive submatrix event, and lower Gram event.
5. The pruned top value query of PRUNED_GAUSSIAN_SUBSET_BOUND.md.
6. The incoming reference-path amplitude event of
   DIRECT_SCALAR_PRUNED_REDUCTION.md, section 4.
7. The optional signed top Gram event of PRUNED_RARE_BLOCK_GEOMETRY.md.
8. The sharp actual initial-query event of section 5, conditional on
   the hidden initialization, without conditioning on \(\Omega_4\).

For completeness, the Gaussian inequalities used have the following
forms. For a deleted Gaussian block \(G\) and an independent coefficient
matrix \(C\) with \(\|C\|_{\rm op}\le K\), two finite \(1/4\)-nets
give
\[
\mathbb P(\|GCP_F\|_{\rm op}>x\mid\text{active data})
 \le2\,9^{|E|+|F|}\exp[-nx^2/(8K^2)].
\]
For an independent vector \(v\) with \(\|v\|_2/\sqrt n\le K\),
the deleted query has independent Gaussian coordinates of variance
at most \(K^2\); its squared norm divided by \(n\) exceeds
\(4K^2(|E|+u)/n\) with probability at most \(e^{-u}\).
This follows from the moment generating function of a squared
standard Gaussian at parameter \(1/4\).
For an independent diagonal \(D\), \(|D_{jj}|\le K\), the centered
Gram bound is
\[
\mathbb P\!\left(\left\|GDG^T-\frac{\operatorname{Tr}D}{n}I_E\right\|_{\rm op}
 >16K[\sqrt{u/n}+u/n]\mid\text{active data}\right)
 \le2\,9^{|E|}e^{-u}.
\]
It follows by expanding the Gaussian-square exponential moment, then
using a quadratic-form net. These are the proved inequalities in the
read dependencies, with their independence hypotheses now verified by
(14)--(16).

There are at most \((en/m)^m\) sets of size \(m\). Union over all
sets, both sizes when applicable, the finite family labels, and all
grid times gives logarithmic costs bounded by the numerator in (4).
For example the residual group's cost is
\(\log(48n^2N/\eta)\); the four-family group's is at most
\(\log(64n^2N/\eta)\). On \(\Omega_M\cap\Omega_4\), selected
paths become genuine, deleted blocks have norm at most \(M\), and
(17) gives interpolation error \(C/\sqrt n\). The value-query
interpolation error is only \(C/n\). Thus one event controls all
sets and all times. Adaptive selection of a set afterward needs no
additional independence or union bound.

Here are the algebraic checks needed to obtain (6), beyond the
probability inequalities. Set \(G=P(W^{(3)}_0)^T\). The four
coefficient paths are exactly
\[
\begin{split}
C_0&=I,\qquad C_1=\widehat B\widehat W^{(3)}Q,\\
C_2&=\widehat B\widehat W^{(3)}Q\widehat D_2\widehat W^{(2)},\qquad
C_3=\widehat B\widehat W^{(3)}Q\widehat D_2\widehat A_2Q.
\end{split}                                                     \tag{18}
\]
They are measurable with respect to (15), including the full
\(\widehat W^{(2)}\) in \(C_2,C_3\); every top matrix factor has
a right \(Q\). On \(\Omega_E^{\rm top}\), their operator norms
are \(O(1)\), and their derivative operator norms are \(O(\sqrt n)\).
The sorted-coordinate-block argument therefore gives, for every
possibly adaptive \(v\) with
\(\|v\|_2/\sqrt n\le K\) and \(\|v\|_1/n\le\ell\le K\),
\[
\frac{\|GC_jv\|_2}{\sqrt n}
 \le C\{K[\sqrt{h(p)}+\epsilon_n]
                    +\ell\sqrt{\log(eK/\ell)}\}.               \tag{19}
\]
The final term is zero if \(\ell=0\). To check this deterministic
step, partition decreasing coordinates into blocks of size
\(k=\lceil n(\ell/K)^2\rceil\); the sum of their Euclidean norms
divided by \(\sqrt n\) is at most \(2K\). The submatrix bound gives
\(K\sqrt{h(k/n)}\), which is bounded by
\(C\ell\sqrt{\log(eK/\ell)}+CK\sqrt{h(1/n)}\).
The latter width term is included in (4). Cases \(K=0\) or
\(\ell=0\) give \(v=0\).

The incoming off-block coefficient is
\(\widehat D_1^2(\widehat W^{(2)})^TQ\). It is measurable with
respect to (14), so the same argument applies with \(G=PW^{(2)}_0\).
The adaptive Gaussian submatrix event also yields, for any signed
diagonal entries \(|a_j|\le1\),
\[
\|G\operatorname{diag}(a)G^T\|_{\rm op}
 \le C\left[h(p)+h\left(\frac1n\sum_j|a_j|\right)+b_n\right].
\]
Indeed dominate by the nonnegative diagonal \(|a|\), integrate the
submatrix bounds over its level sets, and use concavity of \(h\).
Apply this with \(a_j\) the square of the lower squared-gate
difference. Since
\(n^{-1}\sum_j|(D_1^2-\widehat D_1^2)_{jj}|^2
 \le\min\{1,16d_E^2\}\), it gives
\[
\|PW^{(2)}_0(D_1^2-\widehat D_1^2)\|_{\rm op}
            \le C[\sqrt{h(p)}+\mu(d_E)+\epsilon_n].             \tag{20}
\]
This is an adaptive-diagonal bound, not conditional independence of
the actual gate.

The primal comparisons used here are obtained directly by subtraction:
\[
\begin{gathered}
\frac{\|Q(z^{(2)}-\widehat z^{(2)})\|_2}{\sqrt n}\le Cd_E,
\qquad
\frac{\|h^{(2)}-\widehat h^{(2)}\|_2}{\sqrt n}\le Cd_E+c\sqrt p,\\
\frac{\|z^{(3)}-\widehat z^{(3)}\|_2+
          \|\delta^{(3)}-\widehat\delta^{(3)}\|_2+
          \|q^{(2)}-\widehat q^{(2)}\|_2}{\sqrt n}\le C(d_E+\sqrt p).
\end{gathered}                                                   \tag{21}
\]
For example the top backward difference costs
\(\|W^{(4)}-\widehat W^{(4)}\|_2/\sqrt n
 +2R\|z^{(3)}-\widehat z^{(3)}\|_2/\sqrt n\).
Thus the old factor \(2cS\) is replaced by \(2R\), with no new
additive state error. This check also applies to \(B-\widehat B\).

To verify the residual, put
\(\mathcal N=PW^{(2)}D_1^2(W^{(2)})^TQ\) and
\(\mathcal M=PW^{(2)}_0\widehat D_1^2(\widehat W^{(2)})^TQ\).
Expand their difference using (2): the two matrix-difference terms
cost \(Cd_E\), and the intervening gate term is controlled by (20).
Also
\[
\begin{split}
Q(\delta^{(2)}-\widehat\delta^{(2)})
 &=QD_2[\tau(q^{(2)})-\tau(\widehat q^{(2)})]+v_E,\\
v_E&=Q(D_2-\widehat D_2)\tau(\widehat q^{(2)}),\qquad
\frac{\|v_E\|_2}{\sqrt n}\le C,\quad
\frac{\|v_E\|_1}{n}\le Cd_E.
\end{split}                                                     \tag{22}
\]
The off-block residual is exactly
\[
PA_2Q\delta^{(2)}-\widehat g_E
 = (\mathcal N-\mathcal M)Q\delta^{(2)}
    +\mathcal M QD_2[\tau(q^{(2)})-\tau(\widehat q^{(2)})]+\mathcal M v_E.
                                                               \tag{23}
\]
Use (19) for its last term and (21) for its second term.
The identical matrix expansion with right projection \(P\), followed
by the independent lower Gram estimate with diagonal
\(\widehat D_1^2\), proves
\(\|PA_2P-\alpha_EP\|_{\rm op}
 \le C[\sqrt{h(p)}+\mu(d_E)+\epsilon_n]\).
The scalar coercivity is the pointwise inequality
\(\phi(z)^2+\phi'(z)^2\ge1/4\): use \(|z|\le1\) and
\(|z|>1\) separately. This proves the residual line of (6).

Finally differentiate the actual query exactly:
\[
(q^{(2)})'=h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
                           +(W^{(3)})^T\delta^{(3)\prime}.
                                                               \tag{24}
\]
The learned rare top columns satisfy
\[
\|(W^{(3)}(s)-W^{(3)}_0)P\|_{\rm F}
 \le\int_0^s\frac{\|\delta^{(3)}\|_2\|Ph^{(2)}\|_2}{n}\,du
 \le cRS\sqrt p.
\]
Hence \(P(q^{(2)})'=G\delta^{(3)\prime}+r\), with
\(\|r\|_2/\sqrt n\le C\sqrt p\). Also
\(P(\widehat q^{(2)})'=G\widehat\delta^{(3)\prime}\), giving the first
query in (6); (14) and (17) give the incoming velocity query.

To check the remaining actual term, let \(U=(h^{(2)})'\) and
\(\widehat U=(\widehat h^{(2)})'\). Subtract (12) in the order
\[
\delta^{(3)\prime}-\widehat\delta^{(3)\prime}
 =r_{\rm sm}+(B-\widehat B)z^{(3)\prime}
       +\widehat B\widehat W^{(3)}PU
       +\widehat B\widehat W^{(3)}Q(U-\widehat U),               \tag{25}
\]
where
\[
\begin{split}
r_{\rm sm}={}&D_3h^{(3)}-\widehat D_3\widehat h^{(3)}
 +\widehat B\left[
   \frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
    -\frac{\|\widehat h^{(2)}\|_2^2}{n}\widehat\delta^{(3)}\right]
 +\widehat B(W^{(3)}-\widehat W^{(3)})U.
\end{split}
\]
This has Euclidean norm divided by \(\sqrt n\) at most
\(C(d_E+\sqrt p)\). The next vector in (25) has bounded Euclidean
norm divided by \(\sqrt n\) and \(\ell^1\) norm divided by \(n\)
at most \(C(d_E+\sqrt p)\), by Cauchy--Schwarz and (21).

The rare self-return contains
\(\widehat W^{(3)}P=W^{(3)}_0P=G^T\); it is not independent of
\(G\). Bound it by deterministic operators and use the exact identity
\[
P(z^{(2)})'=\alpha_EP\delta^{(2)}+\widehat g_E+\rho_E
\]
to bound \(\|PU\|_2/\sqrt n\) by
\(C\|P\delta^{(2)}\|_2/\sqrt n+
 (\|\widehat g_E\|_2+\|\rho_E\|_2)/\sqrt n\).

Expand the last term of (25) as
\[
Q(U-\widehat U)
 =Q(D_2-\widehat D_2)A_2\delta^{(2)}
  +Q\widehat D_2(A_2-\widehat A_2)\delta^{(2)}
  +Q\widehat D_2\widehat A_2(\delta^{(2)}-\widehat\delta^{(2)}).
\]
After expanding the mobility difference, its only extra gate vector
is \((D_1^2-\widehat D_1^2)(W^{(2)})^T\delta^{(2)}\). The three
exceptional input vectors are therefore this vector,
\(Q(D_2-\widehat D_2)A_2\delta^{(2)}\), and \(v_E\).
Each has bounded Euclidean norm divided by \(\sqrt n\) and
\(\ell^1\) norm divided by \(n\) at most \(Cd_E\). Their outer
coefficients are precisely \(GC_2,GC_1,GC_3\). All other terms
cost \(C(d_E+\sqrt p)\) or \(C\|P\delta^{(2)}\|_2/\sqrt n\).
Apply (19), using
\(\mu(d+\sqrt p)\le C[\mu(d)+\sqrt{h(p)}]\), to prove the last
line of (6). No step in (18)--(25) assumes a zero initial readout.

## 4. The nonzero initial boundary and exact prefix factors

Fix \(E\), and write \(q_E=Pq^{(2)}\), \(u_E=P\tau(q^{(2)})\),
\(h_E=P\phi(z^{(2)})\), \(\delta_E=P\delta^{(2)}\), and
\(r_E=\widehat g_E+\rho_E\). These symbols in this section all
refer to the actual rare coordinates, except for the explicitly
pruned term in \(r_E\). They obey
\[
\delta_E=D_2u_E,\quad
h_E'=PD_2(\alpha_E\delta_E+r_E),\quad
\frac{u_E^Th_E'}n
 =\alpha_E\frac{\|\delta_E\|_2^2}{n}
                              +\frac{\delta_E^Tr_E}{n}.         \tag{26}
\]
Here \(\|h_E\|_2/\sqrt n\le c\sqrt p\),
\(\|u_E'\|_2\le\|q_E'\|_2\) almost everywhere, and
\(\|u_E(0)\|_2^2/n\le I_E\). In general \(u_E(0)\ne0\).

Integration by parts gives
\[
\int_0^t\alpha_E\frac{\|\delta_E\|_2^2}{n}\,ds
 =\frac{u_E(t)^Th_E(t)-u_E(0)^Th_E(0)}n
  -\int_0^t\frac{(u_E')^Th_E+\delta_E^Tr_E}{n}\,ds.             \tag{27}
\]
Use the exact boundary decomposition
\[
u_E(t)^Th_E(t)-u_E(0)^Th_E(0)
 =(u_E(t)-u_E(0))^Th_E(t)
                    +u_E(0)^T(h_E(t)-h_E(0)).                  \tag{28}
\]
The first term of (28), together with the \(u_E'\) integral in
(27), has absolute value divided by \(n\) at most
\(2c\sqrt p\int_0^t\|q_E'\|_2/\sqrt n\,ds\).
The new term is exactly
\[
\frac{u_E(0)^T(h_E(t)-h_E(0))}{n}
 =\int_0^t\frac{u_E(0)^TD_2(s)
                       [\alpha_E(s)\delta_E(s)+r_E(s)]}{n}\,ds.
                                                               \tag{29}
\]
This identity preserves its time integral, rather than estimating
two separate endpoints by a time-independent error.

Put \(A(s)=\|\delta_E(s)\|_2/\sqrt n\) and
\(w(s)=\sqrt{h(p)}+\epsilon_n+\mu(d_E(s))\).
Equations (6), (27)--(29) give
\[
\frac14\int_0^t A^2\,ds
 \le C\int_0^t[
       \sqrt p\,A+\sqrt p\,w+Aw+\sqrt{I_E}A+\sqrt{I_E}w]\,ds.
\]
Apply \(xy\le\varepsilon x^2+y^2/(4\varepsilon)\) to the three
terms containing \(A\), choosing their total absorption below
\(\frac18\int A^2\). Bound the remaining terms by constants
times \(p+w^2+I_E\). Since \(p\le h(p)\), this proves
\[
\int_0^t\frac{\|P\delta^{(2)}\|_2^2}{n}\,ds
 \le C\left\{t[h(p)+\epsilon_n^2+I_E]
                         +\int_0^t\mu(d_E(s))^2\,ds\right\}.
                                                               \tag{30}
\]
Squaring (6) and the exact scalar identity in (26) proves (7).

For each absolutely continuous scalar path,
\(\sup_{s\le t}|v(s)-v(0)|^2\le t\int_0^t|v'|^2\).
Thus (8) follows coordinatewise from (7) and
\(|q^{(2)}_i(s)|^2\le2|q^{(2)}_i(0)|^2+2|q^{(2)}_i(s)-q^{(2)}_i(0)|^2\).
A version retaining the unsplit boundary is
\[
\left(\frac1n\sum_{i\in E}q^{(2)}_{*,i}(t)^2\right)^{1/2}
       \le\sqrt{I_E}+\sqrt{CtJ_E(t)}.                           \tag{31}
\]
At \(t=0\), its right side equals the left side. Formula (8) is
the convenient additive bound used below. The two prefix powers are
\(t^2\) on the entropy/width term and \(t\) before the distance
history. They have not been absorbed into constants depending on \(S\).

For a pruned whole query path the same argument from its derivative
line in (6) gives
\[
\frac1n\sum_{i\in E}\sup_{s\le t}|\widehat q^{(2)}_i(s)|^2
 \le2\widehat I_E+Ct^2[h(p)+\epsilon_n^2],\qquad
\widehat I_E=\frac{\|P\widehat q^{(2)}(0)\|_2^2}{n}\le\frac{4M^2}{n^2}.
\]
One must not identify \(\widehat q^{(2)}(0)\) with \(q^{(2)}(0)\): their top
preactivations differ because of pruning.

## 5. Sharp initial top mass and the all-set prefix interface

Let \(\mathcal H\) be the sigma field of all hidden initialization.
The vector \(z^{(3)}_0\), including its dependence on the full hidden
matrices, is \(\mathcal H\)-measurable. Conditional on \(\mathcal H\),
the actual initial query is a centered Gaussian vector with covariance
\[
\Sigma_0=\frac1{n^2}(W^{(3)}_0)^T
     \operatorname{diag}(\phi'(z^{(3)}_0)^2)W^{(3)}_0
              \preceq\frac{M^2}{n^2}I\quad\hbox{on }\Omega_M.
                                                               \tag{32}
\]
This covariance domination does not assert independence of the query's
coordinates. It uses only \(|\phi'|\le1\) and the hidden operator
bound. Dependence of the gate on \(W^{(3)}_0\) is harmless because
both are fixed under this conditioning.

For an unconditional event construction, define
\(\widetilde q^{(2)}_0=\mathbf1_{\Omega_M}q^{(2)}(0)\). Its conditional law is
either the Gaussian in (32), or the zero vector. This selection is
\(\mathcal H\)-measurable, independent of \(G^{(4)}\).
For a fixed deterministic nonempty set \(E\) of size \(m\),
diagonalize its conditional covariance. Its eigenvalues
\(\lambda_j\) lie in \([0,M^2/n^2]\). Therefore
\[
\begin{split}
\mathbb E\!\left[
 \exp\left(\frac{n^2\|P\widetilde q^{(2)}_0\|_2^2}{4M^2}\right)
                                  \middle|\mathcal H\right]
 &=\prod_{j=1}^m
     \left(1-\frac{n^2\lambda_j}{2M^2}\right)^{-1/2}
 \le 2^{m/2},\\
\mathbb P\!\left(
 \frac{\|P\widetilde q^{(2)}_0\|_2^2}{n}
     >\frac{4M^2}{n^2}\frac{m+u}{n}
                                  \middle|\mathcal H\right)
 &\le e^{-(m+u)}2^{m/2}\le e^{-u},\qquad u\ge0.
\end{split}                                                     \tag{33}
\]
Degenerate eigenvalues cause no problem. Choose
\(u_m=m\log(en/m)+\log(8n/\eta)\). A union bound over at most
\((en/m)^m\) subsets of size \(m\), then over \(1\le m\le n\),
has total failure at most \(\eta/8\). Its success event is group 8
in section 3. On this event intersected with \(\Omega_M\),
simultaneously for all nonempty \(E\),
\[
\begin{split}
I_E&\le\frac{4M^2}{n^2}
       \left[p+h(p)+\frac{\log(8n/\eta)}n\right]\\
   &\le\frac{8M^2}{n^2}
       \left[h(p)+\frac{\log(8n/\eta)}n\right]
    \le\frac{8M^2}{n^2}[h(p)+\epsilon_n^2].
\end{split}                                                     \tag{34}
\]
For the empty set \(I_\varnothing=0\) exactly. The inequality
\(\epsilon_n^2\ge b_n\ge\log(8n/\eta)/n\) explains the last
step. This proof never conditions on \(\Omega_4\): imposing that
event first would truncate the conditional Gaussian law. Instead
\(\Omega_4\) is intersected afterward, as in (41). The event in
(34) is simultaneous before any set is selected from the full path
or \(G^{(4)}\); such postselection is therefore valid.

Define the integer-subset envelopes, for \(0\le r\le1\), by
\[
Y_r(s)=\max_{|E|\le\lfloor nr\rfloor}y_E(s),\qquad
M_r(t)=\max_{|E|\le\lfloor nr\rfloor}
                     \frac1n\sum_{i\in E}q^{(2)}_{*,i}(t)^2.
\]
Both are exactly zero if \(r<1/n\). For every \(r\ge1/n\),
(8), (34), \(\mu(d_E)^2\le4\Phi(y_E)\), and monotonicity give
\[
M_r(t)\le C\left\{
 (t^2+n^{-2})[h(r)+\epsilon_n^2]
                  +t\int_0^t\Phi(Y_r(s))\,ds\right\},
       \qquad 0\le t\le S.                                    \tag{35}
\]
The passage to the maximum inside the nonnegative integral only
enlarges the bound. The term \(t^2n^{-2}[h(r)+\epsilon_n^2]\)
coming from the energy's initial contribution is bounded by
\(t^2[h(r)+\epsilon_n^2]\); this changes no displayed prefix power.

More precisely, the leftover initialization term before this
simplification is
\[
\mathcal R^{\rm query}_{E}(t)=(2+Ct^2)I_E
 \le\frac{8M^2(2+Ct^2)}{n^2}
       \left[h(p)+\frac{\log(8n/\eta)}n\right]
                  \quad(E\ne\varnothing).                     \tag{36}
\]
The corresponding energy term is \(CtI_E\). These formulas specify
both contributions without absorbing a nonzero initial value into a
\(t^2\) error. At time zero, the exact initial query energy is
\(I_E\), and (31) remains exact at that boundary; the factor two in
(36) comes only from the additive square inequality.

Equation (35) is the prefix input for fractional top-mass
interpolation. It holds on the same event for every real \(r\) and
every prefix time, since the underlying subset assertions are
simultaneous. It does not declare fractional mass below \(1/n\)
zero: only the integer-subset envelopes vanish there. The fractional
interpolation and the final weighted-gate history estimate are outside
the scope of this lemma.

## 6. Full/pruned state estimate, including its initialization

On the deterministic bounds above, \(y_E\le C\) uniformly. For
matrix terms use the Frobenius bounds on trained increments in (11)
and their shared initial matrices. For \(x^{(1)}\) use its bounded
velocity and its shared initial value. Initial Gaussian Frobenius
norms and initial \(x^{(1)}\) moments are unnecessary for this claim.

Let \(v_E\) be (22). The direct pair-velocity estimate is
\[
\left(\frac{\|\Delta x^{(1)\prime}\|_2^2}{n}
       +\|\Delta W^{(2)\prime}\|_{\rm F}^2
       +\|\Delta W^{(3)\prime}\|_{\rm F}^2
       +\frac{\|\Delta W^{(4)\prime}\|_2^2}{n}\right)^{1/2}
 \le C\left[\sqrt{y_E}+\sqrt p
          +\frac{\|P\delta^{(2)}\|_2+\|v_E\|_2}{\sqrt n}\right].
                                                               \tag{37}
\]
To verify the lower terms, subtract
\(x^{(1)\prime}=(W^{(2)})^T\delta^{(2)}\) and the rank update
in (1), and substitute
\[
\delta^{(2)}-\widehat\delta^{(2)}
 =P\delta^{(2)}+QD_2[\tau(q^{(2)})-\tau(\widehat q^{(2)})]+v_E.
\]
Use (21) and
\(\|uv^T/n\|_{\rm F}=\|u\|_2\|v\|_2/n\).
For the top rank update subtract its two factors and use (21);
for the readout velocity use
\(\|h^{(3)}-\widehat h^{(3)}\|_2
 \le\|z^{(3)}-\widehat z^{(3)}\|_2\).
The only initial-readout change to these arguments is the bounded
coefficient \(R\) in (21). There is no additive readout mismatch.

The shared initial state implies \(y_E(0)=0\) exactly, although
\[
z^{(3)}_0-\widehat z^{(3)}_0=W^{(3)}_0P\phi(z^{(2)}_0)
\]
need not vanish. This derived-feature discrepancy is the \(\sqrt p\)
term in (21) and (37), not a nonzero initial parameter distance.

Differentiate the squared norm (3), apply Young's inequality to
\(\sqrt{y_E}\sqrt p\) and
\(\sqrt{y_E}\|P\delta^{(2)}\|_2/\sqrt n\), retain the gate
product, and apply (30). It follows that
\[
y_E(t)\le C\left\{
 t[h(p)+\epsilon_n^2+I_E]
 +\int_0^t\Phi(y_E(s))\,ds
 +\int_0^t\sqrt{y_E(s)}\frac{\|v_E(s)\|_2}{\sqrt n}\,ds
                       \right\}.                              \tag{38}
\]
Thus the state estimate itself acquires \(CtI_E\), with zero
initial distance. This is a relative comparison inequality, not a
proved small bound on \(y_E\).

To record exactly how the prefix initialization term enters a weighted
gate, set
\[
\omega_{E,i}(s)=\mathbf1_{\{i\notin E\}}
 |\phi'(z_i^{(2)}(s))-\phi'(\widehat z_i^{(2)}(s))|^2,\qquad
a_E(s)=\frac1n\sum_i\omega_{E,i}(s).
\]
Then \(0\le\omega_{E,i}\le1\),
\(a_E(s)\le\min\{1,Cy_E(s)\}\), and clipping contractivity gives
\[
\frac{\|v_E(s)\|_2^2}{n}
 \le\frac2n\sum_i\omega_{E,i}(s)q^{(2)}_{*,i}(s)^2+C[y_E(s)+p].
                                                               \tag{39}
\]
Indeed add and subtract \(\tau(q^{(2)}_i)\) in (22), then use
\(|\tau(q^{(2)}_i)|\le|q^{(2)}_i|\) and \(|\tau(q^{(2)}_i)-\tau(\widehat q^{(2)}_i)|
 \le|q^{(2)}_i-\widehat q^{(2)}_i|\). Equations (35)--(39) are therefore valid
inputs to a subsequent fractional weighted-gate estimate. The state
source \(CtI_E\) in (38) is now at most
\(Ct n^{-2}[h(p)+\epsilon_n^2]\) and can be included in the same
\(Ct[h(p)+\epsilon_n^2]\) term, with no mass-independent
initialization plateau.

A brief deterministic check of the proposed entropy absorption is
also valid. Put \(A(y)=\min\{1,C_0y\}\), where \(C_0\ge1\) is a
fixed gate-mass comparison constant. For bounded \(y\ge0\),
\[
\frac1n\sqrt{y\,h(A(y))}\le C\Phi(y).                         \tag{40}
\]
When \(0<y\le1/C_0\),
\(h(C_0y)\le C_0y\log(e/y)\), so the left side is bounded by
\(\sqrt{C_0}y\sqrt{\log(e/y)}\le C\Phi(y)\).
When \(y\ge1/C_0\), use \(h(A(y))=1\),
\(\sqrt y\le\sqrt{C_0}y\), and \(\Phi(y)\ge y\).
At \(y=0\) both sides are zero. Thus the new entropy contribution
has the asserted modulus after multiplication by \(\sqrt y\).
This checks that factor only; it does not estimate the remaining
distance histories or perform the subsequent fractional interpolation.

## 7. Dependency audit and probability cost

The four requested dependencies were read in full. The additional
proof dependencies read in full were DIRECT_SCALAR_PRUNED_REDUCTION.md,
ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md, PRUNED_RARE_BLOCK_GEOMETRY.md,
and ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md. Only their finite primal,
scalar, Gaussian, prefix, and pair-comparison arguments are used.
No master status or finite-jet transfer is used as evidence.

| Source and use | Required change and check |
| --- | --- |
| PRUNED_GAUSSIAN_SUBSET_BOUND.md: active independence, primal bounds, value-query grid | Add \(G^{(4)}\) to active data and \(\Omega_4\) to the selection event. Replace \(cS\) readout/backward bounds by \(R\), and the ensuing matrix and Lipschitz constants by (11)--(13). Conditional Gaussian variances and union counts are unchanged. Clipping still enters only through its norm bound. |
| PRUNED_RARE_BLOCK_GEOMETRY.md: lower Gram and scalar center | The lower diagonal remains bounded by one and independent of deleted incoming rows; its derivative bound follows from (11). Coercivity is pointwise and needs no initialization assumption. The optional top signed diagonal bound changes from \(2cS\) to \(2R\), and its derivative bound from \(2c+8cS J_3\) to \(2c+8R J_3\). Its scalar center may have either sign. |
| ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md: all-diagonal event | It is an event for the initial Gaussian matrix alone. Its adaptive diagonal and gate-replacement applications impose no readout hypothesis. Use the new deterministic trained-operator constants. |
| SINGLE_PRUNED_OFFBLOCK_OSGOOD.md: sections 1--5 through the residual | Use (14)--(16); replace readout factor \(2cS\) in its top comparison by \(2R\). Frozen-row identities, sorted-block bounds, adaptive squared-gate comparison, and exact residual decomposition are (19)--(23). No initial boundary occurs. |
| DIRECT_SCALAR_PRUNED_REDUCTION.md: scalar decomposition and rank-memory boundaries | The rare displacement \(e=Pz^{(2)}-PW^{(2)}_0\widehat h^{(1)}\) still has \(e(0)=0\); it is not the backward query. Its scalar identity and both rank-memory integrations by parts retain zero initial boundaries for this reason. \(\alpha_E,1/\alpha_E\), and their first derivatives are bounded by (11)--(12). Its reference amplitude path is selected on \(\Omega_E^{\rm in}\). In finite width all its averages are empirical, and every rank product is \(uv^T/n\). |
| ACTUAL_RARE_BACKWARD_DERIVATIVE.md: all sections | The coefficient sigma fields acquire \(G^{(4)}\); (17) verifies the needed derivative grids with no second derivative of clipping. The four Gaussian coefficients retain every required right \(Q\). The self-return is bounded deterministically. Learned-column increments start at the same hidden matrix, so their zero increment at time zero never required a zero readout. Equations (24)--(25) check the actual top and bulk telescoping. |
| RARE_BACKWARD_ENERGY.md: initial boundary and whole-path corollary | Its assertions \(u_E(0)=q_E(0)=0\) are false here. Replace the boundary by (28)--(29). This gives \(CtI_E\) in energy, and (8), (31) retain the whole initial query mass. The unchanged zero-boundary proof would not establish this extension. |
| ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md: sections 1, 2, and pair estimate in section 4 | Replace its zero-based prefix query by (8) or the sharper (35), and its state inequality by (38). The original shared-state initial zero remains valid. Gate replacement (39) is unchanged, but the query initialization remainder (36) must be included. The new entropy factor passes the direct check (40). No assertion that its history hierarchy closes is imported. |

For clarity concerning the accumulated consequences in the off-block
note, the scalar amplitude proof depends on \(e(0)=0\), bounded
\(\int_0^S\alpha_E\|P\tau(q^{(2)})\|_2/\sqrt n\), and its independent
incoming reference amplitude. All hold by (11), (16), and event
group 6. Its rank-memory formulas depend on the same \(e(0)=0\),
not on \(q^{(2)}(0)=0\). Consequently the relative accumulated estimate
there (its equation (28)) also follows with the same functional form
\(C[p^{1/3}+\sqrt{h(p)}+\widetilde\nu_n+
\int_0^S\mu(d_E(s))\,ds]\), with updated constants and event
allocation. This assertion does not supply an uncompressed bulk
comparison or a new bound on the distance.

The readout event has the elementary failure bound
\[
\mathbb P(\Omega_4^c)
 \le e^{-(1-\frac12\log2)n}+2n e^{-n^2/2}.
\]
For its first term use
\(\mathbb E e^{\|G^{(4)}\|_2^2/4}=2^{n/2}\) and threshold \(4n\);
for its second term use the Gaussian coordinate tail and union bound.
The full operator-event failure stays separate. Thus the stated common
event has probability at least
\[
1-\eta-\mathbb P(\Omega_M^c)
       -e^{-(1-\frac12\log2)n}-2n e^{-n^2/2}.
                                                               \tag{41}
\]
For example, the spherical-net calculation in the read dependencies
gives, at \(M=10\),
\(\mathbb P(\Omega_M^c)\le4e^{-(25/2-2\log9)n}\).
Independence between good events is unnecessary. Adding the independent
readout to active data is what permits the Gaussian estimates; it is
not a reason to condition on the full initial operator event first.

All bounds proved here compare the actual prescribed tiny-readout flow
with its fully pruned flows at that same initialization. They repair
the positive-time premise for these scoped estimates. They leave the
unclosed distance histories, the full global limit theorem, and global
population existence/uniqueness **OPEN**.
