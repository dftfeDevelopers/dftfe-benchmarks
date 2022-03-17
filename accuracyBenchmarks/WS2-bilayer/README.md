Description of the example
==========================
This example demonstrates a ground-state calculation and ionic relaxation on a bilayer of WS2 employing non periodic boundary conditions in all 3 directions.
ONCV pseudopotential from PseudoDojo database, PBE exchange correlation and Fermi-Dirac smearing temperature of 500 K are used. Non-periodic boundary conditions along x, Y, Z directions are
employed with a vaccum layer in all directions.

Studies performed
=======================
* Ground-state calculation: Spin-unpolarized calculation with convergence study of ground-state energy and ionic forces with respect to FE discretization to reach chemical accuracy (see examples 1 and 2). Validation with Quantum espresso refined calculation.
* Ground-state calculation: Spin-polarized ground-state calculation using mesh parameters obained in the above study and validate the ground-state energy and forces with Quantum espresso.
* Ionic relaxation with both spin-unpolarized and spin-polarized calculation by constraining the relaxation of atoms normal to the bilayer.


Discussion on the input parameters and the results
===================================================
* DFT-FE:
        a) Polynomial Order      = 7
        b) MESH SIZE AROUND ATOM  = 1.6
        c) ATOM BALL RADIUS         = 6.0
        d) SCF Tolerance            =5E-5
        e) Mixing Method            = Anderson
        f) MIXING PARAMETER          =0.2
        g) ION OPT =true (for ionic forces relaxation)
        h) ION RELAX FLAGS FILE=relaxationFlags.inp (allows relaxation only in Z direction)
        i) FORCE TOL=2e-4 (all ionic force components relaxed to under 2e-4 Ha/Bohr)
        
* QE:  
        a) ecutwfc                  = 50 Ha    

Study1 --- Ground-state calculation results (Spin unpolarized)
-------------------------------------------
* Ground State Comparison with QE:
    a) Energy Difference = 1.4e-5  Ha/atom
    b) Force Difference =  9e-5 Ha/bohr (max absolute error among all atoms and force components)

Study2 --- Ionic relaxation results (Spin unpolarized)
-----------------------------------
* Relaxed State Comparison with QE:  
    a) Energy Difference =  Ha/atom  

Study3 --- Ground-state calculation results (Spin polarized)
-------------------------------------------
* Ground State Comparison with QE(100 Ha energy cut off):
    a) Energy Difference = 2.80E-06 Ha/atom
    b) Force Difference =  9e-5 Ha/bohr (max absolute error among all atoms and force components)

Study4 --- Ionic relaxation results (Spin polarized)
-----------------------------------
* Relaxed State Comparison with QE:  
    a) Energy Difference =  Ha/atom  
