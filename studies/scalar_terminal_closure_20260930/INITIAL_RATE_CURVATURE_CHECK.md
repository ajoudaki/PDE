# Independent check of the initialized one-input rate curvature

Candidate read in full: `INITIAL_RATE_CURVATURE.md`, SHA256
`6d79cb0c56bd8e3fd2f1f0b896991df6d3da6f62a1fa160a79ebfca45986c0cc`.
Exact-model dependency read in full: `TERMINAL_SCALAR_THEOREM.md`, SHA256
`fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`.
Checker: `/root/scalar_information`, 2026-09-30, on the supervisor's bounded
assignment. No other study or prior review was read. The dependency's exact
model and the use of its conditional terminal conclusion were checked; this
report does not replace a separate check of the complete terminal theorem.
No numerical training or new research route was undertaken.

**Verdict: PASS.** The arbitrary-finite-width initialized identities
`C''(0)=32T`, `L'''(0)=-64G^3-64T`, and the fixed-positive-exponential-mixture
obstruction are correct under the stated hypotheses. No correction to their
formulas or theorem scope is required.

## 1. Model and arbitrary-width derivative check

For m=1 the dependency gives exactly

    r'=-Cr+|r|b,
    C=2[<g,g>+<ell,ell>+<d,d><k,h>],
    b=tau^(-1)<d,v><h-k,h>,

with `<a,b>=a^T b/n` and the actual W0 and W0^T. The normalized input removes
any additional factor from the first-layer contribution. At the stipulated
initial state, r=-y, |r|=1, d=ell=0, w'=2yg, and the first derivatives of
A,v,k,B,h,g vanish. Since r is nonzero, the finite ODE is smooth in a
neighborhood of this state despite the absolute-value notation.

Put `p=g odot j`, `u=s odot W0^T p`, as in the candidate. Differentiating once
more gives

    d'=2yp,                    ell'=2yu,
    A''=4u x^T/sqrt(d),         h''=4s^2 odot W0^T p,
    v''=4p,                    B''=4p h^T/n,
    g''=4j odot [Hp+W0(s^2 odot W0^T p)].

For example, A'' follows from `-2r ell' x^T/sqrt(d)`; h'' then uses
`x^T x/d=1`. B'' has only `v'' k^T/n`, because v=v'=k'=0 initially.
The displayed g'' follows by differentiating tanh(Bh), whose first inner
derivative is zero. No neuron symmetry or eigenbasis reduction is involved.

Contraction with g uses the true transpose:

    <g,j odot W0(s^2 odot W0^T p)>
      =<W0^T p,s^2 odot W0^T p>=E.

Consequently

    <g,g>''=8(HD+E)=8T,
    <ell,ell>''=8E,
    <d,d>''=8D.

The value and first derivative of `<d,d>` vanish, so its product with
`<k,h>` contributes only `8DH`. Hence

    C''=2[8T+8E+8DH]=32T,

with `C(0)=2G` and `C'(0)=0`. These calculations preserve all factors of n.

Because d=O(t), v=O(t^2), and h-k=O(t^2), the memory drift b is O(t^5).
The bounded factor tau^(-1) and the bounded remaining h factor do not change
that order. Thus b,b',b'' all vanish at zero as required by the loss-jet proof.

## 2. Loss and logarithmic derivatives

Directly from the residual equation, the same calculation gives

    r'(0)=2Gy,
    r''(0)=-4G^2y,
    r'''(0)=(8G^3+32T)y.

Differentiating L=r^2 therefore yields

    L'(0)=2r r'=-4G,
    L''(0)=2(r'^2+r r'')=16G^2,
    L'''(0)=6r'r''+2r r'''=-64G^3-64T.

Alternatively, the sign of r is locally fixed and
`(log L)'=-2C+2 sign(r)b`; its next two derivatives give
`(log L)''(0)=0` and `(log L)'''(0)=-64T`. The two checks agree.

Strict positivity also holds as stated. Finite tanh preactivations imply
`j_i>0`. If G>0 then g is nonzero, so p is nonzero and D>0. The same condition
forces h nonzero, since h=0 would imply g=tanh(W0h)=0. Thus H>0, and
T=E+HD>0 even if E happens to vanish. There is no missing probabilistic or
nondegeneracy assumption beyond the candidate's G>0.

## 3. Positive-mixture obstruction and remainder

For a probability measure on [0,infinity) with finite second moment, dominated
convergence gives the first two right derivatives at zero of its Laplace
transform: `L_mix'(0)=-E[lambda]` and `L_mix''(0)=E[lambda^2]`.
The required dominators are lambda and lambda^2, both integrable under the
stated assumption. Matching the candidate's first two derivatives forces

    E[lambda]=4G, E[lambda^2]=16G^2,
    E[(lambda-4G)^2]=0.

Nonnegativity of the integrand implies lambda=4G almost surely. Therefore the
measure is a single atom and all higher derivatives exist; an additional
third-moment assumption is unnecessary. Its third loss derivative is -64G^3,
which disagrees with the actual derivative by -64T<0.

The actual local solution is smooth, so Taylor expansion through degree three
has remainder O(t^4). Subtracting exp(-4Gt), whose lower-order coefficients
match, gives precisely

    L(t)-exp(-4Gt)=-(64T/6)t^3+O(t^4)
                  =-(32/3)T t^3+O(t^4).

The obstruction concerns an exact fixed positive decay spectrum and, as
written, a positive-mixture candidate that matches the initial derivatives.
It supplies no quantitative uniform-error lower bound for all approximate
mixtures, and no such bound is claimed. It does not exclude signed spectra,
nonlinear finite ODEs, or every finite linear state-space representation;
the candidate explicitly leaves those possibilities open. An evolving
instantaneous scalar decay rate is what the calculation establishes, not
universal necessity of a nonlinear realization in every enlarged state.

## 4. Boundary of the checked result

The result holds at every finite width and for arbitrary finite A0,W0 with
g0 nonzero, at the specified zero-readout/value-memory initialization. It is
a one-input theorem and does not assert generic multi-input fitting,
monotonicity of the rate at all times, a population limit, or an efficient
initialization-to-terminal scalar evaluator. The dependency's conditional
terminal model may freeze the complete generator with cubic loss error once
its hypotheses hold; this initialized calculation supplies no proof that
those hypotheses will later hold. These limitations are represented correctly
in the candidate.

## Root verification of title-only clarification

After the independent check, root changed only the candidate's title to
“Feature learning changes the initial scalar decay rate.” The former title
could suggest an obstruction to every linear realization; the actual checked
statement excludes only a fixed positive decay spectrum matching the stated
initial derivatives. No equation, hypothesis, proof or conclusion changed.
Root verified the one-line edit and the resulting candidate SHA256:

`7a01b2b1b4f8bf99c5f89f10d25f69a802cbf2237ec2f08c4ed340a3087ca62b`.

The original independent report remains attached to its original hash.
