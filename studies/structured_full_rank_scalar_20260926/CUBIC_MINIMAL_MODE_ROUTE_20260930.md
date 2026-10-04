# One terminal response mode in a scalar bilinear flow

2026-09-30. Scoped, unreviewed construction in this study. Allowed and read
scientific inputs: `cubic_scalar_ode.py`,
`KERNEL_SCALAR_ROUTE_20260930.md`, `CUBIC_DENSE_DIAGNOSTIC_20260930.md`,
the supervisor-shared frozen `CUBIC_FEEDBACK_REPAIR_ROUTE_20260930.md`, and
the initialization and canonical equations in `dense_compare.py`.
No other studies, saved endpoints, or trained reference arrays were read.
No training experiment is part of this work. The companion prototype is
`cubic_minimal_mode_repair.py`.

The candidate adds **one task-conditioned readout response direction** to
the bilinear flow. Its state has `(m+1)^2` scalar coordinates, including
everything needed to decode a fixed arbitrary query. It has a positive
training kernel and a direct decoder with no interpolation repair. Its
specific benefit is exact recovery of the **terminal cubic coefficient**
omitted by projection onto the initial features. It generally does not
recover the whole cubic transient, genuine feature curvature, tanh
saturation, or arbitrary strong-learning accuracy.

## 1. Contract and hidden gradient convention

The target is the same two-hidden-layer tanh network, training data,
unhalved mean-square loss and mobilities `(n,1,n)` as the assigned sources,
with zero initial readout. The finite initialized weights may be inspected
once to form scalar contractions and then discarded. The prototype is a
finite-initialization implementation; it is not a new proof of a full-rank
Gaussian population limit. The small-amplitude comparison below is for a
fixed direction `y=a ybar`, `a>=0`, and a positive definite initial Gram.

Write `alpha=2/m`, `<c,d>=c^T d/n`, and `K_ab=<H_a,H_b>`.
Let the hidden-parameter Hilbert metric be

    <(dw,dW),(ew,eW)>_hidden = trace(dw.T ew)/n + trace(dW.T eW).

For any readout field C, let `Phi_(a,C)` be the hidden gradient of
`<C,H_a>` at initialization. With the source notation it has components

    gamma_(a,C) = d_a * C,
    beta_(a,C) = q_a * (W0.T gamma_(a,C)),
    Phi_(a,C) = (beta_(a,C) u_a.T, gamma_(a,C) p_a.T/n).

Thus `<Phi_(a,H_b),Phi_(c,H_d)>_hidden=S[(a,b),(c,d)]`.
For any initial hidden displacement `xi`, define `L_x xi=D H_x[xi]`.
The identity

    <C,L_x xi> = <Phi_(x,C),xi>_hidden

fixes all scalings. This construction requires derivative contractions in
addition to the existing K,S: K,S alone do not determine the needed
orthogonal readout direction or the extended response tensor.

## 2. A deterministic mode from the leading terminal readout

The fixed-initial-kernel residual is known from initial data alone:

    r0(t) = -exp(-alpha K t) y.

Use it only to select one initial direction, never as time-dependent
forcing. If `K=V diag(lambda_i) V.T`, `ytilde=V.T y`, the terminal iterated
integral in its eigenbasis is

    Ptilde_(i;jk)(infinity)
       = -ytilde_i ytilde_j ytilde_k /
         [alpha^3 lambda_i (lambda_i+lambda_j)
          (lambda_i+lambda_j+lambda_k)].

To verify it, integrate `r_i(t) r_j(s) r_k(u)` over
`0<u<s<t<infinity`; the substitutions `u=z`, `s=z+w`, `t=z+w+v`
give the three exponential rates
`alpha(lambda_i+lambda_j+lambda_k)`, `alpha(lambda_i+lambda_j)`,
and `alpha lambda_i`. Every rate is positive by K>0.

Transform the tensor

    Btilde_ijk = ytilde_i ytilde_j ytilde_k /
        [lambda_i (lambda_i+lambda_j) (lambda_i+lambda_j+lambda_k)]
    B_abc = sum_ijk V_ai V_bj V_ck Btilde_ijk

back to training indices. The deterministic terminal cubic readout is

    g = sum_abc B_abc L_a Phi_(b,H_c).

This is exactly `-alpha^3 sum_abc P0_(a;bc)(infinity) L_a Phi_(b,H_c)`.
Let `h_i=<H_i,g>`, `d=K^{-1}h`, and

    g_perp = g-sum_i d_i H_i,
    sigma = sqrt(<g_perp,g_perp>),
    E = g_perp/sigma.

If sigma=0, omit the extra mode: the entire missing terminal component is
already zero. If sigma>0, the extended readout basis is

    C=(H_1,...,H_m,E),   p=m+1,   G=diag(K,1).

The normalization removes label amplitude; along a fixed positive label
ray E is unchanged. Repeated eigenvalues and eigenvector signs do not
change g: the spectral formula is the explicit integral of the uniquely
defined matrix-exponential residual. No target outputs or chosen query
grid enter mode selection. The direction is selected by the whole leading
training transient, but compressed into one fixed response field.

For a finite initialization, g can be computed without storing an
`n*m^3` tensor. For each a, contract B first and use

    t_a = sum_bc B_abc (u_a dot u_b) beta_(b,H_c),
    s_a = sum_bc B_abc <p_a,p_b> gamma_(b,H_c),
    g = sum_a d_a * [W0 (q_a*t_a)+s_a].

The prototype rescales all eigenvalues and B by common positive scalars
before this calculation; the normalized E is unchanged. It projects
twice to reduce floating-point cancellation. Numerically unresolved
nonzero directions are a reported constructor failure, not fitted or
regularized directions.

## 3. Extended scalar contractions and closed flow

For training indices a,b and basis indices i,j, compute once

    A_ai = <H_a,C_i>,
    Splus[(a,i),(b,j)] = <Phi_(a,C_i),Phi_(b,C_j)>_hidden.

Analytically `A=[K,0]`. The prototype keeps the actual numerical A,G to
preserve the identities even at finite precision. Keep only

    v in R^p, Theta in R^(m*p),    v(0)=0, Theta(0)=0.

They represent `c=sum_i v_i C_i`,
`theta=sum_bj Theta_bj Phi_(b,C_j)`. Form the training feature matrix

    F_ai = A_ai+sum_bj Splus[(a,i),(b,j)] Theta_bj,
    f_a = sum_i F_ai v_i,    r=f-y.

The frozen candidate is

    v' = -alpha G^{-1} F.T r,
    Theta' = -alpha outer(r,v).

No hidden-field evaluation occurs in this ODE. The model is the exact
gradient flow of the finite bilinear prediction
`<c,H_x+L_x theta>`, restricted to the stated readout and hidden spans.
The theta coordinates may be redundant; their displayed evolution still
equals the physical hidden gradient because that gradient lies in the
span of the same Phi directions. No inverse of Splus is required.

Differentiation gives

    r' = -alpha Kplus r,
    Kplus_ab = (F G^{-1} F.T)_ab
               +sum_ij v_i v_j Splus[(a,i),(b,j)].

Both terms are Gram matrices. Consequently the training loss is
nonincreasing, and `r=0` freezes the entire state. The smooth finite ODE
exists globally: loss bounds |r|, and the two state equations imply
`|v'|+|Theta'| <= C(1+|v|+|Theta|)` on every loss sublevel set;
Gronwall excludes finite-time escape. Global existence does not imply
fitting for arbitrary labels.

Readout energy obeys the exact identity

    d(v.T G v)/dt = -2 alpha r.T f.

This removes the artificial discrepancy between a surrogate training
trajectory and its own readout energy. It does not enforce the tanh output
bound: the linearized features `H_x+L_x theta` remain unbounded.

## 4. Direct decoder and terminal cubic scope

For a query x, precompute only scalar coefficient functions

    k_xi = <H_x,C_i>,
    T_xibj = <Phi_(x,C_i),Phi_(b,C_j)>_hidden.

Then

    fplus(x) = sum_i v_i [k_xi+sum_bj T_xibj Theta_bj].

At a training alias these coefficients are exactly the corresponding
rows of A,Splus. Thus the query decoder equals the training output
identically. It uses no cubic integral states and no K-interpolation
completion.

For fixed label direction and small a, let Q be the orthogonal projector
onto span(C). The leading hidden motion and readout are the original
quadratic theta2 and linear c1. The extended readout's cubic component
is Q c3, where

    c3(t) = -alpha^3 sum_abc P0_(a;bc)(t) L_a Phi_(b,H_c).

To see this, project the readout equation
`c'=-alpha sum_a r_a (H_a+L_a theta)` onto span(C). At order one it
is unchanged because H_a is in the span. At order three the feature
forcing is precisely Q applied to the displayed c3 derivative.
Its residual-feedback contribution is in span(H), also retained by Q.
The additional E components first affect hidden motion at order four.

Since `(I-Q)c3` is orthogonal to every initial training feature, the
training output has the same cubic coefficient at every time. The
general query discrepancy at order three is

    <(I-Q)c3(t),H_x>.

It is usually nonzero at finite t. At infinity c3(infinity)=g belongs
to span(C) by construction, so this term vanishes for every query.
Therefore the terminal output has the full cubic coefficient, whereas
the m-mode direct bilinear decoder need not. This is an exact assertion
about the perturbative coefficients, not evidence of unit-label fidelity.

For a fixed finite smooth initialized network with K>0, the usual small
amplitude bootstrap can strengthen this to terminal O(a^5) output error:
coercivity near K makes the residual exponentially integrable;
`c=O(a)` and `theta=O(a^2)` follow; the tanh feature linearization has
O(a^4) remainder, producing O(a^5) output; the leading c3 mismatch has
the terminal cancellation just proved. A complete uniform population
remainder theorem is not supplied here. In particular the block-population
theorem in the source cannot silently be promoted to full-rank Gaussian
initialization. The fully established claim of this note is the finite
construction and its cubic coefficient identity.

For arbitrary previously unspecified finite-network queries, evaluation
of k_x,T_x still requires the original initialization, or a separately
declared coefficient-function representation. The returned runtime model
stores neither that initialization nor a hidden neuron dictionary. The
prototype supports one-time coefficient construction on specified queries;
its ODE and subsequent prediction use only scalars. For an initial law,
one may define k,T by initial-law contractions, but their efficient
full-rank population construction is not established by this prototype.

## 5. Cost, falsifiers, and status

With one extra nondegenerate mode:

* Evolving state: `p+mp=(m+1)^2` scalars; query count adds no state.
* Static training coefficients: G (`p^2`), A (`mp`),
  Splus (`m^2 p^2`), labels and factorizations: O(m^4).
* RHS: O(m^2 p^2)=O(m^4), plus the fixed p-dimensional solve.
* Static coefficients per query: `p+mp^2=O(m^3)`.
* Finite initialization cost, using dense W: O(n^2 m^2+n m^4+m^4),
  with initialization-sized working arrays discarded after construction.
  Counting this work is essential; no end-to-end advantage is proved.

The added dynamic cost versus the m-mode bilinear model is `2m+1`.
Relative to that candidate this is one new readout mode and its m hidden
response directions, not an arbitrary dictionary escape. Pure K,S data
are insufficient: one must compute E and the new derivative contractions.

The strongest reason it might help is that it couples an explicitly
missing readout response back into hidden evolution while removing the
old interpolated decoder. The strongest contrary evidence in the assigned
diagnostic is that restoring discarded unsaturated response directions
can increase an already overlarge feature approximation. One mode gives
no general damping, no guaranteed lower passive error, and no resolution
of genuine tanh saturation. The scientifically meaningful empirical claim
remains open until a separately authorized, frozen comparison with the
m-mode bilinear and exact dense references. Failure would reject this
specific enrichment, not all aggregate closures.

Status: frozen candidate and API prototype, derivation only; no training
results, arbitrary-accuracy claim, or promotion. Deterministic algebraic
verification, if run, is recorded below separately.

## 6. Frozen coefficient handoff and deterministic check

The supervisor supplied a gated overlap extension after the ungated
candidate above was frozen. The additional constructor API is

    bounded_gram_coefficients(w,W,inputs,labels,queries,batch_size=16)

and returns only `G[p,p]`, `R0[p,m]`, `S[m,p,m,p]`, `kx[q,p]`,
`query_B[q,p,m,p]`, `querydiag[q]`, and scalar mode metadata. Here
`R0[:m]=I`, `R0[m:]=0`, and `querydiag_x=<H_x,H_x>`.
There are no hidden vectors, widths, weights, callables closing over
weights, or chosen training trajectories in the returned dictionary.

This coefficient interface does not itself assert validity of the gate.
For the supervisor's feature-overlap equation, turning gates off gives
exactly the ungated bilinear flow above after the linear coordinate map

    R = G^{-1} F.T,
    R'_ia = -alpha sum_jbc (G^{-1})_ij r_b v_c S[(a,j),(b,c)],
    v' = -alpha R r.

An extra gate equal to `1+O(a^2)` near zero labels changes R' first at
order four, so the same leading theta2 and terminal cubic cancellation
survive. This is a formal order statement, not a strong-label error bound
for a gated model. Mode construction itself remains unchanged.

The scoped author performed deterministic finite algebra checks on
2026-09-30. The frozen prototype SHA256 is
`b878f26e425a1be8d75f9811b31e73a39e69e5a15e258aff2ec28dc7fb7f60de`.
The maintained reproduction source is
`check_cubic_minimal_mode_repair.py`; run it from the repository root with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python studies/structured_full_rank_scalar_20260926/check_cubic_minimal_mode_repair.py

It creates a fresh timestamped output directory on each reproduction.
The first executed result is preserved at
`data/generated/structured_full_rank_scalar_20260926/cubic_minimal_mode_20260930/check.json`.
That execution used a temporary copy of the same check before moving its
source into the study and making reproduction output directories unique.
No scientific check or model source was changed by that source move.

At n=48,m=3, direct finite-network derivative contractions agreed with
the scalar output to `1.39e-17`, with the scalar derivative `-alpha K r`
to `2.78e-17`, and with the readout-energy identity to `6.94e-18`.
Training-query alias error was `1.39e-17`; the random checked kernel's
smallest eigenvalue was `0.02623`. All gated coefficient arrays agreed
with the corresponding standalone model arrays. Independent scalar
quadrature verified all 27 ordered-exponential integral formulas to
`2.08e-17`. Positive label-rescaling changed the normalized mode by at
most `3.67e-15`. Zero labels produce the stationary m-mode fallback.

One constructor-only width-1024,m=3 check with the prescribed Gaussian
seed streams and three training aliases took `0.0217` seconds with one
BLAS thread. The selected orthogonal component retained 0.5592 of the
unprojected response norm, and its initial-feature orthogonality error
was `3.99e-17`. This single timing is not an asymptotic performance claim.
No neural, scalar, gated, or fixed-kernel training integration was run.

These checks support the finite algebra and prototype implementation.
They do not independently review the mathematical argument, test the
hard-task output errors, or promote the construction to established work.
