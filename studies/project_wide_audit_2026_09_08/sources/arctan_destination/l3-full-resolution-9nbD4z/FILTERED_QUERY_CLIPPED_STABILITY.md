# Filtered-query approximation: a fixed-clipping stability bridge

Status: candidate proof. This note compares a causal filtered recursion
to the canonical finite-width flow with one fixed bounded clipping.
It proves stability, not merely a residual along a supplied trajectory.
It does not remove clipping or prove the requested uncut global theorem.
The mesh is in feature time, not an assertion about exact raw GD.

The construction and probabilistic query estimates are in
CAUSAL_FILTERED_QUERY_RANK.md. This note is deterministic conditional
only on explicit initialization and query-error bounds. It states the
entire recurrence it uses, so its deterministic conclusion does not
assume the probabilistic claim from that companion.

## Statement and exact comparison

Fix \(S,M\ge1\), \(R\ge1\), \(n\ge1\), and a scalar map \(\tau\) with
\[
 |\tau(v)|\le |v|,\qquad |\tau(v)|\le R,\qquad
 |\tau(v)-\tau(w)|\le |v-w|.
 \tag{1}
\]
Take \(0<\eta\le1\), an integer \(N\ge1\) with \(N\eta\le S+1\),
and \(\eta\le\varepsilon\le1\).
Every vector norm below is an ordinary Euclidean norm.
Suppose the two initial matrices have operator norm at most \(M\)
and \(\|W^{(4)}_0\|_\infty\le1\).
There is no bound needed on individual coordinates of \(z^{(1)}_0\).

The reference is the canonical finite-width feature flow with
\[
 h^{(\ell)}=\phi(z^{(\ell)}),\quad \phi(z)=\arctan z,\quad
 z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
 \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
 q^{(2)}=(W^{(3)})^{\mathsf T}\delta^{(3)},\quad
 \delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}),
\]
\[
 (z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^{\mathsf T}\delta^{(2)},
 \quad (W^{(2)})'=\delta^{(2)}(h^{(1)})^{\mathsf T}/n,
 \quad (W^{(3)})'=\delta^{(3)}(h^{(2)})^{\mathsf T}/n,
 \quad (W^{(4)})'=h^{(3)}.
 \tag{2}
\]
All initial parameters equal the stated initial values. A prime in
this note means differentiation in feature time.
Put \(F(z)=z+z^3/3\), \(x^{(1)}=F(z^{(1)})\), and
\[
 a^{(2)}(s)=\int_0^s\delta^{(2)}(t)\,dt,\qquad
 M^{(\ell)}=W^{(\ell)}-W^{(\ell)}_0\quad(\ell=2,3),\qquad
 R^{(1)}(s)=\int_0^s (M^{(2)}(t))^{\mathsf T}\delta^{(2)}(t)\,dt.
 \tag{3}
\]
These identities retain every learned matrix term. Exactly,
\[
 x^{(1)}=x^{(1)}_0+(W^{(2)}_0)^{\mathsf T}a^{(2)}+R^{(1)}.
 \tag{4}
\]
Indeed \(F'=1/\phi'\) turns the first equation in (2) into
\((x^{(1)})'=(W^{(2)}_0+M^{(2)})^{\mathsf T}\delta^{(2)}\);
integrating proves (4).

Hats denote the filtered recursion at \(s_k=k\eta\).
At the start of each step set
\[
 \widehat h_k^{(1)}=\phi(F^{-1}(\widehat x_k^{(1)})),\quad
 \widehat h_k^{(2)}=\phi(\widehat z_k^{(2)}),\quad
 \widehat h_k^{(3)}=\phi(\widehat z_k^{(3)}),\quad
 \widehat\delta_k^{(3)}
   =\widehat W_k^{(4)}\odot\phi'(\widehat z_k^{(3)}).
\]
Let the four queried outputs be
\[
 \widehat T_k^{(2)}
  =(W^{(2)}_0)^{\mathsf T}\widehat a_k^{(2)}+e_{T,k}^{(2)},
 \qquad
 \widehat F_k^{(2)}
  =W^{(2)}_0\widehat h_k^{(1)}+e_{F,k}^{(2)},
\]
\[
 \widehat T_k^{(3)}
  =(W^{(3)}_0)^{\mathsf T}\widehat\delta_k^{(3)}+e_{T,k}^{(3)},
 \qquad
 \widehat F_k^{(3)}
  =W^{(3)}_0\widehat h_k^{(2)}+e_{F,k}^{(3)}.
 \tag{5}
\]
Here the query errors may depend arbitrarily on all previous states.
Assume only
\[
 \max_{\ell=2,3;\,0\le k<N}
 \frac{\|e_{T,k}^{(\ell)}\|_2+\|e_{F,k}^{(\ell)}\|_2}{\sqrt n}
 \le b,\qquad 0\le b\le1.
 \tag{6}
\]
Form \(\widehat q_k^{(2)}=\widehat T_k^{(3)}
       +(\widehat M_k^{(3)})^{\mathsf T}\widehat\delta_k^{(3)}\)
and \(\widehat\delta_k^{(2)}
       =\phi'(\widehat z_k^{(2)})\odot\tau(\widehat q_k^{(2)})\).
Every right side in the following simultaneous updates uses step \(k\):
\[
\begin{aligned}
 \widehat a_{k+1}^{(2)}
  &=\widehat a_k^{(2)}+\eta\widehat\delta_k^{(2)},\\
 \widehat M_{k+1}^{(2)}
  &=\widehat M_k^{(2)}
      +\eta\widehat\delta_k^{(2)}(\widehat h_k^{(1)})^{\mathsf T}/n,\\
 \widehat M_{k+1}^{(3)}
  &=\widehat M_k^{(3)}
      +\eta\widehat\delta_k^{(3)}(\widehat h_k^{(2)})^{\mathsf T}/n,\\
 \widehat R_{k+1}^{(1)}
  &=\widehat R_k^{(1)}
      +\eta(\widehat M_k^{(2)})^{\mathsf T}\widehat\delta_k^{(2)},\\
 \widehat W_{k+1}^{(4)}
  &=\widehat W_k^{(4)}+\eta\widehat h_k^{(3)},\\
 \widehat x_{k+1}^{(1)}
  &=(1-\eta/\varepsilon)\widehat x_k^{(1)}
       +(\eta/\varepsilon)
       [x_0^{(1)}+\widehat T_k^{(2)}+\widehat R_k^{(1)}],\\
 \widehat z_{k+1}^{(2)}
  &=(1-\eta/\varepsilon)\widehat z_k^{(2)}
       +(\eta/\varepsilon)
       [\widehat F_k^{(2)}+\widehat M_k^{(2)}\widehat h_k^{(1)}],\\
 \widehat z_{k+1}^{(3)}
  &=(1-\eta/\varepsilon)\widehat z_k^{(3)}
       +(\eta/\varepsilon)
       [\widehat F_k^{(3)}+\widehat M_k^{(3)}\widehat h_k^{(2)}].
\end{aligned}
 \tag{7}
\]
Initially \(\widehat a^{(2)},\widehat R^{(1)},\widehat M^{(2)},
\widehat M^{(3)}\) are zero,
\(\widehat x_0^{(1)}=x_0^{(1)}\), and
\(\widehat W_0^{(4)}=W_0^{(4)}\).
Allow warmup errors satisfying
\[
 d_0:=\frac{\|\widehat z_0^{(2)}-z_0^{(2)}\|_2+
                 \|\widehat z_0^{(3)}-z_0^{(3)}\|_2}{\sqrt n}\le1.
 \tag{8}
\]
Then a constant \(C_{S,M,R}\), independent of \(n,\eta,\varepsilon,b,d_0\)
and of the particular map in (1), satisfies
\[
\begin{split}
 \max_{0\le k\le N}\bigg\{
 &\frac{\|\widehat x_k^{(1)}-x^{(1)}(s_k)\|_2+
          \|\widehat z_k^{(2)}-z^{(2)}(s_k)\|_2+
          \|\widehat z_k^{(3)}-z^{(3)}(s_k)\|_2}{\sqrt n}\\
 &+\frac{\|\widehat a_k^{(2)}-a^{(2)}(s_k)\|_2+
          \|\widehat R_k^{(1)}-R^{(1)}(s_k)\|_2+
          \|\widehat W_k^{(4)}-W^{(4)}(s_k)\|_2}{\sqrt n}\\
 &+\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}
   +\|\widehat M_k^{(3)}-M^{(3)}(s_k)\|_{\rm F}\bigg\}
 \le C_{S,M,R}(\varepsilon+\eta+b+d_0).
\end{split}
 \tag{9}
\]
Thus there is no \(\exp(C/\varepsilon)\) stability loss here.
The constant is not claimed uniform as \(R\) increases.

## Uniform bounds and reference quadrature

Write \(c=\pi/2\) and \(T=S+1\). For either the reference or the
recursion, the readout coordinate bound is \(1+cT\), since each
readout derivative or increment is bounded by \(c\).
Consequently the normalized size of \(\delta^{(3)}\) is bounded
by \(1+cT\). The rank-one inequality
\(\|uv^{\mathsf T}/n\|_{\rm F}=\|u\|_2\|v\|_2/n\)
bounds \(\|M^{(3)}\|_{\rm F}\) and \(\|\widehat M^{(3)}\|_{\rm F}\)
by \(cT(1+cT)\).
Equation (5), (6), and the initial operator bound give
\(\|\widehat q_k^{(2)}\|_2/\sqrt n\le C_{S,M}\);
the same estimate, without query error, holds for the reference.
Domination in (1) gives the bound for both \(\delta^{(2)}\).
Their integrals and rank updates bound \(a^{(2)},M^{(2)},R^{(1)}\)
and their hatted versions, with vector norms divided by \(\sqrt n\)
and matrix Frobenius norms, by \(C_{S,M}\).
This reasoning is sequential: no state-error bound has been used.

The filter coefficient \(\eta/\varepsilon\) is in \([0,1]\).
Thus (7) bounds \(\|\widehat x^{(1)}-x_0^{(1)}\|_2/\sqrt n\)
by the maximum size of its bounded targets, and bounds the two
hatted preactivations similarly. Both their initial normalized sizes
are at most \(Mc+d_0\), by the initial operator bound and (8).
All these bounds are \(C_{S,M}\). The reference preactivations
are bounded by the two trained operator norms times \(c\).

The reference field is locally Lipschitz at each finite \(n\):
\(\tau\) is Lipschitz, the other coordinate functions are smooth,
and its products are locally Lipschitz in finitely many parameters.
The preceding polynomial readout and trained-matrix bounds prevent
escape. Its bottom derivative has normalized size at most
\(\|W^{(2)}\|_{\rm op}\|\delta^{(2)}\|_2/\sqrt n\),
which also prevents bottom escape. Hence its unique local solution
continues throughout \([0,T]\).

The reference velocities \(x^{(1)\prime},z^{(2)\prime},
z^{(3)\prime},h^{(1)\prime},h^{(2)\prime},h^{(3)\prime}\)
have normalized size bounded by \(C_{S,M}\).
For example,
\[
 x^{(1)\prime}=(W^{(2)})^{\mathsf T}\delta^{(2)},\qquad
 h^{(1)\prime}=\phi'(z^{(1)})^2\odot
                       (W^{(2)})^{\mathsf T}\delta^{(2)},
\]
\[
 z^{(2)\prime}
 =\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
       +W^{(2)}h^{(1)\prime},\qquad
 z^{(3)\prime}
 =\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
       +W^{(3)}h^{(2)\prime}.
 \tag{10}
\]
Use \(|\phi'|\le1\) and the established bounds.
Also
\[
 \delta^{(3)\prime}
 =h^{(3)}\odot\phi'(z^{(3)})
       +W^{(4)}\odot\phi''(z^{(3)})\odot z^{(3)\prime},
\]
\[
 q^{(2)\prime}
 =h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
       +(W^{(3)})^{\mathsf T}\delta^{(3)\prime}.
 \tag{11}
\]
These have the same normalized bounds because \(|\phi''|\le2\)
and the readout coordinates are bounded.
For the possibly nondifferentiable clipping, the difference quotient
bound from (1), followed by (10)--(11), gives
\[
 \frac{\|\delta^{(2)}(s)-\delta^{(2)}(t)\|_2}{\sqrt n}
 \le \frac{\|q^{(2)}(s)-q^{(2)}(t)\|_2}{\sqrt n}
       +2R\frac{\|z^{(2)}(s)-z^{(2)}(t)\|_2}{\sqrt n}
 \le C_{S,M,R}|s-t|.
 \tag{12}
\]
All five reference slow right sides
\[
 \delta^{(2)},\quad
 \delta^{(2)}(h^{(1)})^{\mathsf T}/n,\quad
 \delta^{(3)}(h^{(2)})^{\mathsf T}/n,\quad
 (M^{(2)})^{\mathsf T}\delta^{(2)},\quad h^{(3)}
 \tag{13}
\]
are therefore time-Lipschitz with constant \(C_{S,M,R}\) in their
respective norms. For a product, subtract one factor at a time and
use the uniform bounds above and the rank-one inequality.
Integrating its difference from the left endpoint over one step
gives a quadrature error at most \(C_{S,M,R}\eta^2/2\)
for each equation in (13).

## Filter contraction and the slow-state error

Let \(E_k\) be the sum of the last five errors in (9), namely
those in \(a^{(2)},M^{(2)},M^{(3)},R^{(1)},W^{(4)}\), and put
\(D_k=\max_{0\le j\le k}E_j\).
Let \(A_k,B_k,C_k\) be the normalized errors in
\(x^{(1)},z^{(2)},z^{(3)}\), respectively; these are nonnegative
scalars, not matrices. Initially \(E_0=A_0=0\) and \(B_0+C_0=d_0\).
The maps \(F^{-1}\) and \(\phi\circ F^{-1}\) are 1-Lipschitz,
because \(F'\ge1\) and
\((\phi\circ F^{-1})'=(\phi'\circ F^{-1})^2\le1\).

For \(p=\eta/\varepsilon\), (4)--(7) and the reference velocity
bound give
\[
 A_{k+1}\le(1-p)A_k+p(ME_k+E_k+b)+C_{S,M}\eta.
 \tag{14}
\]
The last term is the reference increment
\(x^{(1)}(s_{k+1})-x^{(1)}(s_k)\); its reference target at step
\(k\) equals \(x^{(1)}(s_k)\) exactly, not its next value.
Iterating (14) and using
\(\sum_{j=0}^{k-1}p(1-p)^j\le1\) gives
\[
 \max_{j\le k}A_j\le C_{S,M}(D_k+b+\varepsilon).
 \tag{15}
\]
Here \(\eta\sum_{j\ge0}(1-p)^j=\eta/p=\varepsilon\);
this is why there is no inverse-filter exponential.

Subtract the two layer-two targets. Their normalized difference is
at most
\[
 (M+\|\widehat M_k^{(2)}\|_{\rm op})A_k
       +c\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}+b.
\]
In this expression use the decomposition with the hatted matrix on
the activation difference and the reference activation on the matrix
difference. The same geometric-sum argument and (10) yield
\[
 \max_{j\le k}B_j
 \le B_0+C_{S,M}\big(\max_{j\le k}A_j+D_k+b+\varepsilon\big).
 \tag{16}
\]
For layer three replace \(A_k,M^{(2)}\) by \(B_k,M^{(3)}\):
\[
 \max_{j\le k}C_j
 \le C_0+C_{S,M}\big(\max_{j\le k}B_j+D_k+b+\varepsilon\big).
 \tag{17}
\]
The feedforward order of (15)--(17) gives, without a circular
instantaneous estimate,
\[
 \max_{j\le k}(A_j+B_j+C_j)
 \le C_{S,M}(D_k+b+\varepsilon+d_0).
 \tag{18}
\]

The ordinary top query difference is bounded by
\[
 \frac{\|\widehat q_k^{(2)}-q^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b.
 \tag{19}
\]
Indeed the top backward difference is at most the readout error
plus \(2(1+cT)C_k\); expand the two factors in
\((W^{(3)}_0+\widehat M^{(3)})^{\mathsf T}\widehat\delta^{(3)}\)
and then add the reverse query error. The bounded clipping gives
\[
 \frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b+2RB_k.
 \tag{20}
\]
Subtracting each slow right side in (13), one factor at a time,
therefore bounds its difference by
\(C_{S,M,R}(E_k+A_k+B_k+C_k+b)\).
For the memory right side specifically, use
\[
 \frac{\|(\widehat M_k^{(2)})^{\mathsf T}\widehat\delta_k^{(2)}
              -(M^{(2)}(s_k))^{\mathsf T}\delta^{(2)}(s_k)\|_2}{\sqrt n}
 \le
 \|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}
       \frac{\|\widehat\delta_k^{(2)}\|_2}{\sqrt n}
 +\|M^{(2)}(s_k)\|_{\rm op}
       \frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}(s_k)\|_2}{\sqrt n}.
 \tag{21}
\]
Thus the full returned memory is included.

The quadrature estimate after (13) and (18) imply
\[
 E_{k+1}\le E_k+
 C_{S,M,R}\eta(D_k+b+\varepsilon+d_0+\eta).
 \tag{22}
\]
Summing and maximizing,
\[
 D_k\le C_{S,M,R}(S+1)(b+\varepsilon+d_0+\eta)
       +C_{S,M,R}\eta\sum_{j<k}D_j.
 \tag{23}
\]
If \(H=C_{S,M,R}(S+1)(b+\varepsilon+d_0+\eta)\) and
\(L=C_{S,M,R}\), induction on (23) gives
\(D_k\le H(1+L\eta)^k\le H e^{L(S+1)}\).
This proves (9) together with (18).

## What this bridge does and does not remove

For a warmup of the form
\[
 \widehat z_0^{(2)}=W_0^{(2)}h_0^{(1)}+e_0^{(2)},\qquad
 \widehat z_0^{(3)}=W_0^{(3)}\phi(\widehat z_0^{(2)})+e_0^{(3)},
\]
one has \(d_0\le (1+M)\|e_0^{(2)}\|_2/\sqrt n+
\|e_0^{(3)}\|_2/\sqrt n\). Thus vanishing warmup errors are
covered, without pretending the noisy initial fields equal the
canonical fields. On any events where the rank companion establishes
\(b\to0\), its vanishing \(\varepsilon,\eta\) gives (9) for every
fixed clipping satisfying (1). The reference and the approximation
use the same original hidden matrices and the same prescribed tiny
readout; no comparison to a zero-readout evolved trajectory occurs.

One may reconstruct the forward fields from the approximate raw
parameters instead of from the registers. For example their layer-two
constraint discrepancy is bounded by
\[
 \frac{\|\widehat z_k^{(2)}
 -(W_0^{(2)}+\widehat M_k^{(2)})
      \phi(F^{-1}(\widehat x_k^{(1)}))\|_2}{\sqrt n}
 \le B_k+C_{S,M}(A_k+E_k).
 \tag{24}
\]
The layer-three discrepancy then follows using (24) and the bounded
trained operator norms. Hence the register constraint error also
vanishes under (9); it is not silently set to zero in (7).

For the uncut map \(\tau(v)=v\), (20) is not available with a fixed
constant \(R\). Its exact replacement retains
\[
 [\phi'(\widehat z_k^{(2)})-\phi'(z^{(2)}(s_k))]
       \odot q^{(2)}(s_k).
 \tag{25}
\]
The normalized Euclidean bound on \(q^{(2)}\) alone does not control
this term by \(B_k\), uniformly in width. Small query forcing,
vanishing filter scale, and causal low-rank histories do not discharge
that missing stability step. No uniformity as \(R\to\infty\), uncut
population existence, restartability, or exact raw-GD convergence is
proved here.

The estimate concerns states and the explicitly bounded clipped
queries in (19)--(20). Derivatives of the filter registers have a
factor \(1/\varepsilon\); (9) alone does not imply convergence of
those derivatives. All hidden velocity/kernel and physical-clock
claims of the requested theorem must still be justified separately.
No numerical experiment or new external source theorem is used.
