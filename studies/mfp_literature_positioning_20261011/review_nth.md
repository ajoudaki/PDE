# Huang–Yau: neural tangent hierarchy

## Sources and coverage

Root read the entire ICML 2020 paper (10 PDF pages, including references) and the entire arXiv:1909.08156v1 text (39 PDF pages, including Appendices A–C and references), on 2026-10-11. Primary sources:
- https://proceedings.mlr.press/v119/huang20l.html
- https://proceedings.mlr.press/v119/huang20l/huang20l.pdf
- https://arxiv.org/abs/1909.08156 and https://arxiv.org/pdf/1909.08156v1

The arXiv record lists only v1, 18 September 2019. PMLR's 2020 main text revises exposition and distinguishes the maximum regularity order p* from the truncation order p. Its page links provide no supplementary download; trying the conventional `huang20l-supp.pdf` returned 404. Thus the full proof audit concerns the accessible arXiv appendices, not a verified final-conference supplement. Searches for title + supplement/correction/erratum did not locate a correction. This is a bounded search, not a certification of absence.

Downloads: `data/generated/mfp_literature_positioning_20261011/root/nth.pdf` (SHA256 `2aaddce00cf459fab7408b28fbca555b951a5d1521ceabc205c7e05ac254ceeb`) and `nth_arxiv.pdf` (`2036ab63a3e9ff20fa04c3f8d137dae385b9ba743b41a35aed1a92143e5fc91c`). Text extracts have matching stems.

## What is established, what is claimed

This is a direct predecessor for differentiating kernels repeatedly along training. Its finite-network hierarchy is an exact chain-rule construction. The claimed quantitative results go beyond MFP's initial finite jets: Theorems 2.3 and 2.6 estimate high-order kernels over a width-dependent time interval and compare the finite network with a truncated hierarchy. These positive-time estimates are not consequences of MFP.

Use the source's notation here: width m, sample count n, hidden depth H, activation sigma. These correspond to MFP's n, m, L, phi respectively. Equations (1)–(3) of the conference paper use order-one raw Gaussian weights, hidden activations scaled by 1/sqrt(m), output a^T x^(H), and ordinary Euclidean gradient flow of half-mean squared loss. This yields order-one random initial predictions and an NTK regime. It differs from MFP's showcased output w^T h/n and vector mobilities n, which preserve feature motion in the width limit.

The theorem hypotheses are substantive: bounded activation derivatives through order 2p*+1; bounded nonzero input norms; a uniform lower singular-value bound for every distinct input subset of size at most 2p*+1 (Assumptions 2.1–2.2, conference p.4); for Theorem 2.6, an initial full NTK lower eigenvalue bound lambda>0 and even p<=p*. Duplicate/linearly dependent inputs fall outside that data assumption. Constants depend on depth, derivative bounds and data conditioning; increasing p is not a uniform guarantee for one fixed set of constants.

The finite hierarchy does not itself need those probabilistic hypotheses. Define K^(2) as the gradient Gram and recursively K^(r+1)=<grad_theta K^(r),grad_theta f(x_last)>. Then direct substitution of theta_dot=-(1/n) sum_b (f_b-y_b) grad_theta f_b yields K_dot^(r)=-(1/n) sum_b K^(r+1)(...,x_b)(f_b-y_b). The derivatives act on all factors of K^(r). Section 3 and (3.1) in the arXiv text give explicit replacements of weights, activations and activation derivatives. This anticipates the mathematical shape of MFP's initial derivative subclass. It is not just a theorem about the initial NTK.

## Proof reconstruction and findings

The full argument has three layers. Appendix A compiles each hierarchy kernel into products of normalized vector pairings and uses adaptive Gaussian conditioning to identify initialization values. Appendix B bootstraps operator norms and coordinate maxima along training. Appendix C integrates the next hierarchy level and controls a coupled error system using the initial NTK gap. The last comparison is meaningful *conditional on* the preceding a priori estimates; it uses no approximation that freezes the finite network's actual kernel. However the accessible proof contains the following issues. They do not establish that the intended quantitative theorem is false.

### 1. Physical time derivatives are not obtained by differentiating norm inequalities

Location: arXiv Appendix B, equations (B.25)–(B.29), pp.30–31, and the ensuing (B.34), p.32. These display a first derivative as a sum of field expressions times residuals, bound its norm, and then take repeated derivatives of this inequality to infer a bound with one factor m^(-1/2) per derivative. Differentiation does not preserve an inequality; maxima/norms also need not be multiply differentiable. Moreover ordinary higher time derivatives contain derivatives of residuals.

An explicit check within the stated model is H=1, one input of norm one, sigma(z)=z, unit initialization variances and label zero. Put w=W^(1)x, f=a^T w/sqrt(m), and q=(||a||^2+||w||^2)/m. The exact equations give

    a_dot = -f w/sqrt(m),   w_dot = -f a/sqrt(m),   f_dot = -q f,
    a_ddot = q f w/sqrt(m) + f^2 a/m.

The first term in a_ddot is the differentiated residual contribution. It is generally order m^(-1/2) per coordinate, rather than the m^(-1) suggested by iterating only the field replacements. It cannot be dropped when taking physical time derivatives. A time-ordered integral iteration of the *field hierarchy*, keeping residuals as bounded time-dependent coefficients, is a plausible alternative; it is not the printed repeated differentiation argument. This review does not claim that such a repair supplies all stated constants and time intervals.

Consequence: the displayed proof of the coordinate bootstrap is not independently verified, so the quantitative downstream time guarantees are reported as the paper's theorems with this unresolved proof issue. The exact finite hierarchy and its chain-rule interpretation survive. MFP's initial-jet convention explicitly differentiates residuals and the moving direction; it does not thereby prove the missing positive-time estimate.

### 2. The probability convention is stronger than the Gaussian bounds permit

Location: arXiv §1.3 p.5 defines high probability as at least 1-exp(-m^c); Corollary A.5 p.24 claims ||v(0)||_infinity <= C(log m)^C with that probability. D0 includes the Gaussian readout a. For any fixed constants B,C,c>0,

    P(max_i |a_i| > B(log m)^C) >= P(|a_1| > B(log m)^C).

A Gaussian tail lower bound is a constant times exp(-B^2(log m)^(2C)/2)/(1+B(log m)^C). Its logarithm is of polylogarithmic order, so this failure probability is eventually larger than exp(-m^c). Thus the literal probability-strength assertion is false even for an initialization vector. Bounds with arbitrarily high polynomial probability (with constants chosen appropriately) are a natural repair. This does not refute convergence in probability or a polylogarithmic bootstrap on the corresponding weaker event. The convention is retained in conference §1.3 p.3.

### 3. The nondegeneracy proof uses more than its written assumptions

Location: arXiv p.20, (A.6), and Claim A.4 pp.22–24. At (A.6) the proof rules out a nonzero linear combination of activation features solely from a nondegenerate Gaussian input. Constant sigma is permitted by Assumption 2.1 and makes the feature Gram rank one for two independent inputs, contradicting that intermediate full-rank assertion. This is a repairable omitted case, not a counterexample to the final kernel hierarchy. Later, Claim A.4 infers functional linear independence from distinct formal monomials; distinct syntax alone does not exclude identities among sigma and its derivatives. Handling such redundancies requires an additional argument or a singular-conditioning treatment. The adaptive Gaussian projection identity itself is correct and can be proved directly by orthogonal projection of the Gaussian matrix onto the observed linear constraints.

These observations should not be generalized into a claim that all NTH theory fails. Nor should a different MFP proof be sold as a resolution of NTH's quantitative time theorem: the two targets differ.

## Scope, costs and evidence

The truncated solver retains the actual random finite initialization K_0^(r), r<=p, and f_0, not just their limiting expectations. Explicit storage of all sample entries is at least sum_{r=2}^p n^r before exploiting symmetry or structure, and initialization must be computed from the finite network. The paper proves no inexpensive compiler for arbitrary requested observables. Its time-dependent guarantee is nevertheless substantially more ambitious than MFP's finitely many initial coefficients. “Arbitrary precision” is qualified by regularity order, conditioning, fixed-order constants, width and the stated time bounds; it is not a uniform p-to-infinity theorem.

The paper is theoretical; comparisons to observed neural-network advantages refer to other papers. No new experiment was reproduced here, and no empirical feature-learning advantage is credited to this theorem alone. Generalization benefits are motivation/future work rather than a derived consequence of the hierarchy.

## Positioning consequence

Credit NTH for exact recursive derivatives of kernels and the proposed/claimed quantitative truncation theory. MFP's comparison should emphasize its different mean-field normalization, rank-free fixed-data admissibility, and executable expectation of a user-specified finite derivative computation. Neither high-order differentiation nor the idea of organizing derivative contractions into recurrences is a new MFP principle. MFP supplies no competitor to NTH's positive-time approximation estimates. The strongest software distinction is the returned symbolic Gaussian expectation DAG and the explicit two-derivative conventions, not a claim that earlier work lacked kernel derivatives.

Review status: complete reading of both accessible versions; reconstructed relevant arguments. A fresh reviewer independently confirmed all three findings, with a separate derivation and careful limits on their implications; see [independent_proof_checks.md](independent_proof_checks.md). Full correctness of the time theorem is **not** certified. No manuscript changes made.
