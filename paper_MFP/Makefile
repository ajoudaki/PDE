.PHONY: pdf check examples

PYTHON ?= python3

pdf:
	latexmk -xelatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
	cp build/main.pdf main.pdf

check:
	PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v

examples:
	PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -B code/scripts/example_mfp_calculus.py
	PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -B code/scripts/example_mfp_mlp_derivative.py
	PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -B code/scripts/example_mfp_kernel_jets.py --activation identity
