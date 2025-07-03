Description of the example
==========================
This example demonstrates the inputs required for hubbard correction. This is an example for a non-periodic spin polarized calculation where all the atoms have hubbard corrections. 
 
Studies performed
=======================

Ground-state calculation: convergence study of ground-state energy and ionic forces to reach chemical accuracy with respect to FE discretization, and validation against QUANTUM ESPRESSO (QE).  (Study1)

Ionic relaxation: Relaxation of the atomic positions with spin polarization. (Study2)

Discussion on the input parameters and the results
==================================================
* DFT-FE:

        a) EXCHANGE CORRELATION TYPE   = GGA-PBE+U
        b) HUBBARD PARAMETERS FILE     = hubbard.inp  

    hubbard.inp - This file contains the input parameters used for hubbard corrections. The structure of the file is as follows. 
   3 - Number of hubbard speices. This number specifies the number of different species of hubbard atoms are present in the calculation. In this particular case, both Pt and Ni atoms have hubbard corrections. However, the hubbard Id 0 is specifically assinged to atoms with no hubbard correction. Hence the number of hubbard species is set to 3. 
   0 0 - The hubbard id and the number of orbitals on which the corrections are applied. For hubbard Id 0, the hubbard corrections are not applied for any orbitals. 
   1 28 0.0367492929 1 8.0 - The hubbard id 1 is set to atomic number 28 with a U value of 0.0367492929 Ha (1.0 eV). These corrections are applied on 1 set of orbitals. 8.0 is the initial occupancy on the set of orbitals.
   3 2 - This specifies the orbitals (n and l quantum number) on which the corrections will be applied.
   2 78 0.1102478786 1 9.0 - The hubbard id 2 is set to atomic number 78 with a U value of 0.1102478786 Ha (3.0 eV). These
corrections are applied on 1 set of orbitals. 9.0 is the initial occupancy on the set of orbitals. 
   5 d - This specifies the orbitals (n and l quantum number) on which the corrections will be applied.
   These are followed by the list of atoms  ( copied from the coordinates file)and the correspinding hubbard species id. 
   28 1 - Atomic number (28) and hubbard species id (1).
   78 2 - Atomic number (78) and hubbard species id (2). 
   78 2 - Atomic number (78) and hubbard species id (2).
   78 2 - Atomic number (78) and hubbard species id (2).
   
* QE:  
        a) U Pt-5d 3.0              = Hubbard correction applied to 5 d orbitals of Pt with U = 3.0 eV
        b) U Ni-3d 1.0              = Hubbard correction applied to 3 d orbitals of Ni with U = 1.0 eV                                   
Ground-state calculation results (Study 1)
--------------------------------

* Ground State Comparison with QE(90 Ha energy cut off):
    a) Energy Difference =  1.76E-05 Ha/atom
    b) Force Difference =  3.89E-05 Ha/bohr (max absolute error among all atoms and force components)

Ionic relaxation results (Study 2)
--------------------------------

* Ionic relaxation converged in 6 iterations. 

* Comparison in with QE (60 Ha energy cut off) : The atomic positions differ by 1.74E-04 Bohrs. The energy of the final relaxed structure differed by 4.02E-06 Ha/atom.
