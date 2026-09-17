# Orthogonal endpoint: isolated transverse rank loss

2026-09-16. Frozen scoped analytic continuation. No numerical run was made.
This is an internally derived study result, not promoted material.

Scientific inputs were `docs/README.md`, `docs/NOTATION.md`, complete
`docs/observable_p1.md`, `docs/global_nonlinear.md` C.4.7.9 and
C.4.7.10 B/C.1/D.3, and this study's complete
`three_coordinate_candidate.md` and `perturbation_orthogonal.md`.
The required investigate-conjectures and solve-math-rigorously skills were
used. No other study, route report, review, numerical result or canonical
code was consulted.

**Conclusion.** The prescribed orthogonal initialized flow can lose transverse
tangent rank only at isolated feature times. On every compact feature-time
interval there are finitely many such times, and the transverse eigenvalue
has a strictly positive quadratic leading coefficient at each of them.
Equivalently, among positive common label amplitudes in any bounded interval,
only finitely many can have a degenerate fitting endpoint. This is an
unconditional theorem for the prescribed initialization. It does **not**
exclude the specified unit label amplitude from that finite exceptional set.
The original unit-amplitude endpoint question remains open in this route.

## 1. Fixed object and notation

Keep exactly the Gaussian population p=1 initialization, eta=1/4096,
normalized lower/upper features, full evolving 4-by-7 matrix with its actual
transpose, and population-L2/Frobenius metric of the candidate. The signed
orthogonal inputs and labels are

\[
 (u_1,u_2,u_3)=(e_1,e_2,-e_3),\qquad (y_1,y_2,y_3)=(1,1,-1).
\]

After the exact absorption of the third sign, write

\[
 f_i=f(e_i),\quad a_i=a(e_i),\quad d_i=d(e_i),\quad
 z_i=b_2^TMa_i,\quad H_i=\tanh z_i,\quad
 Q_i=b_1^TM^Td_i,\quad F=\frac13\sum_i f_i.
\]

The auxiliary curve is the exact initialized gradient curve

\[
 X_s=\nabla F,\qquad
 c_s=\frac13\sum_iH_i,\quad
 M_s=\frac13\sum_i d_i a_i^T,\quad
 (w_i)_s=\frac13\operatorname{sech}^2(w_i)Q_i.           \tag{1}
\]

The candidate proves existence for all finite s, the permutation and
simultaneous-negation symmetries, and

\[
 C(s)=E_2[(H_1+H_2+H_3)^2/9]\ge C_0>0,\qquad
 F_s=\|\nabla F\|^2\ge C_0.                            \tag{2}
\]

Removing inactive constant coordinates for notation gives b1 in R6,
b2=Z/R_Z in R3, and M in R^(3-by-6), where

\[
 Z_i=\tanh\Xi_i,\quad R_Z=\sqrt{\tau+\eta},\quad
 S=Z_1+Z_2+Z_3.
\]

The scalar permutation contractions theta_perp and theta_parallel of the
input report give

\[
 z_i=\frac1{R_Z}\left[\theta_\perp(Z_i-S/3)
                          +\theta_\parallel S/3\right]. \tag{3}
\]

Let lambda_perp denote either of the two equal transverse eigenvalues of
the unweighted full prediction tangent Gram. The exact identities from the
input report are

\[
 \lambda_\perp
 =\frac12 E_2[(H_1-H_2)^2]
  +\frac12\|d_1a_1^T-d_2a_2^T\|_F^2
  +E_1[\operatorname{sech}^4(w_1)Q_1^2],               \tag{4}
\]
\[
 \lambda_\perp=0
 \quad\Longleftrightarrow\quad
 \theta_\perp=d_\parallel=0,
 \qquad
 \lambda_\parallel=3\|\nabla F\|^2\ge3C_0.             \tag{5}
\]

Here [d1 d2 d3]=d_perp P_perp+d_parallel P_parallel. The input report
establishes (5); the new conclusion below is a reachability restriction
beyond this criterion, not an assertion that the criterion is excluded.

## 2. The derivative at any degenerate time is nonzero

Suppose lambda_perp(s0)=0 for some finite s0. Equation (5) gives
theta_perp(s0)=d_parallel(s0)=0. Equation (3) then gives identical upper
preactivations z_i=kS, where

\[
 k=\frac{\theta_\parallel(s_0)}{3R_Z}\ne0.             \tag{6}
\]

Indeed k=0 would give all H_i=0 and contradict (2).
At theta_perp=0 the input report's exact symmetry calculation gives
d_perp=0. Thus all d_i=0, hence all Q_i=0. Equation (1) consequently gives,
at s0,

\[
 M_s=0,\quad w_s=0,\quad (a_i)_s=0,\quad (z_i)_s=0,
 \qquad c_s=H:=\tanh(kS).                              \tag{7}
\]

Differentiate the definition d_i=E_2[b2 c sech^2(z_i)]. The upper features
are bounded, c is locally bounded, and the gate and its derivative are
bounded, so differentiation under expectation is justified. By (7),

\[
 (d_i)_s(s_0)=E_2[b_2 H\operatorname{sech}^2(kS)]
             =\frac{\delta}{3}\mathbf1,
\]
\[
 \delta:= (d_\parallel)_s(s_0)
 =\frac1{R_Z}E_2[S\tanh(kS)\operatorname{sech}^2(kS)]. \tag{8}
\]

The equality of the three coordinates uses exchangeability; summing them
gives the displayed scalar. The integrand in (8) has the strict sign of k
whenever S is nonzero. The upper mark law has positive density on the open
cube, so S is not zero almost surely. Therefore

\[
 \delta\ne0,\qquad \operatorname{sign}\delta
                         =\operatorname{sign}k.         \tag{9}
\]

This derivative does not assume that s0 is the first degenerate time or a
fitting endpoint. In particular it applies at the candidate's finite
unit-amplitude fitting time if that time is degenerate.

The local vector field and the scalar contractions are continuously
differentiable in the characteristic norms: tanh and its derivatives are
bounded, features are bounded, and products use bounded c and finite M on
each local existence ball. The unbounded frozen Gaussian g occurs only
inside gates. Thus d_parallel' is continuous near s0. Equation (9) makes
d_parallel strictly monotone on some neighborhood of s0 and permits only
one zero there. Equation (5) then makes s0 an isolated rank-loss time.

## 3. Exact quadratic behavior of the transverse eigenvalue

All unmarked quantities in this section are evaluated at s0. Put

\[
 V=b_1^TM^T\mathbf1,
 \qquad
 J_0=\frac{\|a_1-a_2\|^2}{6}
       +\frac19 E_1[\operatorname{sech}^4(w_1)V^2].     \tag{10}
\]

The coefficient J0 is strictly positive. To check this, write M in its
permutation blocks. Equation (6) implies m_parallel is nonzero, since
theta_parallel=m_parallel^T a_parallel. Hence M^T1 is nonzero. The six
active lower features are linearly independent in L2: normalization is
invertible, and for a vanishing linear combination of raw h_j,k_j,
conditioning on G leaves independent reverse noises with strictly positive
conditional variance in each k_j. All k_j coefficients must vanish.
Independence and positive variance of the h_j then force their coefficients
to vanish. Consequently V is nonzero in L2. Each w1 is finite almost
surely at finite s0, so sech^4(w1)>0 almost surely, giving

\[
 E_1[\operatorname{sech}^4(w_1)V^2]>0.                 \tag{11}
\]

For h=s-s0, (7) and (8) imply

\[
 d_i(s)=\frac{\delta h}{3}\mathbf1+o(h),\qquad
 Q_i(s)=\frac{\delta h}{3}V+o(h).                       \tag{12}
\]

The second remainder is in L-infinity because b1 is bounded and M,d_i
are finite-dimensional continuously differentiable curves. Also
H1(s)-H2(s)=o(h) in L-infinity: the difference is zero at s0 and both
upper preactivation derivatives vanish there. Therefore the first term
of (4) is o(h^2). The middle-gradient difference satisfies

\[
 d_1(s)a_1(s)^T-d_2(s)a_2(s)^T
 =\frac{\delta h}{3}\mathbf1(a_1-a_2)^T+o(h).
\]

Since ||1||^2=3, its half squared norm is
delta^2 h^2 ||a1-a2||^2/6+o(h^2). Continuity of the first-layer gate in
L-infinity and (12) give the remaining term of (4). In total,

\[
 \lambda_\perp(s)
       =\delta^2 J_0(s-s_0)^2+o((s-s_0)^2),
 \qquad J_0>0.                                        \tag{13}
\]

Thus the transverse Gram loses rank quadratically at any such event.
In particular, for some positive constants c,C and sufficiently small
nonzero |s-s0|,

\[
 c(s-s_0)^2\le\lambda_\perp(s)\le C(s-s_0)^2.          \tag{14}
\]

This is stronger than an unquantified assertion that isolated zeros are
generic. It is an exact local conclusion at every possible rank-loss
time of the actual initialized curve.

## 4. Finitely many exceptional times and label amplitudes

At s=0, the initialized upper-field Gram is positive definite, so
lambda_perp(0)>0. On every [0,T], lambda_perp is continuous. Its zero set
there is closed and hence compact. Every zero is isolated by Section 2.
If this compact set were infinite, a sequence of distinct zeros would have
an accumulation point in the set, contradicting isolation. Therefore the
set is finite.

For the amplitude consequence only, explicitly consider labels
(a,a,-a) with a>0 and the same three inputs and initialization. This is a
separate consequence, not a replacement of the required unit-label target.
Permutation invariance gives the same feature curve (1), and physical time
satisfies ds/dt=2(a-F(s)). Equation (2) gives a unique fitting time

\[
 s_a=F^{-1}(a),\qquad 0<s_a\le a/C_0.                  \tag{15}
\]

On [0,s_a] the continuous K=F_s is bounded and bounded below by C0.
The residual e=a-F(s(t)) obeys e'=-2Ke, starting at a, so e stays
positive at finite physical time and tends exponentially to zero. Thus
s(t) increases to s_a, exactly as in the candidate's unit-label proof.

For any A>0, every degenerate fitting endpoint with 0<a<=A corresponds
by (15) to a zero of lambda_perp on [0,A/C0]. There are finitely many.
Away from these amplitudes the full tangent Gram at the fitting endpoint
is positive definite by (5). Positivity persists on an open amplitude
neighborhood by continuity and the strictly increasing continuous inverse
of F. Consequently the admissible positive amplitudes are open and dense,
and the exceptional amplitudes form a locally finite set, with no
accumulation at zero.

## 5. The remaining unit-amplitude gap

The theorem does not decide whether a=1 is exceptional. Finiteness,
isolated zeros, and a nonzero derivative of d_parallel do not exclude one
specified number. No genericity claim is substituted for that exclusion.

Several tempting shortcuts remain invalid. Positive lower response
matrices and the exact first-layer coordinate transform control local
motion, but do not fix the sign of m_perp^T a_perp under common-mode
motion. Nonvanishing m_perp alone does not control that scalar projection.
At a putative rank-loss time, (8) forces d_parallel to cross zero in the
direction sign(theta_parallel); the available initialized estimates do
not prohibit the opposite sign immediately before that time. The
normalized-readout estimate controls the parallel prediction and does
not provide this missing sign invariant.

The unresolved statement for the original target remains the exclusion
of a rank-loss time s with F(s)=1. Nothing here proves that exclusion or
constructs a reachable counterexample. The arbitrary fitting singular
states in the input report also do not establish reachability.

| Claim | Status | Exact scope |
|---|---|---|
| Nonzero d_parallel derivative at transverse degeneracy | Proved here | Every finite degenerate time of the fixed initialized curve |
| Positive quadratic transverse eigenvalue coefficient | Proved here | Equation (13), using the actual first-layer gradient |
| Finitely many rank-loss times on each compact interval | Proved here | The same fixed initialized curve |
| Finitely many exceptional amplitudes in every bounded positive range | Proved here | Labels (a,a,-a), same orthogonal inputs and initialization |
| Full tangent rank at the unit-amplitude fitting endpoint | Open | The specifically requested original endpoint |
| Absence of rank loss at every finite feature time | Open | Stronger than the endpoint target |

No initial-rank inference, numerical evidence, architecture change,
changed optimizer, hidden trajectory input, or other-study result is used.
