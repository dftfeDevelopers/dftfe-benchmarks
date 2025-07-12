Description of the example
==========================
This example demonstrates a Nudged Elastic Band Lithium Oxide 2x2x2 supercell with 1 Li vacancy employing periodic boundary conditions in all directions. ONCV pseudopotentials from pseudodojo database, PBE exchange correlation and Fermi-Dirac smearing temperature of 500 K are used. 

Studies performed
=======================
* Nudged Elastic Band(NEB) calculation of Li tetrahedral-tetrhedral vacancy hoping. 


Discussion on the input parameters and the results:
==================================================
* DFT-FE:
        a) Polynomial Order      = 7
        b) MESH SIZE AROUND ATOM  = 1.2
        c) ATOM BALL RADIUS         = 10.0
        d) SCF Tolerance            =1E-7
        e) Mixing Method            = Anderson
        f) MIXING PARAMETER          =0.2
        g) High QUAD PSP ON
        Activation Energy       = 241.03 meV      
        Li-ion path length traversed             = 3.572 bohr

        
* QE:  
        a) ecutwfc                  = 37.5 Ha                                    
        Activation Energy       = 244.923 meV      
        Li-ion path length traversed             = 3.57 bohr
        Total Path Length                         = 4.076 bohr      

Study -- Nudged Elastic Band results (Spin-unpolarized)
------------------------------------------------------------
* Activation Barrier comparison:
    a) Energy Difference = 3.89 meV
    b) Path Length error% = 0.97 %



