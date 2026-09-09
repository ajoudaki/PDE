# Primary-source screening — not proof dependencies

New scope screen after R29: Dandi, Gamarnik, Pernice, Zdeborova,
"Rigorous Asymptotics for First-Order Algorithms Through the Dynamical
Cavity Method", arXiv:2603.14573v1, 15 Mar 2026;
https://arxiv.org/html/2603.14573v1 . Main read the abstract, introduction,
GFOM definition, assumptions A1--A4, Theorems 1.3/2.2/2.7, and Sections
2.1--2.3 (HTML through line 374). The returned excerpt also included
the opening mollification calculation in A.1 through line 424. The full
proof in A.2/A.3 was NOT read, and no theorem or proof estimate is invoked.
The model uses one fixed random matrix with globally Lipschitz coordinate
instructions, a fixed discrete iteration count, and derivative constants
Gamma_(t,m,p) that depend on that count and higher derivative/moment
orders. This does not supply the needed mesh-uniform uncut multiplicative
instruction bound. Our maps (z,q)->phi'(z)q do not satisfy its global
Lipschitz premise. No exact mapping of the two trained matrices or their
vanishing-step limit has been established. This is a scope exclusion for
direct use, not a claim that no adapted cavity argument can work.
The PMLR landing page was also read; its linked PDF fetch failed due to
content type, so the explicit arXiv v1 above is the text actually screened.
A new attempt to open the older recurrent-neural PMC2649202 source was
blocked by its browser check; no new full-text content was read there.

2026-09-06. This file records scope checks only. No external theorem
below has been invoked in any two-sample proof, and no claim of a
complete theorem/proof audit is made.

1. Petit, Poon, Peyre, arXiv:2605.10775v2, 10 Aug 2026,
   "On the global convergence of gradient flow for wide shallow models
   beyond homogeneous nonlinearities":
   https://arxiv.org/html/2605.10775v2
   Main read the displayed introduction and Section 2 through Theorem 1,
   including Assumption 1. The model is a particle average
   R((1/m)sum_i Phi(u_i)), with each u_i in a fixed finite-dimensional
   space, and fixed feature map Phi with linear-growth derivative and
   specified local derivative Lipschitz bound.
   Its Theorem 1 is an all-time sub-Gaussian-initialization well-posedness
   statement for that model. No reduction of our shared trained nested
   matrices to such a fixed particle feature map has been established.
   We therefore did not invoke it or pretend its proof had been audited.

2. Bieniek, Grasser, Uhrig, arXiv:2604.21563, latest abstract v2
   (13 Aug 2026) and displayed v1 introduction/model:
   https://arxiv.org/abs/2604.21563
   https://arxiv.org/html/2604.21563v1
   This is a finite-temperature quantum-spin mean-field approximation
   and numerical benchmark, with imaginary-time correlations; the shown
   model is an isotropic spin-1/2 Heisenberg Hamiltonian.
   It does not supply the deterministic neural-gradient-flow theorem
   sought here. No theorem from it is invoked.

Search also returned the already-known Celentano--Cheng--Montanari and
Nishiyama--Imaizumi directions. Their existence as search results is
not a new reduction or an applicability result. Do not restart an
exhausted applicability calculation without a new exact mapping.

These checks are not an exhaustive literature survey and do not show
that no applicable theorem exists.

A subsequent search for rigorous deterministic spin/mean-field
dynamics returned the already-known first-order-method result and
Ben Arous--Dembo--Guionnet, "Cugliandolo--Kurchan equations for dynamics
of spin-glasses" (author-hosted PDF, search excerpt only):
https://math.nyu.edu/faculty/benarous/Publications/benarous_64.pdf
The displayed abstract concerns Langevin dynamics of spherical p-spin
models. No full text/proof was read or invoked, and no reduction of
the present trained nested deterministic architecture was established.
This search result is not a mathematical dependency.

A later search for global noiseless/random-neural dynamical limits
again returned fixed-Gaussian-data first-order methods and a recurrent
multi-population neural mean-field construction (abstract excerpt):
https://pmc.ncbi.nlm.nih.gov/articles/PMC2649202/
No primary proof was read or invoked from that search. No reduction
of the two trained nested matrix actions was established. The
existing Nishiyama--Imaizumi scope note was reread in full; its fixed
channel/rowwise Lipschitz conditions still have no verified mapping.
This search added no external proof dependency.

New targeted screening after the actual reverse-query evolution rewrite:
searches for multiplicative random-neural/soft-spin dynamics and for
deep-network global limits did not produce a verified reduction. Search
abstracts of recurrent/Lotka--Volterra models are not theorem premises.

Chaintron, Chizat, Maass, arXiv:2603.18168v1,
"ResNets of All Shapes and Sizes: Convergence of Training Dynamics in
the Large-scale Limit":
https://arxiv.org/abs/2603.18168
https://arxiv.org/html/2603.18168v1
Main read the abstract, introduction/model equations, and the opening
of Theorem 1.1 (HTML through the displayed lines 172), NOT its proof.
The architecture is residual with depth-two blocks and jointly growing
depth/hidden-width/embedding dimension, and its claim is for a bounded
number of training steps. The main theorem uses ClippedGD for the
large-depth part; the text says these cuts are unnecessary for its
separate large-embedding-dimension analysis. None of these statements
is a reduction to our fixed-depth, uncut, continuous-training-time
model. No theorem or proof estimate is imported. This scope check is
not a full-paper review and not evidence that the desired theorem is
impossible or absent from all literature.

Later targeted searches for globally controlled multiplicative/soft-spin
responses returned the same first-order fixed-Gaussian-data frameworks;
no new verified architecture reduction was obtained. A new primary
abstract screened was Akmal Xodarev, arXiv:2605.24710:
https://arxiv.org/abs/2605.24710
It explicitly concerns two-layer networks and noisy mean-field dynamics.
Only the abstract was read; no statement/proof audit or mapping to our
three trained hidden layers was performed. It is not a dependency.
The Gerbelot et al. publisher abstract (10.1137/23M1594388) likewise
describes first-order iterative methods, not a checked joint vanishing-
step theorem for this nested architecture. No theorem was invoked.

New screened primary source: Fan, Ko, Loureiro, Lu, Shen,
arXiv:2504.15556v2 (1 Nov 2025),
https://arxiv.org/html/2504.15556v2
Main read the abstract, introduction, model equations (1)--(6), and
Assumptions 2.1--2.3, HTML through line 174. No theorem proof was read
or invoked. The displayed dynamics have a fixed linear disorder action
-beta X^T(X theta-y), a globally Lipschitz coordinate drift with uniformly
bounded first/second derivatives, and a finite-dimensional adaptive
parameter driven by a Lipschitz empirical-law map, plus Brownian noise.
Our two trained nested matrix actions have no demonstrated reduction to
that form. This is a scope screen, not a claim about all adaptations of
their methods or a complete source audit. No dependency was introduced.
