PYTHON ?= python
PYTHONPATH := lab

.PHONY: check records links markup test scaling log-chain multicore anisotropic strain fetch-2607 compile-2607

check: records links markup test

records:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.records

links:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.links

markup:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.math_markup

test:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s lab/tests -v

scaling:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.scaling

log-chain:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.log_chain

multicore:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.multicore

anisotropic:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.anisotropic

strain:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.strain

fetch-2607:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.source_cache 2607.08866 --version v2

compile-2607: fetch-2607
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.paper_build 2607.08866 --version v2 --main chaos_sphere.tex
