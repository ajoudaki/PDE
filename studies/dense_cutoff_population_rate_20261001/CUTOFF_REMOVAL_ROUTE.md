# Backward-clipped dense flow: uniform fitting and population cutoff removal

Status: proved candidate; internal check pending. This route uses the population
construction and Gaussian carrier bound supplied by `paper/proof_alltime.tex`.
This note does not assert a finite-width concentration rate. Its conclusions
hold at every fixed finite depth and for the activation class in the manuscript.

The useful fact is that clipping changes the hidden updates but leaves the
readout update unchanged. The resulting residual matrix is a mixed pairing of
true derivatives and clipped update directions. It need not be symmetric or
positive semidefinite. Nevertheless, in the small-label regime its hidden
contribution has operator norm of order the squared total residual activity.
The initial readout-feature gap therefore gives exponential fitting uniformly
in the clipping cap. Comparing this fitted flow with the fitted dense reference
then costs an exponential linear in the cap; the dense population's Gaussian
carrier tails absorb that cost.

## 1. Model, cutoff and precise conclusions

Write \(v_a=x_a/\sqrt d\), \(a=1,\ldots,m\), and

\[
 z_a^{(1)}=W^{(1)}v_a,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
 h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
 f_a=\frac{w^\top h_a^{(L)}}n.
\]

Here \(W^{(1)}\in\mathbb R^{n\times d}\), the hidden matrices are
\(n\times n\), and \(w\in\mathbb R^n\). Define

\[
 r_a=f_a-y_a,\qquad \rho=\|r\|_m,
 \qquad \|r\|_m^2=\frac1m\sum_a r_a^2,
 \qquad Y=\|y\|_m.
\]

Assume \(w(0)=0\), and, at each layer,

\[
 \phi_\ell\in C^1(\mathbb R),\qquad
 |\phi_\ell(0)|\le a_0,\qquad
 \|\phi_\ell'\|_\infty\le s,\qquad
 \operatorname{Lip}(\phi_\ell')\le j.
\]

Activation values need not be bounded. No assumption beyond fixed finite
depth is made about \(L\).

Choose one even smooth function \(\eta:\mathbb R\to[0,1]\) equal to one
on \([-1,1]\) and zero outside \((-2,2)\). For \(M>0\), set

\[
 \chi_M(u)=\int_0^u\eta(v/M)\,dv.
\]

Then \(\chi_M\) is smooth and odd, equals the identity on \([-M,M]\),
is constant on each of the two rays outside \([-2M,2M]\), and satisfies

\[
 |\chi_M(u)|\le\min\{|u|,2M\},\qquad
 |\chi_M(u)-\chi_M(v)|\le|u-v|,\qquad
 |\chi_M(u)-u|\le |u|\mathbf1_{\{|u|>M\}}.       \tag{1}
\]

All finite clipping operations below act coordinatewise. At the current
parameter state, define the **clipped update responses** recursively by

\[
 \begin{aligned}
 \delta_a^{(L),M}
   &=\phi_L'(z_a^{(L)})\odot\chi_M(w),\\
 \delta_a^{(\ell),M}
   &=\phi_\ell'(z_a^{(\ell)})\odot
     \chi_M\!\left(W^{(\ell+1)\top}
                         \delta_a^{(\ell+1),M}\right),\quad \ell<L.
 \end{aligned}                                                    \tag{2}
\]

The actual auxiliary algorithm is

\[
 \begin{aligned}
 \dot W^{(1)}&=-\frac2m\sum_a r_a\delta_a^{(1),M}v_a^\top,\\
 \dot W^{(\ell)}&=-\frac2{nm}\sum_a
            r_a\delta_a^{(\ell),M}h_a^{(\ell-1)\top},\quad \ell\ge2,\\
 \dot w&=-\frac2m\sum_a r_a h_a^{(L)}.
 \end{aligned}                                                    \tag{3}
\]

The forward pass is unchanged. In particular, the true derivative of the
output still uses the **unclipped gradient responses**

\[
 \delta_a^{(L)}=\phi_L'(z_a^{(L)})\odot w,
 \qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
                   W^{(\ell+1)\top}\delta_a^{(\ell+1)}.           \tag{4}
\]

Thus (2) and (4) are different fields computed at the same state. They
must not be identified in the residual equation.

The corresponding population system has layer spaces
\(\mathcal H_\ell=L^2(\Omega_\ell)\), first weights
\(W^{(1)}\in L^2(\Omega_1;\mathbb R^d)\), readout
\(w\in\mathcal H_L\), and bounded operators
\(W^{(\ell)}:\mathcal H_{\ell-1}\to\mathcal H_\ell\).
The initial operators are fixed, and their learned increments are
Hilbert--Schmidt. Write its coordinates as \(Z,H,\Delta\); (2)--(4)
hold with the finite transpose replaced by the Hilbert adjoint, pointwise
products in place of \(\odot\), and

\[
 f_a=\mathbb E_L[wH_a^{(L)}],\qquad
 (U\otimes V)g=U\mathbb E[Vg],\qquad
 \dot W^{(\ell)}=-\frac2m\sum_a
                 r_a\Delta_a^{(\ell),M}\otimes H_a^{(\ell-1)}.
                                                                  \tag{5}
\]

The expectation in a rank-one operator is over its input layer. The
first-layer and readout updates retain the factors in (3).

**Uniform fitting proposition.** Suppose the finite initialization obeys

\[
 \max_{\ell\ge2}\|W_0^{(\ell)}\|_{\rm op}\le K_0,\quad
 \max_a\frac{\|W_0^{(1)}v_a\|_2}{\sqrt n}\le A_0,\quad
 \frac{\|W_0^{(1)}\|_F}{\sqrt n}\le C_0,\quad
 \Gamma_w(0):=\left(\frac{h_a^{(L)\top}h_b^{(L)}}{mn}\right)_{ab}
                      \succeq\lambda I_m.                         \tag{6}
\]

There exist \(Y_*>0\), \(\kappa>0\), and \(C<\infty\), depending
only on these fixed bounds, the activation bounds, depth and training
data, such that for \(Y\le Y_*\), every flow (3), for every \(M>0\),
has a unique global solution satisfying

\[
 \rho_M(t)\le Ye^{-\kappa t},\qquad
 \int_0^\infty\rho_M(t)\,dt\le Y/\kappa,                           \tag{7}
\]

\[
 \begin{aligned}
 &\sup_t\left\{\frac{\|w_M(t)\|_2}{\sqrt n}
       +\max_{a,\ell}\frac{\|\delta_{a,M}^{(\ell)}(t)\|_2
                 +\|\delta_{a,M}^{(\ell),M}(t)\|_2}{\sqrt n}\right\}
       \le CY,\\
 &\sup_t\left\{\frac{\|W_M^{(1)}(t)-W_0^{(1)}\|_F}{\sqrt n}
         +\sum_{\ell=2}^L\|W_M^{(\ell)}(t)-W_0^{(\ell)}\|_F\right\}
       \le CY^2.                                                  \tag{8}
 \end{aligned}
\]

Parameters converge as \(t\to\infty\). The identical proposition holds
for the population system with RMS replaced by the stated \(L^2\) norms,
hidden Frobenius norms by Hilbert--Schmidt norms, and the population
version of (6). The constants and label threshold are independent of
\(n,M,t\). Finite-dimensional dense training is the same proposition
with \(\chi_M\) replaced by the identity; the population dense flow is
the one constructed in the supplied manuscript.

**Population cutoff-removal theorem.** Take the Gaussian population
construction of `paper/proof_alltime.tex`, its strictly positive initial
readout-feature Gram gap, and its small-label dense flow
\(\theta_D\). Use a common initialized-operator realization for
\(\theta_D\) and the solutions \(\theta_M\) of (5), as described below.
After decreasing the same fixed label threshold if necessary, there are
\(C,c>0\), independent of \(M\ge1\) and time, such that

\[
 \sup_{t\ge0}d(\theta_M(t),\theta_D(t))\le Ce^{-cM^2},              \tag{9}
\]

where

\[
 d(\theta,\widetilde\theta)
  =\|W^{(1)}-\widetilde W^{(1)}\|_{L^2(\Omega_1;\mathbb R^d)}
   +\sum_{\ell=2}^L\|W^{(\ell)}-\widetilde W^{(\ell)}\|_{\rm HS}
   +\|w-\widetilde w\|_{L^2(\Omega_L)}.                            \tag{10}
\]

In particular, for every probability law \(\mu\) with
\(\int\|x\|_2^2\,d\mu(x)<\infty\),

\[
 \left(\int\sup_{t\ge0}|f_\infty^M(t,x)-f_\infty(t,x)|^2
                  \,d\mu(x)\right)^{1/2}
       \le C_\mu e^{-cM^2}.                                      \tag{11}
\]

No time supremum of a random carrier is assumed sub-Gaussian. No tail
bound for the clipped trajectory is assumed.

## 2. Exact residual matrix and cap-uniform fitting

Differentiating the unchanged forward pass along (3), with (4) as the
actual derivative, gives

\[
 \dot r=-2B_Mr,                                                   \tag{12}
\]

\[
 \begin{aligned}
 (B_M)_{ab}=\frac1m\bigg[&
  \frac{h_a^{(L)\top}h_b^{(L)}}n
  +\frac{\delta_a^{(1)\top}\delta_b^{(1),M}}n\,v_a^\top v_b\\
  &+\sum_{\ell=2}^L
     \frac{\delta_a^{(\ell)\top}\delta_b^{(\ell),M}}n
     \frac{h_a^{(\ell-1)\top}h_b^{(\ell-1)}}n\bigg].            \tag{13}
 \end{aligned}
\]

Its row index is the output being differentiated; its column index is
the sample driving the update. In general this matrix is nonsymmetric.
The population formula replaces each normalized pairing by its same-layer
expectation. The readout contribution is exactly \(\Gamma_w\).

For the a priori estimate, stop at the first exit from the tube

\[
 \|W^{(\ell)}\|_{\rm op}<K_0+1\ (\ell\ge2),\qquad
 \max_a\|z_a^{(1)}\|_2/\sqrt n<A_0+1,
 \qquad S(t):=\int_0^t\rho(u)\,du<S_*.
\]

Set \(D_0=K_0+1\), \(F_1=a_0+s(A_0+1)\), and
\(F_\ell=a_0+sD_0F_{\ell-1}\). On this tube,
\(\|h_a^{(\ell)}\|_2/\sqrt n\le F_\ell\).
The readout update, Cauchy--Schwarz over samples, and \(w(0)=0\) give

\[
 \|w(t)\|_2/\sqrt n\le2F_L S(t).
\]

Both backward recursions then give

\[
 \max_{a,\ell}\frac{\|\delta_a^{(\ell)}\|_2
                      +\|\delta_a^{(\ell),M}\|_2}{\sqrt n}
       \le CS(t).                                                \tag{14}
\]

For the clipped recursion this uses solely
\(|\chi_M(u)|\le|u|\). It never uses the cap \(2M\).
The rank-one Frobenius identity
\(\|uv^\top/n\|_F=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n)\)
and (3) now imply

\[
 \frac{\|\dot W^{(1)}\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F
       \le CS(t)\rho(t),\qquad
 \|\dot w\|_2/\sqrt n\le C\rho(t).                             \tag{15}
\]

Since \(\int_0^t S\rho=S(t)^2/2\), hidden and first-layer
displacements are bounded by \(CS(t)^2\). Forward subtraction through
bounded operators and bounded slopes gives

\[
 \max_{a,\ell}\frac{\|h_a^{(\ell)}(t)-h_a^{(\ell)}(0)\|_2}
                         {\sqrt n}\le CS(t)^2,
 \qquad
 \|\Gamma_w(t)-\Gamma_w(0)\|_{\rm op}\le CS(t)^2.                \tag{16}
\]

For example, subtract a hidden forward action as
\((W(t)-W_0)h(0)+W(t)(h(t)-h(0))\). The first-layer difference
is bounded by its Frobenius displacement times \(\|v_a\|_2\).
For (16), expand a Gram entry into two feature differences and use the
feature RMS bounds. A matrix with entries bounded by \(b/m\) has
operator norm at most \(b\), as its Frobenius norm is at most \(b\).

The same entry estimate applied to (13) and (14) gives

\[
 \|B_M-\Gamma_w\|_{\rm op}\le CS(t)^2.                           \tag{17}
\]

Hence, writing \(\operatorname{sym}B=(B+B^\top)/2\),

\[
 \operatorname{sym}B_M\succeq
     \bigl(\lambda-CS(t)^2\bigr)I_m,\qquad
 \|B_M\|_{\rm op}\le G                                           \tag{18}
\]

whenever \(S_*\le1\), for a fixed \(G\).
Choose \(S_*=4Y/\lambda\) and then \(Y_*\) small enough that
the physical displacements lie strictly within the tube and
\(CS_*^2\le\lambda/2\). At positive residual, (12) gives

\[
 \dot\rho
  =-2\frac{\langle r,(\operatorname{sym}B_M)r\rangle_m}{\rho}
  \le-\lambda\rho.
\]

Consequently \(\rho(t)\le Ye^{-\lambda t}\) and
\(S(t)\le Y/\lambda=S_*/4\). This excludes both stopping
boundaries. The lower inequality
\(\dot\rho\ge-2G\rho\) also gives
\(\rho(t)\ge Ye^{-2Gt}\) when \(Y>0\); no finite-time division by a
zero residual has been used. When \(Y=0\), the initial state is stationary.

At fixed finite \(n,M\), the vector field is locally Lipschitz, and
the parameter bounds exclude a finite maximal existence time. Thus (7)
and (8) hold, with \(\kappa=\lambda\) for this choice of margins.
Integrating (15) on \([t,\infty)\) proves finite total parameter
variation and convergence. The limiting training residual is zero.
The extra full first-layer bound in (6) gives the uniform whole-input
bound used later; it was not needed to preserve the training Gram.

Every estimate just proved carries over verbatim to the population norm
using \(\|U\otimes V\|_{\rm HS}=\|U\|_2\|V\|_2\). The next section
supplies the population local wellposedness needed for that continuation.

## 3. A common population action and wellposed clipped dynamics

There are two source inputs from `paper/proof_alltime.tex`:

1. The fixed Gaussian computation lemma and the following construction
   of bounded initialized operators with their actual adjoints on the
   generated layer spaces. This permits finite unions of computations
   sharing the same initialized arrays, including continuous coordinate
   maps of at most linear growth.
2. The strong dense population flow, with
   \(\sup_{t\ge0,a,\ell}\mathbb E\exp(c_0|P_{a,D}^{(\ell)}(t)|^2)
   \le C_0'\), where
   \(P_{a,D}^{(L)}=w_D\) and
   \(P_{a,D}^{(\ell)}=W_D^{(\ell+1)*}\Delta_{a,D}^{(\ell+1)}\).
   This is the bound labeled `eq:at-pop-gaussian`, passed to the dense
   strong solution, and is a bound on each time marginal.

The present note uses these as supplied manuscript results, not as a
new quantitative finite-width theorem.

For a common realization, include in the manuscript's countable family
of same-array programs all the dense approximating programs, all fixed
Euler programs with rational positive clipping caps and rational finite
meshes, their finite unions, the first-layer Gaussian row coordinates,
and a countable dense set of passive input queries. Close this family
under the forward and reverse initialized-matrix calls, rational linear
combinations, and a countable family of bounded smooth functions dense on
compact sets for each finite tuple dimension. Repeating
these closures countably many times still gives a countable family.
The fixed-program lemma gives consistent joint layer laws. The finite
inequalities

\[
 \|W_0v\|_2/\sqrt n\le K_0\|v\|_2/\sqrt n,
 \qquad u^\top W_0v/n=(W_0^\top u)^\top v/n
\]

pass to every generated finite span and then to its completion. The
bounded smooth coordinate closure makes that completion the \(L^2\)
space of the generated sigma field. Thus each hidden link has one
bounded action \(W_0^{(\ell)}\) and its Hilbert adjoint on these
spaces. Both flows use these same actions. This does not replace a
reverse action by an independent Gaussian map.

Each real \(M>0\) then defines an ODE on the fixed Banach space

\[
 \mathcal B=L^2(\Omega_1;\mathbb R^d)
       \times\prod_{\ell=2}^L
          \mathrm{HS}(\mathcal H_{\ell-1},\mathcal H_\ell)
       \times\mathcal H_L,                                      \tag{19}
\]

with state coordinates consisting of first weights, hidden increments,
and readout. It is not necessary to put uncountably many independent
programs in the initial construction: all pointwise clipped fields are
already elements of the fixed generated \(L^2\) spaces, and the bounded
operators act on their whole completions.

On each bounded subset of (19), forward subtraction is Lipschitz in
the sum norm (10). For a backward gate, (1) gives

\[
 \|\phi_\ell'(Z)\chi_M(P)-\phi_\ell'(\widetilde Z)
                                    \chi_M(\widetilde P)\|_2
 \le 2jM\|Z-\widetilde Z\|_2+s\|P-\widetilde P\|_2.              \tag{20}
\]

For a carrier, the difference of two adjoint actions is bounded by
the operator norm times the response difference plus the hidden
Hilbert--Schmidt difference times the reference response norm.
Descending through the finite depth proves local Lipschitz continuity
of all clipped responses and hence of the rank-one update vector field.
The readout and residual pairings are locally Lipschitz by
Cauchy--Schwarz. The ODE therefore has a unique local \(C^1\) solution;
the Lipschitz constant on a bounded state set can depend on \(M\).

The scalar residual identity (12) is valid on this solution despite
the absence of full Fréchet differentiability of a nonlinear activation
as an \(L^2\)-to-\(L^2\) map. Indeed, along an \(L^2\)-differentiable
curve \(Z(t)\), the bounded derivative of \(\phi\) gives

\[
 \frac{d}{dt}\phi(Z(t))=\phi'(Z(t))\dot Z(t)\quad\hbox{in }L^2.
\]

To verify this, write
\(Z(t+h)=Z(t)+h\dot Z(t)+o_{L^2}(h)\). Lipschitz continuity of
\(\phi\) controls the last term. For the fixed direction
\(\dot Z(t)\), the scalar difference quotient converges pointwise
and is bounded in absolute value by \(s|\dot Z(t)|\), so dominated
convergence gives the \(L^2\) derivative. Applying this argument through
the forward recursion and differentiating the \(L^2\) pairings gives
precisely (12)--(13).

The population fitting proof of Section 2 now applies. Its uniform
state bounds place the entire trajectory in one bounded subset of
(19). For fixed \(M\), the vector field and its Lipschitz constant are
bounded there, so a solution with finite maximal endpoint is Cauchy
at that endpoint and extends from its limit. This proves global
existence, uniqueness, fitting and parameter convergence for the clipped
population. Its construction needs no extra activation regularity.

For completeness, this is the population corresponding to the clipped
finite algorithm, for fixed \(M\). On any fixed horizon, approximate
its solution by a finite Euler program, freeze that program's scalar
coefficients at their population values, and evaluate it on the finite
initialized arrays. The fixed-program lemma transfers all of its
finitely many normalized pairings. Rank-one recomputation errors are
finite sums of those pairing errors multiplied by bounded RMS fields.
At fixed \(M\), (20) makes all recomputation errors tend to zero in RMS.
The vector-field Lipschitz bound is independent of width on the common
physical tube. Ordinary integral comparison therefore bounds the
finite-flow/proxy discrepancy on \([0,T]\) by
\(C_{M,T}(h+o_{\mathbb P}(1))\), where \(h\) is the fixed mesh size.
Take width to infinity first and mesh to zero second. This identifies
the fixed-\(M\) finite population limit on finite lists of inputs.
The fitting speed bounds make the variation after \(T\) at most
\(Ce^{-\kappa T}(1+\|x\|_2/\sqrt d)\). A finite input net and the
whole-input bound in Section 5 then give qualitative all-time convergence
for every fixed finite-second-moment query law. This paragraph supplies
identification only; it supplies no numerical width rate.

## 4. Activity-weighted comparison with the dense reference

All population quantities in this section are on the common spaces.
At the clipped state \(\theta_M(t)\), write
\(\Delta_{a,M}^{(\ell),M}\) for the response used in its update and
\(\Delta_{a,M}^{(\ell)}\) for its true gradient response. At the dense
state \(\theta_D(t)\), write \(\Delta_{a,D}^{(\ell)}\).
The subscript \(M\) labels a trajectory; the superscript \(M\) labels
the clipped recursion, so these two uses are not interchangeable.
Let

\[
 d(t)=d(\theta_M(t),\theta_D(t)),\qquad
 u(t)=r_M(t)-r_D(t),\qquad
 H_D(M,t)=\sum_{\ell=1}^L\max_a
       \|P_{a,D}^{(\ell)}(t)
                     \mathbf1_{\{|P_{a,D}^{(\ell)}(t)|>M\}}\|_2,
\]

\[
 Z_D(M;t)=\int_0^t\rho_D(s)H_D(M,s)\,ds,
 \qquad Z_D(M)=Z_D(M;\infty).                                  \tag{21}
\]

The fitting proposition gives the same fixed operator, feature and
response norm bounds for both paths. Forward subtraction first gives

\[
 \max_{a,\ell}\bigl(\|Z_{a,M}^{(\ell)}-Z_{a,D}^{(\ell)}\|_2
          +\|H_{a,M}^{(\ell)}-H_{a,D}^{(\ell)}\|_2\bigr)
           \le Cd(t).                                           \tag{22}
\]

For the clipped response difference, the exact scalar decomposition
at each layer is

\[
 \begin{aligned}
 \phi'(Z_M)\chi_M(P_M)-\phi'(Z_D)P_D
  ={}&\phi'(Z_M)[\chi_M(P_M)-\chi_M(P_D)]\\
    &+[\phi'(Z_M)-\phi'(Z_D)]\chi_M(P_D)\\
    &+\phi'(Z_D)[\chi_M(P_D)-P_D].
 \end{aligned}                                                   \tag{23}
\]

Here \(P_M=w_M\) at the top, and
\(P_M=W_M^{(\ell+1)*}\Delta_{a,M}^{(\ell+1),M}\) lower down.
Introduce a comparison threshold \(R\ge1\), independent of the algorithm's
cap \(M\ge1\). By \(|\chi_M(P_D)|\le|P_D|\), the three terms in (23)
have \(L^2\) norms at most

\[
 s\|P_M-P_D\|_2,
 \qquad jR\|Z_M-Z_D\|_2
        +2s\|P_D\mathbf1_{\{|P_D|>R\}}\|_2,
 \qquad s\|P_D\mathbf1_{\{|P_D|>M\}}\|_2.
\]

For a lower carrier,

\[
 \|P_M-P_D\|_2
  \le C\|\Delta_{a,M}^{(\ell+1),M}
                    -\Delta_{a,D}^{(\ell+1)}\|_2
       +CY\|W_M^{(\ell+1)}-W_D^{(\ell+1)}\|_{\rm HS}.
\]

Descending induction therefore yields

\[
 \max_{a,\ell}\|\Delta_{a,M}^{(\ell),M}
                    -\Delta_{a,D}^{(\ell)}\|_2
       \le C\{(1+R)d(t)+H_D(R,t)+H_D(M,t)\}.                    \tag{24}
\]

The same estimate holds for the true gradient response at the clipped
state. In that recursion, use instead

\[
 \|[\phi'(Z_M)-\phi'(Z_D)]P_D\|_2
  \le jR\|Z_M-Z_D\|_2
       +2s\|P_D\mathbf1_{\{|P_D|>R\}}\|_2.                     \tag{25}
\]

All other terms are the bounded-gate adjoint differences just displayed.
The factor \(R\) enters additively at each fixed layer; propagating a
response difference through another layer multiplies it only by a fixed
operator-and-slope bound. In particular, no \(R^L\) is introduced.
Only the final term of (23), the actual discarded carrier, uses \(M\).

Let \(B_M(t)\) be the mixed residual matrix (13) at \(\theta_M(t)\),
and let \(\Gamma_D(t)\) be the ordinary dense tangent Gram. Expanding
each pairing in (13), using (22), (24), (25), and the uniform norms gives

\[
 \|B_M(t)-\Gamma_D(t)\|_{\rm op}
     \le C\{(1+R)d(t)+H_D(R,t)+H_D(M,t)\}.                      \tag{26}
\]

For example, a backward pairing is expanded as
\(\langle A,B\rangle-\langle A_D,B_D\rangle
=\langle A-A_D,B\rangle+\langle A_D,B-B_D\rangle\).
The true response is used in \(A\), and the clipped update response in
\(B\). Its feature-pairing multiplier is handled by the same two-term
expansion. This verifies (26) without replacing the mixed matrix by a
gradient Gram.

Subtracting the two **exact** residual equations gives

\[
 \dot u=-2B_Mu-2(B_M-\Gamma_D)r_D.                               \tag{27}
\]

By the cap-uniform lower bound on \(\operatorname{sym}B_M\),

\[
 D^+\|u(t)\|_m
    \le-\kappa_0\|u(t)\|_m
       +C\rho_D(t)\{(1+R)d(t)+H_D(R,t)+H_D(M,t)\},              \tag{28}
\]

for one fixed \(\kappa_0>0\). At a zero of \(u\), this follows from
the upper right derivative of its norm, or from regularizing the norm
by \((\|u\|_m^2+\varepsilon^2)^{1/2}\) and sending
\(\varepsilon\downarrow0\). As \(u(0)=0\), integration gives

\[
 \int_0^t\|u(s)\|_m\,ds
   \le C\left[(1+R)\int_0^t\rho_D(s)d(s)\,ds
                            +Z_D(R;t)+Z_D(M;t)\right].         \tag{29}
\]

For the parameter updates, the exact readout subtraction is

\[
 \dot w_M-\dot w_D
   =-\frac2m\sum_a
       \{u_aH_{a,M}^{(L)}
          +r_{a,D}(H_{a,M}^{(L)}-H_{a,D}^{(L)})\}.                \tag{30}
\]

At a hidden link, the rank-one product subtraction is

\[
 \begin{aligned}
 r_{a,M}\Delta_{a,M}^{(\ell),M}\otimes H_{a,M}^{(\ell-1)}
  -r_{a,D}\Delta_{a,D}^{(\ell)}\otimes H_{a,D}^{(\ell-1)}
  ={}&u_a\Delta_{a,M}^{(\ell),M}\otimes H_{a,M}^{(\ell-1)}\\
   &+r_{a,D}(\Delta_{a,M}^{(\ell),M}
                  -\Delta_{a,D}^{(\ell)})\otimes H_{a,M}^{(\ell-1)}\\
   &+r_{a,D}\Delta_{a,D}^{(\ell)}\otimes
                  (H_{a,M}^{(\ell-1)}-H_{a,D}^{(\ell-1)}).
 \end{aligned}                                                   \tag{31}
\]

The first layer has the analogous two-term identity with fixed \(v_a\).
Use the rank-one norm identity, (22) and (24) in (30)--(31), and integrate
from the common initial state. This gives

\[
 d(t)\le C\int_0^t\|u(s)\|_m\,ds
           +C\int_0^t\rho_D(s)
                    \{(1+R)d(s)+H_D(R,s)+H_D(M,s)\}\,ds.        \tag{32}
\]

Combining (29) and (32), and applying the integral Gronwall inequality
with the integrable coefficient \(C(1+R)\rho_D\), yields

\[
 \sup_{t\ge0}d(t)
   \le C\exp\left(C(1+R)\int_0^\infty\rho_D(s)\,ds\right)
                          [Z_D(R)+Z_D(M)]
   \le Ce^{KYR}[Z_D(R)+Z_D(M)].                                \tag{33}
\]

The last constant absorbs \(\exp(CY)\) for \(Y\le Y_*\).
For the Gronwall step at a terminal time \(t\), replace the
nondecreasing source \(Z_D(R;s)+Z_D(M;s)\) by its value at \(t\), apply the
integrating factor, and then take the supremum over \(t\). This
justifies the step without an assumption about the time monotonicity of
\(d\). No ratio of the two residual norms is introduced.

The source is weighted by the dense residual throughout. Thus there is
no unweighted integral of a marginal tail over an infinite interval.

## 5. Gaussian marginal tails and whole-input error

The supplied dense population bound states that for fixed positive
\(b,C_1\),

\[
 \sup_{t\ge0,a,\ell}
       \mathbb E\exp(b|P_{a,D}^{(\ell)}(t)|^2)\le C_1.
\]

For any variable satisfying this inequality,

\[
 \mathbb E[P^2\mathbf1_{\{|P|>M\}}]
   \le\left(\sup_{v\in\mathbb R}v^2e^{-bv^2/2}\right)
          e^{-bM^2/2}\mathbb E e^{bP^2}
   \le C e^{-bM^2/2}.
\]

Taking square roots and the finite layer/sample maximum gives

\[
 H_D(M,t)\le Ce^{-c_1M^2}\quad\hbox{for every }t\ge0,
 \qquad Z_D(M)\le CY e^{-c_1M^2}.                               \tag{34}
\]

This uses only each time marginal; the deterministic bound is uniform
over time. Choose \(R=M\) in (33), substitute (34), and use \(Y\le Y_*\):

\[
 \sup_t d(t)\le CY\exp(KY M-c_1M^2)
        \le C'\exp(-c_1M^2/2).
\]

For the last inequality, complete the square or maximize
\(KY_*M-c_1M^2/2\) over \(M\). This proves (9) with constants
independent of \(M\). The same argument and (29) also show

\[
 \int_0^\infty\|r_M-r_D\|_m\,dt\le Ce^{-cM^2}
\]

after decreasing \(c\), since a factor \(1+M\) is absorbed into a
Gaussian exponential.

For a general input \(x\in\mathbb R^d\), both first-weight norms
remain bounded in \(L^2(\Omega_1;\mathbb R^d)\), and the hidden
operator norms remain bounded. Therefore linear activation growth and
forward induction give

\[
 \|H^{(\ell)}(t,x)\|_2
      \le C(1+\|x\|_2/\sqrt d),
\]

\[
 \|H_M^{(\ell)}(t,x)-H_D^{(\ell)}(t,x)\|_2
      \le C(1+\|x\|_2/\sqrt d)d(t).
\]

At the first layer the difference is at most
\(s\|W_M^{(1)}-W_D^{(1)}\|_2\|x\|_2/\sqrt d\).
At every further layer subtract the operator action as in (22).
Finally,

\[
 f_\infty^M(t,x)-f_\infty(t,x)
    =\mathbb E[(w_M-w_D)H_M^{(L)}(t,x)]
       +\mathbb E[w_D(H_M^{(L)}(t,x)-H_D^{(L)}(t,x))],
\]

so Cauchy--Schwarz yields

\[
 \sup_{t\ge0}|f_\infty^M(t,x)-f_\infty(t,x)|
    \le Ce^{-cM^2}(1+\|x\|_2/\sqrt d).                          \tag{35}
\]

Squaring and integrating proves (11), with
\(C_\mu=C\{\int(1+\|x\|_2/\sqrt d)^2d\mu(x)\}^{1/2}\).
There is no exchange of a supremum and an integral. The same bound is
uniform on every bounded input set, and parameter convergence includes
the endpoint \(t=\infty\).

## 6. Finite-width consequence and limits of this route

The comparison in Section 4 also holds at finite width for two paths
with the same initialization satisfying (6). Replace population \(L^2\)
norms by normalized Euclidean norms, hidden Hilbert--Schmidt norms by
Frobenius norms, and set

\[
 Z_n(M)=\int_0^\infty\rho_{n,D}(t)
  \sum_{\ell=1}^L\max_a
   \frac{\|k_{a,D}^{(\ell)}(t)
                 \mathbf1_{\{|k_{a,D}^{(\ell)}(t)|>M\}}\|_2}
        {\sqrt n}\,dt.
\]

It gives the deterministic estimate

\[
 \sup_{t\ge0}d_n(\theta_{n,M}(t),\theta_{n,D}(t))
       \le Ce^{KYR}[Z_n(R)+Z_n(M)]\qquad(R,M\ge1).                \tag{36}
\]

and the corresponding whole-input bound with the factor
\(1+\|x\|_2/\sqrt d\). This proves that all three comparisons in
the cutoff strategy can use actual autonomous fitted trajectories,
rather than merely clipped fields evaluated along a different algorithm.

The supplied manuscript establishes only
\(Z_n(M)\le Ce^{-cM^2}+a_n\) simultaneously at integer thresholds,
with \(a_n\to0\) in probability and no numerical width rate. Setting
\(R=M\) in (36) gives

\[
 \sup_t d_n(\theta_{n,M},\theta_{n,D})
       \le Ce^{KYM}(e^{-cM^2}+a_n).
\]

The term \(e^{KYM}a_n\) cannot be discarded for a growing cap.
Thus this specialization does not prove strict root-width finite cutoff
removal. The independent threshold does give a stronger qualitative
consequence: for **every** deterministic \(M_n\to\infty\),

\[
 \sup_{t\ge0}d_n(\theta_{n,M_n}(t),\theta_{n,D}(t))
       \xrightarrow{\mathbb P}0.                               \tag{37}
\]

To prove it, fix an integer \(R\). The manuscript's simultaneous bound
and monotonicity, using \(\lfloor M_n\rfloor\) for a noninteger cap,
make the right side of (36) at most
\[
 Ce^{KYR}\{e^{-cR^2}+e^{-c\lfloor M_n\rfloor^2}+2a_n\}.
\]
First send \(n\) to infinity at this fixed \(R\), then send \(R\) to
infinity. Since \(e^{KYR-cR^2}\to0\), each positive discrepancy
threshold has violation probability tending to zero. The same result
holds in the all-time finite-second-moment query metric by the
whole-input estimate. This avoids an unjustified condition on the
unknown rate of \(a_n\), but it is still only qualitative.

Likewise, if a separate finite-to-population result for the clipped
algorithm has a constant growing like \(e^{CM}\), balancing the
Gaussian cutoff tail with \(M\asymp\sqrt{\log n}\) generally gives
\(n^{-1/2}\exp(O(\sqrt{\log n}))\), not a width-independent
constant times \(n^{-1/2}\).

What is complete here is the cap-uniform fitting theorem and the
all-time population removal error (11), including the unchanged readout,
the exact nonsymmetric residual matrix, common operator actions,
population wellposedness, and finite-second-moment query laws. Strict
root-width finite/population comparison still requires quantitative
finite-network tail control and a finite-to-population estimate with
sufficiently controlled cap dependence. No fitting or population-removal
obstruction remains after the stated reduction of the fixed label
threshold.
