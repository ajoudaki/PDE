# Causal filtered initial-matrix queries: a complete auxiliary proof candidate

## Scope and conclusion

This is a proof for the explicitly defined auxiliary recursion below. It
establishes small effective ranks for that recursion's **own perturbed
histories**, and vanishing errors in its raw initial-matrix query outputs.
It is not a convergence theorem for the canonical L3 arctan network, and
does not identify this recursion with uncut exact GD or gradient flow.
In particular, the rank question for the original unfiltered histories
remains open.

The dependencies read in full and used here are:

- `INTEGRATED_INITIAL_QUERY_COMPRESSION.md`: the integrated representation,
  its four initial-matrix arguments, and its unresolved stability and
  derivative-observable terms;
- `PANAHI_ADAPTIVE_GRAM_MARTINGALE.md`: the proved adaptive estimate, with
  its exact triangular perturbations, causal filtration, and localization;
- `PANAHI_EULER_PERTURBATION_SIZE.md`: the exact triangular formulas and
  deterministic slow-history approximation argument. Its frozen-history
  Gaussian isometries are not applied to adaptive histories.

All probability estimates below use the proved adaptive theorem or
elementary Gaussian calculations derived here. No other probabilistic
theorem is adopted. No experiments or subagents are used.

Fix a feature-time horizon \(S>0\), and, for integers \(n\ge2\), put
\[
 \eta=n^{-2},\qquad N=\lceil Sn^2\rceil,\qquad
 T=N\eta\le S+1,\qquad K=N+1,
 \qquad \sigma=n^{-1/4},\qquad \gamma=1/8,\qquad \epsilon=n^{-\gamma},
 \qquad \ell_n=\log(e+n).
 \tag{1}
\]
Here \(N\) counts updates and \(K\) counts query pairs **per matrix**, including
one warmup. \(T\) is a feature-time horizon, not an established physical-time
horizon. Fix one deterministic scalar map \(\tau:\mathbb R\to\mathbb R\)
satisfying
\[
 |\tau(u)|\le |u|,\qquad |\tau(u)-\tau(v)|\le |u-v|.
 \tag{2}
\]
Apply it coordinatewise. Identity and any fixed clipping map satisfying
(2) are allowed. The constants below depend only on \(S\), not on the
clipping level or on which such map was fixed. The probability assertion
is for each fixed map; it does not assert a single event valid
simultaneously for all maps. A deterministic choice of map at each width
also satisfies the same estimates.

All vector norms below are ordinary Euclidean norms, with each factor
\(1/\sqrt n\) displayed explicitly. For a history
matrix \(X\in\mathbb R^{n\times k}\), define
\[
 \rho(X)=\operatorname{tr}\!\left[
 XX^T(XX^T+\sigma^2I_n)^{-1}\right].
 \tag{3}
\]
This equals the effective-rank expression using \(X^TX\), including when
\(k>n\). The four histories will be the lower and upper reverse arguments
divided by \(\sqrt n\), and the lower and upper forward arguments divided
by \(\sqrt n\), including their warmups.

**Auxiliary theorem.** The recursion in Sections 1--2 is finite and
measurable almost surely for every finite \(n,N\). There are deterministic
constants \(C_S<\infty\) and events \(\mathcal E_n^\tau\) such that
\[
 \mathbb P(\mathcal E_n^\tau)
 \ge 1-4e^{-(8-2\log9)n}-2n e^{-n^2/2}-5n^{-2},
 \tag{4}
\]
and, on these events, every prefix of every one of the four actual
histories satisfies
\[
 \rho\le C_S n^{11/12}\ell_n^{4/3}.
 \tag{5}
\]
For both matrices and both orientations, including warmups, let \(e_l\)
be the raw perturbed output minus the exact initial-matrix action on
that same actual query argument. Then, on the same event,
\[
 \max_l \frac{\|e_l\|_2}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{8/3}+C_S n^{-1/4}.
 \tag{6}
\]
Both terms tend to zero. This comparison is on the auxiliary algorithm's
own arguments, not on arguments imported from an unperturbed trajectory.

The proof first uses the universal ceiling \(\rho\le n\) in the adaptive
theorem. This gives logarithmic state bounds without assuming slow
histories. Relaxation then bounds increments of the actual histories.
A deterministic column approximation proves (5), after which a second,
localized application of the adaptive theorem proves (6). Neither pass
conditions on the realized histories as if their Gaussian law were
unchanged.

## 1. Exact oracle, canonical seeds, and causal warmup

Let \(\phi(z)=\arctan z\), \(F(z)=z+z^3/3\), and
\(\psi=\phi\circ F^{-1}\). These act coordinatewise. \(F\) is a
bijection of \(\mathbb R\), since \(F'(z)=1+z^2\ge1\) and its limits
at the two ends of the line are infinite with opposite signs. In particular,
\[
 |\phi|\le c_\phi:=\pi/2,\quad 0<\phi'\le1,\quad
 \|\phi''\|_\infty\le2,\quad
 \psi'(x)=\frac{1}{(1+(F^{-1}x)^2)^2}\le1.
 \tag{7}
\]

Sample the independent canonical initial blocks
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\quad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).
 \tag{8}
\]
Set \(x^{(1)}_0=F(z^{(1)}_0)\) and \(h^{(1)}_0=\phi(z^{(1)}_0)\).
The notation \(W^{(4)}_0\) will also denote the initial readout register.
For each \(b\in\{2,3\}\), set \(G^{(b)}=\sqrt n W^{(b)}_0\) and
sample independent arrays
\[
 \Gamma^{(b)}\in\mathbb R^{K\times K},\qquad
 U^{(b)}_l,V^{(b)}_l\in\mathbb R^n\quad(1\le l\le K),
 \tag{9}
\]
all with independent standard Gaussian entries. These two collections
are mutually independent and independent of (8).

Here is the exact paired oracle for either matrix; suppress \(b\)
temporarily. At call \(l\), the raw reverse argument is \(v_l\in\mathbb R^n\)
and the raw forward argument is \(h_l\in\mathbb R^n\). Its source variables
are
\[
 \theta_l=v_l/\sqrt n,\qquad\omega_l=h_l,\qquad
 p_l^{\rm src}=G^T\theta_l=W_0^Tv_l,\qquad
 q_l^{\rm src}=G\omega_l/n=W_0h_l/\sqrt n.
 \tag{10}
\]
For each leading history \(\Theta_l=[\theta_1,\ldots,\theta_l]\),
\(\Omega_l=[\omega_1,\ldots,\omega_l]\), take the positive-diagonal
upper Cholesky factors
\[
 A_{\theta,l}^TA_{\theta,l}=\Theta_l^T\Theta_l+\sigma^2I_l,
 \qquad
 A_{\omega,l}^TA_{\omega,l}=\Omega_l^T\Omega_l/n+\sigma^2I_l.
 \tag{11}
\]
Their leading blocks, including inverse leading blocks, agree as calls
are appended. Define the permanent columns
\[
 t_i=(\Theta_l A_{\theta,l}^{-1})_i,\qquad
 s_i=(\Omega_l A_{\omega,l}^{-1})_i/\sqrt n\quad(i\le l).
 \tag{12}
\]
The exact Gamma perturbations from the dependencies are
\[
 \begin{split}
 g_l&=\frac1{\sqrt n}\sum_{i\le l}
 t_i(\Gamma_{[l]\times[l]}A_{\omega,l})_{il},\\
 k_l&=\frac1{\sqrt n}\sum_{i<l}
 s_i(\Gamma_{[l]\times[l]}^T A_{\theta,l})_{il}.
 \end{split}
 \tag{13}
\]
In particular, the reverse sum is strict. Define the raw outputs, which
are the quantities actually used by the recursion, by
\[
 \begin{split}
 \mathcal R_l&=W_0^Tv_l+\sqrt n\,k_l+\sigma U_l,\\
 \mathcal F_l&=W_0h_l+\sqrt n\,g_l+\sigma V_l.
 \end{split}
 \tag{14}
\]
Thus the perturbed source reverse output is \(\widehat p_l=\mathcal R_l\),
while its perturbed normalized forward output is
\(\widehat q_l=\mathcal F_l/\sqrt n=q_l^{\rm src}+g_l+\sigma V_l/\sqrt n\).
The raw query errors and their normalized sizes are consequently
\[
 e_l^{\rm rev}=\sqrt n\,k_l+\sigma U_l,\qquad
 e_l^{\rm for}=\sqrt n\,g_l+\sigma V_l,
 \tag{15}
\]
\[
 \frac{\|e_l^{\rm rev}\|_2}{\sqrt n}\le\|k_l\|_2+\sigma\frac{\|U_l\|_2}{\sqrt n},
 \qquad
 \frac{\|e_l^{\rm for}\|_2}{\sqrt n}\le\|g_l\|_2+\sigma\frac{\|V_l\|_2}{\sqrt n}.
 \tag{16}
\]
The source names the direct noises \(\sigma U/\sqrt m\) in the
normalized forward response and \(\sigma V\) in the raw reverse response,
with independent standard arrays; see
[Panahi v1, p. 4, Eq. (9)](https://arxiv.org/pdf/2603.09310v1#page=4).
Equation (14) simply swaps these independent names: our raw reverse uses
\(U\), and our raw forward uses \(V\). With \(m=n\), both raw direct noises
have coordinate variance \(\sigma^2\), and their contributions to the
errors divided by \(\sqrt n\) are \(\sigma U_l/\sqrt n\) and
\(\sigma V_l/\sqrt n\). This harmless naming swap is fully compatible
with the earlier Euler note. The citation is used only for this
definition; no complex-continuation claim or multi-matrix distribution
theorem is adopted. The Gaussian maximum is derived in Section 4.

Initialize the auxiliary registers
\[
 a^{(2)}_0=R^{(1)}_0=0,\qquad
 M^{(2)}_0=M^{(3)}_0=0,\qquad
 x^{(1)}_0=F(z^{(1)}_0),\qquad W^{(4)}_0\text{ as in (8)}.
 \tag{17}
\]
Here \(a^{(2)},R^{(1)},x^{(1)},W^{(4)},z^{(2)},z^{(3)}\) are vectors of
length \(n\), and \(M^{(2)},M^{(3)}\) are \(n\)-by-\(n\) matrices. The
preactivation registers \(z^{(2)}_0,z^{(3)}_0\) are obtained only by these
two warmup calls:

1. Lower call \(l=1\): use \(v^{(2)}_1=0\),
   \(h^{(2),\mathrm{query}}_1=h^{(1)}_0\), and set
   \(z^{(2)}_0=\mathcal F^{(2)}_1\).
2. Upper call \(l=1\): use \(v^{(3)}_1=0\),
   \(h^{(3),\mathrm{query}}_1=\phi(z^{(2)}_0)\), and set
   \(z^{(3)}_0=\mathcal F^{(3)}_1\).

Discard both warmup reverse outputs. For either warmup, \(\theta_1=0\)
implies \(t_1=0\), so (13) gives \(g_1=k_1=0\). The forward direct noise
does not vanish. In particular, the exact identities for these declared
oracle outputs are
\[
 z^{(2)}_0=W^{(2)}_0h^{(1)}_0+\sigma V^{(2)}_1,
 \qquad
 z^{(3)}_0=W^{(3)}_0\phi(z^{(2)}_0)+\sigma V^{(3)}_1.
 \tag{18}
\]
There are no other initial-matrix calls in initialization. Formula (18)
describes the two noisy calls; it is not an instruction to evaluate their
exact parts separately. The seeds have the canonical distribution (8),
but these warmup registers are not canonical exact network initialization.

## 2. All actual updates and their causal measurability

At each mesh state \(j=0,\ldots,N-1\), first form, entirely from that
pre-step state,
\[
 h^{(1)}_j=\psi(x^{(1)}_j),\qquad
 h^{(2)}_j=\phi(z^{(2)}_j),\qquad
 h^{(3)}_j=\phi(z^{(3)}_j),\qquad
 \delta^{(3)}_j=W^{(4)}_j\odot\phi'(z^{(3)}_j).
 \tag{19}
\]
At call index \(l=j+2\), use
\[
 \begin{array}{c|cc}
   &\theta_l&\omega_l\\\hline
 \text{lower }(b=2)&a^{(2)}_j/\sqrt n&h^{(1)}_j\\
 \text{upper }(b=3)&\delta^{(3)}_j/\sqrt n&h^{(2)}_j.
 \end{array}
 \tag{20}
\]
Execute the lower reverse/forward pair and then the upper reverse/forward
pair. Both arguments of both pairs have already been selected before
these outputs arrive. From the current upper reverse output form
\[
 q^{(2)}_j=\mathcal R^{(3)}_{j+2}
             +(M^{(3)}_j)^T\delta^{(3)}_j,
 \qquad
 \delta^{(2)}_j=\phi'(z^{(2)}_j)\odot\tau(q^{(2)}_j).
 \tag{21}
\]
Now update all registers simultaneously, using exactly the old factors
displayed on the right:
\[
 \begin{split}
 a^{(2)}_{j+1}&=a^{(2)}_j+\eta\delta^{(2)}_j,\\
 M^{(2)}_{j+1}&=M^{(2)}_j+
       \frac\eta n\delta^{(2)}_j(h^{(1)}_j)^T,\\
 M^{(3)}_{j+1}&=M^{(3)}_j+
       \frac\eta n\delta^{(3)}_j(h^{(2)}_j)^T,\\
 R^{(1)}_{j+1}&=R^{(1)}_j+\eta(M^{(2)}_j)^T\delta^{(2)}_j,\\
 W^{(4)}_{j+1}&=W^{(4)}_j+\eta h^{(3)}_j,\\
 x^{(1)}_{j+1}&=x^{(1)}_j+
    \frac\eta\epsilon
      [x^{(1)}_0+\mathcal R^{(2)}_{j+2}+R^{(1)}_j-x^{(1)}_j],\\
 z^{(2)}_{j+1}&=z^{(2)}_j+
    \frac\eta\epsilon
      [\mathcal F^{(2)}_{j+2}+M^{(2)}_j h^{(1)}_j-z^{(2)}_j],\\
 z^{(3)}_{j+1}&=z^{(3)}_j+
    \frac\eta\epsilon
      [\mathcal F^{(3)}_{j+2}+M^{(3)}_j h^{(2)}_j-z^{(3)}_j].
 \end{split}
 \tag{22}
\]
The memories retain every earlier increment. In particular, \(R^{(1)}\)
uses pre-step \(M^{(2)}_j\), not \(M^{(2)}_{j+1}\). The histories in the
theorem are the matrices \(\Theta^{(2)}_l,\Omega^{(2)}_l/\sqrt n,
\Theta^{(3)}_l,\Omega^{(3)}_l/\sqrt n\) actually generated by (17)--(22).

More explicitly, the finite-step memory identities are
\[
 \begin{split}
 M^{(2)}_j&=\frac\eta n\sum_{i<j}
                    \delta^{(2)}_i(h^{(1)}_i)^T,\\
 M^{(3)}_j&=\frac\eta n\sum_{i<j}
                    \delta^{(3)}_i(h^{(2)}_i)^T,\\
 R^{(1)}_j&=\eta\sum_{i<j}(M^{(2)}_i)^T\delta^{(2)}_i
       =\frac{\eta^2}{n}\sum_{0\le u<i<j}
           h^{(1)}_u(\delta^{(2)}_u)^T\delta^{(2)}_i\\
       &=\frac\eta n\sum_{u<j}h^{(1)}_u(\delta^{(2)}_u)^T
                         [a^{(2)}_j-a^{(2)}_{u+1}].
 \end{split}
 \tag{22a}
\]
The last identity uses
\(a^{(2)}_j-a^{(2)}_{u+1}=\eta\sum_{u<i<j}\delta^{(2)}_i\).
Thus \(R^{(1)}\) is the Euler, pre-step accumulated full rank memory;
at finite \(\eta\) it is not literally the continuous integral in the
integrated dependency. The strict time triangle is part of the specified
Euler convention. No trained term or earlier memory update is dropped.

Finiteness and measurability do not require a probability estimate.
All Gaussian entries are finite almost surely. Every regularized Gram
matrix in (11) is positive definite with smallest eigenvalue at least
\(\sigma^2>0\). Positive-diagonal Cholesky factorization and inversion
are continuous on this domain: the recursive diagonal square roots have
positive arguments and their denominators do not vanish. Formula (13)
therefore gives finite measurable outputs at every finite prefix. The
inverse \(F^{-1}\), arctangent, and \(\tau\) are continuous; finite sums
and products in (22) preserve finiteness. Induction over the two warmups
and the \(N\) updates proves the claim. No uniform bound is needed to
perform this induction.

For completeness, the adaptive filtration applies separately to each
matrix despite their interaction. For matrix \(b\), let
\(\mathcal H^{(b)}\) contain all canonical initial blocks, all \(U,V\),
and the other matrix's whole Gamma array. These primitive arrays are
jointly independent of \(\Gamma^{(b)}\). Set
\[
 \mathscr F^{(b)}_l=\mathcal H^{(b)}\vee
  \sigma(\Gamma^{(b)}_{ij}:i,j\le l),\qquad
 \mathscr F^{(b)}_{l-1/2}=\mathscr F^{(b)}_{l-1}\vee
  \sigma(\Gamma^{(b)}_{lj}:j<l).
 \tag{23}
\]
In the warmup, the upper forward argument depends only on the lower
warmup output, which is \(\mathcal H^{(3)}\)-measurable. Its own reverse
argument is zero. At each later call \(l=j+2\), the state at \(j\) uses
only calls through \(l-1\) of both matrices. Inductively it is
\(\mathscr F^{(b)}_{l-1}\)-measurable for each \(b\); the other matrix's
past calculations are measurable functions of the own past prefix and
the arrays already in \(\mathcal H^{(b)}\).

Consequently \(\theta_l\) and \(\omega_l\) in (20) are known before
the own fresh row. The reverse formula (13) uses only that row and the
old prefix. The forward formula then uses the own fresh column,
including the diagonal. The lower current call, when viewed in the
upper filtration, is also measurable before the upper fresh row,
because its arguments were pre-step arguments and its Gamma array is
in \(\mathcal H^{(3)}\). Thus the prescribed
\(\theta\to\widehat p\to\omega\to\widehat q\) order is valid.

The algorithm's query maps themselves need only its initial \(z^{(1)}_0,
W^{(4)}_0\) and its finite transcript of declared outputs. The larger
\(\mathcal H^{(b)}\) is a device for proving the adaptive estimate; it
does not authorize unrecorded matrix calls or supply an external network
trajectory. Nor does it include the other matrix's realized adaptive
transcript as an independent random array: that transcript is generated
by the just-verified measurable recursion.

## 3. The adaptive estimate in the exact form used

Here is the specialization of the proved dependency to \(m=n\). For
either matrix set
\[
 \begin{split}
 B_{l-1/2}&=\sum_{i\le l,\,j<l}t_i\Gamma_{ij}s_j^T,
 &B_l&=\sum_{i,j\le l}t_i\Gamma_{ij}s_j^T,\\
 \mathfrak a_l&=\sum_{j<l}s_j\Gamma_{lj},
 &\mathfrak b_l&=\sum_{i\le l}t_i\Gamma_{il}.
 \end{split}
 \tag{24}
\]
The different font distinguishes these fresh Gaussian residual vectors
from the primitive register \(a^{(2)}\). The exact identities are
\[
 \begin{split}
 g_l&=B_l\omega_l/n+
       \frac{\sigma^2}{\sqrt n A_{\omega,ll}}\mathfrak b_l,\\
 k_l&=B_{l-1/2}^T\theta_l/\sqrt n+
       \frac{\sigma^2}{\sqrt n A_{\theta,ll}}\mathfrak a_l.
 \end{split}
 \tag{25}
\]
For example, (11)--(12) give
\[
 s_i^T\omega_l/\sqrt n
   =(A_\omega-\sigma^2A_\omega^{-T})_{il}.
\]
For \(i<l\) this is \(A_{\omega,il}\); on the diagonal it is
\(A_{\omega,ll}-\sigma^2/A_{\omega,ll}\). Substitution into (13)
gives the forward identity in (25); the same identity for \(t_i^T\theta_l\)
gives the strict reverse identity. Each diagonal is at least \(\sigma\):
its squared Schur complement is
\[
 \sigma^2+y^T[I-X(X^TX+\sigma^2I)^{-1}X^T]y\ge\sigma^2,
\]
where \(X\) comprises the previous normalized query columns. The matrix
in brackets is positive semidefinite, since its eigenvalues are
\(\sigma^2/(d^2+\sigma^2)\) on singular directions and one on the
orthogonal complement.

For a deterministic ceiling \(r>0\) and \(0<\alpha<1\), define
\[
 u=\log(4K/\alpha),\quad v=\log(4n/\alpha),\quad
 c(r)=\sqrt{2r+4u},\quad
 L(r)=2\sqrt{rv}+\tfrac23c(r)v.
 \tag{26}
\]
Let \(E_r^{(b)}\) be the event that both final effective ranks for matrix
\(b\) are at most \(r\). The adaptive theorem states
\[
 \mathbb P\left(E_r^{(b)}\cap\left\{
    \max_h\|B^{(b)}_h\|_{\rm op}>L(r)
    \ \text{or}\ 
    \max_l(\|\mathfrak a^{(b)}_l\|_2\vee
           \|\mathfrak b^{(b)}_l\|_2)>c(r)
 \right\}\right)\le\alpha.
 \tag{27}
\]
Here \(h\) ranges over all half and full steps, so no additional union
over query times is necessary. On \(E_r^{(b)}\), outside that exceptional
event, (25) implies for every call
\[
 \begin{split}
 \|g_l\|_2&\le
       \frac{L(r)\|h_l\|_2}{n}+\frac{\sigma c(r)}{\sqrt n},\\
 \|k_l\|_2&\le
       \frac{L(r)\|v_l\|_2}{n}+\frac{\sigma c(r)}{\sqrt n}.
 \end{split}
 \tag{28}
\]
These are pointwise inequalities; the query norms can subsequently be
bounded on an intersected event.

All hypotheses are satisfied: dimensions and horizon are deterministic
and finite, \(\sigma>0\), (9) supplies independent standard Gamma
entries and an independent \(\mathcal H^{(b)}\), (23) supplies the
required causal order, and (11) uses the required consistent Cholesky
choice. In the dependency, localization uses the actual histories and
does not modify their dynamics. The fresh conditional covariances are
\(\sum_{j<l}s_js_j^T\) and \(\sum_{i\le l}t_it_i^T\), each bounded by
the identity, with traces the corresponding effective ranks. In
particular \(\rho\le n\) always, regardless of raw query magnitudes.
Thus the first application of (27) with \(r=n\) has an automatic rank
premise. The second application below has a deterministic smaller
ceiling proved for these very histories.

## 4. Initial and direct-noise events; first adaptive pass

Let
\[
 E_0=\{\|W^{(2)}_0\|_{\rm op},\|W^{(3)}_0\|_{\rm op}\le8,
                   \ \|W^{(4)}_0\|_\infty\le1\}.
 \tag{29}
\]
We record elementary bounds for its probability instead of assuming a
primal bound for the new recursion. For a standard scalar Gaussian \(Z\),
completion of the square gives \(\mathbb E e^{tZ}=e^{t^2/2}\). Markov's
inequality, with \(t=a\) and then \(t=-a\), gives
\(\mathbb P(|Z|>a)\le2e^{-a^2/2}\). Hence the readout part fails with
probability at most \(2n e^{-n^2/2}\).

The Euclidean unit sphere has a \(1/4\)-net of size at most \(9^n\): take
a maximal separated set, whose disjoint radius-\(1/8\) balls lie in the
radius-\(9/8\) ball, and compare volumes. Maximality gives the net
property. For unit \(x,y\), approximate both by net points \(x_0,y_0\).
The error in \(x^TWy-x_0^TWy_0\) is at most
\(\frac12\|W\|_{\rm op}\), so
\(\|W\|_{\rm op}\le2\max_{x_0,y_0}|x_0^TWy_0|\).
For fixed net points and a matrix from (8), this bilinear form is a
Gaussian of variance \(1/n\). A union bound gives
\[
 \mathbb P(\|W\|_{\rm op}>8)
 \le2\,9^{2n}e^{-8n}.
\]
Applying it to both initial hidden matrices proves
\[
 \mathbb P(E_0^c)\le
 p_0(n):=4e^{-(8-2\log9)n}+2n e^{-n^2/2}.
 \tag{30}
\]
The first-layer Gaussian vector is finite almost surely. No norm bound
on its polynomial transform \(x^{(1)}_0\) will be needed; we bound the
displacement \(x^{(1)}_j-x^{(1)}_0\).

From now on choose \(\alpha=n^{-2}\) in (26), so
\[
 u=\log(4Kn^2),\qquad v=\log(4n^3),\qquad
 D_n=\sqrt{2+4u/n}=c(n)/\sqrt n.
 \tag{31}
\]
For a standard Gaussian vector \(Z\in\mathbb R^n\), integrating its
Gaussian density gives \(\mathbb E e^{\|Z\|_2^2/4}=2^{n/2}\le e^{n/2}\).
Therefore
\[
 \mathbb P(\|Z\|_2^2>2n+4u)\le e^{-u}.
\]
There are exactly \(4K\) direct-noise vectors across two orientations
and two matrices. The event
\[
 E_D=\left\{\max_{b,l}
   \frac{\|U^{(b)}_l\|_2\vee\|V^{(b)}_l\|_2}{\sqrt n}\le D_n\right\}
 \tag{32}
\]
satisfies \(\mathbb P(E_D^c)\le4Ke^{-u}=\alpha\), without any assumption
on the histories those vectors generate.

For each matrix let \(E_C^{(b)}\) be the event that all the bounds inside
(27) hold with \(r=n\). Since the rank premise is automatic,
\(\mathbb P((E_C^{(b)})^c)\le\alpha\). Define
\[
 E_C=E_0\cap E_D\cap E_C^{(2)}\cap E_C^{(3)}.
 \tag{33}
\]
No independence between these events is asserted or needed. Equations
(30)--(33) give \(\mathbb P(E_C^c)\le p_0(n)+3\alpha\).

The deterministic inequalities \(K\le(S+2)n^2\) and \(n\ge2\) imply
\[
 u,v\le C_S\ell_n,\qquad
 D_n\le C_S,\qquad
 c(n)\le C_S\sqrt n,\qquad
 L(n)/\sqrt n\le C_S\ell_n.
 \tag{34}
\]
For example, \(\ell_n/n\) is bounded for \(n\ge2\), and the two terms
in \(L(n)/\sqrt n\) are \(2\sqrt v\) and
\((2/3)D_nv\). Thus (14), (16), (28), and \(E_0\) show, on \(E_C\),
for either oracle and every actual call,
\[
 \frac{\|\mathcal R_l\|_2}{\sqrt n}\le C_S\ell_n\frac{\|v_l\|_2}{\sqrt n}+C_S\sigma,
 \qquad
 \frac{\|\mathcal F_l\|_2}{\sqrt n}\le C_S\ell_n\frac{\|h_l\|_2}{\sqrt n}+C_S\sigma.
 \tag{35}
\]
This conclusion does not presuppose any bound on \(v_l\).

In particular, the warmup identities (18) and \(|\phi|\le c_\phi\)
give
\(\|z^{(2)}_0\|_2/\sqrt n,\|z^{(3)}_0\|_2/\sqrt n
  \le8c_\phi+\sigma D_n\le C_S\).
For orientation only, define the mathematical reference values
\(z^{(2),\mathrm{can}}_0=W^{(2)}_0h^{(1)}_0\) and
\(z^{(3),\mathrm{can}}_0=W^{(3)}_0\phi(z^{(2),\mathrm{can}}_0)\).
They are not evaluated by the algorithm. Their initial differences obey
\[
 \frac{\|z^{(2)}_0-z^{(2),\mathrm{can}}_0\|_2}{\sqrt n}\le\sigma D_n,
 \qquad
 \frac{\|z^{(3)}_0-z^{(3),\mathrm{can}}_0\|_2}{\sqrt n}\le9\sigma D_n,
 \tag{36}
\]
because the upper initial operator norm is at most eight and \(\phi\)
is 1-Lipschitz. This proves small initial discrepancies without hiding
any exact initialization calls.

## 5. Noncircular bounds for the actual states

All bounds in this section are deterministic on \(E_C\), uniform through
state \(N\), and uniform in the fixed choice of \(\tau\). Constants may
increase from line to line. For a rank-one increment,
\[
 \left\|uv^T/n\right\|_F=\frac{\|u\|_2\|v\|_2}{n},\qquad
 \frac{\|Av\|_2}{\sqrt n}\le\|A\|_{\rm op}\frac{\|v\|_2}{\sqrt n}\le\|A\|_F\frac{\|v\|_2}{\sqrt n}.
 \tag{37}
\]

First the readout update alone, independent of every other bound, gives
\[
 \|W^{(4)}_j\|_\infty\le1+j\eta c_\phi
        \le B_4:=1+(S+1)c_\phi,
 \qquad \frac{\|\delta^{(3)}_j\|_2}{\sqrt n}\le B_4.
 \tag{38}
\]
The upper matrix memory therefore satisfies
\[
 \|M^{(3)}_j\|_F
 \le\eta\sum_{i<j}\frac{\|\delta^{(3)}_i\|_2\|h^{(2)}_i\|_2}{n}
 \le T B_4c_\phi\le C_S.
 \tag{39}
\]
The upper reverse query in (20) has raw argument \(\delta^{(3)}_j\).
Using (35), (38), and (39) in (21) gives
\[
 \frac{\|q^{(2)}_j\|_2}{\sqrt n}
 \le C_S\ell_n B_4+C_S\sigma+
          \|M^{(3)}_j\|_F B_4
 \le C_S\ell_n,
 \qquad \frac{\|\delta^{(2)}_j\|_2}{\sqrt n}\le\frac{\|q^{(2)}_j\|_2}{\sqrt n}\le C_S\ell_n.
 \tag{40}
\]
The last inequality uses just (2) and \(\phi'\le1\). Summing the first
two updates in (22) yields
\[
 \frac{\|a^{(2)}_j\|_2}{\sqrt n}\le C_ST\ell_n\le C_S\ell_n,
 \qquad
 \|M^{(2)}_j\|_F\le C_STc_\phi\ell_n\le C_S\ell_n.
 \tag{41}
\]
The pre-step memory formula for \(R^{(1)}\) then yields
\[
 \frac{\|R^{(1)}_j\|_2}{\sqrt n}
 \le\eta\sum_{i<j}\|M^{(2)}_i\|_F\frac{\|\delta^{(2)}_i\|_2}{\sqrt n}
 \le C_S\ell_n^2.
 \tag{42}
\]
In particular, the lower reverse output and the two forward outputs
satisfy
\[
 \frac{\|\mathcal R^{(2)}_{j+2}\|_2}{\sqrt n}\le C_S\ell_n^2,
 \qquad
 \frac{\|\mathcal F^{(2)}_{j+2}\|_2}{\sqrt n},
 \frac{\|\mathcal F^{(3)}_{j+2}\|_2}{\sqrt n}\le C_S\ell_n,
 \tag{43}
\]
by (35), (41), and the uniform bound on every activation.

Set \(y_j=x^{(1)}_j-x^{(1)}_0\) and
\(\lambda=\eta/\epsilon=n^{-15/8}\in(0,1]\). The last three updates
in (22) are convex combinations of the current register and its target:
\[
 \begin{split}
 y_{j+1}&=(1-\lambda)y_j+
     \lambda[\mathcal R^{(2)}_{j+2}+R^{(1)}_j],\\
 z^{(2)}_{j+1}&=(1-\lambda)z^{(2)}_j+
     \lambda[\mathcal F^{(2)}_{j+2}+M^{(2)}_jh^{(1)}_j],\\
 z^{(3)}_{j+1}&=(1-\lambda)z^{(3)}_j+
     \lambda[\mathcal F^{(3)}_{j+2}+M^{(3)}_jh^{(2)}_j].
 \end{split}
 \tag{44}
\]
The targets have normalized norms at most \(C_S\ell_n^2,C_S\ell_n,
C_S\ell_n\), respectively, by (39)--(43). Since \(y_0=0\) and the
warmup preactivations are bounded, the triangle inequality and induction
in (44) give
\[
 \max_{j\le N}\frac{\|x^{(1)}_j-x^{(1)}_0\|_2}{\sqrt n}\le C_S\ell_n^2,
 \qquad
 \max_{j\le N}
 \frac{\|z^{(2)}_j\|_2\vee\|z^{(3)}_j\|_2}{\sqrt n}\le C_S\ell_n.
 \tag{45}
\]
There was no feedback bootstrap in this chain: bounded activations give
the readout and \(\delta^{(3)}\) bounds first, then the upper memory,
then \(\delta^{(2)}\), the lower memories, and finally the relaxed
registers. It uses neither a small effective-rank premise nor bounds
borrowed from an unperturbed network.

## 6. Actual slow histories and the warmup column

Taking differences in (44), and using both the target and state bounds,
gives
\[
 \begin{split}
 \frac{\|x^{(1)}_{j+1}-x^{(1)}_j\|_2}{\sqrt n}
      &\le C_S\eta\ell_n^2/\epsilon,\\
 \frac{\|z^{(2)}_{j+1}-z^{(2)}_j\|_2}{\sqrt n}
  \vee \frac{\|z^{(3)}_{j+1}-z^{(3)}_j\|_2}{\sqrt n}
      &\le C_S\eta\ell_n/\epsilon.
 \end{split}
 \tag{46}
\]
The Lipschitz bounds in (7) transfer these estimates to the first two
activation histories. For the upper reverse history, use the exact
difference identity
\[
 \begin{split}
 \delta^{(3)}_{j+1}-\delta^{(3)}_j
 ={}&(W^{(4)}_{j+1}-W^{(4)}_j)\odot\phi'(z^{(3)}_{j+1})\\
 &+W^{(4)}_j\odot
       [\phi'(z^{(3)}_{j+1})-\phi'(z^{(3)}_j)].
 \end{split}
\]
It and (38), (46) imply
\[
 \frac{\|\delta^{(3)}_{j+1}-\delta^{(3)}_j\|_2}{\sqrt n}
 \le\eta c_\phi+2B_4\frac{\|z^{(3)}_{j+1}-z^{(3)}_j\|_2}{\sqrt n}
 \le C_S\eta\ell_n/\epsilon.
\]
Finally \(\frac{\|a^{(2)}_{j+1}-a^{(2)}_j\|_2}{\sqrt n}\le C_S\eta\ell_n\) follows
directly from (40). Summing adjacent increments proves the discrete
Lipschitz bounds on mesh indices, with constants
\[
 \begin{array}{c|c}
 \text{normalized mesh history}&\text{Lipschitz constant in feature time}\\\hline
 h^{(1)}_j/\sqrt n&C_S\ell_n^2/\epsilon\\
 h^{(2)}_j/\sqrt n&C_S\ell_n/\epsilon\\
 \delta^{(3)}_j/\sqrt n&C_S\ell_n/\epsilon\\
 a^{(2)}_j/\sqrt n&C_S\ell_n.
 \end{array}
 \tag{47}
\]
Choose once a deterministic constant \(C_*(S)\ge1\) large enough that
\[
 M_*:=C_*(S)\ell_n^2/\epsilon
 \tag{48}
\]
dominates all four constants in (47), for all \(n\ge2\). Such a choice
is possible because every preceding constant was deterministic and
independent of \(\tau\).

The warmup needs separate treatment. For the lower reverse history its
warmup and first mesh column are both zero. For the two forward
histories the warmup repeats the first mesh argument. For the upper
reverse history, however, the warmup column is zero while the first
mesh column is \(\delta^{(3)}_0/\sqrt n\), generally nonzero, at the
same physical and feature time. We do **not** assert (47) across this
pair. We keep the warmup column exactly in a column approximation,
costing at most one additional rank direction for each history.

Here is the deterministic estimate, including integer and dimension
choices. Let \(X\) be any one of the \(n\)-by-\(K\) normalized full
histories, comprising one warmup and \(N\) mesh columns. For any integer
\(1\le d\le N\), partition the mesh-column indices \(1,\ldots,N\) into
the nonempty blocks
\[
 \lfloor (a-1)N/d\rfloor< i\le\lfloor aN/d\rfloor,
       \qquad a=1,\ldots,d.
\]
Replace each mesh column by its block's first column, and retain the
warmup exactly, to obtain \(Y\). Then
\[
 \operatorname{rank}Y\le d+1,\qquad
 \|X-Y\|_F^2\le N(M_*T/d)^2.
 \tag{49}
\]
Indeed, each block spans at most
\(\eta(\lceil N/d\rceil-1)\le\eta N/d=T/d\) in feature time,
and (47)--(48) bound each column error by \(M_*T/d\).

To verify the effective-rank implication without a spectral-tail
assumption, let \(P\) be the orthogonal projection onto the column space
of \(Y\), and let \(Q=XX^T(XX^T+\sigma^2I)^{-1}\). Eigenvalues give
\(0\preceq Q\preceq I\) and \(Q\preceq XX^T/\sigma^2\). Consequently
\[
 \begin{split}
 \rho(X)&=\operatorname{tr}(PQ)+\operatorname{tr}((I-P)Q)\\
 &\le d+1+\sigma^{-2}\|(I-P)X\|_F^2\\
 &\le d+1+\frac{NM_*^2T^2}{\sigma^2d^2}.
 \end{split}
 \tag{50}
\]
The last line uses \((I-P)Y=0\). Independently \(\rho(X)\le\min(n,K)\).

Put
\[
 x_*=(NM_*^2T^2/\sigma^2)^{1/3},\qquad
 d=\min\{N,\max\{1,\lceil x_*\rceil\}\}.
 \tag{51}
\]
If \(0<x_*\le N\), then \(d\le x_*+1\), \(d\ge x_*\), and (50) is
at most \(2+2x_*\). If \(x_*=0\), choose \(d=1\), and (50) is at most
two. If \(x_*>N\), take the exact \(K\)-column rank bound; in this case
\(K=N+1\le2+2x_*\). Thus, in every case,
\[
 \rho(X)\le R_n:=\min\{n,K,2+2x_*\}.
 \tag{52}
\]
The ceiling \(R_n>0\) is deterministic; the adaptive theorem permits real
ceilings. The integer \(d\) used to prove it has been specified in (51).
For the chosen parameters,
\[
 \begin{split}
 x_*&=C_*(S)^{2/3}
  (NT^2\epsilon^{-2}\sigma^{-2})^{1/3}\ell_n^{4/3}\\
 &\le C_S\big(n^2 n^{1/4}n^{1/2}\big)^{1/3}\ell_n^{4/3}
  =C_S n^{11/12}\ell_n^{4/3}.
 \end{split}
 \tag{53}
\]
This proves (5) for final histories on \(E_C\), with the extra two
absorbed in \(C_S\). Prefix effective ranks cannot exceed the final
rank: the consistent Cholesky columns express them as
\(\sum_{i\le l}\|t_i\|_2^2\) or \(\sum_{i\le l}\|s_i\|_2^2\).
This also proves (5) for every prefix. Every matrix in (49)--(53) is
the realized perturbed history; no frozen-history probabilistic
calculation was used.

## 7. Second adaptive pass and raw perturbation size

Apply (27) again to each matrix, now with the deterministic ceiling
\(r=R_n\), the same \(K,\sigma\), and failure allowance \(\alpha=n^{-2}\).
For \(b=2,3\), let
\[
 F_b=E_{R_n}^{(b)}\cap\left\{
    \max_h\|B^{(b)}_h\|_{\rm op}>L(R_n)
    \ \text{or}\ 
    \max_l(\|\mathfrak a^{(b)}_l\|_2\vee
           \|\mathfrak b^{(b)}_l\|_2)>c(R_n)
 \right\}.
 \tag{54}
\]
The theorem gives \(\mathbb P(F_b)\le\alpha\) unconditionally. Section 6
proved \(E_C\subseteq E_{R_n}^{(2)}\cap E_{R_n}^{(3)}\). Therefore on
\[
 \mathcal E_n^\tau=E_C\setminus(F_2\cup F_3)
 \tag{55}
\]
all the refined bounds hold for both matrices. The union bound gives
(4). In particular, we have not conditioned the second martingale
argument on the first pass, nor resampled any arrays, nor assumed
independence of the two matrices' resulting bad events.

From (26), (31), and (34),
\[
 \frac{L(R_n)}{\sqrt n}
 \le C_S\left(\sqrt{R_n/n}\,\ell_n+
                  n^{-1/2}\ell_n^{3/2}\right).
 \tag{56}
\]
Here \(\sqrt{R_nv}/\sqrt n\le C_S\sqrt{R_n/n}\ell_n\), and
\(c(R_n)\le\sqrt{2R_n}+2\sqrt u\) bounds the other term. Using (53)
in (56) yields
\[
 \frac{L(R_n)}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{5/3}
       +C_S n^{-1/2}\ell_n^{3/2}.
 \tag{57}
\]
Also \(R_n\le n\) implies
\[
 \sigma c(R_n)/\sqrt n\le\sigma c(n)/\sqrt n\le C_S\sigma.
 \tag{58}
\]
All forward raw arguments obey \(\frac{\|h_l\|_2}{\sqrt n}\le c_\phi\), including
warmups. All upper reverse raw arguments have normalized norm at most
\(B_4\), including the zero warmup. All lower reverse raw arguments have
normalized norm at most \(C_S\ell_n\) by (41), again including the zero
warmup. Thus a common upper bound for every query norm occurring in
(28) is \(C_S\ell_n\). Combining (16), (28), (32), and (57)--(58) gives
\[
 \max_{b,l}
 \frac{\|e_l^{(b),\rm rev}\|_2\vee\|e_l^{(b),\rm for}\|_2}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{8/3}
    +C_S n^{-1/2}\ell_n^{5/2}+C_S\sigma.
 \tag{59}
\]
For \(n\ge2\), the middle term is bounded by the first after enlarging
the constant, since their ratio is \(n^{-11/24}\ell_n^{-1/6}\le1\).
Substitution of \(\sigma=n^{-1/4}\) proves (6).

The rank bound also gives
\(R_n\ell_n^2/n\le C_S n^{-1/12}\ell_n^{10/3}\to0\), consistent
with the adaptive theorem's criterion. For any one of these errors,
its mesh primitive satisfies the purely deterministic bound
\[
 \max_{j\le N}\frac{\left\|\eta\sum_{i<j}e_{i+2}\right\|_2}{\sqrt n}
       \le T\max_{l\ge2}\frac{\|e_l\|_2}{\sqrt n}.
 \tag{60}
\]
Neither (59) nor (60) is a nonlinear trajectory comparison. The theorem
is proved for each prescribed \(\tau\). Its constants and failure
allowances are uniform in clipping level, but its adaptive events may
depend on \(\tau\). No union over all clipping maps has been taken.

For the degenerate horizon \(S=0\), there are no updates and \(K=1\):
the reverse histories are zero, each forward history has effective rank
at most one, the Gamma terms vanish, and the same asymptotic claims
follow directly from the Gaussian maximum for the four warmup noise
vectors. The main proof above treats the nonempty-update case \(S>0\).

## 8. Exact scope of the remaining canonical-network obligations

The separate companion
[FILTERED_QUERY_CLIPPED_STABILITY.md](FILTERED_QUERY_CLIPPED_STABILITY.md)
proves its own deterministic fixed-clipping stability/filter-removal
estimate for this exact recurrence, under its stated hypotheses, using
filter contraction and slow-state Gronwall. With the initial operator
bound fixed at eight, its rate is
\(C_{S,R}(\epsilon+\eta+\max_l\|e_l\|_2/\sqrt n+\text{initial mismatch})\),
without an \(\exp(C/\epsilon)\) factor. That proof is neither duplicated
nor assumed in this rank proof. Statements below identify obligations
outside this rank candidate, not obstructions to that separate approach.

The integrated dependency motivates the registers: in the uncut
feature flow, \(a^{(2)}=\int\delta^{(2)}\), the two \(M\)'s are the
trained matrix increments, and
\(R^{(1)}=\int(M^{(2)})^T\delta^{(2)}\). Its exact algebraic state
relations are
\[
 x^{(1)}=x^{(1)}_0+(W^{(2)}_0)^Ta^{(2)}+R^{(1)},\quad
 z^{(2)}=(W^{(2)}_0+M^{(2)})h^{(1)},\quad
 z^{(3)}=(W^{(3)}_0+M^{(3)})h^{(2)}.
 \tag{61}
\]
In the auxiliary recursion, (61) is replaced by noisy relaxation targets.
In particular, even if one writes \(W^{(b)}_j=W^{(b)}_0+M^{(b)}_j\),
the registers generally do not obey \(z^{(b)}_j=W^{(b)}_jh^{(b-1)}_j\).
The formulas therefore do not define ordinary raw GD of that network.

1. **Trajectory stability under oracle perturbations is separate.**
   Equation (6) controls the additive error at the actual perturbed query,
   rather than the difference of matrix responses at two different
   trajectories. A removal proof must propagate those differences through
   (21)--(22) and the full memories, uniformly in width and in the chosen
   diagonal parameters. The relaxation drift divides an input error by
   \(\epsilon\); the proved leading error bound divided by \(\epsilon\)
   is \(C_S n^{1/12}\ell_n^{8/3}\), which does not tend to zero. This is
   a limitation of that drift estimate, not a lower bound on actual error
   and not a proof that removal is impossible. The separate companion's
   filter-contraction argument avoids this crude drift estimate; that
   argument is not used here.

2. **Filter removal is treated in the separate fixed-clipping companion.**
   Its comparison concerns (22), with \(\epsilon\downarrow0\) and
   \(\eta/\epsilon\to0\), and the intended algebraic integral system (61),
   including the initial layer, tracking error, memory error, and nonlinear
   feedback. Its result is not a premise of this rank proof.
   The Lipschitz constants in (47) grow as \(\epsilon^{-1}\); their use
   to bound ranks does not establish such convergence. The noisy initial
   discrepancies vanish by (36), but small initial discrepancy alone does
   not establish subsequent stability. The fact that \(\sigma\to0\)
   and its own query perturbations vanish is likewise not removal at the
   trajectory or observable level.

3. **Uncut stability and clipping removal remain unresolved.** For a
   bounded clipping map with \(\sup|\tau|\le B_\tau\), the elementary
   difference estimate for the middle gate is
   \[
   \frac{\left\|\phi'(z^{(2)})\odot\tau(q^{(2)})
       -\phi'(\widetilde z^{(2)})\odot\tau(\widetilde q^{(2)})
       \right\|_2}{\sqrt n}
   \le \frac{\|q^{(2)}-\widetilde q^{(2)}\|_2}{\sqrt n}
       +2B_\tau\frac{\|z^{(2)}-\widetilde z^{(2)}\|_2}{\sqrt n}.
   \tag{62}
   \]
   Its stability constant depends on the clipping size, even though our
   rank and query-error constants do not. For identity, the retained term
   is \([\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]
   \odot\widetilde q^{(2)}\).
   For \(Q>0\) its exact tail bound is
   \[
   \frac{\left\|[\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]
                    \odot\widetilde q^{(2)}\right\|_2}{\sqrt n}
   \le2Q\frac{\|z^{(2)}-\widetilde z^{(2)}\|_2}{\sqrt n}
      +2\frac{\left\|\widetilde q^{(2)}
          \odot\mathbf1_{\{|\widetilde q^{(2)}|>Q\}}\right\|_2}{\sqrt n}.
   \tag{63}
   \]
   A bound on \(\|\widetilde q^{(2)}\|_2/\sqrt n\) does not provide a
   width-uniform multiplier bound or the uniform tails and
   tail-versus-stability rate
   needed for removal. Allowing identity in this auxiliary theorem proves
   its filtered rank conclusion for identity; it does not solve the
   uncut nonlinear comparison problem. There is also no simultaneous
   Gaussian event over all \(\tau\) in this proof.

4. **The physical clock and exact GD require separate proofs.** The
   canonical feature clock in the integrated dependency is
   \(ds/dt=-2(f_n-1)\), with
   \(f_n=(W^{(4)})^Th^{(3)}/n\). A finite feature-horizon estimate must
   be transferred to the intended physical horizon with a justified
   clock, including its possible degeneracy at zero residual, before it
   implies a physical-time statement. Defining the same scalar output
   from the filtered registers does not establish the canonical loss
   identity or clock convergence. Separately, (22) is an Euler recursion
   for the auxiliary registers, not canonical exact GD. For example,
   for scalar \(v\),
   \[
    F(z+v)-F(z)=(1+z^2)v+zv^2+v^3/3,
   \]
   so the continuous transformed identity does not commute with a raw
   GD step. A canonical discrete-time transfer must control these
   remainders, its actual step sizes and clock, and discretization errors
   uniformly over the relevant widths and time interval.

5. **Derivative observables and the limiting state remain separate.**
   Even hypothetical uniform convergence of the integrated lower response
   would not imply strong convergence of its derivative. In the unfiltered
   integral system,
   \[
    (W^{(2)})^T\delta^{(2)}
      =\frac d{ds}[(W^{(2)}_0)^Ta^{(2)}]
        +(M^{(2)})^T(a^{(2)})'.
   \tag{64}
   \]
   Hidden velocities, the lower backward signal and the first raw kernel
   block need derivative or energy control beyond (5)--(6). As a simple
   logical check, \(j^{-1}\sin(js)v\) converges uniformly to zero on any
   fixed interval, while its derivatives have nonvanishing time-\(L^2\)
   norm for fixed nonzero \(v\). This is not a canonical-network
   counterexample. Output convergence, a population state space, and
   unique autonomous restart also have not been constructed by a rank
   estimate in the changing ambient spaces \(\mathbb R^n\).

The completed result is the causal auxiliary rank-and-query theorem
(4)--(6). It removes the rank premise for this specified filtered
comparison algorithm and preserves the exact Gamma terms and all memory
updates. All identifications with uncut exact GD/GF, including removal
of noise, filtering, or any chosen clipping at the trajectory level,
remain outside the result.
