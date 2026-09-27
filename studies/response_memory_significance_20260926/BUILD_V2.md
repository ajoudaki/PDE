# V2 build instructions

Run from this directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error CANDIDATE_V2.tex

The self-contained source inputs are:

- `CANDIDATE_V2.tex`
- `REFERENCES_V2.bib`
- `V2_figures/circle_shallow.pdf`
- `V2_figures/circle_deep.pdf`
- `V2_figures/mnist_scatter.pdf`
- `V2_figures/mnist_rms.pdf`

The verified build used latexmk 4.76, pdfTeX
3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian), and BibTeX 0.99d.
It produced `CANDIDATE_V2.pdf` with resolved citations and cross-references.
