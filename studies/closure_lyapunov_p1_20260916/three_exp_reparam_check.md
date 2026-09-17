# Conditional exponential potential: bounded analytical check

2026-09-16. This is a post-freeze check of the supervisor's supplied
variational construction. The original independent invariant report is
unchanged. The additional scientific input read in full was
`generic3_stationary_geometry.md`. No numerical work, external theorem,
other current route, or unassigned study was used.

**Verdict:** the construction is valid conditional on a declared fixed
readout bound and a fixed loss sublevel strictly below `1/3`. Specify
`C>0` and `0<ell<1/3`; the case `ell=0` is already fitted and trivial.
The envelope can also be written as one compact variational problem,
which makes its regularity and empty-set convention particularly clear.
Neither version proves that the initialized trajectory satisfies these
two hypotheses.

## 1. The compact feasible set and the readout norm constraint

Let `Z=(tanh xi_1,tanh xi_2)` have the canonical upper mark law. Its
density is positive on `(-1,1)^2`. Let

\[
 \mathcal F=\overline{\{\tanh(Z\cdot v):v\in\mathbb R^2\}}^{L^2}.
\]

The supplied source proves that this is compact and consists exactly of
the finite-coefficient tanh fields and the fields `sign(Z.d)` with
`|d|=1`. This compactness can also be represented by a finite-dimensional
compact parameter space. For `p` in the closed unit disk, define

\[
 V(p)=
 \begin{cases}
 \tanh\bigl(Z\cdot p/(1-|p|)\bigr),&|p|<1,\\
 \operatorname{sign}(Z\cdot p),&|p|=1.
 \end{cases}                                                   \tag{1}
\]

This map is continuous into `L2`. At an interior point use the Lipschitz
property of tanh. At a boundary point `p`, the coefficient lengths tend
to infinity with directions tending to `p`; pointwise convergence holds
off `Z.p=0`, a null line. All fields are bounded by one, so bounded
convergence gives `L2` convergence. The image of (1) is exactly
`mathcal F`.

For three fields `V_i`, let `G_ij=E[V_iV_j]`, and for a margin vector
`m in R^3` put

\[
 L(m)=\frac13|m-\mathbf1|^2,\qquad
 A(G,m)=\frac49(\mathbf1-m)^TG(\mathbf1-m).
\]

Define the full feasible set

\[
 \Omega_\ell=\left\{(V,m)\in\mathcal F^3\times\mathbb R^3:
       L(m)\le\ell,\quad
       \begin{pmatrix}G&m\\m^T&C^2\end{pmatrix}\succeq0\right\}.
                                                               \tag{2}
\]

It is compact: the three fields belong to a compact set; the margin
vectors belong to the closed ball `|m-1|<=sqrt(3ell)`; all Gram entries
are continuous under strong `L2` convergence; and the positive
semidefinite matrix cone is closed. The latter fact follows directly by
taking limits of its nonnegative quadratic forms.

The block condition in (2) is exactly the existence of a common readout
`c` with `||c||_2<=C` and `m_i=E[cV_i]`. Necessity is the Gram inequality:
for `a in R^3`, `b in R`,

\[
 a^TGa+2b a^Tm+b^2C^2
 =\left\|\sum_i a_iV_i+bc\right\|_2^2
       +b^2(C^2-\|c\|_2^2)\ge0.
\]

For sufficiency, a vector `a in ker G` and arbitrary scalar multiples
of `a` in this inequality force `a.m=0`. Thus `m in range G`. Finite
symmetric diagonalization defines `G^dagger`. With
`c_*=sum_i (G^dagger m)_i V_i`, one has

\[
 E[c_*V_i]=m_i,\qquad \|c_*\|_2^2=m^TG^\dagger m.
\]

The block quadratic form at `a=-G^dagger m`, `b=1` gives
`C^2-m^TG^dagger m>=0`. This proves the asserted equivalence, including
singular Grams. No weak limit of readouts or hidden future information is
needed.

## 2. Vanishing readout speed forces fitting on this set

At every point of (2),

\[
                    m_i\ge1-\sqrt{3\ell}>0.             \tag{3}
\]

Any relation `sum_i a_i V_i=0` gives `a in ker G`, and the preceding
block-matrix argument gives `a.m=0`. Consequently a zero field would
force its margin to vanish; an opposite pair would force the sum of
their margins to vanish; and equal fields force equal margins. The first
two alternatives contradict (3).

Suppose now `A(G,m)=0`. A Gram quadratic form is the squared norm of its
linear combination, so

\[
                     \sum_i(1-m_i)V_i=0.                \tag{4}
\]

Group equal fields. There are no zero or opposite fields, and the
remaining group fields are linearly independent by Sections 2–3 of the
supplied source, including saturated sign fields. Margins are equal
within each group. The coefficient in (4) of a group of size `k` is
`k(1-m_i)`, so every margin equals one. Therefore

\[
        A(G,m)=0\text{ on }\Omega_\ell\quad\Longrightarrow\quad L(m)=0.
                                                               \tag{5}
\]

This argument is algebraic and compact-geometric. It does not assume
the conditional convergence theorem that the construction is intended
to strengthen.

## 3. The minimum and its envelope, including empty sets

For `0<s<=ell`, define

\[
 D(s)=\min\{A(G,m):(V,m)\in\Omega_\ell,\ L(m)\ge s\},
 \qquad D(0)=0,                                      \tag{6}
\]

with `D(s)=+infinity` for an empty constraint set. Any nonempty constraint
set in (6) is compact, so its minimum is attained. By (5), that minimum
is strictly positive. The function `D` is nondecreasing on `(0,ell]`
because increasing `s` shrinks the feasible set; with the declared
`D(0)=0` it is nondecreasing on the whole interval. No continuity of
`D` is needed.

The proposed envelope is

\[
                 d(s)=\inf_{0\le u\le\ell}\{D(u)+|s-u|\}.
                                                               \tag{7}
\]

It has the following equivalent, simpler formula:

\[
 d(s)=\min\left\{s,\ \min_{(V,m)\in\Omega_\ell}
                     \bigl[A(G,m)+(s-L(m))_+\bigr]\right\}.
                                                               \tag{8}
\]

An empty inner minimum is `+infinity`. To verify (8), the choice `u=0`
in (7) supplies the first value `s`. For `u>0`, replace `D(u)` by its
minimum in (6) and minimize jointly over `u` and the feasible state.
For a state with loss `a>0`, the allowed interval is `0<u<=a`, and
`inf |s-u|=(s-a)_+`, attained at `u=min(s,a)` when `s>0`. A feasible
state with `a=0` has `A=0` and would contribute only `s`, already
included. This proves (8), including when the entire set is empty.

Formula (8) proves immediately that `d` is finite, nondecreasing, and
1-Lipschitz: each function being minimized has those properties, and
their common Lipschitz bound passes to the infimum. Also

\[
              d(0)=0,\qquad 0<d(s)\le s,\qquad d(s)\le D(s)
              \quad(0<s\le\ell).                      \tag{9}
\]

For strict positivity, if the second minimum in (8) were zero, its
compactness would give a minimizer with `A=0` and `L>=s`; this
contradicts (5). The first candidate `s` is positive. If the set is
empty, `d(s)=s` directly. Alternatively, (7) and monotonicity of `D`
give the explicit qualitative lower bound
`d(s)>=min{s/2,D(s/2)}>0`, with the extended-real convention.

By (1)–(2), (8) is a compact optimization over three closed disks and
three margin coordinates, using fixed population integrals and a
four-by-four positive semidefinite constraint. It is a finite-dimensional
variational definition. This check does not claim a practical numerical
algorithm or an evaluated value for its minimum.

## 4. Potential, inverse comparison, and the exact derivative

For `0<L<=ell` define

\[
 \Phi(L)=\exp\left[-\int_L^\ell\frac{ds}{d(s)}\right],
 \qquad\Phi(0)=0.                                    \tag{10}
\]

Continuity and positivity of `d` make the integral finite on every
`[L,ell]` with `L>0`. Since `d(s)<=s`,

\[
 \int_L^\ell\frac{ds}{d(s)}\ge\log(\ell/L),
 \qquad 0<\Phi(L)\le L/\ell.                         \tag{11}
\]

Thus `Phi` extends continuously to zero, has `Phi(ell)=1`, and is
strictly increasing. On `(0,ell]` it is continuously differentiable,
with

\[
                        \Phi_L(L)=\Phi(L)/d(L)>0.       \tag{12}
\]

There is therefore a continuous strictly increasing inverse
`h:[0,1]->[0,ell]`, with `h(0)=0`, and `L=h(Phi(L))`. This follows
without an inverse differentiability claim: a convergent sequence of
potential values has inverse values in a compact interval; continuity
and strict injectivity identify every subsequential limit. If a
comparison on all nonnegative arguments is requested, set
`h(z)=ell*z` for `z>=1`, matching the inverse at one.

Consider now any interval of an actual canonical trajectory on which
`L<=ell` and `||c||_2<=C`. Absorb labels into `V_i=y_iH_i` and
`m_i=y_if_i`. The resulting state lies in (2). The exact physical
readout velocity and full energy identity give

\[
 \|\dot c\|_2^2=A(G,m),\qquad
 \dot L\le-\|\dot c\|_2^2\le-D(L)\le-d(L).            \tag{13}
\]

When `L>0`, combine (12)–(13):

\[
                  \frac d{dt}\Phi(L(t))\le-\Phi(L(t)). \tag{14}
\]

If the loss is zero, every residual vanishes, all velocities vanish,
and the potential stays zero. If a finite first zero occurs, integrate
(14) before that time and pass to the continuous zero limit; afterwards
the zero solution supplies the same inequality. No differentiability
of `Phi` at the endpoint `L=0` is needed for this comparison. Therefore
on any such forward interval starting at `t_0`,

\[
 \Phi(L(t))\le\Phi(L(t_0))e^{-(t-t_0)},\qquad
 L(t)\le h\bigl(\Phi(L(t_0))e^{-(t-t_0)}\bigr).        \tag{15}
\]

For an all-time result the two trajectory hypotheses must hold for all
`t>=t_0`. The current-state potential is the composition of (10) with
the current loss; its predeclared constants are `C,ell` and the fixed
canonical mark law. Its construction never queries the future path.

## 5. Scope and source check

The positivity proof, regularizing envelope, inverse, and derivative
are complete. Empty constraint sets cause no defect: (8) stays defined,
and any actual trajectory point satisfying the hypotheses supplies a
nonempty feasible set at its own loss.

The important remaining qualifications are substantive:

* `C` is a declared fixed number in the conditional statement. Taking
  an unknown future supremum of the actual readout as an operational
  input would not meet the user's provenance requirement.
* Entry below `1/3` and a subsequent bound by that declared `C` have
  not been proved for every canonical initialized triple.
* The global envelope concerns a relaxed family of signed upper fields;
  this makes it uniform across data geometry under the two hypotheses.
  It does not establish those hypotheses from initialized geometry.
* No parameter endpoint or finite full-state length is implied by
  (15) alone when the inverse comparison can be very slow.

The construction is therefore a valid conditional exponential
current-state certificate, strengthening the earlier conditional
loss-convergence statement. It is not the requested unconditional
canonical-initialization theorem.

Additional source SHA-256:
`generic3_stationary_geometry.md`:
`170447ad239b991762fd4597a0a52318d04b9c4bad750ad95ca4c0e15dd777db`.
The compactness, finite/saturated independence, and grouping arguments
were checked from its complete text. The exact physical equations and
normalization were already read in the original assigned source scope.
The new construction itself was supplied in the supervisor's post-freeze
assignment; formula (8) is this check's additional simplification.
