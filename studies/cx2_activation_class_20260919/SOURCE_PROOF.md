# Orthogonal clocks with an unbounded readout: a source-control partial

Status: author-derived partial awaiting independent review, not a global theorem and not
established library material. This route does not close the requested
arbitrary-finite-horizon result for all nonaffine C1,1 activations with bounded
derivative. It closes a mesh-uniform source estimate conditional on one finite
response-row cap, gives an explicit sufficient scalar test for that cap, and
proves a reached-Euler-state obstruction to extending the bounded-readout
Hilbert-Lipschitz argument.

Scientific inputs were restricted to the supervisor's assignment and maintained
`docs/NOTATION.md`, `global_nonlinear.md` A, B.1, C.1–C.2,
C.4.7.1–C.4.7.5, `special_data_limits.md` III.F and the explicit conditional
tail/response obstructions, and `finite_dynamics.md` energy estimates. No
other study or another current route was read. No computation or training was
performed. The results below cover arbitrary fixed labels at the orthogonal
reference, including the required opposite-label pair (+1,-1).

## 1. Exact contract and equations

Let the fixed normalized inputs \(u_a=x_a/\sqrt d\), \(1\le a\le m\), be
orthonormal. The loss is the unhalved mean

\[
 \mathcal L=\sum_a p_a(f_a-y_a)^2,\qquad p_a=1/m.
\]

The proof also permits separately fixed positive weights of sum one. Stored
initialization variances are exactly \((1,1/n,1/n^2)\), mobilities are

\[
 (n,1,n),
\]

and the population initial readout is zero. The initial middle action \(A_0\)
and its actual adjoint are the common generated Gaussian actions of III.F.
Only \(K=A-A_0\) is Hilbert–Schmidt. Use separate neuron probability spaces
for the two layers. Write

\[
 z_a=w\cdot u_a,\quad h_a=\phi(z_a),\quad Z_a=Ah_a,\quad
 H_a=\phi(Z_a),\quad d_a=c\phi'(Z_a),\quad Q_a=A^*d_a,
 \quad f_a=E_2[cH_a].
\tag{1.1}
\]

Here \(d_a\) is the second-layer residual-free backward field; it is not a
sample dimension. The exact raw flow is

\[
 \dot w=-2\sum_a p_ar_a\phi'(z_a)Q_a u_a,\qquad
 \dot K=-2\sum_a p_ar_a d_a\otimes h_a,\qquad
 \dot c=-2\sum_a p_ar_aH_a.
\tag{1.2}
\]

The raw norm is the product of \(L^2(\Omega_1;\mathbb R^d)\), HS, and
\(L^2(\Omega_2)\) norms. On every existing strong physical path,

\[
 \mathcal L(t)+\int_0^t\|\dot\theta(s)\|_{\rm raw}^2ds=\mathcal L(0),
 \qquad
 \|\theta(t)-\theta(0)\|_{\rm raw}\le\sqrt{t\mathcal L(0)}.
\tag{1.3}
\]

Finite-width GF is global by this identity and finite-dimensional local
Lipschitzness. Neither (1.3) nor the ensuing raw/action bounds establishes
population existence or incoming-field tails.

First suppose \(\phi\in C^2\), and set

\[
 b=|\phi(0)|,\quad M=\|\phi'\|_\infty,\quad
 L=\|\phi''\|_\infty.
\]

Let \(J(s,g)\) solve \(J_s=\phi'(J)\), \(J(0,g)=g\). Boundedness and
Lipschitzness of the scalar vector field give a global solution and

\[
 |J(s,g)-J(t,g)|\le M|s-t|,\quad
 \partial_s\phi(J(s,g))=\phi'(J(s,g))^2.
\tag{1.4}
\]

Thus \(z_a=J(X_a,g_a)\), with \(g_a=w_0\cdot u_a\), and

\[
 \dot X_a=-2p_ar_aQ_a.
\tag{1.5}
\]

Equations (1.2),(1.5) are exactly equivalent on any strong path for which the
integrals exist: the scalar equation with its integrable coordinatewise
coefficient is unique, and Fubini follows from the \(L^2\) time bounds. No
division by \(\phi'\), monotonicity, or nonvanishing derivative is required.
The components of \(w\) orthogonal to all training inputs remain their full
initial Gaussian components. They must be retained for passive inputs.

## 2. Fixed clock programs and the exact source skeleton

Use an arbitrary positive mesh \(h_k\), with \(\sum_kh_k\le T\). For this
section the frozen controls \(v_{ka}\) are any deterministic numbers with

\[
 |v_{ka}|\le V,\qquad \gamma_{ka}=h_kp_av_{ka}.
\]

Actual physical controls are \(v_{ka}=-2r_{ka}\). The clock Euler program is

\[
 X_{a,k+1}=X_{a,k}+\gamma_{ka}Q_{ka},\quad
 c_{k+1}=c_k+\sum_a\gamma_{ka}H_{ka},\quad
 K_{k+1}=K_k+\sum_a\gamma_{ka}d_{ka}\otimes h_{ka}.
\tag{2.1}
\]

This is an auxiliary proof program. It is not exact raw Euler.

Assume its raw forward and backward RMS sizes are bounded by a known \(S\ge1\):

\[
 \|h_{ka}\|_2,\ \|H_{ka}\|_2,\ \|d_{ka}\|_2,\ \|c_k\|_2\le S.
\tag{2.2}
\]

Such a premise can be imposed by a smooth raw-radius stop in a fixed-cap
construction; it must not be attributed to a false discrete energy identity.

The forward source family \(\xi\) and reverse source family \(\zeta\) are
independent oriented Gaussian families with full, uncentered input Grams

\[
 E_2[\xi_i\xi_j]=E_1[h_ih_j],\qquad
 E_1[\zeta_i\zeta_j]=E_2[d_id_j].
\tag{2.3}
\]

Each named source remains a separate formal argument even at rank loss.
Every derivative below freezes all controls, covariance laws, scalar
contractions, and already produced coefficients. Set

\[
 \alpha_{i,q}=E_1[\partial_{\zeta_q}h_i],\qquad
 \beta_{i,q}=E_2[\partial_{\xi_q}d_i].
\]

For \(i=(k,a)\), exactly,

\[
 F_{i,q}=\alpha_{i,q}+\gamma_qE_1[h_ih_q]\quad(t(q)<k),
\]
\[
 D_{i,q}=\beta_{i,q}
       +\mathbf1_{t(q)<k}\gamma_qE_2[d_id_q],
\]
\[
 Z_i=\xi_i+\sum_{t(q)<k}F_{i,q}d_q,\qquad
 Q_i=\zeta_i+\sum_{t(q)\le k}D_{i,q}h_q.
\tag{2.4}
\]

In particular the current backward coefficient is

\[
 \beta_{ka,kb}=\mathbf1_{a=b}E_2[c_k\phi''(Z_{ka})].
\tag{2.5}
\]

This is the full current row of the true middle action and adjoint. It is
not obtained by replacing the reverse action with an independent map.

At a fixed graph, the value theorem A.1 applies to \(J\), which is continuous
with \(|J(X,g)|\le|g|+M|X|\). For the derivative formulas one may first clip
the frozen root \(g\) and the unbounded backward products. At a fixed graph,
values have a linear envelope in its finite Gaussian list. Named derivatives
of its lower clock feature are bounded by \(M^2\) times prior named clock
derivatives; roots are held fixed. Upper product differentiation contributes
only finitely many factors \(c\). Consequently all named derivatives have a
polynomial envelope in the same finite Gaussian list. Local convergence and
uniform integrability remove the clips chronologically, using covariance
square-root continuity as in A.2. This justifies (2.3)–(2.5) at each fixed
graph. It does not assert uniformity in graph length.

## 3. A deterministic lower pulse bound

Suppose every previously constructed full backward row has absolute sum at
most \(B\). Define the known constants

\[
 D_*=B+VS^2T,\qquad
 a_*=M^2V\exp(VM^2D_*T),\qquad f_*=a_*+VS^2.
\tag{3.1}
\]

Then

\[
 \sum_q|D_{i,q}|\le D_*,\qquad
 |\alpha_{i,sb}|\le a_*h_sp_b,\qquad
 |F_{i,sb}|\le f_*h_sp_b.
\tag{3.2}
\]

Proof: fix a reverse pulse \(q=(s,b)\), and let

\[
 \chi_{a,k;q}=\partial_{\zeta_q}X_{a,k}.
\]

Its exact equation is

\[
 \chi_{a,k+1;q}=\chi_{a,k;q}
 +\gamma_{ka}\left[\mathbf1_{(k,a)=q}
 +\sum_{t(r)\le k}D_{ka,r}\,
        \phi'(J(X_{r},g_{r}))^2\chi_{r;q}\right].
\tag{3.3}
\]

The direct pulse has size at most \(Vh_sp_b\). Taking the maximum over
coordinates and already visited times, and using \(p_a\le1\), gives

\[
 \max_{a,j\le k}|\chi_{a,j;q}|
 \le Vh_sp_b\exp(VM^2D_*T).
\tag{3.4}
\]

This is pointwise: there is no random \(Q\) multiplier in (3.3).
Multiply by the clock feature derivative bounded by \(M^2\), then take
expectation, to obtain (3.2). The learned term uses (2.2).

For a passive unit input \(u\), write its full first projection as

\[
 z_k(u)=\sum_{a\le m}(u\cdot u_a)J(X_{a,k},g_a)
             +w_{0,\perp}\cdot u.
\]

Its named clock derivative is bounded by \(M^2\sqrt m\) times the maximum
clock pulse. Thus the same proof supplies passive \(\alpha,F\) bounds, with
the explicit harmless factor \(\sqrt m\) in \(a_*\). Full-row passive queries
therefore do not require freezing or dropping the untrained perpendicular
coordinates.

## 4. Linear-growth moments under that one response cap

For a scalar variable let

\[
 N(U)=\sup_{p\ge2}\|U\|_p/\sqrt p.
\]

Let \(S_G\) bound this norm for every innovation in (2.3). It depends only
on \(S\), since every innovation is a centered Gaussian of standard deviation
at most \(S\). Let \(G_0=\max_aN(g_a)\) and put

\[
 H_0=b+MG_0,\qquad
 B_1=(H_0+M^2VS_GT)\exp(M^2VD_*T),
\]
\[
 B_Q=S_G+D_*B_1,\qquad
 H_{20}=b+MS_G,\qquad
 B_2=H_{20}\exp[(V+M^2f_*)T].
\tag{4.1}
\]

At every prefix satisfying the backward-row cap,

\[
 N(h_{ka})\le B_1,\quad N(Q_{ka})\le B_Q,
 \quad N(c_k),N(H_{ka})\le B_2,
 \quad N(Z_{ka})\le S_G+Mf_*TB_2.
\tag{4.2}
\]

Proof: the triangle inequality for \(N\), (1.4), (2.1), and (2.4) imply

\[
 N(h_{ka})\le H_0+M^2V\sum_{j<k}h_jN(Q_{ja}),
 \qquad N(Q_{ka})\le S_G+D_*\max_{r:t(r)\le k}N(h_r).
\]

The lower state at time \(k\) only uses previous reverse rows, so discrete
Gronwall yields \(B_1\). The second bound then gives \(B_Q\).

For the upper layer, let \(C_k=N(c_k)\). Equations (2.1),(2.4) give

\[
 N(H_{ka})\le H_{20}+M^2f_*\sum_{j<k}h_j C_j,
 \qquad
 C_{k+1}\le C_k+Vh_k\max_aN(H_{ka}).
\tag{4.3}
\]

The nonnegative majorant pair initialized by \(\bar C_0=0,\bar H_0=H_{20}\)
and updated by

\[
 \bar C_{k+1}=\bar C_k+Vh_k\bar H_k,\qquad
 \bar H_{k+1}=\bar H_k+M^2f_*h_k\bar C_k
\]

dominates (4.3). Its sum is at most \(H_{20}\exp[(V+M^2f_*)T]\).
This proves the last three bounds. No small-time absorption was used in
this section; the constants are finite for every fixed \(B,T\).

The crucial limitation is the phrase “satisfying the backward-row cap.”
Equation (4.2) is not a deduction from a raw \(L^2\) ball alone.

## 5. The upper response and the unresolved cap inequality

For an upper forward pulse \(p\), define

\[
 U_{i;p}=\partial_{\xi_p}Z_i,\quad
 C_{k;p}=\partial_{\xi_p}c_k,\quad
 V_{i;p}=\partial_{\xi_p}d_i.
\]

Exactly,

\[
 U_{i;p}=\mathbf1_{i=p}+\sum_{t(q)<k}F_{i,q}V_{q;p},
\]
\[
 C_{k;p}=\sum_{t(q)<k}\gamma_q\phi'(Z_q)U_{q;p},\qquad
 V_{i;p}=\phi'(Z_i)C_{k;p}+c_k\phi''(Z_i)U_{i;p}.
\tag{5.1}
\]

Let \(R_k\) be the maximum through time \(k\) of the absolute full source-row
sum of \(U\). Summing (5.1), retaining every time/sample mass, gives

\[
 R_k\le1+f_*\sum_{j<k}h_j(VM^2T+L|c_j|)R_j.
\]

Here \(c_j\) is a field of the upper population shared by the sample indices;
there is no maximum over samples or Gaussian history. Hence

\[
 R_k\le\exp\left(f_*VM^2T^2+f_*L\sum_{j<k}h_j|c_j|\right).
\tag{5.2}
\]

For \(N(U)\le B_2\), expanding the exponential series yields

\[
 E\exp(U^2/(8eB_2^2))\le4/3,\qquad
 Ee^{\lambda|U|}\le(4/3)e^{2e\lambda^2B_2^2}.
\]

Jensen with weights \(h_j/\sum h_j\) therefore proves

\[
 \|R_k\|_2\le\sqrt{4/3}\,
 \exp\{f_*VM^2T^2+4e f_*^2L^2T^2B_2^2\}=:\mathcal R(B,T).
\tag{5.3}
\]

Since \(c_0=0\), (2.1),(2.2) also give

\[
 \|c_k\|_2\le VST.
\]

Taking expectations in the last equation of (5.1), and applying
Cauchy–Schwarz only to \(|c_k|R_k\), gives the explicit cap test

\[
 \sum_p|\beta_{i,p}|\le
 VT(M^2+LS)\mathcal R(B,T)=:\Psi_T(B).
\tag{5.4}
\]

All constants in

\[
 \Psi_T(B)<B
\tag{5.5}
\]

are computed from \(b,M,L,V,S,T\) and the Gaussian roots, not from target
tails. If (5.5) holds, chronological first-failure induction proves the cap
for every admitted mesh: the lower pulse and the current forward field use
only past backward rows, and (5.1) then bounds the current row without using
that row as its own premise. At initialization every row is zero. Equations
(4.2) then give mesh-uniform Gaussian tails.

For \(B=1\), (5.5) holds on some strictly positive interval because every
constant in (3.1),(4.1),(5.3) has a finite limit as \(T\downarrow0\), whereas
the prefactor in (5.4) tends to zero. This is a valid explicit local source
criterion. It is not the requested continuation theorem. At fixed large T,
the displayed bound grows faster than B; no finite solution of (5.5) has
been proved. An inequality with this growth cannot be called a global cap
selection or justified by restarting the local theorem.

In particular, the exact remaining analytic issue is to control the
upper coupled system (5.1) by more than absolute Gronwall against

\[
 c_k\phi''(Z_{ka}),
\tag{5.6}
\]

or to produce a different sufficient reached-tail estimate directly from
the true training equations. Replacing (5.6) by \(\|c_k\|_2L\) inside a
pathwise or \(L^2\) operator bound is invalid.

## 6. A reached first-Euler obstruction for an admissible unbounded activation

This example concerns actual raw Euler from canonical initialization. It is
not an arbitrary ambient-state construction, but it is also not a statement
about a positive-time exact GF endpoint.

Take \(m=d=2\), \(u_1=e_1,u_2=e_2\), \(y_1=1,y_2=-1\), and

\[
 \phi(z)=z+\varepsilon\sin z,\qquad 0<\varepsilon<1.
\tag{6.1}
\]

This activation is nonaffine and smooth, its derivative is bounded and
strictly positive, and its derivative is globally Lipschitz. Define

\[
 q_1=E\phi(G)^2>0,\qquad q_2=E\phi(\sqrt{q_1}G)^2>0.
\]

At initialization \(h_1,h_2\) are orthogonal, because \(\phi\) is odd and
the first Gaussian projections are independent. The forward-only Gaussian
law gives independent \(Z_1,Z_2\sim N(0,q_1)\).

Choose any raw Euler step \(0<h<q_2^{-1}\). The first step has exactly

\[
 w_1=w_0,\qquad K_1=0,\qquad
 c_1=h\{\phi(Z_1)-\phi(Z_2)\}.
\tag{6.2}
\]

Indeed both hidden raw velocities vanish when \(c_0=0\). Independence and
oddness imply \(f_1=hq_2,f_2=-hq_2\), so

\[
 r_1=-(1-hq_2)<0,\qquad r_2=1-hq_2>0.
\tag{6.3}
\]

There are positive-measure events \(E_N\) on which \(Z_1\asymp N\),

\[
 \sin Z_1\le-1/2,\qquad |Z_2|\le1,
\]

with probabilities \(p_N\le C e^{-cN^2}\). For example use fixed-length
subintervals centered at \(2\pi N+3\pi/2\) for \(Z_1\). On these events,

\[
 c_1\ge c hN>0,\qquad \phi''(Z_1)=-\varepsilon\sin Z_1\ge\varepsilon/2.
\tag{6.4}
\]

Let \(v_N=p_N^{-1/2}\mathbf1_{E_N}\in L^2(\Omega_2)\), and perturb only
the middle increment in the unit HS direction

\[
 B_N=v_N\otimes h_1/\sqrt{q_1}.
\tag{6.5}
\]

Then \(B_Nh_1=\sqrt{q_1}v_N\) and \(B_Nh_2=0\). Along this one-dimensional
raw line,

\[
 Df_1[B_N]=\sqrt{q_1}E[c_1\phi'(Z_1)v_N],\qquad
 D^2f_1[B_N,B_N]=q_1E[c_1\phi''(Z_1)v_N^2],
\tag{6.6}
\]

and both derivatives for sample 2 vanish. Differentiation is justified
for each N by the bounded \(v_N\), the bounded first two activation
derivatives, and \(c_1\in L^2\).

On \(E_N\), \(|c_1|\le C h(N+1)\), so

\[
 |Df_1[B_N]|\le C h(N+1)\sqrt{p_N}\longrightarrow0,
\quad
 D^2f_1[B_N,B_N]\ge c q_1h\varepsilon N\longrightarrow\infty.
\]

For the specified mean unhalved loss,

\[
 \mathcal L=\tfrac12(r_1^2+r_2^2),
\]

and therefore (6.3) yields

\[
 D^2\mathcal L[B_N,B_N]
  =(Df_1[B_N])^2+r_1D^2f_1[B_N,B_N]\longrightarrow-\infty.
\tag{6.7}
\]

Consequently the raw gradient is not locally Lipschitz at the actual
first-Euler state (6.2). If it had local Lipschitz constant C there, then
its difference quotient paired with every unit \(B_N\) would have absolute
value at most C, contradicting (6.7). The K component is unchanged by the
orthogonal first-layer clock transformation. Pairing the transformed vector
field with this same K-only direction gives the same contradiction, so that
transformed field is not locally Lipschitz either.

This proves a precise limitation of the bounded-readout reference proof:
its uniform Hilbert-Lipschitz fresh-source forcing estimate cannot simply
be extended to the whole activation class. It does not prove divergence of
the signed source coefficients, failure of their Gaussian tails, or
nonexistence/nonuniqueness of the desired strong GF.
In particular it does not disprove a bound confined to independent Gaussian
probe directions: those constitute a smaller class than the concentrated
unit directions in (6.5). Such a bound would need its own proof.

## 7. Limit order, C1,1 passage, and the unresolved theorem bridge

For fixed \(T\), a successful completion needs the following order.

1. Fix the raw stop radius from the prospective physical energy bound.
   Work with actual bounded residuals and a finite source program; if
   backward caps are used, no exact gradient identity is assigned to them.
2. Prove a finite source cap B, or another exponential incoming-tail bound,
   uniformly over the stopped reference meshes through T. The present
   argument proves this only when the explicit test (5.5) can be met.
3. For C1,1 \(\phi\), choose smooth mollifications. Their \(b,M,L\) bounds
   are uniform. The estimates above are therefore uniform whenever one B
   has been selected independently of mollification. The state comparison
   can then remove smoothing; no convergence of pointwise second derivatives
   is presumed.
4. At fixed smoothing/caps and fixed mesh, apply the fixed finite Gaussian
   program theorem, including the full current reverse row and arbitrary
   singular query covariance. Take width first. Remove fixed-program
   auxiliary product/root clips after that fixed-graph convergence.
5. Use the uniform incoming tails in the one-reference raw comparison, with
   one cutoff factor \(C(1+R)\), to send meshes to zero and cutoffs to infinity.
   Exponential tails suffice by the elementary Osgood inequality; Gaussian
   tails are stronger than necessary. This gives a strong canonical path
   and uniqueness against bounded-primal strong competitors. Recover the
   true energy identity only after identification of the uncut field.
6. To obtain a nonzero correlated-input neighborhood, transfer the complete
   source/tail control to the perturbed **actual** programs. Proximity to
   one existing reference curve is not a Cauchy argument for changed-data
   curves. A fixed positive raw proximity bound does not imply that their
   mesh defects vanish.

The sought uniform reference cap in step 2 is unproved for a general finite
raw-bounded horizon. The near-input transfer in step 6 is also not supplied
by this partial. The activation class includes (6.1), so the newly identified
obstruction cannot be removed by quoting boundedness of \(\phi'\) or by
orthogonal clocks alone. The narrowest surviving source question is whether
the actual coupled forward/readout response in (5.1) has a signed or weighted
estimate that stays finite at every finite physical reference horizon,
without assuming its unknown target tails.

Route registry recommendation: **partial / blocked at the global upper
response estimate**. Reopen upon a proved reached-state bound on (5.1), a
different noncircular moment invariant, or a class restriction explicitly
authorized by the supervisor. This report is not a claim that the original
global theorem is false.

## 8. Two further mechanisms checked after the first round

### Feature-time energy does not supply the needed spatial exponential

Suppose a pre-fit feature-time parameterization has already proved

\[
 b'(s)=\|c'(s)\|_2^2+\|\theta'(s)\|^2,\qquad 0\le b(s)\le1.
\]

This controls the time integral of squared Hilbert speed. The random
integrating factor (5.2) requires a spatial exponential moment of the
coordinatewise integral of \(|c(s)|\). The former bound does not imply the
latter, even when \(c(0)=0\).

For an exact counterexample to that inference, take the probability space
\([0,1]\) and

\[
 c_N(s,x)=s\sqrt N\,\mathbf1_{[0,1/N]}(x),\quad
 0\le s\le1,\qquad \theta_N(s)=0,\qquad b_N(s)=s.
\]

Then \(b_N'=\|c_N'\|_2^2=1\), \(b_N\le1\), and \(c_N(0)=0\), while for
every \(\lambda>0\),

\[
 E\exp\left(\lambda\int_0^1|c_N(s)|ds\right)
 =1-1/N+N^{-1}e^{\lambda\sqrt N/2}\longrightarrow\infty.
\tag{8.1}
\]

Its squared endpoint tails also fail uniform integrability. These paths
are not asserted to solve the neural equations. The calculation only
identifies the extra implication a successful use of feature energy must
prove from neural reachability.

### Bounded-activation truncation leaves a reached weighted-tail defect

Take smooth clips \(\tau_R\) that equal the identity on \([-R,R]\), satisfy
\(|\tau_R'|\le1\), and have \(|\tau_R|\le2R\).
Let \(\phi_R=\tau_R\circ\phi\), with second derivative bounds uniform for
\(R\ge1\). For each separately fixed R the bounded-activation orthogonal
theorem gives a global canonical flow. Its exact raw energy controls its
Hilbert ball independently of R on fixed physical intervals, because the
initial readout is zero and the activation derivative bounds are uniform.
However its pointwise readout bound scales as R.

At a state of the S-truncated reference, comparing with a smaller R requires
the forward truncation defect

\[
 \|(\phi_R-\phi_S)(\bar Z)\|_2,
\]

and the upper backward defect

\[
 \|\bar c\,(\phi_R'-\phi_S')(\bar Z)\|_2.
\tag{8.2}
\]

The first is a reached activation-value tail; the second is a reached
weighted gate tail. Their corresponding lower-layer defects involve the
true reverse field \(\bar Q\). A bound on the initial Gaussian clipping
error does not bound (8.2) at later times. Uniform raw \(L^2\) bounds do not
even imply that the first family of defects vanishes uniformly in S.

Thus truncation gives a legitimate hierarchy of global approximating
flows, but the required Cauchy source is still missing. It has not yet
replaced the upper-response problem by a weaker proved estimate.
