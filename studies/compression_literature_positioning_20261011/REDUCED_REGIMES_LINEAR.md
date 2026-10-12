# Deep-linear dynamics: scoped primary-source check

Status: completed source review, 2026-10-11. This is a bounded contribution to the lead review, not an independent review of the manuscript. No manuscript or shared scientific-book edits were made. The review-ai-paper severity rubric and canonical-notation skill, including its neural-network reference, were read and applied.

## Sources and coverage

- Andrew M. Saxe, James L. McClelland, and Surya Ganguli, *Exact solutions to the nonlinear dynamics of learning in deep linear neural networks*, arXiv:1312.6120v3, 19 February 2014. [Version record](https://arxiv.org/abs/1312.6120v3); [PDF](https://arxiv.org/pdf/1312.6120v3). Read all 22 pages, including Appendices A–G. Visually inspected PDF pp. 5–7 and 16, covering the mode equations, learning curves, deeper-network reduction, and a suspect appendix formula.
- Sanjeev Arora, Nadav Cohen, and Elad Hazan, *On the Optimization of Deep Networks: Implicit Acceleration by Overparameterization*, ICML 2018, PMLR 80:244–253. [Publisher record and BibTeX](https://proceedings.mlr.press/v80/arora18a.html); [main PDF](https://proceedings.mlr.press/v80/arora18a/arora18a.pdf); [supplement](https://proceedings.mlr.press/v80/arora18a/arora18a-supp.pdf). Read the complete 10-page main paper and 8-page supplement. Visually inspected main PDF pp. 4 and 7 and supplement pp. 1–2.

Public sources; no confidentiality gate applies. Retrieval succeeded. No source code was supplied in this bounded assignment, and no experiments were reproduced. Files and extracted texts are in `data/generated/compression_literature_positioning_20261011/reduced_regimes_linear/`. Exact PDFs have SHA-256:

```text
saxe2014.pdf       f187bedbefaafad246c040d0384f1ca3da222c1f21e8ca9e264cadf5d64f8a12
arora2018.pdf      0cea8f3f99bf14bad4714a9f2eb1a10f21456690b944be76dd557ddbcd1d47fd
arora2018-supp.pdf 3732d7b3f6a02c9a0be8a953a6a50e736a7f0ea20a13b7df7a1d5d0c8116a873
```

## Achievements and exact boundary

Saxe et al. derive finite-width, nonlinear gradient-flow trajectories in linear networks, including independently evolving task singular modes, sigmoidal learning transitions, and depth-dependent learning times. The exact decoupling uses task-aligned singular vectors and whitened inputs; Appendix E admits input covariance diagonal in the same task basis. Equal layer strengths give a scalar equation per mode; Appendix A considers unequal strengths. General small-random initialization and nonlinear-network agreement are illustrated empirically, not covered by an exact general trajectory theorem. Sections 2–3 and Appendix B analyze favorable initialization and depth-dependent step-size scaling. Their iteration-count conclusions do not establish depth-independent computational cost. Section 4 and Appendix G investigate nonlinear signal propagation, using a Gaussian activity approximation and numerical Jacobian spectra; they do not give a closed nonlinear training model. See §§1.1–1.3, Eqs. (8)–(15), Appendix E, and Fig. 3. [Primary source](https://arxiv.org/pdf/1312.6120v3).

Arora et al. establish an exact autonomous equation for the end-to-end matrix under continuous gradient descent and exact adjacent-Gram balance at initialization. The equation accommodates general differentiable loss, arbitrary depth and compatible rectangular layers, and uniform weight decay. Its state size depends on input/output dimensions rather than hidden widths. This is a substantial exact reduction. Whitened data and task-singular-vector alignment are unnecessary. Equivalence to finite-step factorized gradient descent is approximate; near-zero random initialization is not itself exact balance. The preconditioner can accelerate optimization in selected settings, but is not a universal speedup guarantee. The paper reports comparisons with tuned learning rates and also reports adverse depth effects. Its nonlinear-network experiment factorizes existing layer matrices without changing expressiveness; this does not establish a nonlinear-network closure theorem. See Theorem 1, Eqs. (6)–(10), Claims 1–2, §§7–8, and Appendix A.1. [Main paper](https://proceedings.mlr.press/v80/arora18a/arora18a.pdf).

## Independent checks of the relevant mathematics

Use \(L\) hidden layers and \(D=L+1\) weight matrices. For samples \(x_a\in\mathbb R^d\), targets \(y_a\in\mathbb R^k\), and widths \(n_0=d,n_D=k\), let

\[
h_a^{(0)}=x_a,\qquad h_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
W^{(\ell)}\in\mathbb R^{n_\ell\times n_{\ell-1}},\qquad
M=W^{(D)}\cdots W^{(1)}.
\]

The predictor is \(f_W(x)=Mx\). Despite this linear predictor, both \(W^{(\ell)}(t)\) and hidden features \(h_a^{(\ell)}(t)\) can change nonlinearly with training time. For differentiable sample loss \(\ell\), define \(\mathcal L(M)=m^{-1}\sum_a\ell(Mx_a,y_a)\). With \(\ell(z,y)=\frac12\|z-y\|_2^2\), the residual \(r_a=Mx_a-y_a\) gives \(\nabla_M\mathcal L=m^{-1}\sum_a r_ax_a^\top\).

**Saxe mode check.** The source uses unnormalized sums \(\Sigma^{11}=\sum_a x_ax_a^\top\) and \(\Sigma^{31}=\sum_a y_ax_a^\top\). Assume \(\Sigma^{11}=I\), and let \(s_\alpha\) be a singular value of \(\Sigma^{31}\). Its time constant is \(\tau=1/\lambda\), where its \(\lambda\) denotes learning rate; this is separate from Arora's weight-decay parameter below. Translate its depth as \(D=N_l-1\). On the aligned manifold, let \(a_{\ell,\alpha}\) be the scalar weight for mode \(\alpha\) in layer \(\ell\), and \(u_\alpha=\prod_{\ell=1}^D a_{\ell,\alpha}\). Differentiating the scalar squared residual gives

\[
\tau\dot a_{\ell,\alpha}
=(s_\alpha-u_\alpha)\prod_{j\ne\ell}a_{j,\alpha},\qquad
\frac{d}{dt}(a_{\ell,\alpha}^2-a_{j,\alpha}^2)=0.
\]

For common positive initial layer strength, equality persists, and the product rule yields

\[
\tau\dot u_\alpha=D\,u_\alpha^{2-2/D}(s_\alpha-u_\alpha).
\]

For \(D=2\), differentiation verifies

\[
u_\alpha(t)=\frac{s_\alpha}{1+(s_\alpha/u_\alpha(0)-1)e^{-2s_\alpha t/\tau}}
\]

for \(s_\alpha>0,u_\alpha(0)>0\). This checks the relevant Eq. (12) and Eq. (15) chain directly. Zero initialization is a stationary exceptional case. The source's displayed squared-error convention absorbs the usual factor two into its learning rate; no unit-time equivalence with another loss normalization is being claimed.

**Arora matrix check.** Translate their \(N\) to \(D\), \(W_j\) to \(W^{(j)}\), \(W_e\) to \(M\), and \(L^1\) to \(\mathcal L\), retaining their \(\eta,\lambda\). Under

\[
\dot W^{(\ell)}=-\eta\nabla_{W^{(\ell)}}\mathcal L(M)-\eta\lambda W^{(\ell)},
\]

define the adjacent imbalance

\[
B_\ell=W^{(\ell+1)\top}W^{(\ell+1)}-W^{(\ell)}W^{(\ell)\top}.
\]

The chain rule makes the loss-gradient terms cancel in its derivative, giving \(\dot B_\ell=-2\eta\lambda B_\ell\). Thus exact initial balance \(B_\ell(0)=0\) persists. Compatible singular-value decompositions then identify prefix/suffix Gram products with fractional powers of the two end-to-end Gram matrices. Applying the product rule gives

\[
\dot M=-\eta\lambda D M-\eta\sum_{\ell=1}^D
(MM^\top)^{(D-\ell)/D}
\nabla_M\mathcal L(M)
(M^\top M)^{(\ell-1)/D}.
\]

Zeroth powers are identities, including on null spaces. Reversing the summation index matches main Eq. (8). These steps check Appendix A.1 without requiring invertible or square factors. There are \(kd\) stored evolving entries in \(M\); gradient evaluation still requires the loss/data, and fractional matrix powers still have computational cost. Hidden widths constrain attainable rank and admissible initial states even though they disappear from this vector field. It is therefore appropriate to call this a width-independent end-to-end state reduction, not a universal cost-independent simulator.

## Audit qualifications

- **L1, localized minor source flaw:** Saxe Appendix A, PDF p. 16, Eqs. (23)–(25), has inconsistent factors. Its displayed parametrization gives \(ab=(c_0/2)\sinh\theta\), not \(c_0\sinh\theta\). Substitution in Eq. (8) gives \(\tau\dot\theta=2s-c_0\sinh\theta\). Consequently Eq. (26) cannot be used unchanged with that parametrization. Direct separation repairs the unequal-mode calculation; the checked balanced-mode formulas above are independent and survive. This is a local normalization issue, not evidence against deep-linear reduction.
- **Arora Appendix B coverage limit:** Its special two-coordinate acceleration calculation uses scale separations, approximate updates, and approximate persistence of the large coordinate. It should not be promoted into a general quantitative acceleration theorem or an error-controlled equivalence with finite-step factorized training. The relevant closure theorem has a separate, checked proof. [Supplement](https://proceedings.mlr.press/v80/arora18a/arora18a-supp.pdf).
- The sources' other dependencies, historical optimality claims, and experiments were read but not independently reproduced or exhaustively audited. No paper-level severity verdict is assigned from this scoped check.

## Suggested positioning

Deep-linear networks provide an important class of exact reductions: their predictors remain linear in the input, while factorized weights and hidden representations can evolve through nonlinear training dynamics. Saxe et al. obtain decoupled mode trajectories under aligned initialization and structured input covariance; Arora et al. derive a closed end-to-end matrix flow under exact balance. These results establish substantial compression in their stated regimes. Their assumptions do not by themselves supply an autonomous compressed training model for general deep networks with nonlinear activations and evolving nonlinear features. Avoid saying that deep-linear networks have no feature learning, and avoid treating their exact reductions as merely descriptive approximations.

## Bibliography

The Saxe entry below cites the exact audited version; 2013 is the first-preprint year, while the audited revision is 2014.

```bibtex
@misc{saxe2014exact,
  title = {Exact solutions to the nonlinear dynamics of learning in deep linear neural networks},
  author = {Saxe, Andrew M. and McClelland, James L. and Ganguli, Surya},
  year = {2014},
  eprint = {1312.6120},
  archivePrefix = {arXiv},
  primaryClass = {cs.NE},
  note = {Version 3, 19 February 2014},
  url = {https://arxiv.org/abs/1312.6120v3}
}

@inproceedings{arora2018implicit,
  title = {On the Optimization of Deep Networks: Implicit Acceleration by Overparameterization},
  author = {Arora, Sanjeev and Cohen, Nadav and Hazan, Elad},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning},
  editor = {Dy, Jennifer and Krause, Andreas},
  volume = {80},
  series = {Proceedings of Machine Learning Research},
  pages = {244--253},
  year = {2018},
  publisher = {PMLR},
  url = {https://proceedings.mlr.press/v80/arora18a.html}
}
```
