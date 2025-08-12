Description of the example
============================================================================
This example demonstrates the ion relaxation with periodic boundary conditions for a 2x2x2 supercell of Li<sub>2</sub>O (FCC) crystal (with an Oxygen atom vacancy) that consists of 95 atoms. ONCV pseudopotentials from SG15 database along with r<sup>2</sup>SCAN exchange-correlation functional are used for the calculations.


Studies performed
============================================================================
* Ground state convergence study is performed to determine the optimal ecutwfc, ecutrho and k-point mesh in QE ensuring that the errors in free energy ,and maximum force component are below  1e<sup>-4</sup> Ha/atom and 1e<sup>-4</sup> Ha/Bohr, respectively. 
* Optimum mesh parameters are obtained in DFT-FE, such that the errors in free energy, and maximum force component are below  1e<sup>-4</sup> Ha/atom and 1e<sup>-4</sup> Ha/Bohr with respect to the most accurate QE calculation. The k-point mesh from the QE convergence study is used in this step. 
* Ion relaxation are performed on both QE and DFT-FE such that the maximum force component is less than 1e<sup>-4</sup> Ha/Bohr.

Results
============================================================================
* The optimal parameters obtained from the ground state convergence study are listed below

    * QE: ecutwfc = 100 Ry ,ecutrho = 400 Ry, k-point mesh = 2x2x2
    * DFT-FE: POYNOMIAL ORDER = 7, MESH SIZE AROUND ATOM = 1.2 Bohr, ATOM BALL RADIUS = 6 Bohr (compiled with withHigherQuadPSP = ON)

* For the relaxed structure, between QE and DFT-FE, (a) energy difference = 7.5E-06 Ha/atom, (b) Maximum absolute force component difference = 3.8E-05 Ha/Bohr 