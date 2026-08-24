# Three-hidden-layer arctangent: terminal convergence audit

**Status — 21 August 2026:** the exact autonomous operator IDE, its direct
readouts, its compact-time energy bounds, and every fixed-time-mesh width
limit are established.  The unconditional continuous-time iid-Gaussian
width-identification theorem is **open**, not proved or disproved.  This file
records the exact theorem-strength dependency after all isolated proof-search
and hostile-audit rounds.

This claim level is intentional.  The acceptance protocol says that a formal
IDE or a route-level counterexample is not a C6 theorem.  Conversely, failure
of several proof strategies is not a counterexample to the canonical random
trajectory.

## 1. Exact finite system

On (H_{j,n}=(\mathbb R^n,n^{-1}x^{\mathsf T}y)), put

\[
\begin{aligned}
 X_1&=\arctan u,& Z_2&=G_1X_1,&X_2&=\arctan Z_2,\\
 Z_3&=G_2X_2,&X_3&=\arctan Z_3,&f_n&=\langle A,X_3\rangle_n,
\end{aligned}
\]

and (D_\ell=(1+Z_\ell^2)^{-1}), with (Z_1=u).  Define

\[
 B_3=AD_3,qquad R_2=G_2^*B_3,qquad
 B_2=D_2R_2,qquad Q_1=G_1^*B_2 .                    \tag{1.1}
\]

For (r=u+u^3/3) and
((b\otimes x)v=b\langle x,v\rangle_n), feature ascent is exactly

\[
 A'=X_3,qquad r'=Q_1,qquad
 G_1'=B_2\otimes X_1,qquad G_2'=B_3\otimes X_2.      \tag{1.2}
\]

The exact raw tangent kernel is

\[
 K_n=f_n'
 =\|X_3\|_2^2+\|B_3\|_2^2\|X_2\|_2^2
  +\|B_2\|_2^2\|X_1\|_2^2+\|D_1Q_1\|_2^2.          \tag{1.3}
\]

These identities were derived independently and pass central-difference
checks at widths (3,7,19).

## 2. Exact single-time operator contract

Let (H_1,H_2,H_3) be the three probability Hilbert spaces of one joint
pointed Gaussian source.  It contains endpoint marks (a_0,r_0) and two
independent immutable actions

\[
 \Gamma_1:H_1\to H_2,qquad \Gamma_2:H_2\to H_3,      \tag{2.1}
\]

together with their **actual Hilbert adjoints**.  The source is the
projectively realized master law of every fixed finite program which may
alternate each Gaussian action and its transpose.  A transpose is never
replaced by a fresh independent Gaussian.

The evolving state has only

\[
 (A,r,P_1,P_2,e),                                      \tag{2.2}
\]

where (A\in H_3,r\in H_1), (P_1:H_1\to H_2) and
(P_2:H_2\to H_3) are current trace-class operators, and (e\in\mathbb R).
Set (G_\ell=\Gamma_\ell+P_\ell), reconstruct (1.1), and solve

\[
\boxed{
\begin{aligned}
 \dot A&=2\eta eX_3,& \dot r&=2\eta eQ_1,\\
 \dot P_1&=2\eta eB_2\otimes X_1,&
 \dot P_2&=2\eta eB_3\otimes X_2,\\
 \dot e&=-2\eta eK .
\end{aligned}}                                         \tag{2.3}
\]

The predictor, kernel, residual, and loss are the current readouts

\[
 f=\langle A,X_3\rangle,qquad K\text{ from (1.3)},
 \qquad e=y_\star-f,qquad \mathcal L=e^2.             \tag{2.4}
\]

This is a genuine O(1)-species, one-training-time, autonomous contract.
The future uses each (P_\ell(t)) only as a present operator; it cannot
inspect the times at which its rank-one pieces were created.  There is no
DMFT object, response kernel, two-time covariance, path measure, or growing
list of moments.

## 3. What is proved beyond the algebra

On every compact feature interval, uniformly in width,

* (A,r) remain bounded in normalized (L^2);
* (P_1,P_2) remain bounded in trace norm;
* (G_1,G_2) remain bounded in operator norm;
* (B_3,B_2,Q_1) and (K_n) remain bounded in normalized (L^2) or as
  scalars in the exact combinations in which they occur; and
* no finite-time state escape is possible.

At every **fixed** Euler mesh, eliminating the trained matrices gives

\[
\begin{aligned}
G_\ell^kv&=\Gamma_\ell v+
 \sum_{m<k}hB_{\ell+1}^m\langle X_\ell^m,v\rangle,\\
(G_\ell^k)^*w&=\Gamma_\ell^*w+
 \sum_{m<k}hX_\ell^m\langle B_{\ell+1}^m,w\rangle .  \tag{3.1}
\end{aligned}
\]

Thus a fixed mesh is one finite, transpose-reusing, two-matrix Gaussian
program.  Its complete joint empirical law and every fixed polynomial
moment converge.  This proves C0--C2 and fixed-mesh C4.  It does not permit
the number of program steps to diverge with width.

## 4. The exact missing theorem

The learned part of the middle adjoint is harmless:

\[
 P_2(s)^*B_3(s)=\int_0^s X_2(\sigma)
 \langle B_3(\sigma),B_3(s)\rangle\,d\sigma .          \tag{4.1}
\]

Only the adaptive static query (Gamma_2^*B_3) is unresolved.  A sufficient
theorem-strength statement is, for every compact feature horizon (S),

\[
 \sup_{|s|\le S}\|R_{2,n}(s)\|_{\psi_1,n}
 =O_{\mathbb P,S}(1),                                  \tag{4.2}
\]

uniformly also over the cutoff and comparison flows used in mesh removal.
A sufficient finite-width replacement is the reachable-state estimate

\[
 \|R_{2,n}(s)\|_{p,n}\le C_Sp,qquad
 2\le p\le c_S\log n,                                  \tag{4.3}
\]

together with the corresponding exact-versus-mesh stability estimate.
Once the state is stable, one fixed auxiliary mesh transfers square uniform
integrability to (Q_1); controlling (R_2) alone without that transfer is
not enough for the fourth term of (1.3).

The sharp abstract requirement is slightly weaker than exponential tails.
If, on the required high-probability event,

\[
 \tau_S(L)=\sup_{n,h,|s|\le S}
 \|R_{2,n}^h(s)\mathbf1_{\{|R_{2,n}^h(s)|>L\}}\|_{2,n},
\]

then it is enough that

\[
 \omega_S(\delta)=\inf_{L\ge1}\{L\delta+\tau_S(L)\},
 \qquad
 \int_{0^+}\frac{d\delta}{\delta+\omega_S(\delta)}=\infty,             \tag{4.3a}
\]

with the same estimate in the limiting reachable class.  Arbitrary
qualitative square uniform integrability need not satisfy this Osgood
condition.  Equations (4.2)--(4.3) are clean sufficient ways to obtain it.

The obstruction is visible in the exact difference

\[
 D_2R_2-\widetilde D_2\widetilde R_2
 =D_2(R_2-\widetilde R_2)
 +(D_2-\widetilde D_2)\widetilde R_2.                  \tag{4.4}
\]

An arbitrary (L^2) multiplier does not map an (L^2) difference back to
(L^2).  Under (4.2), interpolation gives the Osgood modulus

\[
 \|R\{d(z)-d(\widetilde z)\}\|_2
 \le C\delta\log(e/\delta),qquad
 \delta=\|z-\widetilde z\|_2,                         \tag{4.5}
\]

which supplies uniqueness, mesh removal, and cutoff stability.  Fixed-mesh
moment convergence plus the elementary tail-transfer inequality

\[
 q^2\mathbf1_{|q|>R}
 \le4(q-v)^2+2v^2\mathbf1_{|v|>R/2}                   \tag{4.6}
\]

then identifies all four raw squares in (1.3).  The physical scalar clock
is routine after this feature-time result.

This proves a complete **conditional theorem**.  It does not prove (4.2).

## 5. Audited failed shortcuts

The following conclusions are exact and narrower than a negative theorem
for the canonical trajectory.

1. **Bare (L^2), ordinary action, and intrinsic (L^1) are insufficient.**
   A one-coordinate spike can be invisible to all bounded/action probes but
   carry order-one (G_1^*)-energy and raw kernel.  A bounded-norm
   Householder state even has (K_n'(0)\asymp-\sqrt n) and an order-one
   kernel change in (O(n^{-1/2})).  These states are not canonical iid
   trajectories.

2. **Finite cotangent, log, Jacobian, and polynomial lifts do not close on
   energy balls.**  Their differentiated equations contain multiplication
   by (B_2^2), or (M_aJ+JM_b), and adjoining the next product raises the
   degree again.

3. **A first Gaussian integration by parts is not enough.**  It creates a
   directional Malliavin tangent with no remaining (n^{-1/2}) gain.
   Differentiating that tangent creates mixed responses of every order.

4. **Absolute response/Fock norms are too strong.**  Same-column
   forward--adjoint feedback leaves only one (n^{-1/2}) factor, which the
   final Gaussian contraction cancels.  The derivative exponential
   generating function has radius (O_T(1)), while (4.3) needs radius
   (\asymp\sqrt{\log n}).

5. **A fixed (2+\varepsilon) moment does not follow from fixed meshes.**
   For (Z\sim N(0,1)),
   \[
     Y'=(Z^2/4)Y,\qquad Y(0)=(1+Z^2)^{-1}
   \]
   has every finite moment on every fixed explicit-Euler mesh and a finite
   (L^2) continuum endpoint, but
   (Y(1)\notin L^{2+\varepsilon}) for every (\varepsilon>0).  Thus the
   (p\mapsto2p\) hierarchy cannot be dismissed by short-time restart.

6. **The obvious middle natural coordinate moves rather than removes the
   singularity.**  Uniform local cancellation forces
   (h'(z)=C(1+z^2)).  It creates
   \[
     D_2^{-1}\{\|X_1\|^2I+G_1D_1^2G_1^*\}D_2,         \tag{5.1}
   \]
   whose operator norm is (\Theta_{\mathbb P}(\log n)) at canonical
   initialization.  A moving weighted fiber makes (5.1) bounded but
   introduces an equally nonuniform connection; this is an exact covariant
   reformulation, not yet a uniform Euler theorem.

7. **Layerwise cutoff is circular without a diagonal tail rate.**  Its
   stability factor grows with the cutoff, whereas fixed-level tensor-program
   moments give no bound uniform along the cutoff diagonal.

8. **Entropy and scalar self-quenching do not close.**  Entropy
   differentiation creates higher log-size-biased moments, while the
   arctangent damping identity leaves an off-diagonal cross-layer forcing
   weighted by the very field whose concentration is in question.

9. **The covariant Hilbert bundle is an exact gauge transform.**  If
   (J_\rho v=D(\rho)v), then (J_\rho) is a fiber isometry and
   (J_{\ell+1}T_\ell J_\ell^{-1}=G_\ell).  Parallel-transport comparison
   therefore becomes the original comparison of ((z,G,b)), including the
   same (L^2)-multiplier discontinuity.

10. **Energy-defect/weak--strong uniqueness is conditional, not a source of
    the strong solution.**  Asymmetric decomposition can put the dangerous
    multiplier on a strong reference trajectory, and an Osgood tail bound
    then eliminates the defect.  Constructing that reference without the
    same tail bound is exactly the unresolved step; the scalar defect from
    (f'=K) does not dominate every constitutive cross-term concentration.

11. **A proposed “two-time covariance is unavoidable” objection was
    rejected.**  Such covariances are one possible way to describe joint
    Gaussian path laws, but they are not required as dynamical state.  The
    immutable joint pointed source retains the actions of each
    (Gamma_\ell,Gamma_\ell^*), and the current (P_\ell) retains all
    learned weight memory.  Equation (3.1) proves this at every fixed mesh.
    The unresolved issue is continuity/delocalization when the mesh is
    removed, not a missing second time coordinate.

Initial Gaussian extremes, direct learned-column motion, and a vanishing-time
raw-kernel boundary layer were also attacked.  They do not produce a
nonvanishing canonical defect by the available estimates.  The only
remaining hostile mechanism is adaptive focusing by the reused static
Gaussian matrices; it has neither been exhibited nor ruled out.

## 6. Claim-level verdict

| Obligation | Status |
|---|---|
| C0 exact finite algebra and (f_n'=K_n) | proved |
| C1 joint immutable two-matrix source with actual adjoints | proved for every fixed finite source program |
| C2 exact O(1)-species, single-time, restartable contract | proved algebraically |
| C3 unconditional well-posedness in a restart-stable canonical class | conditional on (4.2) or an equivalent cancellation theorem |
| C4 fixed-cutoff, fixed-mesh width identification | proved |
| C5 mesh/cutoff removal and raw-kernel identification | open; reduced to (4.2)--(4.3) |
| C6 compact physical-time convergence of (f,K,e,\mathcal L) | open because C3/C5 are open |

Accordingly, it would be mathematically false to label the requested L=3
extension a proved theorem today.  It would be equally false to label it
disproved.  The exact autonomous IDE is the right algebraic candidate and
passes every Markov/no-history audit; the canonical continuous-time
delocalization theorem is the sole surviving bridge.

## 7. Reproducibility

Run

```bash
python3 test_finite_identities.py
python3 audit_tail_scaling.py --widths 128 256 512 --horizon 2 --step 0.02
```

The first command is an exact finite identity check.  The second is bounded
numerical evidence only: in the frozen runs, the empirical (L^4,L^8)
norms of (R_2,B_2,Q_1) remained stable as width increased.  It cannot
promote C5.
