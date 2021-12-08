#!/bin/bash
#SBATCH --job-name mo4x
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=36
#SBATCH --mem-per-cpu=5g
#SBATCH --time=2:00:00
#SBATCH --account=vikramg1
#SBATCH --mail-user=dsambit@umich.edu
#SBATCH --mail-type=BEGIN,END

export OMP_NUM_THREADS=1
mpirun -n 72 /scratch/vikramg_root/vikramg/dsambit/buildnew/release/real/dftfe parameterFileCPU.prm > outputFEOrder7Meshsize2p0
