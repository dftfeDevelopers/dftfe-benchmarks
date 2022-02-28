Description of the example
==========================
This example demonstrates a ground-state calculation, ionic relaxation, cell relaxation on Lithium Lanthanum Zirconate unit-cell employing periodic boundary conditions in all directions. ONCV pseudopotentials from pseudodojo database, PBE exchange correlation and Fermi-Dirac smearing temperature of 500 K are used. 

Studies to be performed
=======================
* Ground-state calculation: Spin-unpolarized calculation with convergence study of ground-state energy, ionic forces and cell stresses with respect to FE discretization to reach chemical accuracy (see examples 1 and 2). Validation with Quantum espresso refined calculation.
* Ground-state calculation: Spin-polarized ground-state calculation using mesh parameters obtained in the above study and validate the ground-state energy, forces and stresses with Quantum espresso.
* Ionic relexation and cell relaxation for both spin-unpolarized and spin-polarized calculation and validation with Quantum espresso.


Discussion on the input parameters and the results:
==================================================
* DFT-FE:
        a) Starting Magnetization = 0.08
        b) Polynomial Order      = 7
        c) MESH SIZE AROUND ATOM  = 1.2
        d) ATOM BALL RADIUS         = 4.0
        e) SCF Tolerance            =1E-5
        f) Mixing Method            = Anderson
        g) MIXING PARAMETER          =0.2
        g) No. of degree of freedom = 2803221
        
* QE:  
        a) Starting Magnetization:
                                        starting_magnetization(Li)= 0.33,
                                        starting_magnetization(O)= 0.1667,
                                        starting_magnetization(La)= 0.09,
                                        starting_magnetization(Zr)=0.1667 
        b) ecutwfc                  = 100 Ha                                    
        


Study1 -- Ground-state calculation results (Spin-unpolarized)
------------------------------------------------------------



Study2 -- Ground-state calculation results (Spin-polarized)
------------------------------------------------------------
* GPU CPU Comparison:
    a) Energy Difference = 1.62E-8 Ha/atom
    b) Force Difference = 1.6E-7 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 1.31E-7 Ha/bohr**3 (Hydrodynamic Stress error)
    d) No. of scf iterations 25(CPU) & 25(GPU)

* Ground State Comparison with QE(100 Ha energy cut off):
    a) Energy Difference = 2.80E-06 Ha/atom
    b) Force Difference = 6.79E-05 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 2.62E-06 Ha/bohr**3 (Hydrodynamic Stress error)
    d) No. of scf iterations 25(DFT-FE) & 13(QE)

Study3 -- Geometric relaxation results (Spin-unpolarized)
------------------------------------------------------------


Study4 -- Geometric relaxation results (Spin-polarized)
------------------------------------------------------------
* Relaxed State Comparison with QE(42.5 Ha ecut):  
    a) Energy Difference = 1.06E-05 Ha/atom  
    b) Force Difference = 2.55E-04 Ha/bohr (max absolute error among all atoms and force components)  
    c) Stress Difference = 4.82E-06 Ha/bohr**3 (Hydrodynamic Stress error)  
* Relaxed Vectors:
    *  Quantum Espresso:  
                         24.9176176	0.0000000	0.0000000   
                         0.0000000	24.9191797	0.0000000   
                         0.0000000	0.0000000	23.8884463   
    *  DFT-FE:  
                        24.9150902	0.0000000	0.0000000     
                        0.0000000	24.9151757	0.0000000     
                        0.0000000	0.0000000	23.8931448     
    *  Max Error is 0.01966 %                     
                    

    
