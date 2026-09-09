# Tame natural gates

This file freezes the nonlinear interface used by the one-action rung of
the calculus. It is deliberately an activation class, not a list of
identities special to arctangent.

## 1. Definition

A scalar activation \(\phi\) is a **tame natural gate** if, with
\(d=\phi'\),

1. \(\phi\in C^2(\mathbb R)\), \(d(x)>0\) for every \(x\), and
   \(\phi,d\) are bounded and globally Lipschitz;
2. the natural coordinate
   \[
     \Theta(x)=\int_0^x\frac{du}{d(u)}
   \]
   is a global increasing \(C^1\) bijection, is pseudo-Lipschitz of some
   finite degree, and \(\Theta(N)\in L^p\) for every finite \(p\) when
   \(N\sim N(0,1)\);
3. writing \(\iota=\Theta^{-1}\),
   \[
     \psi=\phi\circ\iota,\qquad c=d\circ\iota ,
   \]
   the maps \(\psi,c\) are bounded and globally Lipschitz; and
4. all four coordinate maps \(\Theta,\psi,c,d\), and the moment tests
   generated from them by a fixed finite Euler program, are
   pseudo-Lipschitz of finite degree, jointly in every coordinate input and
   every random scalar moment parameter.

The fourth clause is the exact interface to the fixed-program Gaussian
source theorem. It is automatic from the first three clauses whenever
\(\Theta\) is a polynomial, because finite products and finite
compositions of the remaining bounded Lipschitz maps are
pseudo-Lipschitz of finite degree.

The constants attached to a gate are

\[
 M_\phi=\|\phi\|_\infty,\quad M_d=\|d\|_\infty,\quad
 L_\phi,L_d,L_\psi,L_c,
\]

together with a finite pseudo-Lipschitz degree for \(\Theta\). Every
calculus estimate is allowed to depend on these declared constants and on
the compact time horizon, but not on width or an Euler mesh.

## 2. Infinite reciprocal-polynomial subclass

Let \(P\) be a strictly positive real polynomial satisfying

\[
 \int_{\mathbb R}\frac{du}{P(u)}<\infty ,
\]

and define

\[
 d_P(x)=\frac1{P(x)},\qquad
 \phi_P(x)=\int_0^x\frac{du}{P(u)},\qquad
 \Theta_P(x)=\int_0^xP(u)\,du .
\]

Whenever \(d_P'\) is bounded, \(\phi_P\) is a tame natural gate:
\(\Theta_P\) is polynomial, \(\iota_P' = d_P\circ\iota_P\), and

\[
 \psi_P'(r)=d_P(\iota_P(r))^2,\qquad
 c_P'(r)=d_P'(\iota_P(r))d_P(\iota_P(r)),
\]

so \(\psi_P,c_P\) are globally Lipschitz.

In particular, for every integer \(m\in\mathbb N\), \(m\ge1\),

\[
 P_m(x)=1+x^{2m},\qquad
 \phi_m(x)=\int_0^x\frac{du}{1+u^{2m}},\qquad
 \Theta_m(x)=x+\frac{x^{2m+1}}{2m+1}
\]

belongs to the class. The case \(m=1\) is exactly
\(\phi_1=\arctan\), \(\Theta_1(x)=x+x^3/3\).

Thus the natural-coordinate rule is not an arctangent primitive.
Arctangent is merely the lowest-degree member of a nontrivial infinite
class.

## 3. Exclusions are semantic, not aesthetic

The class excludes a gate only when a proof module loses its declared
certificate:

- zeros of \(d\) destroy the global coordinate;
- an unbounded \(\phi\) destroys the bounded pointwise translation of the
  Gaussian readout mark used in cutoff removal;
- a super-polynomial \(\Theta\) falls outside the rigorous fixed-program
  pseudo-Lipschitz theorem used here; and
- failure of the global Lipschitz properties destroys the current
  trace-class/Osgood stability module.

Other backends could enlarge the class. None of these exclusions is claimed
to be a mathematical impossibility theorem for the original network.
