Description of the example
==========================
This example demonstrates the inputs required for hubbard correction. This is an example of a periodic gamma-point calculation where some of the atoms have hubbard corrections.
 
Studies performed
=======================

Ground-state calculation: convergence study of ground-state energy, ionic forces and cell stresses to reach chemical accuracy with respect to FE discretization, and validation against QUANTUM ESPRESSO (QE). (Study1)

ION CELL relaxation: relaxation of the atomic positions and cell parameters while maintaining the cell shape is performed and compared against QUANTUM ESPRESSO (QE). (Study2) 

Discussion on the input parameters and the results
==================================================
* DFT-FE:

        a) EXCHANGE CORRELATION TYPE   = GGA-PBE+U
        b) HUBBARD PARAMETERS FILE     = hubbard.inp  

    hubbard.inp - This file contains the input parameters used for hubbard corrections. The structure of the file is as follows. 
   2 - Number of hubbard speices. This number specifies the number of different species of hubbard atoms are present in the calculation. 
   0 0 - The hubbard id and the number of orbitals on which the corrections are applied. For hubbard Id 0, the hubbard corrections are not applied for any orbitals. 
   1 22 0.1837464643 1 2.0 - The hubbard id 1 is set to atomic number 22 with a U value of 0.1837464643 Ha (5.0 eV). These corrections are applied on 1 set of orbitals. 2.0 is the initial occupancy on the set of orbitals.
   3 2 - This specifies the orbitals (n and l quantum number) on which the corrections will be applied.
   These are followed by the list of atoms  ( copied from the coordinates file)and the correspinding hubbard species id. 
   13 0 - Atomic number (13) and hubbard species id (0).
   22 1 - Atomic number (22) and hubbard species id (1). 
   
* QE:  
        a) ecutwfc                  = 80 Ha 
        b) U Ti-3d 5.0              = Hubbard correction applied to 3 d orbitals of Ti with U = 5.0 eV

Ground-state calculation results (Study1)
--------------------------------

* Ground State Comparison with QE(80 Ha energy cut off):
    a) Energy Difference = 2.134E-05 Ha/atom
    b) Force Difference = 1.88E-06 Ha/bohr (max absolute error among all atoms and force components)
    c) Stress Difference = 2.30707E-07 Ha/bohr**3 (Hydrodynamic Stress error)


Ion and Cell relaxation results (Study 2)
--------------------------------

Comparison with QE (80 Ha energy cut off):

* Atomic positions differed by 1E-03 in fractional coordinates. 

* Lattice parameter differed by 4.5E-04 Bohrs. 

* The energy of the relaxaed structure differed by 1.84 E-05 Ha/atom. 
 
