# Actual fitted-endpoint variability with two tanh hidden layers

2026-10-04. Coordinator derivation in the integrated study. This is an
endpoint lower bound for the actual canonical dense gradient flow, at a
fixed nonzero label size. Neither a frozen-feature replacement nor a
derivative with respect to label amplitude is used. The only imported
training input is the complete fitting theorem and its initialization proof
in `GENERAL_EXPLICIT_FITTING.md`. The covariance argument below is new.
Internal reconstruction status is recorded in `ENDPOINT_LOWER_CHECK.md`.

## Statement

Let the normalized training inputs \(v_a=x_a/\sqrt d\) have norm one and
span a proper subspace \(S\subset\mathbb R^d\). There may be arbitrarily
many inputs in that subspace; they need not be orthogonal. Define

\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}=\mathbb E[\tanh(Z_a)\tanh(Z_b)],
 \quad Z\sim N(0,Q^{(\ell-1)}),\quad \ell=1,2.
\]

Write \(Q=Q^{(2)}\), assume \(\gamma=\lambda_{\min}(Q)>0\), and set

\[
 Y=\|y\|_2/\sqrt m>0,\qquad \lambda=\gamma/m.
\]

The two independent networks both have the forward map

\[
 f_n(t,v)=\frac1n w(t)^\top\tanh\!\big(W(t)\tanh(A(t)v)\big).
 \tag{1}
\]

Here \(A_0\) has independent \(N(0,1)\) entries, \(W_0\) has independent
\(N(0,1/n)\) entries, and \(w_0=0\), with independent blocks and copies.
They train every block by mean-square loss with mobilities \((n,1,n)\):

\[
 \dot w=-\frac2m\sum_a r_a g_a,\quad
 \dot W=-\frac2{mn}\sum_a r_a
      [w\odot(1-g_a^2)]h_a^\top,
\]
\[
 \dot A=-\frac2m\sum_a r_a
      [(1-h_a^2)\odot W^\top(w\odot(1-g_a^2))]v_a^\top,
 \quad r_a=f_n(t,v_a)-y_a,
 \tag{2}
\]

where \(h_a=\tanh(Av_a)\), \(g_a=\tanh(Wh_a)\). All clocks here are
physical time. Assume

\[
 0<Y\le 10^{-6}\gamma/m. \tag{3}
\]

This is implied by the integrated theorem's existing cap
\(Y\le(\gamma/m)\beta^{-60}\), since \(\beta\ge10\); it does not require
a smaller label cap when applying that theorem to this example.

There are numerical constants \(c,p>0\), independent of \(n,m,d,Q,y\),
such that, for every fixed admissible dataset and every fixed unit
\(v\in S^\perp\), for all sufficiently large \(n\),

\[
 \Pr\!\left\{
 \begin{array}{c}
 \text{both flows converge and interpolate, and}\\[1mm]
 |f_n(\infty,v)-\widetilde f_n(\infty,v)|
       \ge c\sqrt{\dfrac{y^\top Q^{-1}y}{n}}
 \end{array}\right\}\ge p.
 \tag{4}
\]

The same event lower-bounds the sphere supremum at the endpoint and the
supremum over all physical time and all sphere queries. The width threshold
can depend on the data; the constants in (4) do not. A quantitative
description of the threshold is given in the proof. The small probability
constant produced below is conservative and is not claimed sharp.

For labels \(y=\sqrt mY u\), where \(u\) is a unit eigenvector of \(Q\)
with eigenvalue \(\gamma\), (4) is

\[
 |f_n(\infty,v)-\widetilde f_n(\infty,v)|
       \ge cY\sqrt{\frac{m}{\gamma n}}.
 \tag{5}
\]

In particular, for \(m\) orthonormal training inputs with \(d\ge m+1\),
oddness gives \(Q=\gamma I_m\). Thus (5) holds for **every** nonzero label
vector satisfying (3), including equal signs, opposite signs and mixed
signs. This is a lower-bound example within the general scope; the upper
theorems do not acquire an orthogonality assumption.

## 1. Randomness unseen by the training dynamics

Decompose \(A=A|_S+A|_{S^\perp}\) using orthogonal projections. Equation
(2) gives \(\dot A|_{S^\perp}=0\). Every quantity evaluated in training is
measurable with respect to \(A_0|_S,W_0\), and is independent of the
Gaussian block \(A_0|_{S^\perp}\). In an orthonormal coordinate system this
is independence between disjoint columns of a standard Gaussian matrix.

Apply `GENERAL_EXPLICIT_FITTING.md` in input dimension \(\dim S\), using
the same \(m\) training coordinates and the same mixers. This reduced
training system is exactly (2) on its active inputs. Its fitting event
depends only on \(A_0|_S,W_0\), and its proof supplies

\[
 \|W_\infty\|_{\rm op}<9,\qquad
 \|W_\infty-W_0\|_F\le16Y^2/\lambda^{3/2},
 \tag{6}
\]

as well as parameter convergence and interpolation. Here \(H=s=1\),
\(F=85\), \(U_2=2\) in that source. Its sufficient fitting cap
\(Y\le\lambda/(8\sqrt{85})\) follows from (3). The event has probability
at least \(1-\varepsilon\) at the source's explicit threshold
\(N_{\rm fit}(\varepsilon)\) with \(d\) replaced by \(\dim S\).

It is essential to restrict this event to the training subspace. Imposing
a cap on the original \(d\)-dimensional \(A_0\) would condition on the
query randomness used next and invalidate its unchanged Gaussian law.

Fix a unit \(v\in S^\perp\). Conditional on the active training blocks,
\(Z=A_0v\sim N(0,I_n)\), independently of the active trained state
\(A_\infty|_S,W_\infty,w_\infty\), and

\[
 f_n(\infty,v)=\frac1n w_\infty^\top\tanh(W_\infty H),
 \qquad H_j=\tanh Z_j. \tag{7}
\]

The independent variables \(H_j\) are centered, symmetric, bounded by one,
and have variance \(\sigma^2=\mathbb E\tanh^2 Z\in[1/16,1]\).
For the lower bound, use
\(\Pr(|Z|\ge1/2)>1/2\) and \(\tanh(1/2)>2/5\).

## 2. A covariance gap for initialized nonlinear query features

We prove that, with probability tending to one over \(W_0\),

\[
 \mathbb E_H[\tanh(W_0H)\tanh(W_0H)^\top]
       \succeq10^{-14}I_n. \tag{8}
\]

The means vanish by symmetry. This is a finite-matrix assertion about the
actual Gaussian mixer. No limiting population or trained Gaussianity is
assumed.

For each unordered triple \(J\subset\{1,\ldots,n\}\), define

\[
 \psi_J(H)=\prod_{j\in J}\frac{H_j}{\sigma}
          =\sigma^{-3}\prod_{j\in J}H_j.
\]

These functions are orthonormal: if two triples differ, their product
contains a centered coordinate to the first power, and independence makes
the expectation zero. Their squared norms equal one.

For a mixer row \(b\in\mathbb R^n\), let

\[
 C_{b,J}=\mathbb E[\tanh(b^\top H)\psi_J(H)],\qquad
 a(b)=\sigma^3\mathbb E\tanh'''(\sigma\|b\|_2 Z).
\]

There is a fixed finite constant \(C\), depending only on the real
derivatives of tanh through order seven, for which

\[
 \left|C_{b,J}-a(b)\prod_{j\in J}b_j\right|
 \le C\left(\sum_{p=1}^n b_p^4+\sum_{j\in J}b_j^2\right)
             \prod_{j\in J}|b_j|.
 \tag{9}
\]

To verify every factor in (9), for a centered symmetric variable \(H\)
write exactly

\[
 \mathbb E[H F(u+bH)]
   =b\,\mathbb E\left[H^2\int_0^1F'(u+tbH)\,dt\right].
\]

Iterate in the three coordinates of \(J\). After dividing by \(\sigma^3\),
this gives \(\sigma^3\prod_{j\in J}b_j\) times an expectation of
\(\tanh'''\) of the remaining sum plus a shift. Each shifted coordinate
has the symmetric probability law tilted by \(H_j^2/\sigma^2\), with
an independent uniform integration variable \(t_j\). The shift has mean
zero and variance at most \(\sum_{j\in J}b_j^2\). Taylor's formula with
bounded fifth derivative changes the expectation by at most a constant
times that sum.

Next replace the remaining \(H_p\)'s one by one by independent
\(\sigma Z_p\). Their first three moments agree (zero, variance
\(\sigma^2\), zero). Taylor expansion of \(\tanh'''\) through order
three, with bounded seventh derivative, bounds the total replacement
error by \(C\sum_{p\notin J}b_p^4\): the fourth moments of both inputs
are bounded by three. Finally restore the omitted Gaussian coordinates.
Taylor expansion in their centered sum costs
\(C\sum_{j\in J}b_j^2\). This proves (9), including cases with a zero
coefficient (both sides then vanish). The derivative bounds are finite:
successive derivatives of tanh are polynomials in tanh, by
\(P_{k+1}(u)=(1-u^2)P_k'(u)\), starting with \(P_0(u)=u\).

For \(9/10\le\|b\|_2\le11/10\), we have

\[
 a(b)\le-10^{-6}. \tag{10}
\]

Here is an elementary lower estimate, not an assumption of a nonzero
Hermite coefficient. If \(s=\sigma\|b\|\in[1/5,6/5]\), two Gaussian
integrations by parts yield

\[
 s^2\mathbb E\tanh'''(sZ)
   =\operatorname{Cov}(Z^2,\operatorname{sech}^2(sZ)).
 \tag{11}
\]

The covariance is negative. For independent \(Z,Z'\), express it as
half the expectation of
\((Z^2-Z'^2)(\operatorname{sech}^2(sZ)-\operatorname{sech}^2(sZ'))\).
The integrand is always nonpositive. The events
\(|Z|\le1/2\) and \(|Z'|\ge3/2\) have probabilities at least \(1/3\)
and \(1/20\), respectively. On them the first-factor gap is at least
two, and

\[
 \operatorname{sech}^2(s/2)-\operatorname{sech}^2(3s/2)
 \ge\int_{s/2}^{s}2\operatorname{sech}^2 u\tanh u\,du>1/300.
\]

The last inequality follows on this interval from
\(u\in[1/10,6/5]\), \(\operatorname{sech}^2 u>1/4\),
\(\tanh u>9/100\), and interval length at least \(1/10\).
Including both orientations of these events cancels the factor one-half.
Thus the covariance magnitude is at least \(1/9000\), and
\(|\mathbb E\tanh'''(sZ)|>1/13000\). Since \(\sigma^3\ge1/64\),
(10) follows.

Let \(b_i\) be the rows of \(W_0\), and set
\(U_{i,J}=\prod_{j\in J}b_{ij}\). With probability tending to one,
simultaneously

\[
 9/10\le\|b_i\|\le11/10,\quad
 \max_{ij}|b_{ij}|\le C\sqrt{\log(en)/n},\quad
 \max_{i\ne k}|b_i^\top b_k|\le C\sqrt{\log(en)/n}.
 \tag{12}
\]

For completeness, scalar Gaussian tails and a union over \(n^2\) entries
give the second assertion. Conditional on \(b_i\),
\(b_i^\top b_k\) is centered Gaussian with variance \(\|b_i\|^2/n\);
a stopped union bound on \(\|b_i\|\le11/10\) gives the third. For row
norms, use \(\mathbb E e^{t n\|b_i\|^2}=(1-2t)^{-n/2}\) for
\(t<1/2\), with fixed small positive and negative \(t\), to obtain an
\(O(ne^{-cn})\) failure bound. Replacing \(\log(en)\) by
\(\log(8n^2/\varepsilon)\) makes the total failure at most
\(\varepsilon\) once \(n\ge C\log(8n^2/\varepsilon)\).

For \(p_j=b_{ij}b_{kj}\), the exact identity

\[
 (UU^\top)_{ik}
 =\frac16\left[(\sum_jp_j)^3
        -3(\sum_jp_j)(\sum_jp_j^2)+2\sum_jp_j^3\right]
 \tag{13}
\]

shows that diagonal entries are at least \(1/20\) for large \(n\).
Indeed they equal \(\|b_i\|^6/6+O(\log(en)/n)\), uniformly in \(i\).
Off-diagonal entries have magnitude at most

\[
 C\left[\frac{\log(en)^{3/2}}{n^{3/2}}
                  +\frac{\log(en)^2}{n^2}\right].
\]

For this bound, use \(\sum p_j^2\le\max_j b_{ij}^2\|b_k\|^2\)
and \(\sum|p_j|^3\le\max_j|p_j|\sum p_j^2\), together with (12).
The sum of off-diagonal absolute entries in each row tends to zero.
The quadratic-form estimate obtained from
\(2|u_i u_k|\le u_i^2+u_k^2\) therefore gives

\[
 UU^\top\succeq I_n/40 \tag{14}
\]

for sufficiently large \(n\) on (12).

By (9), the matrix with entries \(C_{b_i,J}\) differs from
\(\operatorname{diag}(a(b_i))U\) in Frobenius norm by at most
\(C\log(en)/\sqrt n\). In fact
\(\sum b_{ij}^4\le C\log(en)/n\), and
\(\sum_J\prod_{j\in J}b_{ij}^2\le\|b_i\|^6/6\).
Its smallest singular value is therefore at least
\(10^{-6}/\sqrt{40}-C\log(en)/\sqrt n\), which exceeds
\(10^{-7}\) eventually. Orthogonal projection onto the \(\psi_J\)'s
can only decrease the \(L^2\) norm of any linear combination of query
features. This proves (8).

This argument supplies a numerical width condition if desired: in addition
to (12)'s row-norm threshold, require the explicit upper bounds in (13)'s
off-diagonal row sum to be at most \(1/40\) and the coefficient-error
bound to be at most \(10^{-6}/\sqrt{40}-10^{-7}\). All constants can be
computed from the seven tanh derivative polynomials above. None depends
on the training dataset.

## 3. The gap survives actual nonlinear training

For any deterministic mixer perturbation \(E\), Lipschitz continuity of
tanh and independence of the centered coordinates of \(H\) give

\[
 \mathbb E_H\|\tanh((W_0+E)H)-\tanh(W_0H)\|_2^2
       \le\sigma^2\|E\|_F^2. \tag{15}
\]

Thus the operator from a coefficient vector \(u\in\mathbb R^n\) to its
linear combination of query features in \(L^2(H)\) changes by at most
\(\sigma\|E\|_F\). Equation (6), (3), and \(\lambda\le1\) imply

\[
 \|W_\infty-W_0\|_F\le16\cdot10^{-12}\sqrt\lambda
          \le16\cdot10^{-12}<\tfrac12\,10^{-7}.
\]

Consequently (8) gives the convenient conservative bound

\[
 \mathbb E_H[\tanh(W_\infty H)\tanh(W_\infty H)^\top]
            \succeq10^{-16}I_n. \tag{16}
\]

This is uniform over all trained states in the fitting event. In particular,
the dependence of \(W_\infty\) on \(W_0\), labels and training features
does not require a Gaussian law for the trained rows.

## 4. Fitting forces the readout energy to reflect label conditioning

Let \(\mathsf H_t\) be the matrix of top training features. The explicit
initialization proof in the fitting source gives

\[
 \|\mathsf H_0^\top\mathsf H_0/n-Q\|_{\rm op}\le\gamma/2,
 \qquad
 \|\mathsf H_\infty-\mathsf H_0\|_{\rm op}/\sqrt n
       \le\sqrt\gamma/8. \tag{17}
\]

The second inequality follows from its feature displacement bound in the
active input space, after multiplying its normalized training-matrix
bound by \(\sqrt m\). Hence, for every vector \(u\in\mathbb R^m\),

\[
 \|\mathsf H_\infty u\|/\sqrt n
 \le\sqrt{\tfrac32 u^\top Qu}+\tfrac18\sqrt\gamma\|u\|
 <\sqrt{2u^\top Qu}.
\]

Since \(\mathsf H_\infty^\top w_\infty/n=y\), substituting
\(u=Q^{-1}y\) into Cauchy--Schwarz gives

\[
 \frac{\|w_\infty\|_2^2}{n}\ge\frac12 y^\top Q^{-1}y.
 \tag{18}
\]

This estimate retains actual label size and direction. Replacing it by
\(Y^2\) would unnecessarily lose the sample-size and conditioning effect.

## 5. Conditional moments and a fixed-probability endpoint lower bound

For fixed trained \(W,w\), the scalar function

\[
 F(Z)=w^\top\tanh(W\tanh Z)/n
\]

is odd and has Gaussian mean zero. Its global Euclidean Lipschitz
constant is at most \(9\|w\|/n\), since both tanh derivatives have
absolute value at most one and \(\|W\|_{\rm op}<9\). The Gaussian
Poincare inequality \(\operatorname{Var}F\le\mathbb E\|\nabla F\|^2\)
gives \(\mathbb E F^2\le K^2\) for Lipschitz constant \(K\). Applying
it to \(F^2\) gives

\[
 \mathbb E F^4-(\mathbb E F^2)^2
       \le4K^2\mathbb E F^2,\qquad \mathbb E F^4\le5K^4.
 \tag{19}
\]

One direct justification of the inequality used here is the orthonormal
Gaussian Hermite expansion: if \(F=\sum_\alpha c_\alpha H_\alpha\),
then \(\operatorname{Var}F=\sum_{|\alpha|\ge1}c_\alpha^2\), whereas
\(\mathbb E\|\nabla F\|^2=\sum_\alpha |\alpha|c_\alpha^2\).
Approximation by smooth functions and Gaussian truncation extends it to
the Lipschitz functions and their squares here. These are integrable
because Lipschitz growth is at most linear. Thus (19) needs no assumption
on individual trained readout coordinates.

Condition on the two independent active training states, on their fitting
events and the two mixer events (8). Write
\(D=f_n(\infty,v)-\widetilde f_n(\infty,v)\) and, locally in this proof,
\(R=(\|w_\infty\|^2+\|\widetilde w_\infty\|^2)/n^2\).
The remaining Gaussian query vectors are independent. Equations (16),
(19) give

\[
 \mathbb E[D^2\mid\mathrm{training}]\ge10^{-16}R,
 \qquad
 \mathbb E[D^4\mid\mathrm{training}]\le5\cdot9^4R^2.
 \tag{20}
\]

For the fourth bound, expand the fourth power of the difference of two
independent centered variables; the cross term is six times the product
of their second moments. Its coefficient is bounded by the ten appearing
in \(5(a+b)^2\). For a nonnegative random variable \(X\),
Cauchy--Schwarz on \(X1_{X\ge\mathbb EX/2}\) yields
\(\Pr(X\ge\mathbb EX/2)\ge(\mathbb EX)^2/(4\mathbb EX^2)\).
Use \(X=D^2\) and (20). Conditional probability is at least

\[
 p_0=\frac{10^{-32}}{20\cdot9^4}
\]

that \(|D|\ge\sqrt{10^{-16}R/2}\). By (18) for both copies,
\(R\ge y^\top Q^{-1}y/n\). Thus (4) holds with
\(c=10^{-8}/\sqrt2\) and, for instance, \(p=p_0/2\), once each
fitting/mixer event has failure probability at most \(1/8\).

These tiny displayed constants were chosen only to make the proof wholly
auditable. The assertion of interest is the exact power \(n^{-1/2}\)
and the label energy \(y^\top Q^{-1}y\). This is a fixed-probability
lower bound, not a claim that every pair of runs differs by this amount.

## Scope and limits

- Both hidden layers use tanh; every parameter follows actual canonical
  dense training. The proof controls the final fitted states themselves.
- Training data may be correlated. The geometric requirement for this
  argument is a nonzero orthogonal input direction. Full input span is
  not covered by this endpoint proof.
- The bound holds at one fixed unseen input. It therefore lower-bounds
  the full sphere norm, but does not establish its sharp additional
  dependence on the number of unused input directions.
- Labels in weak covariance directions attain the \(\gamma^{-1/2}\)
  factor. Arbitrary labels should retain \(y^\top Q^{-1}y\); replacing
  this by \(mY^2/\gamma\) in a lower bound for every label orientation
  would reverse the relevant inequality.
- A universal positive endpoint lower bound for every admitted activation
  and dataset is false. `LINEAR_ENDPOINT_VARIABILITY_LOWER.md` gives a
  further instructive case: a spanning linear training set fixes the
  entire endpoint function, so independent fitted runs can agree exactly.
- No experiment, trained central limit theorem, cutoff, or comparison to
  a population dynamics has been used.
