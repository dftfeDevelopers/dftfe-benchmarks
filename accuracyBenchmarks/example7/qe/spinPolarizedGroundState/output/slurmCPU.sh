#!/bin/bash
#SBATCH --job-name qe
#SBATCH --nodes=3
#SBATCH --ntasks-per-node=36
#SBATCH --mem-per-cpu=5g
#SBATCH --time=10:00:00
#SBATCH --account=vikramg1
#SBATCH --mail-user=dsambit@umich.edu
#SBATCH --mail-type=BEGIN,END

export OMP_NUM_THREADS=2
mpirun -n 108 pw.x -npool 1 -input WS2Ecut50.scf.in > WS2Ecut50.scf.out
