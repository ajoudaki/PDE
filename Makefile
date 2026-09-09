PYTHON ?= python

.PHONY: check test
check:
	$(PYTHON) -B code/tools/check_library.py
	$(MAKE) test

test:
	PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 $(PYTHON) -B -m unittest discover -s code/tests -p 'test_*.py' -v
