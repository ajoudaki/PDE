# Exact one-hidden-layer identity flow and Stieltjes representation

The model and convention are frozen in `DEPTH1_ORDER13_PROTOCOL.md`.

## 1. Exact finite-width flow

For

\[
 f_{n,1}=\frac1n A^\top u,
 \qquad D_n=n\nabla f_{n,1}\mathbin\cdot\nabla,
\]

feature ascent gives the exact linear system

\[
 \dot A=u,\qquad \dot u=A.
\]

Hence

\[
\begin{aligned}
A(t)&=A_0\cosh t+u_0\sinh t,\\
u(t)&=u_0\cosh t+A_0\sinh t.
\end{aligned}
\]

Writing

\[
c_n=\frac1nA_0^\top u_0,
\qquad q_{A,n}=\frac1n\|A_0\|^2,
\qquad q_{u,n}=\frac1n\|u_0\|^2,
\]

the output is exactly

\[
 f_{n,1}(t)
 =c_n\cosh(2t)+\frac{q_{A,n}+q_{u,n}}2\sinh(2t).
\]

Independent standard-Gaussian initialization gives almost surely

\[
c_n\to0,qquad q_{A,n}\to1,qquad q_{u,n}\to1.
\]

Therefore the width-first feature flow is

\[
\boxed{F_1(t)=\sinh(2t)}.
\]

It follows immediately that

\[
F_1^{(r)}(0)=
\begin{cases}
0,&r\text{ even},\\
2^r,&r\text{ odd}.
\end{cases}
\]

This is an all-order identity for the frozen depth-one model, not merely a
Taylor fit through order thirteen.

## 2. Output-coordinate kernel

Since

\[
F_1^{-1}(y)=\frac12\operatorname{arsinh}(y),
\]

we obtain

\[
\begin{aligned}
K_1(y)
&=F_1'\!\left(F_1^{-1}(y)\right)\\
&=2\cosh\!\left(2F_1^{-1}(y)\right)\\
&=2\sqrt{1+y^2}.
\end{aligned}
\]

Expanding at zero and comparing with

\[
K_1(y)=2+\sum_{r\ge0}(-1)^r\mu_r y^{2r+2}
\]

gives

\[
\mu_r=(-1)^r2{1/2\choose r+1}
=\frac1{4^r(r+1)}{2r\choose r}
=\frac{C_r}{4^r},
\]

where \(C_r\) is the \(r\)-th Catalan number.

## 3. Explicit representing measure

Define the probability measure on \((0,1)\)

\[
\boxed{
d\nu(x)=\frac2\pi\sqrt{\frac{1-x}{x}}\,
\mathbf1_{(0,1)}(x)\,dx.}
\]

Its normalization is

\[
\frac2\pi B\!\left(\frac12,\frac32\right)=1.
\]

For every integer \(r\ge0\),

\[
\begin{aligned}
\int_0^1x^r\,d\nu(x)
&=\frac2\pi B\!\left(r+\frac12,\frac32\right)\\
&=\frac{(2r)!}{4^r r!(r+1)!}\\
&=\frac{C_r}{4^r}=\mu_r.
\end{aligned}
\]

Thus the complete infinite sequence is a Stieltjes moment sequence.

## 4. Strict Hankel positivity at every order

For any nonzero polynomial \(p(x)=\sum_{j=0}^dc_jx^j\),

\[
c^\top H_dc=\int_0^1p(x)^2\,d\nu(x)>0,
\]

and

\[
c^\top H_d^+c=\int_0^1x\,p(x)^2\,d\nu(x)>0.
\]

The inequalities are strict because the density is positive almost
everywhere on an interval and a nonzero polynomial cannot vanish there
almost everywhere.  Hence

\[
\boxed{H_d\succ0,\qquad H_d^+\succ0\quad\text{for every }d\ge0.}
\]

This all-order conclusion is special to the exactly solvable depth-one
identity architecture and does not transfer automatically to greater depth.

