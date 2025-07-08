Description of the example
==========================
This example demonstrates a ground-state calculation bilayer of CrI3 employing semi-periodic boundary conditions (non-periodic along z) and ion+cell relaxation employing periodic boundary conditions in all 3 directions.
ONCV pseudopotential from PseudoDojo database, PBE exchange correlation and Fermi-Dirac smearing temperature of 500 K are used.

Studies performed
=======================
* Ground-state calculation: Spin-polarized calculation with ferromagnetic initial guess convergence study of ground-state energy and ionic forces with respect to FE discretization to reach chemical accuracy (see examples 1 and 2). Validation with Quantum espresso refined calculation.
* Ground-state calculation: Spin-polarized calculation with anti-ferromagnetic (interlayer) initial guess convergence study of ground-state energy and ionic forces with respect to FE discretization to reach chemical accuracy (see examples 1 and 2). Validation with Quantum espresso refined calculation.
* Ionic relaxation with ferromagnetic initial guess by constraining the relaxation of lattice vectors along the xy plane.
* Ionic relaxation with anti-ferromagnetic initial guess by constraining the relaxation of lattice vectors along the xy plane.
* Ground-state calculation: Spin-polarized ground-state calculation with ferromagnetic initial guess with 2x2x1 k-point grid using the relaxed structure from study 3 using fully periodic boundary conditions.
* Ground-state calculation: Spin-polarized ground-state calculation with anti-ferromagnetic initial guess with 2x2x1 k-point grid using the relaxed structure from study 4 using fully periodic boundary conditions.

Discussion on the input parameters and the results
===================================================
* DFT-FE:
        a) Polynomial Order = 5
        b) MESH SIZE AROUND ATOM = 0.85
        c) ATOM BALL RADIUS = 6.0
        d) AUTO ADAPT BASE MESH SIZE = false
        e) BASE MESH SIZE = 12.0
        f) FORCE TOL = 2e-4
        g) STRESS TOL = 1e-6
        
* QE:  
        a) ecutwfc                  = 50 Ha    

Study1 --- Ground-state calculation results (ferromagnetic)
-------------------------------------------
* Ground State Comparison with QE:
    a) Energy Difference = 2.0e-4  Ha/atom
    b) Force Difference =  7.5e-5 Ha/bohr (max absolute error among all atoms and force components)
    c) Net magnetization difference = 1.0e-3 Bohr mag/cell
    d) Absolute magnetization difference = 7.4e-3 Bohr mag/cell

Study1 --- Ground-state calculation results (anti-ferromagnetic)
-------------------------------------------
* Ground State Comparison with QE:
    a) Energy Difference = 2.0e-4  Ha/atom
    b) Force Difference =  7.4e-5 Ha/bohr (max absolute error among all atoms and force components)
    c) Net magnetization difference = 1.8e-6 Bohr mag/cell
    d) Absolute magnetization difference = 6.1e-3 Bohr mag/cell

Study3 --- Geometry optimization results (ferromagnetic)
-----------------------------------
* Optimized geometry Comparison with QE:
    a) Energy Difference = 1.2e-4  Ha/atom
    b) Lattice difference = 0.031 Bohr (max absolute error among all lattice components)
    c) Atomic coordinates difference = 0.06 Bohr (max absolute error among all atom location components)
QE converged in 19 geometry updates and DFT-FE converged in 51 geometry updates

Study4 --- Geometry optimization results (anti-ferromagnetic)
-----------------------------------
* Optimized geometry Comparison with QE:
    a) Energy Difference = 1.2e-4  Ha/atom
    b) Lattice difference = 0.031 Bohr (max absolute error among all lattice components)
    c) Atomic coordinates difference = 0.06 Bohr (max absolute error among all atom location components)
QE converged in 19 geometry updates and DFT-FE converged in 51 geometry updates

Study5 --- Ground-state calculation results (ferromagnetic)
-------------------------------------------
* Ground State runs with 2x2x1 k-point grid with fully periodic boundary conditions

Study6 --- Ground-state calculation results (anti-ferromagnetic)
-----------------------------------
* Ground State runs with 2x2x1 k-point grid with fully periodic boundary conditions
