Description of the example
==========================
This example demonstrates a ground-state calculation with fully non-periodic boundary conditions on Al nanoparticle with 147 atoms. ONCV pseudopotential from Pseudo-dojo database and PBE exchange correlation, and Fermi-Dirac smearing temperature of 500 K are used.

Studies performed
=======================
* Ground-state calculation using DFT-FE at a FE discretization commensurate with chemical accuracy(~1e-4 Ha/atom in energy, ~1e-4 Ha/Bohr in ionic forces). The reference ground-state energy, ionic forces are computed using QUANTUM ESPRESSO (QE) at a high plane-wave cutoff of 50 Ha.

Discussion on the input parameters and the results
==================================================
* Anderson Mixing scheme is used with a Mixing History of 10 and Mixing parameter of 0.1. 

Study1 -- Ground-state calculation results
------------------------------------------
* The run successfully converged in 38 SCF iterations (High Quad PsP on).
* POLYNOMIAL ORDER = 7 and MESH SIZE AROUND ATOM = 2.3 with ATOM BALL RADIUS = 6.0 are found to be sufficient to obtain chemical accuracy as described below. Total degrees of freedom are around 1573887 (10707 DoFs/atom)
* Total Energy = -3.382316942391812518e+02 Ha
* DFT-FE energy difference per atom compared to QE reference: 3.966435931e-05 Ha/atom.
* DFT-FE Ionic forces comparison with QE reference: 6.52232793254028e-05 Ha/Bohr (max absolute error among all atoms and force components)
