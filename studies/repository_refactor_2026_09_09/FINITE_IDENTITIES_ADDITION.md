## 5. Two-layer quadratic and identity reductions

Fix a width `n>=1`, one datum `x=1` in dimension one, a real label `y`, and
two hidden layers. Write the stored parameters as
`u=W^(1) in R^n`, `B=W^(2) in R^(n by n)`, and
`a=W^(3) in R^n`; the first matrix is identified with its sole column.
All three mobility multipliers are one. The parameter metric is

\[
 \frac{\|du\|_2^2}{n}+\|dB\|_F^2+\frac{\|da\|_2^2}{n}.
 \tag{8}
\]

In particular `B` already is the stored, scaled matrix: there is no further
width factor in `Bh`. If one instead stores `\mathsf W=\sqrt n B`,
(8) is `n^{-1}` times the Euclidean metric on `(u,\mathsf W,a)`.
The residual and loss are `r=f-y` and `\mathcal L=r^2`.
A prime below means the metric gradient of the output (unit feature ascent),
and the physical flow is always

\[
 \dot\theta=-2r\theta'.
 \tag{9}
\]

Thus the prime is an algebraic vector field. Its integral curves need not be
global, and no positive or invertible feature clock is assumed. The displayed
physical equations hold also when `r=0` or when the label has either sign.
No initialization distribution is assumed; in particular, no readout is reset
or replaced by its limiting value.

Let `Q(z)=z^2` and `I(z)=z`, coordinatewise. The strings `QI`, `IQ` and `QQ`
specify the first and second hidden activations, in that order. Set
`h=phi^(1)(u)`, `z=Bh`, `v=phi^(2)(z)`, `f=a^T v/n`.
The exact output-ascent fields and scalar kernel blocks are as follows;
the block order is first layer, middle matrix, readout.

\[
\begin{array}{c|c|c|c|c}
 &\text{auxiliary fields}&u'&B'&a'\\ \hline
QI&q=B^Ta&2u\odot q&a h^T/n&z\\
IQ&b=a\odot z,\ q=B^Tb&2q&2b h^T/n&z^2\\
QQ&b=a\odot z,\ q=B^Tb&4u\odot q&2b h^T/n&z^2
\end{array}
\tag{10}
\]

\[
\begin{array}{c|c|c|c}
 &K_1&K_2&K_3\\ \hline
QI&4(u^2)^Tq^2/n&\|a\|_2^2\|h\|_2^2/n^2&\|z\|_2^2/n\\
IQ&4\|q\|_2^2/n&4\|b\|_2^2\|h\|_2^2/n^2&\|z^2\|_2^2/n\\
QQ&16(u^2)^Tq^2/n&4\|b\|_2^2\|h\|_2^2/n^2&\|z^2\|_2^2/n
\end{array}
\tag{11}
\]

Squares and products between vectors in these formulas are coordinatewise.
To verify the first row, differentiate `f=a^TB(u^2)/n` to obtain
`df=z^T da/n+a^T(dB)h/n+(2u\odot B^Ta)^Tdu/n`.
The inverse metric (8) multiplies the `u,a` derivatives by `n` and leaves
the matrix derivative unchanged. For the other two rows,
`df=(z^2)^Tda/n+2(a\odot z)^T[(dB)h+Bdh]/n`, with
`dh=du` for `IQ` and `dh=2u\odot du` for `QQ`. This proves (10).
Taking the squared norm of each block of (10) in (8), using
`\|bc^T/n\|_F^2=\|b\|_2^2\|c\|_2^2/n^2`, proves (11).
Consequently, with `K=K_1+K_2+K_3`,

\[
 f'=K,\qquad \dot f=\dot r=-2rK,\qquad
 \dot{\mathcal L}=-4r^2K.
 \tag{12}
\]

### Isometric block matrices and the two Lax identities

For block operators, pass each neuron vector to ordinary Euclidean
coordinates by `\widehat v=v/\sqrt n`. Indeed
`\widehat v^T\widehat w=v^Tw/n`. A matrix acting between two neuron
spaces retains its numerical entries under these isometries; a map
`c\mapsto ca` from a scalar space has column `\widehat a`; and the
functional `v\mapsto h^Tv/n` has row `\widehat h^T`.
Thus transpose in the following matrices is ordinary Euclidean transpose.
This specifies all block weights, including the scalar blocks.

For `QI` define

\[
 \mathsf Q=[\widehat a\ \ B],\qquad
 S=\begin{pmatrix}0&\widehat h^T\\\widehat h&0\end{pmatrix},
 \quad J=\operatorname{diag}(-1,I_n),\quad
 \mathsf L=J\mathsf Q^T\mathsf Q.
 \tag{13}
\]

Equation (10) gives `\mathsf Q'=\mathsf Q S`: its first column is
`B\widehat h=\widehat z`, and the remaining columns are
`\widehat a\widehat h^T=a h^T/n`. Since `S^T=S` and `JS=-SJ`,

\[
 \mathsf L'=J(S\mathsf Q^T\mathsf Q+\mathsf Q^T\mathsf Q S)
            =\mathsf L S-S\mathsf L=[\mathsf L,S].
 \tag{14}
\]

The lower block of `\mathsf L e_0` is `\widehat q`, and
`h'=4h\odot q`. Hence `(h,\mathsf L)` has an exact autonomous
current-state equation on the states obtained from raw parameters. Its
output is `f=\widehat q^T\widehat h`. Writing
`g=\|a\|_2^2/n` and `C=B^TB`, which are respectively the top-left and
bottom-right blocks of `J\mathsf L`, its kernel is

\[
 K=\frac{h^TCh}{n}+g\frac{\|h\|_2^2}{n}
                  +4\frac{h^Tq^2}{n}.
 \tag{15}
\]

The raw current operator `BB^T-aa^T/n` is also conserved: differentiating
the two products with (10) gives the same matrix
`(az^T+za^T)/n` in each case.

For `IQ` use a scalar as the last block and define

\[
 \mathsf P=\begin{pmatrix}B\\\widehat h^T\end{pmatrix},\qquad
 S=\begin{pmatrix}0&\widehat b\\\widehat b^T&0\end{pmatrix},
 \quad J=\operatorname{diag}(I_n,-1),\quad
 \mathsf L=J\mathsf P\mathsf P^T.
 \tag{16}
\]

Here `\mathsf P'=2S\mathsf P`: the top block is
`2\widehat b\widehat h^T=2b h^T/n`, and the last row is
`2\widehat b^TB=2\widehat q^T`. Differentiating, and again using
`JS=-SJ`, gives

\[
 \mathsf L'=2[\mathsf L,S].
 \tag{17}
\]

The upper block of `\mathsf L e_*` is `\widehat z`; the bottom-right
block of `J\mathsf L` is `\rho_h=\|h\|_2^2/n`, and its top-left block is
`C=BB^T`. Therefore `(a,\mathsf L)` closes on raw-image states:
`a'=z^2`, `b=a\odot z`, `f=a^Tz^2/n`, and

\[
 K=\frac{\|z^2\|_2^2}{n}
       +4\rho_h\frac{\|b\|_2^2}{n}+4\frac{b^TCb}{n}.
 \tag{18}
\]

These claims are exact block identities, not a reduction to a fixed number
of scalar coordinates. Their block matrices still have size `n+1`.
Multiplying their entire vector fields by `-2r` returns both systems to
physical time, including their output and kernel readouts.

For completeness the commutator laws do imply isospectrality without
assuming that `\mathsf L` is self-adjoint. Along a raw solution, either
physical law has the form `\dot{\mathsf L}=[\mathsf L,F(t)]`, with
`F=-2rS` for `QI` and `F=-4rS` for `IQ`. On any compact interval where
the raw solution exists, `F` is continuous and bounded. The integral
equation for `U'=-FU`, `U(0)=I`, has a unique solution: successive
integrations have norm bounded by `(Mt)^k/k!` when `\|F\|<=M`, so the
series converges uniformly, solves the equation, and gives uniqueness by
the same iterated difference bound. The equation `V'=VF`, `V(0)=I` has
the same construction. Differentiating `VU` gives zero, hence `VU=I`;
in finite dimension this also gives `UV=I`. Differentiation now yields
`(V\mathsf L U)'=0`, so
`\mathsf L(t)=U(t)\mathsf L(0)U(t)^{-1}`. Similarity preserves the
characteristic polynomial because
`det(\lambda I-U\mathsf L U^{-1})=det(\lambda I-\mathsf L)`.
The same argument applies to feature ascent on its interval of existence.

### The spectrum does not determine the instantaneous output velocity

For `QI` take `n=3`, `u=(1,\sqrt2,\sqrt3)`, `B=I_3`, and either

\[
 a_1=(1,0,0),\qquad a_2=(1/3,-2/3,2/3).
 \tag{19}
\]

Both states have `h=(1,2,3)`, `\|a_i\|_2^2=1`, and `a_i^Th=1`.
Thus their output is `f=1/3`. Put
`d=(1,1,-1)^T` and `O=I-2dd^T/3`. Since `d^Td=3`, multiplication
gives `O^TO=I`, `Oa_1=a_2`, and `Oh=h`. In isometric coordinates the
Gram matrix in (13) is

\[
 \mathsf Q_i^T\mathsf Q_i=
 \begin{pmatrix}1/3&a_i^T/\sqrt3\\a_i/\sqrt3&I_3\end{pmatrix}.
\]

Conjugating the first such Gram by `diag(1,O)` gives the second.
That conjugating matrix commutes with `J`; hence the two `\mathsf L_i`
are orthogonally similar and have the same spectrum. Nevertheless
`h^Ta_1^2/3=1/3` and `h^Ta_2^2/3=7/9`. Formula (15) gives
`K_1=68/9` and `K_2=28/3`, a difference of `16/9`.
For any common label other than `1/3`, (12) gives different instantaneous
physical output speeds. Thus retaining the spectrum, the actual current
`h`, and the output does not give a restart-sufficient state. This says
nothing against retaining the full operators in (13) or (16).

### Both squares: row and column balances

For `QQ`, (10) gives `h'=8h\odot q`. With the raw auxiliary matrix
`\mathsf W=\sqrt n B`, each row and column obeys

\[
 \left(n\sum_jB_{ij}^2-2a_i^2\right)'=0,\qquad
 \left(n\sum_iB_{ij}^2-\tfrac12u_j^2\right)'=0.
 \tag{20}
\]

Indeed the row derivative of `n\sum_j B_{ij}^2` is
`4b_i\sum_jB_{ij}h_j=4a_i z_i^2`, which cancels `(2a_i^2)'`.
The column derivative is `4h_j\sum_iB_{ij}b_i=4u_j^2q_j`, which
cancels `(u_j^2/2)'`. Equation (9) preserves these zero derivatives in
physical time. The identities assert no common block-Gram Lax law for `QQ`.

## 6. Differentiated RMS normalization at finite width

Keep exactly the finite metric, data and trained parameters in (8)–(9), but
now normalize the vector after each coordinatewise square. Fix
`\varepsilon>0`, and put

\[
 p=u^2,\quad \alpha=\sqrt{\|p\|_2^2/n+\varepsilon},\quad
 h=p/\alpha,\qquad
 z=Bh,\quad w=z^2,\quad
 \beta=\sqrt{\|w\|_2^2/n+\varepsilon},\quad v=w/\beta,
 \quad f=a^Tv/n.
 \tag{21}
\]

This is a different architecture from applying a scalar activation at each
coordinate: the denominators depend on all neurons. They are differentiated
as part of the network. Every parameter block is trained.

For any vector `x`, let
`N_\varepsilon(x)=x/\sigma`, `\sigma^2=\|x\|_2^2/n+\varepsilon`.
Direct differentiation gives

\[
 d\sigma=\frac{x^Tdx}{n\sigma},\qquad
 DN_\varepsilon(x)[dx]=\sigma^{-1}
       \left(I-\frac{N_\varepsilon(x)N_\varepsilon(x)^T}{n}\right)dx.
 \tag{22}
\]

Write `\Pi_h=I-hh^T/n` and `\Pi_v=I-vv^T/n`. These symmetric
matrices are positive definite, not generally idempotent. For a nonzero
`x`, the parenthesis in (22) is the identity perpendicular to `x`, and
has eigenvalue `1-\|x\|_2^2/(n\sigma^2)=\varepsilon/\sigma^2` on
its span. At `x=0` it is `I`. In particular both denominators in (21)
are at least `\sqrt\varepsilon`.

Define the current backward vectors

\[
 c=\Pi_v a=a-fv,\qquad b=\frac2\beta z\odot c,
 \qquad q=B^Tb,\qquad \widetilde q=\Pi_hq.
 \tag{23}
\]

The full differential is

\[
 df=\frac{v^Tda}{n}+\frac{b^T(dB)h}{n}
                      +\frac{(2u\odot\widetilde q)^Tdu}{n\alpha}.
 \tag{24}
\]

To obtain it, (22) first gives `a^Tdv/n=c^Tdw/(n\beta)` and
`dw=2z\odot dz`; next `dz=(dB)h+Bdh`,
`dh=\Pi_h dp/\alpha`, and `dp=2u\odot du`.
Symmetry of `\Pi_h` transfers it to `q`, giving (24). Therefore

\[
 a'=v,\qquad B'=b h^T/n,\qquad u'=2u\odot\widetilde q/\alpha,
 \tag{25}
\]
\[
 K_1=\frac{4\|u\odot\widetilde q\|_2^2}{n\alpha^2}
     =\frac4\alpha\frac{h^T\widetilde q^2}{n},\quad
 K_2=\frac{\|h\|_2^2\|b\|_2^2}{n^2},\quad
 K_3=\frac{\|v\|_2^2}{n}.
 \tag{26}
\]

The first equality and the squared norm of `B'` use exactly (8).
All terms are nonnegative, and (12) again holds for their sum. In particular
`r(t)=r(0)\exp(-2\int_0^tK(s)\,ds)` on every finite physical interval:
differentiate `r(t)\exp(2\int_0^tK)` to check the identity, including
`r(0)=0`. The residual keeps its sign.

### Feature equations, balances, and the finite reduced state

Let `\rho_h=\|h\|_2^2/n`. Differentiating (21) using (25) gives

\[
 p'=4p\odot\widetilde q/\alpha,\qquad
 \alpha'=4(h^2)^T\widetilde q/n,\qquad
 h'=\frac4\alpha\Pi_h(h\odot\widetilde q),
 \tag{27}
\]
\[
 z'=\rho_h b+B h',\qquad w'=2z\odot z',\qquad
 \beta'=\frac{2(z^3)^Tz'}{n\beta},\qquad
 v'=\frac2\beta\Pi_v(z\odot z').
 \tag{28}
\]

For example `\alpha'=h^Tp'/n=4(h^2)^T\widetilde q/n`, and
`h'=\Pi_h p'/\alpha` gives (27). The rank-one formula for `B'`
gives `B'h=\rho_h b`, which proves the first equation of (28); (22) proves
the remaining ones. One useful exact scalar contraction is

\[
 \frac{h^Tq}{n}=\frac{z^Tb}{n}
   =\frac{2\varepsilon f}{\beta^2},\qquad
 \widetilde q=q-\frac{2\varepsilon f}{\beta^2}h.
 \tag{29}
\]

Indeed `z^Tb/n=(2/\beta)(w^Ta/n-f w^Tv/n)` and
`w=\beta v`, `\|v\|_2^2/n=1-\varepsilon/\beta^2` give (29).
The row and column balance laws now have signed drifts:

\[
 \left(n\sum_jB_{ij}^2-2a_i^2\right)'=-4f v_i^2,
 \qquad
 \left(n\sum_iB_{ij}^2-\tfrac12u_j^2\right)'
       =\frac{4\varepsilon f}{\beta^2}h_j^2.
 \tag{30}
\]

For the row, the first derivative is `2b_i z_i=4v_i(a_i-fv_i)`;
subtract `4a_iv_i`. For the column it is `2h_jq_j`; subtract
`u_ju'_j=2h_j\widetilde q_j`, and then use (29). Multiplication by `-2r` converts
both signed drifts to physical time. The row drift does not generally
vanish when epsilon is set to zero at a state with nonzero denominators.
No epsilon-zero dynamics is part of the theorem.

The output-relevant bottom coordinate can be represented by `h`:

\[
 \rho_h=1-\varepsilon/\alpha^2<1,\qquad
 \alpha(h)=\sqrt{\varepsilon/(1-\rho_h)},\qquad
 \mathcal A_h=\frac4{\alpha(h)}\Pi_h\operatorname{diag}(h)\Pi_h.
 \tag{31}
\]

On a raw-image state `h>=0`; thus `\mathcal A_h` is positive
semidefinite, since
`x^T\mathcal A_h x=(4/\alpha)\sum_jh_j(\Pi_h x)_j^2>=0`.
Equations (27) and (26) become `h'=\mathcal A_hq` and
`K_1=q^T\mathcal A_hq/n`.
With a fixed finite matrix `B_0` and current increment `E=B-B_0`, the
reduced state `(a,h,E)` evolves by

\[
 z=(B_0+E)h,\quad v=N_\varepsilon(z^2),\quad f=a^Tv/n,
 \quad b=\frac2\beta z\odot(a-fv),
 \qquad
 a'=v,\quad E'=b h^T/n,\quad h'=\mathcal A_h(B_0+E)^Tb.
 \tag{32}
\]

This system is autonomous and restartable for states reached from finite
raw initial parameters. Here is the precise justification. Its vector
field is smooth on the open set `\|h\|_2^2/n<1`, because `\alpha(h)`
is smooth there and `\beta>=\sqrt\varepsilon`. A raw solution projects
to (32) by (27). Its reached states have `h>=0` and strict `\rho_h<1`.
The coordinate sign of `u_j` is preserved along any finite raw physical
interval: (25) and (9) have the form `\dot u_j=c_j(t)u_j` with continuous
`c_j`, whence `u_j(t)=u_j(t_0)\exp(\int_{t_0}^t c_j)` by
differentiation. In particular zero coordinates remain zero. At a reached
time, recover a finite raw lift from
`u_j=\operatorname{sign}(u_j(t_0))\sqrt{\alpha(h)h_j}`,
with zero when `h_j=0`, and `B=B_0+E`. The recovered squared vector
indeed has normalizer `\alpha(h)` because
`\alpha(h)^2\rho_h+\varepsilon=\alpha(h)^2`.

Each choice of the nonzero signs gives a raw lift. Any such lift projects
to the same locally unique reduced solution: local uniqueness follows
from the smooth reduced vector field by the integral-equation contraction
on a small closed ball inside `\rho_h<1`. The raw global physical continuation
proved below provides its continuation at every later finite time and
preserves `h>=0,\rho_h<1` there. Consequently the reduced future and its output
do not depend on the recovered signs. This argument concerns reached raw
states; it claims neither a solution on `\rho_h=1` nor global feature-ascent
existence. The source matrix `B_0` still has size `n` and is not a
width-independent Gaussian operator construction.

## 7. Global finite physical flow for these models

For each fixed width and finite initial state, all models above have a
unique physical solution for every `t>=0`. The mixed polynomial losses are
smooth, and the normalized loss is smooth because epsilon is positive.
Thus their physical vector fields are locally Lipschitz. Local existence
and uniqueness follow by contraction for the integral equation on a closed
ball of continuous paths: choose its time length so the field stays in
the ball and its Lipschitz constant times that length is less than one.
No distributional initialization hypothesis enters this argument.

For any solution interval, (8), (9), and `f'=K` give

\[
 \frac{\|\dot u\|_2^2}{n}+\|\dot B\|_F^2+
       \frac{\|\dot a\|_2^2}{n}=4r^2K=-\dot{\mathcal L}.
 \tag{33}
\]

After integration, Cauchy–Schwarz in the metric (8) yields, for `s<t`,

\[
 \left(\frac{\|u(t)-u(s)\|_2^2}{n}
       +\|B(t)-B(s)\|_F^2
       +\frac{\|a(t)-a(s)\|_2^2}{n}\right)^{1/2}
 \le\sqrt{(t-s)(\mathcal L(s)-\mathcal L(t))}
 \le\sqrt{(t-s)\mathcal L(0)}.
 \tag{34}
\]

If a maximal forward solution ended at finite `T`, (34) would make its
parameters Cauchy as `t` increased to `T`. For fixed `n` this metric is
equivalent to the Euclidean metric, so they have a finite limit. Local
existence at that limit extends the solution beyond `T`; local uniqueness
joins the extensions. This contradiction proves the assertion. Equation
(34) controls normalized parameter displacements, not coordinate maxima,
kernel uniform integrability, a population limit, or arbitrary-step GD.
