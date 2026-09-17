# Corollary: m signed permutation inputs in d=m coordinates

2026-09-16. Bounded analytic corollary of the frozen
`three_coordinate_candidate.md`. The main three-input candidate is unchanged.
This is a restricted higher-dimensional family, not a theorem for generic
inputs or the original three-input d=2 circle problem. No experiment or
network-identification claim is involved.

## Statement

Fix an integer m>=3, set input dimension d=m, and choose real a,b with

\[
 a^2+(m-1)b^2=1,\qquad a\ne b.
\]

For i=1,...,m, set

\[
 v_i=b\mathbf1+(a-b)e_i,\qquad
 u_i=y_i v_i,\qquad y_i\in\{-1,1\},\qquad x_i=\sqrt m\,u_i.
                                                               \tag{1}
\]

The signs may be chosen arbitrarily; in particular both labels may occur.
Assign mass 1/m to every datum. Use the exact general-d p=1 population
closure from `docs/observable_p1.md`, with eta=1/4096, its full correlated
Gaussian initialization, the full (m+1)-by-(2m+1) matrix M and its actual
transpose, and initial (w,c,M)=(g,0,D). Use the unhalved mean square loss
and the unchanged physical population-L2/Frobenius metric.

Define from the current state

\[
 U=\frac1m\sum_i y_i H^2(u_i)=\frac1m\sum_i H^2(v_i),\qquad
 F=E_2[cU]=\frac1m\sum_i y_i f(u_i),
\]
\[
 q=E_2[c^2],\qquad C=E_2[U^2],\qquad C_0=E_2[U_0^2].             \tag{2}
\]

Then the initialized Gram of all m upper hidden fields H^2_0(u_i) is
positive definite. In particular C_0>0. The unique initialized
characteristic solution exists for every physical t>=0, satisfies
y_i f(u_i)=F for all i, and obeys

\[
 \mathcal L=(1-F)^2,\qquad
 \mathcal L(t)\le e^{-4C_0t},\qquad
 C(t)\ge C_0,\qquad q(t)\le F(t)^2/C_0\le1/C_0.                 \tag{3}
\]

The same mixed potential works with no extra m factor:

\[
 \Psi=\frac{1+q}{C_0+F^2},\qquad
 \Phi=\mathcal L(1+C_0\Psi),\qquad
 \mathcal L\le\Phi\le2\mathcal L,\qquad
 \dot\Phi\le-4C_0\Phi,\qquad \Phi(0)=2.                        \tag{4}
\]

The complete state converges to a fitting state with finite physical
length, including the bound

\[
 \int_t^\infty\|\dot X(r)\|\,dr
       \le\sqrt{\mathcal L(t)/C_0}.                            \tag{5}
\]

Convergence holds in the physical Hilbert norm, in the essential-supremum
norms of w-g and c together with the Frobenius norm of M, and in W2 for
the complete joint laws Law(b_1,g,w) and Law(b_2,c). Constants may depend
on m and the input parameters; no rate uniform in m or geometry is claimed.

## 1. Initialization and dimension transfer

The exact scalar initialized constants are independent of d. With
independent lower pairs G_i~N(0,1), zeta_i~N(0,tau), and independent
upper coordinates Xi_i~N(0,v), put

\[
 v=E\tanh^2G,\quad \tau=E\tanh^2(\sqrt vG),\quad \alpha=1-\tau,
 \quad h_i=\tanh G_i,\quad k_i=\tanh(\zeta_i+\alpha h_i),
 \quad Z_i=\tanh\Xi_i,
\]
\[
 \beta=E[h_i k_i],\quad \sigma=E[k_i^2],\quad\gamma=1-\sigma,
 \quad R_h=\sqrt{v+\eta},\quad
 R_k=\sqrt{\sigma+\eta-\beta^2/(v+\eta)},\quad
 R_Z=\sqrt{\tau+\eta}.
\]

The normalized columns have lengths 2m+1 and m+1:

\[
 b_1=\left((1+\eta)^{-1/2},h/R_h,
          (k-\beta h/(v+\eta))/R_k\right)^T,\qquad
 b_2=\left((1+\eta)^{-1/2},Z/R_Z\right)^T.                       \tag{6}
\]

Initially the only nonzero entries of D are, for each i,

\[
 D_{Z_i,h_i}=\frac{\alpha v}{R_hR_Z},\qquad
 D_{Z_i,k_i}=
 \frac{\alpha\beta\eta/(v+\eta)+\tau\gamma}{R_kR_Z}.              \tag{7}
\]

Thus the same reverse-response term, ridge, normalization, and joint
lower law are retained. Only the number of repeated coordinate blocks
changes. As in the frozen candidate, the feature maps are contractions,
their essential-supremum envelopes B_l are finite for fixed m, and
d_0=||D||op is finite.

For clarity, the scalar initialized map used below is exactly

\[
 (A,B)=(\alpha v,\alpha\beta+\tau\gamma)
 \begin{pmatrix}v+\eta&\beta\\\beta&\sigma+\eta\end{pmatrix}^{-1},
 \quad j(g)=A\tanh g+B E_\zeta\tanh(\zeta+\alpha\tanh g),
\]
\[
 \kappa(t)=\frac1{\tau+\eta}
 E[j(G)\tanh(tG+\sqrt{1-t^2}Z)],\qquad -1\le t\le1,            \tag{8}
\]

where the last G,Z are independent standard scalar Gaussians. Section 5
of the frozen candidate proves from these same scalar definitions that
kappa is odd and strictly increasing; its proof does not contain d or m.
In particular it retains the possibly negative coefficient A and proves
j'(g)>=34alpha sech^2(g)/529, followed by
kappa'(t)=E[j'(G)sech^2(tG+sqrt(1-t^2)Z)]/(tau+eta)>0.
All hypotheses of that scalar result are identical here.

For each unit u in R^m, (g_i,g dot u) is a centered Gaussian pair of
unit variances and correlation u_i. The other m-1 coordinates combine
into an independent Gaussian with variance 1-u_i^2, including its
possible zero-variance endpoint. Eliminating the Cholesky factors in
(6)–(7), coordinate by coordinate, therefore gives exactly

\[
 H^2_0(u)=\tanh\left(\sum_{i=1}^m Z_i\kappa(u_i)\right).        \tag{9}
\]

This verifies the dimension transfer without rotating or modifying
the dictionary.

## 2. Rank m, including the exceptional coefficient sum

Set p=kappa(a), q_*=kappa(b), so p!=q_*. The coefficient vectors of
the fields H^2_0(v_i) are the rows of

\[
 V=(p-q_*)I_m+q_*\mathbf1\mathbf1^T.                           \tag{10}
\]

The raw upper mark Z has positive density throughout (-1,1)^m. If
sum_i t_i H^2_0(v_i)=0 in L2, continuity and this density imply the
same identity throughout the open cube. Its first derivatives at zero
give V^T t=0. The eigenvalues of V are p-q_* on the (m-1)-dimensional
space orthogonal to the constant vector, and p+(m-1)q_* on that vector.

If the latter eigenvalue is nonzero, all t_i vanish. Otherwise
t=t_0*1, p=-(m-1)q_*, and q_*!=0 because p!=q_*. Along Z=r e_1,
the third derivative of the identity is

\[
 0=-2t_0\{p^3+(m-1)q_*^3\}
   =2t_0(m-1)m(m-2)q_*^3.                                  \tag{11}
\]

Since m>=3 and q_*!=0, this again forces t_0=0. Hence the m fields
are linearly independent. Multiplying field i by y_i conjugates its
Gram by an invertible diagonal sign matrix, preserving positive
definiteness. This proves the claim for the original H^2_0(u_i), as
well as C_0>0 for the nonzero linear combination (2).

The weighted readout Gram is (1/m) times the ordinary field Gram and
is likewise positive definite. This initialization statement does not
assert its least eigenvalue stays positive throughout training.

No two original inputs are coincident or antipodal. First v_i=v_j,
i!=j, forces a=b. If v_i=-v_j, choose k distinct from i,j, which is
possible because m>=3; its coordinate forces b=0, and coordinate i
then forces a=0, contradicting unit norm. Multiplication by fixed signs
cannot create equality up to sign between distinct such vectors.

The condition m>=3 is material for this family. For m=2, a=-b gives
v_1=-v_2, the exceptional cubic coefficient in (11) vanishes, and
the label-absorbed targets both equal to +1 cannot be fitted by an odd
prediction. This is not an obstruction for the stated m>=3 corollary.

## 3. Full-block symmetry and population existence

For any current state and any input u, the bias-free closure satisfies
H^2(-u)=-H^2(u) and f(-u)=-f(u). Consequently, for arbitrary prescribed
signs in (1), the ambient loss is exactly

\[
 \mathcal L(X)=\frac1m\sum_i(f(y_i v_i)-y_i)^2
             =\frac1m\sum_i(f(v_i)-1)^2.                     \tag{12}
\]

Let P be any m-coordinate permutation. Permute the complete lower
coordinate pairs and upper coordinates by S_1(G,zeta)=(PG,Pzeta),
S_2 Xi=P Xi. The normalized feature actions are exactly

\[
 Q_1=\operatorname{diag}(1,P,P),\quad Q_2=\operatorname{diag}(1,P),
 \quad b_l\circ S_l=Q_l b_l,\quad Q_2^TDQ_1=D.                 \tag{13}
\]

This follows directly from the repeated scalar blocks in (6)–(7),
so it includes the actual Cholesky normalization. The full state map

\[
 T_P(w,c,M)=(P^T w\circ S_1,c\circ S_2,Q_2^TMQ_1)              \tag{14}
\]

fixes initialization and is an isometry for
||delta X||^2=E_1|delta w|^2+E_2|delta c|^2+||delta M||F^2.
Substitution gives a_T(u)=Q_1^T a(Pu), H^2_T(u)=H^2(Pu) composed
with S_2, and f_T(u)=f(Pu). The transformed reverse action uses
(Q_2^T M Q_1)^T, the transpose of that same full matrix.

Permutations act transitively on the v_i. Thus both the ambient loss
(12) and F=(1/m)sum_i f(v_i) are invariant. Their metric gradients
are equivariant by the isometry chain rule. Local uniqueness from
the prescribed fixed initial state forces every transformed trajectory
to equal the original one, and hence all f(v_i) are equal to F.
The ambient gradient, with every block retained, is therefore

\[
 \dot X=-\frac2m\sum_i(f(v_i)-1)\nabla f(v_i)
        =2(1-F)\nabla F.                                    \tag{15}
\]

The gradient components remain
grad_c f=H^2, grad_M f=d(u)a(u)^T, and
grad_w f=sech^2(w dot u)Q(u)u, with Q=b_1^T M^T d.
They are the full metric derivatives, with no data-size factor omitted.

Here are the existence checks in the new dimension. Use characteristic
increments in L-infinity(Omega_1;R^m), bounded c on Omega_2, and the
finite full matrix M. Bounded features, unit inputs, and bounded
Lipschitz tanh gates give a locally Lipschitz vector field on bounded
sets; the path-integral contraction proves local existence and
uniqueness exactly as in Section 3 of the frozen candidate. The frozen
g is unbounded but appears only inside bounded gates.

The unchanged physical metric identity mathcal L_dot=-||X_dot||^2
and mathcal L(0)=1 imply (1/m)sum_i |r_i|<=1. Contraction of the
feature maps then gives

\[
 \|c(t)\|_\infty\le2t,\quad
 \|M(t)-D\|_F\le2t^2,\quad
 \|w(t)-g\|_\infty\le B_1(2d_0t^2+2t^4).                    \tag{16}
\]

These bounds and bounded speeds on finite intervals preclude finite
escape in the local-existence space. Cauchy endpoints and the same
local argument yield existence for all finite times. They apply for
each fixed finite m; no dimension-uniform envelope is asserted.

## 4. Scalar potential and the limiting state

For completeness the scalar argument and its normalizations are as
follows. On the auxiliary autonomous curve X_s=grad F from initialization,
c_s=U and the other blocks are the arithmetic means of their full
gradient components. The speed bounds are

\[
 \|c(s)\|_\infty\le s,\quad
 \|M(s)\|_{\rm op}\le d_0+s^2/2,\quad
 \|w(s)-g\|_\infty\le B_1(d_0s^2/2+s^4/8).                   \tag{17}
\]

Thus this curve exists for every finite s. With h=(w,M) and
K=||grad F||^2=C+||grad_h F||^2, the exact identities are

\[
 F_s=K,\qquad q_s=2F,\qquad
 c=sU_0+o(s),\quad F=C_0s+o(s),\quad q=C_0s^2+o(s^2).
\]

For s>0, F and q are positive. Since F^2<=qC<=qK,

\[
 (q/F^2)_s=-2(qK-F^2)/F^3\le0,
 \qquad\lim_{s\downarrow0}q/F^2=1/C_0.
\]

Integrating from a positive lower endpoint and then letting it tend
to zero yields q<=F^2/C_0 and K>=C>=C_0. All the derived nonsingular
inequalities extend to s=0 by continuity. In particular

\[
 \Psi_s=-\frac{2F[(qK-F^2)+(K-C_0)]}{(C_0+F^2)^2}\le0.         \tag{18}
\]

There is one s_* in (0,1/C_0] with F(s_*)=1. The physical clock
s_dot=2(1-F(s)) gives e=1-F>0 at finite time and
e_dot=-2Ke, so e<=exp(-2C_0t) and s(t) increases to s_*.
Composing the auxiliary curve with this clock recovers every block
in (15); uniqueness identifies it with the physical solution. The
clock and s_* are proof objects, not operational state or an oracle.

Writing D_*=(qK-F^2)+(K-C_0)>=0, the full potential derivative is

\[
 \dot\Phi=-4K\Phi
       -\frac{4C_0e^3F D_*}{(C_0+F^2)^2}
       \le-4C_0\Phi.                                      \tag{19}
\]

The bound q<=F^2/C_0 gives 0<C_0 Psi<=1, proving every assertion
in (3)–(4), including the initialized value Phi(0)=2.

Finally ||X_dot||=2e sqrt(K)<=-e_dot/sqrt(C_0), which gives (5).
The limit is the finite-feature-time state X(s_*). Its continuity
in the existence norms supplied by (17) proves essential-supremum
and Frobenius convergence as well as physical Hilbert convergence.
Identical frozen-mark couplings give W2 convergence of both complete
joint laws. Their second moments are finite because g is Gaussian,
the frozen b are bounded, and the moving increments are bounded.
Every original label is fitted, as f(u_i)=y_i F tends to y_i.

## Scope and correlated examples

For i!=j the label-absorbed inner product is

\[
 v_i\cdot v_j=2ab+(m-2)b^2,
\]

and the original inner product is this number times y_i y_j. For
a=2/sqrt(m+3), b=1/sqrt(m+3), the common absorbed correlation is
(m+2)/(m+3); the inputs are linearly independent and can be highly
correlated. Arbitrary label signs introduce no new scalar proof
obligation because loss absorption in (12) is an ambient identity.

The mechanism remains restricted: exact permutation symmetry preserves
one signed residual direction on the initialized trajectory even though
the initialized m-field Gram has full rank. Equal weights and common
unit label magnitudes are part of the theorem. No arbitrary-weight,
arbitrary-geometry, endpoint-Gram, strict-hidden-gain, generic-circle,
or higher-dimensional trained-network conclusion follows from it.
