Description of the example
==========================
This example demonstrates a ground-state calculation with fully non-periodic boundary conditions on Al nanoparticle with 147 atoms. ONCV pseudopotential from Pseudo-dojo database and PBE exchange correlation, and Fermi-Dirac smearing temperature of 500 K are used.

Studies performed
=======================
* Ground-state calculation using DFT-FE at a FE discretization commensurate with chemical accuracy(~1e-4 Ha/atom in energy, ~1e-4 Ha/Bohr in ionic forces). The referenace ground-state energy, ionic forces are computed using QUANTUM ESPRESSO (QE) at a high plane-wave cutoff of 50 Ha.


Discussion on the input parameters and the results
==================================================
* Anderson Mixing scheme is used with a Mixing History of 10 and Mixing parameter of 0.1. 

Study1 -- Ground-state calculation results
------------------------------------------
* The run successfully converged in 49 SCF iterations.
* POLYNOMIAL ORDER = 7 and MESH SIZE AROUND ATOM = 2.3 with ATOM BALL RADIUS = 4.0 are found to be sufficient to obtain chemical accuracy as described below. Total degrees of freedom are around 4308881 (29312 DoFs/atom)
* Total Energy = -3.382366051125088120e+02 (Hartree) (previous benchmark: -3.382371304913907011e+02)
* DFT-FE energy per atom comparison with QE reference: 6.25e-06 Ha/atom.
* DFT-FE Ionic forces comparison with QE reference: 1.5e-03 Ha/Bohr (max absolute error among all atoms and force components)

Study1 -- Ground-state calculation results (using domain vectors 60x60x60)
------------------------------------------
* The run successfully converged in 48 SCF iterations.
* POLYNOMIAL ORDER = 7 and MESH SIZE AROUND ATOM = 2.3 with ATOM BALL RADIUS = 4.0 are found to be sufficient to obtain chemical accuracy as described below. Total degrees of freedom are around 1348535 (9173 DoFs/atom)
* Total Energy = -3.382496753162126879e+02 (Hartree) (previous benchmark: -3.382371304913907011e+02)
* DFT-FE energy per atom comparison with QE reference: 8.26e-05 Ha/atom.
* DFT-FE Ionic forces comparison with QE reference: 1.0e-03 Ha/Bohr (max absolute error among all atoms and force components)

Study1 -- Ground-state calculation results for previous benchmarks
------------------------------------------
* The run successfully converged in 39 SCF iterations.
* POLYNOMIAL ORDER = 7 and MESH SIZE AROUND ATOM = 2.3 with ATOM BALL RADIUS = 4.0 are found to be sufficient to obtain chemical accuracy as described below.
* Total degrees of freedom are around 1339596 (9112 DoFs/atom)
* DFT-FE energy per atom comparison with QE reference: 3e-06 Ha/atom. In particular we compared the "Total energy per atom" printed from DFT-FE output and "(Total energy+TS)/totalNumberAtoms" from QE, since QE's Total energy is the free energy.
* DFT-FE Ionic forces comparison with QE reference: 1.4e-04 Ha/Bohr (max absolute error among all atoms and force components) (recheck this)
