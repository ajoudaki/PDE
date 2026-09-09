# Minimal mesh-removal conditions for a width-first continuous-time limit

## 1. Claim hierarchy

Fix hidden depth \(L\).  Write \(F_{N,L}(h)\) for the width-first expected
output after \(N\) population Euler steps of size \(h\).  Five logically
different conclusions must not be conflated.

1. **One scalar, one time.**  For fixed \(T\), the numbers
   \(F_{T/h,L}(h)\) converge along a specified mesh family.
2. **One scalar trajectory.**  Interpolated outputs converge uniformly on
   compact time intervals.
3. **A population state trajectory.**  The complete current fields,
   learned operators, and immutable source actions converge in a specified
   state topology.
4. **A restartable IDE flow.**  The state limit solves an autonomous
   integral equation and is unique in a restart-stable solution class.
5. **The actual finite-width continuous-time limit.**  Exact finite-width
   gradient flows converge uniformly on compact time intervals, and every
   claimed nonlinear or unbounded readout is identified.

A bound on \(F_{N,L}\) alone can prove at most items 1--2.  It cannot prove
items 3--5 without additional state, stability, uniqueness, width-uniform,
and uniform-integrability estimates.

## 2. The exact implication of the proposed \(t^4h^5\) bound

Suppose that, for some \(c_L,C_L<\infty\) and activation integral \(J_L\),

\[
 \left|F_{t,L}(2h)-F_{2t,L}(h)
 +\frac{t(2t-1)}2J_Lh^3\right|
 \le C_Lt^4h^5,
 \qquad 0<h\le c_L/t.                              \tag{2.1}
\]

Set \(T=2th\).  Since \(t(2t-1)/2\le t^2\), (2.1) gives

\[
 \left|F_{t,L}(2h)-F_{2t,L}(h)\right|
 \le h\left(\frac{|J_L|T^2}{4}
              +\frac{C_LT^4}{16}\right).           \tag{2.2}
\]

The radius in (2.1) is equivalent to

\[
 T\le2c_L.                                           \tag{2.3}
\]

Thus (2.1) is a local-in-total-time, first-order global mesh-refinement
estimate.  The fifth-order remainder does not give a fifth-order
continuous-time method: the accumulated cubic discrepancy is already of
order \(h\) at fixed \(T\).

### Proposition 2.1 (scalar dyadic limit)

Assume (2.1).  Fix \(0\le T\le2c_L\), and set

\[
 h_m=T2^{-m},\qquad f_m(T)=F_{2^m,L}(h_m).
\]

Then \((f_m(T))_m\) converges, and with

\[
 A_L(T)=\frac{|J_L|T^2}{4}+\frac{C_LT^4}{16},        \tag{2.4}
\]

its limit \(f_L(T)\) satisfies

\[
 |f_m(T)-f_L(T)|\le A_L(T)h_m.                       \tag{2.5}
\]

#### Proof

To compare levels \(m\) and \(m+1\), use (2.2) with
\(t=2^m\) and fine step \(h_{m+1}\).  Their common total time is
\(2(2^m)h_{m+1}=T\), so

\[
 |f_m(T)-f_{m+1}(T)|\le A_L(T)h_{m+1}.
\]

For \(q>m\), summing gives

\[
 |f_m(T)-f_q(T)|
 \le A_L(T)\sum_{j=m}^{q-1}h_{j+1}
 \le A_L(T)h_m.
\]

Completeness of \(\mathbb R\) and then \(q\to\infty\) prove the claim.
\(\square\)

This proposition is the strongest conclusion obtainable from (2.1)
without another hypothesis.  It gives neither compact-time uniformity nor
mesh-independence outside the chosen dyadic chain.

### Proposition 2.2 (minimal scalar compact-time criterion)

Let \(f_h\) be interpolated scalar trajectories on \([0,T]\).  If, for a
dyadic sequence \(h_m=h_02^{-m}\),

\[
 \|f_{h_{m+1}}-f_{h_m}\|_{C[0,T]}\le a_m,
 \qquad \sum_{m=0}^\infty a_m<\infty,               \tag{2.6}
\]

then \(f_{h_m}\) converges uniformly on \([0,T]\).  This is just the
Cauchy criterion in the Banach space \(C([0,T])\), and summability is the
weakest direct hypothesis of this form.

For grid outputs, (2.2) supplies the aligned-grid part of (2.6).  To obtain
the full supremum norm one additionally needs a mesh-uniform time-increment
bound, for example

\[
 |F_{k+1,L}(h)-F_{k,L}(h)|\le M_T h,
 \qquad kh\le T.                                    \tag{2.7}
\]

Linear interpolation and (2.2) then give \(a_m=O_T(h_m)\), which is
summable.

## 3. A minimal state-level sewing lemma

The right state-level replacement for a scalar remainder is a stable,
summable defect estimate in the topology in which the IDE is to live.
The following lemma is sufficient and exposes every needed assumption.

### Theorem 3.1 (restartable discrete sewing)

Let \(X\) be a Banach space and let \(E_h:X\to X\), \(0<h\le h_T\), be
population one-step maps.  Let \(x_0\in X\).  For each finite \(T\), assume
there is a set \(\mathcal K_T\subset X\), containing every variable-step
trajectory from \(x_0\) of total step at most \(T\), and constants
\(M_T,L_T<\infty\), such that for \(x,y\in\mathcal K_T\),

\[
 \|E_hx-x\|\le M_Th,                                \tag{3.1}
\]

\[
 \|E_hx-E_hy\|\le(1+L_Th)\|x-y\|.                  \tag{3.2}
\]

Assume also that there is a nonnegative modulus \(\rho_T\) with

\[
 \|E_h(E_hx)-E_{2h}x\|\le h\rho_T(h)                \tag{3.3}
\]

whenever all three states occur in \(\mathcal K_T\), and that for one,
hence every sufficiently small, \(h_0\),

\[
 \sum_{m=0}^{\infty}\rho_T(h_02^{-m})<\infty.       \tag{3.4}
\]

Let \(X_h\) be the piecewise-linear interpolation of
\(E_h^kx_0\).  Then the dyadic interpolants \(X_{h_02^{-m}}\) converge
uniformly on \([0,T]\) to an \(M_T\)-Lipschitz curve \(X(\cdot)\).
More precisely,

\[
 \|X_h-X_{2h}\|_{C([0,T];X)}
 \le \frac T2e^{L_TT}\rho_T(h)+2M_Th.               \tag{3.5}
\]

#### Proof

At common coarse-grid times put

\[
 y_j=E_{2h}^jx_0,\qquad z_j=E_h^{2j}x_0.
\]

From (3.2)--(3.3),

\[
\begin{aligned}
 \|y_{j+1}-z_{j+1}\|
 &\le\|E_{2h}y_j-E_h^2y_j\|
      +\|E_h^2y_j-E_h^2z_j\|\\
 &\le h\rho_T(h)+(1+L_Th)^2\|y_j-z_j\|.
\end{aligned}                                       \tag{3.6}
\]

Iteration, \((1+L_Th)^{2j}\le e^{2L_Thj}\), and
\(j\le T/(2h)\) give

\[
 \max_{2jh\le T}\|y_j-z_j\|
 \le\frac T2e^{L_TT}\rho_T(h).                     \tag{3.7}
\]

Between common endpoints, (3.1) bounds the displacement of either linear
interpolant by at most \(2M_Th\).  This proves (3.5).  Equations
(3.4)--(3.5), together with \(\sum_mh_02^{-m}<\infty\), make the dyadic
interpolants Cauchy in \(C([0,T];X)\).  Their segment slopes are at most
\(M_T\), so the uniform limit is \(M_T\)-Lipschitz. \(\square\)

A usual polynomial local defect

\[
 \|E_h^2x-E_{2h}x\|\le C_Th^{1+\alpha},\qquad\alpha>0, \tag{3.8}
\]

corresponds to \(\rho_T(h)=C_Th^\alpha\) and satisfies (3.4).  For a
first-order Euler method \(\alpha=1\), giving a global \(O_T(h)\) mesh
error.

The polynomial form is not essential.  What is essential for this direct
sewing argument is summability of the propagated refinement errors.  A
bare \(o(h)\) local defect can be insufficient if its normalized modulus is
not dyadically summable.

## 4. When the sewn curve is an IDE solution

State convergence alone does not identify an equation.  Add a vector field
\(V:\mathcal K_T\to X\) and assume the generator consistency

\[
 E_hx=x+hV(x)+hr_h(x),
 \qquad
 \sup_{x\in\mathcal K_T}\|r_h(x)\|\xrightarrow[h\downarrow0]{}0, \tag{4.1}
\]

with \(V\) bounded and uniformly continuous on the reachable tube.  Then
the limit in Theorem 3.1 satisfies

\[
 X(t)=x_0+\int_0^tV(X(s))\,ds.                       \tag{4.2}
\]

Indeed, at mesh points the Euler sum is

\[
 E_h^kx_0=x_0+h\sum_{j<k}V(E_h^jx_0)
              +h\sum_{j<k}r_h(E_h^jx_0).             \tag{4.3}
\]

The last sum is at most
\(T\sup_{\mathcal K_T}\|r_h\|\).  Uniform state convergence and uniform
continuity of \(V\) turn the first sum into the Bochner integral in (4.2).

For the exact population Euler map

\[
 E_hx=x+hV(x),                                      \tag{4.4}
\]

generator consistency is automatic.  It is not automatic from scalar
output data \(F_{N,L}(h)\).

### Uniqueness and restartability

Suppose, on the named solution class,

\[
 \|V(x)-V(y)\|\le\omega_T(\|x-y\|),                 \tag{4.5}
\]

where \(\omega_T\) is increasing, \(\omega_T(0)=0\), and

\[
 \int_{0^+}\frac{dr}{\omega_T(r)}=\infty.           \tag{4.6}
\]

The integral inequality obtained from (4.2), followed by
Bihari--Osgood, gives uniqueness.  Lipschitz continuity is the special
case \(\omega_T(r)=L_Tr\).

If (3.1)--(4.6) hold after restarting from every reachable state, with the
same immutable Gaussian source retained as part of the pointed state, then
uniqueness gives

\[
 \Phi_{t+s}(x)=\Phi_t(\Phi_s(x)),                    \tag{4.7}
\]

so the limit is an autonomous restartable flow.  Estimates proved only from
the initialization do not imply (4.7), and a local radius such as
\(T\le2c_L\) cannot be iterated unless the constants are controlled after
restart.

## 5. A still weaker but more intrinsic formulation

The Lipschitz stability (3.2) is convenient, not logically indispensable.
For reachable nonlinear Gaussian systems the sharp estimate may be Osgood.
The minimal replacement is a **forced-trajectory stability statement**:
there exists \(\Gamma_T(r)\downarrow0\) as \(r\downarrow0\) such that any
two variable-step trajectories in the solution class, whose initial
distance plus total inserted local error is at most \(r\), remain within
\(\Gamma_T(r)\) on \([0,T]\).                         \tag{5.1}

If the sum of the local coarse/fine defects over \([0,T]\) tends to zero,
(5.1) makes the mesh trajectories Cauchy.  Bihari--Osgood estimates in the
arctangent and conditional tanh IDE analyses are examples of (5.1).
Merely proving an unforced uniqueness inequality is not enough: mesh
removal needs stability under the accumulated local truncation errors.

## 6. Width-first population flow versus the finite-width flow

The preceding results construct a limit after taking width first at each
fixed mesh.  To prove that the actual finite-width continuous gradient flow
has the same limit, one needs a separate triangular argument.

Let \(X_n(t)\) be the exact finite-width flow, \(X_{n,h}(t)\) its Euler
interpolation, \(X_h(t)\) the width-first population Euler trajectory, and
\(X(t)\) the IDE solution.  A sufficient set of statements is:

1. **Fixed-mesh width identification.**  For every fixed \(h>0\),
   \(X_{n,h}\to X_h\) in the chosen action/state topology as
   \(n\to\infty\).
2. **Dimension-free finite-width mesh removal.**  For every \(T,\epsilon\),
   
   \[
   \lim_{h\downarrow0}\limsup_{n\to\infty}
   \Pr\!\left(\|X_n-X_{n,h}\|_{[0,T]}>\epsilon\right)=0. \tag{6.1}
   \]
3. **Population mesh removal.**  \(X_h\to X\) uniformly on \([0,T]\),
   supplied for example by Theorem 3.1.

Choose \(h\) first, take \(n\to\infty\) at that fixed mesh, and only then
send \(h\downarrow0\).  The triangle inequality proves the compact-time
width limit.  Fixed-program convergence with constants depending on the
number of steps does not prove (6.1), and choosing a diagonal mesh
\(h_n\downarrow0\) without (6.1) is an unsupported limit exchange.

This is precisely the distinction visible in the operator-IDE studies:

- the arctangent depth-two proof has a dimension-free exact-versus-Euler
  estimate on cutoff state balls and then removes the cutoff;
- the depth-three tanh study has fixed-mesh identification but its
  positive-time nonzero-label theorem remains open because the reachable
  adaptive-transpose tail/stability bridge is missing.

## 7. Observables and uniform integrability

Even strong convergence of some state coordinates need not identify every
claimed readout.

- If an observable \(\mathcal O\) is continuous in the chosen state
  topology and uniformly bounded on the reachable set, state convergence
  gives \(\mathcal O(X_h)\to\mathcal O(X)\).
- For an unbounded observable such as a squared cotangent norm or tangent
  kernel, weak convergence and \(L^2\) boundedness are insufficient.  One
  needs uniform integrability, a tail estimate, or convergence in a topology
  strong enough to make that observable continuous.
- Convergence of the expected predictor \(F_{N,L}\) is weaker still: it
  neither gives convergence in probability of the predictor nor controls
  its gradient/kernel.

The square-tail transfer in the arctangent IDE proof is therefore a
logically separate bridge, not a consequence of scalar mesh consistency.

## 8. Adversarial counterexamples to common shortcuts

### 8.1 Perfect scalar convergence with no state limit

Let the output ignore a second state coordinate, and let

\[
 E_h(x,y)=(x,y+h\,a(h)),
\]

where \(a(h)\) is bounded and satisfies \(a(h/2)=a(h)\) but takes different
values on different dyadic equivalence classes.  The scalar output \(x\)
has zero refinement error.  Along each dyadic mesh the hidden coordinate
has a limit with slope \(a(h_0)\), but different starting meshes give
different limits.  Thus even zero scalar error, a one-step \(O(h)\) bound,
and exact dyadic consistency do not identify a mesh-independent state flow.
Generator consistency in (4.1), or an all-mesh substitute, is necessary.

### 8.2 Euler convergence does not prove IDE uniqueness

For

\[
 x'=\sqrt{|x|},\qquad x(0)=0,                         \tag{8.1}
\]

explicit Euler remains identically zero and therefore converges.  The ODE
also has delayed nonzero solutions.  Hence convergence of one selected mesh
trajectory is not uniqueness or restartability; an Osgood/Lipschitz
comparison hypothesis is separate.

### 8.3 Initialization-only estimates do not restart

A refinement estimate can hold for every partition starting at \(x_0\)
while failing at a state reached later, because the output may hide an
unstable component until that time.  Extending the local interval
\(T\le2c_L\) requires a reachable-state estimate, not repeated invocation
of an initialization theorem.

### 8.4 Weak state limits can lose the kernel

A normalized vector can put order-one square energy on \(o(n)\) coordinates
while converging against every bounded coordinate test.  A reused transpose
can select that energy.  Consequently weak program convergence or bounded
empirical tests can coexist with failure of a squared-gradient readout.
This is why square-uniform integrability is explicit in the IDE audits.

## 9. Minimal actionable lemma for the MFP program

For the MFP population dynamics, the most useful single next theorem is not
another scalar Taylor coefficient.  It is the following reachable-state
statement.

**Reachable population mesh lemma.**  For each fixed \(L,T\), construct a
complete pointed state space \(X_L\), including the immutable reused-matrix
source, and activation-defined constants/moduli such that:

1. every variable-step population Euler history of total variation at most
   \(T\) remains in a common reachable class \(\mathcal K_{L,T}\);
2. its one-step map is consistent with one autonomous vector field in the
   sense of (4.1);
3. forced trajectories satisfy (5.1);
4. the local split defect has a summable modulus uniformly over
   \(\mathcal K_{L,T}\);
5. the state topology makes every desired bounded readout continuous, and
   separate uniform-integrability bounds cover each unbounded kernel
   readout.

This lemma immediately yields a unique restartable population IDE by
Theorems 3.1 and Section 4.  If it is supplemented by the finite-width
uniform estimate (6.1) and fixed-mesh width identification, it yields the
actual compact-time width theorem.

For the current time-doubling study, the missing horizon-uniform
generated-response estimate at \(L\ge2\) is exactly part of items 1, 3, and
4.  The scalar \(t^4h^5\) remainder would be a consequence at the predictor
level, but it is neither necessary nor sufficient for the full IDE theorem.

## 10. Final conclusion

The weakest direct scalar requirement is a summable compact-time
coarse/fine discrepancy.  The proposed \(t^4h^5\) bound supplies it locally
after the cubic term is included, producing an \(O(h)\) dyadic scalar limit.

The weakest useful IDE requirement is instead a summable **state-level**
local defect plus forced-trajectory stability, generator consistency, and a
restartable uniqueness class.  Compact-time identification of the actual
finite-width gradient flow additionally requires dimension-free
finite-width mesh removal and uniform integrability for unbounded readouts.
None of those stronger conclusions follows from convergence of
\(F_{N,L}(h)\) alone.
