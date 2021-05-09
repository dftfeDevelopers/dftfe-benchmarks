Description of the example
==========================
This example demonstrates a ground-state calculation with fully periodic boundary conditions on BCC Mo supercell with a mono-vacancy. ONCV pseudopotential from sg15 database, GGA exchange correlation, and Fermi-Dirac smearing temperature of 500 K are used.

Studies to be performed
=======================
* Compute the reference ground-state energy and forces using QUANTUM ESPRESSO (QE) at a high plane-wave cutoff of 50 Ha.
* Ground-state calculation using DFT-FE at a FE discretization commensurate with chemical accuracy (~1e-4 Ha/atom in energy and ~1e-4 Ha/Bohr in forces)


Discussion on the input parameters and the results
=================================================
* Please refer to full input parameters list and their associated description in the manual of DFT-FE. Below, we will go over the key input parameters and comments pertaining to such fully periodic metallic systems.

Results
-------
* DFT-FE Energy per atom comparison with QE reference: 1.7e-4 Ha/atom
* DFT-FE Ionic forces comparison with QE reference: 2.5e-4 Ha/Bohr (max absolute error among all atoms and force components)
