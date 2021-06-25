Description of the example
==========================
This example demonstrates a ground-state calculation with fully periodic boundary conditions and combined ionic-cell relaxation on Al12Mg17 intermetallic. Multiple k-points for sampling the Brillouin zone, norm-conserving pseudopotential, PBE exchange correlation, and Fermi-Dirac smearing temperature of 500 K are used.

Studies to be performed
=======================
* 1) Ground-state calculation: convergence study of ground-state energy and ionic forces to reach chemical accuracy with respect to FE discretization and k-points, and validation against QUANTUM ESPRESSO (QE) for Gamma point and multiple k-point case. Use Kerker preconditioner for SCF convergence.
* 2) Combined ionic and cell relaxation with converged parameters and validation against QE.
* 3) GPU run for Gamma-point case with validation against CPU run


Discussion on the input parameters and the results
==================================================

Study1---Ground-state calculation results
--------------------------------

Study2---Combined ionic and cell relaxation results
------------------------


