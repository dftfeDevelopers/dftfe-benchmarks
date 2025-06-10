Description of the example
============================================================================
This example illustrates the bandstructure calculation for a 2×2×2 supercell (16 atoms) of a Si crystal with periodic boundary conditions. The computations employ ONCV pseudopotentials obtained from SG15 database and r<sup>2</sup>SCAN as the exchange-correlation functional.

Studies performed
============================================================================
* Ground state convergence study (with monovacancy to ensure significant forces for force convergence study) is performed to obtain optimum ecutwfc, ecutrho and k-point mesh in QE such that the error in free energy, and maximum absolute error in any force component remain below  1e<sup>-4</sup> Ha/atom and 2e<sup>-4</sup> Ha/Bohr, respectively. 
* Optimum mesh parameters are obtained in DFT-FE, such that the error in free energy, and maximum force component are below  1e<sup>-4</sup> Ha/atom and 2e<sup>-4</sup> Ha/Bohr, respectively, with respect to the most refined QE calculation. The k-point mesh used in this step corresponds to the optimal k-point mesh previously obtained from QE.
* The complete ground-state calculations are carried out in both QE and DFT-FE (with the full crystal without vacancy) using the optimum parameters. Subsequently, the band structure is obtained using the converged electron density and kinetic energy density from the previous ground state calculation.
* The bandstructure plot in DFT-FE is obtained using PyProcar. (For more details refer [FeCuPt2Postprocess](https://github.com/dftfeDevelopers/dftfe-benchmarks/tree/master/accuracyBenchmarks/FeCuPt2Postprocess).)

Results
============================================================================
* The optimum parameters obtained from the convergence study are listed below,

    * QE: ecutwfc = 40 Ry ,ecutrho = 160 Ry, k-point mesh = 8x8x8
    * DFT-FE: POYNOMIAL ORDER = 5, MESH SIZE AROUND ATOM = 1.4 Bohr, ATOM BALL RADIUS = 6 Bohr (compiled with "withHigherQuadPSP = ON")

* The band structures obtained from QE and DFT-FE show good agreement when using the r<sup>2</sup>SCAN exchange-correlation functional.