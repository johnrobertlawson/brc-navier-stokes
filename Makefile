PYTHON ?= python
PYTHONPATH := lab

.PHONY: check records links markup test scaling log-chain multicore anisotropic covering-entropy perimeter-packing packet-lifetime mixed-lorentz vanishing-tail critical-localization truncated-direction ancient-compactness commutator-bubbles commutator-dust natural-frequency same-solution-granularity projective-alignment vacuum-orientation polar-tensor polar-entropy tensor-adjoint adjoint-kato shear-adjoint trace-adjoint trace-band-flux trace-boundary-flux trace-projective projective-interface trace-excess trace-temporal alignment-excess carrier-microbubble microbubble-decoration strain-jet forcing-jet moving-band tree-budget band-increment fresh-detector frequency-energy scale-defect two-scale-sync fixed-shell-clock strain fetch-2607 compile-2607

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

shear-adjoint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.shear_adjoint

trace-adjoint:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_adjoint

trace-band-flux:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_band_flux

trace-boundary-flux:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_boundary_flux

trace-projective:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_projective_domination

projective-interface:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.projective_zero_interface

trace-excess:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_trace_excess

trace-temporal:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.trace_temporal_modulus

alignment-excess:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_alignment_excess

carrier-microbubble:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.terminal_carrier_microbubble

microbubble-decoration:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.microbubble_decoration

strain-jet:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.strain_jet_freezing

forcing-jet:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.forcing_jet_decoupling

moving-band:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.moving_band_coupling

tree-budget:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.tree_budget

band-increment:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.band_increment

fresh-detector:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.fresh_detector

frequency-energy:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.frequency_energy

scale-defect:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.scale_defect

two-scale-sync:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.two_scale_synchronization

fixed-shell-clock:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.fixed_shell_clock

strain:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.strain

fetch-2607:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.source_cache 2607.08866 --version v2

compile-2607: fetch-2607
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m navier_lab.paper_build 2607.08866 --version v2 --main chaos_sphere.tex
