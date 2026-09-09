# Nonlinear response perturbation on a bounded affine feature interval

The proposed conditional response lemma is true for the actual canonical
finite source programs. Below is a proof, including deterministic causal
coefficient stability. Two details of the proposed argument need repair:
the exponential envelope for a backward output needs a current-coordinate
factor, and a first-exit argument must proceed through the four query
stages, rather than assume all current rows are bounded simultaneously.
Neither repair changes the conclusion.

This is an intermediate result on a fixed feature interval. The amplitude
chosen here depends on its affine bounds and duration. This result does
not select one activation for every input angle, remove the caps in a
continuous flow, or prove the two-residual physical GF/GD theorem.

Sources read completely: `CONTRACT.md`, `NEAR_AFFINE_RESPONSE_ROUTE.md`,
and `TWO_SAMPLE_SOURCE_BASELINE.md` in this directory. The finite Gaussian
conditioning/source derivation in lines 211--455, and the beginning of the
common-action construction immediately following it, were also read in
`/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md`.
The skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read in full.
No outcome of the independent baseline review is assumed. The affine
source bounds below are used as a stated mathematical dependency, with
their primal hypothesis specified explicitly.

## 1. Statement, norms, and the exact program

Fix \(S<\infty\), \(B\ge1\), labels \(y_a\in\{-1,1\}\), and
\(-1\le\rho<1\). Write
\[
 c=(y_1/2,y_2/2)^T,\qquad
 \Gamma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
 \qquad P=\Gamma\operatorname{diag}(c),\qquad
 \mathbf1=(1,1)^T.
\]
For rectangular matrices use the maximum absolute row-sum norm
\(|T|=\max_i\sum_j|T_{ij}|\); it is submultiplicative for compatible
sizes. Thus \(|P|\le1\), \(|c^T|=1\), and \(|\mathbf1|=1\).
For a time row of blocks use
\[
 |T_{k\bullet}|_{\mathrm r}=\sum_{j\le k}|T_{kj}|.
 \tag{1}
\]
In particular, this is a sum of block norms, not a maximum over sample
rows after the time sum. For sample pairs \(X\), write
\(\|X\|_p=(\mathbb E|X|_\infty^p)^{1/p}\).

Take any positive mesh \(0=s_0<\cdots<s_N\le S\), with
\(h_j=s_{j+1}-s_j\) for \(j<N\). Set \(h_N=0\) solely as a convention
for zero current-source forcing terms; no terminal step is taken.
Forward coefficient blocks are extended by zero for \(j\ge k\).
The mesh family is assumed to satisfy the affine
primal hypothesis P(B,S), equation (18) of the baseline note: at each
fixed mesh, the actual affine finite-width Euler trajectory obeys
\[
 \max_{k,a}\|Z^{(1),0}_{k,a}\|_n\le B,\quad
 \max_k\{\|W^0_{2,k}\|_{\rm op},\|W^0_{3,k}\|_{\rm op},
                     \|C^0_k\|_n\}\le B
 \tag{2}
\]
on events whose probability tends to one. A common population action
version of this hypothesis is also sufficient, by equations (30)--(32)
of that note. A bounded continuous affine trajectory supplies (2) only
for sufficiently fine meshes, as explained there; arbitrary coarse
Euler stability is not asserted.

Assume the actual affine source coefficients satisfy
\[
 |a^{\ell,0}_{kj}|\le A_0h_j\quad(j<k),\qquad
 |b^{\ell,0}_{k\bullet}|_{\mathrm r}\le M_0,
 \qquad \ell=2,3.                                      \tag{3}
\]
This is not an additional unproved operator-to-response implication:
the baseline note proves it under (2). In our particular block norm a
safe substitution from its (26)--(29) is
\[
 A_0=2\left(24B^2e^{36B^2S}+\tfrac92B^4\right),\qquad
 M_0=2S\left(8B^2e^{36B^2S}+B^4\right).                 \tag{4}
\]
The second factor 2 accounts for
\(\sum_j\max_a\sum_b|b_{ka,jb}|\le
2\max_a\sum_{j,b}|b_{ka,jb}|\).
One may instead supply any constants satisfying (3).

Use precisely
\[
 \phi_\epsilon(z)=1+z+\epsilon\arctan z,\qquad
 g(z)=(1+z^2)^{-1},\qquad
 \mathcal D_{\epsilon,R}(z,q)=q+\epsilon g(z)\tau_R(q),
 \tag{5}
\]
where \(0\le\epsilon\le1\), \(R<\infty\),
\(|\tau_R'|\le1\), \(|\tau_R(q)|\le\min(|q|,2R)\), and
\(\tau_R(q)=q\) on \([-R,R]\). Monotonicity of the clip, if imposed,
is harmless but not needed. The forward maps are not clipped.

There are three separate coordinate populations. In their respective
populations the exact source equations are
\[
 Z^1_k=Z^1_0+\sum_{r<k}h_rP\delta^1_r,
 \qquad H^1_k=\phi_\epsilon(Z^1_k),\qquad
 q^1_k=\zeta^1_k+\sum_{v\le k}b^2_{kv}H^1_v,
 \tag{6}
\]
\[
 Z^2_k=\xi^2_k+\sum_{r<k}a^2_{kr}\delta^2_r,
 \qquad H^2_k=\phi_\epsilon(Z^2_k),\qquad
 q^2_k=\zeta^2_k+\sum_{v\le k}b^3_{kv}H^2_v,
 \tag{7}
\]
\[
 Z^3_k=\xi^3_k+\sum_{r<k}a^3_{kr}\delta^3_r,
 \qquad H^3_k=\phi_\epsilon(Z^3_k),\qquad
 C_k=\sum_{r<k}h_rc^TH^3_r.                            \tag{8}
\]
Here \(\delta^1=\mathcal D(Z^1,q^1)\),
\(\delta^2=\mathcal D(Z^2,q^2)\), and
\(\delta^3_a=\mathcal D(Z^3_a,C)\). All such maps act coordinatewise.
The initial pair has covariance \(\Gamma\), and \(C_0=0\).
The four centered Gaussian groups are independent of one another and of
the first-layer root. Inside a group all sample/time correlations are
retained, including singular covariances. Their covariances are exactly
the second moments specified in baseline equation (5).

In entries, the coefficient rules are
\[
 a^\ell_{ka,jb}
 =\mathbb E\partial_{\zeta^{\ell-1}_{j,b}}H^{\ell-1}_{k,a}
       +h_jc_b\mathbb E[H^{\ell-1}_{k,a}H^{\ell-1}_{j,b}],
 \quad j<k,                                           \tag{9}
\]
\[
 b^\ell_{ka,jb}
 =\mathbb E\partial_{\xi^\ell_{j,b}}\delta^\ell_{k,a}
       +\mathbf1_{j<k}h_jc_b
                    \mathbb E[\delta^\ell_{k,a}\delta^\ell_{j,b}],
 \quad j\le k.                                       \tag{10}
\]
Derivatives freeze every deterministic coefficient and covariance
parameter, and differentiate named formal source arguments separately.
In particular, the response term does not acquire an extra column label.

**Conclusion.** There exist \(\epsilon_*>0\) and \(K<\infty\), depending
only on \(B,S,A_0,M_0\), such that for every mesh covered by (2), every
finite cap, and \(0\le\epsilon\le\epsilon_*\), the actual coefficients
obey
\[
 \max_{\ell,k,j<k}
   \frac{|a^\ell_{kj}-a^{\ell,0}_{kj}|}{h_j}\le K\epsilon,
 \qquad
 \max_{\ell,k}|b^\ell_{k\bullet}-b^{\ell,0}_{k\bullet}|_{\mathrm r}
       \le K\epsilon.                                \tag{11}
\]
In particular they obey (3) with fixed enlarged constants. Their actual
coordinate laws satisfy, uniformly in these meshes, caps, and amplitudes,
\[
 \sup_k\left(\|C_k\|_p+\|q^2_k\|_p+\|q^1_k\|_p\right)
       \le K\sqrt p,\qquad p\ge2.                    \tag{12}
\]
The same bound holds for all the displayed forward fields and deltas.
Here “actual” means the canonical source program, rather than an affine
surrogate or a law with prescribed independent coordinates. Source
coefficients do not carry a finite-width index. All constants and the
choice of amplitude are independent of width; an unconditional
subGaussian assertion about every finite-width neuron is not being made.

The proof first bounds primal states and source variances, then proves
moment and derivative estimates on bounded coefficient prefixes. Exact
affine recursions at those same coefficients reduce their perturbation
to a deterministic Volterra estimate. A stage-by-stage induction closes
the prefix bounds without a continuity argument.

## 2. Primal comparison and the learned-moment errors

This step does not assume any response bound. Put \(b=2B\ge2\) and use
the state-distance norm (19) of the baseline note. On the ball with all
four primal sizes at most \(b\), the following loose bounds hold:
\[
 \|H^1_\epsilon\|_2\le3b,\quad
 \|H^2_\epsilon\|_2\le4b^2,\quad
 \|H^3_\epsilon\|_2\le5b^3,
\]
\[
 \|\delta^3_\epsilon\|_2\le2b,\quad
 \|q^2_\epsilon\|_2\le2b^2,\quad
 \|\delta^2_\epsilon\|_2\le4b^2,\quad
 \|q^1_\epsilon\|_2\le4b^3,\quad
 \|\delta^1_\epsilon\|_2\le8b^3.                       \tag{13}
\]
These are per sample; they also hold in normalized finite-vector norms.
Indeed \(|\phi_\epsilon(z)|\le1+|z|+\pi/2\),
\(|\mathcal D(z,q)|\le2|q|\), and each matrix action has norm at most
\(b\).

At the *same* raw state the forward differences from the affine queries
are bounded by
\[
 \tfrac\pi2\epsilon,\qquad
 \tfrac\pi2(b+1)\epsilon,\qquad
 \tfrac\pi2(b^2+b+1)\epsilon                            \tag{14}
\]
in layers 1, 2, and 3. Backward induction, using
\(|\mathcal D(z,q)-q|\le\epsilon|q|\), bounds the differences in
\(\delta^3,q^2,\delta^2,q^1,\delta^1\) by respectively
\[
 \epsilon b,\quad \epsilon b^2,\quad3\epsilon b^2,
 \quad3\epsilon b^3,\quad7\epsilon b^3.                \tag{15}
\]
For example the middle delta difference is at most
\(\epsilon\|q^2_\epsilon\|_2+
\|q^2_\epsilon-q^2_0\|_2\le3\epsilon b^2\).

For a learned update use
\[
 \|u\otimes v-\widetilde u\otimes\widetilde v\|_{\rm op}
 \le\|u-\widetilde u\|_2\|v\|_2
          +\|\widetilde u\|_2\|v-\widetilde v\|_2.
\]
Insert (13)--(15), \(\sum_a|c_a|=1\), and \(|P|\le1\) into the four
updates. Their total vector-field difference is at most
\(30b^3\epsilon\). The affine vector field is \(9b^2\)-Lipschitz on
this ball, by the explicit estimates (20)--(21) of the baseline note.
Consequently, at a node before any primal exit,
\[
 d_{k+1}\le(1+9b^2h_k)d_k+30b^3\epsilon h_k,
 \qquad d_0=0,
\]
and finite iteration gives
\[
 d_k\le30b^3S e^{9b^2S}\epsilon.                       \tag{16}
\]
Choose the amplitude so this is at most \(B/2\). Induction proves the
same estimate at the next node from a state already inside the ball, so
the perturbed state stays a positive distance from its boundary. No
Lipschitz constant of the nonlinear vector field, and thus no cap, enters
this comparison.

Combining (14)--(16) with the affine query Lipschitz estimates bounds
every forward/backward query difference by \(K_{B,S}\epsilon\) in
\(L^2\), and bounds their \(L^2\) norms by \(K_{B,S}\). At fixed width this
holds on the affine events (2). At a fixed mesh and cap it passes to the
joint population construction for the two programs sharing their initial
matrices and roots. The conditioning dependency applies: there are
finitely many queries, independent Gaussian initial matrices, iid joint
roots with finite second moments, and the coordinate maps (5) are \(C^1\)
and globally Lipschitz with bounded derivatives for each fixed cap.
Learned contractions are then transferred by the finite induction in
baseline Section 3. In particular this is a coupling of actual programs;
it does not compare square roots of covariance matrices of growing size.

The covariance identities now give a bound \(\sigma^2=K_{B,S}^2\) for
every scalar source variance. For any two of the queries whose products
occur in (9)--(10), Cauchy--Schwarz in that joint coupling gives
\[
 |\mathbb E[U_\epsilon V_\epsilon]-\mathbb E[U_0V_0]|
 \le\|U_\epsilon-U_0\|_2\|V_\epsilon\|_2
       +\|U_0\|_2\|V_\epsilon-V_0\|_2
 \le K_{B,S}\epsilon.                                \tag{17}
\]
Thus a learned forward-block error is at most \(K\epsilon h_j\),
and a full learned backward-row error is at most \(KS\epsilon\).
The factor \(c_b\) is retained in taking these bounds; its absolute
column sum is one.

## 3. Coordinate moments under a coefficient bound

Fix finite constants \(A,M\ge1\). For now assume the coefficients needed
to construct a specified prefix satisfy
\[
 |a^\ell_{kr}|\le Ah_r,
 \qquad |b^\ell_{k\bullet}|_{\mathrm r}\le M.           \tag{18}
\]
All estimates in this section and the next depend only on
\(A,M,\sigma,S\). A symbol \(K\) may be enlarged using only these
quantities. No estimate uses the number of mesh points or the cap.

A centered Gaussian with variance at most \(\sigma^2\) has \(L^p\)
norm at most \(2\sigma\sqrt p\), for \(p\ge2\). This follows, for example,
by integrating the bound \(\mathbb P(|X|>t)\le2e^{-t^2/(2\sigma^2)}\).
The norm of a two-coordinate maximum is at most the sum of the two
coordinate norms. Hence all source-pair norms, and the initial root-pair
norm, are bounded by \(K\sqrt p\), with arbitrary correlations allowed.

For the middle layer, put
\(U_k=\max_{v\le k}\|H^2_v\|_p\); this is a maximum of deterministic
norms, not a random maximum over source times. Equations (7) and (18) give
\[
 \|q^2_r\|_p\le K\sqrt p+MU_r,
 \qquad
 \|H^2_k\|_p\le K\sqrt p+2A\sum_{r<k}h_r\|q^2_r\|_p.
\]
Taking the maximum of the latter inequalities and enlarging nonnegative
sums to the final index gives
\[
 U_k\le K(1+2AS)\sqrt p+2AM\sum_{r<k}h_rU_r.
 \tag{19}
\]
Finite iteration bounds this by \(K\sqrt p\,e^{2AMS}\), and then bounds
\(q^2,H^2,Z^2,\delta^2\) by \(K\sqrt p\).

At the bottom, (6) gives
\[
 \|q^1_r\|_p\le K\sqrt p+M\max_{v\le r}\|H^1_v\|_p,
\]
\[
 \|H^1_k\|_p\le K\sqrt p+2\sum_{r<k}h_r\|q^1_r\|_p.
 \tag{20}
\]
The same finite iteration, with coefficient \(2M\), bounds
\(H^1,Z^1,q^1,\delta^1\).

At the top, write \(V_k=\max_{v\le k}\|C_v\|_p\). From (8),
\[
 \|Z^3_k\|_p\le K\sqrt p+2A\sum_{r<k}h_r\|C_r\|_p,
\]
\[
 \|C_k\|_p\le KS\sqrt p
          +2A\sum_{r<k}h_r\sum_{v<r}h_v\|C_v\|_p
 \le KS\sqrt p+2AS\sum_{v<k}h_vV_v.                  \tag{21}
\]
Taking the deterministic maximum and iterating gives the same conclusion
for \(C,Z^3,H^3,\delta^3\). These proofs also apply to incomplete prefixes
whenever the rows actually used have been bounded: \(H^1_k\) uses only
past \(b^2\); \(H^2_k\) uses current \(a^2\) and past \(b^3\); \(C_k\)
uses only earlier top forward instructions; \(q^2_k\) additionally uses
current \(b^3\); and \(q^1_k\) additionally uses current \(b^2\).

These moment bounds are subGaussian bounds for the possibly noncentered
fields. Explicitly, if \(\|X\|_p\le K\sqrt p\), then expansion of the
exponential and \(m!\ge(m/\mathrm e)^m\) give
\[
 \mathbb E\exp\{X^2/(4\mathrm e K^2)\}
 \le1+\sum_{m\ge1}
       \frac{K^{2m}(2m)^m}{(4\mathrm eK^2)^m m!}\le2.
 \tag{22}
\]

## 4. Formal derivatives and the repaired envelope

For each layer set
\[
 G^\ell_r=\operatorname{diag}(\phi_\epsilon'(Z^\ell_{r,a})),
 \quad V^\ell_r=\operatorname{diag}
       (1+\epsilon g(Z^\ell_{r,a})\tau_R'(m^\ell_{r,a})),
\]
\[
 L^\ell_r=\operatorname{diag}
       (\epsilon g'(Z^\ell_{r,a})\tau_R(m^\ell_{r,a})),
 \quad m^1=q^1,\quad m^2=q^2,\quad m^3_a=C.
\]
Using \(|g'|\le1\),
\[
 |G-I|\le\epsilon,\quad |V-I|\le\epsilon,
 \quad |G|,|V|\le2,\quad |L^\ell_r|\le\epsilon Q_r,
 \tag{23}
\]
where \(Q_r=|q^1_r|_\infty\), \(|q^2_r|_\infty\), or \(|C_r|\) in
the relevant population. In particular all derivatives below are formal
derivatives of the specified source equations, not derivatives along a
singular Gaussian support.

For a bottom transpose source at time \(j\), let
\(J_{k,j}=\partial_{\zeta^1_j}Z^1_k\), a \(2\times2\) block. Its exact
recursion is
\[
 J_{k,j}=\sum_{r<k}h_rP\left[
 L^1_rJ_{r,j}+V^1_r\left(I\mathbf1_{r=j}
             +\sum_{v\le r}b^2_{rv}G^1_vJ_{v,j}\right)\right].
 \tag{24}
\]
It vanishes for \(k\le j\). For \(k>j\), (18) and (23) give
\[
 |J_{k,j}|\le2h_j+
       \sum_{r<k}h_r(\epsilon Q_r+4M)
                      \max_{v\le r}|J_{v,j}|.         \tag{25}
\]

In the middle, for any source perturbation the exact equations are
\[
 J_k=I^\xi_k+\sum_{r<k}a^2_{kr}
       \left[L^2_rJ_r+V^2_r\left(I^\zeta_r
                +\sum_{v\le r}b^3_{rv}G^2_vJ_v\right)\right].
 \tag{26}
\]
Here \(J=\partial Z^2\), and \(I^\xi,I^\zeta\) denote the appropriate
direct source derivative. For one transpose source \(j\), the forcing
has norm at most \(2Ah_j\), and \(J_k=0\) for \(k\le j\). Its analogue
of (25) has coefficient \(A(\epsilon Q_r+4M)\).

For the full row of forward-source derivatives put
\(u_k=\sum_{j\le k}|\partial_{\xi^2_j}Z^2_k|\).
Summing (26) in this norm instead gives
\[
 u_k\le1+A\sum_{r<k}h_r(\epsilon Q_r+4M)
                                  \max_{v\le r}u_v.   \tag{27}
\]
All time rows may be padded with zeros to a common length in taking
these sums, so no factor equal to their length appears.

At the top write \(J_{k,j}=\partial_{\xi^3_j}Z^3_k\) and
\(T_{k,j}=\partial_{\xi^3_j}C_k\), the latter a \(1\times2\) block.
The exact equations, including both label signs, are
\[
 J_{k,j}=I\mathbf1_{k=j}
       +\sum_{r<k}a^3_{kr}
            (V^3_r\mathbf1 T_{r,j}+L^3_rJ_{r,j}),
 \qquad
 T_{k,j}=\sum_{r<k}h_rc^TG^3_rJ_{r,j}.                \tag{28}
\]
For their row sums \(u_k,t_k\), respectively,
\[
 t_k\le2\sum_{r<k}h_ru_r,\qquad
 u_k\le1+2A\sum_{r<k}h_rt_r
                    +A\epsilon\sum_{r<k}h_rQ_ru_r
 \le1+\sum_{r<k}h_r(4AS+A\epsilon Q_r)
                                      \max_{v\le r}u_v. \tag{29}
\]

To justify the exponential estimate used for (25), (27), and (29),
if \(x_k\le f+\sum_{r<k}h_r\lambda_r\max_{v\le r}x_v\), with
nonnegative \(\lambda_r\), its increasing majorant satisfies
\(w_0=f\), \(w_{k+1}=(1+h_k\lambda_k)w_k\).
Induction bounds all \(x_k\) by \(w_k\), and
\(w_k\le f\exp(\sum_{r<k}h_r\lambda_r)\).
Consequently all the preactivation derivatives just considered obey
\[
 |J_{k,j}|\le Kh_j\mathcal E_k
 \quad\hbox{for an individual transpose source},\qquad
 u_k+t_k\le K\mathcal E_k
 \quad\hbox{for a forward-source row},
 \tag{30}
\]
where, in the appropriate population, one can use
\[
 \mathcal E_k=
 \exp\left\{K s_k+K\epsilon\sum_{r<k}h_rQ_r\right\}.
 \tag{31}
\]
The constant \(K\) can for instance dominate
\(2A+4AM+4AS+4M+2S+2\). It is fixed before any mesh is chosen.

There is a correction to the envelope proposed in the route note. The
backward outputs themselves contain \(L_kJ_k\). For the middle and top
forward-source derivative rows, (23), (26), and (28) give only
\[
 \sum_j|\partial_{\xi^2_j}\delta^2_k|
       \le K(1+\epsilon|q^2_k|_\infty)\mathcal E_k,
 \qquad
 \sum_j|\partial_{\xi^3_j}\delta^3_k|
       \le K(1+\epsilon|C_k|)\mathcal E_k.             \tag{32}
\]
The current-coordinate factor is not contained in the past-time
exponential (31). Dropping it would be unjustified.

It causes no integrability loss. To see this without a source-time
maximum, let \(t=s_k\le S\), and suppose \(S>0\). Convexity gives, for
every \(\lambda\ge0\),
\[
 \exp\left(\lambda\sum_{r<k}h_rQ_r\right)
 \le1-t/S+\sum_{r<k}(h_r/S)e^{\lambda S Q_r}.          \tag{33}
\]
Equation (22) and
\(uQ\le Q^2/L^2+u^2L^2/4\) show
\(\mathbb E e^{uQ_r}\le2e^{u^2L^2/4}\) for a uniform \(L\).
Thus for every fixed finite \(p\ge1\),
\[
 \sup_k\|\mathcal E_k\|_p<\infty,
 \qquad
 \sup_k\|(1+Q_k)\mathcal E_k\|_p<\infty.             \tag{34}
\]
The second assertion uses Hölder with \(2p,2p\), and the moments in
Section 3. Its constants can depend on \(p\), but not on cap or mesh.

## 5. Derivative comparison at the same coefficient arrays

In this section the deterministic arrays \(a,b\) stay fixed. A superscript
\(\mathrm{aff}\) means the derivative system with \(G=V=I,L=0\), at
these arrays. It need not be the derivative system at the actual affine
baseline arrays. It is deterministic and does not depend on which
Gaussian realization is used.

We prove
\[
 \left|\mathbb E\partial_{\zeta^1_j}H^1_k
                  -\partial_{\zeta^1_j}H^{1,\mathrm{aff}}_k\right|
 +\left|\mathbb E\partial_{\zeta^2_j}H^2_k
                  -\partial_{\zeta^2_j}H^{2,\mathrm{aff}}_k\right|
       \le K\epsilon h_j,                            \tag{35}
\]
\[
 \sum_{j\le k}
 \left|\mathbb E\partial_{\xi^\ell_j}\delta^\ell_k
                   -\partial_{\xi^\ell_j}
                                      \delta^{\ell,\mathrm{aff}}_k\right|
       \le K\epsilon,\qquad \ell=2,3.                \tag{36}
\]
The estimates also hold with expectation outside the sum of block norms
of the random derivative differences.

Here are the error equations and their bounds. In (26), subtracting the
affine equation leaves its affine feedback on \(J-J^{\mathrm{aff}}\)
plus the three terms
\[
 \sum_{r<k}a^2_{kr}\left[
 (V_r-I)I^\zeta_r+L_rJ_r
 +(V_r-I)\sum_{v\le r}b^3_{rv}G_vJ_v
                 +\sum_{v\le r}b^3_{rv}(G_v-I)J_v\right].
 \tag{37}
\]
In (24) the identical bracket is multiplied by \(h_rP\), and its affine
feedback is \(\sum_{r<k}h_rP\sum_{v\le r}b^2_{rv}
(J_{v,j}-J^{\mathrm{aff}}_{v,j})\).
By (23) and (30), the bracket's accumulated forcing is bounded by
\[
 K\epsilon f\left(1+\sum_{r<k}h_r(1+Q_r)\mathcal E_r\right),
 \tag{38}
\]
where \(f=h_j\) for a single transpose source and \(f=1\) for a full
forward-source row. In the single-source case the first term of (37)
appears only at \(r=j\), with its factor \(h_j\); all other derivatives
vanish through time \(j\) and thereafter carry the factor \(h_j\) in
(30). This verifies the source-step factor even for unequal meshes.
All terms with \(G_v-I\) use the increasing envelope
\(\mathcal E_v\le\mathcal E_r\) when \(v\le r\).

The affine feedback is bounded by \(K\sum_{r<k}h_r\max_{v\le r}d_v\),
where \(d_v\) is the norm of the derivative difference under
consideration. The forcing (38) is increasing in \(k\). Applying the
finite majorant argument above to it, or expanding the same finite
products, gives
\[
 d_k\le K\epsilon f e^{KS}
           \left(1+\sum_{r<k}h_r(1+Q_r)\mathcal E_r\right).
 \tag{39}
\]
Its expectation is \(K\epsilon f\), by (34) and the sum of step sizes.
Multiplication by \(G_k\) to obtain a feature derivative adds at most
\(\epsilon|J_k|\), so this proves (35).

For completeness the top subtraction has the equations
\[
 \Delta J_k=\sum_{r<k}a^3_{kr}
       [\mathbf1\Delta T_r+(V_r-I)\mathbf1 T_r+L_rJ_r],
\]
\[
 \Delta T_k=\sum_{r<k}h_rc^T
                     [\Delta J_r+(G_r-I)J_r].        \tag{40}
\]
Their row-norm affine feedback reduces, by substituting the second
equation in the first and using \(\sum h_r\le S\), to at most
\(AS\sum_{r<k}h_r\max_{v\le r}|\Delta J_v|_{\rm r}\).
The remaining terms are bounded by (38) with \(f=1\). Thus (39), with
enlarged constants, bounds both top derivative rows as well.

Finally, at the middle backward output, the derivative difference is
\[
 L_kJ_k+(V_k-I)\sum_{v\le k}b^3_{kv}G_vJ_v
 +\sum_{v\le k}b^3_{kv}(G_v-I)J_v
 +\sum_{v\le k}b^3_{kv}(J_v-J^{\mathrm{aff}}_v).
 \tag{41}
\]
There is no direct transpose-source forcing when taking a forward-source
row. At the top it is
\[
 L_kJ_k+(V_k-I)\mathbf1 T_k+\mathbf1\Delta T_k.         \tag{42}
\]
The current terms \(L_kJ_k\) have expected row norm at most
\(K\epsilon\mathbb E[Q_k\mathcal E_k]\), which is bounded by
\(K\epsilon\) using (34). The other terms are bounded by (30), (39),
and the row bound \(M\). This proves (36), including its current-source
entries. No derivative of a cap, covariance, or coefficient is omitted;
cap derivatives enter only through \(V\) as prescribed in (23).
## 6. Exact deterministic coefficient stability

We now compare coefficient arrays, rather than source realizations. The
following four deterministic recursions are the complete affine
derivative systems at arbitrary fixed arrays \(a,b\). They also fix all
block orientations and sample labels.

Let \(F_{k,j}\) be the bottom \(\zeta^1_j\)-to-\(H^1_k\) derivative,
\(V_{k,j}\) the middle \(\zeta^2_j\)-to-\(H^2_k\) derivative, and
\(U_{k,j}\) the middle \(\xi^2_j\)-to-\(H^2_k\) derivative. In this
section \(V\) denotes this derivative array, not the local diagonal gate
matrix of Section 4. They satisfy
\[
 F_{k,j}=h_jP\mathbf1_{j<k}
       +\sum_{r<k}h_rP\sum_{v\le r}b^2_{rv}F_{v,j},
 \tag{43}
\]
\[
 V_{k,j}=a^2_{kj}\mathbf1_{j<k}
       +\sum_{r<k}a^2_{kr}\sum_{v\le r}b^3_{rv}V_{v,j},
 \tag{44}
\]
\[
 U_{k,j}=I\mathbf1_{k=j}
       +\sum_{r<k}a^2_{kr}\sum_{v\le r}b^3_{rv}U_{v,j}.
 \tag{45}
\]
All arrays are zero beyond their causal support. The top
\(\xi^3_j\)-to-\(C_k\) derivative \(T_{k,j}\in\mathbb R^{1\times2}\)
satisfies
\[
 T_{k,j}=h_jc^T\mathbf1_{j<k}
       +\sum_{r<k}h_rc^T\sum_{v<r}a^3_{rv}\mathbf1 T_{v,j}.
 \tag{46}
\]
Indeed its top preactivation derivative is
\(I\mathbf1_{k=j}+\sum_{v<k}a^3_{kv}\mathbf1 T_{v,j}\), which gives
(46) on inserting it into the readout sum. The affine top delta
derivative is \(\mathbf1 T_{k,j}\). The affine middle delta derivative is
\[
 W_{k,j}=\sum_{v\le k}b^3_{kv}U_{v,j}.                \tag{47}
\]
In particular, \(T_{k,\bullet}\) depends on \(a^3_{r,\bullet}\) only
for \(r<k\), whereas \(U_{k,\bullet}\) depends on current \(a^2_k\) and
past \(b^3_r\). The product (47) uses current \(b^3_k\); it uses no
current \(b^2_k\).

For these deterministic systems, (18) and finite iteration give
\[
 |F_{k,j}|\le e^{MS}h_j,\qquad
 |V_{k,j}|\le Ae^{AMS}h_j\quad(j<k),
 \tag{48}
\]
\[
 |U_{k\bullet}|_{\rm r}\le e^{AMS},\qquad
 |T_{k\bullet}|_{\rm r}\le S e^{AS^2}.                \tag{49}
\]
For example the row inequality for \(U\) is
\(u_k\le1+AM\sum_{r<k}h_r\max_{v\le r}u_v\).
For \(T\), (46) yields
\(t_k\le S+A\sum_{r<k}h_r\sum_{v<r}h_vt_v
\le S+AS\sum_{v<k}h_vt_v\).
The other two estimates follow in the same explicit way from their
forcing sizes \(h_j\) and \(Ah_j\), respectively, and feedback
coefficients \(M\) and \(AM\). Denote the constants on the right of
(48)--(49) by \(K_F,K_V,K_U,K_T\), omitting their factors \(h_j\).

Use a superscript 0 on \(F,V,U,T,W\) to mean the same recursions at the
actual baseline arrays. Combining (17), (35)--(36), and (9)--(10) gives
the exact difference identities
\[
 a^2_{kj}-a^{2,0}_{kj}=F_{k,j}-F^0_{k,j}+\eta^2_{kj},
 \qquad
 a^3_{kj}-a^{3,0}_{kj}=V_{k,j}-V^0_{k,j}+\eta^3_{kj},
 \tag{50}
\]
\[
 b^3_{kj}-b^{3,0}_{kj}=\mathbf1(T_{k,j}-T^0_{k,j})+\nu^3_{kj},
 \qquad
 b^2_{kj}-b^{2,0}_{kj}=W_{k,j}-W^0_{k,j}+\nu^2_{kj},
 \tag{51}
\]
where
\[
 |\eta^\ell_{kj}|\le K\epsilon h_j,
 \qquad |\nu^\ell_{k\bullet}|_{\rm r}\le K\epsilon.
 \tag{52}
\]
The remainders have been bounded in Sections 2 and 5; (52) is not a new
stability assumption. In particular, they retain all nonlinear current
returns and all learned-moment differences, with their column labels.

Define nonnegative deterministic discrepancies
\[
 \alpha^\ell_k=\max_{j<k}
                  \frac{|a^\ell_{kj}-a^{\ell,0}_{kj}|}{h_j},
 \qquad
 \beta^\ell_k=|b^\ell_{k\bullet}-b^{\ell,0}_{k\bullet}|_{\rm r},
\]
\[
 E_k=\beta^2_k+\beta^3_k,\qquad
 I_k=\sum_{r<k}h_rE_r.                                \tag{53}
\]
An empty maximum is zero. We next prove bounds for each current
discrepancy in the actual construction order. The increasing quantity
\(I_k\) uses only completed, strictly earlier backward rows.

**First forward row.** Subtract (43) at the two arrays, expanding
\(b^2F-b^{2,0}F^0=(b^2-b^{2,0})F+b^{2,0}(F-F^0)\). For each \(j<k\),
\[
 \frac{|F_{k,j}-F^0_{k,j}|}{h_j}
 \le K_F\sum_{r<k}h_r\beta^2_r
       +M\sum_{r<k}h_r
             \max_{v\le r}\frac{|F_{v,j}-F^0_{v,j}|}{h_j}.
 \tag{54}
\]
Terms with \(v\le j\) vanish. The first term is increasing with \(k\);
finite iteration therefore bounds (54) by \(K_Fe^{MS}I_k\).
The first identity (50) now gives
\[
 \alpha^2_k\le K(\epsilon+I_k).                       \tag{55}
\]
Only \(b^2_r\) for \(r<k\) was used, including in the nonlinear
derivative estimate producing \(\eta^2_k\).

**Second forward row.** Expanding the feedback in (44) as
\[
 a^2b^3V-a^{2,0}b^{3,0}V^0
 =(a^2-a^{2,0})b^3V
       +a^{2,0}(b^3-b^{3,0})V
       +a^{2,0}b^{3,0}(V-V^0)
\]
and using (48) gives, with \(d^j_k=|V_{k,j}-V^0_{k,j}|/h_j\),
\[
 d^j_k\le(1+MSK_V)\alpha^2_k
       +AK_V\sum_{r<k}h_r\beta^3_r
       +AM\sum_{r<k}h_r\max_{v\le r}d^j_v.            \tag{56}
\]
For example the first feedback term uses

\(\sum_{r<k}|a^2_{kr}-a^{2,0}_{kr}|
  \sum_{v\le r}|b^3_{rv}|\,|V_{v,j}|/h_j
\le MSK_V\alpha^2_k\).

Thus the current forward-row discrepancy multiplies a finite time
integral; it is not an extra unknown on the left of (55).
Insert (55) at each already available time. Since
\(\epsilon+I_v\le\epsilon+I_k\) for \(v\le k\), the forcing in (56)
is bounded by \(K(\epsilon+I_k)\). Finite iteration gives
\(d^j_k\le K(\epsilon+I_k)\), and the second identity (50) proves
\[
 \alpha^3_k\le K(\epsilon+I_k).                       \tag{57}
\]
This uses current \(a^2_k\) and only past \(b^3_r\).

**Top backward row.** Let
\(t_k=|T_{k\bullet}-T^0_{k\bullet}|_{\rm r}\).
The forcing \(h_jc^T\) cancels exactly in (46). Expanding the remaining
products in the order
\((a^3-a^{3,0})\mathbf1 T+a^{3,0}\mathbf1(T-T^0)\),
and summing the source blocks, gives
\[
 t_k\le SK_T\sum_{r<k}h_r\alpha^3_r
                  +AS\sum_{v<k}h_vt_v.              \tag{58}
\]
The factor \(S\) in the feedback follows by exchanging the finite
nonnegative sums:
\(\sum_{r<k}h_r\sum_{v<r}h_vt_v
=\sum_{v<k}h_vt_v\sum_{v<r<k}h_r\le S\sum_{v<k}h_vt_v\).
Finite iteration of (58), followed by (57), yields
\[
 t_k\le K\sum_{r<k}h_r\alpha^3_r
      \le K(\epsilon+I_k),
\]
because \(\sum_{r<k}h_r I_r\le S I_k\).
The first identity (51) therefore gives
\[
 \beta^3_k\le K(\epsilon+I_k).                        \tag{59}
\]
There is no current \(\alpha^3_k\) in (58). The nonlinear remainder at
this stage uses the current \(a^3_k\) bound, already established at the
previous stage, but uses no \(b^3_k\) bound.

**Middle backward row.** Let
\(u_k=|U_{k\bullet}-U^0_{k\bullet}|_{\rm r}\).
Subtracting (45) and making the same three-product expansion as in (56)
gives
\[
 u_k\le MSK_U\alpha^2_k
       +AK_U\sum_{r<k}h_r\beta^3_r
       +AM\sum_{r<k}h_r\max_{v\le r}u_v.              \tag{60}
\]
There is no direct-source difference. Equations (55) and (53) bound its
forcing by \(K(\epsilon+I_k)\), so finite iteration gives
\[
 u_k\le K(\epsilon+I_k).                              \tag{61}
\]
Now use the exact product (47), in the form
\[
 W_k-W^0_k=(b^3_k-b^{3,0}_k)U+b^{3,0}_k(U-U^0).
\]
Submultiplicativity in the block-row norm gives
\[
 |W_{k\bullet}-W^0_{k\bullet}|_{\rm r}
 \le K_U\beta^3_k+
                   \sum_{v\le k}|b^{3,0}_{kv}|u_v
 \le K_U\beta^3_k+M_0\max_{v\le k}u_v.
 \tag{62}
\]
Combining (59)--(62) and the second identity (51) proves
\[
 \beta^2_k\le K(\epsilon+I_k).                        \tag{63}
\]
The current \(b^3_k\) is allowed here because it has just been bounded
by (59). The current \(U_k\) in (62) depends only on current \(a^2_k\)
and past \(b^3_r\), so it creates no new unknown backward row. In fact
the affine baseline satisfies \(b^{3,0}_{kk}=0\); the estimate remains
valid even without exploiting that zero.

Taking one constant large enough for all these explicitly derived
inequalities gives, at each completed time,
\[
 \alpha^2_k,\alpha^3_k,\beta^2_k,\beta^3_k
      \le K(\epsilon+I_k),\qquad
 E_k\le K\epsilon+K\sum_{r<k}h_rE_r.                 \tag{64}
\]
This is the desired deterministic causal stability bound. It was derived
from the actual coefficient identities, not from continuity of a finite
system or an assumed Lipschitz constant in its growing dimension.

## 7. Closing the coefficient bounds, including current returns

Fix \(A=A_0+1\), \(M=M_0+1\), and the variance bound from Section 2.
Choose \(K\ge1\) large enough for every stage inequality in (64) using
these fixed constants. For \(S>0\), define
\[
 \epsilon_*=
 \min\left\{1,
       \frac{B}{60b^3S e^{9b^2S}},
       \frac{1}{2K e^{KS}}\right\},\qquad b=2B.
 \tag{65}
\]
The middle term closes the primal comparison (16). For \(S=0\), take
any \(\epsilon_*\le1\): there are no updates and all backward inputs
and response coefficients are zero.

Here is a literal induction establishing that the bounded prefixes used
above exist through every stage. Suppose all four coefficient rows have
been constructed and bounded at times \(r<k\), and satisfy
\[
 E_r\le K\epsilon\prod_{v<r}(1+Kh_v).
 \tag{66}
\]
The telescoping product identity implies
\[
 \epsilon+I_k
 \le\epsilon\left[1+\sum_{r<k}Kh_r
                         \prod_{v<r}(1+Kh_v)\right]
 =\epsilon\prod_{r<k}(1+Kh_r)
 \le\epsilon e^{KS}.                                \tag{67}
\]
At time \(k\), perform the following four stages in order.

1. Construct \(a^2_k\). Its response uses \(Z^1_k,H^1_k\) and bottom
   derivative paths whose last backward input is at time \(k-1\).
   Equations (20), (24)--(25), and (35) require only past \(b^2\), so
   (55) applies before any bound on this new forward row is assumed.
   Equations (65), (67) give \(\alpha^2_k\le1/2\), hence
   \(|a^2_{kj}|\le(A_0+1/2)h_j<Ah_j\).
2. Construct \(a^3_k\). The just-bounded \(a^2_k\) constructs \(Z^2_k,H^2_k\).
   Their transpose-source derivative paths use only \(q^2_r\), \(r<k\).
   Thus (19), (26), and (35) give (57) using current \(a^2_k\) and past
   \(b^3\). It yields \(\alpha^3_k\le1/2\), hence the required \(a^3\)
   bound. In particular no bound on current \(q^2_k\) has been used here.
3. Construct \(b^3_k\). The readout \(C_k\) and the current \(Z^3_k\) are
   available. The top moment and derivative estimates (21), (28)--(34),
   and (40), (42) use \(a^3\) through time \(k\), now bounded, and no
   backward row. Equation (59) gives \(\beta^3_k\le1/2\), so
   \(|b^3_{k\bullet}|_{\rm r}<M\). This row now defines \(q^2_k\), whose
   subGaussian bound follows from (19) with the current \(H^2_k\).
4. Construct \(b^2_k\). All inputs to its middle derivative equation,
   including current \(q^2_k\) and \(b^3_k\), are now bounded as required.
   Equations (41) and (60)--(63) give \(\beta^2_k\le1/2\), hence its
   row bound. Only now is the current \(q^1_k\) defined and bounded using
   (20).

All learned moments required at a stage are moments of fields already
constructed at that stage; (17) has bounded them independently of this
induction. The bound on \(E_k\) in (64), together with (67), proves
(66) for the newly completed time. At \(k=0\) all forward rows are empty.
Since \(C_0=0\), the top delta and its source derivatives vanish,
\(b^3_{0\bullet}=0\), and the middle backward inputs and their responses
also vanish. Thus \(b^2_{0\bullet}=0\), giving the induction base.

For clarity, the exact current-source blocks computed by this schedule
are, in entries, with \(p^\ell_{k,a}=(L^\ell_k)_{aa}\),
\(v^\ell_{k,a}=(V^\ell_k)_{aa}\), and
\(d^\ell_{k,a}=(G^\ell_k)_{aa}\),
\[
 b^3_{ka,kb}=\mathbf1_{a=b}\mathbb E p^3_{k,a},
 \tag{68}
\]
\[
 b^2_{ka,kb}=\mathbf1_{a=b}\mathbb E p^2_{k,a}
               +b^3_{ka,kb}\mathbb E[v^2_{k,a}d^2_{k,b}].
 \tag{69}
\]
To check these directly, \(C_k\) does not depend on current \(\xi^3_k\)
and \(\partial_{\xi^3_k}Z^3_k=I\), proving (68). Similarly
\(\partial_{\xi^2_k}Z^2_k=I\) and
\(\partial_{\xi^2_k}q^2_k=b^3_{kk}G^2_k\), proving (69).
The factor order and the column sample \(b\) in \(d^2_{k,b}\) are fixed
by this matrix product. Thus off-diagonal current entries are zero for
this schedule, while earlier blocks can be full. From (23) and Section 3,
\(|b^3_{kk}|\le K\epsilon\) and
\(|b^2_{kk}|\le K\epsilon+4|b^3_{kk}|\le K\epsilon\).
These are included in (36), (51), and the row estimate; they were never
dropped or solved by an implicit inverse.

Equations (66)--(67) prove (11), after absorbing \(e^{KS}\) in its
constant. The coefficient bounds now hold on the entire program, so
Section 3 proves (12) on the entire program. Equations (30), (32), and
(34) also prove uniform expected absolute response bounds:
\[
 \mathbb E|\partial_{\zeta^{\ell-1}_j}H^{\ell-1}_k|
       \le Kh_j\quad(j<k),\qquad
 \mathbb E\sum_{j\le k}|\partial_{\xi^\ell_j}\delta^\ell_k|
       \le K,\quad \ell=2,3.                        \tag{70}
\]
No random supremum over Gaussian source times occurs in these estimates.

## 8. What has and has not been supplied

This proves the route note's five-step perturbation lemma under its
bounded affine premise, using the baseline's actual source bounds rather
than an assumed operator-norm identification. It supplies cap- and
mesh-uniform subGaussian tails for the actual three backward inputs,
including the bottom raw-coordinate input. The input Gram and label
factors remain in (6), (9)--(10), (24), (28), and (43)--(46); no inverse
input Gram, covariance inverse, or independence between samples is used.
The proof therefore includes \(\rho=-1\) and arbitrary labels.

The constants are functions of a fixed affine bound and a fixed finite
feature duration. Any bounded interval certified by an affine target
argument may be substituted once its premise (2) is available. No bound
uniform in those affine bounds or durations, and hence no single
amplitude for all angles, has been established here.

The repairs to the proposed proof are quantitative: (32) retains the
terminal multiplier, (33)--(34) control it without a time maximum, and
(55)--(69) resolve every current-row dependency by the exact construction
order. No unresolved envelope or current-row bound is hidden in a named
lemma. Separate cutoff removal and physical-flow arguments can use this
result, but are not conclusions of this file. If a sequence of these
coordinate laws has a weak limit, its subGaussian estimate is inherited
by applying weak convergence to bounded truncations of the continuous
function in (22) and then monotone convergence; no existence of such a
limit is assumed to prove the response result.
