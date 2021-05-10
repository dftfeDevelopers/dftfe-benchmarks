This directory contains examples, which are designed to cover most of the capabilities of the DFT-FE code. Please refer to the README file inside each example directory for more detailed information regarding the example, the associated accuracy studies, and any important notes for the user to setup similar or related calculations using DFT-FE.

General guidelines on Finite-element discretization input parameters
============================================================================
We refer to DFT-FE manual (provide link) for full input parameters list, their associated description, and the precedure to setup the input file. The manual also provides more in-depth discussion on the usage of the key input parameters in DFT-FE. Below, we briefly discuss the key Finite-element (FE) discretization related input parameters which will be repeatedly used in all the examples. Other input parameters specific to the example are discussed inside the associated example subfolder.

The two key FE discretization related parameters in DFT-FE are the POLYNOMIAL ORDER and the MESH SIZE AROUND ATOM. The POLYNOMIAL ORDER, which sets the order of the FE interpolating polynomial, is set to a very high value of 7 which affords computational efficiency. As a thumb-rule based on our numerical investigations, we recommend POLYNOMIAL ORDER=7 for soft pseudopotentials (<20 Ha plane-wave cutoff), POLYNOMIAL ORDER=6 for medium/hard pseudpotentials, and POLYNOMIAL ORDER=5 for all-electron calculations. The most important parameter for the user to control for pseudopotential calculations is the MESH SIZE AROUND ATOM, which sets the size of the FE mesh element around the atoms. This parameter is inversely related to the plane-wave cutoff in plane-wave based DFT codes. The smaller the mesh size the lower the discretization related errors. Based on our numerical validation studies as will be demonstrated in many of the examples, we obtain chemical accuracy (~1e-4 Ha/atom in energy, ~1e-4 Ha/Bohr in ionic forces and ~5e-6 Ha/Bohr^3 in cell stresses) for soft pseudopotentials using following choice of discretization parameters (POLYNOMIAL ORDER=7, MESH SIZE AROUND ATOM=1.7---2.3), and (POLYNOMIAL ORDER=6, MESH SIZE AROUND ATOM=0.9---1.4) for medium/hard pseudopotentials. We advice the users to use the above as starting choices only and always check the convergence of their quantity of interest with respect to the above discretization parameters.


List and brief description of the examples
==========================================

* **example1** 

This example demonstrates a ground-state calculation with fully periodic boundary conditions on BCC Mo supercell with a mono-vacancy. Norm-conserving pseudopotential and GGA exchange correlation are used.

* **example2** 

This example demonstrates a ground-state calculation with non-periodic boundary conditions on Al nanoparticle. Norm-conserving pseudopotential and GGA exchange correlation are used.

* **example3** (To be done by Bikash)

This example demonstrates an all-electron ground-state calculation with non-periodic boundary conditions and ionic relaxation on Benzamide. GGA exchange correlation is used.

* **example4** (To be done by Nelson)

This example demonstrates an all-electron ground-state calculation with fully periodic boundary conditions and cell relaxation on GaAs cubic diamond unit cell. Multiple k-points for sampling the Brillouin zone, and GGA exchange correlation are used.

* **example5** (To be done by Phani and Phani's group)

This example demonstrates a ground-state calculation with fully periodic boundary conditions and combined ionic-cell relaxation on Al12Mg17 intermetallic. Multiple k-points for sampling the Brillouin zone, norm-conserving pseudopotential, and GGA exchange correlation are used.

* **example6** (To be done by Bikash)

This example demonstrates a ground-state calculation with semi-periodic boundary conditions and ionic relaxation on InP-water layer. Multiple k-points for sampling the Brillouin zone along the periodic directions, norm-conserving pseudopotential and GGA exchange correlation are used.

* **example7** (To be done by Ian)

DNA molecule with 8 base pairs

* **example8** (To be done by Sambit)

Bilayer of WS2

* **example9** (To be done by Sambit and Phani's group)

Lithium lanthanum Zirconate
