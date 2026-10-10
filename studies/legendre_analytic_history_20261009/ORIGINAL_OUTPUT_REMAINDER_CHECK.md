# Scoped check of the original-model output lower bound

Verdict: **PASS.** No gap was found in the width- and order-uniform
remainder estimates or in propagation of the hidden-matrix defect to the
actual output. The fifth-order prediction coefficient and the resulting
\(q^{-10}\) lower bound are correct under the paper's imported
order-independent fitting statement. Identity activations are admissible,
and one initialization event supports all finite orders.

The conclusion rules out subpolynomial order for the displayed absolute
accuracy target of the original method. It does not by itself rule out the
headline's relative-error criterion; the candidate correctly identifies
the additional dense-variability upper bound needed for that stronger
conclusion.

## Scope and frozen inputs

The complete candidate was read. The only scientific sources consulted for
this check were that candidate and the original setup, fitting statements,
Legendre equations, and projection identities in the three allowed paper
files. No other study notes, prior verdicts, or experiments were used. The
unchanged required rigorous-mathematics and canonical-notation instructions
were reused. This is a scoped proof check, not a promotion review or an
independent reproof of the imported global fitting theorem.

| Input | SHA-256 |
| --- | --- |
| `ORIGINAL_OUTPUT_ANALYSIS.md` | `6bf9c51316b5425eb0cb9288a0859b24e6f08d5adcf6155e21bf2dbfad967320` |
| `paper/compact.tex` | `47199d5c9e374b80b9eafefd60699c2f4bfe06dde00ebd0a1c53e2805598a0c4` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |

## Admissibility and the common event

The paper requires strip holomorphy and bounded first derivative, but does
not require a non-affine activation. The identity is entire, is real on
the real axis, and has derivatives \(1\) and \(0\). For example,
choosing strip parameter \(a=2\) gives \(\beta=10\). With
\(L=m=d=2\), normalized inputs \(v_1=e_1,v_2=e_2\), and actual
inputs \(x_a=\sqrt2v_a\), all input norms are correct. Identity
activations preserve the population Gram, so every population Gram is
\(I_2\), \(\gamma=1\), and \(m/\gamma=2\). Nonzero labels
satisfying \(Y\le\tfrac12\beta^{-60}\) exist and obey the exact
small-label condition.

On the paper's initialization event, its final empirical-Gram condition
becomes \(G/2\succeq I_2/4\), hence
\(G=A_0^\top B_0^\top B_0A_0\succeq I_2/2\). The initialized
operator bounds and subsequent dense fitting bounds have constants
independent of width. Claim `cp:legendre-fit` explicitly supplies the
corresponding physical bounds for every finite \(q\) on this same
initialization event. Thus no union bound over orders, or order-dependent
width threshold, is being inserted. Its probability tends to one by
`cp:fit`.

## Scaled equations and uniform short-time estimates

With \(A=W^{(1)}/\sqrt n\), \(B=W^{(2)}\), and
\(c=w/\sqrt n\), the training prediction vector is
\(f=A^\top B^\top c\). Substituting \(m=2\) in the canonical
mobility-scaled equations gives exactly
\[
\dot A=-B^\top cr^\top,\qquad
\dot B=-c(Ar)^\top,\qquad
\dot c=-BAr.
\]
The original Legendre defect has prefactor \(\rho/n\); each of
its two unscaled history errors contributes \(\sqrt n\).
Consequently its scaled defect is exactly
\(\mathcal E=\rho e_b e_h^\top\), with
\(h=A\) and \(b=cr^\top/\rho\). There is no lost width or
sample normalization.

The width-uniform short interval can be made explicit from the imported
physical bounds. Both trajectories have
\(\|A\|_{\rm op},\|B\|_{\rm op}\le9\) and
\(\|r\|_2\le\|y\|_2\), so
\[
\|c(t)\|_2\le81\|y\|_2t,
\qquad \|f(t)\|_2\le6561\|y\|_2t.
\]
Therefore \(|\rho(t)-Y|\le6561Yt\), and taking
\(t_*\le1/13122\) ensures \(\rho\ge Y/2\) independently of
width, order, and initialization within the event. The first-layer
equation similarly yields \(A-A_0=O(t^2)\). All constants may be
enlarged to depend on the fixed labels, as permitted by the claim.

Since \(\tau\ge1\), the endpoint kernel bound gives
\[
\|(\Pi_q^{\tau(t)}g)(\tau(t))\|
\le q^2\int_0^t\rho(s)\|g(\tau(s))\|\,ds
\]
for either history after subtracting its constant prefix. There is no
inverse residual factor after changing variables. It follows that on
\(0\le t\le\min(t_*,q^{-2})\),
\[
e_b=O(t),\quad e_h=O(t^2),\quad
\mathcal E=O(t^3),\quad B-B_0=O(t^2),
\]
with constants independent of \(n,q\). This coarse estimate is an
essential step: it prevents an unnecessary factor of \(q\) from
entering the subsequent physical expansions.

Writing \(u=B_0A_0y\), the refined endpoint expansions are
\[
e_b=-u y^\top t/Y+O(q^2t^2),\qquad
e_h=\tfrac12B_0^\top u y^\top t^2+O(q^2t^3).
\]
The product of the remainders is \(O(q^4t^5)\). The restriction
\(q^2t\le1\) makes it \(O(q^2t^4)\), which validates the
candidate's crucial uniform forcing expansion
\[
\mathcal E(t)=E_3t^3+O(q^2t^4),\qquad
E_3=-\tfrac12\|y\|_2^2uu^\top B_0.
\]
All occurrences of the full mixer use its operator norm. The proof never
requires the width-growing Frobenius norm of \(B_0\); only mixer
differences are measured in Frobenius norm. The first layer has two
columns, so its Frobenius norm is bounded by \(\sqrt2\) times its
operator norm.

## The output coefficient includes the readout response

Let \(\Delta\) denote Legendre minus dense quantities. Subtracting
products one factor at a time shows that the physical polynomial vector
field is Lipschitz in
\(\|\Delta A\|_F+\|\Delta B\|_F+\|\Delta c\|_2\)
with a width-independent constant on the stated physical region. Gronwall
and the coarse \(O(t^3)\) forcing first give total discrepancy
\(O(t^4)\). Because the first layer and readout have no direct defect,
their equations sharpen this to
\[
\Delta c=O(t^5),\qquad \Delta f=\Delta r=O(t^5),\qquad
\Delta A=O(t^6).
\]
These steps are valid uniformly in \(q\) on the same short interval.

The refined hidden-matrix and readout expansions are then
\[
\Delta B=\tfrac14E_3t^4+O(q^2t^5),\qquad
\Delta c=\tfrac1{20}E_3A_0y\,t^5+O(q^2t^6).
\]
In particular, omitting the readout discrepancy would give an incorrect
coefficient. The exact output subtraction has three terms. Its
first-layer term is \(O(t^7)\); the other two leading terms are
\[
\tfrac14 A_0^\top E_3^\top u\,t^5
\quad\text{and}\quad
\tfrac1{20}A_0^\top B_0^\top E_3A_0y\,t^5.
\]
They have the same sign. Using
\(\|u\|_2^2=y^\top Gy\) and
\(A_0^\top B_0^\top u=Gy\), their sum is
\[
\Delta f(t)
=-\frac3{20}\|y\|_2^2(y^\top Gy)Gy\,t^5+R_q(t),
\qquad \|R_q(t)\|_2\le Cq^2t^6.
\]
The constant remains uniform over the initialization event and over
\(n,q\). For each fixed finite order, the stored-state ODE is analytic
near initialization because \(\tau(0)=1\) and \(\rho(0)=Y>0\),
so the stated fifth-derivative interpretation is also valid. Multiplying
the coefficient by \(5!\) gives the claimed factor \(-18\).

## The uniform lower bound and its precise consequence

The Gram lower bound implies that the coefficient norm is at least
\(a_y=3\|y\|_2^5/80\). Choosing
\(\eta\le\min(t_*,1,a_y/(2C))\) and evaluating at
\(t_q=\eta/q^2\) makes the remainder at most half the leading
term. Thus the prediction-vector norm is at least
\(a_y\eta^5q^{-10}/2\), and one of the two training coordinates
has at least this magnitude divided by \(\sqrt2\). The whole-sphere
supremum equals the vector norm in this linear-in-input example, since
the two normalized training inputs form an orthonormal basis.

All constants can be selected once for the fixed problem and the common
initialization event. The conclusion consequently allows arbitrary
width-dependent finite orders \(q=q(n)\), rather than only orders
held fixed before the width limit.

Comparing with the displayed original-method target
\(CY/(\sqrt n[\log(en)]^3)\) gives exactly the necessary order
\(q\ge c_{\rm problem}n^{1/20}[\log(en)]^{3/10}\).
This excludes \(q=n^{o(1)}\) for that absolute target under the
paper's full activation/data assumptions. It gives no endpoint lower
bound and does not establish optimal order. The paper's lower bound on
independent dense variability cannot turn this into a failure of relative
accuracy; an appropriate upper bound on that denominator is indeed still
needed. No stronger conclusion should be attributed to this candidate.

No corrective edits are requested within the assigned scope.
