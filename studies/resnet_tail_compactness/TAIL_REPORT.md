# Neural-PDE high-to-low tail: common-reference degree-7 round

**Date:** 25 July 2026  
**Scope:** canonical dense Euclidean \(\mu\)P residual-\(\tanh\) benchmark  
**Question:** Is the remaining aggregate Hermite feedback gap a bridgeable
shell-multiplicity effect, or a coherent obstruction to arbitrary-accuracy
finite-PDE convergence?

## Executive verdict

This round rules out one important failure mechanism, but it does **not**
close the convergence theorem.

The degree-7 experiment used one parity-reduced high-order trajectory as a
common reference. It therefore measured the actual adjacent projection
commutators without the confound of comparing separately trained low-order
PDEs.

At \(t=0.25\),

\[
C_3=3.2531680\times10^{-3},\qquad
C_5=7.2582602\times10^{-3},\qquad
C_7=9.6223820\times10^{-3}.
\]

Thus

\[
\frac{C_7}{C_5}=1.3257147.
\]

The theorem-facing aggregate commutator has therefore **not** turned over by
degree seven. The normalized observable-generator defect also grew:

\[
\frac{4.8980306\times10^{-5}}
     {3.0283637\times10^{-5}}
=1.6173852.
\]

Those are adverse facts for any claim of already-observed aggregate
convergence.

The mechanism, however, is substantially less adverse:

- after removing only the known shell-cardinality factor,
  \[
  q_7
  =
  \frac{C_7}{C_5}\sqrt{\frac{56}{120}}
  =0.9056355<1;
  \]
- the degree-7 shell has weaker RMS amplitude per mode than degree five for
  \(c,\dot c,h\), and \(p\);
- degree-7 energy is much more distributed across modes, rather than being
  dominated by a new resonant coordinate;
- the dominant successive commutator directions are essentially orthogonal.

In the discrete common-reference calculation, \(99.9989\%\) of the
degree-\(3\to5\) \(B\)-commutator energy lies in Hermite degree five, and
\(99.9983\%\) of the degree-\(5\to7\) energy lies in degree seven. Their
weighted cosine is

\[
4.62\times10^{-4}.
\]

Because \(B\) supplies more than \(99.92\%\) of the squared total
commutator at both rungs, even allowing worst-case alignment of the unsaved
\(c\)-components bounds the full adjacent-commutator cosine by

\[
-1.83\times10^{-4}
\le \cos(\Delta_5,\Delta_7)
\le 1.13\times10^{-3}.
\]

Therefore the observed growth is not a coherent low-mode resonance at this
checkpoint. It is a broader, nearly orthogonal new shell whose aggregate
norm is still increasing.

The strongest defensible conclusion is

\[
\boxed{\text{No finite-level structural obstruction was found.}}
\]

\[
\boxed{\text{Aggregate and observable tail contraction is still unobserved.}}
\]

\[
\boxed{\text{The remaining make-or-break gap is an adjoint/Malliavin
tail-compactness theorem.}}
\]

This moves the theory one significant step closer by isolating a single
analytic mechanism. It does not justify saying that no major gap remains.

## 1. Why this was the highest-leverage test

The preceding round found:

1. the old \(P=5\to15\to35\) comparison was invalid because even Hermite
   shells are symmetry-inert;
2. on the correct odd ladder, the lifted outgoing source contracted sharply;
3. actual aggregate high-to-low feedback still grew from degree three to
   degree five.

The saved data then exposed an important qualification. The old
`R_out_lift` quantity is the velocity of a newly opened shell at a lifted
low-order state with that shell set to zero. It is not the trained
high-shell velocity. At degree five, the actual trained shell velocity was
roughly \(28\)–\(89\) times the lifted boundary diagnostic.

Consequently, another lifted-source measurement would not address the
remaining theorem gap. The correct target is the projection commutator on a
single high-order state:

\[
\Delta_{d\to d+2}(Y)
=
\Pi_d F_{d+2}(\Pi_{d+2}Y)
-
F_d(\Pi_dY).
\]

This simultaneously measures:

- actual trained-shell feedback;
- coherent low-state contamination;
- observable-generator contamination;
- shell amplitude and concentration.

It also avoids evolving redundant lower PDEs.

## 2. Hard-capped design

The main run used:

| item | value |
|---|---:|
| maximum odd Hermite degree | \(7\) |
| full complete-basis size | \(330\) |
| active odd modes | \(200\) |
| depth nodes \(N\) | \(1\) |
| base Gauss-Hermite order | \(8\) |
| base points \(M\) | \(8^4=4096\) |
| parity-paired fast points \(R\) | \(512\) |
| time step | \(0.025\) |
| integrator | explicit midpoint |
| checkpoint | \(t=0.25\) |
| cubature seed | 20260723 |

Even modes were deleted exactly; this is the parity reduction proved and
validated in the preceding round. The Gaussian fast rule was antithetically
paired and block-orthonormalized on the active odd prefixes

\[
4,\ 24,\ 80,\ 200.
\]

Only the degree-7 state was evolved. At the checkpoint, it was projected
through the lower prefixes and their vector fields were evaluated on the
same master quadrature.

### Calibration

Before the high-order run, the same common-reference diagnostic was run
through degree five at \(N=1\) and \(N=2\). The adjacent aggregate ratios
were

\[
1.3732\quad(N=1),
\qquad
1.3835\quad(N=2),
\]

consistent with the earlier \(N=4\) result of approximately \(1.39\).
This makes a gross depth-discretization explanation unlikely, although it
does not certify degree-7 depth convergence.

### Stop rule

The degree-7 run was the only high-order positive-time run. No degree-nine
extension, independent-seed campaign, bootstrap, dense-network campaign, or
new response compiler was authorized.

## 3. Common-reference commutators

Let \(C_d=\|\Delta_{d-2\to d}\|\) in the project's weighted state norm.

| adjacent shell | \(B\)-velocity | \(a\)-velocity | \(c\)-velocity | total \(C_d\) | normalized observable defect |
|---|---:|---:|---:|---:|---:|
| degree \(1\to3\) | \(3.25184\times10^{-3}\) | \(4.64588\times10^{-6}\) | \(9.30013\times10^{-5}\) | \(3.25317\times10^{-3}\) | \(6.02185\times10^{-6}\) |
| degree \(3\to5\) | \(7.25556\times10^{-3}\) | \(2.08310\times10^{-5}\) | \(1.96960\times10^{-4}\) | \(7.25826\times10^{-3}\) | \(3.02836\times10^{-5}\) |
| degree \(5\to7\) | \(9.61952\times10^{-3}\) | \(3.41145\times10^{-5}\) | \(2.32111\times10^{-4}\) | \(9.62238\times10^{-3}\) | \(4.89803\times10^{-5}\) |

For the degree-seven versus degree-five step:

| channel | aggregate ratio | ratio after \(\sqrt{56/120}\) |
|---|---:|---:|
| \(B\)-velocity | 1.32581 | 0.90570 |
| \(a\)-velocity | 1.63768 | 1.11875 |
| \(c\)-velocity | 1.17847 | 0.80505 |
| total state | 1.32571 | 0.90564 |
| output generator | 1.54922 | 1.05832 |
| Gram generator | 1.61739 | 1.10488 |

The total state passes the shell-cardinality-adjusted screen, but the small
\(a\)-channel and both observable channels do not. Cardinality adjustment is
a mechanism diagnostic, not a convergence bound.

## 4. Actual trained-shell structure

The actual shell norms inside the same trained degree-7 state were:

| quantity | degree 5 | degree 7 | aggregate ratio | RMS-per-mode ratio |
|---|---:|---:|---:|---:|
| learned state \(c\) | \(4.77252\times10^{-5}\) | \(6.04330\times10^{-5}\) | 1.26627 | 0.86503 |
| velocity \(\dot c\) | \(4.01395\times10^{-4}\) | \(5.08386\times10^{-4}\) | 1.26655 | 0.86522 |
| forward coefficients \(h\) | \(1.30955\times10^{-3}\) | \(1.73090\times10^{-3}\) | 1.32175 | 0.90293 |
| adjoint coefficients \(p\) | \(1.43739\times10^{-2}\) | \(2.02970\times10^{-2}\) | 1.41207 | 0.96463 |

All four RMS-per-mode quantities contract. The adjoint is the weakest:
its contraction is only \(3.54\%\).

The shell effective participation counts and largest-mode energy fractions
were:

| quantity | \(N_{\rm eff}\), degree 5 | \(N_{\rm eff}\), degree 7 | largest fraction, degree 5 | largest fraction, degree 7 |
|---|---:|---:|---:|---:|
| \(c\) | 2.68 | 21.12 | 0.585 | 0.135 |
| \(\dot c\) | 2.71 | 21.65 | 0.581 | 0.132 |
| \(h\) | 3.19 | 23.41 | 0.530 | 0.112 |
| \(p\) | 4.76 | 25.16 | 0.419 | 0.118 |

This rejects the simplest “one new resonant mode” explanation. It does not
prove cancellation after the nonlinear feedback map.

## 5. Orthogonality audit

The signed \(B\)-commutators were projected back onto the same tensor
Gauss-Hermite basis.

For the degree-\(3\to5\) increment:

- \(99.9989025\%\) of the discrete \(B\)-energy is in degree five;
- only \(0.0010975\%\) lies in all other saved odd degrees.

For the degree-\(5\to7\) increment:

- \(99.9982509\%\) is in degree seven;
- only \(0.0017491\%\) lies in lower saved odd degrees.

The adjacent \(B\)-increment cosine is \(4.6209\times10^{-4}\). Since \(B\)
dominates the full commutator, even adversarial alignment of the unsaved
signed \(c\)-increment leaves the total adjacent cosine within about
\(1.1\times10^{-3}\) of zero.

This matters theoretically. The raw scalar sequence

\[
\|\Delta_3\|,\|\Delta_5\|,\|\Delta_7\|
\]

looks noncontracting, but successive increments are not coherently adding
in one low direction. A Hilbert-space proof may therefore use orthogonal or
square-summable tail control rather than an unnecessarily strong
\(\ell^1\) sum of shell norms.

The observable defect does not inherit a demonstrated orthogonality result;
its signed vectors were not retained. Its \(61.7\%\) growth remains an
unresolved warning.

## 6. The precise theoretical bridge

Let

\[
H_{\rm odd}=L^2_{\rm odd}(\mu)
\]

and let \(\Pi_K\) be projection onto odd Hermites through degree \(2K+1\).
Represent the frozen Gaussian row by one common isonormal process \(W\):

\[
\mathbb E[W(u)W(v)]
=
\sigma_w^2\langle u,v\rangle_H.
\]

For every fixed query \(u\),

\[
\|W(u)-W(\Pi_Ku)\|_{L^2(\Omega)}
=
\sigma_w\|(I-\Pi_K)u\|_H.
\]

For a sufficiently Malliavin-regular adjoint field \(\beta\), Gaussian
integration by parts gives

\[
\mathbb E[W(\phi_\nu)\beta]
=
\sigma_w\,\mathbb E[D_\nu\beta].
\]

Consequently the dangerous shared-transpose tail satisfies the
dimension-free bound

\[
\left\|
(I-\Pi_K)\mathbb E[W\,\beta]
\right\|_H
\le
\sigma_w
\left(
\mathbb E
\left\|
(I-\Pi_K)D\beta
\right\|_H^2
\right)^{1/2}.
\]

The learned-row term has a complementary Cauchy-Schwarz bound in terms of
the \(H\)-tail of \(c\) and moments of \(\beta\).

This yields the following conditional Galerkin statement.

### Conditional compact-time convergence lemma

Assume on \([0,T]\):

1. the infinite cylindrical flow and every odd-Hermite Galerkin flow exist
   uniquely;
2. their trajectory and moment bounds are uniform in \(K\);
3. the vector fields have a \(K\)-uniform local stability constant \(L_T\);
4. the forward query family is relatively compact in \(H_{\rm odd}\);
5. \(c\) is tail-compact in \(L^2(\Omega;H_{\rm odd})\);
6. the Malliavin gradients of the trained adjoint fields are uniformly
   tail-compact;
7. all finite systems are projections of the same isonormal process.

Then bounded \(\tanh,\tanh'\), and \(\tanh''\) give

\[
\eta_K(T)
\le
C_T
\left[
\sup_{q\in\mathcal Q_T}\|(I-\Pi_K)q\|_H
+
\|(I-\Pi_K)c\|_{L^2(\Omega;H)}
+
\|(I-\Pi_K)D\beta\|_{L^2(\Omega;H)}
\right]
\longrightarrow0,
\]

and therefore

\[
\sup_{t\le T}
\|Y_K(t)-\Pi_KY(t)\|
\le
e^{L_TT}
\left(
\delta_K+T\eta_K(T)
\right)
\longrightarrow0.
\]

Locally Lipschitz output and Gram readouts then converge as well.

This is the right theoretical target because the iid Gaussian coefficient
sequence is cylindrical and is not itself an \(\ell^2\) vector. Only its
actions on the compact trained-query family need converge.

## 7. What is now closed and what remains

| issue | status after this round |
|---|---|
| Separately evolved low/high trajectories confound the generator comparison | **Closed.** One high state and exact prefix projections were used. |
| A few degree-7 modes create a new resonance | **Disfavored.** Effective participation rises sharply and largest-mode fractions fall. |
| Successive state commutators align coherently | **Ruled out at this checkpoint.** The dominant \(B\)-increments are shell-orthogonal. |
| Per-mode state/forward/adjoint amplitudes worsen at degree seven | **No.** All RMS-per-mode ratios are below one. |
| Aggregate state commutator contracts | **No.** It grows \(32.6\%\). |
| Observable-generator defect contracts | **No.** It grows \(61.7\%\). |
| Actual trained tail velocity contracts | **No.** Degree-7 \(\dot c\) is \(1.2665\times\) the degree-5 norm. |
| Uniform tail summability on compact time/parameter sets | **Unproved.** This is the central remaining finite-\(P\) theorem gap. |
| Infinite isonormal flow and \(K\)-uniform stability | **Unproved.** Needed by the conditional lemma. |

The empirical evidence favors a bridgeable Hilbert/Malliavin compactness
mechanism over a fundamental static-closure obstruction. But the aggregate
and observable metrics prevent upgrading that preference into a convergence
claim.

## 8. Relation to the full neural-PDE conjecture

Within the finite-P operator hierarchy, the remaining make-or-break item is
now narrow:

> Prove uniform compactness of the trained forward queries, learned row
> field, and especially the adjoint Malliavin-gradient tail, then combine it
> with a cutoff-independent flow stability estimate.

The full dense-network theorem still separately requires:

- ordered width/depth identification of the infinite operator PDE;
- trained-depth homogenization of centered innovations;
- compact-time-to-all-time stability.

Earlier experiments support those mechanisms but do not prove them.
Therefore it would be inaccurate to say that the full convergence theorem
has no major gaps left.

## 9. Budget

Positive-time scientific computation:

- degree-5 \(N=1\) calibration: 11.9 s;
- degree-5 \(N=2\) calibration: 22.0 s;
- degree-7 common-reference run: 166.3 s.

Total positive-time compute was approximately **200 seconds**.

Zero-time feasibility checks used approximately 37 seconds. No additional
scientific trajectory was run after the degree-7 result.

## Final conclusion

The round resolves the uncertainty asymmetrically:

> The remaining feedback growth is not behaving like a coherent, resonant
> high-to-low instability. New-shell modes become individually weaker and
> substantially more diffuse, while the dominant shell increments are
> nearly orthogonal.

But:

> The aggregate state commutator and the observable-generator defect still
> grow through degree seven. Arbitrary-accuracy convergence is therefore not
> empirically established, and the earlier lifted-source contraction must
> not be used as a substitute for actual trained-tail contraction.

The theory is now best viewed as **plausibly bridgeable but not closed**.
The next progress must be analytic—an isonormal/Malliavin tail-compactness
and stability theorem—not another low-order shell sweep.
