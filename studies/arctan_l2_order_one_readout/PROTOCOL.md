# Nonlinear two-hidden-layer operator-IDE resolution protocol

Status: completed; arctangent passed C0--C5, 21 August 2026.  The frozen
criteria below are retained as the prespecified audit protocol.

## 1. Finite-width model

Let \(H_n=\mathbb R^n\) with
\(\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w\).  The independent
initial fields \(A_0,u_0\) have iid \(N(0,1)\) coordinates and
\(G_0=W/\sqrt n\), where the entries of \(W\) are iid \(N(0,1)\).
For one scalar input and one scalar output, put

\[
 X=\phi(u),\qquad Z=GX,\qquad Y=\phi(Z),\qquad
 f_n=\langle A,Y\rangle_n .
\]

With \((p\otimes r)v=p\langle r,v\rangle_n\), define

\[
 B=A\odot\phi'(Z),\qquad R=G^*B.
\]

The exact feature-ascent equations are

\[
 A'=Y,\qquad G'=B\otimes X,\qquad
 u'=\phi'(u)\odot R.                                    \tag{1.1}
\]

The feature kernel is

\[
 K_n=\langle Y^2\rangle_n
 +\langle B^2\rangle_n\langle X^2\rangle_n
 +\langle \phi'(u)^2R^2\rangle_n=f_n'.                 \tag{1.2}
\]

Full-MSE physical time multiplies (1.1) by \(2\eta e_n\), where
\(e_n=y_\star-f_n\), and

\[
 \dot e_n=-2\eta e_nK_n,\qquad \mathcal L_n=e_n^2.      \tag{1.3}
\]

An overall deterministic normalization of \(\phi\) is allowed.  Changing
the initialization, freezing a layer, using different activations in the two
hidden layers, or replacing true derivatives by surrogate derivatives is not
allowed in the primary claim.  Such variants may only be recorded as scoped
comparators.

## 2. Primary conjecture

There exists a non-affine scalar activation \(\phi\), nondegenerate in the
sense that \(\phi'\ne0\) on a set of positive Gaussian measure, for which the
canonical iid-Gaussian width limit of (1.1)--(1.3) is described by a single
deterministic autonomous and restartable operator IDE having:

1. one immutable, explicitly specified Gaussian pointed source;
2. a width-independent finite number of current vector, operator, scalar, or
   probability-measure fields;
3. no second training time, response kernel, history variable, or externally
   supplied clock;
4. current-state formulas for \(f,K,e\), and the loss;
5. a named solution class in which existence and uniqueness hold; and
6. compact-physical-time convergence in probability of the finite-width loss
   curve, with the predictor and every asserted kernel readout identified.

The source and a field may be infinite-dimensional; the number and type of
fields cannot grow with width, time discretization, or requested Taylor
order.  A projective measure that merely renames the full unresolved moment
hierarchy does not count unless tightness, all nonlinear identifications, and
uniqueness in a stated growth class are proved.

## 3. Decision problem

The selected activation must optimize two competing costs.

* **Contract cost:** exact algebra, number of fields, source complexity, and
  directness of the \(f,K\) readouts.
* **Identification cost:** well-posedness, uniform integrability, source
  convergence, compactness, nonlinear limit passage, and uniqueness.

The following families must be compared before selection: superlinear
polynomials, bounded smooth monotone activations, bounded oscillatory
activations, piecewise-linear activations, and globally Lipschitz residual
perturbations of identity.  Degenerate step/sign activations whose hidden
gradients vanish almost everywhere are excluded as easier-model
substitutions.

## 4. Claim ladder

* **C0 (exact finite algebra):** (1.1)--(1.3) and any changed variables are
  verified at every finite width.
* **C1 (source):** the immutable pointed Gaussian source is constructed and
  its finite-width convergence is proved for the operations actually used.
* **C2 (formal IDE):** a finite-field autonomous current-state system and
  raw readouts are written exactly.
* **C3 (well-posed IDE):** the vector field and readouts are defined and
  unique in a named, restart-stable class on every finite physical interval.
* **C4 (width identification):** finite-width trajectories and claimed
  readouts converge on compact physical-time intervals.
* **C5 (resolved conjecture):** C0--C4 all hold for one admissible genuinely
  nonlinear activation, and the loss identity is internal to the IDE.

No formal jet agreement, cutoff calculation, or finite-width simulation can
promote a claim past C2.

## 5. Prespecified falsifiers and hostile checks

The primary claim fails if any of the following remains unproved.

1. A displayed product is not defined on the claimed solution class.
2. The raw \(f\) or \(K\) readout is not finite and continuous in the
   topology used for identification.
3. A cutoff is introduced without a uniform cutoff-removal estimate for the
   canonical iid trajectory.
4. Pointed source convergence is asserted only for polynomials although the
   IDE uses an unproved nonlinear functional calculus.
5. Compactness loses an adaptive row/column correlation needed by \(G\) or
   \(G^*\).
6. Uniqueness is inferred from coordinatewise moment equations without a
   quasi-analytic or otherwise determinate growth class.
7. A nonsmooth activation uses an unspecified derivative at kinks or ignores
   crossings/local time.
8. A perturbation of identity is called nonlinear while the proof silently
   sends the perturbation strength to zero.
9. The description stores a forbidden second time or the entire finite-width
   sequence under a new name.

The quadratic one-cell and adaptive-alignment witnesses remain mandatory
diagnostics.  They refute only a candidate or proof topology to which their
hypotheses apply; they are not universal no-go theorems for canonical
Gaussian initialization.

## 6. Evidence policy

Every result is labeled exact, proved limit theorem, conditional theorem,
formal construction, numerical evidence, or refuted route.  Later hostile
audits supersede earlier drafts.  The final theorem must contain a separate
claim-boundary section and must state every external theorem together with
the hypotheses used.
