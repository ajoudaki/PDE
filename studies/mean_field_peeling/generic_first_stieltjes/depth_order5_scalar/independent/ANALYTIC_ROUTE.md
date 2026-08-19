# Independent analytic contraction: exact closed sectors and exact obstruction

**Superseded route-stage note.**  This file records the first frozen stage of
Route A.  Its then-open \(H^2p\) residual was subsequently closed by the
independently frozen moving-gradient passes in
`FULL_SCALAR_RECURRENCE.md`.  The partial equations below remain valid, but
the statement that the full recurrence is open is superseded by that report.

This note was derived without inspecting Route S.  The two machine-readable
transition tables were frozen before any comparison with an accepted
depth-order-five map:

- `FROZEN_FORWARD_RECURRENCE.json`;
- `FROZEN_REVERSE_RECURRENCE.json`.

Every right-hand side in those tables is a literal sparse polynomial with
exact rational coefficients.  There is no Gaussian, covariance matrix,
response operator, pseudoinverse, or implicit Wick instruction in either
frozen transition.

## 1. Six-family identity and a useful regrouping

Work in whitened parameter coordinates and put

\[
 p=\nabla f,\qquad A=Hp,\qquad B=T[p,p],\qquad c=H^2p,
 \qquad C=U[p,p,p].
\]

The exact finite-width identity is

\[
\begin{aligned}
D^5f={}&2V[p^5]+22U[A,p^3]+14\langle B,B\rangle
 +30\langle B,c\rangle\\
&+36T[A,A,p]+16\langle c,c\rangle .
\end{aligned}
\tag{1.1}
\]

For reference, if (m_2=D^2p=B+c) and (m_3=D^3p), direct differentiation
gives

\[
 \langle A,m_3\rangle
 =U[A,p^3]+3T[A,A,p]+\langle B,c\rangle+\langle c,c\rangle,
\tag{1.2}
\]

and hence the independently checked equivalent form

\[
\boxed{
D^5f=2V[p^5]+10U[A,p^3]
 +10\langle B,m_2\rangle+4\langle m_2,m_2\rangle
 +12\langle A,m_3\rangle .}
\tag{1.3}
\]

The recurrence below closes exactly

\[
V[p^5],\qquad U[A,p^3]=\langle \nabla\widehat f_1,
\nabla\widehat f_3\rangle,
\qquad \langle B,B\rangle=|\nabla\widehat f_2\|^2,
\tag{1.4}
\]

where (widehat f(s)=f(\theta+sp)) uses a frozen direction.  Equations
(1.1)--(1.3) show exactly what is still missing.

## 2. Atom alphabet and deterministic depth data

Throughout,

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},
\qquad G\sim N(0,1),\qquad M_{200000}=1,
\]

and

\[
d=M_{020000},\qquad b_\ell=d^{H-\ell},\qquad
\tau_\ell=\sum_{r=0}^{\ell}d^r.
\tag{2.1}
\]

All formulas use ordinary, not divided, directional derivatives.

## 3. Seven-scalar forward contraction

The seven scalar states are

\[
(u_\ell,v_\ell,w_\ell,x_\ell,y_\ell,j_\ell,k_\ell)
=(G_{02},G_{04},G_{11},G_{13},G_{22},a_3,a_5)_\ell .
\tag{3.1}
\]

The semantic names in (3.1) are used only to derive the recurrence.  The
displayed transition below is its completely contracted definition.

At the first layer,

\[
\begin{aligned}
u_1&=b_1M_{121000},&
v_1&=3b_1^2M_{140010},&
w_1&=b_1M_{040000},\\
x_1&=3b_1^2M_{050100},&
y_1&=3b_1^2M_{042000},&
j_1&=3b_1M_{030100},\\
k_1&=15b_1^2M_{050001}.&&
\end{aligned}
\tag{3.2}
\]

For (2\leq\ell\leq H), abbreviate

\[
L_1=\tau_{\ell-1},\qquad L_3=j_{\ell-1}+3u_{\ell-1},
\qquad L_5=k_{\ell-1}+5v_{\ell-1},\qquad b=b_\ell,
\tag{3.3}
\]

and write (u,v,w,x,y,j,k) for the layer-(ell-1) values.  Complete
Wick--Stein contraction gives

\[
\begin{aligned}
u^+={}&M_{020000}u+M_{101000}(u+w)+M_{121000}bL_1^2,\\
w^+={}&M_{020000}w+M_{040000}bL_1^2,\\
j^+={}&3M_{002000}L_1u+3M_{010100}L_1(u+w)
       +M_{020000}L_3+3M_{030100}bL_1^3,
\end{aligned}
\tag{3.4}
\]

\[
\begin{aligned}
v^+={}&3M_{002000}u^2+6M_{010100}u(u+w)+M_{020000}v\\
&+6M_{030100}bL_1^2u
 +3M_{100010}(u^2+2uw+w^2)+M_{101000}(v+4x+3y)\\
&+12M_{111100}bL_1^2u
 +6M_{120010}bL_1^2(u+w)
 +4M_{121000}bL_1L_3+3M_{140010}b^2L_1^4,
\end{aligned}
\tag{3.5}
\]

\[
\begin{aligned}
x^+={}&3M_{002000}uw+3M_{010100}(uw+w^2)+M_{020000}x\\
&+9M_{022000}bL_1^2u+3M_{030100}bL_1^2(u+2w)
 +M_{040000}bL_1L_3+3M_{050100}b^2L_1^4,
\end{aligned}
\tag{3.6}
\]

\[
\begin{aligned}
y^+={}&2M_{002000}u^2+2M_{002000}uw+3M_{002000}w^2
 +2M_{010100}(u^2+uw)+M_{020000}y\\
&+6M_{022000}bL_1^2(u+w)+2M_{030100}bL_1^2u
 +3M_{042000}b^2L_1^4,
\end{aligned}
\tag{3.7}
\]

and

\[
\begin{aligned}
k^+={}&15M_{000200}L_1u^2
 +30M_{001010}L_1(u^2+uw)+5M_{002000}L_1v+10M_{002000}L_3u\\
&+15M_{010001}L_1(u^2+2uw+w^2)
 +5M_{010100}L_1(v+4x+3y)\\
&+10M_{010100}L_3(u+w)+M_{020000}L_5
 +90M_{021010}bL_1^3u\\
&+30M_{030001}bL_1^3(u+w)+30M_{030100}bL_1^2L_3
 +15M_{050001}b^2L_1^5.
\end{aligned}
\tag{3.8}
\]

Here (u^+=u_\ell,ldots,k^+=k_\ell).  The frozen straight fifth
derivative is therefore

\[
\boxed{S_{5,H}=V[p^5]=k_H+5v_H.}
\tag{3.9}
\]

Equations (3.2)--(3.8) contain only (M)-atoms, deterministic powers of
(d), (	au), and prior scalar states.  Their exact sparse coefficient
table is the forward JSON artifact.

### Lower-order projection

The projection ((w,u,j)) is exactly the accepted order-three state
((V,M,J)): equations (3.2), (3.4), and the (j)-line reproduce Section
7.1 literally after the renaming (w=V,u=M,j=J).  In particular,

\[
T_{3,H}=j_H+3u_H.
\tag{3.10}
\]

## 4. Eight local reverse scalars plus two accumulators

After parity and liveness pruning, the local reverse state is

\[
(e_{02},e_{11},e_{13},e_{22},c_{10},c_{21},c_{30},c_{32}).
\tag{4.1}
\]

Its top initialization is

\[
(e_{02},e_{11},e_{13},e_{22})=(0,0,0,0),\qquad
(c_{10},c_{21},c_{30},c_{32})=(1,0,0,0).
\tag{4.2}
\]

At layer (ell), set (b=b_\ell), use (3.3), and use
((u,v,w,x,y)=(0,0,0,0,0)), (L_3=0) when (ell=1); otherwise use the
stored forward state at (ell-1).  The complete eight-scalar polynomial
transition and the five source contractions

\[
(s_{00},s_{02},s_{11},s_{13},s_{22})
\tag{4.3}
\]

are printed term-by-term in `FROZEN_REVERSE_TRANSITIONS.md` and, in canonical
sparse-map form, under `formatted` in `FROZEN_REVERSE_RECURRENCE.json`.
This is not an instruction to perform a
Gaussian evaluation: each entry there is already the final explicit
polynomial in the declared (M)-atoms and scalar state.  The table has term
counts

\[
\begin{array}{c|rrrrrrrrr}
&e_{02}^+&e_{11}^+&e_{13}^+&e_{22}^+&c_{10}^+&c_{21}^+&c_{30}^+&c_{32}^+\\
\hline
\#&7&5&47&35&5&3&38&3.
\end{array}
\tag{4.4}
\]

There is no live (e_{33}): it enters neither (s_{13}), (s_{22}), nor
any lower response coefficient.  Thus it was removed rather than stored.

Initialize two additional deterministic accumulators by

\[
\Gamma_{13}=x_H,\qquad \Gamma_{22}=y_H.
\tag{4.5}
\]

For (ell=H,H-1,\ldots,2), after computing the sources (4.3), update

\[
\begin{aligned}
\Gamma_{13}&\mathrel{+}=s_{13}+3s_{11}u_{\ell-1}
 +3s_{02}w_{\ell-1}+s_{00}x_{\ell-1},\\
\Gamma_{22}&\mathrel{+}=s_{22}+4s_{11}w_{\ell-1}
 +2s_{02}u_{\ell-1}+s_{00}y_{\ell-1}.
\end{aligned}
\tag{4.6}
\]

At (ell=1), update instead

\[
\Gamma_{13}\mathrel{+}=s_{13},\qquad
\Gamma_{22}\mathrel{+}=s_{22}.
\tag{4.7}
\]

Then the exact meanings of the two terminal scalars are

\[
\boxed{
\Gamma_{13}=U[A,p^3],\qquad
\Gamma_{22}=\langle B,B\rangle .}
\tag{4.8}
\]

The smallest state found by this *partial* route is therefore seven forward
scalars and ten backward scalars (eight local scalars and two accumulators).
No minimality claim is made.

## 5. Exact partial terminal formula

The three closed tensor families contribute

\[
\boxed{C_H^{\rm closed}=2(k_H+5v_H)+22\Gamma_{13}+14\Gamma_{22}.}
\tag{5.1}
\]

This is not (C_H).  The exact residual is

\[
\boxed{
R_H=30\langle B,H^2p\rangle
 +36T[Hp,Hp,p]+16\|H^2p\|^2.}
\tag{5.2}
\]

Thus (C_H=C_H^{\rm closed}+R_H).

## 6. Why the contraction stops here

Let (q=H^2p=H A).  Computing (5.2) layerwise requires the feature tangent
in the *secondary* direction (A).  For a hidden matrix layer its direct
parameter direction is

\[
A_{W^\ell}
=\Delta_1^\ell(X_0^{\ell-1})^T
 +\Delta_0^\ell(X_1^{\ell-1})^T.
\tag{6.1}
\]

Consequently the secondary forward tangent at layer (ell) depends on the
first differentiated reverse carrier (Delta_1^\ell).  That carrier is
only available after the top-down pass (4.1)--(4.3), while propagating the
secondary feature tangent requires a new bottom-up pass.  A final mixed
reverse pass is then needed for (q).  No identity found in this route
expresses all three terms in (5.2) from the seventeen already closed local
states.

This is an exact dependency obstruction for the present witness, not a
no-go theorem for every possible scalar realization.  In particular, it
does not disprove that a different Route S state can absorb the secondary
direction into a single depth transition.

## 7. Audits passed and not passed

The local exact tests in `test_analytic_route.py` prove:

1. the ((w,u,j)) projection agrees coefficient-by-coefficient with the
   accepted order-three recurrence;
2. the ((e_{11},c_{10})) projection agrees coefficient-by-coefficient with
   its accepted order-three reverse recurrence;
3. the regrouped tensor identity (1.3) reproduces the six coefficients
   ((2,22,14,30,36,16));
4. every emitted terminal atom uses derivatives only through
   (phi^{(5)});
5. the (H=1) linear control puts all of its nonzero (C_1=32) in the
   explicitly unresolved mixed sector, as it must.

The mandatory (H=2,3,4) comparisons against the **complete** accepted maps
are not passed by this route because (5.2) has not been contracted.  It would
be misleading to compare (5.1) with those total maps and count the expected
residual as a discrepancy in an allegedly complete witness.

Readout parity is inherited exactly from the frozen line: forward derivative
order (r) has parity ((-1)^r), and the reverse-gradient derivative order
(r) has parity ((-1)^{r+1}).  These parities are what remove all odd-sum
pairings in (3.1) and (4.1).

## 8. Probability boundary

The formulas above are algebraic contractions of the already audited
fixed-depth tensor-program limit.  To identify them with annealed limits it
is sufficient to assume, for each separately fixed (H), that
(phi\in C^\infty), every derivative has polynomial growth, and the
finite NETSOR\({}^T+\) program converges in every finite (L^p).  A weaker
route may instead assume the required convergence in probability together
with

\[
\sup_n\mathbb E|D_n^k f_n|^{1+\epsilon}<\infty,
\qquad k=1,3,5,
\]

for some (epsilon>0).  Neither statement is uniform in growing depth, and
neither supplies the missing algebraic residual (5.2).
