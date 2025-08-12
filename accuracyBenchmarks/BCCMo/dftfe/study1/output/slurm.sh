#!/bin/bash
#SBATCH --job-name Al147
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=48
#SBATCH --mem-per-cpu=5g
#SBATCH --time=72:00:00

mpirun -np 48 /home/nishantg/DFT/build/release/real/dftfe parameterFileCPU.prm>outputCPUFEOrder7Mesh2d0Ball0d0_nodes1_cpus48_gammaPt
