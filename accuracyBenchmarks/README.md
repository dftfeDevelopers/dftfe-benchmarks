This directory contains examples, which are designed to cover most of the capabilities of the DFT-FE code. Please refer to the README file inside each example directory for more detailed information regarding the example, the associated accuracy studies, and any important notes for the user to setup similar or related calculations using DFT-FE.

General guidelines on Finite-element discretization input parameters
============================================================================
We refer to DFT-FE manual (provide link) for full input parameters list, their associated description, and the precedure to setup the input file. The manual also provides more in-depth discussion on the usage of the key input parameters in DFT-FE. Below, we briefly discuss the Finite-element (FE) discretization related input parameters which will be repeatedly used in all the examples. Other input parameters specific to the example are discussed inside the associated example subfolder.

The three important FE discretization related parameters in DFT-FE, which the user needs to set are the POLYNOMIAL ORDER, MESH SIZE AROUND ATOM, and ATOM BALL RADIUS.

* First, the POLYNOMIAL ORDER sets the order of the piecewise continuous FE interpolating polynomial, with higher values affording faster convergence rates with respect to discretization. Based on our numerical investigations, we recommend POLYNOMIAL ORDER=7 for soft pseudopotentials (<20 Ha plane-wave cutoff), POLYNOMIAL ORDER=6 for medium/hard pseudpotentials, and POLYNOMIAL ORDER=5 for all-electron calculations to be most computationally efficient choices on both CPUs and GPUs.

* The second input parameter is the MESH SIZE AROUND ATOM, which sets the size (in Bohr units) of the FE mesh element around the atoms, with the mesh sizes away from the atoms and the intervening mesh adaptivity heuristically set inside the code depending on the domain boundary conditions. **The MESH SIZE AROUND ATOM is the most important parameter for the user to control in pseudopotential DFT calculations**. This parameter is inversely related to the plane-wave cutoff in plane-wave based DFT codes. The smaller the mesh size the lower the discretization related errors. Based on our numerical validation studies as will be demonstrated in many of the examples, we obtain chemical accuracy (~1e-4 Ha/atom in energy, ~1e-4 Ha/Bohr in ionic forces and ~5e-6 Ha/Bohr^3 in cell stresses) for soft pseudopotentials using following choice of discretization parameters (POLYNOMIAL ORDER=7, MESH SIZE AROUND ATOM=1.7---2.3), and (POLYNOMIAL ORDER=6, MESH SIZE AROUND ATOM=0.9---1.4) for medium/hard pseudopotentials. We advice the users to use the above recommendations as starting choices only and always check the convergence of their quantity of interest with respect to the above discretization parameters.

* The third input parameter is the ATOM BALL RADIUS, which denotes the Radius of ball enclosing every atom, inside which the mesh size is set close to MESH SIZE AROUND ATOM and coarse-grained in the region outside the enclosing balls. For the default value of 0.0, a heuristically determined value is used, which is good enough for most cases but can be a bit conservative choice for fully non-periodic and semi-periodic problems as well as all-electron problems. To improve the computational efficiency user may experiment with values of ATOM BALL RADIUS ranging between 3.0 to 6.0, and ranging between 1.0 to 2.5 for all-electron problems.


List and brief description of the examples
==========================================
Examples 2, 7, 8 and 9 are not yet set up.

* **example1** 

This example demonstrates a ground-state calculation with fully periodic boundary conditions on BCC Mo supercell with a mono-vacancy. Norm-conserving pseudopotential and PBE exchange correlation are used.

* **example2** 

This example demonstrates a ground-state calculation with non-periodic boundary conditions on Al nanoparticle. Norm-conserving pseudopotential and PBE exchange correlation are used.

* **example3** (To be done by Bikash, also test on Greatlakes GPU nodes)

This example demonstrates an all-electron ground-state calculation with non-periodic boundary conditions and ionic relaxation on Benzamide. PBE exchange correlation is used.

* **example4** (To be done by Nelson)

This example demonstrates an all-electron ground-state calculation with fully periodic boundary conditions and cell relaxation on GaAs cubic diamond unit cell. Multiple k-points for sampling the Brillouin zone, and PBE exchange correlation are used.

* **example5** (To be done by Phani and Phani's group, also test on GPU nodes in Phani's group for Gamma point case)

This example demonstrates a ground-state calculation with fully periodic boundary conditions and combined ionic-cell relaxation on Al12Mg17 intermetallic. Multiple k-points for sampling the Brillouin zone, norm-conserving pseudopotential, and PBE exchange correlation are used.

* **example6** (To be done by Bikash)

This example demonstrates a ground-state calculation with semi-periodic boundary conditions and ionic relaxation on water molecule over InP slab. Multiple k-points for sampling the Brillouin zone along the periodic directions, norm-conserving pseudopotential and PBE exchange correlation are used.

* **example7** (To be done by Ian, also test on Greatlakes GPU nodes)

DNA molecule with 8 base pairs

* **example8** (To be done by Sambit)

Bilayer of WS2

* **example9** (To be done by Sambit and Phani's group)

Lithium lanthanum Zirconate
