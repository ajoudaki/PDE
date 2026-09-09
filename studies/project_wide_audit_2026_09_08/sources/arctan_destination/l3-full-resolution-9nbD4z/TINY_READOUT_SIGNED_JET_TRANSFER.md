# Candidate: tiny-readout transfer of the fifth signed primitive jet

Status: candidate route lemma, pending independent audit. This note proves the
specified finite-initial-jet transfer using the stated primary theorem.
It does not compute the zero-readout coefficient or claim a time-uniform
response estimate. No numerical experiment is used.

## 1. Statement and complete finite-width setup

There are three separate neuron populations \(I_1,I_2,I_3\), each of size
\(n\). Put \(\phi(z)=\arctan z\), \(\phi'(z)=(1+z^2)^{-1}\),
\(F(z)=z+z^3/3\), and \(\chi=\phi\circ F^{-1}\).
Vector magnitudes are measured by \(\|u\|_2/\sqrt n\). Width-averaged
dot products and learned rank-one updates display their factor \(1/n\)
explicitly; only vectors on the same population are paired in dot products.
All transposes, Euclidean norms, and matrix traces are ordinary ones.

The initial variables are mutually independent:
\[
 z^{(1)}_0\in\mathbb R^{I_1},\quad G_4\in\mathbb R^{I_3}
       \quad\text{with independent standard Gaussian coordinates},
\]
\[
 W^{(2)}_0:\mathbb R^{I_1}\to\mathbb R^{I_2},\qquad
 W^{(3)}_0:\mathbb R^{I_2}\to\mathbb R^{I_3},
 \qquad (W^{(\ell)}_0)_{ab}\sim N(0,1/n)\text{ independently}.
\]
For a real number \(\rho\), initialize
\(x^{(1)}(0)=F(z^{(1)}_0)\), \(W^{(2)}(0)=W^{(2)}_0\),
\(W^{(3)}(0)=W^{(3)}_0\), and \(W^{(4)}(0)=\rho G_4\).
All values of \(\rho\), including \(0\) and \(n^{-1}\), use these
same hidden variables and the same \(G_4\).

The canonical, uncut feature-time equations are
\[
 \begin{aligned}
 h^{(1)}&=\chi(x^{(1)}),& z^{(1)}&=F^{-1}(x^{(1)}),&D^{(1)}&=\operatorname{diag}\phi'(z^{(1)}),\\
 z^{(2)}&=W^{(2)}h^{(1)},&h^{(2)}&=\phi(z^{(2)}),&D^{(2)}&=\operatorname{diag}\phi'(z^{(2)}),\\
 z^{(3)}&=W^{(3)}h^{(2)},&h^{(3)}&=\phi(z^{(3)}),&D^{(3)}&=\operatorname{diag}\phi'(z^{(3)}),\\
 \delta^{(3)}&=D^{(3)}W^{(4)},&q^{(2)}&=(W^{(3)})^\top\delta^{(3)},&\delta^{(2)}&=D^{(2)}q^{(2)},\\
 x^{(1)}'&=(W^{(2)})^\top\delta^{(2)},&W^{(2)}'&=\frac{\delta^{(2)} (h^{(1)})^\top}{n},\\
 W^{(3)}'&=\frac{\delta^{(3)} (h^{(2)})^\top}{n},&W^{(4)}'&=h^{(3)}.
 \end{aligned}                                                    \tag{1}
\]
Here \(x^{(1)},h^{(1)}\) belong to \(I_1\), \(z^{(2)},h^{(2)},q^{(2)},\delta^{(2)}\) to
\(I_2\), and \(z^{(3)},h^{(3)},W^{(4)},\delta^{(3)}\) to \(I_3\).
Coordinate products below always stay within their indicated population.

For \(i\in I_2\), let \(K_i=\xi e_i^\top/\sqrt n\), with
\(\xi\in\mathbb R^{I_3}\) standard Gaussian independent of the initialization.
The variation changes only the initial \(W^{(3)}\), in direction \(K_i\).
Its transformed learned-state variation
\[
 y_i=(\widehat x^{(1)}_i,A_i,B_i,v_{4,i})
 =\bigl(\operatorname{var}x^{(1)},\operatorname{var}W^{(2)},
    \operatorname{var}(W^{(3)}-W^{(3)}_0),\operatorname{var}W^{(4)}\bigr)
\]
starts at zero. The total \(W^{(3)}\) variation is \(K_i+B_i\).
The subscript \(i\) labels a probe, not a coordinate of its vector response.
Write
\[
 \zeta_i=\operatorname{var}z^{(2)},\qquad
 a_i(s)=\int_0^s\operatorname{var}\delta^{(2)}(u)\,du,\qquad
 c_i=(D^{(2)})^{-1}a_i=(1+(z^{(2)})^2)\odot a_i,
 \qquad \beta(z)=\frac{\phi''(z)}{\phi'(z)}=-\frac{2z}{1+z^2}.
\]
Expectations over a probe always condition on
\(\mathcal F_n=\sigma(z^{(1)}_0,W^{(2)}_0,W^{(3)}_0,G_4)\).
Define exactly the requested full signed work
\[
 \mathcal W_n^\rho(s)=\frac1n\sum_{i\in I_2}\mathbb E_\xi
 \left[c_i^\top\operatorname{diag}(\beta(z^{(2)}))
       \bigl(q^{(2)}\odot\zeta_i-z^{(2)}'\odot c_i\bigr)
       \,\middle|\,\mathcal F_n\right].                         \tag{2}
\]
We use \([s^k]v=v^{(k)}(0)/k!\), always at finite width first.

**Candidate lemma.** Under the initialization and dynamics (1),
\[
 P_n(\rho):=[s^5]\mathcal W_n^\rho(s)
       =\sum_{m=0}^6 A_{n,m}\rho^m,\qquad A_{n,m}=O_{\mathbb P}(1).
                                                                    \tag{3}
\]
The coefficients are \(\mathcal F_n\)-measurable. Consequently,
\[
 [s^5]\mathcal W_n^{\mathrm{tiny}}
       -[s^5]\mathcal W_n^{\mathrm{zero}}
 =P_n(n^{-1})-P_n(0)=O_{\mathbb P}(n^{-1})
 \xrightarrow{\mathbb P}0.                                      \tag{4}
\]
The initial readout in (4) is precisely \(n^{-1}G_4\).

The proof has four parts: combine the column probes without changing their
normalization; bound the degree in \(\rho\); compile each fixed-amplitude jet
into an admissible finite Gaussian program; and convert its realized probe
norm bounds into conditional trace bounds before interpolating in \(\rho\).

## 2. Exact replacement by one full Gaussian matrix probe

Let \(J:\mathbb R^{I_2}\to\mathbb R^{I_3}\) have independent
\(N(0,1/n)\) entries, independent of
\(\mathcal F_n\). For any direction \(K\), use brackets such as \(c[K]\)
and \(\zeta[K]\) for the corresponding first variation and primitive.
At fixed initialization every one of these is linear in \(K\).

To verify that all trained factors are present, their exact equations are
\[
 \begin{aligned}
 \widehat h^{(1)}&=(D^{(1)})^2\widehat x^{(1)},&\zeta&=Ah^{(1)}+W^{(2)}\widehat h^{(1)},&\widehat h^{(2)}&=D^{(2)}\zeta,\\
 \zeta^{(3)}&=(K+B)h^{(2)}+W^{(3)}\widehat h^{(2)},\\
 \widehat\delta^{(3)}&=D^{(3)}v_4+W^{(4)}\odot\phi''(z^{(3)})\odot\zeta^{(3)},\\
 \widehat q^{(2)}&=(K+B)^\top\delta^{(3)}+(W^{(3)})^\top\widehat\delta^{(3)},\\
 \widehat\delta^{(2)}&=D^{(2)}\widehat q^{(2)}+
                         \phi''(z^{(2)})\odot q^{(2)}\odot\zeta,\\
 (\widehat x^{(1)})'&=A^\top\delta^{(2)}+(W^{(2)})^\top\widehat\delta^{(2)},\\
 A'&=\frac{\widehat\delta^{(2)} (h^{(1)})^\top}{n}+\frac{\delta^{(2)} (\widehat h^{(1)})^\top}{n},\\
 B'&=\frac{\widehat\delta^{(3)} (h^{(2)})^\top}{n}+\frac{\delta^{(3)} (\widehat h^{(2)})^\top}{n},\\
 v_4'&=D^{(3)}\zeta^{(3)},&a'&=\widehat\delta^{(2)},&c&=(1+(z^{(2)})^2)\odot a,
 \end{aligned}                                                     \tag{5}
\]
with \(\widehat x^{(1)}(0)=A(0)=B(0)=v_4(0)=a(0)=0\). Hats denote variation,
not a new independent backward query. These equations follow by
differentiating (1); \(\chi'(x^{(1)})=\phi'(z^{(1)})^2\).

Realize \(J=\sum_iK_i\) with independent column vectors \(\xi_i\).
For any two linear response maps \(U,V\), and any
\(\mathcal F_n\)-measurable matrix \(M\), the cross-column terms have zero
conditional expectation, so
\[
 \mathbb E_J[U[J]^\top M V[J]\mid\mathcal F_n]
 =\sum_i\mathbb E_{\xi_i}[U[K_i]^\top M V[K_i]\mid\mathcal F_n].
                                                                    \tag{6}
\]
This does not require different responses to be independent conditional on
the realized probe. It uses independent centered columns only inside a
bilinear expression whose response maps are fixed given \(\mathcal F_n\).

It follows that (2) is exactly
\[
 \mathcal W_n^\rho(s)
 =\mathbb E_J\left[
   \frac{c[J]^\top}{n}\left[
     \beta(z^{(2)})\odot\bigl(q^{(2)}\odot\zeta[J]-z^{(2)}'\odot c[J]\bigr)
   \right]\,\middle|\,\mathcal F_n\right].              \tag{7}
\]
Equivalently, putting \(\widetilde c_i=\sqrt n\,c_i\),
\[
 \mathbb E_J[c[J]c[J]^\top\mid\mathcal F_n]
 =\frac1n\sum_i
       \mathbb E_{\xi_i}[\widetilde c_i\widetilde c_i^\top
                         \mid\mathcal F_n],                      \tag{8}
\]
and the same identity holds for cross covariances. Thus the full probe
represents the averaged covariance of the rescaled column responses.
There is no extra factor \(n\) in (7).

For each finite \(n\), the vector fields in (1) and (5) are smooth near
their initial states; \(F'>0\) and \(\phi'>0\) everywhere. All required local
solutions and derivatives therefore exist. Conditional probe expectations
in (6)--(7) are finite-dimensional Gaussian quadratic forms with smooth
coefficient matrices. Taking five derivatives is a finite trace
differentiation. It requires no limit exchange in width or uniform
neighborhood of time zero.

## 3. The readout-amplitude degree is at most six

Write \(v_k=[s^k]v\). This subsection concerns polynomial degree in
\(\rho\), not polynomial degree in the Gaussian inputs.

Let \(\Theta=(x^{(1)},W^{(2)},W^{(3)})\). At fixed width, (1) has the form
\[
 \Theta'=\mathscr B(\Theta)W^{(4)},\qquad
 W^{(4)}'=\mathscr V(\Theta),                              \tag{9}
\]
where \(\mathscr B\) is a smooth linear map in its displayed readout
argument, and \(\mathscr V\) is smooth. The initial \(\Theta_0\) is
independent of \(\rho\).

For any smooth function \(f\) of \(\Theta\), its \(k\)-th time
coefficient is a finite sum of multilinear derivatives of \(f\) at
\(\Theta_0\), evaluated on \(\Theta_{r_1},\ldots,\Theta_{r_t}\)
with positive indices summing to \(k\). Hence, if
\(\deg_\rho\Theta_r\le r\), that coefficient has degree at most \(k\).
Induction in (9) now gives
\[
 \deg_\rho\Theta_k\le k,\qquad
 \deg_\rho(W^{(4)})_0\le1,\qquad
 \deg_\rho(W^{(4)})_k\le k-1\quad(k\ge1).                \tag{10}
\]
Indeed, at order \(k\) the term with \((W^{(4)})_0\) in
\(\mathscr B(\Theta)W^{(4)}\) has degree at most \(k+1\), and every term
with \((W^{(4)})_j\), \(j\ge1\), has degree at most \(k-1\).
Division by \(k+1\) gives \(\Theta_{k+1}\); the second equation in
(9) gives \((W^{(4)})_{k+1}\) degree at most \(k\). This also starts the
induction at \(k=0\).

Differentiate these polynomial identities with respect to
\(W^{(3)}_0\) in direction \(J\), holding \(\rho\) and \(G_4\) fixed.
Their degree bounds persist. Since \(q^{(2)}\) and \(\delta^{(2)}\) are smooth
functions of \(\Theta\), linear in \(W^{(4)}\),
\[
 \begin{array}{c|c}
 \text{time coefficient}&\text{upper bound on its degree in }\rho\\ \hline
 (z^{(2)})_k,\ \zeta[J]_k,\ [s^k]\beta(z^{(2)})&k\\
 (q^{(2)})_k,\ (\delta^{(2)})_k,\ \widehat\delta^{(2)}_k,\ (z^{(2)}')_k&k+1\\
 a[J]_k,\ c[J]_k&k
 \end{array}                                                       \tag{11}
\]
The last line uses \(a_0=c_0=0\),
\(a_k=\widehat\delta^{(2)}_{k-1}/k\) for \(k\ge1\), and
\((D^{(2)})^{-1}=\operatorname{diag}(1+(z^{(2)})^2)\).

For fixed \(\rho\), abbreviate
\[
 c_r=[s^r]c[J],\quad \zeta_v=[s^v]\zeta[J],\quad
 b_t=[s^t]\beta(z^{(2)}),\quad q^{(2)}_u=[s^u]q^{(2)},\quad
 \nu_u=[s^u]z^{(2)}'.
\]
Taking the coefficient of (7) gives the exact finite sum
\[
 P_n(\rho)=\sum_{r+t+u+v=5}\mathbb E_J\left[
   \frac{c_r^\top(b_t\odot q^{(2)}_u\odot\zeta_v)}{n}
  -\frac{c_r^\top(b_t\odot\nu_u\odot c_v)}{n}
       \,\middle|\,\mathcal F_n\right].                         \tag{12}
\]
Every summand has degree at most \(r+t+(u+1)+v=6\).
Its probe expectation preserves polynomiality, since the probe dependence
is quadratic. This proves the polynomial assertion in (3), with no claim
yet about its coefficient sizes.

## 4. A finite program for every fixed-amplitude jet

Fix a deterministic \(\rho\) independent of \(n\). Primal time jets
through order six and the response jets needed in (12) can be computed by
a number of instructions independent of \(n\). In particular, one never
uses a separate matrix variable for each of its \(n^2\) coordinates.

Here is an explicit compilation. For a scalar coordinate map \(f\),
\[
 [s^k]f(v(s))=
 \sum_{t=0}^k\frac{f^{(t)}(v_0)}{t!}
 \sum_{\substack{r_1+\cdots+r_t=k\\r_j\ge1}}
              v_{r_1}\odot\cdots\odot v_{r_t}.                  \tag{13}
\]
The empty term is \(f(v_0)\) at \(k=0\), and zero otherwise.
Products use finite convolutions of their time coefficients. From (1),
\[
 \begin{aligned}
 x^{(1)}_{k+1}&=\frac1{k+1}[s^k]((W^{(2)})^\top\delta^{(2)}),\\
 (W^{(4)})_{k+1}&=\frac1{k+1}(h^{(3)})_k,\\
 (W^{(\ell)})_k&=\frac1k\sum_{a+b=k-1}
                 \frac{(\delta^{(\ell)})_a (h^{(\ell-1)})_b^\top}{n},
                 &&\ell=2,3,\quad k\ge1.
 \end{aligned}                                                    \tag{14}
\]
Consequently, for every subsequent vector argument \(v\),
\[
 \begin{aligned}
 (W^{(\ell)})_kv&=\frac1k\sum_{a+b=k-1}
       (\delta^{(\ell)})_a\frac{(h^{(\ell-1)})_b^\top v}{n},\\
 (W^{(\ell)})_k^\top v&=\frac1k\sum_{a+b=k-1}
       (h^{(\ell-1)})_b\frac{(\delta^{(\ell)})_a^\top v}{n}.
 \end{aligned}                                                    \tag{15}
\]
Thus positive-order matrix jets reduce to a fixed finite number of vector
operations and ordinary scalar dot products divided by \(n\). Only
order-zero matrix actions use \(W^{(2)}_0,W^{(3)}_0\) or their actual
transposes.

Differentiating each instruction in (13)--(15) once gives the program for
(5). In particular, for \(k\ge1\),
\[
 \operatorname{var}(W^{(\ell)})_k
 =\frac1k\sum_{a+b=k-1}
    \left(\frac{\widehat\delta^{(\ell)}_a(h^{(\ell-1)})_b^\top}{n}
            +\frac{(\delta^{(\ell)})_a(\widehat h^{(\ell-1)}_b)^\top}{n}\right).
                                                                    \tag{16}
\]
Their actions again reduce by (15). The order-zero \(W^{(3)}\) action
differentiates as
\[
 \operatorname{var}(W^{(3)}_0v)=Jv+W^{(3)}_0\widehat v,
 \qquad
 \operatorname{var}(W^{(3)}_0^\top v)=J^\top v+W^{(3)}_0^\top\widehat v.
                                                                    \tag{17}
\]
The analogous \(W^{(2)}\) formula has no \(J\) term. Scalar contractions
differentiate as
\(\operatorname{var}\frac{u^\top v}{n}
=\frac{\widehat u^\top v}{n}+\frac{u^\top\widehat v}{n}\).
These rules preserve every derivative path through either reused hidden
matrix, including learned lower and top matrix increments.

The instructions have the following regularity, uniformly in width for
each fixed jet order:

* Addition, coordinate products, multiplication by previously computed
  scalar contractions, and the integrals' factors \(1/k\) are polynomial
  operations of fixed degree. A dot product divided by \(n\) is the empirical
  mean of the polynomial map \((u,v)\mapsto uv\).
* The initial \(z^{(2)}_0=W^{(2)}_0\phi(z^{(1)}_0)\) and
  \(z^{(3)}_0=W^{(3)}_0\phi(z^{(2)}_0)\) are generated nodes, not independent
  Gaussian roots. All derivatives of \(\phi,\phi',\beta\) used at these
  nodes are bounded smooth functions with bounded first derivatives.
* For the first transformed layer, generate \(x^{(1)}_0=F(z^{(1)}_0)\) as a
  polynomial node. In (13), the coefficient maps for \(h^{(1)}=\chi(x^{(1)})\)
  can be generated directly from the Gaussian root using
  \[
    \chi^{(t)}(F(z))=(\phi'(z)\partial_z)^t\phi(z).          \tag{18}
  \]
  For \(t=0\) this is \(\arctan z\). For \(t\ge1\), repeated
  differentiation gives rational functions with denominator a power of
  \(1+z^2\), decaying at infinity; their first derivatives are bounded
  too. This follows inductively from \(\phi'(z)=O(|z|^{-2})\) and
  differentiating such rational functions. The coefficient maps for
  \(\chi'(x^{(1)})\) in \(\widehat h^{(1)}\) are the same maps with \(t\) increased by
  one. Thus no unsupported global regularity of an inverse-coordinate
  composition is being assumed.
* The primitive transformation uses the polynomial
  \((z,a)\mapsto(1+z^2)a\), not inversion of a random scalar parameter.
  No inverse empirical Gram matrix or width-dependent cutoff occurs.

In particular every fixed coordinate map used here is polynomially bounded:
\[
                   |f(u)|\le C(1+\|u\|_2^d) .          \tag{19}
\]
The finite products in (13) can have large degree, but the degree is fixed
as \(n\to\infty\). There is no restriction to degree two or to a universal
degree shared by all possible jet programs. The empirical scalars appearing
in (15)--(16) will be removed from the program inputs by exact algebra below.

The only independent Gaussian matrices of the compiled program are
\[
 W^{(2)}_0:\mathbb R^{I_1}\to\mathbb R^{I_2},\qquad
 W^{(3)}_0,J:\mathbb R^{I_2}\to\mathbb R^{I_3}.        \tag{20}
\]
Each transpose in the program is the transpose of that same matrix.
All response coefficients and all weighted response vectors in (12) are
linear in \(J\), even though the joint program contains higher-degree
products of other coordinates. This also follows directly from the first
variation equations (5).

### Exact closure without empirical scalar feedback

Call a vector **pure** if it is generated from the Gaussian roots and
matrices (20) using only fixed parameterless coordinate maps and matrix
actions in either direction. Constants such as a fixed \(\rho\) may be
built into those maps. No empirical scalar is an input to a pure program.
All pure vectors used in a finite calculation may be included in a single
finite program by concatenating their constructions while preserving the
identities of the Gaussian matrices and roots.

Let \(\mathscr S\) be the scalar algebra of polynomials, with fixed
deterministic coefficients, in finitely many contractions
\(\frac{p^\top q}{n}\) of pure vectors on the same population.
For each population let \(\mathscr M\) consist of finite sums
\[
                   u=\sum_{a=1}^L\alpha_a p_a,
               \qquad \alpha_a\in\mathscr S,\quad p_a\text{ pure}.
                                                                    \tag{20a}
\]
These are identities between finite-width random objects. The scalars
\(\alpha_a\) may depend on every Gaussian matrix, including \(J\).
The construction never assumes that these scalars and vectors are
independent. All sum lengths and degrees below are fixed in width.

Here is closure for every operation required by the jet recurrences:

1. Addition and multiplication by a scalar in \(\mathscr S\) preserve
   (20a) by distributing the finite sums.
2. If \(u=\sum_a\alpha_ap_a\) and \(v=\sum_b\gamma_bq_b\) are on the
   same population, then
   \[
       u\odot v=\sum_{a,b}\alpha_a\gamma_b(p_a\odot q_b).
   \]
   Append \(p_a\odot q_b\) by the fixed polynomial coordinate map
   \((p,q)\mapsto pq\). Thus the result is again in \(\mathscr M\).
   This also covers multiplication by an initialized gate or gate
   derivative, since each such gate is pure.
3. For any compatible oriented matrix \(W\) in (20), including its
   transpose, exact finite-width linearity gives
   \[
                    Wu=\sum_a\alpha_a(Wp_a).
   \]
   Append each \(Wp_a\) to the pure program. Pulling a scalar outside
   a matrix product is valid even when that scalar depends on \(W\).
4. For same-population vectors as in item 2,
   \[
       \frac{u^\top v}{n}
         =\sum_{a,b}\alpha_a\gamma_b\frac{p_a^\top q_b}{n}
          \in\mathscr S.                                \tag{20b}
   \]
   Thus taking a contraction of previously expanded vectors produces
   only a polynomial in contractions of pure vectors. Its subsequent
   occurrences are scalar prefactors, handled by items 1--3.

The starting values and all initialized gate derivatives are pure. Every
operation in (13)--(17), as well as \(a_k=\widehat\delta^{(2)}_{k-1}/k\),
\(c=(1+(z^{(2)})^2)\odot a\), and the products in (12), is among these four
operations. In differentiating (13), a coefficient
\(f^{(t)}(v_0)\) becomes
\(f^{(t+1)}(v_0)\odot\widehat v_0\), which has the same form.
For example \(\widehat z^{(3)}_0=Jh^{(2)}_0\) is a pure vector.

The crucial restriction is that the nonpolynomial functions in this
calculation are evaluated only at the initialized preactivations, or at
the root in (18). All dependence on positive time-jet coefficients is
polynomial by the exact coefficient rule (13). There is therefore no
instruction \(f(\sum_a\alpha_ap_a)\) with nonpolynomial \(f\) and
empirical scalar prefactors that would defeat the expansion. This is an
identity for a finite jet, not a polynomial approximation of a trajectory.

Finite induction through the prescribed jet order proves that every
required vector belongs to \(\mathscr M\) and every required scalar
belongs to \(\mathscr S\). The induction may append many pure vectors,
but only finitely many, independent of width. Thus one pure program,
containing no empirical-scalar feedback, suffices for all the contractions
used by the calculation.

## 5. Primary theorem and its hypotheses in this application

The external probabilistic input is Greg Yang, *Tensor Programs III:
Neural Matrix Laws*, [arXiv:2009.10685v3](https://arxiv.org/pdf/2009.10685v3),
Definition 2.1 (printed pp. 6--7), **Setup 2.2** (p. 7), and
**Theorem 2.10** (p. 9).

The needed specialization is this: a fixed finite program uses independent
Gaussian matrices with entry variance \(1/n\), their transposes, and iid
jointly Gaussian root tuples independent of the matrices. Its instructions
are parameterless coordinate maps and matrix actions only. If its
nonlinearities obey (19), then for any fixed vector tuple and any
polynomially bounded test \(\psi\), the normalized empirical average of
\(\psi\) converges almost surely to the finite expectation of \(\psi\)
under the scalar law in Box 1. This theorem has no additional
rank-stability premise. We need only convergence in probability of pure
vector contractions, with test \(\psi(u,v)=uv\).

Here are the substitutions and the remaining checks, rather than an
extension of the supplied fixed-mesh theorem:

1. The theorem is applied to the **pure program constructed by
   (20a)--(20b)** from (13)--(17) and the products in (12), not to a program
   with empirical scalar inputs. Its instruction count and all coordinate
   functions are independent of \(n\). Contractions are evaluated only
   as output test averages for the theorem and combined by finite
   polynomial algebra outside the pure program.
2. Its random matrices are precisely (20), which meet the independence and
   entry-variance requirements. Repeated forward and transpose uses are
   permitted program instructions; they are not replaced by fresh matrices.
3. Its nonconstant Gaussian roots are \(z^{(1)}_0\) and \(G_4\).
   Deterministic zero and one vectors may be generated by constant maps.
   The transformed root \(F(z^{(1)}_0)\) is generated, so it need not be
   Gaussian. Constants, including the fixed \(\rho\), are built into
   parameterless maps; no random scalar is a program input.
4. All populations have cardinality \(n\), so the square-matrix version
   of the theorem applies after enumerating each population. If its root
   setup uses one common coordinate index, the artificially aligned root
   tuple \((z^{(1)}_{0,\alpha},G_{4,\alpha})\) is iid
   \(N(0,\operatorname{Id}_{2\times2})\).
   This is only an encoding of independent roots in equal-dimensional
   arrays. Every actual vector product and empirical mean in our program
   uses one population, and every matrix action has its type in (20).
   No cross-population coordinate identification is used in the equations.
5. The pure coordinate maps are bounded initialized gates, polynomials,
   and finite compositions thereof, all satisfying (19). Their degrees
   may be arbitrarily high but are fixed. The output contraction test
   \((u,v)\mapsto uv\) is polynomially bounded. No inverse, pseudoinverse,
   nondegenerate limiting Gram assumption, or empirical-scalar rank
   assertion is used.

For clarity, the passage from pure vectors to the actual expanded vectors
uses an exact identity. If \(V[J]=\sum_a\alpha_ap_a\) is (20a), then
\[
        \frac{\|V[J]\|_2^2}{n}
          =\sum_{a,b}\alpha_a\alpha_b\frac{p_a^\top p_b}{n}.
                                                                    \tag{20c}
\]
All contractions entering \(\alpha_a\) and the displayed dot products
divided by \(n\) converge jointly in probability by Theorem 2.10 applied
to the one finite pure program. Each \(\alpha_a\) is a fixed polynomial in those
contractions. Finite sums and products preserve convergence to finite
limits, so (20c) is tight. Consequently, for each fixed \(\rho\) and each
required vector \(V[J]\),
\[
                     \frac{\|V[J]\|_2^2}{n}=O_{\mathbb P}(1)               \tag{21}
\]
under the joint law of \(\mathcal F_n\) and \(J\). In particular we may
take, for every index tuple in (12),
\[
     V[J]=c_r,\qquad
     V[J]=b_t\odot q^{(2)}_u\odot\zeta_v,\qquad
     V[J]=b_t\odot\nu_u\odot c_v.                    \tag{22}
\]
These weights are part of the actual initial-jet program. Their
dependence on the hidden matrices and their returned responses is retained.

The proof invokes neither Appendix E.11 nor any other theorem for
empirical scalar feedback. It also invokes no convergence-in-mean
extension: Theorem 2.10 and finite algebra establish (21) for realized
random objects only. They do not justify a conditional expectation bound.
That step is supplied next. No iid claim about finite-width coordinates
after reuse appears in this argument.

## 6. Tight realized Gaussian quadratic forms give tight conditional traces

The following elementary fact is sufficient. Let \(\mathcal F\) be a
sigma-field, \(g\) an independent standard Gaussian vector of any finite
dimension, and \(T\) an \(\mathcal F\)-measurable linear map into
\(\mathbb R^n\). Put
\[
       Q=\frac{\|Tg\|_2^2}{n},\qquad
       \mu=\mathbb E[Q\mid\mathcal F].
\]
Set \(\mathsf M=T^\top T/n\succeq0\). Conditional Gaussian second and fourth
moments give
\[
 \mu=\operatorname{Tr}\mathsf M,\qquad
 \mathbb E[Q^2\mid\mathcal F]
       =(\operatorname{Tr}\mathsf M)^2+2\operatorname{Tr}(\mathsf M^2)
       \le3\mu^2.                                      \tag{23}
\]
For completeness, diagonalize \(\mathsf M\) and write
\(Q=\sum_j\lambda_jg_j^2\); use
\(\mathbb Eg_j^4=3\), \(\mathbb Eg_j^2g_k^2=1\) for \(j\ne k\),
and \(\sum_j\lambda_j^2\le(\sum_j\lambda_j)^2\).
For \(\mu>0\), Cauchy--Schwarz and
\(\mathbb E[Q\mathbf1_{\{Q>\mu/2\}}\mid\mathcal F]\ge\mu/2\)
therefore give
\[
             \mathbb P(Q>\mu/2\mid\mathcal F)\ge\frac1{12}.
\]
It follows, for every \(R>0\), that
\[
             \mathbb P(\mu>2R)\le12\mathbb P(Q>R).     \tag{24}
\]
The case \(\mu=0\) needs no lower bound. Thus tightness of the realized
quadratic forms implies tightness of their conditional means. This is the
Gaussian quadratic-form Paley--Zygmund argument, proved here in the exact
normalization needed. It does not assert uniform integrability or bounded
unconditional expectations.

Apply it with \(\mathcal F=\mathcal F_n\) and
\(g=\operatorname{vec}(\sqrt n J)\in\mathbb R^{n^2}\).
Each vector in (22) is an \(\mathcal F_n\)-measurable linear map of this
\(g\), and (21) applies. Consequently all the conditional traces
\[
 \mathbb E_J\frac{\|c_r\|_2^2}{n},\qquad
 \mathbb E_J\frac{\|b_t\odot q^{(2)}_u\odot\zeta_v\|_2^2}{n},\qquad
 \mathbb E_J\frac{\|b_t\odot\nu_u\odot c_v\|_2^2}{n}
                         \quad\text{are }O_{\mathbb P}(1).       \tag{25}
\]
Conditioning on \(\mathcal F_n\) is implicit in (25). There are finitely
many such traces. Conditional Cauchy--Schwarz, for example, gives
\[
 \left|\mathbb E_J
       \frac{c_r^\top(b_t\odot q^{(2)}_u\odot\zeta_v)}{n}\right|
 \le
  \bigl(\mathbb E_J\frac{\|c_r\|_2^2}{n}\bigr)^{1/2}
  \bigl(\mathbb E_J\frac{\|b_t\odot q^{(2)}_u\odot\zeta_v\|_2^2}{n}\bigr)^{1/2}
 =O_{\mathbb P}(1).                                    \tag{26}
\]
The other term in (12) is bounded in the same way, using the third trace
in (25). Therefore
\[
                       P_n(\rho)=O_{\mathbb P}(1)
                  \quad\text{for every fixed }\rho.             \tag{27}
\]
This is a bound for the signed coefficient with its full conditional
covariance. It does not assume a sign, isotropy, commutation, or independence
between a weight and that covariance.

## 7. Coefficient bounds and evaluation at the prescribed tiny readout

Use the seven deterministic amplitudes \(\rho_j=j\), \(j=0,\ldots,6\).
They are auxiliary evaluations of finite jets only; no assertion about
their trajectories on a common nonzero time interval is needed.
Apply Sections 4--6 to each. Since this is a finite set,
\[
                    \max_{0\le j\le6}|P_n(j)|=O_{\mathbb P}(1).
                                                                    \tag{28}
\]
The Vandermonde matrix \(V_{jm}=j^m\), with the constant column equal
to one, is a fixed invertible \(7\times7\) matrix: its determinant is
\(\prod_{0\le i<j\le6}(j-i)\ne0\). From the degree bound,
\[
     (A_{n,0},\ldots,A_{n,6})^\top
          =V^{-1}(P_n(0),\ldots,P_n(6))^\top.          \tag{29}
\]
Thus all coefficient magnitudes are tight, as asserted in (3). This step
supplies an explicit width bound on the polynomial coefficients through
the conditional trace bounds (25), without a theorem for conditional
expectations of arbitrary polynomial programs.

Finally, on the original coupled initialization,
\[
 P_n(n^{-1})-P_n(0)=\sum_{m=1}^6n^{-m}A_{n,m},\qquad
 n|P_n(n^{-1})-P_n(0)|\le\sum_{m=1}^6|A_{n,m}|.
                                                                    \tag{30}
\]
The right side is tight, proving (4). The probability here is over the
hidden initialization and \(G_4\); all auxiliary probes have already been
averaged out. This completes the candidate lemma.

## 8. Dependencies, provenance, and scope

The following supplied files were read, and are unchanged:

* [ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md](ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md):
  canonical transformed response, actual primitive, and complete source.
  Its equations (1)--(6) identify the response being used here. All finite
  equations needed for the present proof are restated in (1) and (5).
  SHA256: `067e1bc7d38c7409dab9639f29f84543abd2d0b7a9b9d543f9a47a6747e54d1e`.
* [ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md](ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md):
  its full-layer signed combination is the quantity in (2); its memory
  term remains inside the actual \(\zeta_i\). No sign estimate or
  off-diagonal cancellation is used to bound (12).
  SHA256: `f7f1b24a4f53cacdf0f86258eafb9b4ae86473b894d70fc9346af0726697df04`.
* [ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md](ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md):
  its zero-readout covariance jet is not substituted for a tiny-readout
  jet. No covariance-commutation premise from that discussion is used.
  SHA256: `5770d934df3840184d0b19bc3a15eae82290cc879201fe862786ba56d24c6c76`.
* [L3_FIXED_MESH_SOURCE_IDENTIFICATION.md](../L3_FIXED_MESH_SOURCE_IDENTIFICATION.md),
  including its final eleven lines: used to check the canonical Gaussian
  initialization and feature-time normalization. Its tiny-readout result
  concerns fixed clipped bounded-Lipschitz calculations. It is **not** a
  polynomial-program theorem and supplies none of (21), (25), or (29).
  SHA256: `ba5cd7a52674a2031bf18ccb633bbb6eeeadd8f2a207369b38695d66ec40c03a`.

The independent mathematical input is exactly the versioned primary
Theorem 2.10, Definition 2.1, and Setup 2.2 identified in Section 5.
Closure into a pure program with polynomial contraction prefactors is
proved in (20a)--(20c). No Appendix E scalar-feedback theorem is used.
The Gaussian quadratic-form estimate and the degree/interpolation
arguments are also proved in this note. No convergence in mean for
general polynomial-test programs is assumed or concluded.

Additional local context consulted was
`ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md` (the explicit tangent equations),
`TIME_ANALYTICITY_DERIVATIVE_AUDIT.md` (the restriction against a
primal-only uniform derivative estimate), and visible contextual material
in `CONTRACT_AND_LEDGER.md`. No additional proposition from those files is
an unproved premise of this lemma.

This transfers only the fifth coefficient of the full signed primitive
work for the actual uncut canonical model. It neither determines that
coefficient at zero readout nor estimates a Taylor remainder. It makes no
claim about a Taylor radius, positive-time convergence, exchange of time
and width limits, response continuation, clipping removal, or the complete
canonical research target. Status remains **candidate until independently
audited**.
