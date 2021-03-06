Description of the example
==========================
This example demonstrates a ground-state calculation with fully periodic boundary conditions on BCC Mo 4x4x4 supercell with a mono-vacancy, containing 127 Mo atoms (1778 electrons) ONCV pseudopotential from sg15 database, PBE exchange correlation, and Fermi-Dirac smearing temperature of 500 K are used.

Studies performed
=======================
* 1) Ground-state calculation using DFT-FE at a FE discretization commensurate with chemical accuracy (~1e-4 Ha/atom in energy, ~1e-4 Ha/Bohr in ionic forces and ~1e-6 Ha/Bohr^3 in cell stresses). The reference ground-state energy, ionic forces, and cell streses are computed using QUANTUM ESPRESSO (QE) at a high plane-wave cutoff of 50 Ha.


Discussion on the input parameters and the results
=================================================
* Since it a homogeneous metallic system, we use Keker preconditioner implemented in DFT-FE, via the ANDERSON\_WITH\_KERKER choice for the MIXING METHOD. We also use a MIXING PARAMETER value of 0.7, which is higher than the default value of 0.2.


Study1---ground-state calculation results
-------
* The run successfully converged in 19 SCF iterations.

* POLYNOMIAL ORDER=7 and MESH SIZE AROUND ATOM=2.0 are found to be sufficient to obtain chemical accuracy as shown below. Total degrees of freedom are 614125 (4835 per atom).

* DFT-FE Energy per atom comparison with QE reference: 8.2e-5 Ha/atom. In particular we compared the "Total energy per atom" printed from DFT-FE output and "(Total energy+TS)/totalNumberAtoms" from QE, since QE's Total energy is the free energy.

* DFT-FE Ionic forces comparison with QE reference: 5.1e-5 Ha/Bohr (max absolute error among all atoms and force components). 

* DFT-FE Cell stress comparison with QE reference: 2.6e-6 Ha/Bohr^3 (max absolute error among all stress components)
