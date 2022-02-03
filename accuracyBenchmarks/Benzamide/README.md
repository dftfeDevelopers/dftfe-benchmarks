Description of the example
==========================
This example demonstrates an all-electron ground-state calculation with non-periodic boundary conditions and ionic relaxation on Benzamide. PBE exchange correlation and Fermi-Dirac smearing temperatrure of 500 K are used.

Studies to be performed
=======================
* 1) Spin unpolarized ground-state calculation: convergence study of ground-state energy and ionic forces to reach chemical accuracy (defined in the common README) with respect to discretization, and validation against NWChem. 


Discussion on the input parameters and the results
==================================================


DFT-FE
==================================================
    a) Polynomial Order      = 5
    b) MESH SIZE AROUND ATOM  = 0.4
    c) SCF Tolerance            = 1e-5
    d) Mixing Method            = Anderson
    e) Anderson MIXING PARAMETER  = 0.2 (default)

NWChem
==================================================
    a) Basis = pc-3
    b) SCF Tolerance            = 1e-6
    c) Quadrture grid  = medium (default) 

Study1---Ground-state calculation results
--------------------------------
1. In DFT-FE, to obtain convergence with respect to discretization (i.e. a mesh commensurate with a chemical accuracy of ~1e-4 Ha/atom in energy and ~1e-4 Ha/Bohr in ionic forces), ground state calculations are performed using mesh size around atoms to be {0.4, 0.3, 0.2} (in a.u.). We attain the convergence in both energy and forces at 0.4 a.u. Total DoFs=1480251.

2. In NWChem, to obtain convergence with respect to discretization (i.e. a basis with a chemical accuracy of ~1meV/atom), ground state calculations are performed using pc-2, pc-3, and pc-4 basis. We attain the convergence at pc-3 basis.

3. At convergence, the DFT-FE energy is -25.040833498463442 Ha/atom, and the NWChem energy is -25.040754748382188 Ha/atom. Thus, the difference in groundstate energy between DFT-FE and NWChem is 7.9e-05 Ha/atom. 
