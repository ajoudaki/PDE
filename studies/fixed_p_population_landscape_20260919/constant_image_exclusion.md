# Constant upper images cannot support a bad local minimum

2026-09-19. Lead continuation within the present study. This completes the
constant-image and rank-zero cases left open by `rank_one_exclusion.md`.
It does not settle effective upper rank two or greater at arbitrary sample
count. The exact model, topology, and small-population-subset necessary
condition are those proved in sections 1–3 of `finite_sample_theorem.md`.
No moment-interiority theorem or external purification theorem is used.

## 1. Statement

Use the model (1) and effective lower space \(B_1\) of
`finite_sample_theorem.md`, for any finite number \(m\) of distinct-modulo-sign
unit input directions \(u_i\), positive weights, and finite real labels.
The lower carrier is nonatomic and both mark columns are bounded. Assume
that the constant function belongs to both mark spans and that the upper
mark span contains a nonconstant function. These assumptions hold for the
full canonical dictionary at every \(p\ge1\).

Let \(U_2h=b_2^Th\) and \(K=U_2M|_{B_1}\). At an ambient local minimum, if

\[
                  \operatorname{range}K\subseteq\operatorname{span}\{1\},
\tag{1}
\]

then the loss is zero. This includes \(K=0\). There is no sample-count
restriction and no input linear-independence assumption.

Represent (1) as \(Kh=(v\cdot h)1\) for a fixed \(v\in B_1\), allowing
\(v=0\). Write \(a_0=E_1b_1\ne0\); its nonzero value follows because the
lower mark span contains the constant. Then

\[
 z_i=\alpha_i=v\cdot a_i,\qquad
 f_i=(E_2c)\phi(\alpha_i),\qquad \phi=\tanh.
\tag{2}
\]

## 2. An elementary ridge-independence extension

For any real \(\kappa\), define the scalar function

\[
                  h_\kappa(t)=\phi(t)\phi'(\kappa\phi(t)).
\tag{3}
\]

It is odd, bounded, and real analytic on the real line, with
\(h_\kappa'(0)=1\). Its Taylor expansion at zero has infinitely many
nonzero odd coefficients. Otherwise it would agree with a polynomial on
a neighborhood of zero and then on the whole real line by analytic
continuation. A bounded real polynomial is constant, contradicting its
derivative at zero.

The functions \(s\mapsto h_\kappa(s\cdot u_i)\) are linearly independent.
Choose a vector \(\eta\) such that \(\beta_i=\eta\cdot u_i\) are nonzero
and have distinct squares; the finite excluded hyperplanes are proper.
Choose any \(m\) nonzero Taylor coefficients, at odd orders
\(2n_1+1<\cdots<2n_m+1\). Restriction to \(s=t\eta\) of a putative linear
relation yields

\[
             \sum_i \gamma_i\beta_i(\beta_i^2)^{n_j}=0,
                  \qquad j=1,\ldots,m.
\]

The generalized Vandermonde matrix is invertible for distinct positive
nodes. Here is the needed proof. A nonzero polynomial with at most \(m\)
nonzero monomials has at most \(m-1\) distinct positive roots. Induct on
the number of its monomials: divide by its smallest monomial; the
derivative has at most \(m-1\) monomials, so Rolle's theorem bounds the
number of roots of the original function by one more than the derivative
bound. A singular evaluation matrix would supply a nonzero combination
of its \(m\) monomials vanishing at all \(m\) positive nodes, a
contradiction. Therefore every \(\gamma_i=0\).

## 3. The fully flat lower-field case

Suppose a positive-loss local minimum satisfying (1) also has zero
prediction for every choice of the lower field with the same \(M,c\).
By (2), this holds whenever \(v=0\) or \(E_2c=0\). The residual vector is
then the fixed nonzero vector \(r=-y\).

We claim that necessarily

\[
                            E_2[b_2c]=0.
\tag{4}
\]

Otherwise matrix stationarity, with
\(d_i=E_2[b_2c]\phi'(v\cdot a_i)\), would give

\[
                \sum_i\mu_i r_i\phi'(v\cdot a_i)a_i=0
\tag{5}
\]

at every sufficiently nearby lower field. Indeed all these fields have
the same loss, and every equal-value point inside a local-minimum ball
is a local minimum on a smaller ball. The nonzero vector \(E_2[b_2c]\)
can be cancelled from its outer product with the left side of (5).

Replace \(w\), if necessary, by a bounded truncation sufficiently close
in \(L^2\) to remain inside that ball. This preserves the predictions and
local minimality, so call the resulting bounded field \(\widetilde w\).
For any finite \(s\in\mathbb R^d\), consider

\[
                      w_t=(1-t)\widetilde w+ts.
\]

Equation (5) holds for all sufficiently small real \(t\). Its left side
is real analytic in \(t\) on the entire real line. To verify this without
an unbounded-field analyticity assumption, on each bounded real interval
both \(\widetilde w\) and \(s\) are bounded. The tanh arguments admit a
common complex neighborhood avoiding their poles, and the integrands
are bounded uniformly there. Integration against bounded \(b_1\)
preserves holomorphy (integrate the uniformly bounded power series, or
use Cauchy's formula and Fubini). The finite outer tanh derivatives
likewise have a sufficiently small pole-free neighborhood of each real
\(t\). This proves the assertion.

The real analytic identity therefore holds at \(t=1\), for every \(s\).
There \(a_i=a_0\phi(s\cdot u_i)\). With \(\kappa=v\cdot a_0\), (5) gives

\[
                a_0\sum_i\mu_i r_i h_\kappa(s\cdot u_i)=0
                    \quad\hbox{for every }s.
\tag{6}
\]

Since \(a_0\ne0\), section 2 forces every \(\mu_i r_i=0\), contradicting
the positive loss. This proves (4).

## 4. Excluding both constant-image cases

First let \(v=0\). All predictions are zero regardless of \(w,c\).
Arbitrarily small changes \(c\mapsto c+\varepsilon\) preserve that loss
and local minimality. By (4) applied before and after,

\[
                 E_2[b_2c]=E_2[b_2(c+\varepsilon)]=0.
\]

But \(E_2b_2\ne0\) since the upper span contains the constant. A nonzero
\(\varepsilon\) contradicts these two equations. Thus no positive-loss
local minimum has \(K=0\).

Now let \(v\ne0\). The small-set necessary condition established in the
main proof is

\[
                    r_i b_1^TM^Td_i=0 \quad\hbox{a.s.}
\]

Under (1) it becomes

\[
        r_i(v\cdot b_1)(E_2c)\phi'(\alpha_i)=0\quad\hbox{a.s.}
\]

For any nonzero residual, \(\phi'(\alpha_i)>0\), and
\(E_1(v\cdot b_1)^2>0\) by \(v\in B_1\setminus\{0\}\). Hence
\(E_2c=0\). We are in section 3, and (4) follows.

Choose a nonconstant upper mark combination \(B=e^Tb_2\) and set
\(k=B-E_2B\). It is bounded, has mean zero, and

\[
                 e^TE_2[b_2k]=\operatorname{Var}(B)>0.
\]

The change \(c\mapsto c+\varepsilon k\) keeps its mean zero and all
predictions zero. For small nonzero \(\varepsilon\) it preserves local
minimality, so (4) applies at the new point as well. Subtracting (4)
gives \(\varepsilon E_2[b_2k]=0\), a contradiction. This completes the
theorem.

## 5. Consequence and limits

At every fixed canonical \(p\ge1\), all upper marks are continuous
functions of a finite full-support Gaussian source vector. Thus any
nonconstant scalar image has infinite essential support: its support
is the closure of a nonconstant connected continuous image, a
nondegenerate interval. Together with `rank_one_exclusion.md`, the
present theorem proves:

**For any finite compatible dataset on the circle, a canonical ambient
local minimum with effective current operator rank at most one has zero
loss, at every fixed \(p\ge1\).**

There is no restriction to low raw matrix rank; null mark coordinates
are factored out in \(K\). These subsidiary results impose a state-rank
condition and do not replace the unconditional sample-bounded theorem.
For incompatible repeated/antipodal labels, group them as in the main
proof and replace zero by its explicit architectural loss floor.
Nothing here proves that the initialized dynamics converges to a local
minimum, maintains rank one, or fits at a specified rate.
