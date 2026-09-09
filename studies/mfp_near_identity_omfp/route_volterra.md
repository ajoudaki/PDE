# Near-identity OMFP: the amplitude-Volterra route and its first unresolved bridge

## 1. Verdict

Let

\[
 \psi_\alpha(x)=\frac{x+\alpha\varphi(x)}{\sigma_\alpha},
 \qquad
 \sigma_\alpha^2=\mathbb E\bigl[Z+\alpha\varphi(Z)\bigr]^2,
 \qquad Z\sim N(0,1).                                      \tag{1.1}
\]

The proposed continuation from the identity activation is a genuinely useful
idea, but continuity at each fixed horizon is not enough.  The uniform
statement needed for time refinement is an *equicontinuity in activation
amplitude* statement for the complete generated/source-response ledger.  That
statement was not proved by the identity-activation theorem.

There is an exact and favorable triangularity.  After the width limit has been
taken at a fixed finite schedule, expansion in \(\alpha\) makes the order-
\(k\) state and every order-\(k\) mixed response jet solve the same linear
identity-background Volterra system; nonlinear forcing contains only lower
amplitude orders.  This is proved in Section 5, including the moving-query
sources needed by the paired coarse/fine defect.

The triangularity does **not**, by itself, give a positive radius uniform in
the number of time steps.  The first estimate not supplied by the existing
identity theorem occurs already at third activation-amplitude order.  It
requires a horizon-uniform \(L^4\) estimate for an aggregate reused-adjoint
image of the first nonlinear susceptibility.  Concretely, the top activation
contains

\[
 \frac12\varphi''(z^{\langle0\rangle})
       \bigl(J^*x^{\langle1\rangle}\bigr)^2.             \tag{1.2}
\]

For the paired-defect third derivative one needs the same estimate with up to
three normalized step derivatives and one transported-defect derivative.
The identity theorem alone controls \(J^*\) only in \(L^2\); \(J^*:L^2\to
L^4\) is not bounded.  A proposed finite-ledger closure of this first test
fails audit: applying an aggregate adjoint to a one-source-marked field
requires a second source derivative, and no mixed response row-sum bound is
available.  Thus even the first generated \(L^4\) susceptibility remains
open.

Accordingly, this route still does not presently prove

\[
 b^*_{t,2}(c)\le C t^4                              \tag{1.3}
\]

for any open \(C_b^{12}\) neighborhood of the identity.  It does sharpen the
problem to an all-source-order aggregate-adjoint estimate on the identity
background.  A precise conditional theorem is stated in Section 9; its
unproved hypothesis is a generated-core analytic norm, not an output or
trajectory modulus.

## 2. Explicit nonlinear class and normalization bounds

Assume throughout that \(\varphi\) is genuinely non-affine and

\[
 M:=\max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\vee1<\infty.            \tag{2.1}
\]

This is a concrete subclass of the earlier at-most-linear \(C^{12}\) class;
in particular the nonlinear residual itself is bounded.  If

\[
                         |\alpha|M\le\frac14,             \tag{2.2}
\]

then the reverse triangle inequality in \(L^2(\gamma)\) gives

\[
 \frac34\le \sigma_\alpha\le\frac54.                    \tag{2.3}
\]

Consequently

\[
 |\psi_\alpha(x)|\le\frac43|x|+\frac13,\qquad
 \|\psi_\alpha'\|_\infty\le\frac53,                    \tag{2.4}
\]

and, for \(2\le r\le12\),

\[
 \|\psi_\alpha^{(r)}\|_\infty
 \le \frac43|\alpha|M.                                  \tag{2.5}
\]

Thus every genuinely nonlinear derivative carries an explicit amplitude
factor.  Notice, however, that the back-propagated multiplier is

\[
 a\,\psi_\alpha''(z),                                    \tag{2.6}
\]

and is not bounded pointwise because \(a\) is Gaussian-tailed.  This is the
reason that (2.5), by itself, is not a bounded perturbation of the identity
operator in the Hilbert state norm.

If an all-order *formal* amplitude argument is desired, strengthen (2.1) to

\[
 \|\varphi^{(r)}\|_\infty\le R A^r r!,\qquad r\ge0,       \tag{2.7}
\]

for specified \(R,A<\infty\).  The class is nonempty and genuinely
nonlinear; for example, a constant multiple of \(\sin x\) satisfies (2.7).
Condition (2.7) gives all formal amplitude coefficients, but it does not by
itself give a positive radius in an \(L^p\) space along unbounded Gaussian
directions.  That radius is part of the separate majorant (NIR) below.
The finite-order triangularity needs only (2.1).

## 3. Exact width-first depth-two recursion

Fix a finite real schedule \(e_0,\ldots,e_{N-1}\).  Width is taken to
infinity at this fixed schedule.  On the resulting two-sided pointed Gaussian
source let

\[
 G_s=\Gamma+q_s,qquad x_s=\psi_\alpha(u_s),qquad
 z_s=G_sx_s,qquad y_s=\psi_\alpha(z_s),                 \tag{3.1}
\]

\[
 b_s=a_s\psi_\alpha'(z_s),qquad
 r_s=G_s^*b_s,qquad d_s=\psi_\alpha'(u_s)r_s.           \tag{3.2}
\]

The exact population update is

\[
 a_{s+1}=a_s+e_sy_s,qquad
 u_{s+1}=u_s+e_sd_s,qquad
 q_{s+1}=q_s+e_s b_s\otimes x_s.                        \tag{3.3}
\]

This is the pointwise fixed-schedule limit of the actual network, with the
same reused connector in both directions.  Iterating the last equation gives

\[
 G_s=\Gamma+\sum_{i<s}e_i b_i\otimes x_i.               \tag{3.4}
\]

Write the fixed Gaussian action as

\[
 \Gamma=I+J^*,\qquad \Gamma^*=I^*+J.                   \tag{3.5}
\]

Then, with \(\xi_s=Ix_s\), \(\chi_s=Jb_s\),

\[
 z_s=\xi_s+\sum_{i<s}e_i
       \{Q_{is}+\bar\rho_{si}\}b_i,                    \tag{3.6}
\]

\[
 r_s=\chi_s+\sigma_{ss}x_s+
       \sum_{i<s}e_i\{K_{is}+\bar\sigma_{si}\}x_i,    \tag{3.7}
\]

where

\[
 Q_{is}=\mathbb E[x_ix_s],\quad
 K_{is}=\mathbb E[b_ib_s],\quad
 \sigma_{ss}=\mathbb E[a_s\psi_\alpha''(z_s)].         \tag{3.8}
\]

The normalized historical responses are exactly the source tangents in
`temporary_depth_time_doubling/UNIFORM_L2.md`, equations (4.1)--(4.8):

\[
 \bar\rho_{si}=\mathbb E[\psi_\alpha'(u_s)p_s^i],
 \qquad
 \bar\sigma_{si}=\mathbb E[q_s^i].                     \tag{3.9}
\]

Every historical term in (3.6)--(3.7) carries \(e_i\).  The current term
\(\sigma_{ss}x_s\) does not; by (2.5), its coefficient is nevertheless
proportional to \(\alpha\).

## 4. The enlarged mixed-response ledger

The coarse/fine transported-defect identity requires more than the undirected
source tangents in (3.9).  Let \(h\) be the common scalar mesh parameter and
let \(\lambda\) mark the one local-defect interpolation direction.  Use
divided jets

\[
 V_s^{[q,r]}=\frac1{q!}\,(t^{-1}\partial_h)^q
                 \partial_\lambda^r V_s,qquad
 0\le q\le3,quad r\in\{0,1\}.                         \tag{4.1}
\]

Only terms with \(r\le1\) are retained.  For each query jet introduce the
moving Gaussian actions

\[
 \xi_{s,q,r}=I x_s^{[q,r]},qquad
 \chi_{s,q,r}=J b_s^{[q,r]}.                            \tag{4.2}
\]

They are not identified with old-source cylindrical derivatives.  They are
new Gaussian source coordinates in the enlarged chronology.  For a generated
field \(V\), let \(\mathscr D_JV\) and \(\mathscr D_IV\) denote its
Malliavin gradients in the two isonormal source blocks.  Gaussian integration
by parts gives the coordinate-free aggregate identities

\[
 J^*V=\mathbb E[\mathscr D_JV],
 \qquad I^*V=\mathbb E[\mathscr D_IV].                 \tag{4.3a}
\]

For a fixed cylindrical representation this reads

\[
 J^*V=\sum_{i,q,r}
     \mathbb E[\partial_{\chi_{i,q,r}}V]\,b_i^{[q,r]},
 \qquad
 I^*V=\sum_{i,q,r}
     \mathbb E[\partial_{\xi_{i,q,r}}V]\,x_i^{[q,r]}.  \tag{4.3b}
\]

where only coordinates on which \(V\) chronologically depends occur.  At a
singular source Gram, (4.3) is an identity for the aggregate sums; individual
coordinate coefficients are not assigned intrinsic meaning.

The causal divisibility proof is unchanged after the source list is enlarged.
A coordinate exposed at time \(i\) can affect a later trained state only
through the update at time \(i\).  After applying the divided derivative in
(4.1), each historical coefficient is therefore a sum of terms carrying
either

\[
 |e_i|\quad\text{or}\quad t^{-1}|\partial_he_i|.         \tag{4.4}
\]

For the coarse, fine, and hybrid strings, the sums of the first weights are
bounded by total step variation and the sums of the second weights are bounded
by an absolute numerical constant.  This is the exact source of the desired
horizon independence.  It is not yet a norm estimate for (4.3).

The candidate finite ledger \(\mathscr L_{t,\alpha}\) used below consists of all
fields in (3.1)--(3.2), their jets (4.1), the source derivatives of those jets
with respect to (4.2), the aggregate sums (4.3), and the scalar contractions
of these fields.  It contains every mixed moving-query and aggregate-adjoint
term needed by three \(h\)-derivatives of the transported local defect.  Its
putative one-source-marked aggregate sums.  There are eight base field types,
two source sorts, and eight jet marks \((q,r)\).  This finite list is enough
to *write* the desired first marked quantities, but it is not closed under
(4.3a): applying an aggregate adjoint to
\(D_\zeta V\) produces
\(\mathbb E[\mathscr D_JD_\zeta V]\), a second source derivative.  This
source-order escalation is the decisive audit issue in Section 7.

## 5. Exact activation-amplitude triangularity

For a field or scalar node \(V\) write

\[
 V^{\langle k\rangle}
   =\frac1{k!}\partial_\alpha^kV\big|_{\alpha=0}.       \tag{5.1}
\]

This notation can be applied simultaneously with the marks in Section 4.

### Lemma 5.1 (fixed-schedule triangularity)

For every fixed finite schedule, take any finite collection of state and
response expressions for which the required derivatives exist.  At every
admissible amplitude order \(k\), its amplitude-order \(k\) coefficients
solve a causal affine system

\[
 \mathscr L_{s+1}^{\langle k\rangle}
 =\mathcal A_s\mathscr L_s^{\langle k\rangle}
  +\mathcal R_{s,k}
       (\mathscr L^{\langle0\rangle},\ldots,
        \mathscr L^{\langle k-1\rangle}),              \tag{5.2}
\]

where \(\mathcal A_s\) is exactly the linearized, enlarged source-response
operator of the identity-activation recursion along its identity trajectory.
In particular, no amplitude-order \(k\) field occurs in a product with
another amplitude-order \(k\) field, and every genuinely nonlinear local
multiplier in the remainder uses only orders below \(k\).

The same assertion holds for all \(k\) under (2.7).

#### Proof

The normalization \(c(\alpha)=\sigma_\alpha^{-1}\) is \(C^{12}\) under
(2.2), and analytic under (2.7).  Write

\[
 \psi_\alpha(v)=c(\alpha)v+\alpha c(\alpha)\varphi(v). \tag{5.3}
\]

For any smooth finite-arity node \(H(\alpha,V_1(\alpha),\ldots,V_m(\alpha))\),
coefficient extraction at order \(k\) gives

\[
 [H]_{k}=\sum_{j=1}^m
 D_jH(0,V^{\langle0\rangle})V_j^{\langle k\rangle}
 +R_k(V^{\langle0\rangle},\ldots,V^{\langle k-1\rangle}).             \tag{5.4}
\]

This follows directly from the multivariate product and chain rules: a term
containing an order-\(k\) input has no remaining positive amplitude order,
so every other factor is evaluated at order zero.  For (5.3), all derivatives
of order at least two in the field variable arise from the second summand and
therefore carry a positive activation order.

Apply (5.4) in chronological order to (3.1)--(3.3).  The coefficients of the
order-\(k\) state are precisely the derivative of the identity vector field
along the order-zero trajectory.  All other terms use lower amplitude orders.

For the response ledger, first enlarge the moving source list as in (4.2).
Both \(I\) and \(J\) are fixed linear maps, so coefficient extraction commutes
with (4.2).  Gaussian integration by parts (4.3) is linear in the queried
field and in each moving source direction.  Its order-\(k\) part therefore
contains the identity-background linear response applied to the order-\(k\)
marked field and lower-order convolutions only.  The causal source-tangent
recurrences are made from sums, products, expectations, and activation
compositions, so (5.4) applies to every one of them.  Finally, divided
\(h\)- and \(\lambda\)-differentiation commutes with coefficient extraction.
This proves (5.2) for the chosen finite expression list.  It does not assert
that the one-source list in Section 4 is closed under recursively applied
aggregate adjoints. \(\square\)

Lemma 5.1 is the substantive positive content of the near-identity idea.  It
rules out an \(\exp(c|\alpha|t)\) factor caused merely by repeatedly placing
the highest amplitude unknown into a nonlinear multiplier.  It does not yet
bound the identity-background resolvent in the moment norms required by the
lower-order forcing.

For a genuinely closed list with three mesh marks, one defect mark, and one
source mark, derivative bookkeeping would consume up to \(k+5\) derivatives
of \(\varphi\).  But Section 7 shows that aggregate reuse raises source order,
so \(C^{12}\) does not support a horizon-independent finite-mark closure by
this argument.  The all-order envelope (2.7) is necessary for the proposed
analytic-scale repair.

## 6. Why fixed-horizon continuity is insufficient

For each fixed \(t\), the generated-core theorem and (2.1) imply that every
node is differentiable in \(\alpha\) a finite number of times and has finite
Gaussian moments.  Hence \(b^*_{t,2}(c;\alpha)\) is locally finite for that
fixed \(t\).  The permissible neighborhood may nevertheless shrink with
\(t\).

The elementary family

\[
                         C_t(\alpha)=t^4e^{t|\alpha|}    \tag{6.1}
\]

is continuous at \(\alpha=0\) for every \(t\) and satisfies
\(C_t(0)=t^4\), but no nonzero \(\alpha_0\) gives
\(\sup_{|\alpha|\le\alpha_0}C_t(\alpha)/t^{4+\beta}<\infty\) for any
fixed \(\beta\).  This is only a logical counterexample, not an OMFP
realization.  It proves that pointwise continuity is not the missing bridge.
One must exploit the step weights in Section 4 to prove equicontinuity.

## 7. The first uncontrolled generated term

Let \(z_\alpha=z_0+\alpha z_1+\alpha^2z_2+\cdots\) denote divided
amplitude coefficients.  From (5.3), the order-three coefficient of the top
activation contains

\[
 [\alpha c(\alpha)\varphi(z_\alpha)]_3
 \supset \frac12\varphi''(z_0)z_1^2.                  \tag{7.1}
\]

The coefficient \(z_1\) contains

\[
                         \Gamma x_1=Ix_1+J^*x_1.       \tag{7.2}
\]

Since \(\varphi''\) is bounded, estimating (7.1) in \(L^2\) requires at
least

\[
                         \|J^*x_1\|_4<\infty.          \tag{7.3}
\]

For the uniform paired-defect theorem the actual requirement is

\[
 \sup_{t\ge1}\sup_{s\le2t}\sup_{|h|t\le c}
 \left\|t^{-q}\partial_h^q\partial_\lambda^r
             J^*x_{s}^{\langle1\rangle}\right\|_4
 <\infty,
 \quad 0\le q\le3, r\in\{0,1\},                     \tag{7.4}
\]

together with the one-source-marked versions generated by (4.3).

The identity theorem gives an \(L^2\) Hilbert/trace-class estimate, not
(7.4).  There is no ambient replacement: choose
\(c\in L^2\setminus L^4\) and put \(X=Jc\).  Then \(X\) is Gaussian and
belongs to every \(L^p\), while

\[
                              J^*X=c\notin L^4.         \tag{7.5}
\]

Thus no estimate of the form
\(\|J^*X\|_4\le C\|X\|_p\) follows from the fixed-operator theorem.
The vector \(x_1\) in (7.3) is generated and may be much better than an
arbitrary \(X\); proving precisely that fact is the new theorem required.

Small amplitude alone does not remove this obstruction.  The contribution to
the actual state is \(\alpha^3\) times (7.1), but a missing or
horizon-dependent \(L^4\) bound cannot be converted into a uniform estimate
by multiplying it by a fixed \(|\alpha|^3>0\).  The generated chronology does,
however, supply more structure than the ambient map.  We now record exactly
what it proves.

Let

\[
 \gamma_p=(\mathbb E|Z|^p)^{1/p},\qquad Z\sim N(0,1).   \tag{7.6}
\]

Evaluate the terminating identity constants \(X_r,T_r,H_r,W_r\) in
`temporary_omfp_continuous_time/route_d.md`, (4.4)--(4.10), at
\(K=27,c=1/432\), and let \(\mathcal I_0\) be one plus their maximum.  Define

\[
 N_0=1,qquad N_{j+1}=16(j+2)N_j^2\quad(0\le j\le6),
 \qquad N=N_7,                                         \tag{7.7}
\]

To include the deterministic identity source tangents and their five mixed
marks, set

\[
 S_0=2,qquad
 S_{j+1}=2N(1+\mathcal I_0+S_j)^N
 \exp\!\left\{\frac{4N(1+\mathcal I_0+S_j)^N}{432}\right\}
 \quad(0\le j\le4),                                    \tag{7.7a}
\]

and put \(\mathcal I=\max\{\mathcal I_0,S_0,\ldots,S_5\}\).  This is a
finite numerical recursion.  At mark zero, \(S_0=2\) closes the identity
recurrences (4.1)--(4.8), since \(Q,K\le4\) and
\(4(4+2)/432<1\).  Differentiating one further mark produces at most \(N\)
lower-mark terms and the same step-weighted homogeneous block; discrete
Gronwall gives exactly (7.7a).  Thus \(\mathcal I\) controls the source-marked
identity ledger as well as the Hilbert state jets.

and

\[
 \Lambda=N(1+\mathcal I)^N.                            \tag{7.8}
\]

The deliberately large integer \(N\) majorizes the number of local
Leibniz--Bell terms produced by the eight field types, one source mark, and
total differential order at most seven.  The recursion proves this by
induction: differentiating a local sum, product, contraction, Gaussian
action, or activation node introduces at most \(16(j+2)\) choices and pairs
two previously generated lists, hence the update in (7.7).

For the normalization coefficients put

\[
 m_1=\mathbb E[Z\varphi(Z)],\qquad m_2=\mathbb E[\varphi(Z)^2],        \tag{7.9}
\]

\[
 c_k=[\alpha^k](1+2m_1\alpha+m_2\alpha^2)^{-1/2}
 =\sum_{\ell=\lceil k/2\rceil}^{k}
 { -\tfrac12\choose\ell}{\ell\choose k-\ell}
 (2m_1)^{2\ell-k}m_2^{k-\ell}.                        \tag{7.10}
\]

For each \(p\ge2\), define moment majorants recursively.  Set

\[
 H_0(p)=\mathcal I(1+\gamma_p)^N.                      \tag{7.11}
\]

For \(k\ge1\), let

\[
 M_k^\sharp=1\vee\max_{0\le r\le k+5}\|\varphi^{(r)}\|_\infty,
 \qquad
 D_k=N(1+M_k^\sharp)^N
       \left(1+\max_{0\le j\le k}|c_j|\right),         \tag{7.12}
\]

\[
 R_k(p)=D_k\left[
  1+\sum_{r=1}^{k+7} 
  \sum_{\substack{k_1+\cdots+k_r\le k\\0\le k_i<k}}
       \prod_{i=1}^r H_{k_i}(rp)
 \right],                                             \tag{7.13}
\]

and

First define

\[
 H_k(2)=\Lambda R_k(2)
       \exp\!\left(\frac{4\Lambda}{432}\right),        \tag{7.14a}
\]

and then, for \(p>2\), define

\[
 H_k(p)=\Lambda\{R_k(p)+\gamma_pH_k(2)\}
       \exp\!\left(\frac{4\Lambda}{432}\right).        \tag{7.14b}
\]

Every sum in (7.13) is finite and uses only \(H_j\) with \(j<k\), so this
is a terminating recursion for every fixed \(k,p\).

### Failed Candidate 7.1 (uniform closure at fixed amplitude order)

The attempted claim was that, for every fixed \(k\le7\) under (2.1), every
\(p\ge2\), and all coarse,
fine, and one-defect hybrid strings satisfying \(|h|t\le1/432\),

\[
 \max_{s\le2t}\max_{q\le3,r\le1,\dagger}
 \|\mathscr L_{s,k}^{q,r,\dagger}\|_p\le H_k(p).       \tag{7.15}
\]

Here the jets are normalized as in (4.1), and \(\dagger\) ranges over no
source mark, one source mark, and the intrinsic aggregate adjoint sums.  Under
(2.7), (7.15) holds for every fixed \(k\).

#### Failed derivation

At amplitude order zero the activation is the identity.  In the inverse-free
recursion (3.6)--(3.9), all pointwise nonlinear products disappear,
\(\sigma_{ss}=0\), and the source tangents are deterministic Volterra
coefficients.  Chronological induction shows that every field and every
normalized \(h\)- or defect-direction jet is a linear combination of jointly
Gaussian raw actions with deterministic coefficients.  The Hilbert bounds
encoded by \(\mathcal I\), followed by
\(\|G\|_p=\gamma_p\|G\|_2\) for a centered Gaussian, give (7.11).

Assume (7.15) through amplitude order \(k-1\).  By Lemma 5.1, every order-
\(k\) node is obtained by applying the identity-background linear ledger
operator to the order-\(k\) unknown, plus a forcing containing only lower
orders.  Holder's inequality with exponent \(rp\), the derivative envelope,
the normalization formula (7.10), and the term count (7.7) bound the complete
forcing by (7.13).

It remains to bound the homogeneous operator, including the reused adjoint.
For a moving query, the fresh actions satisfy

\[
 \|IV\|_p=\gamma_p\|V\|_2,
 \qquad
 \|JV\|_p=\gamma_p\|V\|_2.                            \tag{7.16}
\]

For an adjoint action, first use the aggregate expansion (4.3).  At amplitude
order \(k\), its homogeneous part is

\[
 \sum_{i,\mu}
 \left{
  c^{\langle0\rangle}_{s;i,\mu}V^{\langle k\rangle}_{i,\mu}
  +c^{\langle k\rangle}_{s;i,\mu}V^{\langle0\rangle}_{i,\mu}
 \right},                                            \tag{7.17}
\]

where \(\mu=(q,r)\); the second summand is part of the coupled marked
unknown.  Every historical term in (7.17) carries its actual step weight.
The current reverse-response coefficient is zero in the homogeneous identity
operator, because \(\psi_0''=0\).  Thus all same-order marked unknowns form
one causal *linear* Volterra block.  The local forward/reverse sweep is
acyclic; eliminating it in chronological node order costs at most \(\Lambda\).
Crucially, a fresh action in (7.16) costs \(\gamma_p\) times the already
controlled \(L^2\) block, rather than \(\gamma_p\) times the unknown
\(L^p\) block.  Likewise, the second term in (7.17) is a scalar \(L^2\)
response coefficient times an identity-background Gaussian.  Only the
historical aggregate sum propagates the same \(L^p\) unknown, and its
coefficient is bounded by \(\Lambda\), independently of \(p\).

Writing \(X_s(p)\) for the maximum \(L^p\) norm of that coupled block, it
follows first that

\[
 X_s(2)\le\Lambda R_k(2)+
           \Lambda\sum_{i<s}|e_i|X_i(2),               \tag{7.18a}
\]

and, after solving this block, that

\[
 X_s(p)\le\Lambda\{R_k(p)+\gamma_pH_k(2)\}
           +\Lambda\sum_{i<s}|e_i|X_i(p).              \tag{7.18b}
\]

Terms in which a normalized mesh derivative hits \(e_i\) use lower mesh
order and were already placed in \(R_k\); they do not enter the homogeneous
coefficient.  Since every relevant string has
\(\sum_i|e_i|\le4/432\), the discrete Volterra Gronwall inequality would give
(7.14a) and then (7.14b).  The missing implication is the passage from the
aggregate adjoint formula (7.17) to the scalar row estimate (7.18); it is not
proved by the displayed constants.

Thus Failed Candidate 7.1 does not prove (7.4), even at amplitude order one.
The obstruction is audited next.

### Proposition 7.2 (the finite marked ledger is not closed)

Applying an aggregate adjoint to a one-source-marked field requires a second
source derivative:

\[
 J^*D_\zeta V=\mathbb E[\mathscr D_JD_\zeta V].        \tag{7.19}
\]

After another reused adjoint, a third source derivative appears, and so on.
These terms do not vanish for a genuine nonlinearity.  For example,

\[
 D^re^{i\lambda z}
 =e^{i\lambda z}B_r(i\lambda Dz,\ldots,i\lambda D^rz)
 \neq0\qquad(r\ge1).                                   \tag{7.20}
\]

Hence a ledger containing at most one source mark is not invariant under the
exact moving-query aggregate-adjoint recursion.

#### Proof

Equation (7.19) is the coordinate-free identity (4.3a) applied to
\(D_\zeta V\).  Repetition raises Malliavin order by one each time.  Equation
(7.20) is the ordinary Malliavin chain rule, with \(B_r\) the complete Bell
polynomial, and is nonzero for every \(r\) when \(\lambda\ne0\). \(\square\)

There is a second independent missing estimate.  Even for an unmarked field,
causal divisibility yields a syntactic row

\[
 \sum_{i<s}e_i c_{si}V_i,                              \tag{7.21}
\]

but it does not yield

\[
 \sup_s\sum_{i<s}|e_i|\,|c_{si}|<\infty               \tag{7.22}
\]

for the mixed moving-query response coefficients.  The identity Hilbert
constants and the term-count recursion do not control this
\(\ell^1\)-in-source norm.  Equation (7.18) therefore assumes exactly the
aggregate-resolvent estimate it was intended to prove.

The rigorous fixed-order verdict is consequently

\[
 \boxed{\text{the generated }L^4\text{ susceptibility estimate (7.4)
 remains open}.}                                      \tag{7.23}
\]

Any repair must either construct an all-source-order analytic scale with a
controlled loss under \(V\mapsto\mathbb E[\mathscr D_JV]\), or prove a
direct intrinsic \(L^p\) estimate for aggregate adjoints on the reachable
marked core.  No such estimate is proved here.

## 8. The exact non-circular lemma that would close the route

For a residual satisfying (2.7), let \(\mathscr L_{s,k}^{q,r}\) range over
the field types of Section 4, and let \(\mathscr D^m\) denote the joint
\(m\)-th Malliavin derivative in all moving \(I\)- and \(J\)-source blocks.
For \(\rho>0\), define the all-source analytic norm

\[
 \mathfrak N_k(c,\rho)=
 \sup_{t,s,|h|t\le c}
 \max_{q\le3,r\le1}
 \sup_{p\ge2}
 \sum_{m=0}^{\infty}\frac{\rho^m}{m!}
 \frac{\|\mathscr D^m\mathscr L_{s,k}^{q,r}\|_p}
      {p^{(k+m+6)/2}}.                                 \tag{8.1}
\]

There is no factor \(t^q\) in (8.1), because the jets were already normalized
by \((t^{-1}\partial_h)^q\) in (4.1).  The power of \(p\) is intentionally
generous: amplitude order, source order, and the fixed paired-defect marks
all contribute to moment degree.  The sought generated-core susceptibility
estimate is: there are \(c,\rho,C_0,C_1>0\) such that

\[
 \boxed{
   \mathfrak N_k(c,\rho)\le C_0 C_1^k
   \quad(k\ge0).}                                      \tag{NIR}
\]

All quantities in (8.1) are activation-state/source-response nodes of the
explicit width-first DAG.  No output, trained-trajectory continuity modulus,
or derivative of \(F_t\) is used.  The estimate is rank independent and
retains the aggregate response at singular Grams.

Lemma 5.1 shows that the order-\(k\) equation uses only the
identity-background resolvent on the left.  Failed Candidate 7.1 shows that
this observation is insufficient until the resolver is controlled on an
all-source scale.  Such a proof would proceed by:

1. proving the identity-background aggregate resolver in the norm (8.1),
   with a quantified loss from a source radius \(\rho\) to
   \(\rho'<\rho\);
2. applying the derivative envelope (2.7) to the
   lower-order convolutions;
3. using the chronological step simplex to replace \(N\)-fold history counts
   by powers of total variation divided by \(N!\); and
4. closing the resulting Cauchy-product majorant for sufficiently small
   explicit \(c\).

The formal source shift itself has the expected Cauchy loss.  If
\(0<\rho'<\rho\), then

\[
 \sum_{m\ge0}\frac{(\rho')^m}{m!}
 \|\mathbb E[\mathscr D^{m+1}V]\|_p
 \le \frac{\rho}{(\rho-\rho')^2}
 \sum_{m\ge0}\frac{\rho^m}{m!}\|\mathscr D^mV\|_p.   \tag{8.2}
\]

Indeed, after shifting \(n=m+1\), the coefficient ratio is
\(n(\rho'/\rho)^{n-1}/\rho\), bounded by
\(\rho/(\rho-\rho')^2\).  What is unproved is how to spend this radius loss
through arbitrarily many reused adjoints using only total step variation,
while also closing the moving source directions and response row sums
(7.22).  The ambient shortcut remains forbidden by (7.5).  Hence (NIR) is
open already at the first susceptibility.

### 8.1 Direct nonzero-amplitude random-Gronwall test

One can try to avoid summing the amplitude series.  For the finitely many
mesh/defect jet types, let \(G_{i,\tau}\) denote their moving fresh Gaussian
actions and set

\[
 S_s=\sum_\tau\sum_{i<s}|e_i|\,|G_{i,\tau}|.            \tag{8.3}
\]

Whenever their variances are bounded by \(V^2\), the correlated-Gaussian
estimate gives, for every \(\lambda\ge0\),

\[
 \mathbb E e^{\lambda S_s}
 \le 2^{|\tau|}
 \exp\{C\lambda^2|\tau|^2V^2(\sum_i|e_i|)^2\}.         \tag{8.4}
\]

Ignoring aggregate adjoints, the causal state and source-tangent recurrences
can indeed be dominated by a finite polynomial in the current raw Gaussians
times \(e^{C\mu S_s}\), where

\[
 \mu=\max_{2\le r\le12}\|\psi_\alpha^{(r)}\|_\infty
 \le\frac43|\alpha|M.                                  \tag{8.5}
\]

The dangerous current multipliers \(a_s\psi''(z_s)\) and
\(r_s\psi''(u_s)\) then enter a step-weighted random-Gronwall exponent.
Thus the small-curvature block itself is not a demonstrated no-go; (8.4)
would control it once the remaining coefficients were closed.

The argument fails when the exact aggregate moving adjoints are restored.
Let \(\mathcal X_m\) denote a norm containing source derivatives through
order \(m\).  The response operation has the type

\[
 V\longmapsto\mathbb E[\mathscr D_JV]:
 \mathcal X_{m+1}\longrightarrow\mathcal X_m.          \tag{8.6}
\]

Estimating its action on an \(m\)-marked query therefore requires the
\((m+1)\)-marked state.  The nonlinear perturbation of the identity response
block is not an endomorphism of any finite ledger:

\[
 \mathcal R_\alpha:\mathcal X_m\not\longrightarrow\mathcal X_m.     \tag{8.7}
\]

A Neumann estimate for \((I-\alpha\mathcal R)^{-1}\) cannot be formulated
on that space: each power requests another source derivative.  Multiplying
by small \(|\alpha|\) does not repair the missing domain or the unproved row
sum (7.22).

An all-source analytic scale could in principle replace (8.7) by maps
\(\mathcal X_\rho\to\mathcal X_{\rho'}\) with the loss (8.2).  To close a
direct nonzero-\(\alpha\) theorem one must prove that causal step weights pay
for the accumulated source-radius loss, including the unweighted current
response, and that a positive radius remains over every partition of fixed
total variation.  This is precisely the missing strengthened OMFP theorem.

Hence the direct random-Gronwall route does **not** close with a finite
\(C_b^{12}\) derivative/moment budget.  It remains viable only through either
an all-source analytic-scale construction or a direct aggregate-adjoint
estimate avoiding recursive Malliavin expansion.  Neither is proved here.

## 9. Conditional implication for the fifth remainder

For completeness, here is the exact payoff of (NIR).  Put \(P_*=32\); after
the all-source norm has closed the adjoints, the terminal Leibniz ledger for
three mesh derivatives and one defect direction uses no moment above
\(L^{32}\).

### Proposition 9.1

Assume (2.7) and (NIR).  If

\[
                  |\alpha|C_1\sqrt{P_*}\le\frac12,     \tag{9.1}
\]

then the amplitude series of every ledger node in Section 4 converges in all
the moment spaces needed by the transported-defect third derivative.  There
are explicit constants

\[
 c_{\varphi,2}=c,qquad
 C_{\varphi,2}=P(R,A,C_0,C_1,c),                       \tag{9.2}
\]

where \(P\) is the finite Leibniz--Bell polynomial obtained from the eight
field types and the derivative marks \(q\le3,r\le1\), such that

\[
 \left|F_{t,2}(2h)-F_{2t,2}(h)-\kappa_{t,2}(\alpha)h^3\right|
 \le C_{\varphi,2}t^4|h|^5,qquad |h|t\le c.           \tag{9.3}
\]

#### Proof

By (8.1) and (NIR), for each \(2\le p\le P_*\) the amplitude series is
majorized by
\(C_0p^3\sum_{k\ge0}(|\alpha|C_1\sqrt p)^k\).  Condition (9.1) bounds this
by \(2C_0p^3\).  The finite products in the paired-defect ledger are then
controlled by Holder using exponents at most \(P_*\).  Termwise source
integration by parts and the mixed derivatives in Section 4 are dominated.

Use the exact paired-Euler factorization

\[
 F_{t,2}(2h)-F_{2t,2}(h)=h^2Q_t(h).                    \tag{9.4}
\]

The finite transported-defect ledger and (NIR) give

\[
 \sup_{|h|t\le c}|Q_t'''(h)|
 \le 6P(R,A,C_0,C_1,c)t^4.                             \tag{9.5}
\]

Oddness gives \(Q_t(0)=Q_t''(0)=0\).  Taylor's integral formula therefore
yields

\[
 |h^2Q_t(h)-Q_t'(0)h^3|
 \le P(R,A,C_0,C_1,c)t^4|h|^5.                        \tag{9.6}
\]

Set \(\kappa_{t,2}(\alpha)=Q_t'(0)\).  This proves (9.3). \(\square\)

This coefficient is not left output-defined.  The independently established
width-first cubic marked recursion gives

\[
 \kappa_{t,2}(\alpha)
 =-\frac{t(2t-1)}2\,J_{\psi_\alpha,2},                 \tag{9.7}
\]

where \(J_{\psi_\alpha,2}\) is the finite polynomial in the nine stated
Gaussian activation integrals in
`temporary_depth_time_doubling/CUBIC_DEPTH_TIME.md`.  Equation (9.6) implies
uniqueness of the cubic coefficient, so (9.7) and \(Q_t'(0)\) agree; (9.7),
not an unknown-output derivative, is the canonical definition used in the
theorem.

Proposition 9.1 is conditional because (NIR) is open.  It is included to show
that no further conceptual bridge is hidden after the marked resolvent
estimate.

## 10. Audit and research conclusion

1. **Limit order.**  All activation-amplitude statements are made after the
   fixed-schedule width limit.  No finite-width Taylor expansion or diagonal
   width/mesh limit is used.
2. **Reused connector.**  Both \(I+J^*\) and \(I^*+J\) occur, and the moving
   source jets (4.2) are retained.
3. **Singular Grams.**  Only the aggregate identities (4.3) are assigned
   intrinsic meaning.
4. **Continuity.**  Fixed-horizon continuity is not promoted to uniform
   equicontinuity; Section 6 explains the missing quantifier.
5. **Small amplitude.**  The factor in (2.5) is recorded, but is not used to
   pretend that an unbounded \(L^2\to L^4\) map becomes bounded.
6. **Triangularity.**  Lemma 5.1 is exact.  It shows that amplitude expansion
   is a better route than direct perturbation of the nonzero-\(\alpha\)
   highest-order block.
7. **Failed finite-ledger closure.**  Failed Candidate 7.1 does not establish
   (7.4).  Aggregate adjoints raise source order and the needed response row
   sums are unproved.
8. **Fatal gap.**  Even the first susceptibility requires either a direct
   generated-adjoint estimate or an all-source analytic scale.  An actual
   open nonlinear neighborhood additionally needs the geometric bound (NIR).
9. **Claim level.**  The existence of a fixed nonzero nonlinear neighborhood
   satisfying (1.3) remains open.  The near-identity proposal has a good shot
   at pushing the problem forward because it triangularizes the difficult
   response block, but it has not yet closed the generated-adjoint moment
   estimate.

The highest-leverage next result is not another terminal-output Taylor
calculation.  It is the all-source aggregate-resolvent estimate (8.1)--(8.2),
including the row sum (7.22).  Only after this first-susceptibility gate is
closed does the geometric-in-amplitude part of (NIR) become the next issue.

## 11. Depth-three transfer

The algebraic triangularity above transfers to depth three.  Add
one forward source family \(I_3x_{2,s}^{[q,r]}\), one reverse family
\(J_3b_{3,s}^{[q,r]}\), and their one-source-marked aggregate adjoints.  The
source-time divisibility proof applies separately at each connector.  At
amplitude order \(k\), coefficient extraction again leaves the depth-three
identity-background linear ledger on the left and lower amplitude orders on
the right.  Each connector, however, has its own source-order escalation.
Consequently the finite-ledger Gronwall construction fails at depth three for
the same reason as at depth two; no horizon-uniform fixed-amplitude moment
theorem is claimed.

This does not prove even the first uniform nonlinear susceptibility at depth
three, much less a nonzero amplitude radius.  Its exact missing bridge is the
two-connector version of (NIR), with one common geometric
constant after both aggregate response blocks are composed.  A depth-two NIR
proof would therefore be the correct testbed: it would expose whether the
multigraded norm survives one connector before attempting the second.
