Description of the example
==========================
This example demonstrates a ground-state calculation, ionic relaxation, cell relaxation on Lithium Lanthanum Zirconate unit-cell employing periodic boundary conditions in all directions. ONCV pseudopotentials from pseudodojo database, PBE exchange correlation and Fermi-Dirac smearing temperature of 500 K are used. 

Studies performed
=======================
* Ground-state calculation: Spin-unpolarized calculation with convergence study of ground-state energy, ionic forces and cell stresses with respect to FE discretization to reach chemical accuracy (see examples 1 and 2). Validation with Quantum espresso refined calculation.
* Ground-state calculation: Spin-polarized ground-state calculation using mesh parameters obtained in the above study and validate the ground-state energy, forces and stresses with Quantum espresso.
* Ionic relexation and cell relaxation for both spin-unpolarized and spin-polarized calculation and validation with Quantum espresso.


Discussion on the input parameters and the results:
==================================================
* DFT-FE:
        a) POLYNOMIAL ORDER      = 5
        b) MESH SIZE AROUND ATOM  = 0.8
        c) ATOM BALL RADIUS         = 6.0
        d) TOLERANCE            =1E-5
        e) MIXING METHOD            = Anderson
        f) MIXING PARAMETER          =0.2
        g) ION OPT =true (for ionic forces relaxation)
        h) CELL OPT=true (for cell stress relaxation)
        i) CELL CONSTRAINT TYPE=9 (cell relax along domain vector components v1x, v2y and v3z)
        
* QE:  
        a) ecutwfc                  = 42.5 Ha                                    
* Both DFT-FE and QE:
        a) Starting Magnetization (for spin-polarized calculations):
                                        starting_magnetization(Li)= 0.33,
                                        starting_magnetization(O)= 0.1667,
                                        starting_magnetization(La)= 0.09,
                                        starting_magnetization(Zr)=0.1667
          In DFT-FE starting magnetization is set using the last column in 
          the coordinates file
        


Study1 -- Ground-state calculation results (Spin-unpolarized)
------------------------------------------------------------
* Ground State Comparison with QE(42.5 Ha energy cut off):
    a) Energy Difference = 2.2e-5  Ha/atom
    b) Force Difference = 9.1e-5   Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 2.8e-6 Ha/bohr**3 (Hydrodynamic Stress error)


Study2 -- Ground-state calculation results (Spin-polarized)
------------------------------------------------------------
* GPU CPU Comparison (both DFT-FE):
    a) Energy Difference =6.4e-10  Ha/atom
    b) Force Difference =7.4e-7  Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference =7.9e-8  Ha/bohr**3 (Hydrodynamic Stress error)
    d) No. of scf iterations 24(CPU) & 24(GPU)

* Ground State Comparison with QE(100 Ha energy cut off):
    a) Energy Difference =1.9e-5  Ha/atom
    b) Force Difference =6.4e-5 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference =1.4e-6  Ha/bohr**3 (Hydrodynamic Stress error)

Study3 -- Geometric relaxation results (Spin-unpolarized)
------------------------------------------------------------
* Relaxed State Comparison with QE(42.5 Ha ecut):  
    a) Energy Difference =2.3e-5  Ha/atom  
* Relaxed lattice Vectors:
    *  Quantum Espresso:  
                         24.9176 0.00000 0.00000   
                         0.00000 24.9192 0.00000   
                         0.00000 0.00000 23.8885  
    *  DFT-FE: 
                        24.916590	0.00000	0.00000     
                        0.00000 24.916604 0.00000     
                        0.00000	0.00000	23.902025    

Study4 -- Geometric relaxation results (Spin-polarized)
------------------------------------------------------------
* Relaxed State Comparison with QE(42.5 Ha ecut):  
    a) Energy Difference = 2.3E-05 Ha/atom  
* Relaxed lattice Vectors:
    *  Quantum Espresso:  
                         24.9176176	0.0000000	0.0000000   
                         0.0000000	24.9191797	0.0000000   
                         0.0000000	0.0000000	23.8884463   
    *  DFT-FE: 
                        24.911261	0.0000000	0.0000000     
                        0.0000000	24.911237	0.0000000     
                        0.0000000	0.0000000	23.907110     
