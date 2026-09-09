# Primary continuous-time DMFT applicability audit

Status: none of the three routes below supplies the missing all-finite-time
population theorem for the prescribed three-hidden-layer arctangent network.
This is an applicability result about the inspected theorems, not a
nonexistence result or an exhaustive claim about the literature.

The audit keeps both independent Gaussian initialization matrices and their
reused transposes, all trained blocks, zero limiting readout, and continuous
time. A fixed-step theorem or a theorem after clipping does not settle this
obligation.

## 1. Deterministic high-dimensional first-order DMFT

Celentano, Cheng and Montanari, *The high-dimensional asymptotics of first
order methods with random data*, equation (12), Assumption 1, and Theorems
1--2, prove global DMFT well-posedness and finite-horizon empirical-path
convergence for
\[
 \dot\Theta=-\Theta\Lambda(t)^\top
             -\delta^{-1}X^\top\ell_t(X\Theta;z),
 \qquad \Theta\in\mathbb R^{d\times k},
\]
with fixed internal dimension \(k\), one iid sub-Gaussian matrix \(X\),
initial data independent of \(X\), and a rowwise map \(\ell\).
Assumption 1(b), equations (19a)--(19b), requires \(\ell\) and its Jacobian
to be globally Lipschitz in the dynamic arguments, uniformly over the
external argument \(z\). The bounded symmetric \(\Lambda(t)\) is prescribed.
[Primary source, version 3](https://arxiv.org/html/2112.07572v3).

The arctangent backward gate, viewed as a row map in its current variables,
is
\[
 G(z,q)=\frac{q}{1+z^2},
 \qquad \partial_zG(1,q)=-\frac q2.
\]
It has linear growth and is locally Lipschitz, but fails precisely the
global Lipschitz hypothesis above. Boundedness of the activation and of the
current readout does not bound this middle \(q\).

There is also an unverified architecture reduction: stacking the two
independent forward matrices and their transposes produces a structured
block matrix, not the iid \(X\) in the theorem. Retaining the learned
matrix rows as neuron state makes the internal dimension grow with width;
eliminating them introduces the full causal training history. Neither is
the displayed finite-dimensional rowwise flow. These observations do not
prove that every alternative encoding is impossible; they identify the
missing reduction.

The newer stochastic extension by Nishiyama and Imaizumi does not weaken
this decisive regularity requirement: its Assumption 2 imposes global
Lipschitz conditions on \(\ell\), its Jacobian, and its Hessian. The additional
polynomial-growth clause does not replace those conditions. Its Theorem 1
gives global existence for zero diffusion or affine \(\ell\), and only a
local theorem for its general stochastic model.
[Primary source, Assumption 2 and Theorem 1](https://arxiv.org/html/2602.06320v1).

## 2. Gaussian multi-population recurrent-network fixed points

Faugeras, Touboul and Cessac, *A constructive mean-field analysis of multi
population neural networks with random synaptic weights and stochastic
inputs*, treat bounded sigmoidal firing maps and finite-dimensional linear
synaptic filters. Theorem 4 constructs a unique Gaussian-process fixed
point on any finite interval. Assumption 1(b) requires the noise matrix to
have every singular value bounded below by a strictly positive constant;
Theorem 4 also assumes a nondegenerate Gaussian initial state. The
microscopic synaptic variables are independent directed weights.
[Primary source, Assumption 1 and Theorem 4](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/neuro.10.001.2009/full).

The exact network has no dynamical Brownian noise. Its zero readout is a
degenerate state component, its reused transpose couples opposite
directions, and its weights are learned. The effective canonical process
also contains response-memory terms rather than being the Gaussian
voltage process obtained from a deterministic linear filter driven by
Gaussian inputs. Each of these distinctions must be handled before
Theorem 4 can be invoked. In particular, a bounded random state-dependent
operator cannot be substituted for its prescribed linear filter while
retaining the theorem unchanged.

Adding nondegenerate noise and later taking a zero-noise limit would be a
new approximation theorem requiring uniform estimates. It is not covered
by this result and would not bypass the current stability obligation.

## 3. Polynomial Gaussian spin-glass dynamics

Ben Arous, Dembo and Guionnet, *Cugliandolo--Kurchan equations for dynamics
of Spin-Glasses*, genuinely allow polynomial random interactions and prove
an all-finite-horizon limit. Their equations (1.2), (1.6), and (1.7) specify
a finite-degree Gaussian polynomial Hamiltonian with permutation-symmetric
independent Gaussian tensor coefficients, radial confining drift, and
additive Brownian noise. Theorem 1.2 establishes convergence and uniqueness
of the correlation/response equations on every fixed \([0,T]\), under the
stated confinement and concentration hypotheses.
[Primary source, pages 3--5](https://perso.ens-lyon.fr/aguionne/skp070904.pdf).

This is not a theorem for arbitrary locally Lipschitz Gaussian-matrix
systems with polynomial growth. After writing the trained matrices as
initial Gaussian matrices plus learned corrections, the network's
Hamiltonian is a nonlinear, generally non-Gaussian function of those
initial matrices. For example, at a fixed state with fixed nonzero readout,
its output is bounded by
\[
 |f|\le \frac{\pi}{2}\,\mathbb E|W^{(4)}|.
\]
For configurations where it depends nontrivially on the Gaussian matrices,
this bounded random variable cannot be a nondegenerate Gaussian
Hamiltonian value. Conversely, regarding every weight as a state variable
makes the objective deterministic with Gaussian initial data, not a
Gaussian polynomial random Hamiltonian of the specified type.

The deterministic zero-noise network also lacks the radial confining
drift used by that theorem. Its action bound is a different estimate, not
the paper's Hamiltonian covariance or confinement assumption. Finally,
the quoted theorem identifies correlation and integrated response;
it is not an automatic full empirical-neuron-law identification result
for an arbitrary replacement architecture.

## Why the bounded linear middle-field equation does not repair these maps

This paragraph is a direct calculation for the exact network, not a claim
borrowed from the sources. Work in feature time with normalized Euclidean
inner products, or the corresponding probability-space notation. Set
\[
 D_\ell=\operatorname{diag}\phi'(z^{(\ell)}),\quad
 m_\ell=\mathbb E|h^{(\ell)}|^2,\quad
 A_2=m_1 I+W^{(2)}D_1^2(W^{(2)})^*,
 \qquad \phi(z)=\arctan z.
\]
For \(q^{(2)}=(W^{(3)})^*\delta^{(3)}\), differentiating all trained factors
gives the exact equation
\[
 \dot q^{(2)}=\mathcal B_\theta+\mathcal L_\theta q^{(2)},
\]
where
\[
\begin{split}
 \mathcal L_\theta
 &=(W^{(3)})^*
   \operatorname{diag}(W^{(4)}\phi''(z^{(3)}))
   W^{(3)}D_2 A_2D_2,\\
 \mathcal B_\theta
 &=h^{(2)}\mathbb E|\delta^{(3)}|^2\\
 &\quad +(W^{(3)})^*
 \left[D_3h^{(3)}
 +\operatorname{diag}(W^{(4)}\phi''(z^{(3)}))
       m_2\delta^{(3)}\right].
\end{split}
\]
Indeed, \((W^{(3)})'= \delta^{(3)}\otimes h^{(2)}\),
\((W^{(4)})'=h^{(3)}\), and
\((z^{(3)})'=m_2\delta^{(3)}+W^{(3)}D_2A_2D_2q^{(2)}\).
For \(a=\pi/2\), \(s\le S\), zero initial readout, and
\(\|W^{(\ell)}\|_{\rm op}\le M_\ell\), this implies
\[
 \|\mathcal L_\theta\|_{\rm op}
 \le 2aS\,M_3^2(a^2+M_2^2),
 \qquad
 \|\mathcal B_\theta\|_2
 \le a^3S^2+M_3(a+2a^4S^2).
\]
Thus fixing the full coefficient path does give an ordinary bounded
linear equation in \(q^{(2)}\). It does not give the coupled DMFT
well-posedness or matrix-to-population convergence theorem.

In particular, comparing two coupled coefficient paths yields
\[
 (\Delta q^{(2)})'
 =\mathcal L_\theta\Delta q^{(2)}
  +(\mathcal L_\theta-\mathcal L_{\widetilde\theta})
       \widetilde q^{(2)}
  +\mathcal B_\theta-\mathcal B_{\widetilde\theta}.
\]
The second term is not controlled by the individual operator-norm bounds.
Its rightmost gate difference contains
\[
 (D_2-\widetilde D_2)\widetilde q^{(2)}.
\]
No smallness in normalized \(L^2\) follows from a small \(L^2\)
preactivation difference using only these bounds. This is the exact
state-dependent coefficient issue, not a claim that the actual Gaussian
orbit exhibits instability.

Moreover, \(\mathcal L_\theta\) is not an independent Gaussian random
matrix: it contains reused matrices, their adjoints, adapted diagonal
gates, and trained corrections. Even a fixed-gate product \(W^*MW\) is
generally not Gaussian. None of the three theorems says that an arbitrary
adapted bounded-operator replacement preserves its Gaussian response
description.

Conclusion: the bounded middle-field generator remains potentially
useful input to a new architecture-specific argument. These inspected
primary results do not turn that input into the missing global
continuation theorem. A justified extension must control the coupled
state dependence or causal response kernels, not only the frozen
generator norm.
