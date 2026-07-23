PYTHON ?= python
PYTHONPATH := lab

.PHONY: check records links markup test scaling log-chain multicore anisotropic covering-entropy perimeter-packing packet-lifetime mixed-lorentz vanishing-tail critical-localization truncated-direction ancient-compactness commutator-bubbles commutator-dust natural-frequency same-solution-granularity projective-alignment vacuum-orientation polar-tensor polar-entropy tensor-adjoint adjoint-kato strain fetch-2607 compile-2607

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

covering-entropy:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.covering_entropy

perimeter-packing:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.perimeter_packing

packet-lifetime:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.packet_lifetime

mixed-lorentz:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.mixed_lorentz

vanishing-tail:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.vanishing_tail

critical-localization:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.critical_localization

truncated-direction:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.truncated_direction

ancient-compactness:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.ancient_compactness

commutator-bubbles:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.commutator_bubbles

commutator-dust:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.commutator_dust

natural-frequency:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.natural_frequency

same-solution-granularity:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.same_solution_granularity

projective-alignment:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.alignment_defect

vacuum-orientation:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.vacuum_orientation

polar-tensor:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.polar_tensor_evolution

polar-entropy:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.polar_entropy_barrier

tensor-adjoint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.tensor_adjoint_closure

adjoint-kato:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.adjoint_kato

strain:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.strain

fetch-2607:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.source_cache 2607.08866 --version v2

compile-2607: fetch-2607
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.paper_build 2607.08866 --version v2 --main chaos_sphere.tex
