Description of the example
==========================
This example demonstrates a ground-state calculation with fully periodic boundary conditions and combined ionic-cell relaxation on Al12Mg17 intermetallic. Multiple k-points for sampling the Brillouin zone, norm-conserving pseudopotential, PBE exchange correlation, and Fermi-Dirac smearing temperature of 500 K are used.

Studies performed
=======================
 1) Ground-state calculation: convergence study of ground-state energy and ionic forces to reach chemical accuracy (see examples 1 and 2) with respect to FE discretization and k-points, and validation against QUANTUM ESPRESSO (QE) for Gamma point and multiple k-point case. Use Kerker preconditioner for SCF convergence.
 2) Combined ionic and cell relaxation with converged parameters and validation against QE.
 3) GPU run for Gamma-point case with validation against CPU run


Discussion on the input parameters and the results
==================================================
* DFT-FE:

        a) Polynomial Order         = 6
        b) MESH SIZE AROUND ATOM    = 0.9
        c) ATOM BALL RADIUS         = 5.0
        d) SCF Tolerance            =1E-5
        e) Mixing Method            = ANDERSON_WITH_KERKER
        f) No. of degree of freedom = 2352637
        g) NPKPT for new benchmarks = 8
* QE:  
        a) ecutwfc                  = 50 Ha                                    
        


Study1---Ground-state calculation results
--------------------------------
* GPU v/s CPU Comparison: a) Energy Difference = 1.578E-9 Ha/atom b) Force Difference = 4.154E-05 Ha/bohr (max absolute error among all atoms and force components) c) Stress Difference = 1.1699E-07 Ha/bohr**3 (max abs error in stress any component) d) No. of scf iterations 12(CPU) & 11(GPU)

* Ground State Comparison with QE(100 Ha energy cut off):
    a) Energy Difference = 1.284E-05 Ha/atom
    b) Force Difference  = 2.712E-04 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 5.827E-06 Ha/bohr**3 (Hydrostatic Stress error)

Study2---Combined ionic and cell relaxation results
------------------------
* Relaxed State Comparison with QE(50 Ha and koint rule 4x4x4)and DFT-FE(poly 6 mesh 0.9 and kpoint rule 4x4x4, , scf tolerance 5e-5):  
    a) Energy Difference = 1.31E-05 Ha/atom  
    b) Force Difference = 4.05E-04 Ha/bohr (max absolute error among all atoms and force components)  
    c) Stress Difference = 1.0473E-06 Ha/bohr**3 (maximum error in any component of stress tensor)  
* Relaxed Vectors:
    *  Quantum Espresso:
    
      19.903699232	 0.0000000	0.0000000   
      0.0000000	         19.903699232	0.0000000   
      0.0000000	         0.0000000	19.903699232
    *  DFT-FE:

      1.990369923161320642e+01   -1.105948615815581056e-19  1.289979235970946107e-21
      -2.581618102749298907e-20  1.990369923161321353e+01   -4.655978766434789362e-20
      4.422871699991971504e-21   3.152792601212958235e-20   1.990369923161321353e+01

