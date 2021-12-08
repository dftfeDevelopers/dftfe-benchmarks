#!/bin/bash
#SBATCH --job-name WS2
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=36
#SBATCH --mem-per-cpu=5g
#SBATCH --time=100:00:00
#SBATCH --account=vikramg1
#SBATCH --mail-user=dsambit@umich.edu
#SBATCH --mail-type=BEGIN,END

export OMP_NUM_THREADS=1
mpirun -n 144 /scratch/vikramg_root/vikramg/dsambit/buildTest/release/real/dftfe parameterFile.prm > outputFeorder7Mesh1p6Atomballradius6p0Relaxation
