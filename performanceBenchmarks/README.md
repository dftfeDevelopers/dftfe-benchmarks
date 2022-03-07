This directory contains performance benchmarks using the DFT-FE code on various medium and large-scale benchmark systems. The performance of the benchmark systems will be tracked as the architectures evolve (upcoming exascale machines) and future methodology and implementation enhancements in DFT-FE while maintaining the same accuracy. Additional performance benchmarks will also be added in the future as new capabilites are added into DFT-FE for example hybrid exchange-correlation functionals, time-dependent DFT, enriched finite-elements for large-scale all-electron calculations etc. The input and output files for all performance benchmarks are provided in the corresponding folders. The file structure from the top-down follows the following order  DFT-FE version-> Architecture -> Type of electronic-stucture calculation -> Nature of performance benchmarks -> different material systems. 

Ground-state DFT performance for pseudopotential DFT calulations using DFT-FE v1.0
==================================================================================
All benchmark calculations are run using ONCV pseudopotentials and finite-element discretization parameters are commensurate with chemical accuracy (~1e-4 Ha/atom in ground-state energy, ~1e-4 Ha/Bohr in ionic forces and ~5e-6 Ha/Bohr^3 in cell stresses).

* **Architectures used for the benchmarks**

i. Summit: 6 NVIDIA V100 GPUs and 2 IBM POWER9 CPUs (42 cores total) per node
  

* **Computational cost benchmarks**

Phani: create table with following columns: (system and benchmark relative folder path, architecture and resources used (number of nodes), total wall time, average per scf wall-time, CPU-GPU speedup)

we will use different rows for different architectures

* **Strong parallel scaling**


* **Minimum wall-time**
