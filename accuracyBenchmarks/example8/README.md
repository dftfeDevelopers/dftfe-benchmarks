Description of the example
==========================
This example demonstrates a ground-state calculation and ionic relaxation on a bilayer of WS2 employing non periodic boundary conditions in all 3 directions.
ONCV pseudopotential from PseudoDojo database, PBE exchange correlation and Fermi-Dirac smearing temperature of 500 K are used. Non-periodic boundary conditions along x, Y, Z directions are
employed with a vaccum layer in all directions.

Studies to be performed
=======================
* Ground-state calculation: Spin-unpolarized calculation with convergence study of ground-state energy and ionic forces with respect to FE discretization to reach chemical accuracy. Validation with Quantum espresso refined calculation.
* Ground-state calculation: Spin-polarized ground-state calculation using mesh parameters obained in the above study and validate the ground-state energy and forces with Quantum espresso.
* Ionic relaxation with both spin-unpolarized and spin-polarized calculation by constraining the relaxation of atoms normal to the bilayer.


Discussion on the input parameters and the results
===================================================

Study1 --- Ground-state calculation results
-------------------------------------------

Study2 --- Ionic relaxation results
-----------------------------------
