Description of the example
==========================
This example demonstrates a ground-state calculation with fully periodic boundary conditions and combined ionic-cell relaxation on Al12Mg17 intermetallic. Multiple k-points for sampling the Brillouin zone, norm-conserving pseudopotential, PBE exchange correlation, and Fermi-Dirac smearing temperature of 500 K are used.

Studies to be performed
=======================
* 1) Ground-state calculation: convergence study of ground-state energy and ionic forces to reach chemical accuracy (see examples 1 and 2) with respect to FE discretization and k-points, and validation against QUANTUM ESPRESSO (QE) for Gamma point and multiple k-point case. Use Kerker preconditioner for SCF convergence.
* 2) Combined ionic and cell relaxation with converged parameters and validation against QE.
* 3) GPU run for Gamma-point case with validation against CPU run


Discussion on the input parameters and the results
==================================================
1) DFT-FE:
        a) Polynomial Order      = 6
        b) MESH SIZE AROUND ATOM  = 0.9
        c) ATOM BALL RADIUS         = 5
        d) SCF Tolerance            =1E-5
        e) Mixing Method            = ANDERSON_WITH_KERKER, mixing parameter 0.2
        f) No. of degree of freedom = 2352637
        h) No. of KS Wavefunctions = 245
        
2)QE:  

        b) ecutwfc                  = 200 Ry
Study1---Ground-state calculation results
--------------------------------
1) GPU CPU Comparison:
    a) Energy Difference = 1.62E-8 Ha/atom
    b) Force Difference = 1.6E-7 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 1.31E-7 Ha/bohr**3 (Hydrodynamic Stress error)
    d) No. of scf iterations 25(CPU) & 25(GPU)

2) Ground State Comparison with QE(200 Ry energy cut off):
    a) Energy Difference = 2.80E-06 Ha/atom
    b) Force Difference = 6.79E-05 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 2.62E-06 Ha/bohr**3 (Hydrodynamic Stress error)
    d) No. of scf iterations 25(DFT-FE) & 13(QE)
Study2---Combined ionic and cell relaxation results
------------------------
1) Relaxed State Comparison with QE(85 Ry):
    a) Energy Difference = 1.06E-05 Ha/atom
    b) Force Difference = 2.55E-04 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 4.82E-06 Ha/bohr**3 (Hydrodynamic Stress error)
2) Relaxed Co-ordinates:
    a) Quantum Espresso:
                        24.9176176	0.0000000	0.0000000
                        0.0000000	24.9191797	0.0000000
                        0.0000000	0.0000000	23.8884463
    b) DFT-FE:
                        24.9150902	0.0000000	0.0000000
                        0.0000000	24.9151757	0.0000000
                        0.0000000	0.0000000	23.8931448
    c) Max Error is 0.01966 %                     
                    

