Description of the example
==========================
This example demonstrates an all-electron ground-state calculation with non-periodic boundary conditions and ionic relaxation on Benzamide. PBE exchange correlation and Fermi-Dirac smearing temperatrure of 500 K are used.

Studies to be performed
=======================
* 1) Ground-state calculation: convergence study of ground-state energy to reach chemical accuracy (see examples 1 and 2) with respect to discretization, and validation against NWChem. 


Discussion on the input parameters and the results
==================================================


DFT-FE
==================================================
    a) Spin unpolarized 
    b) Polynomial Order      = 5
    c) MESH SIZE AROUND ATOM  = 0.3
    d) SCF Tolerance            = 1e-5
    e) Mixing Method            = Anderson
    f) Anderson MIXING PARAMETER  = 0.2 (default)
    g) No. of degree of freedom = 2047163

NWChem
==================================================
    a) Spin unpolarized 
    b) Basis = pc-3
    c) SCF Tolerance            = 1e-6
    d) Quadrture grid  = medium (default) 

Study1---Ground-state calculation results
--------------------------------
1. In DFT-FE, to obtain convergence with respect to discretization (i.e. a mesh commensurate with a chemical accuracy of ~1e-4 Ha/atom in energy), ground state calculations are performed using mesh size around atoms to be {0.3, 0.2} (in a.u.). We attain the convergence at 0.3 a.u.

2. In NWChem, to obtain convergence with respect to discretization (i.e. a basis with a chemical accuracy of ~1meV/atom), ground state calculations are performed using pc-2, pc-3, and pc-4 basis. We attain the convergence at pc-3 basis.

3. It takes 19 and 21 SCF iterations in DFT-FE and NWChem, respectively, to reach convergence in density.

4. At convergence, the DFT-FE energy is -25.040821238250167 Ha/atom, and the NWChem energy is -25.040754748382188 Ha/atom. Thus, the difference in groundstate energy between DFT-FE and NWChem is -6.6e-05 Ha/atom. 
