Description of the example
--------------------------
This example demonstrates an all-electron ground-state calculation with fully periodic boundary conditions and cell relaxation on GaAs cubic diamond unit cell. Multiple k-points for sampling the Brillouin zone, GGA exchange correlation, and spin-unpolarized calculation, Fermi-Dirac smearing temperature of 500 K are used.

Studies to be performed
------------------------
* Ground-state calculation for both Gamma-point and multiple k-point. Convergence study of ground-state energy and cell stresses with respect to discretization and k-points, and validation against ELK (widely used LAPW+lo code). 

* Volumetric cell relaxation and validation against ELK.


Discussion on the input parameters and the results
-------------------------------------------
Point group symmetrization when using multiple k-points cannot be used in DFT-FE since ionic forces and cell stresses are not implemented in this case. However, time reversal symmetry can be used as used in this example.

