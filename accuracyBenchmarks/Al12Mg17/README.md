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
Discussion on the input parameters and the results:
==================================================
# DFT-FE:

        a) Polynomial Order      = 6
        b) MESH SIZE AROUND ATOM  = 0.9
        c) ATOM BALL RADIUS         = 5.0
        d) SCF Tolerance            =1E-5
        e) Mixing Method            = ANDERSON_WITH_KERKER
        f) No. of degree of freedom = 2352637
        
# QE:  
        a) ecutwfc                  = 50 Ha                                    
        

Study1---Ground-state calculation results
--------------------------------
# GPU v/s CPU Comparison:
    a) Energy Difference = 3.62E-12 Ha/atom
    b) Force Difference = 1.11E-05 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 1.06013E-07 Ha/bohr**3 (Hydrodynamic Stress error)
    d) No. of scf iterations 18(CPU) & 14(GPU)

# Ground State Comparison with QE(100 Ha energy cut off):
    a) Energy Difference = 1.84E-05 Ha/atom
    b) Force Difference = 2.95E-04 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 7.44199E-06 Ha/bohr**3 (Hydrodynamic Stress error)
    
Study2---Combined ionic and cell relaxation results
------------------------
* Relaxed State Comparison with QE(50 Ha and koint rule 4x4x4)and DFT-FE(poly 6 mesh 0.9 and kpoint rule 4x4x4, , scf tolerance 5e-5):  
    a) Energy Difference = 1.06E-05 Ha/atom  
    b) Force Difference = 2.55E-04 Ha/bohr (max absolute error among all atoms and force components)  
    c) Stress Difference = 4.82E-06 Ha/bohr**3 (Hydrodynamic Stress error)  
* Relaxed Vectors:
    *  Quantum Espresso:  
                         19.903699232	0.0000000	0.0000000   
                         0.0000000	19.903699232	0.0000000   
                         0.0000000	0.0000000	19.903699232   
    *  DFT-FE:  
                        1.990369923161319932e+01	0.000000000000000000e+00	0.000000000000000000e+00     
                        0.000000000000000000e+00	1.990369923161319932e+01	0.000000000000000000e+00     
                        0.000000000000000000e+00	0.000000000000000000e+00	1.990369923161319932e+01     
    *  Max Error is 0.0 %                    
                    

